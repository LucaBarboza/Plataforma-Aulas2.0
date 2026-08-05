import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDEgLSBUw7NwaWNvIDEuMTogRm9ybWFzIGVzcGVjaWFpcyBkZSB2ZXRvcmVzIGUgbWF0cml6ZXMsIGFwbGljYcOnw7VlcyBlbSBFc3RhdMOtc3RpY2FzOiBlbmZvcXVlIGNvbXB1dGFjaW9uYWwiLCAicmVmZXJlbmNpYXNfYmlibGlvZ3JhZmljYXNfZmluYWlzIjogWyJMdW5hICYgRXN0ZXZlcywgTW9kZWxvcyBMaW5lYXJlcyAtIENhcC4gMSwgcHAuIDQtNywgOC0xMCwgMTQtMTYsIDI0LTI1IiwgIkJpc3BvLCBJbnRyb2R1w6fDo28gYW9zIE1vZGVsb3MgTGluZWFyZXMgLSBBdWxhIDMsIHBwLiAxMi0xOCwgcHAuIDEzLTE0LCBBdWxhcyA0LTYsIHBwLiA5LTExIl19').decode('utf-8'))

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
    
    # Título do Subtópico
    st.header(r"Estruturas Fundamentais: Vetores e Matrizes no Contexto Computacional")
    
    # Introdução Teórica
    st.markdown(r"""
    A transição da análise estatística clássica, realizada em grande parte de maneira manual, para a estatística computacional contemporânea, marca uma verdadeira revolução na forma como concebemos o dado. À medida que a ciência avança para modelos multivariados de alta complexidade, a manipulação escalar torna-se logisticamente impossível.
    """)
    
    st.info(r"A álgebra linear revela-se como a linguagem fundamental do estatístico moderno, transformando a massa bruta de informações em estruturas organizadas e computacionalmente tratáveis.")
    
    st.markdown(r"""
    Para organizar essa complexidade, utilizamos duas estruturas principais:
    *   **Vetor:** Representa uma única característica medida através de uma amostra de tamanho $n$.
    *   **Matriz:** O arranjo definitivo, onde cada linha representa uma unidade amostral ($i$) e cada coluna representa uma variável ($j$).
    """)
    
    # Formalismo Matemático
    st.markdown(r"### 📐 A Estrutura Formal: Representação Matricial")
    st.latex(r"\mathbf{A}_{(n \times m)} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1m} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nm} \end{pmatrix}")
    
    st.markdown(r"""
    Esta notação viabiliza a **vetorização das operações**, permitindo que processadores apliquem instruções de forma paralela, resultando em ganhos de performance que reduzem o tempo de convergência de horas para milissegundos.
    """)
    
    # Deduções Analíticas
    st.markdown(r"### 🧮 O Rigor Analítico: Regressão Linear Múltipla")
    st.latex(r"\mathbf{y}_{(n \times 1)} = \begin{pmatrix} y_1 & y_2 & \cdots & y_n \end{pmatrix}^\top")
    st.write(r"O modelo de regressão é expresso pela equação matricial:")
    st.latex(r"\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}")
    st.write(r"Onde as dimensões se equilibram perfeitamente:")
    st.latex(r"\text{Dim}(\mathbf{X}\boldsymbol{\beta}) = (n \times k) \times (k \times 1) = (n \times 1)")
    st.latex(r"\text{Dim}(\mathbf{y}) = (n \times 1) \implies \text{Dim}(\mathbf{y}) = \text{Dim}(\mathbf{X}\boldsymbol{\beta})")
    
    # Simulador Interativo
    st.markdown(r"### 🖥️ Simulador: Construtor de Matriz de Delineamento")
    st.write(r"Utilize o editor abaixo para definir sua matriz de desenho $\mathbf{X}$ (3x2) e observar a transformação geométrica no produto $\mathbf{X}^{\top}\mathbf{X}$.")
    
    col_a, col_b = st.columns([1, 1])
    
    with col_a:
        df_input = pd.DataFrame(
            [[20.0, 100.0], [25.0, 110.0], [30.0, 120.0]],
            columns=["Var 1", "Var 2"]
        )
        edited_df = st.data_editor(df_input, key=r"editor_matriz_subtopico_1")
        X = edited_df.values
        XtX = X.T @ X
    
    with col_b:
        st.markdown(r"**Resultado de $\mathbf{X}^{\top}\mathbf{X}$:**")
        st.latex(np.array2string(XtX, precision=2, separator=', '))
    
    # Plotagem do Simulador
    fig = go.Figure()
    fig.add_trace(go.Heatmap(
        z=XtX,
        colorscale="Blues",
        showscale=True
    ))
    fig.update_layout(
        title=dict(text=r"<b>Visualização da Matriz de Momentos (XtX)</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        xaxis=dict(title=dict(text=r"Coluna", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Linha", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    st.info(rf"O determinante resultante é {np.linalg.det(XtX):.2f}. Valores próximos a zero indicam alta multicolinearidade, tornando a matriz instável para inversão.")
    
    # Exemplo Prático
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Experimento Clínico")
        st.markdown(r"Considere um experimento relacionando resposta $y$ com temperatura e pressão para $n=3$ observações.")
        st.latex(r"\mathbf{X} = \begin{pmatrix} 20 & 100 \\ 25 & 110 \\ 30 & 120 \end{pmatrix}")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- 1. Transposição: Obter $\mathbf{X}^{\top}$ invertendo linhas e colunas.")
        st.markdown(r"- 2. Produto Interno: Realizar a multiplicação matricial $\mathbf{X}^{\top}\mathbf{X}$.")
        st.markdown(r"- 3. Síntese: O resultado $\begin{pmatrix} 1925 & 8850 \\ 8850 & 40700 \end{pmatrix}$ reduz os dados para uma forma tratável.")
        st.success(r"A matriz resultante é o núcleo do estimador de mínimos quadrados, permitindo a calibração precisa do modelo estatístico.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    
    # Cabeçalho do Subtópico
    st.header(r"Operações Matriciais e a Álgebra das Transformações Lineares")
    
    # Introdução e Contexto
    st.markdown(r"""
    A álgebra matricial é a espinha dorsal do processamento computacional em estatística, permitindo manipular grandes bases de dados coletivamente. Longe de ser apenas um arranjo mecânico de números, ela constitui a linguagem fundamental na qual a estatística multivariada é articulada.
    """)
    
    st.info(r"Ao adotarmos a notação de matrizes e vetores, transcendemos a visão bidimensional, concebendo o conjunto de dados como um único objeto matemático — um ponto em um espaço de alta dimensão cuja geometria revela estruturas ocultas.")
    
    st.markdown(r"""
    ### 📐 Fundamentos das Transformações Lineares
    Quando operamos com matrizes, estamos essencialmente realizando transformações sobre vetores. O processo de multiplicação matricial, frequentemente reduzido a uma regra de 'linha por coluna', deve ser compreendido como um mapeamento linear que reorienta o espaço amostral:
    
    - **Combinação Linear:** Ao multiplicar uma matriz de dados $\mathbf{X}$ por um vetor de pesos $\mathbf{w}$, criamos índices compostos ou valores preditos.
    - **Dualidade:** A transposição $\mathbf{X}^{\top}$ permite alternar o foco entre observações e a co-variação entre variáveis.
    - **Projeção Ortogonal:** A resolução de sistemas, como na regressão linear, é geometricamente a projeção do vetor de resposta sobre o espaço coluna da matriz de desenho.
    """)
    
    # Formalismo Matemático
    st.subheader(r"O Coração Matemático: Composição de Transformações")
    st.latex(r"r_{ik} = \sum_{j=1}^{m} a_{ij}c_{jk}")
    
    # Dedução Analítica das Linhas
    st.markdown(r"Abaixo, demonstramos a propriedade de transposição do produto de duas matrizes:")
    st.latex(r"(\mathbf{AB})^{\top} \text{ possui elementos na posição } (k,i) \text{ iguais a } r_{ik} \text{ do produto original.}")
    st.latex(r"r_{ik} = \sum_{j=1}^{m} a_{ij}b_{jk}")
    st.latex(r"(\mathbf{AB})^{\top}_{ki} = \sum_{j=1}^{m} a_{ij}b_{jk}")
    st.latex(r"(\mathbf{AB})^{\top}_{ki} = \sum_{j=1}^{m} (\mathbf{B}^{\top})_{kj} (\mathbf{A}^{\top})_{ji}")
    st.latex(r"(\mathbf{AB})^{\top} = \mathbf{B}^{\top}\mathbf{A}^{\top}")
    
    # Casos de Aplicação Prática
    st.subheader(r"📈 Casos de Aplicação Prática: Agregação em IoT")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Média Ponderada Diária")
        st.markdown(r"Considere dois dias de dados de um sensor IoT (temperatura em graus Celsius). Temos a matriz $\mathbf{D}_{(2 \times 2)}$ e o vetor de pesos $\mathbf{w}_{(2 \times 1)}$. Calcule o vetor de médias diárias $\mathbf{y} = \mathbf{D}\mathbf{w}$.")
        st.latex(r"\mathbf{D} = \begin{pmatrix} 20 & 22 \\ 21 & 23 \end{pmatrix}, \mathbf{w} = \begin{pmatrix} 0.5 \\ 0.5 \end{pmatrix}")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- $\mathbf{y} = \begin{pmatrix} (20 \cdot 0.5 + 22 \cdot 0.5) \\ (21 \cdot 0.5 + 23 \cdot 0.5) \end{pmatrix}$")
        st.markdown(r"- $\mathbf{y} = \begin{pmatrix} (10 + 11) \\ (10.5 + 11.5) \end{pmatrix}$")
        st.markdown(r"- $\mathbf{y} = \begin{pmatrix} 21 \\ 22 \end{pmatrix}$")
        st.success(r"O vetor resultante $[21, 22]^{\top}$ representa as médias ponderadas diárias do sensor, demonstrando a eficiência da notação matricial para agregação de dados em sistemas de monitoramento em tempo real.")
    
    # Simulador conceitual de Projeção (Visualização de Vetores)
    st.subheader(r"💻 Simulador Visual: Projeção de Variáveis")
    col1, col2 = st.columns([1, 2])
    with col1:
        angulo = st.slider(r"Ângulo de projeção (graus)", 0, 90, 30, key=r"angulo_projecao_subtopico_2")
        mostrar_proj = st.toggle(r"Exibir Vetor Projeção", True, key=r"toggle_proj_subtopico_2")
    
    # Lógica do Gráfico
    rad = np.radians(angulo)
    v1 = [1, 0]
    v2 = [np.cos(rad), np.sin(rad)]
    proj = [np.cos(rad), 0]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, v1[0]], y=[0, v1[1]], mode="lines+markers", name=r"Variável X", line=dict(color="#1E3A8A", width=3)))
    fig.add_trace(go.Scatter(x=[0, v2[0]], y=[0, v2[1]], mode="lines+markers", name=r"Variável Y", line=dict(color="#10B981", width=3)))
    
    if mostrar_proj:
        fig.add_trace(go.Scatter(x=[0, proj[0]], y=[0, proj[1]], mode="lines", name=r"Projeção", line=dict(color="#991B1B", dash="dash")))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Geometria de Projeção Vetorial</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Dimensão 1", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Dimensão 2", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    st.info(r"Ao manipular o ângulo entre as variáveis, observamos a mudança na correlação: quanto menor o ângulo, maior a colinearidade entre as direções no espaço vetorial, refletindo a dependência estatística entre os dados.")

    # Cabeçalho do Subtópico
    st.header(r"Propriedades e Tipologias: Matrizes Simétricas, Idempotentes e Ortogonais")
    
    # Introdução Teórica
    st.markdown(r"""
    Na jornada pela Estatística Matemática e modelos lineares, o domínio da Álgebra Matricial não é um exercício de abstração, mas o alicerce da inferência multivariada e da teoria de mínimos quadrados. Estruturas matriciais especiais conferem elegância, parcimônia e estabilidade computacional aos procedimentos estatísticos, transformando problemas de otimização em operações de álgebra linear direta.
    """)
    
    # Seção: Matrizes Simétricas
    st.subheader(r"📐 Simetria: A Essência das Relações de Covariância")
    st.markdown(r"""
    As matrizes simétricas representam a comutatividade das relações de covariância. Uma matriz $\mathbf{A}$ é simétrica se atende à condição abaixo:
    """)
    st.latex(r"\mathbf{A} = \mathbf{A}^{\top}")
    st.markdown(r"""
    **Principais Implicações:**
    * **Covariância:** A covariância entre $X_i$ e $X_j$ é idêntica à covariância entre $X_j$ e $X_i$, definindo a estrutura das matrizes $\Sigma$.
    * **Teorema Espectral:** Garantimos que todos os autovalores são reais e que os autovetores associados a autovalores distintos são ortogonais.
    * **Redução de Dimensionalidade:** Esta propriedade é a base fundamental para a Análise de Componentes Principais (PCA), permitindo a projeção de dados em subespaços de variação máxima.
    """)
    
    # Seção: Matrizes Idempotentes
    st.subheader(r"🏗️ Idempotência: Operadores de Projeção no Espaço Coluna")
    st.markdown(r"""
    Uma matriz $\mathbf{A}$ é dita idempotente quando a aplicação do operador não altera o resultado após a primeira transformação, ou seja, $\mathbf{A} \mathbf{A} = \mathbf{A}$. Na teoria de modelos lineares, essas matrizes são os operadores que realizam a projeção ortogonal.
    """)
    
    # Dedução Analítica (Fora de expander conforme diretrizes)
    st.markdown(r"**Demonstração da Idempotência da Matriz Chapéu ($\mathbf{P}$):**")
    st.latex(r"\mathbf{P} = \mathbf{X}(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}")
    st.latex(r"\mathbf{P}^2 = \mathbf{X}(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top} \cdot \mathbf{X}(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}")
    st.latex(r"\mathbf{P}^2 = \mathbf{X}(\mathbf{X}^{\top}\mathbf{X})^{-1} (\mathbf{X}^{\top}\mathbf{X}) (\mathbf{X}^{\top}\mathbf{X})^{-1} \mathbf{X}^{\top}")
    st.latex(r"\mathbf{P}^2 = \mathbf{X}(\mathbf{X}^{\top}\mathbf{X})^{-1} \mathbf{I} \mathbf{X}^{\top} = \mathbf{P}")
    st.markdown(r"""
    O resultado confirma que projetar um vetor no espaço coluna de $\mathbf{X}$ duas vezes é o mesmo que projetá-lo apenas uma vez, mantendo a integridade da partição da soma de quadrados total.
    """)
    
    # Seção: Matrizes Ortogonais
    st.subheader(r"🛡️ Ortogonalidade: Estabilidade e Preservação Geométrica")
    st.markdown(r"""
    As matrizes ortogonais representam o epítome da preservação da estrutura geométrica, mantendo a norma euclidiana e os ângulos entre vetores após transformações lineares.
    """)
    st.latex(r"\mathbf{A}\mathbf{A}^{\top} = \mathbf{I}")
    st.info(r"Em algoritmos como a Decomposição QR, utilizamos transformações ortogonais para garantir estabilidade numérica, blindando o sistema contra o acúmulo de erros de arredondamento e garantindo que a informação não seja distorcida.")
    
    # Seção: O papel do Traço
    st.subheader(r"🧮 O Traço e os Graus de Liberdade")
    st.markdown(r"O traço, definido como a soma dos elementos da diagonal principal, possui propriedades cíclicas vitais para a inferência:")
    st.latex(r"\text{tr}(\mathbf{A}) = \sum_{i=1}^{n} a_{ii}")
    st.markdown(r"""
    Para matrizes idempotentes, o posto da matriz é numericamente idêntico ao seu traço, $r(\mathbf{A}) = \text{tr}(\mathbf{A})$, permitindo a identificação imediata dos graus de liberdade estatísticos.
    """)
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Cálculo do Traço em Projeções")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Traço da Matriz de Projeção")
        st.markdown(r"Considere o operador de projeção $\mathbf{P} = \mathbf{X}(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}$ usado na regressão. Calcule o traço de $\mathbf{P}$ para uma matriz com $k=2$ colunas.")
        st.latex(r"k=2, \mathbf{P} \text{ idempotente}")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- $\text{tr}(\mathbf{P}) = \text{tr}(\mathbf{X}(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top})$")
        st.markdown(r"- Utilizando a propriedade cíclica $\text{tr}(\mathbf{AB}) = \text{tr}(\mathbf{BA})$: $\text{tr}(\mathbf{P}) = \text{tr}(\mathbf{X}^{\top}\mathbf{X}(\mathbf{X}^{\top}\mathbf{X})^{-1})$")
        st.markdown(r"- Resultando em $\text{tr}(\mathbf{I}_{(k)}) = k$")
        st.success(r"O traço igual a 2 confirma que o modelo de regressão consome 2 graus de liberdade do sistema, uma análise crítica para determinar a complexidade do modelo em relação ao número de observações.")

    # Importações necessárias (assumindo que o ambiente possui estas bibliotecas básicas)
    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    
    # Cabeçalho do Subtópico
    st.header(r"Decomposição Espectral e Estrutura de Autovalores")
    
    # Introdução e Contextualização
    st.markdown(r"""
    A compreensão profunda da álgebra linear, especificamente no que tange à decomposição de matrizes, constitui a pedra angular sobre a qual repousa toda a estrutura da estatística multivariada contemporânea. 
    Quando nos deparamos com uma matriz quadrada simétrica, como a nossa matriz de covariância populacional $\Sigma$, não estamos diante de um mero conjunto de números dispostos em uma grade, mas sim diante de uma representação de um operador linear que descreve a estrutura de variabilidade e dependência entre múltiplas variáveis aleatórias.
    """)
    
    st.info(r"A decomposição espectral emerge como uma ferramenta analítica indispensável que nos permite desmontar essa complexidade, identificando as direções principais ao longo das quais os dados se estendem e quantificando o quão importante é cada uma dessas direções.")
    
    st.markdown(r"""
    Historicamente, a aplicação desses conceitos na análise de componentes principais revolucionou a capacidade humana de visualizar dimensões que transcendem a nossa percepção. Antes desta adoção, pesquisadores enfrentavam imensas dificuldades em interpretar sistemas onde as variáveis eram altamente correlacionadas, resultando em uma redundância informacional que mascarava os padrões subjacentes. 
    A decomposição espectral resolve este dilema ao realizar uma rotação ortogonal do espaço original para um novo sistema de coordenadas, onde os eixos são não correlacionados.
    """)
    
    # O Coração Matemático
    st.subheader(r"📐 O Coração Matemático: Formalismo Espectral")
    
    st.markdown(r"O formalismo matemático é encapsulado pela expressão fundamental da decomposição de uma matriz simétrica $\mathbf{A}$:")
    
    st.latex(r"\mathbf{A} = \sum_{i=1}^{n} \lambda_i \mathbf{u}_i \mathbf{u}_i^{\top}")
    
    st.markdown(r"""
    Nesta construção:
    *   **$\lambda_i$**: Representam os autovalores, que quantificam a magnitude da variância ao longo da direção definida.
    *   **$\mathbf{u}_i$**: São os autovetores, que servem como uma base ortonormal para o espaço vetorial.
    *   **Hierarquia de Variância**: Ao ordenar $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n \ge 0$, isolamos as componentes mais informativas das de ruído.
    """)
    
    # Demonstração Analítica
    st.subheader(r"🧮 Dedução da Estrutura de Autovalores")
    
    st.markdown(r"Abaixo, apresentamos os passos lógicos que sustentam a decomposição de uma matriz simétrica:")
    
    st.latex(r"\mathbf{A} \mathbf{U} = \mathbf{U} \mathbf{\Lambda}")
    st.markdown(r"Assumindo que $\mathbf{U}$ é ortogonal, temos que $\mathbf{U}^{\top} = \mathbf{U}^{-1}$. Multiplicando à direita:")
    st.latex(r"\mathbf{A} \mathbf{U} \mathbf{U}^{\top} = \mathbf{U} \mathbf{\Lambda} \mathbf{U}^{\top}")
    st.markdown(r"Como $\mathbf{U} \mathbf{U}^{\top} = \mathbf{I}$, chegamos à representação espectral final:")
    st.latex(r"\mathbf{A} = \mathbf{U} \mathbf{\Lambda} \mathbf{U}^{\top}")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Análise de Variabilidade")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Variabilidade em Sistema Industrial")
        st.markdown(r"Dada a matriz de covariância $\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, determine seus autovalores para verificar a variabilidade do processo.")
        
        st.latex(r"\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Montagem do polinômio característico: $|\mathbf{A} - \lambda \mathbf{I}| = 0 \implies (2-\lambda)^2 - 1 = 0$")
        st.markdown(r"- Resolução da equação quadrática: $\lambda^2 - 4\lambda + 3 = 0$")
        st.markdown(r"- Cálculo das raízes: $(\lambda - 3)(\lambda - 1) = 0 \implies \lambda_1 = 3, \lambda_2 = 1$")
        
        st.success(r"Com autovalores 3 e 1, o sistema industrial apresenta três vezes mais variabilidade na direção do primeiro autovetor do que na direção do segundo, indicando uma dominância clara de um fator sobre o outro na variabilidade dos dados.")
    
    # Reflexão Final
    st.markdown(r"""
    ---
    ### 💡 Síntese Didática
    A decomposição espectral transcende a mera computação matricial, permitindo realizar uma 'filtragem' espectral, onde retemos a essência dos dados e descartamos dimensões de baixa variância. Esta prática é o fundamento para a redução de dimensionalidade e técnicas de regularização, garantindo que a simplificação do modelo não comprometa o rigor estatístico.
    """)

    import streamlit as st
    import numpy as np
    import pandas as pd
    
    # Cabeçalho do subtópico
    st.header(r"Formas Quadráticas, Definições de Positividade e Inversas Generalizadas")
    
    # Prosa teórica estruturada
    st.markdown(r"""
    A transição entre a álgebra linear básica e a estatística multivariada exige uma compreensão profunda de como as estruturas matriciais encapsulam a geometria dos dados. As formas quadráticas emergem como a linguagem fundamental para representar a variabilidade e a dispersão em sistemas estocásticos.
    """)
    
    st.info(r"A forma quadrática é definida pela expressão abaixo, onde a matriz A pondera as interações entre os componentes de um vetor de variáveis x.")
    st.latex(r"Q(\mathbf{x}) = \mathbf{x}^{\top}\mathbf{A}\mathbf{x}")
    
    st.markdown(r"""
    ### 📊 A Geometria da Variabilidade
    Em estatística, operamos frequentemente com matrizes de covariância $\Sigma$. A forma quadrática permite:
    - Calcular a **Distância de Mahalanobis** em espaços de alta dimensão.
    - Determinar a **variância** de combinações lineares de variáveis aleatórias.
    - Estabelecer a consistência física e probabilística através da **positividade**.
    
    Exigir que $\mathbf{A}$ seja definida positiva garante que $Q(\mathbf{x}) > 0$ para todo vetor não nulo $\mathbf{x}$, assegurando que medidas de variância não sejam negativas. Quando a matriz é apenas semidefinida positiva, reconhecemos a presença de **colinearidade perfeita**, reduzindo a dimensionalidade efetiva do sistema.
    """)
    
    # Formalismo e Deduções
    st.subheader(r"📐 O Coração Matemático: Inversão Generalizada e Moore-Penrose")
    st.markdown(r"""
    Quando matrizes de informação são singulares, a inversa tradicional $\mathbf{A}^{-1}$ deixa de existir. A **Inversa de Moore-Penrose** ($\mathbf{A}^{+}$) permite resolver sistemas lineares inconsistentes projetando o sistema sobre o subespaço viável.
    """)
    
    st.latex(r"\mathbf{A}\mathbf{A}^{+}\mathbf{A} = \mathbf{A}")
    
    st.markdown(r"A dedução baseada na Decomposição em Valores Singulares (SVD) segue o rigor lógico abaixo:")
    st.latex(r"\text{Dada SVD: } \mathbf{A} = \mathbf{U}\mathbf{D}\mathbf{V}^{\top}")
    st.latex(r"\text{Definição: } \mathbf{A}^{+} = \mathbf{V}\mathbf{D}^{+}\mathbf{U}^{\top}")
    st.latex(r"\text{Verificação: } \mathbf{A}\mathbf{A}^{+}\mathbf{A} = (\mathbf{U}\mathbf{D}\mathbf{V}^{\top})(\mathbf{V}\mathbf{D}^{+}\mathbf{U}^{\top})(\mathbf{U}\mathbf{D}\mathbf{V}^{\top})")
    st.latex(r"\mathbf{U}\mathbf{D}(\mathbf{V}^{\top}\mathbf{V})\mathbf{D}^{+}(\mathbf{U}^{\top}\mathbf{U})\mathbf{D}\mathbf{V}^{\top} = \mathbf{U}\mathbf{D}\mathbf{D}^{+}\mathbf{D}\mathbf{V}^{\top} = \mathbf{A}")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Regressão em Sistemas Singulares")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Estimação com Multicolinearidade")
        st.markdown(r"Resolva o sistema de mínimos quadrados $\mathbf{X}\hat{\theta} = \mathbf{y}$ onde a redundância das variáveis explicativas impede a inversão direta da matriz de momentos.")
        
        st.latex(r"\mathbf{X} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \\ 1 & 0 \\ 1 & 0 \end{pmatrix}, \quad \mathbf{y} = \begin{pmatrix} 4 \\ 3 \\ 4 \\ 4 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo da matriz de momentos: $\mathbf{X}^{\top}\mathbf{X} = \begin{pmatrix} 4 & 2 \\ 2 & 2 \end{pmatrix}$")
        st.markdown(r"- Inversão da matriz (não singular neste caso simples, mas ilustrativa): $(\mathbf{X}^{\top}\mathbf{X})^{-1} = \begin{pmatrix} 0.5 & -0.5 \\ -0.5 & 1.0 \end{pmatrix}$")
        st.markdown(r"- Obtenção da pseudoinversa: $\mathbf{X}^{+} = (\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top} = \begin{pmatrix} 0 & 0 & 0.5 & 0.5 \\ 0.5 & 0.5 & -0.5 & -0.5 \end{pmatrix}$")
        st.markdown(r"- Solução para $\hat{\theta}$: $\hat{\theta} = \mathbf{X}^{+}\mathbf{y} = \begin{pmatrix} 4 \\ -0.5 \end{pmatrix}$")
        
        st.success(r"O vetor de estimativas $[4, -0.5]^{\top}$ minimiza a norma do resíduo quadrático. A utilização da inversa generalizada garante que, mesmo diante de redundância perfeita ou sistemas subdeterminados, o modelo estatístico produza uma solução de norma mínima robusta.")
    
    # Nota Final de Fechamento
    st.markdown(r"""
    ---
    *Nota: A teoria das formas quadráticas e da inversa de Moore-Penrose constitui a base para técnicas avançadas como a Análise de Componentes Principais (PCA) e a Regressão Ridge, fundamentais para a ciência de dados moderna.*
    """)

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDEgLSBUw7NwaWNvIDEuMTogRm9ybWFzIGVzcGVjaWFpcyBkZSB2ZXRvcmVzIGUgbWF0cml6ZXMsIGFwbGljYcOnw7VlcyBlbSBFc3RhdMOtc3RpY2FzOiBlbmZvcXVlIGNvbXB1dGFjaW9uYWwiLCAicXVlc3RvZXNfbXVsdGlwbGFfZXNjb2xoYSI6IFt7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gY2zDrW5pY28gcGFyYSBhdmFsaWFyIG8gaW1wYWN0byBkZSBub3ZvcyBwcm90b2NvbG9zIGRlIHRyYXRhbWVudG8sIHZvY8OqIGNvbGV0b3UgZGFkb3MgZGUgMTUgcGFjaWVudGVzIGRpc3RpbnRvcy4gUGFyYSBjYWRhIGluZGl2w61kdW8sIGZvcmFtIHJlZ2lzdHJhZGFzIDQgdmFyacOhdmVpczogaWRhZGUsIHBlc28sIGFsdHVyYSBlIMOtbmRpY2UgZGUgcHJlc3PDo28gYXJ0ZXJpYWwuIEFvIG9yZ2FuaXphciBlc3NlcyBkYWRvcyBlbSB1bWEgZXN0cnV0dXJhIGNvbXB1dGFjaW9uYWwgbWF0cmljaWFsICRcXG1hdGhiZntBfSQsIG9uZGUgY2FkYSBsaW5oYSByZXByZXNlbnRhIHVtIHBhY2llbnRlIGUgY2FkYSBjb2x1bmEgcmVwcmVzZW50YSB1bWEgdmFyacOhdmVsLCBxdWFsIMOpIGEgZGltZW5zw6NvIGNvcnJldGEgZGEgbWF0cml6ICRcXG1hdGhiZntBfSQgZSBjb21vIGVsYSDDqSBkZW5vdGFkYSBzZWd1bmRvIG8gZm9ybWFsaXNtbyBtYXRyaWNpYWwgcGFkcsOjbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgbWF0cml6ICRcXG1hdGhiZntBfSQgcG9zc3VpIGRpbWVuc8OjbyAkKDQgXFx0aW1lcyAxNSkkLCBzZW5kbyBkZW5vdGFkYSBjb21vICRcXG1hdGhiZntBfV97KDQgXFx0aW1lcyAxNSl9JC4iLCAiQiI6ICJBIG1hdHJpeiAkXFxtYXRoYmZ7QX0kIHBvc3N1aSBkaW1lbnPDo28gJCgxNSBcXHRpbWVzIDQpJCwgc2VuZG8gZGVub3RhZGEgY29tbyAkXFxtYXRoYmZ7QX1feygxNSBcXHRpbWVzIDQpfSQuIiwgIkMiOiAiQSBtYXRyaXogJFxcbWF0aGJme0F9JCDDqSB1bSB2ZXRvciBjb2x1bmEgZGUgZGltZW5zw6NvICQoNjAgXFx0aW1lcyAxKSQsIGRlbm90YWRvIGNvbW8gJFxcbWF0aGJme0F9X3soNjAgXFx0aW1lcyAxKX0kLiIsICJEIjogIkEgbWF0cml6ICRcXG1hdGhiZntBfSQgcG9zc3VpIGRpbWVuc8OjbyAkKDE1IFxcdGltZXMgMTUpJCwgcG9pcyBkZXZlIHNlciBxdWFkcmFkYSBwYXJhIHBlcm1pdGlyIGPDoWxjdWxvcyBlc3RhdMOtc3RpY29zLCBkZW5vdGFkYSBjb21vICRcXG1hdGhiZntBfV97KDE1IFxcdGltZXMgMTUpfSQuIiwgIkUiOiAiQSBkaW1lbnPDo28gZGEgbWF0cml6IMOpIGluZGV0ZXJtaW5hZGEgc2VtIGEgZXNwZWNpZmljYcOnw6NvIGRvcyB2YWxvcmVzIHJlYWlzIGRhcyBtZWRpZGFzIGRlIGNhZGEgcGFjaWVudGUuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIGVtIGVzdGF0w61zdGljYSBjb21wdXRhY2lvbmFsLCBhIGNvbnZlbsOnw6NvIHBhZHLDo28gb3JnYW5pemEgb3MgZGFkb3MgZGUgdGFsIGZvcm1hIHF1ZSBvIG7Dum1lcm8gZGUgbGluaGFzICgkbiQpIGNvcnJlc3BvbmRlIMOgcyBvYnNlcnZhw6fDtWVzIChhbW9zdHJhcykgZSBvIG7Dum1lcm8gZGUgY29sdW5hcyAoJG0kKSBjb3JyZXNwb25kZSDDoHMgdmFyacOhdmVpcyAoY2FyYWN0ZXLDrXN0aWNhcykuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGRlZmluacOnw6NvIGZvcm1hbCBkZSB1bWEgbWF0cml6ICRcXG1hdGhiZntBfV97KG4gXFx0aW1lcyBtKX0kIGVzdGFiZWxlY2UgcXVlICRuJCDDqSBvIG7Dum1lcm8gZGUgbGluaGFzIGUgJG0kIMOpIG8gbsO6bWVybyBkZSBjb2x1bmFzLiBDb21vIHRlbW9zIDE1IHBhY2llbnRlcyAob2JzZXJ2YcOnw7VlcywgJG49MTUkKSBlIDQgdmFyacOhdmVpcyAoY2FyYWN0ZXLDrXN0aWNhcywgJG09NCQpLCBhIGVzdHJ1dHVyYSByZXN1bHRhbnRlIMOpIHVtYSBtYXRyaXogZGUgMTUgbGluaGFzIGUgNCBjb2x1bmFzLCBkZW5vdGFkYSBwb3IgJFxcbWF0aGJme0F9X3soMTUgXFx0aW1lcyA0KX0kLiBBIGFsdGVybmF0aXZhIEIgw6kgYSDDum5pY2EgcXVlIHJlc3BlaXRhIGVzc2Egb3JkZW5hw6fDo28gZnVuZGFtZW50YWwgZGUgZGFkb3MgYW1vc3RyYWlzLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtIHZldG9yIGNvbHVuYSAkXFxtYXRoYmZ7dn0gPSAodl8xLCB2XzIsIFxcZG90cywgdl9uKV5cXHRvcCQuIE5vIHByb2Nlc3NhbWVudG8gZXN0YXTDrXN0aWNvLCBmcmVxdWVudGVtZW50ZSBwcmVjaXNhbW9zIHRyYW5zcG9yIHZldG9yZXMgcGFyYSByZWFsaXphciBvcGVyYcOnw7VlcyBkZSBwcm9kdXRvIGludGVybm8gb3UgYWp1c3RhciBkaW1lbnPDtWVzIGVtIG1vZGVsb3MgbGluZWFyZXMuIFNlIGFwbGljYXJtb3MgYSBvcGVyYcOnw6NvIGRlIHRyYW5zcG9zacOnw6NvIGFvIHZldG9yICRcXG1hdGhiZnt2fSQsIHF1YWwgZGFzIGFmaXJtYcOnw7VlcyBhYmFpeG8gZGVzY3JldmUgY29ycmV0YW1lbnRlIGEgbmF0dXJlemEgZSBhIGVzdHJ1dHVyYSBkbyByZXN1bHRhZG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIHJlc3VsdGFkbyDDqSB1bSBlc2NhbGFyLCBjYWxjdWxhZG8gY29tbyBhIHNvbWEgZG9zIGVsZW1lbnRvcyBkbyB2ZXRvciBvcmlnaW5hbC4iLCAiQiI6ICJPIHJlc3VsdGFkbyDDqSB1bSBub3ZvIHZldG9yIGNvbHVuYSBkZSBkaW1lbnPDo28gJChuIFxcdGltZXMgMSkkLCBpZMOqbnRpY28gYW8gb3JpZ2luYWwuIiwgIkMiOiAiTyByZXN1bHRhZG8gw6kgdW0gdmV0b3IgbGluaGEgZGUgZGltZW5zw6NvICQoMSBcXHRpbWVzIG4pJCwgZGVub3RhZG8gcG9yICRcXG1hdGhiZnt2fV5cXHRvcCA9ICh2XzEsIHZfMiwgXFxkb3RzLCB2X24pJC4iLCAiRCI6ICJBIHRyYW5zcG9zacOnw6NvIGRlIHVtIHZldG9yIGNvbHVuYSDDqSBwcm9pYmlkYSBuYSDDoWxnZWJyYSBtYXRyaWNpYWwsIGRldmVuZG8tc2UgdXRpbGl6YXIgYXBlbmFzIG1hdHJpemVzIHF1YWRyYWRhcy4iLCAiRSI6ICJPIHJlc3VsdGFkbyDDqSB1bWEgbWF0cml6IGRpYWdvbmFsIGNvbSBvcyBlbGVtZW50b3MgZGUgJFxcbWF0aGJme3Z9JCBuYSBkaWFnb25hbCBwcmluY2lwYWwuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJBIG9wZXJhw6fDo28gZGUgdHJhbnNwb3Npw6fDo28gdHJvY2EgYXMgbGluaGFzIHBlbGFzIGNvbHVuYXMuIFNlIG8gdmV0b3Igb3JpZ2luYWwgdGVtIHVtYSBjb2x1bmEgZSAkbiQgbGluaGFzLCBvIHRyYW5zcG9zdG8gdGVyw6EgdW1hIGxpbmhhIGUgJG4kIGNvbHVuYXMuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQb3IgZGVmaW5pw6fDo28sIHVtIHZldG9yIGNvbHVuYSDDqSB1bWEgbWF0cml6IGRlIGRpbWVuc8OjbyAkKG4gXFx0aW1lcyAxKSQuIEFvIGFwbGljYXIgYSB0cmFuc3Bvc2nDp8OjbywgYSBkaW1lbnPDo28gZGEgbWF0cml6IHJlc3VsdGFudGUgw6kgaW52ZXJ0aWRhIHBhcmEgJCgxIFxcdGltZXMgbikkLiBPIHZldG9yICRcXG1hdGhiZnt2fV5cXHRvcCQgcGFzc2EgYSBzZXIgdW0gYXJyYW5qbyBob3Jpem9udGFsICh2ZXRvciBsaW5oYSkgY29udGVuZG8gb3MgbWVzbW9zIGVsZW1lbnRvcyBuYSBtZXNtYSBvcmRlbSwgc2F0aXNmYXplbmRvIGEgZGVmaW5pw6fDo28gbWF0ZW3DoXRpY2EgZGUgdHJhbnNwb3Npw6fDo28gZGUgbWF0cml6ZXMuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBhbmFsaXN0YSBkZSBkYWRvcyB0cmFiYWxoYSBjb20gdW1hIG1hdHJpeiBkZSBvYnNlcnZhw6fDtWVzICRcXG1hdGhiZntYfSQgZGUgZGltZW5zw6NvICQobiBcXHRpbWVzIG0pJCwgb25kZSAkbj0xMDAkIHJlcHJlc2VudGFtIG9zIGNsaWVudGVzIGUgJG09NSQgcmVwcmVzZW50YW0gYXMgY2FyYWN0ZXLDrXN0aWNhcyBzb2Npb2Vjb27DtG1pY2FzLiBQYXJhIHJlYWxpemFyIHVtYSByZWR1w6fDo28gZGUgZGltZW5zaW9uYWxpZGFkZSBsaW5lYXIsIGVsZSBtdWx0aXBsaWNhIGVzdGEgbWF0cml6IHBvciB1bWEgbWF0cml6IGRlIHBlc29zICRcXG1hdGhiZntXfSQgZGUgZGltZW5zw6NvICQobSBcXHRpbWVzIDIpJC4gUXVhbCDDqSBhIGRpbWVuc8OjbyBkYSBtYXRyaXogcmVzdWx0YW50ZSAkXFxtYXRoYmZ7Un0gPSBcXG1hdGhiZntYfVxcbWF0aGJme1d9JCBlIHF1YWwgYSBjb25kacOnw6NvIGRlIGNvbmZvcm1pZGFkZSBmdW5kYW1lbnRhbCBwYXJhIHF1ZSBlc3RlIHByb2R1dG8gbWF0cmljaWFsIHNlamEgbWF0ZW1hdGljYW1lbnRlIHBvc3PDrXZlbD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkRpbWVuc8OjbyAkKDEwMCBcXHRpbWVzIDIpJDsgbyBuw7ptZXJvIGRlIGNvbHVuYXMgZGUgJFxcbWF0aGJme1h9JCBkZXZlIHNlciBpZ3VhbCBhbyBuw7ptZXJvIGRlIGxpbmhhcyBkZSAkXFxtYXRoYmZ7V30kLiIsICJCIjogIkRpbWVuc8OjbyAkKDUgXFx0aW1lcyAyKSQ7IG8gbsO6bWVybyBkZSBsaW5oYXMgZGUgJFxcbWF0aGJme1h9JCBkZXZlIHNlciBpZ3VhbCBhbyBuw7ptZXJvIGRlIGNvbHVuYXMgZGUgJFxcbWF0aGJme1d9JC4iLCAiQyI6ICJEaW1lbnPDo28gJCgxMDAgXFx0aW1lcyA1KSQ7IGFzIGRpbWVuc8O1ZXMgZGFzIG1hdHJpemVzIGRldmVtIHNlciBvYnJpZ2F0b3JpYW1lbnRlIGlkw6pudGljYXMuIiwgIkQiOiAiRGltZW5zw6NvICQoMiBcXHRpbWVzIDEwMCkkOyBvIG7Dum1lcm8gZGUgY29sdW5hcyBkZSAkXFxtYXRoYmZ7V30kIGRldmUgc2VyIGlndWFsIGFvIG7Dum1lcm8gZGUgbGluaGFzIGRlICRcXG1hdGhiZntYfSQuIiwgIkUiOiAiRGltZW5zw6NvICQoNTAgXFx0aW1lcyAyKSQ7IG8gbsO6bWVybyBkZSBjb2x1bmFzIGRlICRcXG1hdGhiZntYfSQgZGV2ZSBzZXIgaWd1YWwgYW8gbsO6bWVybyBkZSBjb2x1bmFzIGRlICRcXG1hdGhiZntXfSQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgcmVncmEgZGUgb3VybyBkYSBtdWx0aXBsaWNhw6fDo28gbWF0cmljaWFsOiBwYXJhIG8gcHJvZHV0byAkXFxtYXRoYmZ7QX1feyhuIFxcdGltZXMgbSl9IFxcbWF0aGJme0J9X3sobSBcXHRpbWVzIGMpfSA9IFxcbWF0aGJme1J9X3sobiBcXHRpbWVzIGMpfSQsIG9zIMOtbmRpY2VzIGludGVybm9zIGRldmVtIGNvaW5jaWRpci4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBhcmEgcmVhbGl6YXIgbyBwcm9kdXRvIG1hdHJpY2lhbCAkXFxtYXRoYmZ7WH1feyhuIFxcdGltZXMgbSl9IFxcbWF0aGJme1d9X3sobSBcXHRpbWVzIGMpfSQsIGEgY29uZGnDp8OjbyBkZSBjb25mb3JtaWRhZGUgZXhpZ2UgcXVlIG8gbsO6bWVybyBkZSBjb2x1bmFzIGRhIHByaW1laXJhIG1hdHJpeiAoJG09NSQpIHNlamEgaWd1YWwgYW8gbsO6bWVybyBkZSBsaW5oYXMgZGEgc2VndW5kYSBtYXRyaXogKCRtPTUkKS4gTyByZXN1bHRhZG8gw6kgdW1hIG5vdmEgbWF0cml6ICRcXG1hdGhiZntSfSQgY3VqYXMgZGltZW5zw7VlcyBzw6NvIGRhZGFzIHBlbG8gbsO6bWVybyBkZSBsaW5oYXMgZGEgcHJpbWVpcmEgbWF0cml6ICgkbj0xMDAkKSBlIG8gbsO6bWVybyBkZSBjb2x1bmFzIGRhIHNlZ3VuZGEgbWF0cml6ICgkYz0yJCksIHJlc3VsdGFuZG8gZW0gJCgxMDAgXFx0aW1lcyAyKSQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgZHVhcyBtYXRyaXplcyBkZSBkYWRvcyAkXFxtYXRoYmZ7QX1feyhuIFxcdGltZXMgbSl9JCBlICRcXG1hdGhiZntCfV97KG4gXFx0aW1lcyBtKX0kLiBTZSByZWFsaXphcm1vcyBhIG9wZXJhw6fDo28gZGUgdHJhbnNwb3Npw6fDo28gbmEgc29tYSBkZXNzYXMgbWF0cml6ZXMsIG91IHNlamEsICQoXFxtYXRoYmZ7QX0gKyBcXG1hdGhiZntCfSlee1xcdG9wfSQsIHF1YWwgZGFzIGlndWFsZGFkZXMgYWJhaXhvIGRlc2NyZXZlIGNvcnJldGFtZW50ZSBhIMOhbGdlYnJhIGRhcyB0cmFuc2Zvcm1hw6fDtWVzIGxpbmVhcmVzPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJChcXG1hdGhiZntBfSArIFxcbWF0aGJme0J9KV57XFx0b3B9ID0gXFxtYXRoYmZ7QX1ee1xcdG9wfSBcXG1hdGhiZntCfV57XFx0b3B9JCIsICJCIjogIiQoXFxtYXRoYmZ7QX0gKyBcXG1hdGhiZntCfSlee1xcdG9wfSA9IFxcbWF0aGJme0J9XntcXHRvcH0gKyBcXG1hdGhiZntBfV57XFx0b3B9JCIsICJDIjogIiQoXFxtYXRoYmZ7QX0gKyBcXG1hdGhiZntCfSlee1xcdG9wfSA9IFxcbWF0aGJme0F9ICsgXFxtYXRoYmZ7Qn0kIiwgIkQiOiAiJChcXG1hdGhiZntBfSArIFxcbWF0aGJme0J9KV57XFx0b3B9ID0gXFxtYXRoYmZ7QX1ee1xcdG9wfSArIFxcbWF0aGJme0J9XntcXHRvcH0kIiwgIkUiOiAiJChcXG1hdGhiZntBfSArIFxcbWF0aGJme0J9KV57XFx0b3B9ID0gXFxtYXRoYmZ7Qn0gKyBcXG1hdGhiZntBfSQifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiRCIsICJkaWNhIjogIkEgdHJhbnNwb3Npw6fDo28gw6kgdW0gb3BlcmFkb3IgbGluZWFyIHF1ZSBwcmVzZXJ2YSBhIHNvbWEuIFBlbnNlIHF1ZSBvIGVsZW1lbnRvIG5hIHBvc2nDp8OjbyAkKGksaikkIGRhIHNvbWEgb3JpZ2luYWwgw6kgJGFfe2lqfSArIGJfe2lqfSQsIGUgbmEgdHJhbnNwb3N0YSBlbGUgZGV2ZSBpciBwYXJhIGEgcG9zacOnw6NvICQoaixpKSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIHByb3ByaWVkYWRlIGZ1bmRhbWVudGFsIGRhIHRyYW5zcG9zacOnw6NvIGVtIHNvbWFzIG1hdHJpY2lhaXMgw6kgcXVlIGEgdHJhbnNwb3N0YSBkYSBzb21hIMOpIGlndWFsIMOgIHNvbWEgZGFzIHRyYW5zcG9zdGFzOiAkKFxcbWF0aGJme0F9ICsgXFxtYXRoYmZ7Qn0pXntcXHRvcH0gPSBcXG1hdGhiZntBfV57XFx0b3B9ICsgXFxtYXRoYmZ7Qn1ee1xcdG9wfSQuIE5vdGUgcXVlIGEgYWx0ZXJuYXRpdmEgQiB0YW1iw6ltIMOpIHRlY25pY2FtZW50ZSB2ZXJkYWRlaXJhIHBlbGEgcHJvcHJpZWRhZGUgY29tdXRhdGl2YSBkYSBhZGnDp8OjbywgbWFzIGEgZm9ybWEgRCDDqSBhIGV4cHJlc3PDo28gZGlyZXRhIGRhIHByb3ByaWVkYWRlIGRvIG9wZXJhZG9yIHRyYW5zcG9zacOnw6NvIGFwbGljYWRhIGxpbmVhcm1lbnRlIGEgY2FkYSB0ZXJtby4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBkZSBtb2RlbGFnZW0gbGluZWFyIG5hIGVuZ2VuaGFyaWEgZGUgc2Vuc29yZXMgSW9ULCB1bSBwZXNxdWlzYWRvciB0cmFiYWxoYSBjb20gdW1hIG1hdHJpeiBkZSBwcm9qZcOnw6NvICRcXG1hdGhiZntQfSQgcXVlIMOpIGRlZmluaWRhIGEgcGFydGlyIGRhIG1hdHJpeiBkZSBwcm9qZXRvICRcXG1hdGhiZntYfSQgY29tbyAkXFxtYXRoYmZ7UH0gPSBcXG1hdGhiZntYfShcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0pXnstMX1cXG1hdGhiZntYfV57XFx0b3B9JCwgb25kZSAkXFxtYXRoYmZ7WH0kIHBvc3N1aSBwb3N0byBjb2x1bmEgY29tcGxldG8uIFNhYmVuZG8gcXVlIGVzc2EgbWF0cml6IMOpIGZ1bmRhbWVudGFsIHBhcmEgbyBjw6FsY3VsbyBkb3MgdmFsb3JlcyBwcmVkaXRvcyAkXFxoYXR7XFxtYXRoYmZ7eX19ID0gXFxtYXRoYmZ7UH1cXG1hdGhiZnt5fSQsIGFzc2luYWxlIGEgYWx0ZXJuYXRpdmEgcXVlIGRlc2NyZXZlIGNvcnJldGFtZW50ZSBhcyBwcm9wcmllZGFkZXMgbWF0ZW3DoXRpY2FzIGRhIG1hdHJpeiAkXFxtYXRoYmZ7UH0kLiIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBtYXRyaXogJFxcbWF0aGJme1B9JCDDqSBzZW1wcmUgaW52ZXJ0w612ZWwsIGluZGVwZW5kZW50ZW1lbnRlIGRhIG1hdHJpeiAkXFxtYXRoYmZ7WH0kLiIsICJCIjogIkEgbWF0cml6ICRcXG1hdGhiZntQfSQgw6kgXFxzaW3DqXRyaWNhIGUgaWRlbXBvdGVudGUsIGdhcmFudGluZG8gcXVlICRcXG1hdGhiZntQfV4yID0gXFxtYXRoYmZ7UH0kIGUgJFxcbWF0aGJme1B9ID0gXFxtYXRoYmZ7UH1ee1xcdG9wfSQuIiwgIkMiOiAiTyB0cmHDp28gZGEgbWF0cml6ICRcXG1hdGhiZntQfSQsICRcXHRleHR7dHJ9KFxcbWF0aGJme1B9KSQsIMOpIHNlbXByZSBpZ3VhbCDDoCBkaW1lbnPDo28gZGEgbWF0cml6ICRcXG1hdGhiZntYfSQgdG90YWwuIiwgIkQiOiAiQSBtYXRyaXogJFxcbWF0aGJme1B9JCDDqSBvYnJpZ2F0b3JpYW1lbnRlIHVtYSBtYXRyaXogb3J0b2dvbmFsLCBzYXRpc2ZhemVuZG8gJFxcbWF0aGJme1B9XntcXHRvcH1cXG1hdGhiZntQfSA9IFxcbWF0aGJme0l9X3sobil9JC4iLCAiRSI6ICJBIG1hdHJpeiAkXFxtYXRoYmZ7UH0kIG7Do28gcG9zc3VpIHJlbGHDp8OjbyBjb20gcHJvamXDp8O1ZXMgZ2VvbcOpdHJpY2FzLCBzZW5kbyBhcGVuYXMgdW1hIHRyYW5zZm9ybWHDp8OjbyBsaW5lYXIgYXJiaXRyw6FyaWEuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgZGVmaW5pw6fDo28gZGUgbWF0cml6IGRlIHByb2plw6fDo28gb3J0b2dvbmFsIGUgZGEgY2FyYWN0ZXLDrXN0aWNhIGRlIGlkZW1wb3TDqm5jaWEgZW0gbW9kZWxvcyBkZSByZWdyZXNzw6NvIGxpbmVhci4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgbWF0cml6ICRcXG1hdGhiZntQfSA9IFxcbWF0aGJme1h9KFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfVxcbWF0aGJme1h9XntcXHRvcH0kIMOpIGEgbWF0cml6IGRlIHByb2plw6fDo28gKG91IG1hdHJpeiBjaGFww6l1KS4gRWxhIMOpIFxcc2ltw6l0cmljYSwgcG9pcyAkXFxtYXRoYmZ7UH1ee1xcdG9wfSA9IChcXG1hdGhiZntYfShcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0pXnstMX1cXG1hdGhiZntYfV57XFx0b3B9KV57XFx0b3B9ID0gXFxtYXRoYmZ7WH0oKFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfSlee1xcdG9wfVxcbWF0aGJme1h9XntcXHRvcH0gPSBcXG1hdGhiZntYfShcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0pXnstMX1cXG1hdGhiZntYfV57XFx0b3B9ID0gXFxtYXRoYmZ7UH0kLiBBbMOpbSBkaXNzbywgw6kgaWRlbXBvdGVudGU6ICRcXG1hdGhiZntQfV4yID0gXFxtYXRoYmZ7WH0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9XFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfVxcbWF0aGJme1h9XntcXHRvcH0gPSBcXG1hdGhiZntYfVxcbWF0aGJme0l9KFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfVxcbWF0aGJme1h9XntcXHRvcH0gPSBcXG1hdGhiZntQfSQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgQ2FwIDIsIHAuIDQwIn0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bWEgbWF0cml6IGRlIHRyYW5zacOnw6NvICRcXG1hdGhiZntBfV97KG4gXFx0aW1lcyBuKX0kIHV0aWxpemFkYSBlbSB1bSBhbGdvcml0bW8gZGUgcHJvY2Vzc2FtZW50byBkZSBzaW5haXMsIHRhbCBxdWUgJFxcbWF0aGJme0F9XntcXHRvcH1cXG1hdGhiZntBfSA9IFxcbWF0aGJme0F9XFxtYXRoYmZ7QX1ee1xcdG9wfSA9IFxcbWF0aGJme0l9X3sobil9JC4gUXVhbCBkYXMgc2VndWludGVzIHByb3ByaWVkYWRlcyDDqSB2ZXJkYWRlaXJhIHNvYnJlIGVzdGEgbWF0cml6PyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBtYXRyaXogJFxcbWF0aGJme0F9JCDDqSBuZWNlc3NhcmlhbWVudGUgaWRlbXBvdGVudGUsIGxvZ28gJFxcbWF0aGJme0F9XjIgPSBcXG1hdGhiZntBfSQuIiwgIkIiOiAiTyB0cmHDp28gZGEgbWF0cml6ICRcXG1hdGhiZntBfSQgw6kgaWd1YWwgYSB6ZXJvLCBzZW1wcmUuIiwgIkMiOiAiQSBtYXRyaXogJFxcbWF0aGJme0F9JCBwcmVzZXJ2YSBvIHByb2R1dG8gaW50ZXJubyBlIGEgbm9ybWEgZXVjbGlkaWFuYSwgY2FyYWN0ZXJpemFuZG8tYSBjb21vIHVtYSBtYXRyaXogb3J0b2dvbmFsLiIsICJEIjogIkEgbWF0cml6ICRcXG1hdGhiZntBfSQgZGV2ZSBwb3NzdWlyIGF1dG92YWxvcmVzIGVzdHJpdGFtZW50ZSBwb3NpdGl2b3MgZSBtZW5vcmVzIHF1ZSAxLiIsICJFIjogIkEgbWF0cml6ICRcXG1hdGhiZntBfSQgbsOjbyDDqSB1bWEgbWF0cml6IGludmVydMOtdmVsLCBwb2lzIHN1YSBpbnZlcnNhIG7Do28gZXhpc3RlLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiQW5hbGlzZSBhIGRlZmluacOnw6NvIGRhZGEgbm8gZW51bmNpYWRvOiAkXFxtYXRoYmZ7QX1ee1xcdG9wfVxcbWF0aGJme0F9ID0gXFxtYXRoYmZ7SX0kLiBRdWFsIHRpcG8gZGUgbWF0cml6IHBvc3N1aSBlc3NhIGNhcmFjdGVyw61zdGljYSBkZSBpbnZlcnNpYmlsaWRhZGUgb25kZSBhIHRyYW5zcG9zdGEgw6kgaWd1YWwgw6AgaW52ZXJzYT8iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBlbGEgZGVmaW5pw6fDo28gZm9ybmVjaWRhLCAkXFxtYXRoYmZ7QX1ee1xcdG9wfVxcbWF0aGJme0F9ID0gXFxtYXRoYmZ7QX1cXG1hdGhiZntBfV57XFx0b3B9ID0gXFxtYXRoYmZ7SX1feyhuKX0kLCBhIG1hdHJpeiDDqSBvcnRvZ29uYWwuIE1hdHJpemVzIG9ydG9nb25haXMgcHJlc2VydmFtIGEgbm9ybWEgKGNvbXByaW1lbnRvKSBlIG8gw6JuZ3VsbyBlbnRyZSB2ZXRvcmVzLCBmdW5jaW9uYW5kbyBjb21vIHRyYW5zZm9ybWHDp8O1ZXMgZGUgcm90YcOnw6NvIG91IHJlZmxleMOjbywgc2VuZG8gZXNzZW5jaWFpcyBwYXJhIGEgZXN0YWJpbGlkYWRlIG51bcOpcmljYSBlbSBhbGdvcml0bW9zIGRldmlkbyDDoCBwcmVzZXJ2YcOnw6NvIGRhIG5vcm1hIGV1Y2xpZGlhbmEuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gZGUgb3RpbWl6YcOnw6NvIGRlIHByb2Nlc3NvcyBpbmR1c3RyaWFpcywgYSBtYXRyaXogZGUgY292YXJpw6JuY2lhICRcXG1hdGhiZntBfV97KDMgXFx0aW1lcyAzKX0kIGVudHJlIHRyw6pzIHNlbnNvcmVzIGRlIHRlbXBlcmF0dXJhIGZvaSBkZXRlcm1pbmFkYSBjb21vIHNlbmRvIHVtYSBtYXRyaXogXFxzaW3DqXRyaWNhIGN1am9zIGF1dG92YWxvcmVzIHPDo28gJFxcbGFtYmRhXzEgPSAxMi4wJCwgJFxcbGFtYmRhXzIgPSAzLjAkIGUgJFxcbGFtYmRhXzMgPSAwLjUkLiBTYWJlbmRvIHF1ZSBhIGRlY29tcG9zacOnw6NvIGVzcGVjdHJhbCBwZXJtaXRlIHJlcHJlc2VudGFyIGEgbWF0cml6IGNvbW8gJFxcbWF0aGJme0F9ID0gXFxzdW1fe2k9MX1eezN9IFxcbGFtYmRhX2kgXFxtYXRoYmZ7dX1faSBcXG1hdGhiZnt1fV9pXntcXHRvcH0kLCBlIGNvbnNpZGVyYW5kbyBxdWUgb3MgYXV0b3ZldG9yZXMgJFxcbWF0aGJme3V9X2kkIHPDo28gb3J0b25vcm1haXMsIHF1YWwgZGFzIGFmaXJtYcOnw7VlcyBhYmFpeG8gZGVzY3JldmUgY29ycmV0YW1lbnRlIGEgaW1wb3J0w6JuY2lhIGRvcyBhdXRvdmFsb3JlcyBuZXN0ZSBjb250ZXh0byBkZSByZWR1w6fDo28gZGUgZGltZW5zaW9uYWxpZGFkZT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gYXV0b3ZhbG9yICRcXGxhbWJkYV8zJCByZXByZXNlbnRhIGEgbWFpb3IgdmFyaWFiaWxpZGFkZSBkbyBzaXN0ZW1hLCBkZXZlbmRvIHNlciBwcmlvcml6YWRvIG5hIGFuw6FsaXNlLiIsICJCIjogIkEgc29tYSBkb3MgYXV0b3ZhbG9yZXMgJFxcc3VtX3tpPTF9XnszfSBcXGxhbWJkYV9pID0gMTUuNSQgcmVwcmVzZW50YSBhIHZhcmnDom5jaWEgdG90YWwgZG9zIGRhZG9zIG1vbml0b3JhZG9zIHBlbG9zIHNlbnNvcmVzLiIsICJDIjogIkNvbW8gJFxcbWF0aGJme0F9JCDDqSB1bWEgbWF0cml6IFxcc2ltw6l0cmljYSwgb3MgYXV0b3ZhbG9yZXMgcG9kZW0gc2VyIG5lZ2F0aXZvcywgaW5kaWNhbmRvIGRpcmXDp8O1ZXMgZGUgdmFyaWFiaWxpZGFkZSBpbnZlcnNhLiIsICJEIjogIk8gYXV0b3ZldG9yICRcXG1hdGhiZnt1fV8xJCBhc3NvY2lhZG8gYSAkXFxsYW1iZGFfMSQgw6kgYSBkaXJlw6fDo28gZGUgbWVub3IgdmFyaWFiaWxpZGFkZSwgZGV2ZW5kbyBzZXIgZGVzY2FydGFkby4iLCAiRSI6ICJBIGRlY29tcG9zacOnw6NvIGVzcGVjdHJhbCDDqSBpbXBvc3PDrXZlbCBzZSBhIG1hdHJpeiAkXFxtYXRoYmZ7QX0kIHBvc3N1aXIgYXV0b3ZhbG9yZXMgZGlzdGludG9zLCBvIHF1ZSBuw6NvIMOpIG8gY2FzbyBkZXN0ZSBwcm9ibGVtYS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBwcm9wcmllZGFkZSBkbyB0cmHDp28gZGEgbWF0cml6IGUgZGEgcmVsYcOnw6NvIGVudHJlIGEgdmFyacOibmNpYSB0b3RhbCBlIGEgc29tYSBkb3MgYXV0b3ZhbG9yZXMgbmEgZGVjb21wb3Npw6fDo28gZXNwZWN0cmFsIGRlIG1hdHJpemVzIGRlIGNvdmFyacOibmNpYS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgbWF0cml6IGRlIGNvdmFyacOibmNpYSAkXFxtYXRoYmZ7QX0kIMOpIHVtYSBtYXRyaXogXFxzaW3DqXRyaWNhIGRlZmluaWRhIHBvc2l0aXZhIChuZXN0ZSBjb250ZXh0byBmw61zaWNvKS4gVW1hIGRhcyBwcm9wcmllZGFkZXMgZnVuZGFtZW50YWlzIGRhIGRlY29tcG9zacOnw6NvIGVzcGVjdHJhbCDDqSBxdWUgbyB0cmHDp28gZGEgbWF0cml6LCAkXFx0ZXh0e3RyfShcXG1hdGhiZntBfSkkLCBxdWUgY29ycmVzcG9uZGUgw6AgdmFyacOibmNpYSB0b3RhbCBkb3MgZGFkb3MsIMOpIGlndWFsIMOgIHNvbWEgZG9zIHNldXMgYXV0b3ZhbG9yZXM6ICRcXHRleHR7dHJ9KFxcbWF0aGJme0F9KSA9IFxcc3VtX3tpPTF9Xm4gXFxsYW1iZGFfaSQuIFBvcnRhbnRvLCAkMTIuMCArIDMuMCArIDAuNSA9IDE1LjUkLiBPIGF1dG92YWxvciAkXFxsYW1iZGFfMSQgw6kgbyBtYWlvciwgaW5kaWNhbmRvIHF1ZSBhIGRpcmXDp8OjbyBkbyBhdXRvdmV0b3IgJFxcbWF0aGJme3V9XzEkIGNhcHR1cmEgYSBtYWlvciBwYXJ0ZSBkYSB2YXJpYWJpbGlkYWRlIChjb21wb25lbnRlIHByaW5jaXBhbCksIGludmFsaWRhbmRvIGFzIG9ww6fDtWVzIEEgZSBELiBNYXRyaXplcyBkZSBjb3ZhcmnDom5jaWEgc8OjbyBzZW1pZGVmaW5pZGFzIHBvc2l0aXZhcywgbG9nbyBzZXVzIGF1dG92YWxvcmVzIG7Do28gc8OjbyBuZWdhdGl2b3MuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKGRhdGE9W2dvLkJhcih4PVsnQXV0b3ZhbG9yIDEnLCAnQXV0b3ZhbG9yIDInLCAnQXV0b3ZhbG9yIDMnXSwgeT1bMTIuMCwgMy4wLCAwLjVdLCBtYXJrZXJfY29sb3I9JyMxRTNBOEEnKV0pXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+RGlzdHJpYnVpw6fDo28gZGUgQXV0b3ZhbG9yZXM8L2I+JywgeGF4aXNfdGl0bGU9J0NvbXBvbmVudGVzJywgeWF4aXNfdGl0bGU9J1ZhbG9yIGRlIFZhcmnDom5jaWEgKEF1dG92YWxvciknLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgdW1hIG1hdHJpeiBkZSB0cmFuc2Zvcm1hw6fDo28gJFxcbWF0aGJme0F9ID0gXFxiZWdpbntwbWF0cml4fSAyICYgMSBcXFxcIDEgJiAyIFxcZW5ke3BtYXRyaXh9JC4gVW0gYW5hbGlzdGEgZGVzZWphIGRlY29tcG9yIGVzc2EgbWF0cml6IHBhcmEgZW50ZW5kZXIgc3VhcyBkaXJlw6fDtWVzIGRlIGVzdGlyYW1lbnRvIHByaW5jaXBhaXMuIEFvIGNhbGN1bGFyIG9zIGF1dG92YWxvcmVzLCBlbmNvbnRyYS1zZSAkXFxsYW1iZGFfMSA9IDMkIGUgJFxcbGFtYmRhXzIgPSAxJC4gUXVhaXMgc8OjbyBvcyBhdXRvdmV0b3JlcyBub3JtYWxpemFkb3MgYXNzb2NpYWRvcyBhIGVzc2VzIGF1dG92YWxvcmVzPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJFxcbWF0aGJme3V9XzEgPSBbMSwgMV1ee1xcdG9wfSAvIFxcc3FydHsyfSQgZSAkXFxtYXRoYmZ7dX1fMiA9IFsxLCAtMV1ee1xcdG9wfSAvIFxcc3FydHsyfSQiLCAiQiI6ICIkXFxtYXRoYmZ7dX1fMSA9IFsxLCAwXV57XFx0b3B9JCBlICRcXG1hdGhiZnt1fV8yID0gWzAsIDFdXntcXHRvcH0kIiwgIkMiOiAiJFxcbWF0aGJme3V9XzEgPSBbMSwgLTFdXntcXHRvcH0gLyBcXHNxcnR7Mn0kIGUgJFxcbWF0aGJme3V9XzIgPSBbMSwgMV1ee1xcdG9wfSAvIFxcc3FydHsyfSQiLCAiRCI6ICIkXFxtYXRoYmZ7dX1fMSA9IFsyLCAxXV57XFx0b3B9IC8gXFxzcXJ0ezV9JCBlICRcXG1hdGhiZnt1fV8yID0gWzEsIDJdXntcXHRvcH0gLyBcXHNxcnR7NX0kIiwgIkUiOiAiJFxcbWF0aGJme3V9XzEgPSBbMSwgMl1ee1xcdG9wfSAvIFxcc3FydHs1fSQgZSAkXFxtYXRoYmZ7dX1fMiA9IFsyLCAxXV57XFx0b3B9IC8gXFxzcXJ0ezV9JCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiUmVzb2x2YSBvIHNpc3RlbWEgJChcXG1hdGhiZntBfSAtIFxcbGFtYmRhIFxcbWF0aGJme0l9KVxcbWF0aGJme3V9ID0gMCQgcGFyYSBjYWRhIGF1dG92YWxvciBlIGNlcnRpZmlxdWUtc2UgZGUgcXVlIG9zIHZldG9yZXMgcmVzdWx0YW50ZXMgdGVuaGFtIG5vcm1hIHVuaXTDoXJpYS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBhcmEgJFxcbGFtYmRhXzEgPSAzJDogJChcXG1hdGhiZntBfSAtIDNcXG1hdGhiZntJfSlcXG1hdGhiZnt1fV8xID0gMCBcXGltcGxpZXMgXFxiZWdpbntwbWF0cml4fSAtMSAmIDEgXFxcXCAxICYgLTEgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSB4IFxcXFwgeSBcXGVuZHtwbWF0cml4fSA9IDAkLCBvIHF1ZSBpbXBsaWNhICQteCArIHkgPSAwJCwgbG9nbyAkeD15JC4gTm9ybWFsaXphbmRvLCB0ZW1vcyAkXFxtYXRoYmZ7dX1fMSA9IFsxLCAxXV57XFx0b3B9L1xcc3FydHsyfSQuIFBhcmEgJFxcbGFtYmRhXzIgPSAxJDogJChcXG1hdGhiZntBfSAtIDFcXG1hdGhiZntJfSlcXG1hdGhiZnt1fV8yID0gMCBcXGltcGxpZXMgXFxiZWdpbntwbWF0cml4fSAxICYgMSBcXFxcIDEgJiAxIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0geCBcXFxcIHkgXFxlbmR7cG1hdHJpeH0gPSAwJCwgbyBxdWUgaW1wbGljYSAkeCt5PTAkLCBsb2dvICR4PS15JC4gTm9ybWFsaXphbmRvLCB0ZW1vcyAkXFxtYXRoYmZ7dX1fMiA9IFsxLCAtMV1ee1xcdG9wfS9cXHNxcnR7Mn0kLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfV0sICJxdWVzdG9lc19kaXNjdXJzaXZhcyI6IFt7ImVudW5jaWFkbyI6ICJVbSBwZXNxdWlzYWRvciBlc3TDoSBtb2RlbGFuZG8gYSByZWxhw6fDo28gZW50cmUgbyBjdXN0byBkZSBtYW51dGVuw6fDo28gZGUgbcOhcXVpbmFzIGVtIHVtYSBmw6FicmljYSAoJHkkKSBlIGR1YXMgdmFyacOhdmVpcyBleHBsaWNhdGl2YXM6IG8gdGVtcG8gZGUgdXNvIGVtIGhvcmFzICgkeF8xJCkgZSBhIGlkYWRlIGRhIG3DoXF1aW5hIGVtIGFub3MgKCR4XzIkKS4gUGFyYSB1bWEgYW1vc3RyYSBkZSA0IG3DoXF1aW5hcywgbyBwZXNxdWlzYWRvciBkZXNlamEgbW9udGFyIGEgbWF0cml6IGRlIGRlbGluZWFtZW50byAkXFxtYXRoYmZ7WH0kIHBhcmEgbyBtb2RlbG8gJFxcbWF0aGJme3l9ID0gXFxtYXRoYmZ7WH1cXG1hdGhiZntcXGJldGF9ICsgXFxtYXRoYmZ7ZX0kLiBFeHBsaXF1ZSBjb21vIGEgbWF0cml6ICRcXG1hdGhiZntYfSQgZGV2ZSBzZXIgY29uc3RydcOtZGEgZSBxdWFsIGEgc3VhIGRpbWVuc8OjbyBmaW5hbCwgY29uc2lkZXJhbmRvIGEgaW5jbHVzw6NvIGRlIHVtYSBjb2x1bmEgZGUgaW50ZXJjZXB0byBwYXJhIG8gbW9kZWxvIGxpbmVhci4iLCAiZGljYSI6ICJPIG1vZGVsbyBsaW5lYXIgY29tcGxldG8gaW5jbHVpIHVtIGludGVyY2VwdG8gKCRcXGJldGFfMCQpLCBvIHF1ZSByZXF1ZXIgdW1hIGNvbHVuYSBkZSB2YWxvcmVzIHVuaXTDoXJpb3MgbmEgbWF0cml6IGRlIGRlbGluZWFtZW50byAkXFxtYXRoYmZ7WH0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXJhIHVtIG1vZGVsbyBsaW5lYXIgY29tIDIgdmFyacOhdmVpcyBwcmVkaXRvcmFzIGUgdW0gaW50ZXJjZXB0bywgdGVtb3MgdW0gdG90YWwgZGUgMyBwYXLDom1ldHJvcyBhIGVzdGltYXIgKCRcXGJldGFfMCwgXFxiZXRhXzEsIFxcYmV0YV8yJCkuIiwgIkEgbWF0cml6IGRlIGRlbGluZWFtZW50byAkXFxtYXRoYmZ7WH0kIGRldmUgdGVyICRuJCBsaW5oYXMgKG7Dum1lcm8gZGUgb2JzZXJ2YcOnw7VlcykgZSAkbSQgY29sdW5hcyAobsO6bWVybyBkZSBwYXLDom1ldHJvcykuIiwgIkRhZG8gcXVlICRuPTQkIGUgJG09MyQsIGEgZGltZW5zw6NvIGRhIG1hdHJpeiDDqSAkKDQgXFx0aW1lcyAzKSQuIiwgIkEgZm9ybWEgZGEgbWF0cml6IMOpOiAkJFxcbWF0aGJme1h9ID0gXFxiZWdpbntwbWF0cml4fSAxICYgeF97MTF9ICYgeF97MjF9IFxcXFwgMSAmIHhfezEyfSAmIHhfezIyfSBcXFxcIDEgJiB4X3sxM30gJiB4X3syM30gXFxcXCAxICYgeF97MTR9ICYgeF97MjR9IFxcZW5ke3BtYXRyaXh9JCQiLCAiQSBwcmltZWlyYSBjb2x1bmEgZGUgMXMgcmVwcmVzZW50YSBvIGNvZWZpY2llbnRlIGRlIGludGVyY2VwdG8gKCRcXGJldGFfMCQpLCBlbnF1YW50byBhcyBjb2x1bmFzIHN1YnNlcXVlbnRlcyBjb250w6ptIGFzIG9ic2VydmHDp8O1ZXMgZGFzIHZhcmnDoXZlaXMgZXhwbGljYXRpdmFzLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkRhZG8gdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIGV4cHJlc3NvIHBlbGEgZXF1YcOnw6NvIG1hdHJpY2lhbCAkXFxtYXRoYmZ7eX0gPSBcXG1hdGhiZntYfVxcbWF0aGJme1xcYmV0YX0gKyBcXG1hdGhiZntlfSQsIG9uZGUgJFxcbWF0aGJme3l9JCDDqSB1bSB2ZXRvciBkZSBvYnNlcnZhw6fDtWVzIGRlIGRpbWVuc8OjbyAkKDIwIFxcdGltZXMgMSkkIGUgJFxcbWF0aGJme1h9JCDDqSBhIG1hdHJpeiBkZSBkZWxpbmVhbWVudG8gZGUgZGltZW5zw6NvICQoMjAgXFx0aW1lcyA1KSQuIERldGVybWluZSBhIGRpbWVuc8OjbyBleGF0YSBkbyB2ZXRvciBkZSBwYXLDom1ldHJvcyAkXFxtYXRoYmZ7XFxiZXRhfSQgcGFyYSBxdWUgYSBvcGVyYcOnw6NvIGRlIG11bHRpcGxpY2HDp8OjbyBtYXRyaWNpYWwgJFxcbWF0aGJme1h9XFxtYXRoYmZ7XFxiZXRhfSQgc2VqYSBtYXRlbWF0aWNhbWVudGUgdsOhbGlkYS4iLCAiZGljYSI6ICJQYXJhIG11bHRpcGxpY2FyIHVtYSBtYXRyaXogJFxcbWF0aGJme0F9X3sobiBcXHRpbWVzIG0pfSQgcG9yIHVtIHZldG9yICRcXG1hdGhiZntifV97KGsgXFx0aW1lcyAxKX0kLCBvIG7Dum1lcm8gZGUgY29sdW5hcyBkZSAkXFxtYXRoYmZ7QX0kIGRldmUgc2VyIGlndWFsIGFvIG7Dum1lcm8gZGUgbGluaGFzIGRlICRcXG1hdGhiZntifSQgKCRtPWskKS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSBjb25kacOnw6NvIGRlIGNvbmZvcm1pZGFkZSBwYXJhIGEgbXVsdGlwbGljYcOnw6NvIG1hdHJpY2lhbCAkXFxtYXRoYmZ7WH1feyhuIFxcdGltZXMgbSl9IFxcbWF0aGJme1xcYmV0YX1feyhrIFxcdGltZXMgMSl9JCBleGlnZSBxdWUgbyBuw7ptZXJvIGRlIGNvbHVuYXMgZGEgcHJpbWVpcmEgbWF0cml6IHNlamEgaWd1YWwgYW8gbsO6bWVybyBkZSBsaW5oYXMgZGEgc2VndW5kYSwgb3Ugc2VqYSwgJG0gPSBrJC4iLCAiTmEgZXhwcmVzc8OjbyAkXFxtYXRoYmZ7WH1feygyMCBcXHRpbWVzIDUpfSQsIHRlbW9zICRtPTUkLiIsICJQb3J0YW50bywgbyB2ZXRvciBkZSBwYXLDom1ldHJvcyAkXFxtYXRoYmZ7XFxiZXRhfSQgZGV2ZSBwb3NzdWlyIG9icmlnYXRvcmlhbWVudGUgNSBsaW5oYXMgcGFyYSBxdWUgbyBwcm9kdXRvICRcXG1hdGhiZntYfVxcbWF0aGJme1xcYmV0YX0kIHNlamEgcG9zc8OtdmVsLiIsICJDb21vICRcXG1hdGhiZntcXGJldGF9JCDDqSB1bSB2ZXRvciwgZWxlIHBvc3N1aSBhcGVuYXMgMSBjb2x1bmEuIiwgIkFzc2ltLCBhIGRpbWVuc8OjbyBkZSAkXFxtYXRoYmZ7XFxiZXRhfSQgw6kgJCg1IFxcdGltZXMgMSkkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogNS4wfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIGFzIG1hdHJpemVzICRcXG1hdGhiZntBfV97KDMgXFx0aW1lcyAyKX0kIGUgJFxcbWF0aGJme0J9X3soMiBcXHRpbWVzIDMpfSQuIEV4cGxpcXVlLCB1dGlsaXphbmRvIG9zIGNvbmNlaXRvcyBkZSDDoWxnZWJyYSBtYXRyaWNpYWwsIHBvciBxdWUgYSBzb21hICRcXG1hdGhiZntBfSArIFxcbWF0aGJme0J9JCBuw6NvIMOpIHVtYSBvcGVyYcOnw6NvIGRlZmluaWRhLCBlbnF1YW50byBvIHByb2R1dG8gJFxcbWF0aGJme0F9XFxtYXRoYmZ7Qn0kIMOpIHVtYSBvcGVyYcOnw6NvIHBvc3PDrXZlbC4iLCAiZGljYSI6ICJSZXZpc2UgYXMgcmVncmFzIGRlIGNvbmZvcm1pZGFkZSBwYXJhIGEgc29tYSAocmVxdWVyIGRpbWVuc8O1ZXMgaWTDqm50aWNhcykgZSBwYXJhIG8gcHJvZHV0byBtYXRyaWNpYWwgKHJlcXVlciBxdWUgYXMgY29sdW5hcyBkYSBwcmltZWlyYSBjb2luY2lkYW0gY29tIGFzIGxpbmhhcyBkYSBzZWd1bmRhKS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUmVncmEgZGEgU29tYTogUGFyYSBzb21hciBkdWFzIG1hdHJpemVzLCBlbGFzIGRldmVtIHRlciBleGF0YW1lbnRlIGEgbWVzbWEgZGltZW5zw6NvLCBwb2lzIGEgc29tYSDDqSBkZWZpbmlkYSBlbGVtZW50byBhIGVsZW1lbnRvICgkYV97aWp9ICsgYl97aWp9JCkuIENvbW8gJFxcbWF0aGJme0F9JCDDqSAkKDMgXFx0aW1lcyAyKSQgZSAkXFxtYXRoYmZ7Qn0kIMOpICQoMiBcXHRpbWVzIDMpJCwgYSBzb21hICRcXG1hdGhiZntBfSArIFxcbWF0aGJme0J9JCDDqSBpbXBvc3PDrXZlbC4iLCAiUmVncmEgZG8gUHJvZHV0bzogUGFyYSBvIHByb2R1dG8gJFxcbWF0aGJme0F9XFxtYXRoYmZ7Qn0kLCBvIG7Dum1lcm8gZGUgY29sdW5hcyBkYSBwcmltZWlyYSBtYXRyaXogKCRtX0EgPSAyJCkgZGV2ZSBzZXIgaWd1YWwgYW8gbsO6bWVybyBkZSBsaW5oYXMgZGEgc2VndW5kYSBtYXRyaXogKCRuX0IgPSAyJCkuIiwgIkNvbW8gJG1fQSA9IG5fQiA9IDIkLCBhIG11bHRpcGxpY2HDp8OjbyDDqSBkZWZpbmlkYS4iLCAiQSBkaW1lbnPDo28gcmVzdWx0YW50ZSBkbyBwcm9kdXRvICRcXG1hdGhiZntBfV97KDMgXFx0aW1lcyAyKX0gXFxtYXRoYmZ7Qn1feygyIFxcdGltZXMgMyl9JCBzZXLDoSAkKDMgXFx0aW1lcyAzKSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGFkYSBhIG1hdHJpeiBkZSBkYWRvcyBkZSBlbnRyYWRhICRcXG1hdGhiZntBfSA9IFxcYmVnaW57cG1hdHJpeH0gMiAmIDEgXFxcXCAwICYgMyBcXFxcIDEgJiAyIFxcZW5ke3BtYXRyaXh9JCBlIG8gdmV0b3IgZGUgY29lZmljaWVudGVzIChwZXNvcykgJFxcbWF0aGJme3h9ID0gXFxiZWdpbntwbWF0cml4fSAxIFxcXFwgMiBcXGVuZHtwbWF0cml4fSQsIGNhbGN1bGUgbyBwcm9kdXRvIHJlc3VsdGFudGUgJFxcbWF0aGJme3l9ID0gXFxtYXRoYmZ7QX1cXG1hdGhiZnt4fSQuIEV4cGxpcXVlIG8gc2lnbmlmaWNhZG8gZXN0YXTDrXN0aWNvIGRlc3NhIG9wZXJhw6fDo28gY29tbyB1bWEgY29tYmluYcOnw6NvIGxpbmVhciBkYXMgY29sdW5hcyBkZSAkXFxtYXRoYmZ7QX0kLiIsICJkaWNhIjogIkNhZGEgZWxlbWVudG8gJHlfaSQgZG8gdmV0b3IgcmVzdWx0YW50ZSDDqSBvYnRpZG8gcGVsbyBwcm9kdXRvIGVzY2FsYXIgZGEgJGkkLcOpc2ltYSBsaW5oYSBkZSAkXFxtYXRoYmZ7QX0kIHBlbG8gdmV0b3IgJFxcbWF0aGJme3h9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSBtYXRyaXogJFxcbWF0aGJme0F9JCDDqSAkKDMgXFx0aW1lcyAyKSQgZSBvIHZldG9yICRcXG1hdGhiZnt4fSQgw6kgJCgyIFxcdGltZXMgMSkkLCBsb2dvICRcXG1hdGhiZnt5fSQgc2Vyw6EgJCgzIFxcdGltZXMgMSkkLiIsICJDw6FsY3VsbyBkYSBwcmltZWlyYSBsaW5oYTogJHlfMSA9ICgyIFxcdGltZXMgMSkgKyAoMSBcXHRpbWVzIDIpID0gNCQuIiwgIkPDoWxjdWxvIGRhIHNlZ3VuZGEgbGluaGE6ICR5XzIgPSAoMCBcXHRpbWVzIDEpICsgKDMgXFx0aW1lcyAyKSA9IDYkLiIsICJDw6FsY3VsbyBkYSB0ZXJjZWlyYSBsaW5oYTogJHlfMyA9ICgxIFxcdGltZXMgMSkgKyAoMiBcXHRpbWVzIDIpID0gNSQuIiwgIk8gdmV0b3IgcmVzdWx0YW50ZSDDqSAkXFxtYXRoYmZ7eX0gPSBcXGJlZ2lue3BtYXRyaXh9IDQgXFxcXCA2IFxcXFwgNSBcXGVuZHtwbWF0cml4fSQuIiwgIlNpZ25pZmljYWRvOiAkXFxtYXRoYmZ7eX0kIMOpIHVtYSBjb21iaW5hw6fDo28gbGluZWFyIGRhcyBjb2x1bmFzIGRlICRcXG1hdGhiZntBfSQgcG9uZGVyYWRhcyBwZWxvcyB2YWxvcmVzIGVtICRcXG1hdGhiZnt4fSQuIEVzdGF0aXN0aWNhbWVudGUsIGlzc28gcmVwcmVzZW50YSBvIGPDoWxjdWxvIGRlIHZhbG9yZXMgcHJlZGl0b3MgZW0gdW0gbW9kZWxvIGxpbmVhci4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgYSBtYXRyaXogZGUgb2JzZXJ2YcOnw7VlcyAkXFxtYXRoYmZ7WH1feyhuIFxcdGltZXMgbSl9JC4gRGVtb25zdHJlLCBhdHJhdsOpcyBkYSByZWdyYSBkZSBkaW1lbnPDtWVzLCBxdWFsIMOpIGEgZGltZW5zw6NvIGRhIG1hdHJpeiAkXFxtYXRoYmZ7TX0gPSBcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0kLiBQb3IgcXVlIGVzc2EgbWF0cml6IHJlc3VsdGFudGUgw6kgZnVuZGFtZW50YWwgcGFyYSBjYWxjdWxhciBhIHZhcmlhYmlsaWRhZGUgZG9zIGRhZG9zIGVtIGVzdGF0w61zdGljYSBtdWx0aXZhcmlhZGE/IiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBzZSAkXFxtYXRoYmZ7WH0kIMOpICQobiBcXHRpbWVzIG0pJCwgZW50w6NvICRcXG1hdGhiZntYfV57XFx0b3B9JCDDqSAkKG0gXFx0aW1lcyBuKSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkRpbWVuc8OjbyBkZSAkXFxtYXRoYmZ7WH1ee1xcdG9wfSQgw6kgJChtIFxcdGltZXMgbikkLiIsICJEaW1lbnPDo28gZGUgJFxcbWF0aGJme1h9JCDDqSAkKG4gXFx0aW1lcyBtKSQuIiwgIlByb2R1dG8gZGUgJChtIFxcdGltZXMgbikkIHBvciAkKG4gXFx0aW1lcyBtKSQgcmVzdWx0YSBlbSB1bWEgbWF0cml6IGRlIGRpbWVuc8OjbyAkKG0gXFx0aW1lcyBtKSQuIiwgIkVzdGF0aXN0aWNhbWVudGUsIGVzdGEgbWF0cml6IMOpIGEgYmFzZSBwYXJhIGEgbWF0cml6IGRlIGNvdmFyacOibmNpYSAob3UgZGlzcGVyc8OjbyksIHBvaXMgc2V1cyBlbGVtZW50b3MgcmVwcmVzZW50YW0gc29tYXMgZGUgcHJvZHV0b3MgY3J1emFkb3MgZGFzIHZhcmnDoXZlaXMgKGNvbHVuYXMgZGUgJFxcbWF0aGJme1h9JCksIGNhcHR1cmFuZG8gY29tbyBhcyB2YXJpw6F2ZWlzIHZhcmlhbSBjb25qdW50YW1lbnRlLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoZGF0YT1bZ28uVGFibGUoaGVhZGVyPWRpY3QodmFsdWVzPVsnTWF0cml6JywgJ0RpbWVuc8OjbyddKSwgY2VsbHM9ZGljdCh2YWx1ZXM9W1snWCcsICdYXlQnLCAnWF5UIFgnXSwgWycobiB4IG0pJywgJyhtIHggbiknLCAnKG0geCBtKSddLF0pKV0pIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiU2VqYSAkXFxtYXRoYmZ7QX0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwIFxcXFwgMCAmIDIgXFxlbmR7cG1hdHJpeH0kIHVtYSBtYXRyaXogZGUgdHJhbnNmb3JtYcOnw6NvIGxpbmVhciBlbSB1bSBlc3Bhw6dvIGJpZGltZW5zaW9uYWwuIFNlIGFwbGljYXJtb3MgZXNzYSBtYXRyaXogYSB1bSBwb250byAkXFxtYXRoYmZ7dn0gPSBcXGJlZ2lue3BtYXRyaXh9IHhfMSBcXFxcIHhfMiBcXGVuZHtwbWF0cml4fSQsIGNhbGN1bGUgbyBwb250byB0cmFuc2Zvcm1hZG8gJFxcbWF0aGJme3Z9JyA9IFxcbWF0aGJme0F9XFxtYXRoYmZ7dn0kIGUgZGVzY3JldmEgZ2VvbWV0cmljYW1lbnRlIG8gZWZlaXRvIGRlc3NhIG9wZXJhw6fDo28gbm9zIGVpeG9zIGRvIHNpc3RlbWEuIiwgImRpY2EiOiAiUmVhbGl6ZSBvIHByb2R1dG8gbWF0cmljaWFsIGRlICQyIFxcdGltZXMgMiQgcG9yICQyIFxcdGltZXMgMSQuIE9ic2VydmUgY29tbyBjYWRhIGNvbXBvbmVudGUgb3JpZ2luYWwgw6kgZXNjYWxvbmFkby4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiJFxcbWF0aGJme3Z9JyA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAwICYgMiBcXGVuZHtwbWF0cml4fSBcXGJlZ2lue3BtYXRyaXh9IHhfMSBcXFxcIHhfMiBcXGVuZHtwbWF0cml4fSQiLCAiJHhfMScgPSAoMSBcXHRpbWVzIHhfMSkgKyAoMCBcXHRpbWVzIHhfMikgPSB4XzEkIiwgIiR4XzInID0gKDAgXFx0aW1lcyB4XzEpICsgKDIgXFx0aW1lcyB4XzIpID0gMnhfMiQiLCAiUG9ydGFudG8sICRcXG1hdGhiZnt2fScgPSBcXGJlZ2lue3BtYXRyaXh9IHhfMSBcXFxcIDJ4XzIgXFxlbmR7cG1hdHJpeH0kLiIsICJHZW9tZXRyaWNhbWVudGUsIGVzdGEgdHJhbnNmb3JtYcOnw6NvIG1hbnTDqW0gbyBjb21wb25lbnRlIGRvIGVpeG8gaG9yaXpvbnRhbCBpbmFsdGVyYWRvIGUgZXN0aWNhIG8gY29tcG9uZW50ZSBkbyBlaXhvIHZlcnRpY2FsIHBvciB1bSBmYXRvciBkZSAyLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9WzEsIDFdLCB5PVswLCAyXSwgbW9kZT0nbGluZXMrbWFya2VycycsIG5hbWU9J1RyYW5zZm9ybWFkbycsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVsxLCAxXSwgeT1bMCwgMV0sIG1vZGU9J2xpbmVzK21hcmtlcnMnLCBuYW1lPSdPcmlnaW5hbCcsIGxpbmU9ZGljdChjb2xvcj0nIzEwQjk4MScpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdUcmFuc2Zvcm1hw6fDo28gTGluZWFyIChFc2NhbG9uYW1lbnRvIFZlcnRpY2FsKScsIHhheGlzX3RpdGxlPSd4MScsIHlheGlzX3RpdGxlPSd4MicpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiU2VqYSAkXFxtYXRoYmZ7TX0kIHVtYSBtYXRyaXogaWRlbXBvdGVudGUgZGUgZGltZW5zw6NvICRuIFxcdGltZXMgbiQuIFByb3ZlIHF1ZSBhIG1hdHJpeiAkXFxtYXRoYmZ7SX0gLSBcXG1hdGhiZntNfSQgdGFtYsOpbSDDqSBpZGVtcG90ZW50ZSBlIHF1ZSBvIHByb2R1dG8gJFxcbWF0aGJme019KFxcbWF0aGJme0l9IC0gXFxtYXRoYmZ7TX0pJCByZXN1bHRhIG5hIG1hdHJpeiBudWxhLiIsICJkaWNhIjogIlV0aWxpemUgYSBkZWZpbmnDp8OjbyBkZSBtYXRyaXogaWRlbXBvdGVudGU6ICRcXG1hdGhiZntNfV4yID0gXFxtYXRoYmZ7TX0kLiBBcGxpcXVlIGVzc2EgZGVmaW5pw6fDo28gbmEgw6FsZ2VicmEgbWF0cmljaWFsIHNvbGljaXRhZGEuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIFBhcmEgcHJvdmFyIHF1ZSAkKFxcbWF0aGJme0l9IC0gXFxtYXRoYmZ7TX0pJCDDqSBpZGVtcG90ZW50ZSwgY2FsY3VsYW1vcyAkKFxcbWF0aGJme0l9IC0gXFxtYXRoYmZ7TX0pXjIgPSAoXFxtYXRoYmZ7SX0gLSBcXG1hdGhiZntNfSkoXFxtYXRoYmZ7SX0gLSBcXG1hdGhiZntNfSkkLiIsICIyLiBFeHBhbmRpbmRvOiAkKFxcbWF0aGJme0l9IC0gXFxtYXRoYmZ7TX0pKFxcbWF0aGJme0l9IC0gXFxtYXRoYmZ7TX0pID0gXFxtYXRoYmZ7SX1cXG1hdGhiZntJfSAtIFxcbWF0aGJme0l9XFxtYXRoYmZ7TX0gLSBcXG1hdGhiZntNfVxcbWF0aGJme0l9ICsgXFxtYXRoYmZ7TX1eMiQuIiwgIjMuIENvbW8gJFxcbWF0aGJme019XjIgPSBcXG1hdGhiZntNfSQgKGlkZW1wb3RlbnRlKSBlICRcXG1hdGhiZntJfVxcbWF0aGJme019ID0gXFxtYXRoYmZ7TX1cXG1hdGhiZntJfSA9IFxcbWF0aGJme019JCwgdGVtb3M6ICRcXG1hdGhiZntJfSAtIFxcbWF0aGJme019IC0gXFxtYXRoYmZ7TX0gKyBcXG1hdGhiZntNfSA9IFxcbWF0aGJme0l9IC0gXFxtYXRoYmZ7TX0kLiBMb2dvLCDDqSBpZGVtcG90ZW50ZS4iLCAiNC4gUGFyYSBvIHByb2R1dG8gJFxcbWF0aGJme019KFxcbWF0aGJme0l9IC0gXFxtYXRoYmZ7TX0pJCwgZXhwYW5kaW1vczogJFxcbWF0aGJme019XFxtYXRoYmZ7SX0gLSBcXG1hdGhiZntNfV4yJC4iLCAiNS4gU3Vic3RpdHVpbmRvICRcXG1hdGhiZntNfV4yID0gXFxtYXRoYmZ7TX0kLCBvYnRlbW9zICRcXG1hdGhiZntNfSAtIFxcbWF0aGJme019ID0gXFxtYXRoYmZ7MH0kLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEgJiBFc3RldmVzLCBDYXAgMiwgcC4gNTciLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtYSBtYXRyaXogXFxzaW3DqXRyaWNhICRcXG1hdGhiZntBfSA9IFxcYmVnaW57cG1hdHJpeH0gMiAmIDEgXFxcXCAxICYgMiBcXGVuZHtwbWF0cml4fSQuIENhbGN1bGUgbyBzZXUgdHJhw6dvICRcXHRleHR7dHJ9KFxcbWF0aGJme0F9KSQgZSB2ZXJpZmlxdWUgc2UgZWxhIMOpIFxcc2ltw6l0cmljYSBkZSBhY29yZG8gY29tIGEgZGVmaW5pw6fDo28gJFxcbWF0aGJme0F9ID0gXFxtYXRoYmZ7QX1ee1xcdG9wfSQuIiwgImRpY2EiOiAiTyB0cmHDp28gZGUgdW1hIG1hdHJpeiDDqSBhIHNvbWEgZG9zIGVsZW1lbnRvcyBkYSBkaWFnb25hbCBwcmluY2lwYWwuIEEgc2ltZXRyaWEgb2NvcnJlIHF1YW5kbyBvIGVsZW1lbnRvICRhX3tpan0gPSBhX3tqaX0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBEZWZpbmnDp8OjbyBkbyB0cmHDp286ICRcXHRleHR7dHJ9KFxcbWF0aGJme0F9KSA9IFxcc3VtIGFfe2lpfSA9IGFfezExfSArIGFfezIyfSQuIiwgIjIuIEPDoWxjdWxvOiAkXFx0ZXh0e3RyfShcXG1hdGhiZntBfSkgPSAyICsgMiA9IDQkLiIsICIzLiBWZXJpZmljYcOnw6NvIGRlIHNpbWV0cmlhOiBUcmFuc3Bvc3RhICRcXG1hdGhiZntBfV57XFx0b3B9ID0gXFxiZWdpbntwbWF0cml4fSAyICYgMSBcXFxcIDEgJiAyIFxcZW5ke3BtYXRyaXh9JC4iLCAiNC4gQ29tcGFyYcOnw6NvOiAkXFxtYXRoYmZ7QX0gPSBcXG1hdGhiZntBfV57XFx0b3B9JCwgbG9nbyBhIG1hdHJpeiDDqSBcXHNpbcOpdHJpY2EuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZShkYXRhPVtnby5IZWF0bWFwKHo9W1syLCAxXSwgWzEsIDJdXSwgY29sb3JzY2FsZT0nQmx1ZXMnKV0pXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nVmlzdWFsaXphw6fDo28gZGEgTWF0cml6IFNpbcOpdHJpY2EgQScsIHhheGlzX3RpdGxlPSdDb2x1bmEnLCB5YXhpc190aXRsZT0nTGluaGEnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogNC4wfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28sIHRlbW9zIHF1ZSAkXFxtYXRoYmZ7eX0gPSBcXG1hdGhiZntYfVxcdGhldGEgKyBcXG1hdGhiZntlfSQsIG9uZGUgJFxcbWF0aGJme1B9ID0gXFxtYXRoYmZ7WH0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9XFxtYXRoYmZ7WH1ee1xcdG9wfSQgcHJvamV0YSAkXFxtYXRoYmZ7eX0kIG5vIGVzcGHDp28gZGFzIGNvbHVuYXMgZGUgJFxcbWF0aGJme1h9JC4gQ2FsY3VsZSBvIHRyYcOnbyBkYSBtYXRyaXogJFxcbWF0aGJme1B9JCBzYWJlbmRvIHF1ZSAkXFxtYXRoYmZ7WH0kIMOpIGRlIGRpbWVuc8OjbyAkbiBcXHRpbWVzIGskIGNvbSBwb3N0byBjb2x1bmEgY29tcGxldG8gJGskLiBMZW1icmUtc2UgcXVlICRcXHRleHR7dHJ9KFxcbWF0aGJme0F9XFxtYXRoYmZ7Qn0pID0gXFx0ZXh0e3RyfShcXG1hdGhiZntCfVxcbWF0aGJme0F9KSQuIiwgImRpY2EiOiAiVXNlIGEgcHJvcHJpZWRhZGUgY8OtY2xpY2EgZG8gdHJhw6dvOiAkXFx0ZXh0e3RyfShcXG1hdGhiZntBfVxcbWF0aGJme0J9KSA9IFxcdGV4dHt0cn0oXFxtYXRoYmZ7Qn1cXG1hdGhiZntBfSkkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBRdWVyZW1vcyAkXFx0ZXh0e3RyfShcXG1hdGhiZntQfSkgPSBcXHRleHR7dHJ9KFxcbWF0aGJme1h9KFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfVxcbWF0aGJme1h9XntcXHRvcH0pJC4iLCAiMi4gUGVsYSBwcm9wcmllZGFkZSBjw61jbGljYSwgJFxcdGV4dHt0cn0oXFxtYXRoYmZ7QX1cXG1hdGhiZntCfVxcbWF0aGJme0N9KSA9IFxcdGV4dHt0cn0oXFxtYXRoYmZ7Q31cXG1hdGhiZntBfVxcbWF0aGJme0J9KSQuIiwgIjMuIEFzc2ltLCAkXFx0ZXh0e3RyfShcXG1hdGhiZntYfShcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0pXnstMX1cXG1hdGhiZntYfV57XFx0b3B9KSA9IFxcdGV4dHt0cn0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfSkkLiIsICI0LiBDb21vICRcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9ID0gXFxtYXRoYmZ7SX1feyhrKX0kLCB0ZW1vcyAkXFx0ZXh0e3RyfShcXG1hdGhiZntJfV97KGspfSkkLiIsICI1LiBPIHRyYcOnbyBkYSBtYXRyaXogaWRlbnRpZGFkZSBkZSBvcmRlbSAkayQgw6kgaWd1YWwgw6Agc3VhIGRpbWVuc8OjbzogJGskLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEgJiBFc3RldmVzLCBDYXAgMywgcC4gNzYiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGFkYSBhIG1hdHJpeiBcXHNpbcOpdHJpY2EgJFxcbWF0aGJme0F9ID0gXFxiZWdpbntwbWF0cml4fSA1ICYgMiBcXFxcIDIgJiAyIFxcZW5ke3BtYXRyaXh9JCwgY2FsY3VsZSBhbmFsaXRpY2FtZW50ZSBzZXVzIGF1dG92YWxvcmVzIGUgYXV0b3ZldG9yZXMuIEVtIHNlZ3VpZGEsIHZlcmlmaXF1ZSBzZSBhIGRlY29tcG9zacOnw6NvIGVzcGVjdHJhbCAkXFxtYXRoYmZ7QX0gPSBcXGxhbWJkYV8xIFxcbWF0aGJme3V9XzEgXFxtYXRoYmZ7dX1fMV57XFx0b3B9ICsgXFxsYW1iZGFfMiBcXG1hdGhiZnt1fV8yIFxcbWF0aGJme3V9XzJee1xcdG9wfSQgw6kgc2F0aXNmZWl0YS4iLCAiZGljYSI6ICJVc2UgbyBwb2xpbsO0bWlvIGNhcmFjdGVyw61zdGljbyAkXFxkZXQoXFxtYXRoYmZ7QX0gLSBcXGxhbWJkYSBcXG1hdGhiZntJfSkgPSAwJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogRW5jb250cmFyIG8gcG9saW7DtG1pbyBjYXJhY3RlcsOtc3RpY286ICRcXGRldCBcXGJlZ2lue3BtYXRyaXh9IDUtXFxsYW1iZGEgJiAyIFxcXFwgMiAmIDItXFxsYW1iZGEgXFxlbmR7cG1hdHJpeH0gPSAoNS1cXGxhbWJkYSkoMi1cXGxhbWJkYSkgLSA0ID0gXFxsYW1iZGFeMiAtIDdcXGxhbWJkYSArIDYgPSAwJC4iLCAiUGFzc28gMjogUmVzb2x2ZXIgYSBlcXVhw6fDo28gcXVhZHLDoXRpY2E6ICQoXFxsYW1iZGEgLSA2KShcXGxhbWJkYSAtIDEpID0gMCQsIHBvcnRhbnRvICRcXGxhbWJkYV8xID0gNiQgZSAkXFxsYW1iZGFfMiA9IDEkLiIsICJQYXNzbyAzOiBQYXJhICRcXGxhbWJkYV8xID0gNiQsIG8gc2lzdGVtYSAkKFxcbWF0aGJme0F9IC0gNlxcbWF0aGJme0l9KVxcbWF0aGJme3V9XzEgPSAwJCByZXN1bHRhIGVtICQteCArIDJ5ID0gMCBcXGltcGxpZXMgeCA9IDJ5JC4gVmV0b3IgbsOjbyBub3JtYWxpemFkbyAkWzIsIDFdXntcXHRvcH0kLiBOb3JtYWxpemFuZG86ICRcXG1hdGhiZnt1fV8xID0gWzIvXFxzcXJ0ezV9LCAxL1xcc3FydHs1fV1ee1xcdG9wfSQuIiwgIlBhc3NvIDQ6IFBhcmEgJFxcbGFtYmRhXzIgPSAxJCwgbyBzaXN0ZW1hICQoXFxtYXRoYmZ7QX0gLSAxXFxtYXRoYmZ7SX0pXFxtYXRoYmZ7dX1fMiA9IDAkIHJlc3VsdGEgZW0gJDR4ICsgMnkgPSAwIFxcaW1wbGllcyB5ID0gLTJ4JC4gVmV0b3IgbsOjbyBub3JtYWxpemFkbyAkWzEsIC0yXV57XFx0b3B9JC4gTm9ybWFsaXphbmRvOiAkXFxtYXRoYmZ7dX1fMiA9IFsxL1xcc3FydHs1fSwgLTIvXFxzcXJ0ezV9XV57XFx0b3B9JC4iLCAiUGFzc28gNTogVmVyaWZpY2FyIGEgcmVjb25zdHJ1w6fDo286ICQ2IFxcYmVnaW57cG1hdHJpeH0gNC81ICYgMi81IFxcXFwgMi81ICYgMS81IFxcZW5ke3BtYXRyaXh9ICsgMSBcXGJlZ2lue3BtYXRyaXh9IDEvNSAmIC0yLzUgXFxcXCAtMi81ICYgNC81IFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAyNC81KzEvNSAmIDEyLzUtMi81IFxcXFwgMTIvNS0yLzUgJiA2LzUrNC81IFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSA1ICYgMiBcXFxcIDIgJiAyIFxcZW5ke3BtYXRyaXh9ID0gXFxtYXRoYmZ7QX0kLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtYSBtYXRyaXogZGUgY292YXJpw6JuY2lhIHBvcHVsYWNpb25hbCAkXFxTaWdtYSQgdGVtIGF1dG92YWxvcmVzICRcXGxhbWJkYV8xID0gMTAkLCAkXFxsYW1iZGFfMiA9IDIkIGUgJFxcbGFtYmRhXzMgPSAwLjUkLiBDYWxjdWxlIGEgcHJvcG9yw6fDo28gZGEgdmFyacOibmNpYSB0b3RhbCBleHBsaWNhZGEgcGVsb3MgZG9pcyBwcmltZWlyb3MgY29tcG9uZW50ZXMgcHJpbmNpcGFpcy4iLCAiZGljYSI6ICJBIHByb3BvcsOnw6NvIGRhIHZhcmnDom5jaWEgZXhwbGljYWRhIHBlbG8gaS3DqXNpbW8gY29tcG9uZW50ZSDDqSBkYWRhIHBvciAkXFxsYW1iZGFfaSAvIFxcc3VtX3tqPTF9XntufSBcXGxhbWJkYV9qJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogQ2FsY3VsYXIgYSB2YXJpw6JuY2lhIHRvdGFsOiAkXFxzdW1fe2o9MX1eezN9IFxcbGFtYmRhX2ogPSAxMCArIDIgKyAwLjUgPSAxMi41JC4iLCAiUGFzc28gMjogQ2FsY3VsYXIgYSB2YXJpw6JuY2lhIGV4cGxpY2FkYSBwZWxvcyBkb2lzIHByaW1laXJvcyBjb21wb25lbnRlczogJDEwICsgMiA9IDEyJC4iLCAiUGFzc28gMzogQ2FsY3VsYXIgYSBwcm9wb3LDp8OjbzogJFxcdGV4dHtQcm9wb3LDp8Ojb30gPSAxMiAvIDEyLjUgPSAwLjk2JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuOTZ9LCB7ImVudW5jaWFkbyI6ICJNb3N0cmUgbWF0ZW1hdGljYW1lbnRlLCB1dGlsaXphbmRvIGEgZGVjb21wb3Npw6fDo28gZXNwZWN0cmFsICRcXG1hdGhiZntBfSA9IFxcbWF0aGJme1V9IFxcbWF0aGJme1xcTGFtYmRhfSBcXG1hdGhiZntVfV57XFx0b3B9JCwgcXVlIG8gZGV0ZXJtaW5hbnRlIGRlIHVtYSBtYXRyaXogXFxzaW3DqXRyaWNhICRcXG1hdGhiZntBfSQgw6kgbyBwcm9kdXRvIGRlIHNldXMgYXV0b3ZhbG9yZXM6ICRcXGRldChcXG1hdGhiZntBfSkgPSBcXHByb2Rfe2k9MX1ee259IFxcbGFtYmRhX2kkLiIsICJkaWNhIjogIlVzZSBhIHByb3ByaWVkYWRlIG11bHRpcGxpY2F0aXZhIGRvIGRldGVybWluYW50ZTogJFxcZGV0KFxcbWF0aGJme0FCfSkgPSBcXGRldChcXG1hdGhiZntBfSlcXGRldChcXG1hdGhiZntCfSkkIGUgbyBmYXRvIGRlIHF1ZSAkXFxtYXRoYmZ7VX0kIMOpIG9ydG9nb25hbCwgbG9nbyAkXFxkZXQoXFxtYXRoYmZ7VX1ee1xcdG9wfSkgPSAxL1xcZGV0KFxcbWF0aGJme1V9KSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IEFwbGljYXIgbyBkZXRlcm1pbmFudGUgbmEgZGVjb21wb3Npw6fDo286ICRcXGRldChcXG1hdGhiZntBfSkgPSBcXGRldChcXG1hdGhiZntVfSBcXG1hdGhiZntcXExhbWJkYX0gXFxtYXRoYmZ7VX1ee1xcdG9wfSkkLiIsICJQYXNzbyAyOiBVdGlsaXphciBhIHByb3ByaWVkYWRlIG11bHRpcGxpY2F0aXZhOiAkXFxkZXQoXFxtYXRoYmZ7QX0pID0gXFxkZXQoXFxtYXRoYmZ7VX0pIFxcY2RvdCBcXGRldChcXG1hdGhiZntcXExhbWJkYX0pIFxcY2RvdCBcXGRldChcXG1hdGhiZntVfV57XFx0b3B9KSQuIiwgIlBhc3NvIDM6IENvbW8gJFxcbWF0aGJme1V9JCDDqSBvcnRvZ29uYWwsICRcXG1hdGhiZntVfV57XFx0b3B9XFxtYXRoYmZ7VX0gPSBcXG1hdGhiZntJfSQsIGVudMOjbyAkXFxkZXQoXFxtYXRoYmZ7VX1ee1xcdG9wfVxcbWF0aGJme1V9KSA9IFxcZGV0KFxcbWF0aGJme1V9XntcXHRvcH0pXFxkZXQoXFxtYXRoYmZ7VX0pID0gMSQuIElzc28gaW1wbGljYSAkXFxkZXQoXFxtYXRoYmZ7VX1ee1xcdG9wfSkgPSAxL1xcZGV0KFxcbWF0aGJme1V9KSQuIiwgIlBhc3NvIDQ6IFN1YnN0aXR1aXI6ICRcXGRldChcXG1hdGhiZntBfSkgPSBcXGRldChcXG1hdGhiZntVfSkgXFxjZG90IFxcZGV0KFxcbWF0aGJme1xcTGFtYmRhfSkgXFxjZG90IFxcZnJhY3sxfXtcXGRldChcXG1hdGhiZntVfSl9ID0gXFxkZXQoXFxtYXRoYmZ7XFxMYW1iZGF9KSQuIiwgIlBhc3NvIDU6IE8gZGV0ZXJtaW5hbnRlIGRlIHVtYSBtYXRyaXogZGlhZ29uYWwgw6kgbyBwcm9kdXRvIGRlIHNldXMgZWxlbWVudG9zIGRhIGRpYWdvbmFsOiAkXFxkZXQoXFxtYXRoYmZ7XFxMYW1iZGF9KSA9IFxccHJvZF97aT0xfV57bn0gXFxsYW1iZGFfaSQuIExvZ28sICRcXGRldChcXG1hdGhiZntBfSkgPSBcXHByb2Rfe2k9MX1ee259IFxcbGFtYmRhX2kkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH1dfQ==').decode('utf-8'))


    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do total de exercícios
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discursivas = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcqs) + len(discursivas)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    # Barra de progresso e status
    st.markdown("---")
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    st.markdown("---")
    
    # Renderização de Questões de Múltipla Escolha
    for i, questao in enumerate(mcqs):
        st.subheader(f"Questão MCQ {i + 1}")
        st.write(questao.get("enunciado", ""))
        
        # Execução de gráfico Plotly se existir
        codigo_plotly = questao.get("codigo_plotly")
        if codigo_plotly:
            local_vars = {}
            try:
                exec(codigo_plotly, globals(), local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
            except Exception as e:
                st.error(f"Erro ao renderizar gráfico: {e}")
    
        # Alternativas
        alternativas = questao.get("alternativas", {})
        opcao_escolhida = st.radio("Escolha uma opção:", list(alternativas.values()), key=f"radio_mcq_{i}", index=None)
        
        # Dica e Referência
        if st.button("💡 Dica", key=f"btn_dica_mcq_{i}"):
            st.info(questao.get("dica", "Dica indisponível"))
        
        ref = questao.get("referencia_livro")
        if ref:
            st.markdown(f"📖 *Referência: {ref}*")
            
        # Verificação
        if st.button("✅ Verificar Resposta", key=f"btn_verify_mcq_{i}"):
            # Encontrar a chave da alternativa correta
            chaves = list(alternativas.keys())
            valores = list(alternativas.values())
            idx_correto = chaves.index(questao.get("alternativa_correta"))
            texto_correto = valores[idx_correto]
            
            if opcao_escolhida == texto_correto:
                st.session_state.respostas_certas[f"mcq_{i}"] = True
                st.success("Correto! Muito bem.")
                st.rerun()
            else:
                st.session_state.respostas_certas[f"mcq_{i}"] = False
                st.error("Resposta incorreta. Tente novamente!")
                
        with st.expander("✅ Ver Gabarito Comentado"):
            st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
        st.markdown("---")
    
    # Renderização de Questões Discursivas
    for i, questao in enumerate(discursivas):
        st.subheader(f"Questão Discursiva {i + 1}")
        st.write(questao.get("enunciado", ""))
        
        # Execução de gráfico Plotly
        codigo_plotly = questao.get("codigo_plotly")
        if codigo_plotly:
            local_vars = {}
            try:
                exec(codigo_plotly, globals(), local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
            except Exception as e:
                st.error(f"Erro ao renderizar gráfico: {e}")
                
        st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
        
        # Validação Numérica se houver
        valor_esperado = questao.get("resposta_numerica_esperada")
        if valor_esperado is not None:
            user_val = st.number_input("Digite o resultado numérico calculado:", key=f"num_disc_{i}", format="%.4f")
            if st.button("Validar Cálculo", key=f"btn_valid_disc_{i}"):
                if abs(user_val - valor_esperado) <= max(0.01, 0.01 * abs(valor_esperado)):
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                    st.success("Resposta Numérica Correta! Excelente trabalho.")
                    st.rerun()
                else:
                    st.session_state.respostas_certas[f"disc_{i}"] = False
                    st.error("O valor calculado difere do gabarito. Verifique e tente novamente.")
        else:
            # Checkbox para controle de estudo
            if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                st.session_state.respostas_certas[f"disc_{i}"] = True
            else:
                st.session_state.respostas_certas[f"disc_{i}"] = False
                
        # Botões auxiliares
        if st.button("💡 Dica", key=f"btn_dica_disc_{i}"):
            st.info(questao.get("dica", "Dica indisponível"))
            
        ref = questao.get("referencia_livro")
        if ref:
            st.markdown(f"📖 *Referência: {ref}*")
            
        with st.expander("✅ Ver Resolução Detalhada"):
            passos = questao.get("gabarito_passo_a_passo", [])
            for p in passos:
                st.write(f"- {p}")
        st.markdown("---")
