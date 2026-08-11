import sys
import re

sys.setrecursionlimit(10000)

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

def sanitizar_payload_latex(obj, visited=None):
    """Percorre recursivamente um dicionário, lista ou string e aplica a sanitização de LaTeX com limite de profundidade seguro."""
    if visited is None:
        visited = set()

    if isinstance(obj, str):
        return sanitizar_string_latex(obj)

    if not isinstance(obj, (dict, list, tuple, set)):
        return obj

    obj_id = id(obj)
    if obj_id in visited:
        return obj

    visited.add(obj_id)

    if isinstance(obj, dict):
        res = {}
        for k, v in obj.items():
            key_san = sanitizar_string_latex(k) if isinstance(k, str) else k
            res[key_san] = sanitizar_payload_latex(v, visited)
        return res
    elif isinstance(obj, list):
        return [sanitizar_payload_latex(item, visited) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(sanitizar_payload_latex(item, visited) for item in obj)
    elif isinstance(obj, set):
        return {sanitizar_payload_latex(item, visited) for item in obj}
    
    return obj

