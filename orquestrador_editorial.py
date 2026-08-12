import os
import json
import re
from google import genai
from google.genai import types
from schemas import AulaUnificadaELapidada

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
def lapidar_conteudo_global(caminho_payload_teoria: str, diretrizes_texto: str = None):
    # Garante a inicialização da chave
    carregar_chave_api()
    client = genai.Client(http_options={"timeout": 300_000})

    if not os.path.exists(caminho_payload_teoria):
        print(f"[ERRO] O arquivo '{caminho_payload_teoria}' não foi encontrado.")
        return None

    with open(caminho_payload_teoria, "r", encoding="utf-8") as f:
        payload_bruto = json.load(f)

    dados_entrada_str = json.dumps(payload_bruto, ensure_ascii=False)

    print("\n[Agente 3.5] Assumindo o controle editorial. Unificando e eliminando repetições da aula...")

    prompt_editorial = f"""
Você é o Editor-Chefe de uma prestigiada editora de livros didáticos universitários de Estatística.

### CONTEXTO E MISSÃO
Você receberá o [CAPÍTULO_BRUTO_AULA] (em JSON), contendo as páginas geradas separadamente ou em paralelo pelo Agente Escritor para a aula '{payload_bruto['tema']}'.
Sua missão é atuar como editor unificador: você deve lapidar, costurar, desduplicar e organizar as páginas para que funcionem como um capítulo contínuo, fluido, coeso e visualmente impecável de um livro didático premium, preenchendo a estrutura 'AulaUnificadaELapidada'.

---

### DIRETRIZES DE ORGANIZAÇÃO, DESDUPLICAÇÃO E LAPIDAÇÃO (MANDATÓRIO)
1. Divisão de Trabalho, Desduplicação e Unificação (SUPORTE À GERAÇÃO PARALELA): Como os subtópicos foram gerados em paralelo, analise a aula inteira de ponta a ponta e ELIMINE QUALQUER REPETIÇÃO DE CONCEITOS, INTRODUÇÕES DUPLICADAS, FÓRMULAS SOBREPOSTAS OU CONTEXTOS HISTÓRICOS REDUNDANTES entre subtópicos adjacentes. Preserve a primeira definição detalhada e faça os subtópicos seguintes avançarem diretamente com fluidez, criando frases de transição suaves.
2. Linguagem Fluida de Professor (SEM CLICHÊS GENÉRICOS): Unifique a prosa utilizando a linguagem natural, articulada, elegante e fluida de um professor universitário em sala de aula. É TERMINANTEMENTE PROIBIDO utilizar metáforas vazias ou clichês genéricos como "o coração da matemática", "a alma da estatística", "o motor conceitual" ou frases dramáticas desnecessárias.
3. Foco no Ensino e Didática Rica: Ao unificar a prosa, garanta que o texto mantenha o foco em ENSINAR os conceitos intuitivamente com clareza. Não elimine parágrafos explicativos úteis ou analogias didáticas reais; a aula deve ser densa em conteúdo explicativo e fácil de compreender.
4. Rigor Absoluto de Notação Dinâmica (Tolerância Zero para Adulterações): Você é OBRIGADO a seguir e preservar todas as notações matemáticas e símbolos estatísticos gerados originalmente pelo Escritor de acordo com o bloco [DIRETRIZES_DE_ESTILO] abaixo. Não mude, simplifique ou reverta nenhum símbolo para termos planos ou notações informais.
5. DEDUPLICAÇÃO E UNICIDADE ABSOLUTA DE SIMULADORES E GRÁFICOS INTERATIVOS: Analise todas as recomendações de simulador que vêm dos subtópicos. É TERMINANTEMENTE PROIBIDO manter múltiplos simuladores com propostas, gráficos ou tipos de dados semelhantes (ex: múltiplos gráficos de dispersão simples ou histogramas repetidos). Selecione NO MÁXIMO 1 OU 2 SIMULADORES PARA A AULA INTEIRA, garantindo que cada um deles explore um conceito visual e tipo de gráfico COMPLETAMENTE DIFERENTE (ex: se 1 for um gráfico 2D de resíduos, o 2º deve ser uma superfície 3D ou mapa de calor). Se as recomendações forem parecidas ou irrelevantes, MANTENHA APENAS 1 OU DEIXE A LISTA 'simuladores_da_aula' VAZIA [].
6. Rigor de Rodapé Bibliográfico: Colete APENAS as fontes que vieram ESTRITAMENTE do RAG em 'fontes_rag'. Elimine duplicatas e monte a lista 'referencias_bibliograficas_finais'. Se NÃO houver fontes RAG presentes no capítulo bruto, defina a lista 'referencias_bibliograficas_finais' OBRIGATORIAMENTE como VAZIA []. É TERMINANTEMENTE PROIBIDO inventar autores, livros fictícios ou colocar nomes de obras genéricas fora do RAG.

---

### DIRETRIZES DE ESTILO E NOTAÇÃO DO PROFESSOR (MANDATÓRIO)
[DIRETRIZES_DE_ESTILO]:
{diretrizes_texto or "Não fornecidas."}

---

### ENTRADAS DO USUÁRIO
- [CAPÍTULO_BRUTO_AULA]:
{dados_entrada_str}
"""

    config_editorial = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="medium"), # Carga pesada de pensamento para analisar a coerência global
        temperature=1.0,
        response_mime_type="application/json",
        response_schema=AulaUnificadaELapidada
    )

    try:
        resposta = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=[dados_entrada_str, prompt_editorial],
            config=config_editorial
        )

        print(" [OK] Aula unificada, referências compiladas no rodapé e livre de repetições!")
        return json.loads(resposta.text)

    except Exception as e:
        print(f" [ERRO] Erro crítico no processo editorial: {e}")
        try:
            # Fallback robusto que mapeia os campos do payload bruto para a estrutura esperada
            print(" [FALLBACK] Mapeando payload_bruto para a estrutura da AulaUnificadaELapidada...")
            paginas_conteudo = []
            simuladores_da_aula = []
            referencias_set = set()
            
            for idx, pag in enumerate(payload_bruto.get("conteudo_paginas", [])):
                titulo = pag.get("titulo_subtopico", f"Subtópico {idx + 1}")
                conteudo = pag.get("conteudo", {})
                
                # Extrai fontes RAG
                fontes = pag.get("fontes_rag", [])
                for f in fontes:
                    livro = str(f.get("livro_autor", "") or "").strip()
                    cap = str(f.get("capitulo", "") or "").strip()
                    paginas = str(f.get("paginas_utilizadas", "") or "").strip()
                    
                    if re.match(r'^(files/|store-?|[a-z0-9_-]{8,40}$)', livro, re.I) or not livro or livro.lower() in ["n/a", "none", "null"]:
                        livro = "Material de Apoio do Professor"
                        
                    ref_str = f"{livro}"
                    if cap and cap.lower() not in ["n/a", "n/a (grounding)", "none", "null"]:
                        ref_str += f" - {cap}"
                    if paginas and paginas.lower() not in ["n/a", "p. não especificada", "none", "null"]:
                        ref_str += f", {paginas}"
                        
                    if ref_str:
                        referencias_set.add(ref_str)
                        
                # Extrai exemplo
                ex_canonico = conteudo.get("exemplo_canonico")
                exemplos_ricos = []
                if ex_canonico:
                    exemplos_ricos.append({
                        "contexto_e_enunciado": ex_canonico.get("enunciado", ""),
                        "dados_brutos_sumarizados": "Dados do exemplo canônico.",
                        "desenvolvimento_aritmético_passo_a_passo": ex_canonico.get("passo_a_passo_solucao", []),
                        "conclusao_e_laudo_comercial": ex_canonico.get("resultado_final", "")
                    })
                    
                # Extrai simulador recomendado
                sim_rec = conteudo.get("simulador_interativo_recomendado")
                if sim_rec:
                    simuladores_da_aula.append({
                        "indice_pagina": str(idx + 1),
                        "nome_simulador": f"Simulador: {titulo}",
                        "descricao_simulador": sim_rec
                    })
                    
                paginas_conteudo.append({
                    "titulo_subtopico": titulo,
                    "discussao_teorica_prosa": conteudo.get("conceito_intuitivo", ""),
                    "prosa_longa_expandida": conteudo.get("conceito_intuitivo", ""),
                    "formalismo_latex": conteudo.get("conceito_formal", ""),
                    "deducao_analitica_linhas": conteudo.get("deducao_formal_passo_a_passo") or [],
                    "exemplos_praticos_ricos": exemplos_ricos,
                    "simulador_interativo_recomendado": sim_rec
                })
                
            resultado_final = {
                "tema_global": payload_bruto.get("tema", "Aula Teórica"),
                "paginas_conteudo": paginas_conteudo,
                "simuladores_da_aula": simuladores_da_aula,
                "referencias_bibliograficas_finais": list(referencias_set) if referencias_set else []
            }
            from latex_sanitizer import sanitizar_payload_latex
            return sanitizar_payload_latex(resultado_final)
        except Exception as ex_fallback:
            print(f" [ERRO] Falha crítica também no fallback editorial: {ex_fallback}")
            from latex_sanitizer import sanitizar_payload_latex
            return sanitizar_payload_latex(payload_bruto)

def expandir_subtopico_para_prosa_livro(dados_subtopico: dict, diretrizes_texto: str = None) -> str:
    carregar_chave_api()
    client = genai.Client(http_options={"timeout": 300_000})
    
    prompt = f"""
    Você é um Professor Catedrático de Estatística Matemática. Sua única missão é pegar o esboço conceitual e formal de um subtópico e expandi-lo em um capítulo longo, denso e exaustivo de um livro didático de nível universitário premium.
    
    REGRAS DE CONSTRUÇÃO DE TEXTO E PEDAGOGIA:
    1. FOCO TOTAL NO ENSINO E DIDÁTICA DO PROFESSOR: O foco pedagógico, a intuição conceitual, os exemplos e a ênfase dos tópicos DEVEM espelhar primariamente os Materiais de Apoio, notas de aula e slides do Professor. Dedique a prosa a explicar o significado prático e a lógica do conceito no estilo didático do docente.
    2. ESCREVA EM PROSA FLUIDA, RICA E SEM LIMITE DE PARÁGRAFOS: NÃO HÁ LIMITE NO NÚMERO DE PARÁGRAFOS — quanto mais longo, denso, enciclopédico e detalhado for o texto, melhor! Use todo o espaço disponível para dar máxima profundidade pedagógica ao texto. É terminantemente proibido resumir, abreviar ou usar listas simples com tópicos/bullets (-). Seja o mais exaustivo e didático possível.
    3. PROFUNDIDADE HISTÓRICA E MOTIVAÇÃO: Explique o porquê desse conceito existir, qual problema prático da ciência ele resolve, como os pesquisadores pensavam antes dele e as implicações práticas de sua aplicação.
    4. RIGOR DE NOTAÇÃO E RENDERIZAÇÃO DO LATEX (KaTeX Compatible): Conecte o texto de forma elegante com as fórmulas em LaTeX ($ ou $$) fornecidas. Você é OBRIGADO a respeitar estritamente as diretrizes de notação no bloco [DIRETRIZES_DE_ESTILO].
       - TEXTO EM PORTUGUÊS NO LATEX: Toda e qualquer palavra em português dentro do ambiente LaTeX DEVE estar contida no comando `\\text{{...}}` (ex: `\\hat{{\\beta}} \\text{{ onde }} x`).
       - SEM PACOTES INCOMPATÍVEIS: Proibido usar `\\textgreek`, `\\bm` ou sintaxes não suportadas pelo KaTeX. Use comandos KaTeX padrão (`\\Delta`, `\\boldsymbol{{\\theta}}`, `\\varepsilon`, `\\sigma^2`).
    
    [DIRETRIZES_DE_ESTILO]:
    {diretrizes_texto or "Não fornecidas."}

    Retorne o texto limpo em Markdown contendo os parágrafos de prosa profundos.
    """
    
    resposta = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=[json.dumps(dados_subtopico, ensure_ascii=False), prompt],
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_level="medium"),
            temperature=1.0
        )
    )
    return resposta.text.strip()

def construir_prosa_longa_capitulo(caminho_payload_lapidado: str, diretrizes_texto: str = None) -> dict:
    """
    Percorre cada página do payload lapidado e expande sua prosa qualitativa em capítulo longo.
    """
    if not os.path.exists(caminho_payload_lapidado):
        return {}
    with open(caminho_payload_lapidado, "r", encoding="utf-8") as f:
        payload = json.load(f)
    
    paginas = payload.get("paginas_conteudo", []) or payload.get("conteudo_paginas", [])
    for idx, pagina in enumerate(paginas):
        dados_subtopico = {
            "titulo_subtopico": pagina.get("titulo_subtopico", f"Subtópico {idx+1}"),
            "discussao_teorica_prosa": pagina.get("discussao_teorica_prosa", "") or pagina.get("conteudo", {}).get("conceito_intuitivo", ""),
            "formalismo_latex": pagina.get("formalismo_latex", "") or pagina.get("conteudo", {}).get("conceito_formal", "")
        }
        try:
            prosa_expandida = expandir_subtopico_para_prosa_livro(dados_subtopico, diretrizes_texto)
            pagina["prosa_longa_expandida"] = prosa_expandida
        except Exception as e_exp:
            print(f"[AVISO] Falha ao expandir prosa do subtópico {idx+1}: {e_exp}")
            pagina["prosa_longa_expandida"] = dados_subtopico["discussao_teorica_prosa"]
            
    payload["paginas_conteudo"] = paginas
    from latex_sanitizer import sanitizar_payload_latex
    return sanitizar_payload_latex(payload)

def gerar_resumo_compacto_aula(payload_aula: dict) -> str:
    """
    Gera um resumo ultracompacto (~150-250 palavras) de uma aula finalizada
    para servir de memória pedagógica acumulada para as próximas aulas sem sobrecarregar o contexto.
    """
    if not isinstance(payload_aula, dict):
        return ""

    tema = payload_aula.get("tema_global") or payload_aula.get("tema") or "Aula"
    paginas = payload_aula.get("paginas_conteudo") or []
    
    titulos_subtopicos = []
    formulas_mencionadas = []
    exemplos_cenarios = []

    for p in paginas:
        if isinstance(p, dict):
            if p.get("titulo_subtopico"):
                titulos_subtopicos.append(p["titulo_subtopico"])
            if p.get("formalismo_latex"):
                formulas_mencionadas.append(str(p["formalismo_latex"])[:100])
            for ex in p.get("exemplos_praticos_ricos", []):
                if isinstance(ex, dict) and ex.get("contexto_e_enunciado"):
                    exemplos_cenarios.append(str(ex["contexto_e_enunciado"])[:120])

    resumo = f"### [MEMÓRIA DE AULA CONCLUÍDA: {tema}]\n"
    resumo += f"- Subtópicos apresentados: {', '.join(titulos_subtopicos)}\n"
    if formulas_mencionadas:
        resumo += f"- Fórmulas principais introduzidas: {'; '.join(formulas_mencionadas[:4])}\n"
    if exemplos_cenarios:
        resumo += f"- Cenários dos exemplos aplicados: {'; '.join(exemplos_cenarios[:3])}\n"
    resumo += "- Ponto de parada: Conteúdo e deduções deste tópico foram finalizados e aprovados.\n"
    
    return resumo

if __name__ == "__main__":
    print("[AVISO] O processo editorial deve ser executado a partir da interface do Streamlit.")
    print("Por favor, execute o comando: streamlit run app.py")
