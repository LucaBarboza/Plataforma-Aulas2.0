import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDQgLSBUw7NwaWNvIDQuMjogTyB1c28gZGUgbWF0cml6IGludmVyc2EgZ2VuZXJhbGl6YWRhIiwgInJlZmVyZW5jaWFzX2JpYmxpb2dyYWZpY2FzX2ZpbmFpcyI6IFsiTHVuYSAmIEVzdGV2ZXMsIEludHJvZHXDp8OjbyBhb3MgTW9kZWxvcyBMaW5lYXJlcyAtIENhcC4gMS0yLCBwcC4gMzgtOTgiLCAiQmlzcG8sIE7DrXZlYSAtIE1hdGVyaWFsIGRlIEF1bGEgKERFU1QtVUZCQSksIEF1bGEgOTogSW52ZXJzYSBHZW5lcmFsaXphZGEgZGUgTWF0cml6ZXMsIHBwLiAyLTgiXX0=').decode('utf-8'))

# Injeção de Estilos CSS Acadêmicos Premium
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        /* Aplicar fonte premium */
        html, body, [class*="css"], .stApp {
            font-family: 'Outfit', 'Segoe UI', sans-serif;
        }
        
        .premium-title { 
            font-size: 2.5rem; 
            font-weight: 800; 
            background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2rem; 
        }
        .premium-subtitle { 
            font-size: 1.15rem; 
            color: #64748B; 
            margin-bottom: 1.8rem; 
            font-style: italic; 
        }
        
        /* Tabs da Aula */
        div[data-baseweb="tab-list"] {
            gap: 12px;
        }
        button[data-baseweb="tab"] {
            border-radius: 8px 8px 0 0 !important;
            background-color: #F8FAFC !important;
            border: 1px solid #E2E8F0 !important;
            border-bottom: none !important;
            color: #475569 !important;
            padding: 10px 20px !important;
            font-weight: 500 !important;
        }
        button[aria-selected="true"] {
            background-color: #FFFFFF !important;
            border-top: 3px solid #1E3A8A !important;
            color: #0F172A !important;
            font-weight: 600 !important;
        }
        
        /* Estilização de Containers de Conteúdo e Exemplo */
        div[data-testid="stVerticalBlock"] > div[style*="border"] {
            border-radius: 12px !important;
            border: 1px solid #E2E8F0 !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03), 0 2px 4px -2px rgba(0, 0, 0, 0.03) !important;
            background-color: #FFFFFF !important;
            padding: 1.5rem !important;
            margin-bottom: 1.5rem !important;
        }
        
        /* Estilização das caixas st.info, st.success, etc. */
        div.stAlert {
            border-radius: 10px !important;
            border: 1px solid rgba(0, 0, 0, 0.05) !important;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02) !important;
        }
        
        /* Estilização do progresso */
        div.stProgress > div {
            background-color: #E2E8F0 !important;
            border-radius: 10px !important;
            height: 10px !important;
        }
        div.stProgress > div > div {
            background: linear-gradient(90deg, #1E3A8A 0%, #10B981 100%) !important;
            border-radius: 10px !important;
        }
        
        /* Inputs e Sliders na aula */
        div.stSlider [data-testid="stSliderTickBar"] {
            background-color: #1E3A8A !important;
        }
        
        /* Botões na aula */
        div.stButton > button {
            background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%) !important;
            color: white !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 0.5rem 1.2rem !important;
            font-weight: 600 !important;
            transition: all 0.2s ease !important;
        }
        div.stButton > button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown(f'<div class="premium-title">{metadata["tema_global"]}</div>', unsafe_allow_html=True)
st.markdown('<div class="premium-subtitle">Conteúdo Acadêmico Digital e Simuladores Integrados</div>', unsafe_allow_html=True)

# Definição de Cores Globais da Paleta Premium
PRIMARY_BLUE = "#1E3A8A"
SECONDARY_GREEN = "#10B981"
WARNING_AMBER = "#F59E0B"
CRITICAL_RED = "#991B1B"

# Criação das Duas Grandes Abas Globais
tab_conteudo, tab_exercicios = st.tabs(["📚 Conteúdo Acadêmico Interativo", "📝 Caderno de Exercícios"])

with tab_conteudo:

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    
    # Cabeçalho do Subtópico
    st.header(r"Limitações da Inversão Tradicional em Modelos Lineares")
    
    # Prosa Teórica - Parte 1
    st.markdown(r"""
    No domínio da modelagem linear, o objetivo fundamental reside em estimar o vetor de parâmetros desconhecidos, $\theta$, por meio da resolução do sistema de equações normais. Sob a premissa de que a matriz do modelo possui colunas linearmente independentes, assegura-se que a matriz dos produtos cruzados seja de posto coluna completo, garantindo assim sua inversibilidade.
    """)
    
    st.info(r"Entretanto, em contextos práticos de experimentação, é frequente encontrarmos restrições de delineamento ou multicolinearidade que induzem a singularidade desta matriz. Nesses cenários, o determinante da matriz torna-se nulo, impossibilitando a obtenção da inversa tradicional.")
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Equações Normais")
    st.markdown(r"A resolução do sistema de mínimos quadrados ordinários é governada pela equação matricial abaixo:")
    st.latex(r"(X^{\top}X)\theta = X^{\top}y")
    
    # Dedução Analítica
    st.markdown(r"A dedução do problema de singularidade segue a lógica sequencial apresentada:")
    st.latex(r"y = X\theta + e")
    st.markdown(r"Multiplicando pela transposta da matriz $X$ e assumindo a ortogonalidade dos resíduos:")
    st.latex(r"X^{\top}y = X^{\top}X\theta + X^{\top}e")
    st.latex(r"X^{\top}y = X^{\top}X\theta")
    st.markdown(r"Quando as variáveis explicativas não são linearmente independentes, a estrutura da matriz $X^{\top}X$ colapsa:")
    st.latex(r"\det(X^{\top}X) = 0")
    st.latex(r"\nexists (X^{\top}X)^{-1}")
    
    # Simulador Interativo: Visualizador de Posto de Matriz
    st.markdown(r"### 🎛️ Simulador: Visualizador de Posto de Matriz")
    st.markdown(r"Altere os valores da matriz $3 \times 3$ abaixo para observar como a dependência linear entre as colunas afeta o determinante e a capacidade de inversão.")
    
    col1, col2, col3 = st.columns(3)
    m11 = col1.number_input(r"M[0,0]", value=1.0, key=r"m11_subtopico_1")
    m12 = col2.number_input(r"M[0,1]", value=1.0, key=r"m12_subtopico_1")
    m13 = col3.number_input(r"M[0,2]", value=0.0, key=r"m13_subtopico_1")
    m21 = col1.number_input(r"M[1,0]", value=1.0, key=r"m21_subtopico_1")
    m22 = col2.number_input(r"M[1,1]", value=1.0, key=r"m22_subtopico_1")
    m23 = col3.number_input(r"M[1,2]", value=0.0, key=r"m23_subtopico_1")
    m31 = col1.number_input(r"M[2,0]", value=1.0, key=r"m31_subtopico_1")
    m32 = col2.number_input(r"M[2,1]", value=0.0, key=r"m32_subtopico_1")
    m33 = col3.number_input(r"M[2,2]", value=1.0, key=r"m33_subtopico_1")
    
    matriz_x = np.array([[m11, m12, m13], [m21, m22, m23], [m31, m32, m33]])
    det_val = np.linalg.det(matriz_x)
    rank_val = np.linalg.matrix_rank(matriz_x)
    
    fig = go.Figure(data=[go.Heatmap(z=matriz_x, colorscale='Blues')])
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Visualização da Matriz X</b>", font=dict(size=14, color="#1E293B"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Colunas", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", fixedrange=True),
        yaxis=dict(title=dict(text="Linhas", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", fixedrange=True)
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    # Laudo Dinâmico
    if abs(det_val) < 1e-6:
        st.error(rf"Determinante: {det_val:.4f} | Posto: {rank_val}. Matriz Singular: A inversão tradicional não é possível.")
    else:
        st.success(rf"Determinante: {det_val:.4f} | Posto: {rank_val}. Matriz não singular: Solução possível.")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática: Delineamento Desbalanceado")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Experimento de Três Tratamentos")
        st.markdown(r"Considere um experimento onde a soma das colunas de tratamentos é igual à coluna do intercepto.")
        st.latex(r"X = \begin{pmatrix} 1 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 \\ 1 & 0 & 1 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- A matriz de produtos cruzados resulta em $X^{\top}X$ com determinante nulo.")
        st.markdown(r"- Verifica-se a dependência linear: $C_1 = C_2 + C_3 + C_4$.")
        
        st.success(r"Conclusão: A singularidade detectada impede o uso do método de mínimos quadrados ordinários convencional, pois o sistema não possui uma solução única. Requer-se a imposição de restrições paramétricas adicionais.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Definição e Condições da Inversa Generalizada")
    
    # Introdução
    st.markdown(r"""
    Na jornada da álgebra linear aplicada à estatística, um dos obstáculos mais persistentes é a inversibilidade de matrizes. 
    Enquanto a inversão clássica exige posto pleno e determinante não nulo, a realidade dos modelos lineares complexos 
    frequentemente nos apresenta matrizes singulares.
    """)
    
    st.markdown(r"""
    A **inversa generalizada** (ou $g$-inversa) surge como a solução para este dilema, permitindo extrair inferências 
    estatísticas mesmo em sistemas colineares ou com redundância de dados.
    """)
    
    # Bloco conceitual sobre a natureza da g-inversa
    st.warning(r"A motivação fundamental para o uso de uma inversa generalizada reside na resolução de sistemas consistentes sem solução única. Ela não tenta recuperar informações perdidas pelo 'achatamento' de dimensões da matriz, mas sim preservar a estrutura de mapeamento possível.")
    
    # Formalismo
    st.markdown(r"### 📐 O Coração Matemático: Critério de Consistência")
    st.markdown(r"Uma matriz $A^{-}$ é definida como inversa generalizada de $A$ se, e somente se, satisfaz a condição:")
    st.latex(r"A A^{-} A = A")
    
    st.markdown(r"""
    Esta expressão garante que o produto $A A^{-}$ atua como um projetor sobre o espaço coluna de $A$. 
    Diferente da inversa clássica ($A A^{-1} = I$), a inversa generalizada não exige identidade, 
    mas sim que o mapeamento final seja consistente com a estrutura original do sistema.
    """)
    
    # Dedução Analítica
    st.markdown(r"### 🔍 Dedução da Solução do Sistema")
    st.markdown(r"Considere o sistema linear abaixo onde $A$ é singular:")
    st.latex(r"Ax = g")
    
    st.markdown(r"Ao multiplicarmos pela inversa generalizada, preservamos a consistência:")
    st.latex(r"A A^{-} A x = A x")
    
    st.markdown(r"Substituindo e rearranjando, obtemos a estrutura de solução geral:")
    st.latex(r"A (A^{-} A x) = g")
    
    st.markdown(r"A solução geral para o vetor de parâmetros é dada por:")
    st.latex(r"x = A^{-} g + (I - A^{-} A)z")
    st.markdown(r"Onde $z$ representa qualquer vetor arbitrário, evidenciando que a não-unicidade é inerente ao sistema.")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Redundância de Variáveis")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Sistema Singular Simples")
        st.markdown(r"""
        Em um cenário onde observamos redundância total entre variáveis explicativas, temos a matriz de delineamento 
        e o vetor de resultados definidos como:
        """)
        st.latex(r"A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}, \quad g = \begin{pmatrix} 2 \\ 2 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"""
        - **Passo 1:** Assumimos uma matriz genérica $A^{-} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$.
        - **Passo 2:** Aplicamos a condição $A A^{-} A = A$, o que impõe a restrição $a+b+c+d=1$.
        - **Passo 3:** Escolhemos uma das infinitas soluções, como $a=1$ e $b=c=d=0$, obtendo $A^{-} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.
        - **Passo 4:** Calculamos o estimador $\theta = A^{-}g$.
        """)
        
        st.success(r"O resultado obtido é $\theta = (2, 0)^{\top}$, que satisfaz o sistema e demonstra como a inversa generalizada contorna a singularidade para permitir a estimação.")
    
    # Conclusão Didática
    st.info(r"Ao utilizar a inversa generalizada, o pesquisador aceita que o parâmetro populacional pode ser inidentificável, mas garante a obtenção de um estimador não viciado de uma combinação linear estimável, mantendo o rigor inferencial.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    
    # Cabeçalho Acadêmico
    st.header(r"A Inversa de Moore-Penrose: Existência e Unicidade")
    
    # Introdução
    st.markdown(r"""
    A busca pela inversibilidade de operadores lineares é um pilar da Álgebra Linear aplicada, sendo fundamental para resolver sistemas lineares na Estatística e Econometria. 
    Historicamente, a inversa clássica $A^{-1}$ é definida apenas para matrizes quadradas não singulares. Contudo, em modelos com multicolinearidade ou sistemas sobredeterminados, precisamos de uma extensão robusta.
    """)
    
    st.markdown(r"""
    A inversa de Moore-Penrose, $A^{+}$, supera as limitações das matrizes singulares ou retangulares, oferecendo:
    - **Unicidade absoluta** através das quatro condições de Penrose.
    - **Minimização de resíduos** em sistemas sobredeterminados.
    - **Estabilidade numérica** superior em algoritmos de estimação.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: As Condições de Penrose")
    st.markdown(r"A elegância do formalismo de Moore-Penrose reside em quatro condições rigorosas que garantem a unicidade da solução:")
    
    st.latex(r"A A^+ A = A")
    st.latex(r"A^+ A A^+ = A^+")
    st.latex(r"(A A^+)^{\top} = A A^+")
    st.latex(r"(A^+ A)^{\top} = A^+ A")
    
    st.markdown(r"Estas condições definem a pseudoinversa como uma projeção ortogonal, permitindo o cálculo do estimador de variância mínima, conforme estabelecido abaixo:")
    st.latex(r"\hat{\theta} = (X^{\top}X)^+ X^{\top}y")
    
    # Simulador Interativo
    st.subheader(r"🎯 Simulador: Projeção de Moore-Penrose")
    st.markdown(r"Explore como a pseudoinversa projeta um vetor $y$ no espaço coluna de uma matriz singular $A$.")
    
    col1, col2 = st.columns(2)
    with col1:
        y1 = st.slider(r"Valor y1", -5.0, 5.0, 2.0, key=r"y1_subtopico_3")
        y2 = st.slider(r"Valor y2", -5.0, 5.0, 1.0, key=r"y2_subtopico_3")
    with col2:
        singular_val = st.toggle(r"Matriz Singular", value=True, key=r"singular_toggle_subtopico_3")
    
    # Cálculo do simulador
    y = np.array([y1, y2])
    if singular_val:
        A = np.array([[1, 0], [0, 0]])
    else:
        A = np.array([[1, 0.5], [0.5, 0.25]]) # Aproximação de singularidade
    
    A_pinv = np.linalg.pinv(A)
    y_proj = A @ (A_pinv @ y)
    
    # Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, y[0]], y=[0, y[1]], name=r"Vetor Original", line=dict(color="#64748B", dash="dot")))
    fig.add_trace(go.Scatter(x=[0, y_proj[0]], y=[0, y_proj[1]], name=r"Projeção (Moore-Penrose)", line=dict(color="#1E3A8A", width=3)))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Visualização da Projeção de Moore-Penrose</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Eixo X", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Eixo Y", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    st.info(f"O vetor foi projetado no espaço imagem de A. A norma resultante é {np.linalg.norm(y_proj):.2f}, minimizando a distância euclidiana para qualquer vetor no espaço coluna.")
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática: Inversa de Moore-Penrose")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Sistema Singular Simples")
        st.markdown(r"Considere o sistema $A\theta = g$ onde $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ e $g = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$.")
        st.latex(r"A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad g = \begin{pmatrix} 2 \\ 0 \end{pmatrix}")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Para matrizes diagonais, inverte-se apenas elementos não nulos.")
        st.markdown(r"- A pseudoinversa resulta na própria matriz: $A^+ = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.")
        st.markdown(r"- O estimador é calculado via $\hat{\theta} = A^+ g$.")
        st.success(r"O estimador $\hat{\theta} = (2, 0)^{\top}$ é a solução de norma mínima que minimiza a variância dos parâmetros, essencial para estabilidade em colinearidade.")

    # Módulo de Conteúdo Acadêmico: Algoritmos e Métodos de Cálculo da Inversa Generalizada
    
    st.header(r"Algoritmos e Métodos de Cálculo da Inversa Generalizada")
    
    st.markdown(r"""
    A álgebra matricial atua como a espinha dorsal da estatística multivariada e da teoria dos modelos lineares. Em cenários onde a multicolinearidade perfeita ou a natureza estrutural dos dados impõe uma singularidade à matriz, a inversa convencional deixa de existir.
    """)
    
    st.info(r"A inversa generalizada, denotada por $A^{-}$, permite que extraiam-se soluções consistentes mesmo em espaços onde a informação é redundante, superando a barreira da singularidade.")
    
    st.markdown(r"""
    ### ⚙️ A Metodologia de Searle e a Decomposição Estrutural
    O método de Searle é uma técnica notável por sua clareza procedimental. A lógica fundamental reside na premissa de que qualquer matriz $A$ ($n \times n$) de posto $r < n$ possui uma subestrutura informativa:
    
    * **Identificação de Submatrizes:** Rearranjamos a matriz para isolar uma submatriz $M$ de posto pleno $r$.
    * **Núcleo Operacional:** A submatriz $M$ atua como o núcleo, sendo invertível e retendo a essência do espaço coluna original.
    * **Projeção:** Ao invertermos apenas $M$, ignoramos direções redundantes no espaço de parâmetros.
    """)
    
    st.subheader(r"📐 Formalismo e Estrutura da Inversa")
    
    st.latex(r"A^{-} = \begin{pmatrix} M^{-1} & 0 \\ 0 & 0 \end{pmatrix}")
    
    st.markdown(r"""
    Nesta configuração, a inversa generalizada projeta o vetor de observações de forma ortogonal sobre o espaço coluna, garantindo que o sistema $A\beta = Y$ possua ao menos uma solução na forma $\hat{\beta} = A^{-}Y$.
    """)
    
    st.subheader(r"🔍 Demonstração Analítica da Existência")
    
    st.markdown(r"Considere a decomposição de posto $A = BC$. A construção de $A^{-}$ segue a relação abaixo:")
    st.latex(r"A^{-} = C^{\top}(CC^{\top})^{-1}(B^{\top}B)^{-1}B^{\top}")
    
    st.markdown(r"Verificamos a condição fundamental de consistência:")
    st.latex(r"AA^{-}A = B(CC^{\top})(CC^{\top})^{-1}(B^{\top}B)^{-1}(B^{\top}B)C")
    st.latex(r"AA^{-}A = BC = A")
    
    st.subheader(r"📈 Casos de Aplicação Prática: Inversa de Searle")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Cálculo via Partição de Posto Pleno")
        st.markdown(r"Utilize o algoritmo de Searle para encontrar a inversa generalizada de $A$ (posto 2):")
        st.latex(r"A = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Extrair a submatriz de posto pleno $M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$.")
        st.markdown(r"- Calcular a inversa da submatriz: $M^{-1} = \begin{pmatrix} 0 & 1 \\ 1 & -1 \end{pmatrix}$.")
        st.markdown(r"- Compor a inversa generalizada $A^{-}$ inserindo $M^{-1}$ no quadrante superior e completando com nulos.")
        
        st.latex(r"A^{-} = \begin{pmatrix} 0 & 1 & 0 \\ 1 & -1 & 0 \\ 0 & 0 & 0 \end{pmatrix}")
        
        st.success(r"Laudo: A matriz calculada satisfaz a propriedade $AA^{-}A = A$, provendo uma solução robusta para o sistema sem necessidade de inversão direta da matriz singular.")
    
    st.markdown(r"""
    ---
    ### 💡 Nota Pedagógica
    A escolha de $A^{-}$ não é única, exceto sob condições restritas como as de Moore-Penrose. Na prática estatística, a flexibilidade desta construção permite que modelos com preditores colineares sejam computados com eficiência, transformando a singularidade em uma característica da geometria dos dados, e não em um erro absoluto do sistema.
    """)

    # Cabeçalho do Subtópico
    st.header(r"Aplicações em Sistemas Lineares e Modelos de Posto Incompleto")
    
    # Introdução Estruturada
    st.markdown(r"""
    No estudo da estatística inferencial e da modelagem linear, frequentemente somos confrontados com a hipótese de posto completo. No entanto, ao avançarmos para análises mais complexas — como em modelos de ANOVA com múltiplos fatores ou situações de multicolinearidade severa —, deparamo-nos com a realidade matemática dos **modelos de posto incompleto**.
    """)
    
    st.info(r"Nesses cenários, a matriz de informação $X^{\top}X$ torna-se singular (determinante nulo), impedindo a inversão convencional. Esta singularidade não é um erro de cálculo, mas uma característica do design experimental.")
    
    st.markdown(r"""
    A introdução da **inversa generalizada** $(X^{\top}X)^{-}$ permite operar sobre o espaço das soluções, mesmo quando este não é unívoco. A lógica fundamental é que, embora o vetor de parâmetros $\beta$ possa não ser identificável de forma única, o subespaço gerado pelas colunas de $X$ permanece inalterado.
    """)
    
    # O Coração Matemático: Dedução Analítica
    st.markdown(r"### 📐 O Coração Matemático: Estimação e Predição")
    
    st.markdown(r"A projeção do vetor de resposta $y$ sobre o espaço coluna de $X$ é um operador linear estável. O processo analítico segue estes passos:")
    
    st.latex(r"X^{\top}X\hat{\theta} = X^{\top}y")
    st.markdown(r"Partindo das equações normais, aplicamos a inversa generalizada:")
    st.latex(r"\hat{\theta} = (X^{\top}X)^{-}X^{\top}y")
    st.markdown(r"O valor predito é a projeção no espaço das observações:")
    st.latex(r"\hat{y} = X\hat{\theta}")
    st.markdown(r"Resultando no operador de projeção $P$:")
    st.latex(r"\hat{y} = P y")
    
    st.success(r"A elegância deste formalismo reside no fato de que $\hat{y}$ é invariante, independentemente da inversa generalizada escolhida. Isso garante robustez à decisão estratégica.")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Invariância na Predição")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Matriz de Redundância")
        st.markdown(r"Considere o vetor $y = (10, 12, 14, 16)^{\top}$ e a matriz de desenho $X$ com redundância estrutural.")
        
        st.latex(r"X = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & 0 & 1 \end{pmatrix}, y = \begin{pmatrix} 10 \\ 12 \\ 14 \\ 16 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Primeiro, calculamos a matriz de informação: $X^{\top}X = \begin{pmatrix} 4 & 2 & 2 \\ 2 & 2 & 0 \\ 2 & 0 & 2 \end{pmatrix}$")
        st.markdown(r"- Aplicando a inversa generalizada dada: $(X^{\top}X)^{-} = \text{diag}(0, 0.5, 0.5)$")
        st.markdown(r"- Calculamos o vetor de parâmetros: $\hat{\theta} = (X^{\top}X)^{-}X^{\top}y = (0, 11, 15)^{\top}$")
        st.markdown(r"- Finalizamos com a predição: $\hat{y} = X\hat{\theta} = (11, 11, 15, 15)^{\top}$")
        
        st.success(r"O vetor de predições é único. Este resultado demonstra que, mesmo em modelos com parâmetros não identificáveis, a previsão é perfeitamente definida e confiável para fins de suporte à decisão.")
    
    # Considerações Finais
    st.markdown(r"""
    ### 💡 Implicações para a Ciência de Dados
    O estatístico experiente reconhece que, ao manter a redundância e utilizar a álgebra de posto incompleto, preservamos a simetria da análise. 
    - **Robustez:** Evita a exclusão arbitrária de variáveis.
    - **Estimabilidade:** Permite avaliar contrastes de interesse mesmo em sistemas singulares.
    - **Flexibilidade:** A singularidade torna-se uma ferramenta, não um obstáculo.
    """)

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDQgLSBUw7NwaWNvIDQuMjogTyB1c28gZGUgbWF0cml6IGludmVyc2EgZ2VuZXJhbGl6YWRhIiwgInF1ZXN0b2VzX211bHRpcGxhX2VzY29saGEiOiBbeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIGVuZ2VuaGFyaWEgZGUgbWF0ZXJpYWlzLCB1bSBwZXNxdWlzYWRvciBkZXNlamEgbW9kZWxhciBhIHJlc2lzdMOqbmNpYSDDoCB0cmHDp8OjbyAoJHkkKSBkZSBwb2zDrW1lcm9zIGVtIGZ1bsOnw6NvIGRlIGRvaXMgdGlwb3MgZGUgYWRpdGl2b3MsIGNvZGlmaWNhZG9zIGNvbW8gdmFyacOhdmVpcyBpbmRpY2Fkb3JhcyAkeF8xJCBlICR4XzIkLiBEZXZpZG8gYSB1bWEgcmVzdHJpw6fDo28gZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlLCBvIHBlc3F1aXNhZG9yIGluY2x1aSB1bSBpbnRlcmNlcHRvICgkXGJcXGV0YV8wJCkgZSBkZWZpbmUgcXVlIG8gYWRpdGl2byDDqSBzZW1wcmUgdW0gb3Ugb3V0cm8sIHJlc3VsdGFuZG8gbmEgcmVzdHJpw6fDo28gJHhfMSArIHhfMiA9IDEkIHBhcmEgdG9kYXMgYXMgb2JzZXJ2YcOnw7Vlcy4gQ29uc2lkZXJhbmRvIG8gc2lzdGVtYSBkZSBlcXVhw6fDtWVzIG5vcm1haXMgJChYXntcdG9wfVgpXHRoZXRhID0gWF57XHRvcH15JCwgYXNzaW5hbGUgYSBhbHRlcm5hdGl2YSBxdWUgZGVzY3JldmUgY29ycmV0YW1lbnRlIG8gaW1wYWN0byBkZXNzYSByZXN0cmnDp8OjbyBuYSBtYXRyaXogZG8gbW9kZWxvICRYJCBlIG5vIHNpc3RlbWEgZGUgZXN0aW1hw6fDo28uIiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIG1hdHJpeiAkKFhee1x0b3B9WCkkIHNlcsOhIGRlIHBvc3RvIGNvbXBsZXRvLCBnYXJhbnRpbmRvIHF1ZSBvIGVzdGltYWRvciBkZSBtw61uaW1vcyBxdWFkcmFkb3Mgb3JkaW7DoXJpb3MgJFxcaGF0e1xcdGhldGF9JCBzZWphIMO6bmljbyBlIGNhbGN1bMOhdmVsIHBlbGEgaW52ZXJzYSB0cmFkaWNpb25hbC4iLCAiQiI6ICJBIG1hdHJpeiAkWCQgcG9zc3VpIGNvbHVuYXMgbGluZWFybWVudGUgZGVwZW5kZW50ZXMgZGV2aWRvIMOgIHJlc3RyacOnw6NvLCB0b3JuYW5kbyBvIGRldGVybWluYW50ZSBkZSAkKFhee1x0b3B9WCkkIGlndWFsIGEgemVybyBlIGltcG9zc2liaWxpdGFuZG8gYSBvYnRlbsOnw6NvIGRlIHVtYSDDum5pY2Egc29sdcOnw6NvIHBhcmEgJFxcdGhldGEkIHZpYSBpbnZlcnNhIHRyYWRpY2lvbmFsLiIsICJDIjogIkEgaW5jbHVzw6NvIGRvIGludGVyY2VwdG8gJFxcYmV0YV8wJCBzZW1wcmUgY29tcGVuc2EgYSBkZXBlbmTDqm5jaWEgbGluZWFyIGVudHJlICR4XzEkIGUgJHhfMiQsIGdhcmFudGluZG8gcXVlIG8gc2lzdGVtYSBzZWphIHBlcmZlaXRhbWVudGUgZGV0ZXJtaW5hZG8uIiwgIkQiOiAiTyBlcnJvICRlJCBzZXLDoSBudWxvIHBhcmEgdG9kYXMgYXMgb2JzZXJ2YcOnw7VlcywgaW5kZXBlbmRlbnRlbWVudGUgZG9zIHZhbG9yZXMgZGUgJFxcdGhldGEkLCBkZXZpZG8gw6Agc2luZ3VsYXJpZGFkZSBkYSBtYXRyaXouIiwgIkUiOiAiQSByZXN0cmnDp8OjbyAkeF8xICsgeF8yID0gMSQgbsOjbyBhZmV0YSBvIHBvc3RvIGRhIG1hdHJpeiwgbWFzIGFsdGVyYSBhIGVzY2FsYSBkb3MgcmVzw61kdW9zICRlX2kkLCB0b3JuYW5kbyBvIG1vZGVsbyBoZXRlcm9jZWTDoXN0aWNvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGNvbmRpw6fDo28gZGUgcG9zdG8gcGxlbm8gcGFyYSBhIGludmVyc8Ojbzogc2UgYXMgY29sdW5hcyBkYSBtYXRyaXogJFgkIG7Do28gc8OjbyBsaW5lYXJtZW50ZSBpbmRlcGVuZGVudGVzLCBvIHF1ZSBvY29ycmUgY29tIG8gZGV0ZXJtaW5hbnRlIGRlICQoWF57XFx0b3B9WCkkPyIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBkZXBlbmTDqm5jaWEgbGluZWFyICR4XzEgKyB4XzIgPSAxJCBpbXBsaWNhIHF1ZSB1bWEgY29sdW5hIGRhIG1hdHJpeiBwb2RlIHNlciBlc2NyaXRhIGNvbW8gY29tYmluYcOnw6NvIGxpbmVhciBkYSBvdXRyYSAoc29tYWRhIGFvIGludGVyY2VwdG8pLCByZWR1emluZG8gbyBwb3N0byBkZSAkWCQuIENvbW8gJHIoWCkgPCBtJCwgYSBtYXRyaXogZGUgcHJvZHV0b3MgY3J1emFkb3MgJChYXntcXHRvcH1YKSQgbsOjbyDDqSBpbnZlcnPDrXZlbCwgb3Ugc2VqYSwgJFxcZGV0KFhee1xcdG9wfVgpID0gMCQuIFBvcnRhbnRvLCBuw6NvIGV4aXN0ZSAkKFhee1xcdG9wfVgpXnstMX0kIMO6bmljYSwgaW1wb3NzaWJpbGl0YW5kbyBhIHNvbHXDp8OjbyBjb252ZW5jaW9uYWwgJFxcaGF0e1xcdGhldGF9ID0gKFhee1xcdG9wfVgpXnstMX1YXntcdG9wfXkkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTW9udGdvbWVyeSwgUGVjayAmIFZpbmluZywgSW50cm9kdWN0aW9uIFxcdG8gTGluZWFyIFJlZ3Jlc3Npb24gQW5hbHlzaXMsIENhcCAzIn0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBvbmRlIGEgbWF0cml6IGRlIGRlbGluZWFtZW50byAkWCQgKCRuPTEwLCBtPTMkKSBhcHJlc2VudGEgY29sdW5hcyBsaW5lYXJtZW50ZSBkZXBlbmRlbnRlcyB0YWwgcXVlIGEgY29sdW5hICR4XzMkIMOpIGEgc29tYSBkZSAkeF8xJCBlICR4XzIkLiBTZSB0ZW50YXJtb3MgcmVzb2x2ZXIgbyBzaXN0ZW1hIGRlIGVxdWHDp8O1ZXMgbm9ybWFpcyAkKFhee1x0b3B9WClcdGhldGEgPSBYXntcdG9wfXkkLCBxdWFsIMOpIGEgY29uc2VxdcOqbmNpYSBtYXRlbcOhdGljYSBkaXJldGEgc29icmUgYSBzb2x1w6fDo28gJFxcdGhldGEkPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyBzaXN0ZW1hIGFkbWl0ZSBleGF0YW1lbnRlIHVtYSBzb2x1w6fDo28gcXVlIG1pbmltaXphIG8gZXJybywgbWVzbW8gc2VuZG8gYSBtYXRyaXogc2luZ3VsYXIuIiwgIkIiOiAiQSBzb2x1w6fDo28gJFxcdGhldGEkIMOpIGluY29uc2lzdGVudGUgZSBvIHJlc8OtZHVvICRlJCBzZXLDoSBzZW1wcmUgbWFpb3IgcXVlIG8gdmFsb3Igb2JzZXJ2YWRvICR5JC4iLCAiQyI6ICJPIHNpc3RlbWEgw6kgaW5kZXRlcm1pbmFkbywgYWRtaXRpbmRvIGluZmluaXRhcyBzb2x1w6fDtWVzIHBhcmEgJFxcdGhldGEkLCB2aXN0byBxdWUgbsOjbyBleGlzdGUgdW1hIGludmVyc2Egw7puaWNhIHBhcmEgJChYXntcXHRvcH1YKSQuIiwgIkQiOiAiTyBkZXRlcm1pbmFudGUgZGUgJChYXntcXHRvcH1YKSQgdG9ybmEtc2UgbmVnYXRpdm8sIGluZGljYW5kbyBxdWUgbyBtb2RlbG8gw6kgaW52w6FsaWRvLiIsICJFIjogIkEgc2luZ3VsYXJpZGFkZSBhcGVuYXMgYWZldGEgbyBjw6FsY3VsbyBkbyBwLXZhbG9yLCBtYXMgbsOjbyBhIGVzdGltYcOnw6NvIGRvcyBwYXLDom1ldHJvcyAkXFx0aGV0YSQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJFbSB1bSBzaXN0ZW1hIGxpbmVhciAkQXg9YiQsIHNlICRBJCDDqSBzaW5ndWxhciwgYSBleGlzdMOqbmNpYSBkZSBzb2x1w6fDtWVzIGRlcGVuZGUgZG8gZXNwYcOnbyBjb2x1bmEgZGUgJEEkLiBBIGZhbHRhIGRlIHBvc3RvIGNvbXBsZXRvIHJlc3VsdGEgZW0gdW0gc3ViZXNwYcOnbyBkZSBzb2x1w6fDtWVzIHBvc3PDrXZlaXMuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJRdWFuZG8gJFgkIG7Do28gcG9zc3VpIHBvc3RvIGNvbHVuYSBjb21wbGV0bywgbyBzaXN0ZW1hICQoWF57XFx0b3B9WClcdGhldGEgPSBYXntcdG9wfXkkIMOpIHVtIHNpc3RlbWEgc2luZ3VsYXIuIEVtIMOhbGdlYnJhIGxpbmVhciwgc2lzdGVtYXMgc2luZ3VsYXJlcyBjb21wYXTDrXZlaXMgbsOjbyBwb3NzdWVtIHVtYSBzb2x1w6fDo28gw7puaWNhOyBlbGVzIHBvc3N1ZW0gaW5maW5pdGFzIHNvbHXDp8O1ZXMsIHBvaXMgZXhpc3RlIHVtIG7DumNsZW8gKG51bGwgc3BhY2UpIG7Do28gdHJpdmlhbC4gQSBhdXPDqm5jaWEgZGUgaW52ZXJzYSB0cmFkaWNpb25hbCAkKFhee1xcdG9wfVgpXnstMX0kIHJlZmxldGUgZXhhdGFtZW50ZSBlc3NhIGluZGV0ZXJtaW5hw6fDo28gZG8gcGFyw6JtZXRybyAkXFx0aGV0YSQuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKGRhdGE9W2dvLlNjYXR0ZXIoeD1bMCwgMSwgMl0sIHk9WzAsIDEsIDJdLCBtb2RlPSdsaW5lcyttYXJrZXJzJywgbmFtZT0nQ29sdW5hIFgxJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJykpXSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVswLCAxLCAyXSwgeT1bMCwgMiwgNF0sIG1vZGU9J2xpbmVzK21hcmtlcnMnLCBuYW1lPSdDb2x1bmEgWDIgKDIqWDEpJywgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJykpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0lsdXN0cmHDp8OjbyBkZSBDb2x1bmFzIExpbmVhcm1lbnRlIERlcGVuZGVudGVzJywgeGF4aXNfdGl0bGU9J09ic2VydmHDp8O1ZXMnLCB5YXhpc190aXRsZT0nVmFsb3JlcycsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGV4cGVyaW1lbnRvIGRlIGVuZ2VuaGFyaWEgcGFyYSBhdmFsaWFyIGEgZWZpY2nDqm5jaWEgZGUgcXVhdHJvIG3DoXF1aW5hcyBkaXN0aW50YXMsIGEgbWF0cml6IGRlIHBsYW5lamFtZW50byAkWCQgcG9zc3VpIGNvbGluZWFyaWRhZGUgZGV2aWRvIGEgdW1hIHJlZHVuZMOibmNpYSBuYSBjb25maWd1cmHDp8OjbyBkZSBpbnN0YWxhw6fDo28uIE8gc2lzdGVtYSBkZSBlcXVhw6fDtWVzIG5vcm1haXMgYXNzb2NpYWRvIMOpICRYXntcdG9wfVggXHRoZXRhID0gWF57XHRvcH15JC4gU2FiZW5kbyBxdWUgJFhee1x0b3B9WCQgw6kgdW1hIG1hdHJpeiBzaW5ndWxhciwgdW0gZW5nZW5oZWlybyBkZWNpZGUgdXRpbGl6YXIgdW1hIGludmVyc2EgZ2VuZXJhbGl6YWRhICRBXnstfSQgcGFyYSBvYnRlciB1bWEgc29sdcOnw6NvICRcXHRoZXRhID0gQV57LX1YXntcdG9wfXkkLiBDb25zaWRlcmFuZG8gYSBkZWZpbmnDp8OjbyBmdW5kYW1lbnRhbCBkZSBpbnZlcnNhIGdlbmVyYWxpemFkYSwgcXVhbCBkYXMgY29uZGnDp8O1ZXMgYWJhaXhvIGRldmUgc2VyIHNhdGlzZmVpdGEgcGVsYSBtYXRyaXogJEFeey19JCBwYXJhIGdhcmFudGlyIGEgY29uc2lzdMOqbmNpYSBkbyBzaXN0ZW1hIG9yaWdpbmFsLCBhc3N1bWluZG8gcXVlICRBID0gWF57XHRvcH1YJD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIiRBXnstfUFBXnstfSA9IEFeey19JCIsICJCIjogIiRBQV57LX1BID0gQSQiLCAiQyI6ICIkQV57LX1BID0gKEFeey19QSlee1xcdG9wfSQiLCAiRCI6ICIkQUFeey19ID0gKEFBXnstfSlee1xcdG9wfSQiLCAiRSI6ICIkQV57LX1BID0gSSQifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBkZSBxdWUgYSBpbnZlcnNhIGdlbmVyYWxpemFkYSAob3UgaW52ZXJzYSBjb25kaWNpb25hbCkgcmVsYXhhIGFzIHByb3ByaWVkYWRlcyBkZSB1bmljaWRhZGUgZSBzaW1ldHJpYSBkYSBpbnZlcnNhIGNvbXVtLCBmb2NhbmRvIG5hIHByZXNlcnZhw6fDo28gZGEgZXN0cnV0dXJhIGRvIHNpc3RlbWEgYXRyYXbDqXMgZGUgdW1hIGlkZW50aWRhZGUgYsOhc2ljYS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBlbGEgZGVmaW5pw6fDo28gZGUgaW52ZXJzYSBnZW5lcmFsaXphZGEgKG91IGludmVyc2EgY29uZGljaW9uYWwpIGFwcmVzZW50YWRhIG5vIHN1YnTDs3BpY28sIHVtYSBtYXRyaXogJEFeey19JCDDqSBpbnZlcnNhIGdlbmVyYWxpemFkYSBkZSAkQSQgc2UsIGUgc29tZW50ZSBzZSwgc2F0aXNmYXogYSBjb25kacOnw6NvIGZ1bmRhbWVudGFsICRBQV57LX1BID0gQSQuIEVzdGEgY29uZGnDp8OjbyDDqSBuZWNlc3PDoXJpYSBlIHN1ZmljaWVudGUgcGFyYSBnYXJhbnRpciBxdWUsIGNhc28gbyBzaXN0ZW1hICRBeCA9IGckIHNlamEgY29uc2lzdGVudGUsIG8gdmV0b3IgJHhebyA9IEFeey19ZyQgc2VqYSB1bWEgc29sdcOnw6NvIHbDoWxpZGEgZG8gc2lzdGVtYSwgcG9pcyAkQXhebyA9IEFBXnstfWcgPSAoQUFeey19QSl4Xm8gPSBBeF5vID0gZyQuIEFzIG91dHJhcyBhbHRlcm5hdGl2YXMgcmVmZXJlbS1zZSBhIGNvbmRpw6fDtWVzIGFkaWNpb25haXMgZGUgb3V0cm9zIHRpcG9zIGRlIGludmVyc2FzLCBjb21vIGEgZGUgTW9vcmUtUGVucm9zZS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEsIEouIEcuICYgRXN0ZXZlcywgRS4gTS4sIEludHJvZHXDp8OjbyBhb3MgTW9kZWxvcyBMaW5lYXJlcywgQ2FwIDIsIHAuIDUwIn0sIHsiZW51bmNpYWRvIjogIlVtIGFuYWxpc3RhIGRlIGRhZG9zIHRyYWJhbGhhIGNvbSB1bSBtb2RlbG8gbGluZWFyIG9uZGUgYSBtYXRyaXogJEEkIMOpIGRlIGRpbWVuc8OjbyAkMyBcXHRpbWVzIDIkIGUgcG9zdG8gJHIoQSkgPSAxJC4gQW8gYnVzY2FyIHVtYSBpbnZlcnNhIGdlbmVyYWxpemFkYSBkZSBNb29yZS1QZW5yb3NlLCAkQV57K30kLCBwYXJhIGNhbGN1bGFyIGVzdGltYWRvcmVzIGVtIHVtIHByb2JsZW1hIGRlIG90aW1pemHDp8OjbywgbyBhbmFsaXN0YSBkZXZlIHZlcmlmaWNhciBzZSBhcyBwcm9wcmllZGFkZXMgZXhpZ2lkYXMgcGVsYSBkZWZpbmnDp8OjbyBkZSBQZW5yb3NlICgxOTU1KSBzw6NvIGF0ZW5kaWRhcy4gUXVhbCBkYXMgYWx0ZXJuYXRpdmFzIGFiYWl4byBOw4NPIGZheiBwYXJ0ZSBkYXMgcXVhdHJvIGNvbmRpw6fDtWVzIGRlIFBlbnJvc2UgcGFyYSBhIGludmVyc2EgZGUgTW9vcmUtUGVucm9zZT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIiRBQV57K31BID0gQSQiLCAiQiI6ICIkQV57K31BQV57K30gPSBBXnsrfSQiLCAiQyI6ICIkKEFeeyt9QSlee1xcdG9wfSA9IEFeeyt9QSQiLCAiRCI6ICIkQUFeeyt9ID0gQV57K31BJCIsICJFIjogIiQoQUFeeyt9KV57XFx0b3B9ID0gQUFeeyt9JCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJEIiwgImRpY2EiOiAiQSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2Ugw6kgZGVmaW5pZGEgcG9yIHF1YXRybyBjb25kacOnw7VlcyBmb3JtYWlzIHF1ZSBnYXJhbnRlbSBzdWEgZXhpc3TDqm5jaWEgZSB1bmljaWRhZGUuIEFuYWxpc2UgY2FkYSBjb25kacOnw6NvIGRhIGRlZmluacOnw6NvIGRlIFBlbnJvc2UgKDE5NTUpLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiRGUgYWNvcmRvIGNvbSBhIGxpdGVyYXR1cmEgKFBlbnJvc2UsIDE5NTU7IE7DrXZlYSBCaXNwbywgQXVsYSA5KSwgYSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgJEFeeyt9JCBkZXZlIHNhdGlzZmF6ZXI6ICgxKSAkQUFeeyt9QT1BJDsgKDIpICRBXnsrfUFBXnsrfT1BXnsrfSQ7ICgzKSAkKEFeeyt9QSlee1xcdG9wfT1BXnsrfUEkIChzaW1ldHJpYSk7ICg0KSAkKEFBXnsrfSlee1xcdG9wfT1BQV57K30kIChzaW1ldHJpYSkuIEEgY29uZGnDp8OjbyAkQUFeeyt9ID0gQV57K31BJCAoY29tdXRhdGl2aWRhZGUpIG7Do28gw6kgdW1hIGV4aWfDqm5jaWEgZGEgZGVmaW5pw6fDo28gZGUgTW9vcmUtUGVucm9zZSwgZW1ib3JhIHBvc3NhIG9jb3JyZXIgZW0gY2Fzb3MgcGFydGljdWxhcmVzLCBjb21vIHBhcmEgbWF0cml6ZXMgXFxzaW3DqXRyaWNhcy4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIk7DrXZlYSBCaXNwbywgTUFURDQxLCBBdWxhIDksIHAuIDYifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gc2lzdGVtYSBkZSBtb2RlbGFnZW0gbGluZWFyIHV0aWxpemFkbyBwYXJhIG1vbml0b3JhbWVudG8gZGUgc2Vuc29yZXMgSW9ULCBhIG1hdHJpeiBkZSBkZXNpZ24gJEEkIGFwcmVzZW50YSBhbHRhIGNvbGluZWFyaWRhZGUsIHJlc3VsdGFuZG8gZW0gdW1hIG1hdHJpeiBzaW5ndWxhci4gUGFyYSBlbmNvbnRyYXIgdW0gZXN0aW1hZG9yIHJvYnVzdG8gZGUgcGFyw6JtZXRyb3MsIHV0aWxpemEtc2UgYSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgJEFeKyQuIENvbnNpZGVyYW5kbyBhcyBxdWF0cm8gY29uZGnDp8O1ZXMgZGUgUGVucm9zZSwgcXVhbCBkYXMgYWx0ZXJuYXRpdmFzIGFiYWl4byBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgYSBuYXR1cmV6YSBkYSBtYXRyaXogZGUgcHJvamXDp8OjbyAkUCA9IEEgQV4rJD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgbWF0cml6ICRBIEFeKyQgw6kgdW1hIHByb2plw6fDo28gb2Jsw61xdWEgc29icmUgbyBlc3Bhw6dvIGNvbHVuYSBkZSAkQSQsIG9uZGUgYSBzaW1ldHJpYSBuw6NvIMOpIGdhcmFudGlkYS4iLCAiQiI6ICJBIG1hdHJpeiAkQSBBXiskIMOpIGEgcHJvamXDp8OjbyBvcnRvZ29uYWwgc29icmUgbyBlc3Bhw6dvIGxpbmhhIGRlICRBJCwgZ2FyYW50aW5kbyBhIG1pbmltaXphw6fDo28gZGEgbm9ybWEgZG8gcmVzw61kdW8uIiwgIkMiOiAiQSBtYXRyaXogJEEgQV4rJCDDqSB1bWEgcHJvamXDp8OjbyBvcnRvZ29uYWwgc29icmUgbyBlc3Bhw6dvIGNvbHVuYSBkZSAkQSQsIHNlbmRvIGlkZW1wb3RlbnQgZSBcXHNpbcOpdHJpY2EuIiwgIkQiOiAiQSBtYXRyaXogJEEgQV4rJCByZXN1bHRhIG5hIG1hdHJpeiBpZGVudGlkYWRlIHNlbXByZSBxdWUgJEEkIMOpIHVtYSBtYXRyaXogcXVhZHJhZGEgZGUgcG9zdG8gY29tcGxldG8uIiwgIkUiOiAiQSBtYXRyaXogJEEgQV4rJCBuw6NvIHBvc3N1aSBwcm9wcmllZGFkZXMgZGUgcHJvamXDp8Ojbywgc2VydmluZG8gYXBlbmFzIHBhcmEgcmVzb2x2ZXIgc2lzdGVtYXMgaW5jb25zaXN0ZW50ZXMuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgZGVmaW5pw6fDo28gZGUgcHJvamXDp8O1ZXMgb3J0b2dvbmFpcyBlIGNvbW8gYXMgY29uZGnDp8O1ZXMgZGUgUGVucm9zZSAoMykgJChBIEFeKylee1xcdG9wfSA9IEEgQV4rJCBlIGEgcHJvcHJpZWRhZGUgZGUgaWRlbXBvdMOqbmNpYSAkQSBBXisgQSBBXisgPSBBIEFeKyQgc2UgcmVsYWNpb25hbSBjb20gYSBnZW9tZXRyaWEgZG8gZXNwYcOnbyBjb2x1bmEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQZWxhIGRlZmluacOnw6NvIGRhIGludmVyc2EgZGUgTW9vcmUtUGVucm9zZSwgYSBjb25kacOnw6NvICgzKSBhZmlybWEgcXVlICQoQSBBXispXntcXHRvcH0gPSBBIEFeKyQsIG8gcXVlIGNhcmFjdGVyaXphIHVtYSBtYXRyaXogXFxzaW3DqXRyaWNhLiBBbMOpbSBkaXNzbywgZGEgY29uZGnDp8OjbyAoMSkgJEEgQV4rIEEgPSBBJCwgcG9kZW1vcyBkZXJpdmFyIGEgaWRlbXBvdMOqbmNpYTogJChBIEFeKykoQSBBXispID0gKEEgQV4rIEEpIEFeKyA9IEEgQV4rJC4gVW1hIG1hdHJpeiBxdWUgw6kgc2ltdWx0YW5lYW1lbnRlIFxcc2ltw6l0cmljYSBlIGlkZW1wb3RlbnRlIMOpLCBwb3IgZGVmaW5pw6fDo28sIHVtYSBtYXRyaXogZGUgcHJvamXDp8OjbyBvcnRvZ29uYWwuIE8gZXNwYcOnbyBzb2JyZSBvIHF1YWwgZWxhIHByb2pldGEgw6kgbyBlc3Bhw6dvIGNvbHVuYSBkZSAkQSQsIGRlbm90YWRvIHBvciAkQyhBKSQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJTdXBvbmhhIHVtYSBtYXRyaXogJEEkIGRlIGRpbWVuc8OjbyAkMyBcXHRpbWVzIDIkIGNvbSBwb3N0byAxLiBEZXNlamEtc2UgZW5jb250cmFyIHVtYSBtYXRyaXogJEFeKyQgcXVlIHNhdGlzZmHDp2EgYXMgY29uZGnDp8O1ZXMgZGUgUGVucm9zZS4gU2UgdW0gb3BlcmFkb3IgbWF0ZW3DoXRpY28gJEFeKyQgc2F0aXNmYXogJEEgQV4rIEEgPSBBJCBlICRBXisgQSBBXisgPSBBXiskLCBwb2RlbW9zIGFmaXJtYXIgc29icmUgYSB1bmljaWRhZGUgZGVzdGEgaW52ZXJzYT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkV4aXN0ZW0gaW5maW5pdGFzIGludmVyc2FzIHF1ZSBzYXRpc2ZhemVtIGFwZW5hcyBhcyBkdWFzIHByaW1laXJhcyBjb25kacOnw7VlcywgbWFzIGFwZW5hcyB1bWEgc2F0aXNmYXogYXMgcXVhdHJvIGNvbmRpw6fDtWVzIGRlIFBlbnJvc2UuIiwgIkIiOiAiQSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgbsOjbyDDqSDDum5pY2EsIHBvaXMgZGVwZW5kZSBkYSBlc2NvbGhhIGRvIGFsZ29yaXRtbyBkZSBkZWNvbXBvc2nDp8OjbyBlbSB2YWxvcmVzIHNpbmd1bGFyZXMuIiwgIkMiOiAiUXVhbHF1ZXIgaW52ZXJzYSBnZW5lcmFsaXphZGEgKGctaW52ZXJzYSkgcXVlIHNhdGlzZmHDp2EgYXBlbmFzICRBIEFeKyBBID0gQSQgw6kgZXF1aXZhbGVudGUgw6AgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlLiIsICJEIjogIkEgdW5pY2lkYWRlIHPDsyDDqSBnYXJhbnRpZGEgc2UgJEEkIGZvciB1bWEgbWF0cml6IHF1YWRyYWRhIG7Do28gc2luZ3VsYXIuIiwgIkUiOiAiQXMgY29uZGnDp8O1ZXMgKDMpIGUgKDQpIHPDo28gcmVkdW5kYW50ZXMsIGxvZ28gcXVhbHF1ZXIgaW52ZXJzYSBxdWUgc2F0aXNmYcOnYSAoMSkgZSAoMikgw6kgYSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJSZWZsaXRhIHNvYnJlIG8gcGFwZWwgZGFzIGNvbmRpw6fDtWVzICgzKSBlICg0KSBuYSByZXN0cmnDp8OjbyBkYSBsaWJlcmRhZGUgZ2VvbcOpdHJpY2EgZGEgaW52ZXJzYS4gQXMgY29uZGnDp8O1ZXMgKDEpIGUgKDIpIGRlZmluZW0gdW1hIGNsYXNzZSBkZSBpbnZlcnNhcyBnZW5lcmFsaXphZGFzIChyZWZsZXhpdmFzKSwgZW5xdWFudG8gYXMgY29uZGnDp8O1ZXMgKDMpIGUgKDQpIGltcMO1ZW0gYSBvcnRvZ29uYWxpZGFkZS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlIMOpIGRlZmluaWRhIGRlIGZvcm1hIHF1ZSB0b2RhcyBhcyBxdWF0cm8gY29uZGnDp8O1ZXMgc2VqYW0gc2F0aXNmZWl0YXMgc2ltdWx0YW5lYW1lbnRlLiBBcyBjb25kacOnw7VlcyAoMSkgZSAoMikgZGVmaW5lbSBvIHF1ZSBjaGFtYW1vcyBkZSBpbnZlcnNhIHJlZmxleGl2YSwgZSBwb2RlbSBleGlzdGlyIG11aXRhcyBtYXRyaXplcyBxdWUgYXMgc2F0aXNmYXplbS4gTm8gZW50YW50bywgYSBhZGnDp8OjbyBkYXMgY29uZGnDp8O1ZXMgKDMpIGUgKDQpIHJlc3RyaW5nZSBhIGVzY29saGEsIGZvcsOnYW5kbyBhIG1hdHJpeiAkQV4rJCBhIHNlciBhIMO6bmljYSBxdWUgc2F0aXNmYXogdG9kYXMgYXMgcXVhdHJvIHByb3ByaWVkYWRlcywgZ2FyYW50aW5kbyBhIHVuaWNpZGFkZSBlIGEgZXN0YWJpbGlkYWRlIG51bcOpcmljYSBuYSBtaW5pbWl6YcOnw6NvIGRhcyBub3JtYXMgZGUgJFkgLSBBXFxiZXRhJCBlIGRlICRcXGJldGEkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gc2lzdGVtYSBkZSBtb25pdG9yYW1lbnRvIGRlIElvVCBpbmR1c3RyaWFsLCBhIG1hdHJpeiBkZSBkZWxpbmVhbWVudG8gZXhwZXJpbWVudGFsICRBJCBhcHJlc2VudGEgY29saW5lYXJpZGFkZSwgcmVzdWx0YW5kbyBlbSB1bSBwb3N0byAkcihBKSA9IDIkIG1lbm9yIHF1ZSBzdWEgZGltZW5zw6NvIGRlIGNvbHVuYXMuIFBhcmEgZXN0aW1hciBvcyBwYXLDom1ldHJvcyBkbyBtb2RlbG8sIHVtIGVuZ2VuaGVpcm8gZGVjaWRlIHV0aWxpemFyIG8gYWxnb3JpdG1vIGRlIFNlYXJsZSBwYXJhIG9idGVyIHVtYSBpbnZlcnNhIGdlbmVyYWxpemFkYSBjb25kaWNpb25hbCAkQV57LX0kLiBEYWRhIGEgbWF0cml6IGRlIGRhZG9zIHNpbXBsaWZpY2FkYSAkQSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgJiAwIFxcXFwgMSAmIDEgJiAwIFxcXFwgMSAmIDAgJiAxIFxcXFwgMSAmIDAgJiAxIFxcZW5ke3BtYXRyaXh9JCwgcXVhbCBkYXMgb3DDp8O1ZXMgYWJhaXhvIHJlcHJlc2VudGEgdW1hIG1hdHJpeiAkQV57LX0kIGNvcnJldGEgb2J0aWRhIHZpYSBhbGdvcml0bW8gZGUgU2VhcmxlLCBjb25zaWRlcmFuZG8gYSBlc2NvbGhhIGRhIHN1Ym1hdHJpeiAkTSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAwICYgMSBcXGVuZHtwbWF0cml4fSQgbmEgc3ViZXN0cnV0dXJhIGRlIHBvc3RvIHBsZW5vPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJEFeey19ID0gXFxiZWdpbntwbWF0cml4fSAwICYgMCAmIDAgJiAwIFxcXFwgMCAmIDEgJiAwICYgMCBcXFxcIDAgJiAwICYgMSAmIDAgXFxlbmR7cG1hdHJpeH0kIiwgIkIiOiAiJEFeey19ID0gXFxiZWdpbntwbWF0cml4fSAwICYgMCAmIDAgJiAxIFxcXFwgMCAmIDEgJiAwICYgMCBcXFxcIDAgJiAwICYgMSAmIDAgXFxlbmR7cG1hdHJpeH0kIiwgIkMiOiAiJEFeey19ID0gXFxiZWdpbntwbWF0cml4fSAxICYgMCAmIDAgJiAwIFxcXFwgMCAmIDEgJiAwICYgMCBcXFxcIDAgJiAwICYgMSAmIDAgXFxlbmR7cG1hdHJpeH0kIiwgIkQiOiAiJEFeey19ID0gXFxiZWdpbntwbWF0cml4fSAwICYgMCAmIDAgJiAwIFxcXFwgMSAmIDAgJiAwICYgMCBcXFxcIDAgJiAxICYgMCAmIDAgXFxlbmR7cG1hdHJpeH0kIiwgIkUiOiAiJEFeey19ID0gXFxiZWdpbntwbWF0cml4fSAwICYgMSAmIDAgJiAwIFxcXFwgMCAmIDAgJiAxICYgMCBcXFxcIDAgJiAwICYgMCAmIDEgXFxlbmR7cG1hdHJpeH0kIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJPIGFsZ29yaXRtbyBkZSBTZWFybGUgY29uc2lzdGUgZW0gaXNvbGFyIHVtYSBzdWJtYXRyaXogJE0kIGRlIHBvc3RvIHBsZW5vICRrJCwgaW52ZXJ0ZXIsIHRyYW5zcG9yLCBlIGFsb2NhciBuYSBwb3Npw6fDo28gb3JpZ2luYWwgZGVudHJvIGRlIHVtYSBtYXRyaXogZGUgemVyb3MgZGUgZGltZW5zw7VlcyB0cmFuc3Bvc3Rhcywgc2VndWlkYSBwZWxhIHRyYW5zcG9zacOnw6NvIGZpbmFsIGRhIG1hdHJpeiByZXN1bHRhbnRlLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiMS4gSWRlbnRpZmljYW1vcyAkcihBKSA9IDIkLiBFc2NvbGhlbW9zICRNID0gXFxiZWdpbntwbWF0cml4fSAxICYgMCBcXFxcIDAgJiAxIFxcZW5ke3BtYXRyaXh9JCAobGluaGFzIDIgZSAzLCBjb2x1bmFzIDIgZSAzIGRlICRBJCkuIDIuICRNXnstMX0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwIFxcXFwgMCAmIDEgXFxlbmR7cG1hdHJpeH0kLCBsb2dvICQoTV57LTF9KV57XFx0b3B9ID0gXFxiZWdpbntwbWF0cml4fSAxICYgMCBcXFxcIDAgJiAxIFxcZW5ke3BtYXRyaXh9JC4gMy4gU3Vic3RpdHXDrW1vcyAkTSQgZW0gJEEkIHBvciAkKE1eey0xfSlee1xcdG9wfSQgZSBhbnVsYW1vcyBvIHJlc3RhbnRlOiAkXFxiZWdpbntwbWF0cml4fSAwICYgMCAmIDAgXFxcXCAwICYgMSAmIDAgXFxcXCAwICYgMCAmIDEgXFxcXCAwICYgMCAmIDAgXFxlbmR7cG1hdHJpeH0kLiA0LiBUcmFuc3BvbW9zIHBhcmEgb2J0ZXIgJEFeey19ID0gXFxiZWdpbntwbWF0cml4fSAwICYgMCAmIDAgJiAwIFxcXFwgMCAmIDEgJiAwICYgMCBcXFxcIDAgJiAwICYgMSAmIDAgXFxlbmR7cG1hdHJpeH0kLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTHVuYSwgSi4gRy4gJiBFc3RldmVzLCBFLiBNLiwgQ2FwIDEsIHAuIDM4In0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bWEgbWF0cml6ICRBJCBkZSBvYnNlcnZhw6fDtWVzIGVtIHVtIGV4cGVyaW1lbnRvIGNsw61uaWNvIGNvbSBwb3N0byAkcihBKT1rJC4gQSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgJEFeeyt9JCDDqSBhbXBsYW1lbnRlIHV0aWxpemFkYSBwb3Igc2VyIMO6bmljYSBlIHNhdGlzZmF6ZXIgcHJvcHJpZWRhZGVzIGlkZWFpcyBkZSBtw61uaW1vcyBxdWFkcmFkb3MuIFNhYmVuZG8gcXVlICRBXnsrfSQgZGV2ZSBzYXRpc2ZhemVyICRBQV57K31BPUEkLCAkQV57K31BQV57K309QV57K30kLCAkKEFeeyt9QSlee1xcdG9wfSA9IEFeeyt9QSQgZSAkKEFBXnsrfSlee1xcdG9wfSA9IEFBXnsrfSQsIHF1YWwgZGFzIGFmaXJtYcOnw7VlcyBhYmFpeG8gZGVzY3JldmUgY29ycmV0YW1lbnRlIG8gY29tcG9ydGFtZW50byBkZSAkQV57K30kIHF1YW5kbyBhIG1hdHJpeiAkQSQgw6kgZGUgcG9zdG8gbGluaGEgY29tcGxldG8gKCRyKEEpPW0kLCBvbmRlICRtJCDDqSBvIG7Dum1lcm8gZGUgbGluaGFzKT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIiRBXnsrfSA9IChBXntcXHRvcH1BKV57LTF9QV57XFx0b3B9JCBlICRBQV57K30gPSBJX3sobSl9JCIsICJCIjogIiRBXnsrfSA9IEFee1xcdG9wfShBQV57XFx0b3B9KV57LTF9JCBlICRBQV57K30gPSBJX3sobSl9JCIsICJDIjogIiRBXnsrfSA9IEFee1xcdG9wfShBQV57XFx0b3B9KV57LTF9JCBlICRBXnsrfUEgPSBJX3sobSl9JCIsICJEIjogIiRBXnsrfSA9IChBXntcXHRvcH1BKV57LTF9QV57XFx0b3B9JCBlICRBXnsrfUEgPSBJX3sobSl9JCIsICJFIjogIkEgaW52ZXJzYSAkQV57K30kIG7Do28gZXhpc3RlIHNlIGEgbWF0cml6IG7Do28gZm9yIHF1YWRyYWRhLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGRpc3RpbsOnw6NvIGVudHJlIHBvc3RvIGxpbmhhIGNvbXBsZXRvIGUgcG9zdG8gY29sdW5hIGNvbXBsZXRvLiBQYXJhIHBvc3RvIGxpbmhhIGNvbXBsZXRvICgkcihBKT1tJCksIGEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlIHJlc3VsdGEgZW0gdW1hIGludmVyc2Egw6AgZGlyZWl0YS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkNvbmZvcm1lIGEgdGVvcmlhIGRlIGludmVyc2FzIGdlbmVyYWxpemFkYXMsIHNlICRyKEEpPW0kIChwb3N0byBsaW5oYSBjb21wbGV0byksIGEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlIMOpIGRhZGEgcG9yICRBXnsrfSA9IEFee1xcdG9wfShBQV57XFx0b3B9KV57LTF9JC4gQ29tbyBjb25zZXF1w6puY2lhIGRpcmV0YSwgJEFBXnsrfSA9IEEoQV57XFx0b3B9KEFBXntcXHRvcH0pXnstMX0pID0gKEFBXntcXHRvcH0pKEFBXntcXHRvcH0pXnstMX0gPSBJX3sobSl9JC4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEsIEouIEcuICYgRXN0ZXZlcywgRS4gTS4sIENhcCAxLCBwLiAzNyJ9XSwgInF1ZXN0b2VzX2Rpc2N1cnNpdmFzIjogW3siZW51bmNpYWRvIjogIkRlbW9uc3RyZSBtYXRlbWF0aWNhbWVudGUgcG9yIHF1ZSwgc2UgbyBwb3N0byBkZSAkWCQgw6kgJHIgPCBtJCwgYSBtYXRyaXogJChYXntcXHRvcH1YKSQgw6kgc2luZ3VsYXIuIFV0aWxpemUgYSBkZWZpbmnDp8OjbyBkZSBtYXRyaXogc2luZ3VsYXIgYXRyYXbDqXMgZG8gZGV0ZXJtaW5hbnRlIG91IGRhIGV4aXN0w6puY2lhIGRlIHVtIHZldG9yIG7Do28gbnVsbyAkdiQgdGFsIHF1ZSAkKFhee1xcdG9wfVgpdiA9IDAkLiIsICJkaWNhIjogIkNvbnNpZGVyZSBxdWUgc2UgbyBwb3N0byDDqSAkciA8IG0kLCBlbnTDo28gZXhpc3RlIHVtIHZldG9yICR2IFxcbmVxIDAkIHRhbCBxdWUgJFh2ID0gMCQuIE8gcXVlIG9jb3JyZSBxdWFuZG8gbXVsdGlwbGljYW1vcyBwb3IgJFhee1xcdG9wfSQ/IiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlNlIG8gcG9zdG8gZGEgbWF0cml6ICRYJCDDqSAkciA8IG0kLCBlbnTDo28gYXMgY29sdW5hcyBkZSAkWCQgc8OjbyBsaW5lYXJtZW50ZSBkZXBlbmRlbnRlcy4iLCAiSXNzbyBpbXBsaWNhIHF1ZSBleGlzdGUgdW0gdmV0b3IgbsOjbyBudWxvICR2IFxcaW4gXFxtYXRoYmJ7Un1ebSQgdGFsIHF1ZSAkWHYgPSAwJC4iLCAiTXVsdGlwbGljYW1vcyBhbWJvcyBvcyBsYWRvcyBwb3IgJFhee1xcdG9wfSQ6ICRYXntcXHRvcH0oWHYpID0gWF57XFx0b3B9MCQuIiwgIlJlc3VsdGEgcXVlICQoWF57XFx0b3B9WCl2ID0gMCQuIiwgIkNvbW8gJHYkIMOpIHVtIHZldG9yIG7Do28gbnVsbyBxdWUgc2F0aXNmYXogJChYXntcXHRvcH1YKXYgPSAwJCwgYSBtYXRyaXogJChYXntcXHRvcH1YKSQgcG9zc3VpIHVtIG7DumNsZW8gKG51bGwgc3BhY2UpIG7Do28gdHJpdmlhbC4iLCAiUG9yIGRlZmluacOnw6NvLCB1bWEgbWF0cml6IHF1YWRyYWRhIHF1ZSBtYXBlaWEgdW0gdmV0b3IgbsOjbyBudWxvIHBhcmEgemVybyDDqSBzaW5ndWxhciwgbG9nbyAkXFxkZXQoWF57XFx0b3B9WCkgPSAwJCBlIGEgaW52ZXJzYSB0cmFkaWNpb25hbCAkKFhee1xcdG9wfVgpXnstMX0kIG7Do28gZXhpc3RlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSBtb2RlbG8gbGluZWFyIHNpbXBsZXMgJHkgPSBYXFx0aGV0YSArIGUkIG9uZGUgJFggPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxIFxcXFwgMSAmIDEgXFxlbmR7cG1hdHJpeH0kLiBDYWxjdWxlICQoWF57XFx0b3B9WCkkIGUgdmVyaWZpcXVlIG8gdmFsb3IgZG8gZGV0ZXJtaW5hbnRlLiBFeHBsaXF1ZSwgY29tIGJhc2Ugbm8gcmVzdWx0YWRvLCBwb3IgcXVlIGEgZXN0aW1hdGl2YSAkXFxoYXR7XFx0aGV0YX0gPSAoWF57XFx0b3B9WCleey0xfVhee1xcdG9wfXkkIGZhbGhhIG5lc3RlIGNlbsOhcmlvLiIsICJkaWNhIjogIkNhbGN1bGUgcHJpbWVpcm8gYSB0cmFuc3Bvc3RhICRYXntcXHRvcH0kLCBkZXBvaXMgbyBwcm9kdXRvIG1hdHJpY2lhbCAkWF57XFx0b3B9WCQuIExlbWJyZS1zZSBxdWUgJFxcZGV0KEEpID0gYWQgLSBiYyQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlByaW1laXJvLCBjYWxjdWxhbW9zICRYXntcXHRvcH0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxIFxcXFwgMSAmIDEgXFxlbmR7cG1hdHJpeH0kLiIsICJPIHByb2R1dG8gJFhee1xcdG9wfVggPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxIFxcXFwgMSAmIDEgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSAxICYgMSBcXFxcIDEgJiAxIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAyICYgMiBcXFxcIDIgJiAyIFxcZW5ke3BtYXRyaXh9JC4iLCAiTyBkZXRlcm1pbmFudGUgZGUgJChYXntcXHRvcH1YKSQgw6kgJDIoMikgLSAyKDIpID0gNCAtIDQgPSAwJC4iLCAiQ29tbyAkXFxkZXQoWF57XFx0b3B9WCkgPSAwJCwgYSBtYXRyaXogw6kgc2luZ3VsYXIuIiwgIkEgaW52ZXJzYSAkKFhee1xcdG9wfVgpXnstMX0kIMOpIGRlZmluaWRhIGNvbW8gJFxcZnJhY3sxfXtcXGRldChBKX0gXFx0ZXh0e2Fkan0oQSkkLCBxdWUgZW52b2x2ZSBhIGRpdmlzw6NvIHBvciB6ZXJvLCBsb2dvIGEgaW52ZXJzYSBuw6NvIGVzdMOhIGRlZmluaWRhLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4wfSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUgbyBwYXBlbCBkYSBpbnZlcnNhIGdlbmVyYWxpemFkYSAoJEckKSBuYSByZXNvbHXDp8OjbyBkbyBzaXN0ZW1hIGRlIGVxdWHDp8O1ZXMgbm9ybWFpcyBxdWFuZG8gJChYXntcXHRvcH1YKSQgw6kgc2luZ3VsYXIuIENvbW8gYSBtYXRyaXogJEckLCB0YWwgcXVlICRYXntcXHRvcH1YIEcgWF57XFx0b3B9WCA9IFhee1xcdG9wfVgkLCBwZXJtaXRlIGNvbnRvcm5hciBhIGxpbWl0YcOnw6NvIGRhIGludmVyc2EgdHJhZGljaW9uYWw/IiwgImRpY2EiOiAiUGVuc2UgcXVlLCBlbSB2ZXogZGUgdW1hIGludmVyc2Egw7puaWNhLCBhIGludmVyc2EgZ2VuZXJhbGl6YWRhIGZvcm5lY2UgdW1hICdwc2V1ZG9pbnZlcnNhJyBxdWUgcGVybWl0ZSBlbmNvbnRyYXIgdW1hIHNvbHXDp8OjbyBwYXJ0aWN1bGFyIHBhcmEgbyBzaXN0ZW1hLCBtZXNtbyBxdWUgbsOjbyBzZWphIGEgw7puaWNhLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBIGludmVyc2EgdHJhZGljaW9uYWwgZXhpZ2UgcXVlIGEgbWF0cml6IHNlamEgZGUgcG9zdG8gcGxlbm8gKGludmVyc8OtdmVsKS4gUXVhbmRvICRyKFgpIDwgbSQsIG8gc2lzdGVtYSDDqSBpbmRldGVybWluYWRvLiIsICJBIGludmVyc2EgZ2VuZXJhbGl6YWRhICRHJCDDqSBxdWFscXVlciBtYXRyaXogcXVlIHNhdGlzZmF6ICRYXntcXHRvcH1YIEcgWF57XFx0b3B9WCA9IFhee1xcdG9wfVgkLiIsICJBbyB1dGlsaXphciAkXFxoYXR7XFx0aGV0YX0gPSBHIFhee1xcdG9wfXkkLCBvYnRlbW9zIHVtYSBzb2x1w6fDo28gcGFydGljdWxhciBxdWUgbWluaW1pemEgYSBzb21hIGRlIHF1YWRyYWRvcyBkb3MgcmVzw61kdW9zICRTUUUgPSBcXHN1bSBlX2leMiQuIiwgIkVtYm9yYSAkXFxoYXR7XFx0aGV0YX0kIG7Do28gc2VqYSDDum5pY28gKGV4aXN0ZW0gaW5maW5pdGFzIHNvbHXDp8O1ZXMpLCBhIGludmVyc2EgZ2VuZXJhbGl6YWRhIGZvcm5lY2UgdW0gbcOpdG9kbyBhbGfDqWJyaWNvIHBhcmEgZXNjb2xoZXIgdW1hIGRlc3NhcyBzb2x1w6fDtWVzIGUgYXZhbsOnYXIgY29tIGEgbW9kZWxhZ2VtIGVzdGF0w61zdGljYS4iLCAiSXNzbyDDqSBmdW5kYW1lbnRhbCBlbSBBTk9WQSBlIG1vZGVsb3MgY29tIHZhcmnDoXZlaXMgZHVtbXksIG9uZGUgYSByZWR1bmTDom5jaWEgw6kgZXN0cnV0dXJhbCBubyBkZXNpZ24uIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiU2VqYSBvIHNpc3RlbWEgZGUgZXF1YcOnw7VlcyBsaW5lYXJlcyAkQXggPSBnJCBkYWRvIHBvciAkJCBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxIFxcXFwgMSAmIC0xIFxcXFwgLTIgJiAwIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0geF8xIFxcXFwgeF8yIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAzIFxcXFwgMSBcXFxcIC00IFxcZW5ke3BtYXRyaXh9ICQkIE1vc3RyZSwgdXRpbGl6YW5kbyB1bWEgaW52ZXJzYSBjb25kaWNpb25hbCAkQV57LX0kIG9idGlkYSBwZWxvIG3DqXRvZG8gZGUgc3VibWF0cml6ZXMsIHNlIG8gc2lzdGVtYSDDqSBjb25zaXN0ZW50ZSB2ZXJpZmljYW5kbyBhIGNvbmRpw6fDo28gJEFBXnstfWcgPSBnJC4iLCAiZGljYSI6ICJVbWEgaW52ZXJzYSBjb25kaWNpb25hbCAkQV57LX0kIHNhdGlzZmF6ICRBQV57LX1BID0gQSQuIFRlbnRlIGVuY29udHJhciB1bWEgc3VibWF0cml6IGludmVydMOtdmVsIGRlIEEsIGNhbGN1bGFyIHN1YSBpbnZlcnNhIGUgZXhwYW5kaS1sYSBwYXJhIGFzIGRpbWVuc8O1ZXMgb3JpZ2luYWlzIGRlICRBXntcXHRvcH0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJJZGVudGlmaWNhbW9zIHF1ZSBvIHBvc3RvIGRhIG1hdHJpeiBBIMOpICRyKEEpID0gMiQuIEVzY29saGVtb3MgYSBzdWJtYXRyaXogJE0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxIFxcXFwgMSAmIC0xIFxcZW5ke3BtYXRyaXh9JC4iLCAiQ2FsY3VsYW1vcyAkTV57LTF9ID0gXFxmcmFjezF9ey0yfSBcXGJlZ2lue3BtYXRyaXh9IC0xICYgLTEgXFxcXCAtMSAmIDEgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDAuNSAmIDAuNSBcXFxcIDAuNSAmIC0wLjUgXFxlbmR7cG1hdHJpeH0kLiIsICJDb25zdHJ1w61tb3MgJEFeey19ID0gXFxiZWdpbntwbWF0cml4fSBNXnstMX0gJiAwIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAwLjUgJiAwLjUgJiAwIFxcXFwgMC41ICYgLTAuNSAmIDAgXFxlbmR7cG1hdHJpeH0kLiIsICJWZXJpZmljYW1vcyAkQUFeey19ZyA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgXFxcXCAxICYgLTEgXFxcXCAtMiAmIDAgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSAwLjUgJiAwLjUgJiAwIFxcXFwgMC41ICYgLTAuNSAmIDAgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSAzIFxcXFwgMSBcXFxcIC00IFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAxICYgMCAmIDAgXFxcXCAwICYgMSAmIDAgXFxcXCAtMSAmIC0xICYgMCBcXGVuZHtwbWF0cml4fSBcXGJlZ2lue3BtYXRyaXh9IDMgXFxcXCAxIFxcXFwgLTQgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDMgXFxcXCAxIFxcXFwgLTQgXFxlbmR7cG1hdHJpeH0kLiIsICJDb21vICRBQV57LX1nID0gZyQsIG8gc2lzdGVtYSDDqSBjb25zaXN0ZW50ZS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hLCBKLiBHLiAmIEVzdGV2ZXMsIEUuIE0uLCBJbnRyb2R1w6fDo28gYW9zIE1vZGVsb3MgTGluZWFyZXMsIENhcCAyLCBwLiA0OSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJEYWRhIGEgbWF0cml6IFxcc2ltw6l0cmljYSAkQSA9IFxcYmVnaW57cG1hdHJpeH0gNCAmIDIgXFxcXCAyICYgMiBcXGVuZHtwbWF0cml4fSQsIGNhbGN1bGUgYSBzdWEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlICRBXnsrfSQuIENvbnNpZGVyZSBhIGRlY29tcG9zacOnw6NvIGVzcGVjdHJhbCAkQSA9IFAgXFxMYW1iZGEgUF57XFx0b3B9JCBzZSBuZWNlc3PDoXJpby4iLCAiZGljYSI6ICJQYXJhIG1hdHJpemVzIFxcc2ltw6l0cmljYXMsIGEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlIMOpIGRhZGEgcG9yICRBXnsrfSA9IFAgXFxMYW1iZGFeeyt9IFBee1xcdG9wfSQsIG9uZGUgJFxcTGFtYmRhXnsrfSQgY29udMOpbSBvcyByZWPDrXByb2NvcyBkb3MgYXV0b3ZhbG9yZXMgbsOjbyBudWxvcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRW5jb250cmFtb3Mgb3MgYXV0b3ZhbG9yZXMgZGUgJEEkOiAkXFxkZXQoQSAtIFxcbGFtYmRhIEkpID0gKDQtXFxsYW1iZGEpKDItXFxsYW1iZGEpIC0gNCA9IFxcbGFtYmRhXjIgLSA2XFxsYW1iZGEgKyA0ID0gMCQuIEFzIHJhw616ZXMgc8OjbyAkXFxsYW1iZGFfMSA9IDMrXFxzcXJ0ezV9JCBlICRcXGxhbWJkYV8yID0gMy1cXHNxcnR7NX0kLiIsICJDb21vIGEgbWF0cml6IMOpIG7Do28gc2luZ3VsYXIgKCRcXFxcZGV0KEEpID0gNCBcXG5lcSAwJCksIGEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlIGNvaW5jaWRlIGNvbSBhIGludmVyc2EgdXN1YWwgJEFeey0xfSQuIiwgIkNhbGN1bGFtb3MgJEFeey0xfSA9IFxcZnJhY3sxfXs0fSBcXGJlZ2lue3BtYXRyaXh9IDIgJiAtMiBcXFxcIC0yICYgNCBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMC41ICYgLTAuNSBcXFxcIC0wLjUgJiAxLjAgXFxlbmR7cG1hdHJpeH0kLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCB1dGlsaXphbmRvIG8gZm9ybWFsaXNtbyBkYSBpbnZlcnNhIGdlbmVyYWxpemFkYSAkQV57LX0kLCBwb3IgcXVlIGVtIG1vZGVsb3MgZGUgcmVncmVzc8OjbyBsaW5lYXIgY29tIGNvbGluZWFyaWRhZGUgcGVyZmVpdGEgZW50cmUgYXMgdmFyacOhdmVpcyBleHBsaWNhdGl2YXMsIGEgbWF0cml6ICRYXntcXHRvcH1YJCBuw6NvIGFkbWl0ZSBpbnZlcnNhIMO6bmljYSwgZSBjb21vIGEgZXNjb2xoYSBkZSBkaWZlcmVudGVzIGludmVyc2FzIGNvbmRpY2lvbmFpcyBhZmV0YSBhIGVzdGltYXRpdmEgZG9zIHBhcsOibWV0cm9zICRcXHRoZXRhJCBubyBzaXN0ZW1hIGRlIGVxdWHDp8O1ZXMgbm9ybWFpcy4iLCAiZGljYSI6ICJQZW5zZSBuYSByZWxhw6fDo28gJHggPSBBXnstfWckIGUgbm8gdGVybW8gJChJIC0gQV57LX1BKWgkIHF1ZSBjb21ww7VlIGEgc29sdcOnw6NvIGdlcmFsIGRvIHNpc3RlbWEgY29uc2lzdGVudGUuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgY29saW5lYXJpZGFkZSBwZXJmZWl0YSBpbXBsaWNhIHF1ZSAkcihYXntcXHRvcH1YKSA8IG0kLCBvbmRlICRtJCDDqSBvIG7Dum1lcm8gZGUgY29sdW5hcywgdG9ybmFuZG8gJFhee1xcdG9wfVgkIHNpbmd1bGFyLiIsICJQYXJhIHVtIHNpc3RlbWEgY29uc2lzdGVudGUgJEFcXHRoZXRhID0gZyQsIGEgc29sdcOnw6NvIGdlcmFsIMOpIGRhZGEgcG9yICRcXHRoZXRhID0gQV57LX1nICsgKEkgLSBBXnstfUEpaCQsIG9uZGUgJGgkIMOpIHVtIHZldG9yIGFyYml0csOhcmlvLiIsICJEaWZlcmVudGVzIGVzY29saGFzIGRlICRBXnstfSQgcmVzdWx0YW0gZW0gZGlmZXJlbnRlcyB2ZXRvcmVzIGRlIGVzdGltYXRpdmFzICRcXHRoZXRhJCwgcmVmbGV0aW5kbyBxdWUsIHNlbSByZXN0cmnDp8O1ZXMgYWRpY2lvbmFpcywgbsOjbyBow6EgdW0gZXN0aW1hZG9yIMO6bmljbyBwYXJhIGNhZGEgcGFyw6JtZXRybyBpbmRpdmlkdWFsIHF1YW5kbyBleGlzdGUgY29saW5lYXJpZGFkZS4iLCAiQ29udHVkbywgYSBwcm9qZcOnw6NvICRYXFx0aGV0YSQgcGVybWFuZWNlIGludmFyaWFudGUgcGFyYSBxdWFscXVlciBpbnZlcnNhIGdlbmVyYWxpemFkYSBlc2NvbGhpZGEsIGdhcmFudGluZG8gcXVlIGFzIHByZXZpc8O1ZXMgZG8gbW9kZWxvIHNlamFtIGVzdMOhdmVpcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hLCBKLiBHLiAmIEVzdGV2ZXMsIEUuIE0uLCBJbnRyb2R1w6fDo28gYW9zIE1vZGVsb3MgTGluZWFyZXMsIENhcCAyLCBwLiA1MC01MSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJEYWRhIHVtYSBtYXRyaXogJEEgPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwIFxcXFwgMCAmIDAgXFxlbmR7cG1hdHJpeH0kLCB2ZXJpZmlxdWUgc2UgYSBtYXRyaXogJEFeKyA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAwICYgMCBcXGVuZHtwbWF0cml4fSQgc2F0aXNmYXogYXMgcXVhdHJvIGNvbmRpw6fDtWVzIGRlIFBlbnJvc2UuIEp1c3RpZmlxdWUgZGV0YWxoYWRhbWVudGUgY2FkYSBjb25kacOnw6NvLiIsICJkaWNhIjogIkNhbGN1bGUgcGFzc28gYSBwYXNzbyBvcyBwcm9kdXRvcyBtYXRyaWNpYWlzICRBIEFeKyBBJCwgJEFeKyBBIEFeKyQsIGUgdmVyaWZpcXVlIGEgc2ltZXRyaWEgJChBIEFeKylee1xcdG9wfSQgZSAkKEFeKyBBKV57XFx0b3B9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMSkgVmVyaWZpY2FuZG8gJEEgQV4rIEEgPSBBJDogJEEgQV4rID0gXFxiZWdpbntwbWF0cml4fSAxICYgMCBcXFxcIDAgJiAwIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAwICYgMCBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAwICYgMCBcXGVuZHtwbWF0cml4fSQuIExvZ28sICRBIEFeKyBBID0gXFxiZWdpbntwbWF0cml4fSAxICYgMCBcXFxcIDAgJiAwIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAwICYgMCBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAwICYgMCBcXGVuZHtwbWF0cml4fSA9IEEkLiBDb25kacOnw6NvIHNhdGlzZmVpdGEuIiwgIjIpIFZlcmlmaWNhbmRvICRBXisgQSBBXisgPSBBXiskOiAkQV4rIEEgPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwIFxcXFwgMCAmIDAgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSAxICYgMCBcXFxcIDAgJiAwIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAxICYgMCBcXFxcIDAgJiAwIFxcZW5ke3BtYXRyaXh9JC4gTG9nbywgJEFeKyBBIEFeKyA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAwICYgMCBcXGVuZHtwbWF0cml4fSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwIFxcXFwgMCAmIDAgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwIFxcXFwgMCAmIDAgXFxlbmR7cG1hdHJpeH0gPSBBXiskLiBDb25kacOnw6NvIHNhdGlzZmVpdGEuIiwgIjMpIFZlcmlmaWNhbmRvICQoQSBBXispXntcXHRvcH0gPSBBIEFeKyQ6ICRBIEFeKyA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAwICYgMCBcXGVuZHtwbWF0cml4fSQsIHF1ZSDDqSB1bWEgbWF0cml6IGRpYWdvbmFsIGUsIHBvcnRhbnRvLCBcXHNpbcOpdHJpY2EuIENvbmRpw6fDo28gc2F0aXNmZWl0YS4iLCAiNCkgVmVyaWZpY2FuZG8gJChBXisgQSlee1xcdG9wfSA9IEFeKyBBJDogJEFeKyBBID0gXFxiZWdpbntwbWF0cml4fSAxICYgMCBcXFxcIDAgJiAwIFxcZW5ke3BtYXRyaXh9JCwgcXVlIHRhbWLDqW0gw6kgXFxzaW3DqXRyaWNhLiBDb25kacOnw6NvIHNhdGlzZmVpdGEuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIGRvIHBvbnRvIGRlIHZpc3RhIGRhIGdlb21ldHJpYSB2ZXRvcmlhbCwgcG9yIHF1ZSBhIGNvbmRpw6fDo28gJChBIEFeKylee1xcdG9wfSA9IEEgQV4rJCDDqSBmdW5kYW1lbnRhbCBwYXJhIHF1ZSAkQSBBXiskIHNlamEgY29uc2lkZXJhZGEgdW1hIHByb2plw6fDo28gb3J0b2dvbmFsIGUgbsOjbyBhcGVuYXMgdW1hIHByb2plw6fDo28gb2Jsw61xdWEuIiwgImRpY2EiOiAiQ29uc2lkZXJlIG8gdGVvcmVtYSBkYSBkZWNvbXBvc2nDp8OjbyBvcnRvZ29uYWwgZGUgdW0gdmV0b3IgZSBhIGRlZmluacOnw6NvIGRlIG1hdHJpeiBkZSBwcm9qZcOnw6NvICRQJC4gTyBxdWUgb2NvcnJlIHF1YW5kbyB1bWEgbWF0cml6IMOpIGlkZW1wb3RlbnRlIG1hcyBuw6NvIFxcc2ltw6l0cmljYT8iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiVW1hIG1hdHJpeiAkUCQgw6kgdW1hIHByb2plw6fDo28gc2UgZm9yIGlkZW1wb3RlbnRlLCBvdSBzZWphLCAkUF4yID0gUCQuIiwgIlVtYSBwcm9qZcOnw6NvIMOpIGRpdGEgb3J0b2dvbmFsIHNlLCBlIHNvbWVudGUgc2UsIGVsYSBmb3IgXFxzaW3DqXRyaWNhLCAkUF57XFx0b3B9ID0gUCQuIiwgIlNlIHVtYSBtYXRyaXogJFAkIMOpIGFwZW5hcyBpZGVtcG90ZW50ZSwgZWxhIHByb2pldGEgdW0gdmV0b3IgJHYkIGVtIHVtIHN1YmVzcGHDp28gYW8gbG9uZ28gZGUgdW0gc3ViZXNwYcOnbyBjb21wbGVtZW50YXIsIG1hcyBhIGRpcmXDp8OjbyBkZXNzYSBwcm9qZcOnw6NvIG7Do28gw6kgbmVjZXNzYXJpYW1lbnRlIG9ydG9nb25hbCBhbyBzdWJlc3Bhw6dvIGRlIGRlc3Rpbm8uIiwgIkEgY29uZGnDp8OjbyAkKEEgQV4rKV57XFx0b3B9ID0gQSBBXiskIGdhcmFudGUgcXVlIG8gcmVzw61kdW8gZGEgcHJvamXDp8OjbyAkKEkgLSBBIEFeKyl2JCBzZWphIG9ydG9nb25hbCBhbyBlc3Bhw6dvIGNvbHVuYSAkQyhBKSQuIiwgIlNlbSBhIHNpbWV0cmlhLCBvIGVycm8gZGUgcHJvamXDp8OjbyBuw6NvIGVzdGFyaWEgbWluaW1pemFkbyBlbSBub3JtYSBldWNsaWRpYW5hLCBvIHF1ZSBpbnZhbGlkYXJpYSBhIHByb3ByaWVkYWRlIGRlICdtZW5vciBub3JtYScgZG8gZXN0aW1hZG9yIGRlIE1vb3JlLVBlbnJvc2UuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiU2VqYSAkQSQgdW1hIG1hdHJpeiBkZSBwb3N0byBjb21wbGV0byBkZSBjb2x1bmFzLiBNb3N0cmUgcXVlIGEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlIHBvZGUgc2VyIGV4cHJlc3NhIGNvbW8gJEFeKyA9IChBXntcXHRvcH0gQSleey0xfSBBXntcXHRvcH0kLiBWZXJpZmlxdWUgc2UgZXN0YSBleHByZXNzw6NvIHNhdGlzZmF6IGEgcHJpbWVpcmEgY29uZGnDp8OjbyBkZSBQZW5yb3NlICgkQSBBXisgQSA9IEEkKS4iLCAiZGljYSI6ICJTdWJzdGl0dWEgJEFeKyQgbmEgY29uZGnDp8OjbyAoMSkgZSB1dGlsaXplIGFzIHByb3ByaWVkYWRlcyBkYSDDoWxnZWJyYSBtYXRyaWNpYWwuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlF1ZXJlbW9zIHZlcmlmaWNhciBzZSAkQSBBXisgQSA9IEEkIGNvbSAkQV4rID0gKEFee1xcdG9wfSBBKV57LTF9IEFee1xcdG9wfSQuIiwgIlN1YnN0aXR1aW5kbyBuYSBleHByZXNzw6NvOiAkQSBbKEFee1xcdG9wfSBBKV57LTF9IEFee1xcdG9wfV0gQSQuIiwgIlBlbGEgYXNzb2NpYXRpdmlkYWRlIGRhIG11bHRpcGxpY2HDp8OjbyBtYXRyaWNpYWwsIHRlbW9zOiAkQSAoQV57XFx0b3B9IEEpXnstMX0gKEFee1xcdG9wfSBBKSQuIiwgIlNhYmVtb3MgcXVlICQoQV57XFx0b3B9IEEpXnstMX0gKEFee1xcdG9wfSBBKSA9IEkkLCBvbmRlICRJJCDDqSBhIG1hdHJpeiBpZGVudGlkYWRlIGRlIGRpbWVuc8OjbyBhcHJvcHJpYWRhLiIsICJMb2dvLCBhIGV4cHJlc3PDo28gc2UgcmVkdXogYSAkQSBcXGNkb3QgSSA9IEEkLiIsICJQb3J0YW50bywgJEEgQV4rIEEgPSBBJCwgY29uZmlybWFuZG8gcXVlIGVzdGEgZm9ybWEgZGEgaW52ZXJzYSBzYXRpc2ZheiBhIHByaW1laXJhIGNvbmRpw6fDo28gZGUgUGVucm9zZS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJEYWRhIGEgbWF0cml6ICRBID0gXFxiZWdpbntwbWF0cml4fSAxICYgMSAmIDEgXFxcXCAxICYgLTEgJiAxIFxcXFwgMiAmIDIgJiAyIFxcZW5ke3BtYXRyaXh9JCwgZW5jb250cmUgdW1hIGludmVyc2EgZ2VuZXJhbGl6YWRhIGNvbmRpY2lvbmFsICRBXnstfSQgdXRpbGl6YW5kbyBvIGFsZ29yaXRtbyBkZSBTZWFybGUuIERldGFsaGUgY2FkYSBwYXNzbyBkbyBwcm9jZXNzby4iLCAiZGljYSI6ICJPIHBvc3RvIGRhIG1hdHJpeiAkcihBKSQgw6kgZXNzZW5jaWFsLiBPYnNlcnZlIGEgZGVwZW5kw6puY2lhIGxpbmVhciBlbnRyZSBhcyBsaW5oYXMgMSBlIDMuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIERldGVybWluYXIgbyBwb3N0bzogT2JzZXJ2YW1vcyBxdWUgYSBsaW5oYSAzIMOpIG8gZG9icm8gZGEgbGluaGEgMSwgbG9nbyAkcihBKSA9IDIkLiIsICIyLiBFc2NvbGhlciBhIHN1Ym1hdHJpeiAkTSQgZGUgcG9zdG8gMjogUG9kZW1vcyB0b21hciAkTSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgXFxcXCAxICYgLTEgXFxlbmR7cG1hdHJpeH0kIChwcmltZWlyYXMgZHVhcyBsaW5oYXMgZSBkdWFzIGNvbHVuYXMpLiIsICIzLiBJbnZlcnRlciAkTSQ6ICRcXGRldChNKSA9IC0xIC0gMSA9IC0yJC4gJE1eey0xfSA9IFxcZnJhY3sxfXstMn0gXFxiZWdpbntwbWF0cml4fSAtMSAmIC0xIFxcXFwgLTEgJiAxIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAwLjUgJiAwLjUgXFxcXCAwLjUgJiAtMC41IFxcZW5ke3BtYXRyaXh9JC4iLCAiNC4gVHJhbnNwb3IgJE1eey0xfSQ6ICQoTV57LTF9KV57XFx0b3B9ID0gXFxiZWdpbntwbWF0cml4fSAwLjUgJiAwLjUgXFxcXCAwLjUgJiAtMC41IFxcZW5ke3BtYXRyaXh9JC4iLCAiNS4gQWxvY2FyIGVtIG1hdHJpeiAkMyBcXHRpbWVzIDMkIGUgdHJhbnNwb3I6IFN1YnN0aXR1aW5kbyBlbSAkQSQgZSBhbnVsYW5kbyBvIHJlc3RvLCB0ZW1vcyAkXFxiZWdpbntwbWF0cml4fSAwLjUgJiAwLjUgJiAwIFxcXFwgMC41ICYgLTAuNSAmIDAgXFxcXCAwICYgMCAmIDAgXFxlbmR7cG1hdHJpeH0kLiBUcmFuc3BvbmRvLCBvYnRlbW9zICRBXnstfSA9IFxcYmVnaW57cG1hdHJpeH0gMC41ICYgMC41ICYgMCBcXFxcIDAuNSAmIC0wLjUgJiAwIFxcXFwgMCAmIDAgJiAwIFxcZW5ke3BtYXRyaXh9JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJOw612ZWEgQmlzcG8sIEF1bGEgOTogSW52ZXJzYSBHZW5lcmFsaXphZGEgZGUgTWF0cml6ZXMsIERFU1QtVUZCQSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyBzaXN0ZW1hIGRlIGVxdWHDp8O1ZXMgbGluZWFyZXMgJEF4ID0gZyQgb25kZSAkQSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgXFxcXCAxICYgLTEgXFxcXCAtMiAmIDAgXFxlbmR7cG1hdHJpeH0kIGUgJGcgPSBcXGJlZ2lue3BtYXRyaXh9IDMgXFxcXCAxIFxcXFwgLTQgXFxlbmR7cG1hdHJpeH0kLiBEZXRlcm1pbmUgc2UgbyBzaXN0ZW1hIMOpIGNvbnNpc3RlbnRlIHV0aWxpemFuZG8gYSBjb25kacOnw6NvICRBQV57LX1nID0gZyQsIGNvbSAkQV57LX0gPSBcXGJlZ2lue3BtYXRyaXh9IDAuNSAmIDAuNSAmIDAgXFxcXCAwLjUgJiAtMC41ICYgMCBcXGVuZHtwbWF0cml4fSQuIiwgImRpY2EiOiAiTyBzaXN0ZW1hIMOpIGNvbnNpc3RlbnRlIHNlLCBlIHNvbWVudGUgc2UsICRBQV57LX1nID0gZyQuIFJlYWxpemUgYSBtdWx0aXBsaWNhw6fDo28gbWF0cmljaWFsIHBhc3NvIGEgcGFzc28uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIENhbGN1bGFyICRBQV57LX0kOiAkXFxiZWdpbntwbWF0cml4fSAxICYgMSBcXFxcIDEgJiAtMSBcXFxcIC0yICYgMCBcXGVuZHtwbWF0cml4fSBcXGJlZ2lue3BtYXRyaXh9IDAuNSAmIDAuNSAmIDAgXFxcXCAwLjUgJiAtMC41ICYgMCBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgJiAwIFxcXFwgMCAmIDEgJiAwIFxcXFwgLTEgJiAtMSAmIDAgXFxlbmR7cG1hdHJpeH0kLiIsICIyLiBQcsOpLW11bHRpcGxpY2FyIHBvciAkZyQ6ICRcXGJlZ2lue3BtYXRyaXh9IDEgJiAwICYgMCBcXFxcIDAgJiAxICYgMCBcXFxcIC0xICYgLTEgJiAwIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMyBcXFxcIDEgXFxcXCAtNCBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMyBcXFxcIDEgXFxcXCAtNCBcXGVuZHtwbWF0cml4fSQuIiwgIjMuIENvbXBhcmFyIGNvbSAkZyQ6IENvbW8gJEFBXnstfWcgPSBnJCwgbyBzaXN0ZW1hIMOpIGNvbnNpc3RlbnRlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEsIEouIEcuICYgRXN0ZXZlcywgRS4gTS4sIENhcCAyLCBwLiA0OSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJEYWRhIGEgbWF0cml6ICRBID0gXFxiZWdpbntwbWF0cml4fSA0ICYgMiBcXFxcIDIgJiAyIFxcZW5ke3BtYXRyaXh9JCAocXVlIMOpIFxcc2ltw6l0cmljYSksIGNhbGN1bGUgYSBzdWEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlICRBXnsrfSQuIiwgImRpY2EiOiAiQ29tbyBhIG1hdHJpeiDDqSBxdWFkcmFkYSBlIFxcc2ltw6l0cmljYSwgcG9kZS1zZSB1c2FyIGEgZGVjb21wb3Npw6fDo28gZXNwZWN0cmFsICRBID0gUFxcTGFtYmRhIFBee1xcdG9wfSQsIG9uZGUgJEFeeyt9ID0gUFxcTGFtYmRhXnsrfVBee1xcdG9wfSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIEVuY29udHJhciBhdXRvdmFsb3JlcyBkZSAkQSQ6ICRcXGRldChBIC0gXFxsYW1iZGEgSSkgPSAoNC1cXGxhbWJkYSkoMi1cXGxhbWJkYSkgLSA0ID0gXFxsYW1iZGFeMiAtIDZcXGxhbWJkYSArIDQgPSAwJC4gJFxcbGFtYmRhID0gXFxmcmFjezYgXFxwbSBcXHNxcnR7MzYtMTZ9fXsyfSA9IDMgXFxwbSBcXHNxcnR7NX0kLiIsICIyLiBDb21vIGEgbWF0cml6IMOpIG7Do28tc2luZ3VsYXIgKCRcXGRldChBKSA9IDQgXFxuZXEgMCQpLCAkQV57K30gPSBBXnstMX0kLiIsICIzLiBDYWxjdWxhciAkQV57LTF9ID0gXFxmcmFjezF9e1xcZGV0KEEpfSBhZGooQSkgPSBcXGZyYWN7MX17NH0gXFxiZWdpbntwbWF0cml4fSAyICYgLTIgXFxcXCAtMiAmIDQgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDAuNSAmIC0wLjUgXFxcXCAtMC41ICYgMSBcXGVuZHtwbWF0cml4fSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjV9XX0=').decode('utf-8'))


    import plotly.graph_objects as go
    
    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    mcq_questions = dados_exercicios.get("questoes_multipla_escolha", [])
    disc_questions = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcq_questions) + len(disc_questions)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    # Interface de Progresso
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    
    st.divider()
    
    # Seção de Múltipla Escolha
    st.subheader("📝 Questões de Múltipla Escolha")
    for i, questao in enumerate(mcq_questions):
        st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', 'Enunciado não disponível')}")
        
        # Renderização de gráfico se existir
        codigo = questao.get("codigo_plotly")
        if codigo:
            local_vars = {}
            try:
                exec(codigo, {"go": go}, local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
            except Exception as e:
                st.error("Erro ao carregar o gráfico interativo.")
    
        alternativas = questao.get("alternativas", {})
        escolha = st.radio(
            "Selecione a alternativa correta:",
            options=list(alternativas.keys()),
            format_func=lambda x: f"{x}: {alternativas[x]}",
            key=f"radio_mcq_{i}"
        )
    
        if st.button("💡 Dica", key=f"dica_mcq_{i}"):
            st.info(questao.get("dica", "Dica indisponível"))
    
        if questao.get("referencia_livro"):
            st.markdown(f"📖 *Referência: {questao.get('referencia_livro')}*")
    
        if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
            if escolha == questao.get("alternativa_correta"):
                st.success("Correto! Muito bem.")
                st.session_state.respostas_certas[f"mcq_{i}"] = True
                st.rerun()
            else:
                st.error("Resposta incorreta. Tente novamente!")
                st.session_state.respostas_certas[f"mcq_{i}"] = False
                st.rerun()
    
        with st.expander("✅ Ver Gabarito Comentado"):
            st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
        st.divider()
    
    # Seção de Discursivas
    st.subheader("✍️ Questões Discursivas")
    for i, questao in enumerate(disc_questions):
        st.markdown(f"**Questão Discursiva {i+1}:** {questao.get('enunciado', 'Enunciado não disponível')}")
        
        codigo = questao.get("codigo_plotly")
        if codigo:
            local_vars = {}
            try:
                exec(codigo, {"go": go}, local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
            except Exception:
                pass
    
        st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
    
        if questao.get("referencia_livro"):
            st.markdown(f"📖 *Referência: {questao.get('referencia_livro')}*")
        
        if st.button("💡 Dica", key=f"dica_disc_{i}"):
            st.info(questao.get("dica", "Dica indisponível"))
    
        esperada = questao.get("resposta_numerica_esperada")
        if esperada is not None:
            val = st.number_input("Digite o resultado numérico para validação:", key=f"num_disc_{i}", format="%f")
            if st.button("Validar Cálculo", key=f"btn_calc_{i}"):
                if abs(val - esperada) <= max(0.01, 0.01 * abs(esperada)):
                    st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                    st.rerun()
                else:
                    st.error("O valor calculado difere do gabarito oficial. Verifique e tente novamente.")
                    st.session_state.respostas_certas[f"disc_{i}"] = False
                    st.rerun()
        else:
            concluido = st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}")
            if concluido:
                st.session_state.respostas_certas[f"disc_{i}"] = True
            else:
                st.session_state.respostas_certas[f"disc_{i}"] = False
    
        with st.expander("✅ Ver Resolução Detalhada"):
            passos = questao.get("gabarito_passo_a_passo", [])
            for p_idx, passo in enumerate(passos):
                st.write(f"{p_idx+1}. {passo}")
        st.divider()
