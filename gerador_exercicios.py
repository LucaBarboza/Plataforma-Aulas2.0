import os
import json
import re
import time
from google import genai
from google.genai import types

# Importando o contrato estruturado do caderno de exercícios
from schemas import CadernoExerciciosSubtopico

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

# ==============================================================================
# FUNÇÃO PRINCIPAL DE ORQUESTRAÇÃO DE EXERCÍCIOS
# ==============================================================================
def gerar_caderno_exercicios(caminho_payload_teoria: str, nome_professor: str = None, codigo_disciplina: str = None, diretrizes_texto: str = None):
    # Garante que temos a chave configurada
    if not os.environ.get("GEMINI_API_KEY"):
        raise ValueError("Chave de API 'GEMINI_API_KEY' não configurada. Configure a chave nos Secrets do Streamlit ou no ambiente.")

    try:
        client = genai.Client(http_options={"timeout": 300_000})
    except Exception as e:
        print(f"[ERRO] Erro ao inicializar o cliente do Google GenAI: {e}")
        return None
    
    # 1. Valida se o insumo do Agente 2 existe na máquina local
    if not os.path.exists(caminho_payload_teoria):
        print(f"[ERRO] Erro crítico: O arquivo '{caminho_payload_teoria}' não foi encontrado. Gere a teoria primeiro.")
        return None
        
    with open(caminho_payload_teoria, "r", encoding="utf-8") as f:
        payload_teoria = json.load(f)
        
    tema_aula = payload_teoria["tema"]
    print(f"\n[Agente 3] Iniciando a criação do caderno de exercícios fatiado por subtópico para a aula: '{tema_aula}'...")

    # 2. Valida as diretrizes de estilo do professor (enviadas obrigatoriamente pelo Streamlit)
    if not diretrizes_texto or not diretrizes_texto.strip():
        raise ValueError("As diretrizes de notação e estilo são obrigatórias e devem ser fornecidas pelo Streamlit.")

    # 3. Busca e Configuração das Stores do RAG (File Search)
    store_names = []
    if nome_professor and codigo_disciplina:
        NOME_STORE = f"store-{nome_professor.lower().strip()}-{codigo_disciplina.lower().strip()}"
        NOME_STORE_FALLBACK = "plataforma-estatistica-db"
        try:
            stores_disponiveis = list(client.file_search_stores.list())
            # Busca store específica
            for store in stores_disponiveis:
                if store.display_name == NOME_STORE:
                    store_names.append(store.name)
                    print(f"[RAG Exercícios] RAG específico do professor ativado! Store: {store.display_name}")
            # Busca store global
            for store in stores_disponiveis:
                if store.display_name == NOME_STORE_FALLBACK:
                    store_names.append(store.name)
                    print(f"[RAG Exercícios] RAG de livros ativado! Store: {store.display_name}")
        except Exception as e:
            print(f"[ALERTA Exercícios] Erro ao pesquisar stores de arquivos RAG: {e}")

    questoes_multipla_escolha_acumuladas = []
    questoes_discursivas_acumuladas = []

    # 4. Processamento e Geração por Subtópico
    paginas = payload_teoria.get("conteudo_paginas", [])
    for idx, pag in enumerate(paginas):
        titulo_sub = pag.get("titulo_subtopico", f"Subtópico {idx+1}")
        conteudo_sub = pag.get("conteudo", {})
        intencao_sub = conteudo_sub.get("conceito_intuitivo", "")
        formalismo_sub = conteudo_sub.get("conceito_formal", "")
        
        print(f"   -> [Subtópico {idx+1}/{len(paginas)}] Gerando 2 fechadas e 3 abertas com RAG/Plotly para: '{titulo_sub}'...")

        # Configura as tools RAG por subtópico se existirem
        tools_config = None
        if store_names:
            tools_config = [
                types.Tool(
                    file_search=types.FileSearch(
                        file_search_store_names=store_names,
                        metadata_filter=f'discipline="{codigo_disciplina.upper().strip()}"',
                        top_k=25
                    )
                )
            ]

        prompt_exercicios = fr"""
Você é um Professor Universitário Titular e Avaliador Acadêmico de Estatística e Probabilidade.

### CONTEXTO E MISSÃO
Você receberá o [SUBTOPICO_DA_AULA] que acabou de ser gerado, acesso aos materiais de apoio via RAG (notas de aula e slides do professor, além de livros-texto) e as [DIRETRIZES_DE_ESTILO] estritas de notação.
Sua missão é atuar como um elaborador de bancas examinadoras de topo: você deve projetar um caderno de exercícios de altíssimo nível universitário, profundo e pedagogicamente envolvente sobre este subtópico específico, preenchendo a estrutura 'CadernoExerciciosSubtopico'.

---

### DIRETRIZES DE ESCOPO, TOM DE VOZ E PEDAGOGIA (MANDATÓRIO)

1. LINGUAGEM NATURAL E DIRETA DE PROFESSOR (TOLERÂNCIA ZERO PARA CLICHÊS ARTIFICIAIS):
   - BANIMENTO DE CLICHÊS DRAMÁTICOS: É estritamente proibido usar expressões genéricas ou românticas vazias como "o coração da matemática", "a alma da estatística", "o motor conceitual" ou frases poéticas desnecessárias.
   - LINGUAGEM FLUIDA E ARTICULADA: Escreva os enunciados, opções de resposta, dicas e gabaritos na prosa elegante, cristalina, direta e didática de um professor universitário conversando com seus alunos.
   - FIDELIDADE AO RAG DO PROFESSOR: Adote o tom de voz, os bordões didáticos, o vocabulário técnico e os hábitos de resolução presentes nos Materiais de Apoio e slides do docente.

2. CENÁRIOS IMERSIVOS DO MUNDO REAL (SEM ENUNCIADOS ABSTRATOS):
   - Crie problemas ancorados em contextos reais e práticos: ensaios clínicos farmacêuticos, análise de risco financeiro, controle estatístico de qualidade industrial, modelos preditivos de machine learning, testes A/B de produtos digitais ou redes de sensores IoT.
   - Proibido enunciados puramente formais e descontextualizados (ex: "Seja X uma V.A..."). Introduza a origem dos dados, a pergunta de negócio/pesquisa e o desafio prático.

3. DISTRATORES INTELIGENTES E GABARITO DIDÁTICO (QUESTÕES FECHADAS):
   - DISTRATORES PLAUSÍVEIS: Nas questões de múltipla escolha (A, B, C, D, E), as alternativas incorretas (distratores) NÃO devem ser números aleatórios soltos. Elas DEVEM representar exatamente os resultados de erros conceituais ou operacionais típicos de estudantes de graduação (ex: esquecer de dividir pelo erro padrão $\sqrt{{n}}$, confundir teste uni vs. bicaudal, trocar desvio padrão por variância, ou errar o sinal da estatística $z$/$t$).
   - GABARITO MINI-AULA: O `gabarito_comentado` deve demonstrar detalhadamente a resolução correta em LaTeX ($$) E explicar brevemente a origem do erro de cada uma das alternativas incorretas.

4. DEDUÇÃO E SUB-ITENS DIDÁTICOS (QUESTÕES DISCURSIVAS ABERTAS):
   - Estruture o enunciado com sub-itens lógicos encadeados:
     * (a) Identificação e formulação matemática das hipóteses $H_0$ e $H_1$ em LaTeX.
     * (b) Desenvolvimento do cálculo algebraico da estatística de teste e definição do valor-crítico ou $p$-valor.
     * (c) Decisão estatística conclusiva acompanhada de um laudo prático em português para a tomada de decisão.
   - O `gabarito_passo_a_passo` deve apresentar a substituição explícita de cada valor numérico nas equações em LaTeX ($$), sem pular passagens intermediárias.

5. REGRAS ESTRITAS DE RELEVÂNCIA PARA GRÁFICOS PLOTLY E CALCULADORAS VISUAIS DE DISTRIBUIÇÃO (codigo_plotly):
   - MÁXIMA RELEVÂNCIA PRÁTICA: Gere o código Plotly no campo 'codigo_plotly' SE E SOMENTE SE o recurso gráfico for uma ferramenta didática crucial para resolver ou interpretar o exercício.
   - CALCULADORAS VISUAIS DE DISTRIBUIÇÃO ENCORAJADAS: Para questões de teste de hipóteses, intervalos de confiança ou probabilidades, recomenda-se fortemente construir uma Calculadora Visual de Distribuição em Plotly (ex: densidade Gaussian/Normal $z$, $t$ de Student, Qui-Quadrado $\chi^2$ ou $F$ de Snedecor). O gráfico deve exibir a curva contínua (`go.Scatter`) com a região de rejeição $RC$, cauda de probabilidade ou $p$-valor sombreado com transparência em destaque (usando a paleta de cores do professor: `PRIMARY_BLUE`, `CRITICAL_RED`, etc.).
   - PROIBIDO GRÁFICOS DECORATIVOS: Se a questão for teórica qualitativa ou de aritmética básica sem utilidade gráfica, defina o campo 'codigo_plotly' OBRIGATORIAMENTE como null.
   - REGRAS DE CÓDIGO PLOTLY:
     * Crie e configure o objeto de figura nomeado estritamente como `fig` (ex: `fig = go.Figure(...)`).
     * PROIBIDO incluir importações (`import ...`). Assuma que `go`, `px`, `np`, `pd` e `stats` (da SciPy) já estão previamente importadas no escopo global.
     * Use o template `"plotly_white"`, margens limpas (`margin=dict(l=20, r=20, t=30, b=20)`) e paleta dinâmica do professor.

6. RIGOR ABSOLUTO DE LATEX (KaTeX COMPATIBLE):
   - Toda notação matemática, símbolos, estatísticas e fórmulas devem estar em LaTeX ($ ou $$).
   - OBRIGATÓRIO: Qualquer texto explicativo em português dentro de blocos matemáticos deve estar envelopado pelo comando `\text{{...}}`.
   - Mapeie rigorosamente as Notações do Professor fornecidas no bloco [DIRETRIZES_DE_ESTILO].

7. RESPOSTA NUMÉRICA ESPERADA PARA AUTO-CORREÇÃO AUTOMÁTICA:
   - No campo `resposta_numerica_esperada` das questões abertas, forneça o valor escalar em `float` (arredondado para 2 a 4 casas decimais) correspondente ao resultado numérico final da questão (ex: `0.0456` para um p-valor, ou `2.45` para um valor t calculado). Se a questão for puramente qualitativa/discursiva sem um único resultado numérico, defina como `null`.

8. HIERARQUIA DE FONTES RAG E TERMINOLOGIA:
   - Os Materiais de Apoio, notas de aula e slides do Professor são a FONTE PRIMÁRIA MÁXIMA para o vocabulário, notações e estilo das questões.
   - Se uma questão for inspirada em um problema extraído de um material recuperado do RAG, preencha o campo `referencia_livro` com a citação exata desse material. Caso o conteúdo não tenha vindo do RAG ou se nenhum RAG estiver disponível, defina OBRIGATORIAMENTE como `null`. É TERMINANTEMENTE PROIBIDO inventar ou alucinar citações fictícias.

---

### INSTRUÇÕES PARA PREENCHIMENTO DO SCHEMA DE RETORNO

1. 'questoes_multipla_escolha' (lista contendo exatamente 2 objetos QuestaoFechada):
   - 'enunciado' (string): Situação prática realista e pergunta clara.
   - 'alternativas' (objeto AlternativasFechadas): Opções 'A', 'B', 'C', 'D' e 'E' plausíveis baseadas em erros conceituais e acertos.
   - 'alternativa_correta' (string): Letra única da resposta correta ('A', 'B', 'C', 'D' ou 'E').
   - 'dica' (string): Insight conceitual sutil sem dar o gabarito.
   - 'gabarito_comentado' (string): Demonstração matemática completa e explicação de por que a correta é a certa e as outras estão erradas.
   - 'codigo_plotly' (string ou null): Script Plotly da Calculadora Visual de Distribuição ou gráfico de suporte, se indispensável.
   - 'referencia_livro' (string ou null): Citação bibliográfica RAG ou null.

2. 'questoes_discursivas' (lista contendo exatamente 3 objetos QuestaoAberta):
   - 'enunciado' (string): Problema denso com sub-itens (a, b, c).
   - 'dica' (string): Direcionamento inicial.
   - 'gabarito_passo_a_passo' (lista de strings): Etapas de cálculo em LaTeX ($$) com frases explicativas em cada passagem.
   - 'codigo_plotly' (string ou null): Script Plotly se aplicável.
   - 'referencia_livro' (string ou null): Citação bibliográfica RAG ou null.
   - 'resposta_numerica_esperada' (float ou null): O resultado escalar exato para validação automática na UI.

---

### ENTRADAS DO USUÁRIO
- [SUBTOPICO_DA_AULA]:
  * Subtópico: {titulo_sub}
  * Intuição: {intencao_sub}
  * Formalismo: {formalismo_sub}
- [DIRETRIZES_DE_ESTILO]:
{diretrizes_texto}
"""

        config_exercicios = types.GenerateContentConfig(
            tools=tools_config,
            thinking_config=types.ThinkingConfig(thinking_level="medium"),
            temperature=1.0,
            response_mime_type="application/json",
            response_schema=CadernoExerciciosSubtopico
        )
        
        try:
            resposta_exercicios = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=[f"Subtópico: {titulo_sub}", prompt_exercicios],
                config=config_exercicios
            )
            
            subtopico_caderno = CadernoExerciciosSubtopico.model_validate_json(resposta_exercicios.text)
            
            questoes_multipla_escolha_acumuladas.extend(subtopico_caderno.questoes_multipla_escolha)
            questoes_discursivas_acumuladas.extend(subtopico_caderno.questoes_discursivas)
            
            print(f"   [OK] Subtópico '{titulo_sub}' concluído: 2 fechadas e 3 abertas adicionadas!")
            
            time.sleep(1)
            
        except Exception as e:
            print(f"   [ERRO] Falha ao gerar exercícios para o subtópico '{titulo_sub}': {e}")
            continue

    # 5. Consolida e formata em dicionário
    caderno_final = {
        "topico_aula": tema_aula,
        "questoes_multipla_escolha": [q.model_dump() if hasattr(q, "model_dump") else q for q in questoes_multipla_escolha_acumuladas],
        "questoes_discursivas": [q.model_dump() if hasattr(q, "model_dump") else q for q in questoes_discursivas_acumuladas]
    }
    
    print(f"   [SUCESSO] Caderno de exercícios concluído! Total: {len(caderno_final['questoes_multipla_escolha'])} fechadas e {len(caderno_final['questoes_discursivas'])} abertas.")
    from latex_sanitizer import sanitizar_payload_latex
    return sanitizar_payload_latex(caderno_final)

if __name__ == "__main__":
    print("[AVISO] A geração de exercícios deve ser executada a partir da interface do Streamlit.")
    print("Por favor, execute o comando: streamlit run app.py")
