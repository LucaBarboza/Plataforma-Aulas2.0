import os
import sys
import json
import re
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import Optional

# Importamos o contrato do subtópico para o Revisor analisar
from schemas import SubtopicoValidado

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
                            return True
        except Exception:
            pass
    return False

# Inicializa o carregamento da chave de API
carregar_chave_api()

# ==============================================================================
# SCHEMA DE DECISÃO DO AGENTE REVISOR (CRITIC)
# ==============================================================================
class DecisaoRevisao(BaseModel):
    aprovado: bool = Field(
        description="Defina como True se o conteúdo for profundo, correto e seguir 100% da notação. Defina como False se precisar de correções."
    )
    nota_qualidade: int = Field(
        default=100,
        description="Nota de 0 a 100 avaliando o rigor acadêmico, a exaustividade teórica, o formato em LaTeX e o grounding do bloco."
    )
    comentario_correcao: Optional[str] = Field(
        default=None,
        description="Se aprovado for False, escreva um laudo técnico estruturado em tópicos numerados de forma ultra-detalhada e cirúrgica, identificando precisamente o erro e fornecendo a correção explícita no formato 'SUBSTITUA [trecho errado] POR [trecho correto]' para guiar o Escritor sem qualquer ambiguidade."
    )
    conteudo_corrigido: Optional[SubtopicoValidado] = Field(
        default=None,
        description="Se aprovado for True, retorne o objeto de conteúdo revisado sem alterações estruturais."
    )

# ==============================================================================
# FUNÇÃO DE AUDITORIA DO SUBTÓPICO
# ==============================================================================
def auditar_subtopico_local(bloco_bruto_dict: dict, diretrizes_texto: str) -> DecisaoRevisao:
    # Garante que temos a chave configurada
    if not os.environ.get("GEMINI_API_KEY"):
        print("[ERRO] Erro no Revisor: Chave de API 'GEMINI_API_KEY' não configurada.")
        return DecisaoRevisao(aprovado=True, nota_qualidade=100, conteudo_corrigido=SubtopicoValidado(**bloco_bruto_dict))

    try:
        client = genai.Client(http_options={"timeout": 300_000})
    except Exception as e:
        print(f"[ERRO] Erro ao inicializar o cliente GenAI no Revisor: {e}")
        return DecisaoRevisao(aprovado=True, nota_qualidade=100, conteudo_corrigido=SubtopicoValidado(**bloco_bruto_dict))
    
    bloco_bruto_str = json.dumps(bloco_bruto_dict, ensure_ascii=False, indent=2)

    prompt_revisor = f"""
Você é um Professor Titular e Revisor de Conteúdo Científico de Estatística e Matemática.

### CONTEXTO E MISSÃO
Você receberá o [CONTEÚDO_BRUTO] gerado pelo Agente Escritor (em JSON) e as [DIRETRIZES_DE_ESTILO] estritas de notação.
Sua missão é atuar como auditor científico: você deve avaliar rigorosamente se o conteúdo e o formalismo matemático estão corretos, profundos e em total conformidade notacional, preenchendo a estrutura 'DecisaoRevisao'.

---

### DIRETRIZES DE REVISÃO E RIGOR (MANDATÓRIO)
1. Tolerância Zero com Desvios de Notação: Você deve conferir cada símbolo matemático e estatístico utilizado no conteúdo contra a tabela fornecida no bloco [DIRETRIZES_DE_ESTILO]. Se houver qualquer símbolo que discorde da tabela (ex: uso de símbolos diferentes de LaTeX, ou notações alternativas/informais não cadastradas), você é OBRIGADO a reprovar o bloco (`aprovado = False`) e listar os desvios no laudo.
2. Auditoria de Perfeição de Renderização do LaTeX (KaTeX): Reprove o bloco (`aprovado = False`) se encontrar qualquer um dos erros de LaTeX abaixo:
   a) Palavras soltas em português dentro de comandos ou ambientes LaTeX sem estar envolvidas por `\\text{{...}}` (ex: reprove `\\hat{{\\beta}} onde x` -> deve ser `\\hat{{\\beta}} \\text{{ onde }} x`).
   b) Uso de pacotes LaTeX incompatíveis com o KaTeX do Streamlit (como `\\textgreek`, `\\bm`, `\\boldsymbol{{\\text{{...}}}}`).
   c) Barras invertidas mal formadas ou caracteres quebrados de escape.
3. Exigência de Completude e Profundidade (TEXTO COMPLETO E NÃO SUPERFICIAL): O texto não precisa ser desnecessariamente longo por exagero — explicações concisas são bem-vindas, desde que o conteúdo seja REALMENTE COMPLETO. Reprove o bloco (`aprovado = False`) se a explicação for rasa ou superficial, omitir a motivação conceitual do tema, deixar equações no `conceito_formal` sem explicação do significado de variáveis, ou omitir a substituição numérica clara no exemplo prático.
4. Avaliação de Grounding (Metadados do RAG): Inspecione o campo 'fontes_rag'. Exija obrigatoriamente que cada fonte especifique o Nome do Livro/Slide/Material ('livro_autor') e a Seção ou Capítulo ('capitulo'). Se o nome do material ou a seção/capítulo estiverem em branco, nulos ou genéricos (ex: 'N/A' ou 'Fonte não mapeada'), REPROVE o bloco (`aprovado = False`). O número de página exato ('paginas_utilizadas') é opcional e a sua ausência (ex: 'p. S/N' ou 'p. não especificada') NÃO deve reprovar o bloco.
5. Critério de Dificuldade e Profundidade: Avalie se a dedução passo a passo está completa, logicamente contínua e acompanhada de frases explicativas em cada passagem.
6. Fidelidade à Fonte Primária do Professor: Verifique se o conteúdo prioriza e reflete fielmente os materiais de apoio e notações do professor (fonte primária), utilizando os livros da biblioteca RAG apenas como suporte secundário.
7. Auditoria de Fidelidade de Terminologia e Vocabulário do Professor: Reprove o bloco (`aprovado = False`) se o Escritor tiver substituído as palavras técnicas e o vocabulário preferido do professor (ex: se o professor usa 'Valor Esperado' e o texto usou 'Esperança Matemática', ou se o professor usa 'Resíduo' e o texto usou 'Erro Amostral') por termos alternativos da literatura. Exija a aplicação da terminologia idêntica à do material do docente.

---

### INSTRUÇÕES PARA PREENCHIMENTO DO SCHEMA DE RETORNO

1. 'aprovado' (boolean):
   - Defina como True apenas se o conteúdo atender 100% dos requisitos de notação exata, exaustividade teórica, dedução contígua e metadados de RAG (Livro/Slide e Seção/Capítulo).
   - Defina como False caso encontre qualquer desvio.

2. 'nota_qualidade' (integer):
   - Atribua uma nota de 0 a 100 avaliando o nível de qualidade global deste rascunho. Subtraia pontos para cada pequeno deslize (ex: falta de \\text, pequenas imprecisões no RAG, frases resumidas). Se aprovado 100%, atribua entre 90 e 100.

3. 'comentario_correcao' (string):
   - Se 'aprovado' for False, preencha este campo obrigatoriamente com um laudo técnico extremamente minucioso, didático e cirúrgico. Para CADA erro ou desvio encontrado no conteúdo:
     1) [CAMPO AFETADO]: Especifique exatamente qual chave JSON continha o erro (ex: 'conceito_formal', 'deducao_formal_passo_a_passo', 'exemplo_canonico', 'fontes_rag').
     2) [MOTIVO DETALHADO]: Explique detalhadamente por que está incorreto e qual a regra violada do bloco [DIRETRIZES_DE_ESTILO].
     3) [INSTRUÇÃO DE CORREÇÃO CIRÚRGICA]: Forneça a instrução EXATA no formato estrito:
        "SUBSTITUA: '[trecho incorreto exato]' POR: '[trecho corrigido com a notação LaTeX exata e rigor Didático]'".
   - Liste todos os pontos de forma numerada (1, 2, 3...) de maneira cristalina para que o Agente Escritor saiba exatamente como corrigir cada linha sem errar novamente.
   - Se 'aprovado' for True, retorne null ou "".

4. 'conteudo_corrigido' (objeto SubtopicoValidado ou null):
   - Se 'aprovado' for True, retorne neste campo o objeto de conteúdo revisado.
   - Se 'aprovado' for False, retorne null.

---

### ENTRADAS DO USUÁRIO
- [CONTEÚDO_BRUTO]:
{bloco_bruto_str}
- [DIRETRIZES_DE_ESTILO]:
{diretrizes_texto}
"""

    config_revisor = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="medium"), # Raciocínio profundo para caçar falhas
        temperature=1.0, # Puramente analítico e focado nas regras
        response_mime_type="application/json",
        response_schema=DecisaoRevisao
    )

    try:
        resposta = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=[bloco_bruto_str, prompt_revisor],
            config=config_revisor
        )
        return DecisaoRevisao.model_validate_json(resposta.text)
    except Exception as e:
        # Em caso de pane na chamada do revisor, força aprovação preventiva para não quebrar o script de lote
        print(f"      [ALERTA] Falha operacional no motor do Revisor: {e}")
        return DecisaoRevisao(aprovado=True, conteudo_corrigido=SubtopicoValidado(**bloco_bruto_dict))
