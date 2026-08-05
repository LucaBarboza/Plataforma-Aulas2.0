import os
import sys
import time
import unicodedata
from google import genai
from google.genai import types

def print_safe(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    file = kwargs.get('file', sys.stdout)
    text = sep.join(str(arg) for arg in args) + end
    encoding = getattr(file, 'encoding', 'utf-8') or 'utf-8'
    try:
        file.write(text)
    except UnicodeEncodeError:
        safe_text = text.encode(encoding, errors='replace').decode(encoding)
        file.write(safe_text)
    file.flush()

print = print_safe

def remover_acentos(texto):
    nfkd_form = unicodedata.normalize('NFKD', texto)
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def inicializar_e_indexar(nome_professor: str, codigo_disciplina: str, pasta_livros: str):
    client = genai.Client(http_options={"timeout": 120_000})
    
    # Gerando o nome da Store (usa plataforma-estatistica-db se for 'global', caso contrário cria Store específica)
    if nome_professor.lower().strip() == "global":
        NOME_STORE = "plataforma-estatistica-db"
    else:
        NOME_STORE = f"store-{nome_professor.lower().strip()}-{codigo_disciplina.lower().strip()}"
    print(f"📦 Inicializando verificação para a Store: {NOME_STORE}")
    
    store_alvo = None
    try:
        for store in client.file_search_stores.list():
            if store.display_name == NOME_STORE:
                store_alvo = store
                print(f"✅ Store encontrada no servidor do Google: {store_alvo.name}")
                break
    except Exception as e:
        raise RuntimeError(f"Erro ao listar stores: {e}")
        
    if not store_alvo:
        print(f"⚠️ Store não existente. Criando nova store corporativa...")
        store_alvo = client.file_search_stores.create(
            config={
                'display_name': NOME_STORE
            }
        )
        print(f"🎉 Store criada com sucesso: {store_alvo.name}")

    # Mapeia arquivos já indexados na Store para evitar re-uploads desnecessários
    arquivos_ja_indexados = set()
    try:
        docs_existentes = list(client.file_search_stores.documents.list(parent=store_alvo.name))
        for doc in docs_existentes:
            if doc.custom_metadata:
                for meta in doc.custom_metadata:
                    if meta.key == 'filename' and meta.string_value:
                        arquivos_ja_indexados.add(meta.string_value.lower())
        if arquivos_ja_indexados:
            print(f"🔍 {len(arquivos_ja_indexados)} documento(s) já indexados na Store '{NOME_STORE}'.")
    except Exception as e_list:
        print(f"⚠️ Aviso ao listar documentos existentes na Store: {e_list}")

    if not os.path.exists(pasta_livros):
        print(f"Erro: A pasta local '{pasta_livros}' não existe.")
        return

    arquivos_locais = [f for f in os.listdir(pasta_livros) if f.endswith(".pdf")]
    if not arquivos_locais:
        print(f"ℹ️ Nenhum arquivo PDF para indexar na pasta '{pasta_livros}'.")
        return

    for arquivo in arquivos_locais:
        caminho_completo = os.path.join(pasta_livros, arquivo)
        
        # Remove acentos do nome do arquivo para evitar problemas de codificação no Windows
        arquivo_seguro = remover_acentos(arquivo)
        caminho_seguro = os.path.join(pasta_livros, arquivo_seguro)
        if caminho_completo != caminho_seguro:
            os.rename(caminho_completo, caminho_seguro)

        # Checa se o arquivo já consta da store
        if arquivo_seguro.lower() in arquivos_ja_indexados or arquivo.lower() in arquivos_ja_indexados:
            print(f"⚡ '{arquivo}' já está 100% indexado no RAG do Google. Pulando upload.")
            continue

        print(f"\n🚀 Enviando '{arquivo}' para processamento vetorial (RAG)...")
        
        # Tenta fazer o upload com até 3 tentativas para lidar com erros 503 transitórios da API
        for tentativa_upload in range(1, 4):
            try:
                # 1. Faz o upload temporário do arquivo usando Files API
                file_obj = client.files.upload(file=caminho_seguro)
                
                # Aguarda o estado do arquivo ficar ACTIVE se necessário
                while getattr(file_obj.state, 'name', str(file_obj.state)) == "PROCESSING":
                    time.sleep(2)
                    file_obj = client.files.get(name=file_obj.name)
                
                # 2. Importa o arquivo para a Store do RAG com os metadados customizados de disciplina e nome de arquivo
                operation = client.file_search_stores.import_file(
                    file_search_store_name=store_alvo.name,
                    file_name=file_obj.name,
                    config={
                        'customMetadata': [
                            {'key': 'discipline', 'stringValue': codigo_disciplina.upper().strip()},
                            {'key': 'filename', 'stringValue': arquivo_seguro}
                        ]
                    }
                )
                print(f"📤 Upload concluído. Operação iniciada: {operation.name}")
                
                # LOOP DE POLLING: Bloqueia o terminal local até o status da operação ser concluída no Google
                print("⏳ Aguardando indexação e geração de embeddings no servidor do Google RAG...")
                while not operation.done:
                    time.sleep(4)
                    operation = client.operations.get(operation)
                    print("   Processando e gerando embeddings...")
                    
                print(f"💪 Sucesso! '{arquivo}' está 100% pronto e indexado na store para buscas estatísticas.")
                arquivos_ja_indexados.add(arquivo_seguro.lower())
                break
            except Exception as e:
                print(f"⚠️ Tentativa {tentativa_upload}/3 falhou para '{arquivo}': {e}")
                if tentativa_upload < 3:
                    time.sleep(5)
                else:
                    print(f"❌ Não foi possível indexar o arquivo '{arquivo}' após 3 tentativas. Ignorando e prosseguindo...")
