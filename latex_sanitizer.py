import re

# Padrão Regex extremamente preciso que encontra comandos LaTeX matemáticos
# que perderam a barra invertida inicial '\' durante a desserialização do JSON.
LATEX_COMMANDS_PATTERN = re.compile(
    r'(?<![a-zA-Z\\])(varepsilon|alpha|beta|gamma|delta|epsilon|zeta|eta|theta|vartheta|iota|kappa|lambda|mu|nu|xi|pi|varpi|rho|varrho|sigma|varsigma|tau|upsilon|phi|varphi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega|frac|sum|prod|int|iint|iiint|oint|sqrt|lim|log|ln|exp|max|min|sup|inf|det|dim|ker|hat|widehat|bar|tilde|widetilde|vec|dot|ddot|check|breve|acute|grave|infty|partial|nabla|cdot|times|div|pm|mp|le|leq|ge|geq|neq|approx|sim|simeq|equiv|in|notin|subset|subseteq|supset|supseteq|cap|cup|forall|exists|nexists|to|rightarrow|Rightarrow|leftarrow|Leftarrow|leftrightarrow|Leftrightarrow|quad|qquad|mathbf|boldsymbol|mathrm|mathcal|mathbb)(?=[^a-zA-Z]|$)'
)

def sanitizar_string_latex(texto: str) -> str:
    """Restaura barras invertidas ausentes em símbolos e comandos LaTeX matemáticos."""
    if not isinstance(texto, str) or not texto.strip():
        return texto

    # Restaura barras invertidas ausentes em comandos e letras gregas
    texto_corrigido = LATEX_COMMANDS_PATTERN.sub(r'\\\1', texto)

    return texto_corrigido

def sanitizar_payload_latex(obj):
    """Percorre recursivamente um dicionário, lista ou string e aplica a sanitização de LaTeX em todos os campos de texto."""
    if isinstance(obj, str):
        return sanitizar_string_latex(obj)
    elif isinstance(obj, dict):
        return {k: sanitizar_payload_latex(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sanitizar_payload_latex(item) for item in obj]
    return obj
