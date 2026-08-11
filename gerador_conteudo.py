import os
import sys
import json
import re
import time

sys.setrecursionlimit(10000)
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

# Importando os schemas estruturados que criamos no arquivo anterior
from schemas import SubtopicoValidado, FonteRDetalhada
# Importamos a função do revisor local para auditoria
from revisor_notacao import auditar_subtopico_local

# ==============================================================================
# FALLBACK DE SEGURANÇA PARA A CHAVE DE API (GEMINI_API_KEY)
# ==============================================================================
def carregar_chave_api():
    """Garante a leitura da API key a partir do ambiente, do st.secrets (Streamlit Cloud) ou do secrets.toml local."""
    if "GEMINI_API_KEY" in os.environ and os.environ["GEMINI_API_KEY"].strip():
        return True
        
    # Tenta obter do st.secrets do Streamlit
    try:
        import streamlit as st
        if "GEMINI_API_KEY" in st.secrets:
            val = st.secrets["GEMINI_API_KEY"]
            if val and val.strip():
                os.environ["GEMINI_API_KEY"] = val.strip()
                return True
    except Exception:
        pass
        
    # Tenta ler do secrets.toml da pasta local
    path = os.path.join(".streamlit", "secrets.toml")
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                for linha in f:
                    if "GEMINI_API_KEY" in linha:
                        match = re.search(r'(?:GEMINI_API_KEY\s*=\s*["\'])(.*?)(?:["\'])', linha)
                        if match:
                            os.environ["GEMINI_API_KEY"] = match.group(1).strip()
                            print(f"[KEY] Chave de API carregada com sucesso a partir de '{path}'.")
                            return True
        except Exception as e:
            print(f"[ALERTA] Erro ao tentar ler {path}: {e}")
                
    return False

# Inicializa o carregamento da chave de API
carregar_chave_api()

def converter_subtopico_para_markdown(subtopico: SubtopicoValidado) -> str:
    conteudo = subtopico.conteudo
    md = []
    md.append(f"# {subtopico.titulo_subtopico}\n")
    
    if conteudo.conceito_intuitivo:
        md.append("## Conceito Intuitivo")
        md.append(conteudo.conceito_intuitivo.strip() + "\n")
        
    if conteudo.conceito_formal:
        md.append("## Conceito Formal")
        md.append(conteudo.conceito_formal.strip() + "\n")
        
    if conteudo.propriedades_do_conceito:
        md.append("## Propriedades do Conceito")
        for prop in conteudo.propriedades_do_conceito:
            md.append(f"- {prop.strip()}")
        md.append("")
        
    if conteudo.pre_requisitos_e_auxiliares:
        md.append("## Pré-requisitos e Auxiliares")
        for pre in conteudo.pre_requisitos_e_auxiliares:
            md.append(f"- {pre.strip()}")
        md.append("")
        
    if conteudo.condicoes_de_contorno:
        md.append("## Condições de Contorno")
        for cond in conteudo.condicoes_de_contorno:
            md.append(f"- {cond.strip()}")
        md.append("")
        
    if conteudo.deducao_formal_passo_a_passo:
        md.append("## Dedução Formal Passo a Passo")
        for passo in conteudo.deducao_formal_passo_a_passo:
            md.append(f"- {passo.strip()}")
        md.append("")
        
    if conteudo.interpretacao_geometrica_grafica:
        md.append("## Interpretação Geométrica / Gráfica")
        md.append(conteudo.interpretacao_geometrica_grafica.strip() + "\n")
        
    if conteudo.exemplo_canonico:
        ex = conteudo.exemplo_canonico
        md.append("## Exemplo Canônico")
        md.append(f"**Enunciado:**\n{ex.enunciado.strip()}\n")
        if ex.passo_a_passo_solucao:
            md.append("**Resolução Passo a Passo:**")
            for passo in ex.passo_a_passo_solucao:
                md.append(f"- {passo.strip()}")
            md.append("")
        md.append(f"**Resultado Final e Interpretação:**\n{ex.resultado_final.strip()}\n")
        
    if subtopico.fontes_rag:
        md.append("## Referências Bibliográficas (RAG)")
        for f in subtopico.fontes_rag:
            md.append(f"- **Livro/Autor:** {f.livro_autor} | **Capítulo:** {f.capitulo} | **Páginas:** {f.paginas_utilizadas}")
        md.append("")
        
    return "\n".join(md) + "\n"

# ==============================================================================
# SCHEMA AUXILIAR APENAS PARA O AGENTE 1 (ROTEIRISTA)
# ==============================================================================
class SubtopicoRoteiro(BaseModel):
    titulo: str = Field(description="Título curto e direto do sub-tópico conceitual.")
    conceitos_chave_rag: List[str] = Field(description="Lista de 3 a 5 termos estatísticos específicos e exatos para guiar a busca vetorial.")

class RoteiroCompletoAula(BaseModel):
    topico_principal: str
    esquema_paginas: List[SubtopicoRoteiro]

# ==============================================================================
# FUNÇÃO PRINCIPAL DE ORQUESTRAÇÃO DE CONTEÚDO
# ==============================================================================
def gerar_conteudo_aula(nome_professor: str, codigo_disciplina: str, tema_solicitado: str, ementa_pdf_path: str = None, diretrizes_texto: str = None, status_callback=None, memoria_pedagogica_acumulada: str = ""):
    t_inicio_roteirista = 0.0
    t_fim_roteirista = 0.0
    t_inicio_escrita = 0.0
    t_fim_escrita = 0.0
    log_subtopicos = []
    
    # Garante que temos a chave configurada
    if not os.environ.get("GEMINI_API_KEY"):
        raise ValueError("Chave de API 'GEMINI_API_KEY' não configurada. Configure a chave nos Secrets do Streamlit ou no ambiente.")

    try:
        client = genai.Client(http_options={"timeout": 300_000})
    except Exception as e:
        print(f"[ERRO] Erro ao inicializar o cliente do Google GenAI: {e}")
        return None
        
    # 1. Recupera as Stores do professor e de livros globais para busca híbrida simultânea
    NOME_STORE = f"store-{nome_professor.lower().strip()}-{codigo_disciplina.lower().strip()}"
    NOME_STORE_FALLBACK = "plataforma-estatistica-db"
    store_names = []
    
    try:
        # Faz uma busca por ambas as stores
        stores_disponiveis = list(client.file_search_stores.list())
        
        # 1. Tenta achar a store específica do professor
        for store in stores_disponiveis:
            if store.display_name == NOME_STORE:
                store_names.append(store.name)
                print(f"[RAG] RAG especifico do professor ativado! Usando a Store: {store.display_name}")
                
        # 2. Tenta achar a store global plataforma-estatistica-db que contem os livros
        for store in stores_disponiveis:
            if store.display_name == NOME_STORE_FALLBACK:
                store_names.append(store.name)
                print(f"[RAG] RAG global de livros ativado! Usando a Store: {store.display_name}")
    except Exception as e:
        print(f"[ALERTA] Alerta ao buscar stores no Google Cloud: {e}")
            
    tools_config = None
    if store_names:
        tools_config = [
            types.Tool(
                file_search=types.FileSearch(
                    file_search_store_names=store_names,
                    metadata_filter=f'discipline="{codigo_disciplina.upper().strip()}"',
                    top_k=45
                )
            )
        ]
    else:
        print(f"[AVISO] Nenhuma base de dados RAG ('{NOME_STORE}' ou '{NOME_STORE_FALLBACK}') foi encontrada. Continuando em modo sem RAG...")

    # 2. Carrega a ementa oficial como guia (fornecido obrigatoriamente via Streamlit)
    ementa_pdf = None
    if ementa_pdf_path:
        path_efetivo = ementa_pdf_path
        if not os.path.exists(path_efetivo):
            filename = os.path.basename(ementa_pdf_path)
            cand1 = os.path.join("Ementas", filename)
            cand2 = os.path.join("cache", filename)
            if os.path.exists(cand1):
                path_efetivo = cand1
            elif os.path.exists(cand2):
                path_efetivo = cand2

        if os.path.exists(path_efetivo):
            print(f"[EMENTA] Carregando ementa oficial '{path_efetivo}' para alinhamento de escopo...")
            try:
                ementa_pdf = client.files.upload(file=path_efetivo)
                while getattr(ementa_pdf.state, 'name', str(ementa_pdf.state)) == "PROCESSING":
                    time.sleep(2)
                    ementa_pdf = client.files.get(name=ementa_pdf.name)
            except Exception as e:
                print(f"[AVISO EMENTA] Falha ao enviar ementa para a API: {e}. Prosseguindo sem anexo...")
        else:
            print(f"[AVISO EMENTA] Arquivo de ementa '{ementa_pdf_path}' não encontrado. Prosseguindo com RAG e diretrizes...")

    # 3. Valida as diretrizes de notação e design enviadas pelo Streamlit
    if not diretrizes_texto or not diretrizes_texto.strip():
        raise ValueError("As diretrizes de notação e estilo são obrigatórias e devem ser fornecidas pelo Streamlit.")

    # ==============================================================================
    # FASE 1: AGENTE 1 - O ROTEIRISTA DA EMENTA
    # ==============================================================================
    t_inicio_roteirista = time.time()
    print("\n[Agente 1] Analisando a ementa e estruturando a trilha pedagógica da aula...")
    
    prompt_roteirista = f"""
Você é um Designer Instrucional Especialista em Ensino Superior de Matemática e Estatística, com foco em modelagem de currículos acadêmicos rigorosos.

### CONTEXTO E MISSÃO
Você receberá a [EMENTA] de uma disciplina universitária (anexada em PDF), as [DIRETRIZES_DO_PROFESSOR], a [MEMÓRIA_DE_AULAS_ANTERIORES] e um [TÓPICO_SOLICITADO] (um recorte extraído dessa ementa). 
Sua missão é atuar como um arquiteto de conteúdo: você deve quebrar o [TÓPICO_SOLICITADO] em uma sequência lógica, 
linear e exaustiva de subtópicos teóricos, preenchendo rigorosamente a estrutura 'RoteiroCompletoAula'.

---

### DIRETRIZES DE ESCOPO E COBERTURA (MANDATÓRIO)
1. Referência Flexível de Ementa e Âncora Temática: Use a [EMENTA] em PDF (se fornecida) como um guia conceitual de referência sobre o programa do curso. O [TÓPICO_SOLICITADO] é a âncora principal da aula, mas VOCÊ TEM LIBERDADE PEDAGÓGICA TOTAL para incluir tópicos adicionais, abordagens complementares ou expansões de conteúdo solicitadas pelo professor nas diretrizes, sem ficar travado exclusivamente ao PDF da ementa.
2. PRIORIDADE MÁXIMA E ABSOLUTA AOS MATERIAIS DE APOIO DO PROFESSOR (RAG): A divisão didática da aula, o formato da explicação, a ordenação dos conceitos, o tom de voz e o sequenciamento DEVEM espelhar e priorizar com peso máximo os Materiais de Apoio do Professor (slides, notas de aula, apostilas, provas) recuperados via RAG. Se o professor estrutura o assunto em um determinado formato ou divisão em seus slides, o roteiro deve obrigatoriamente espelhar e enriquecer essa exata divisão.
3. Granularidade Didática e Particionamento Exaustivo: Garanta que a aula seja dividida em subtópicos extremamente bem organizados, progressivos e encadeados. Fatie o assunto ao máximo em passos lógicos onde cada subtópico aborda um único foco conceitual denso, garantindo que o tema seja fatiado em partes detalhadas para que a aula final seja completa e didaticamente estruturada.
4. Formalismo Teórico Exclusivo: O foco deve ser a intuição conceitual, o formalismo matemático e as deduções analíticas. 
É TERMINANTEMENTE PROIBIDO incluir, sugerir ou criar componentes de programação, sintaxe de código ou laboratórios computacionais (como R, Python, SAS ou Julia).
5. Continuidade e Proibição de Repetição de Conteúdo: Examine minuciosamente a [MEMÓRIA_DE_AULAS_ANTERIORES]. Não redefina nem reintroduza conceitos, teoremas ou fórmulas primárias que já foram exaustivamente ensinados nas aulas anteriores. Prossiga a partir do ponto de parada exato registrado na memória.

---

### INSTRUÇÕES PARA PREENCHIMENTO DO SCHEMA DE RETORNO

1. 'topico_principal' (string): 
   - Nomeie o tema da aula de forma fluida, clara e contextualizada. 
   - Exemplo: "Fundamentos Teóricos e Aplicações da Regressão Linear Simples".

2. 'esquema_paginas' (lista de SubtopicoRoteiro):
   Cada item representa um subtópico que se tornará uma página teórica e deve conter:
   
   - 'titulo' (string): Título científico elegante, imersivo e de alta sonoridade acadêmica. Evite nomes curtos, genéricos ou informais.
     * Exemplo Ruim: "Introdução ao Teste t"
     * Exemplo Ideal: "A Engenharia Inferencial: Testes de Hipóteses e Distribuição t de Student"
     
   - 'conceitos_chave_rag' (lista de strings): Forneça de 3 a 5 palavras-chave cirúrgicas e termos técnicos exatos associados ao conceito (em português ou inglês). 
     * IMPORTANTE: Esses termos serão usados por um Agente Escritor para busca vetorial (RAG) nos materiais do professor e livros. Use jargões estatísticos precisos, notações ou nomes de teoremas/estimadores.

---

### ENTRADAS DO USUÁRIO
- [EMENTA]: O arquivo PDF em anexo contendo a ementa da disciplina
- [TÓPICO_SOLICITADO]: {tema_solicitado}
- [DIRETRIZES_DO_PROFESSOR]: {diretrizes_texto}
"""
    
    contents_roteirista = []
    if ementa_pdf:
        contents_roteirista.append(ementa_pdf)
    contents_roteirista.append(prompt_roteirista)

    tentativas_roteiro = 0
    roteiro_pedagogico = None
    while tentativas_roteiro < 10 and not roteiro_pedagogico:
        tentativas_roteiro += 1
        try:
            # Usando gemini-3.1-flash-lite com capacidade máxima de raciocínio profundo
            resposta_roteiro = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=contents_roteirista,
                config=types.GenerateContentConfig(
                    temperature=1.0,
                    thinking_config=types.ThinkingConfig(thinking_level="medium"),
                    response_mime_type="application/json",
                    response_schema=RoteiroCompletoAula,
                    tools=tools_config
                )
            )
            roteiro_pedagogico = RoteiroCompletoAula.model_validate_json(resposta_roteiro.text)
        except Exception as e_rot:
            erro_str = str(e_rot)
            if ("429" in erro_str or "RESOURCE_EXHAUSTED" in erro_str or "Quota" in erro_str) and tentativas_roteiro < 10:
                espera = min(15 * tentativas_roteiro, 60)
                print(f"[AVISO ROTEIRISTA] Limite de cota (429). Aguardando {espera}s (Tentativa {tentativas_roteiro}/10)...")
                if status_callback:
                    status_callback({
                        "etapa": "erro_api",
                        "titulo": "Roteiro da Aula",
                        "erro": erro_str,
                        "tipo_erro": "429"
                    })
                time.sleep(espera)
            elif ("503" in erro_str or "UNAVAILABLE" in erro_str or "500" in erro_str or "timeout" in erro_str.lower()) and tentativas_roteiro < 10:
                espera = min(5 * tentativas_roteiro, 30)
                print(f"[AVISO ROTEIRISTA] Servidor ocupado/Timeout. Retentando em {espera}s...")
                if status_callback:
                    status_callback({
                        "etapa": "erro_api",
                        "titulo": "Roteiro da Aula",
                        "erro": erro_str,
                        "tipo_erro": "503"
                    })
                time.sleep(espera)
            else:
                if status_callback:
                    status_callback({
                        "etapa": "erro_api",
                        "titulo": "Roteiro da Aula",
                        "erro": erro_str,
                        "tipo_erro": "outro"
                    })
                time.sleep(3)
                if tentativas_roteiro >= 10 or ("timeout" not in erro_str.lower() and "connection" not in erro_str.lower()):
                    raise e_rot

    t_fim_roteirista = time.time()
    print(f"[OK] Roteiro gerado com sucesso! {len(roteiro_pedagogico.esquema_paginas)} subtópicos mapeados.")
    if status_callback:
        status_callback({
            "etapa": "roteiro_concluido",
            "subtopicos": [sub.titulo for sub in roteiro_pedagogico.esquema_paginas],
            "esquema": [sub.model_dump() for sub in roteiro_pedagogico.esquema_paginas]
        })

    # ==============================================================================
    # FASE 2: AGENTE 2 + 2.5 - O ESCRITOR COM LOOP DE REVISÃO ATIVA
    # ==============================================================================
    t_inicio_escrita = time.time()
    print("\n[Agente 2 + 2.5] Iniciando laço de escrita com loop de revisão ativa...")
    aulas_conteudo_final = []
    MAX_TENTATIVAS_REVISAO = 5

    # Inicializa o arquivo de progresso incremental em Markdown
    os.makedirs("cache", exist_ok=True)
    progresso_md_path = os.path.join("cache", "progresso_conteudo.md")
    if os.path.exists(progresso_md_path):
        try:
            os.remove(progresso_md_path)
        except Exception as e_del:
            print(f"[AVISO] Não foi possível limpar o progresso anterior: {e_del}")

    from concurrent.futures import ThreadPoolExecutor, as_completed

    def processar_subtopico_worker(item_sub):
        idx, sub = item_sub
        t_inicio_sub = time.time()
        print(f"\n   -> [Paralelo] Iniciando Subtópico [{idx+1}/{len(roteiro_pedagogico.esquema_paginas)}]: {sub.titulo}")
        if status_callback:
            status_callback({
                "etapa": "subtopico_iniciado",
                "index": idx,
                "titulo": sub.titulo,
                "total": len(roteiro_pedagogico.esquema_paginas)
            })
        
        termos_busca = " ".join(sub.conceitos_chave_rag)
        query_rag = f"{tema_solicitado} - {sub.titulo} - {termos_busca}"
        
        tentativa = 0
        bloco_aprovado = False
        comentario_feedback_llm = "Nenhum. Esta é a primeira tentativa de escrita do bloco."
        subtopico_atual_dados = None
        dados_escritor_dict = None
        
        feedbacks = []
        historico_rascunhos = []
        erros_api_consecutivos = 0
        erros_429 = 0
        erros_503 = 0
        erros_outros = 0

        while tentativa < MAX_TENTATIVAS_REVISAO and not bloco_aprovado:
            tentativa += 1
            print(f"      [{sub.titulo}] (Tentativa {tentativa}/{MAX_TENTATIVAS_REVISAO}) Enviando para o Escritor...")
            if status_callback:
                status_callback({
                    "etapa": "subtopico_tentativa",
                    "index": idx,
                    "titulo": sub.titulo,
                    "tentativa": tentativa,
                    "max_tentativas": MAX_TENTATIVAS_REVISAO
                })

            if store_names:
                diretriz_veracidade = """HIERARQUIA E PRIORIDADE ABSOLUTA DAS FONTES RAG (FONTE PRIMÁRIA DO PROFESSOR):
1. FONTE PRIMÁRIA OBRIGATÓRIA (PESO MÁXIMO ABSOLUTO): Os Materiais de Apoio, notas de aula, slides, apostilas e ementas fornecidos diretamente pelo Professor (recuperados via RAG). Todo o formato da aula, a divisão dos conceitos, a notação matemática, o tom de voz, o estilo explicativo e o vocabulário DEVEM derivar obrigatoriamente dessa fonte primária.
2. FONTE SECUNDÁRIA COMPLEMENTAR: Os livros-texto gerais da biblioteca RAG. Devem ser utilizados estritamente como apoio secundário para aprofundar demonstrações, fornecer citações bibliográficas cruzadas e enriquecer exemplos, NUNCA sobrepondo o formato, a didática ou alterando as notações do material do professor."""
                contexto_rag_descricao = "os materiais de apoio do professor (fonte primária) e os livros-texto da base RAG (fonte secundária)"
                tools_config_worker = [
                    types.Tool(
                        file_search=types.FileSearch(
                            file_search_store_names=store_names,
                            metadata_filter=f'discipline="{codigo_disciplina.upper().strip()}"',
                            top_k=45
                        )
                    )
                ]
            else:
                diretriz_veracidade = "Como não há base RAG de apoio disponível, baseie-se no conhecimento estatístico consolidado da literatura acadêmica padrão (ex: Bussab & Morettin, Morettin & Singer, etc.). É terminantemente proibido inventar teoremas ou deduzir propriedades errôneas. Cite obras e páginas reais e verossímeis nas referências bibliográficas do retorno."
                contexto_rag_descricao = "o conhecimento estatístico consolidado da literatura acadêmica padrão"
                tools_config_worker = None

            prompt_escritor_worker = f"""
Você é um Professor Universitário de Estatística com didática extremamente fluida, moderna, clara e engajadora.

### CONTEXTO E MISSÃO
Você receberá as Diretrizes de Notação e Design do professor, {contexto_rag_descricao} e um [SUBTÓPICO_ALVO] que integra o [TÓPICO_DA_AULA].
Sua missão é atuar como o produtor científico principal do conteúdo teórico: você deve redigir a teoria acadêmica e formalismo matemático de forma extremamente completa, fluida e exaustiva para o [SUBTÓPICO_ALVO], preenchendo rigorosamente a estrutura 'SubtopicoValidado'.

---

### DIRETRIZES DE ESCOPO, TOM DE VOZ E PEDAGOGIA (MANDATÓRIO)
1. Linguagem Natural de Professor Acadêmico (SEM CLICHÊS GENÉRICOS OU PROSA COMPLICADA):
   - PROIBIDO USAR CLICHÊS ARTIFICIAIS: É terminantemente proibido utilizar expressões dramáticas ou vazias como "o coração da matemática", "a alma da estatística", "o motor conceitual" ou frases genéricas semelhantes.
   - LINGUAGEM FLUIDA E DIRETA: Escreva com a linguagem natural, elegante e articulada de um professor universitário em sala de aula. Explique o conceito com clareza cristalina, sem floreios desnecessários ou termos exageradamente complicados.
   - ADAPTAÇÃO AO ESTILO DO PROFESSOR (RAG): Se houver materiais do professor recuperados via RAG (slides, apostilas, notas de aula), ADAPTE O TOM DE VOZ E A LINGUAGEM para imitar a didática e o vocabulário preferido do professor.
2. Escrita Didática e Completa (SEM LIMITE DE PARÁGRAFOS): Sua principal prioridade é ENSINAR o conceito com extrema profundidade e clareza. Use prosa fluida, analogias reais do dia a dia e explicações passo a passo. Explique minuciosamente o significado prático de cada componente, variável, letra grega e parâmetro da fórmula matemática.
3. Regra de Ouro de Veracidade: {diretriz_veracidade}
4. Rigor de Notação e Perfeição de Renderização em LaTeX (KaTeX Compatible):
   - Toda notação matemática formal, hipóteses, coeficientes, variabilidades, erros e estatísticas de teste devem ser apresentadas em LaTeX ($ ou $$).
   - Mapeie cada conceito para os símbolos exatos definidos no bloco [DIRETRIZES_DE_ESTILO].
   - REGRAS ESTRITAS DE LATEX:
     a) O texto em português dentro de fórmulas deve estar envelopado pelo comando `\\text{{...}}`.
     b) Use apenas comandos KaTeX nativos (ex: `\\Delta`, `\\hat{{\\beta}}`, `\\bar{{X}}`).
     c) Escape todas as barras invertidas no JSON (`\\\\alpha`, `\\\\text`) para garantir integridade.
5. FIDELIDADE STRICTA AO FORMATO, LINGUAGEM E VOCABULÁRIO DO PROFESSOR (MANDATÓRIO):
   - Prioridade Absoluta aos Materiais do RAG: Adote obrigatoriamente a estrutura da aula, o formato das explicações, a divisão pedagógica, a linguagem e as convenções de terminologia presentes nos Materiais de Apoio e slides do Professor.
   - Por exemplo: se o professor usa o termo "Valor Esperado" em vez de "Esperança Matemática", ou "Resíduo" em vez de "Erro Amostral", você é OBRIGADO a utilizar "Valor Esperado" e "Resíduo" em toda a prosa, equações e exemplos da aula.
6. Tratamento de Feedbacks da Revisão (Tolerância Zero para Reincidência): Se a seção [FEEDBACKS_REVISAO] contiver apontamentos de reprovação e instruções de correção de tentativas anteriores, você deve ler cada um dos itens apontados com atenção cirúrgica. É MANDATÓRIO realizar as correções indicadas, reescrevendo os trechos com desvio e aplicando o formato, rigor ou explicação solicitados. Não repita os mesmos erros ou desvios em hipótese alguma.

---

### INSTRUÇÕES PARA PREENCHIMENTO DO SCHEMA DE RETORNO

1. 'titulo_subtopico' (string):
   - Deve conter o título exato do subtópico: '{sub.titulo}'.

2. 'conteudo' (objeto ConteudoSubtopico):
   - 'tipo_bloco' (string): Deve ser preenchido estritamente como 'teorico'.
   - 'conceito_intuitivo' (string): Prosa explicativa longa, fluida e profundamente didática (SEM LIMITE DE PARÁGRAFOS). Explique a motivação histórica, o problema prático do mundo real que impulsionou a criação deste conceito, analogias do dia a dia e desdobramentos de mercado. ATENÇÃO: Proibido inserir qualquer notação LaTeX matemática ($ ou $$) neste campo. Mantenha o foco puramente na prosa qualitativa.
   - 'conceito_formal' (string): Apresente o enunciado matemático definitivo do conceito ou teorema em LaTeX ($$ ou $). Após o enunciado da fórmula, explique minuciosamente por extenso em texto o significado de cada símbolo, matriz, vetor, parâmetro e suposição contida na fórmula.
   - 'propriedades_do_conceito' (lista de strings): Mapeie de forma exaustiva e detalhada todas as leis, teoremas e propriedades matemáticas deduzidas diretamente desse conceito.
   - 'pre_requisitos_e_auxiliares' (lista de strings): Liste os pré-requisitos conceituais e ferramentas de cálculo necessários para compreender este subtópico.
   - 'condicoes_de_contorno' (lista de strings): Descreva todas as premissas matemáticas e suposições fundamentais para a validade do modelo (ex: homocedasticidade, independência dos erros, normalidade). Se não houver, preencha 'N/A'.
   - 'simulador_interativo_recomendado' (string ou null): RELEVÂNCIA ESTRITA: Proponha uma simulação interativa baseada em Plotly APENAS se for altamente relevante e pedagógica para o conceito do subtópico (como diagnóstico de resíduos, regressão/correlação, estatística descritiva). Não recomende simuladores irrelevantes apenas para ter um gráfico. Se o conceito não se beneficiar diretamente de uma simulação visual essencial, defina estritamente como null.
   - 'deducao_formal_passo_a_passo' (lista de strings): Forneça a demonstração matemática completa. Cada item da lista deve conter a fórmula em LaTeX ($$) acompanhada de uma frase explicativa que descreva a transformação algébrica realizada naquela passagem.
   - 'interpretacao_geometrica_grafica' (string): Explique de forma detalhada como visualizar esse conceito graficamente ou espacialmente (ex: inclinação da reta, áreas sob curvas de densidade, projeções ortogonais de vetores de erro).
   - 'exemplo_canonico' (objeto EstruturaExemplo):
     * 'enunciado' (string): Enunciado realista, denso e complexo sobre o mundo real (controle de qualidade, ensaios clínicos, finanças, IoT), contextualizando a origem dos dados e o desafio.
     * 'passo_a_passo_solucao' (lista de strings): As passagens e etapas de cálculo detalhadas em LaTeX ($$), mostrando explicitamente a substituição de cada valor numérico nas fórmulas, sem pular nenhuma conta intermediária.
     * 'resultado_final' (string): O resultado aritmético final acompanhado de uma interpretação prática e laudo conclusivo detalhado em múltiplos parágrafos.

3. 'fontes_rag' (lista de FonteRDetalhada):
   Cada item representa uma fonte bibliográfica e deve conter:
   - 'livro_autor' (string): OBRIGATÓRIO. Sobrenome dos autores e título clássico do livro, slide ou material de apoio.
   - 'capitulo' (string): OBRIGATÓRIO. Nome ou número do capítulo, seção ou unidade consultada.
   - 'paginas_utilizadas' (string): O número da página ou intervalo de páginas (ex: "p. 142" ou "pp. 210-214"). Caso a página não conste no RAG, utilize "p. S/N". ATENÇÃO: A omissão do nome do livro/material ou do capítulo/seção causará REPROVAÇÃO IMEDIATA pelo Revisor.

---

### ENTRADAS DO USUÁRIO
- [TÓPICO_DA_AULA]: {tema_solicitado}
- [SUBTÓPICO_ALVO]: {sub.titulo}
- [DIRETRIZES_DE_ESTILO]:
{diretrizes_texto}
- [FEEDBACKS_REVISAO]: {comentario_feedback_llm}
"""

            config_escritor_worker = types.GenerateContentConfig(
                tools=tools_config_worker,
                thinking_config=types.ThinkingConfig(thinking_level="medium"),
                temperature=1.0,
                response_mime_type="application/json",
                response_schema=SubtopicoValidado
            )

            try:
                resposta_escritor = client.models.generate_content(
                    model="gemini-3.1-flash-lite",
                    contents=[query_rag, prompt_escritor_worker],
                    config=config_escritor_worker
                )
                
                dados_escritor_dict = json.loads(resposta_escritor.text)
                from latex_sanitizer import sanitizar_payload_latex
                dados_escritor_dict = sanitizar_payload_latex(dados_escritor_dict)
                
                laudo_revisao = auditar_subtopico_local(dados_escritor_dict, diretrizes_texto)
                obj_rascunho = laudo_revisao.conteudo_corrigido or SubtopicoValidado(**dados_escritor_dict)
                nota_rascunho = getattr(laudo_revisao, "nota_qualidade", 50)
                historico_rascunhos.append((nota_rascunho, obj_rascunho))

                if laudo_revisao.aprovado:
                    print(f"      [OK - {sub.titulo}] Bloco APROVADO! (Nota: {nota_rascunho}/100)")
                    bloco_aprovado = True
                    if status_callback:
                        status_callback({
                            "etapa": "subtopico_aprovado",
                            "index": idx,
                            "titulo": sub.titulo,
                            "dados": obj_rascunho.model_dump()
                        })
                    
                    subtopico_atual_dados = obj_rascunho
                    
                    fontes_capturadas = []
                    if hasattr(resposta_escritor, "grounding_metadata") and resposta_escritor.grounding_metadata:
                        chunks = resposta_escritor.grounding_metadata.grounding_chunks
                        if chunks:
                            for chunk in chunks:
                                if hasattr(chunk, "retrieved_context") and chunk.retrieved_context:
                                    ctx = chunk.retrieved_context
                                    title = getattr(ctx, "title", "Livro Ingerido")
                                    page = str(getattr(ctx, "page_number", "S/N"))
                                    fontes_capturadas.append(
                                        FonteRDetalhada(
                                            livro_autor=title,
                                            capitulo="N/A (Grounding)",
                                            paginas_utilizadas=f"p. {page}" if page != "S/N" else "p. não especificada"
                                        )
                                    )
                    if fontes_capturadas:
                        vistas = set()
                        fontes_unicas = []
                        for f_c in fontes_capturadas:
                            chave = (f_c.livro_autor, f_c.paginas_utilizadas)
                            if chave not in vistas:
                                vistas.add(chave)
                                fontes_unicas.append(f_c)
                        subtopico_atual_dados.fontes_rag = fontes_unicas
                else:
                    feedbacks.append(laudo_revisao.comentario_correcao)
                    comentario_feedback_llm = f"ALERTA DE REPROVAÇÃO: {laudo_revisao.comentario_correcao}"

            except Exception as e_err:
                tentativa -= 1
                erros_api_consecutivos += 1
                erro_str = str(e_err)
                if "429" in erro_str or "RESOURCE_EXHAUSTED" in erro_str or "Quota" in erro_str:
                    erros_429 += 1
                    tempo_espera = min(15 * erros_api_consecutivos, 45)
                    print(f"      [AVISO API - {sub.titulo}] Limite de cota (429). Aguardando {tempo_espera}s para retentar...")
                    time.sleep(tempo_espera)
                elif "503" in erro_str or "UNAVAILABLE" in erro_str or "500" in erro_str or "timeout" in erro_str.lower():
                    erros_503 += 1
                    tempo_espera = min(5 * erros_api_consecutivos, 25)
                    print(f"      [AVISO API - {sub.titulo}] Servidor ocupado (503). Retentando em {tempo_espera}s...")
                    time.sleep(tempo_espera)
                else:
                    erros_outros += 1
                    print(f"      [ERRO - {sub.titulo}] Oscilação de API: {erro_str[:80]}. Retentando em 3s...")
                    time.sleep(3)

        if not subtopico_atual_dados and historico_rascunhos:
            melhor_nota, melhor_rascunho = max(historico_rascunhos, key=lambda x: x[0])
            subtopico_atual_dados = melhor_rascunho

        t_fim_sub = time.time()
        log_sub_item = {
            "titulo": sub.titulo,
            "tentativas": tentativa,
            "max_tentativas": MAX_TENTATIVAS_REVISAO,
            "reprovacoes": len(feedbacks),
            "feedbacks": feedbacks,
            "erros_api": {
                "429": erros_429,
                "503": erros_503,
                "outros": erros_outros
            },
            "tempo_segundos": round(t_fim_sub - t_inicio_sub, 2),
            "aprovado": bloco_aprovado
        }

        return (idx, subtopico_atual_dados, log_sub_item)

    items_to_process = list(enumerate(roteiro_pedagogico.esquema_paginas))
    resultados_subtopicos = []

    # Dispara TODOS os subtópicos em paralelo simultaneamente
    max_workers_count = max(len(items_to_process), 1)
    with ThreadPoolExecutor(max_workers=max_workers_count) as executor:
        futures = [executor.submit(processar_subtopico_worker, item) for item in items_to_process]
        for future in as_completed(futures):
            try:
                res = future.result()
                if res and res[1]:
                    resultados_subtopicos.append(res)
            except Exception as e_fut:
                print(f"[ERRO THREAD] Falha na thread de subtópico: {e_fut}")

    resultados_subtopicos.sort(key=lambda x: x[0])
    aulas_conteudo_final = [res[1] for res in resultados_subtopicos if res[1] is not None]
    log_subtopicos = [res[2] for res in resultados_subtopicos if res[2] is not None]

    t_fim_escrita = time.time()

    return {
        "tema": tema_solicitado,
        "conteudo_paginas": [p.model_dump() for p in aulas_conteudo_final],
        "log_gerador": {
            "tempo_roteirista_segundos": round(t_fim_roteirista - t_inicio_roteirista, 2),
            "tempo_escrita_revisao_segundos": round(t_fim_escrita - t_inicio_escrita, 2),
            "subtopicos": log_subtopicos
        }
    }

if __name__ == "__main__":
    print("[AVISO] A geração de conteúdo deve ser executada a partir da interface do Streamlit.")
    print("Por favor, execute o comando: streamlit run app.py")
