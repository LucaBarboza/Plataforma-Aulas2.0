import sys
import os
import json
import time
from google import genai
from google.genai import types
from schemas import DiretrizesProfessorMapeadas
from gerador_conteudo import carregar_chave_api

def processar_arquivo_diretrizes_ia(arquivos_info) -> dict:
    """
    Envia o(s) arquivo(s) de diretrizes e/ou materiais de apoio do professor para o Gemini para mapear
    as preferências nos campos de notação matemática e design de estilo usando Structured Outputs.
    'arquivos_info' pode ser uma tupla (caminho_arquivo, nome_original) ou uma lista de tuplas.
    """
    # Garante a carga da chave de API
    carregar_chave_api()
    if not os.environ.get("GEMINI_API_KEY"):
        raise ValueError("Chave de API 'GEMINI_API_KEY' não configurada no ambiente ou secrets.")

    client = genai.Client(http_options={"timeout": 120_000})
    
    # Normaliza a entrada para uma lista de tuplas (caminho, nome)
    if isinstance(arquivos_info, tuple) and len(arquivos_info) == 2:
        lista_arquivos = [arquivos_info]
    elif isinstance(arquivos_info, list):
        lista_arquivos = arquivos_info
    else:
        raise ValueError("Formato de entrada de arquivos inválido para o analisador de diretrizes.")

    prompt = """
    Você é um Engenheiro Pedagógico e Assistente Especialista de IA para análise de diretrizes e materiais acadêmicos.
    Sua tarefa é analisar o(s) documento(s), notas de aula, slides ou arquivos de preferências do professor fornecidos e categorizar as preferências nos campos correspondentes do schema 'DiretrizesProfessorMapeadas'.
    
    INSTRUÇÕES DE PREENCHIMENTO:
    1. Preencha apenas os campos que forem explicitamente mencionados ou que puderem ser claramente deduzidos dos materiais e preferências do professor.
    2. Para notações matemáticas (como média populacional, hipótese nula, etc.), você deve retornar a notação exata em formato LaTeX (ex: $n$, $\\mu$, $\\bar{X}$, $H_0$). Certifique-se de que a barra invertida seja escapada corretamente para JSON.
    3. Se houver alguma outra notação específica que não se enquadre nos campos padrão, crie um item correspondente na lista 'notacoes_customizadas' com chaves 'conceito' e 'simbolo'.
    4. Se forem mencionadas cores preferidas para a identidade visual da plataforma, extraia-as em formato hex (ex: #1E3A8A) no dicionário 'cores_preferidas' (chaves válidas: 'cor_primaria', 'cor_secundaria', 'cor_alerta', 'cor_critica').
    5. No campo 'diretrizes_estilo_livre', consolide quaisquer outras diretrizes gerais sobre tom de escrita, foco de exemplos (ex: "focar em exemplos de ciências da saúde"), proibição de termos em inglês, convenções de notação, etc.
    6. Se o campo não for citado ou não puder ser extraído dos materiais, deixe-o como null (ou omitido).
    """

    contents = []
    uploaded_refs = []

    try:
        for caminho_arquivo, nome_original in lista_arquivos:
            extensao = os.path.splitext(nome_original.lower())[1]
            
            if extensao in [".pdf", ".png", ".jpg", ".jpeg", ".webp"]:
                print(f"[Analisador Diretrizes] Fazendo upload do arquivo ({extensao}) '{nome_original}' para o Gemini Cloud...")
                midia_ref = client.files.upload(file=caminho_arquivo)
                uploaded_refs.append(midia_ref.name)
                
                # Aguarda o arquivo atingir o estado ACTIVE na API
                while getattr(midia_ref.state, 'name', str(midia_ref.state)) == "PROCESSING":
                    time.sleep(1.5)
                    midia_ref = client.files.get(name=midia_ref.name)
                    
                contents.append(midia_ref)
            else:
                print(f"[Analisador Diretrizes] Lendo arquivo de texto local '{nome_original}'...")
                with open(caminho_arquivo, "r", encoding="utf-8", errors="ignore") as f:
                    conteudo_texto = f.read()
                contents.append(f"### CONTEÚDO DO MATERIAL DO PROFESSOR ({nome_original}):\n{conteudo_texto}\n\n")

        contents.append(prompt)

        print(f"[Analisador Diretrizes] Processando {len(lista_arquivos)} arquivo(s) com Gemini 3.1 Flash Lite...")
        resposta = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=contents,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=DiretrizesProfessorMapeadas,
                temperature=0.2
            )
        )

        dados_dicionario = json.loads(resposta.text)
        return dados_dicionario

    except Exception as e:
        print(f"[Analisador Diretrizes] Erro durante o processamento das diretrizes: {e}")
        raise e
    finally:
        # Limpa todos os arquivos enviados para o Gemini Cloud
        for ref_name in uploaded_refs:
            try:
                client.files.delete(name=ref_name)
            except Exception as e_del:
                print(f"[Analisador Diretrizes] Erro ao deletar arquivo temporário da nuvem ({ref_name}): {e_del}")
