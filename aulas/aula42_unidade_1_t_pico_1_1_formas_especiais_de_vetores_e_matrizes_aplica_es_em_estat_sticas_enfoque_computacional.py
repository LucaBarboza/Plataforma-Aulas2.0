import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDEgLSBUw7NwaWNvIDEuMTogRm9ybWFzIGVzcGVjaWFpcyBkZSB2ZXRvcmVzIGUgbWF0cml6ZXMsIGFwbGljYcOnw7VlcyBlbSBFc3RhdMOtc3RpY2FzOiBlbmZvcXVlIGNvbXB1dGFjaW9uYWwiLCAicmVmZXJlbmNpYXNfYmlibGlvZ3JhZmljYXNfZmluYWlzIjogWyJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDE0LCBwcC4gMzQwLTM0NSIsICJCaXNwbywgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzIC0gQ2FwLiAyLCBwcC4gNTUtNjIiLCAiTHVuYSAmIEVzdGV2ZXMsIFTDs3BpY29zIGRlIE1hdHJpemVzIC0gQ2FwLiAxLCBwcC4gMS0zIiwgIkx1bmEgJiBFc3RldmVzLCBUw7NwaWNvcyBkZSBNYXRyaXplcyAtIENhcC4gMywgcHAuIDYxLTY1IiwgIkJpc3BvLCBJbnRyb2R1w6fDo28gYW9zIE1vZGVsb3MgTGluZWFyZXMgLSBDYXAuIDcsIHBwLiA0LTEwIl19').decode('utf-8'))

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

    # Cabeçalho do subtópico
    st.header(r"Arquitetura e Representação Matricial em Estatística")
    
    # Introdução teórica fragmentada
    st.markdown(r"""
    A transição da análise estatística univariada para a complexidade exigida pelos modelos de dados contemporâneos marca um divisor de águas na formação do estatístico e do cientista de dados. Enquanto a estatística clássica, em sua gênese, frequentemente lidava com variáveis isoladas, a realidade experimental moderna impõe uma estrutura de dados de alta dimensionalidade.
    
    Para organizar essa realidade, a arquitetura matricial apresenta-se não apenas como um artifício de conveniência, mas como o alicerce fundamental, a "gramática" sobre a qual toda a álgebra multivariada é construída. Sem o formalismo matricial, estaríamos condenados a representar relações entre variáveis através de sistemas de equações escalares extenuantes e de difícil interpretação.
    """)
    
    st.info(r"Uma matriz é, essencialmente, uma coleção ordenada de informações onde cada dimensão carrega um significado ontológico distinto: linhas representam observações e colunas representam variáveis.")
    
    st.markdown(r"""
    Historicamente, a necessidade de organizar dados experimentais de forma sistemática acompanhou o desenvolvimento da própria estatística. Foi a codificação da álgebra linear o que permitiu que estruturas de grade fossem manipuladas de modo eficiente. Convencionamos que a matriz $\mathbf{A}_{(n \times m)}$ transforma um conjunto caótico de observações em um objeto matemático único, passível de transposição, inversão e projeção.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Arquitetura Matricial")
    st.markdown(r"A estrutura formal da matriz $\mathbf{A}_{(n \times m)}$ define o espaço de trabalho do pesquisador, onde $n$ captura a realidade das unidades amostrais e $m$ denota a profundidade dos atributos.")
    st.latex(r"\mathbf{A}_{(n \times m)} = \begin{pmatrix} a_{11} & a_{12} & \cdots & a_{1m} \\ a_{21} & a_{22} & \cdots & a_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nm} \end{pmatrix}")
    
    # Deduções Analíticas (Hardcoded sem loops)
    st.markdown(r"Abaixo, detalhamos as operações fundamentais que regem a manipulação destes objetos:")
    st.latex(r"\text{Definição de matriz } \mathbf{A}_{(n \times m)} \text{ com elementos } a_{ij}.")
    st.latex(r"\text{Transposição: } \mathbf{A}^{\top} = (a_{ji}), \text{ onde o elemento } (i, j) \text{ torna-se } (j, i).")
    st.latex(r"\text{Vetor coluna: } \mathbf{a}_{(n \times 1)} = (a_1, a_2, \dots, a_n)^{\top}.")
    st.latex(r"\text{Vetor linha (transposta): } \mathbf{a}^{\top}_{(1 \times n)} = (a_1, a_2, \dots, a_n).")
    
    # Contexto de aplicação (Prosa adicional)
    st.markdown(r"""
    A intuição geométrica é o ganho mais significativo dessa representação. Ao visualizarmos as colunas de uma matriz como vetores em um espaço de dimensão $n$, interpretamos relações estatísticas como projeções e distâncias. Além disso, softwares modernos como Python e R tratam essas matrizes como blocos contíguos de memória, otimizando drasticamente algoritmos de regressão e aprendizado de máquina.
    """)
    
    # Exemplo Prático Richo (Hardcoded sem loops)
    st.subheader(r"📈 Casos de Aplicação Prática: Produção Industrial")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Monitoramento de Máquinas")
        st.markdown(r"Uma empresa monitora a produção diária de duas máquinas ($M_1$ e $M_2$) ao longo de três dias. Dados: Dia 1: 10 e 20 unidades; Dia 2: 15 e 25 unidades; Dia 3: 12 e 22 unidades.")
        
        st.latex(r"\mathbf{A}_{(3 \times 2)} = \begin{pmatrix} 10 & 20 \\ 15 & 25 \\ 12 & 22 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Linha 1 (Dia 1):** $a_{11}=10, a_{12}=20$.")
        st.markdown(r"- **Linha 2 (Dia 2):** $a_{21}=15, a_{22}=25$.")
        st.markdown(r"- **Linha 3 (Dia 3):** $a_{31}=12, a_{32}=22$.")
        
        st.success(r"A matriz $\mathbf{A}$ permite que a produção total por máquina seja calculada via operações de soma vetorial. Em um modelo de regressão linear $\mathbf{y} = \mathbf{X}\beta + \epsilon$, $\beta$ representaria o vetor de coeficientes, permitindo estimar a produção esperada a partir das variáveis de entrada.")
    
    # Considerações finais
    st.markdown(r"""
    ---
    **Nota Final:** O domínio dessa arquitetura é o passaporte do estatístico para lidar com problemas que transcendem a tabulação simples, alcançando áreas como visão computacional e séries temporais. Internalize que este formalismo não é uma burocracia, mas uma ferramenta de libertação intelectual.
    """)

    import streamlit as st
    import numpy as np
    
    # Cabeçalho principal
    st.header(r"Tipologia Fundamental de Matrizes")
    
    st.markdown(r"""
    A transição do pensamento estatístico univariado para o domínio multivariado exige uma mudança de paradigma na organização da informação. Quando lidamos com dados vetoriais, a álgebra matricial torna-se a linguagem intrínseca que descreve dependências, variabilidades e estruturas latentes.
    """)
    
    st.info(r"As matrizes não são meras grades numéricas, mas estruturas que impõem propriedades geométricas vitais para a inferência estatística, como o isolamento de variáveis e a estabilidade numérica.")
    
    st.markdown(r"""
    ### 📐 O Coração Matemático: Tipologia Fundamental de Matrizes
    
    A estrutura fundamental das matrizes divide-se em categorias que otimizam o processamento de modelos complexos:
    
    *   **Matrizes Quadradas ($n \times n$):** Representam endomorfismos, atuando como o alicerce para a análise da matriz de covariância populacional $\Sigma$, encapsulando toda a estrutura de dispersão do sistema.
    *   **Matrizes Diagonais:** Definidas pela ausência de acoplamento entre variáveis ($a_{ij} = 0$ para $i \neq j$), sendo o objetivo final de técnicas como a Análise de Componentes Principais.
    *   **Matrizes Triangulares:** Essenciais para a eficiência computacional, permitindo a resolução estável de sistemas lineares via decomposição de Cholesky.
    """)
    
    # Dedução Analítica
    st.subheader(r"Estrutura Formal das Matrizes")
    st.markdown(r"Abaixo, formalizamos as propriedades estruturais elementares que definem a tipologia de uma matriz $\mathbf{A}_{(n)}$:")
    
    st.latex(r"\text{Seja } \mathbf{A}_{(n)} \text{ uma matriz quadrada.}")
    st.latex(r"\text{Matriz Diagonal: } \forall i \neq j, a_{ij} = 0")
    st.latex(r"\text{Matriz Identidade: } \forall i, a_{ii} = 1 \text{ e } a_{ij}=0, i \neq j")
    st.latex(r"\text{Matriz Triangular Superior: } i > j \implies a_{ij} = 0")
    st.latex(r"\text{Matriz Triangular Inferior: } i < j \implies a_{ij} = 0")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Tipologia Fundamental de Matrizes")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Identificação e Transposição")
        st.markdown(r"Considere o modelo de regressão onde a matriz de covariância dos erros é $\Sigma = \text{diag}\{\sigma_1^2, \sigma_2^2\}$. Analise a matriz $\mathbf{A}$ abaixo:")
        
        st.latex(r"\mathbf{A} = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Identificação:** Observamos que $a_{21}=0$. Logo, $\mathbf{A}$ é uma matriz triangular superior.")
        st.markdown(r"- **Cálculo da Transposta:** Invertendo linhas por colunas, obtemos $\mathbf{A}^{\top} = \begin{pmatrix} 2 & 0 \\ 1 & 3 \end{pmatrix}$.")
        st.markdown(r"- **Classificação da Transposta:** Como os elementos acima da diagonal principal são nulos, $\mathbf{A}^{\top}$ é classificada como triangular inferior.")
        
        st.success(r"A transposição altera a estrutura triangular, um fato explorado em algoritmos de decomposição que exigem que o sistema esteja organizado em formas específicas para garantir a convergência numérica em modelos estatísticos.")
    
    st.markdown(r"""
    ---
    ### Conclusão Teórica
    A compreensão exaustiva dessas tipologias permite que o cientista estatístico identifique, sob o capô dos algoritmos, como problemas complexos são reduzidos. Seja através da ortogonalização em matrizes diagonais ou da substituição sucessiva em matrizes triangulares, o rigor na manipulação desses objetos é o que garante a validade das inferências e a robustez dos estimadores $\hat{\beta}$.
    """)

    # Cabeçalho do Subtópico
    st.header(r"Propriedades e Operações Matriciais de Base")
    
    # Prosa Teórica - Bloco 1
    st.markdown(r"""
    A álgebra matricial não é apenas uma ferramenta de conveniência notacional; ela é a estrutura fundamental sobre a qual edificamos todo o edifício da estatística moderna e da inferência multivariada. Para o estatístico, a matriz é o contêiner lógico de um conjunto de dados, onde as colunas frequentemente representam variáveis aleatórias e as linhas representam observações individuais extraídas de uma população.
    """)
    
    st.markdown(r"""
    Compreender como manipulamos esses objetos exige um domínio rigoroso das operações elementares, cujas propriedades transcendem a simples aritmética, permitindo-nos modelar fenômenos complexos através de sistemas lineares compactos. Quando iniciamos nosso estudo, devemos encarar a matriz não como um arranjo estático, mas como um operador que transforma espaços vetoriais.
    """)
    
    # Destaque Teórico
    st.info(r"As propriedades das operações matriciais são a base necessária para derivar estimadores de mínimos quadrados ordinários e para decompor a variabilidade inerente a um modelo estatístico.")
    
    # Prosa Teórica - Bloco 2
    st.markdown(r"""
    A operação de soma matricial, embora intuitiva, exige conformidade dimensional absoluta, refletindo a necessidade de que estamos comparando entidades da mesma natureza no espaço amostral. O produto matricial, por sua vez, representa a aplicação sucessiva de projeções e combinações lineares.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Produto e Transposição")
    st.latex(r"r_{ik} = \sum_{j=1}^{m} a_{ij}b_{jk}, \quad (\mathbf{A}\mathbf{B})^{\top} = \mathbf{B}^{\top}\mathbf{A}^{\top}")
    
    # Dedução Analítica (Direta e Sem Expanders)
    st.markdown(r"### 🧠 Demonstração da Inversão no Produto Transposto")
    st.latex(r"(\mathbf{A}\mathbf{B})^{\top} = (r_{ik})^{\top} = (r_{ki})")
    st.markdown(r"O elemento $r_{ki}$ do produto original é definido pela soma dos produtos dos elementos correspondentes:")
    st.latex(r"r_{ki} = \sum_{j=1}^{m} a_{kj}b_{ji}")
    st.markdown(r"Aplicando a transposição sobre o somatório, temos a reordenação dos índices:")
    st.latex(r"(\mathbf{A}\mathbf{B})^{\top} = \left( \sum_{j=1}^{m} a_{kj}b_{ji} \right)^{\top} = \sum_{j=1}^{m} b_{ji}a_{kj}")
    st.markdown(r"Pela definição de transposta, $b_{ji}$ é o elemento da matriz $\mathbf{B}^{\top}$ e $a_{kj}$ da matriz $\mathbf{A}^{\top}$, concluindo assim a demonstração:")
    st.latex(r"\sum_{j=1}^{m} b_{ji}a_{kj} = \mathbf{B}^{\top}\mathbf{A}^{\top}")
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática: Cálculo da Matriz de Produto Cruzado")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Produto $\mathbf{X}^{\top}\mathbf{X}$")
        st.markdown(r"Para um conjunto de dados com $n=3$ observações e 2 colunas, calculamos a matriz de produto $\mathbf{M} = \mathbf{X}^{\top}\mathbf{X}$, essencial nas equações normais de uma regressão linear.")
        
        st.latex(r"\mathbf{X} = \begin{pmatrix} 1 & 10 \\ 1 & 20 \\ 1 & 30 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Primeiro, obtemos a transposta: $\mathbf{X}^{\top} = \begin{pmatrix} 1 & 1 & 1 \\ 10 & 20 & 30 \end{pmatrix}$")
        st.markdown(r"- Realizamos o produto $\mathbf{M} = \mathbf{X}^{\top}\mathbf{X}$:")
        st.latex(r"\mathbf{M} = \begin{pmatrix} 1 & 1 & 1 \\ 10 & 20 & 30 \end{pmatrix} \begin{pmatrix} 1 & 10 \\ 1 & 20 \\ 1 & 30 \end{pmatrix} = \begin{pmatrix} 3 & 60 \\ 60 & 1400 \end{pmatrix}")
        
        st.success(r"A matriz resultante é simétrica, um comportamento esperado para o produto $\mathbf{X}^{\top}\mathbf{X}$. Esta propriedade garante que o sistema de equações normais seja bem comportado para a inversão necessária na estimativa dos coeficientes $\hat{\beta}$.")
    
    # Prosa Teórica - Bloco Final
    st.markdown(r"""
    A simetria, como vimos na matriz de covariância ($\Sigma$), não é um detalhe estético; ela garante a existência de autovalores reais e autovetores ortogonais. Dominar essas operações é o que separa um analista que apenas aplica pacotes prontos de um cientista de dados capaz de derivar novos métodos e interpretar as entranhas matemáticas de um modelo.
    """)

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título da Seção
    st.header(r"Geometria e Ortogonalidade em Espaços Vetoriais")
    
    # Introdução com Estilo
    st.markdown(r"""
    A geometria vetorial aplicada à estatística representa uma mudança de paradigma fundamental na forma como compreendemos a inferência e a modelagem. Ao adotarmos a perspectiva dos espaços vetoriais, enxergamos variáveis como direções em um espaço euclidiano de dimensão $n$, transformando a análise de dados em uma tarefa de decomposição geométrica.
    """)
    
    st.info(r"A correlação entre variáveis é interpretada como o ângulo entre dois vetores. Ortogonalidade, por sua vez, é a tradução geométrica da independência linear e da ausência de redundância informacional.")
    
    # Seção: Fundamentos Matemáticos
    st.markdown(r"### 📐 O Coração Matemático: Produto Interno e Norma")
    st.markdown(r"O produto interno formaliza a afinidade entre vetores, enquanto a norma define a dispersão dos dados. Em termos estatísticos, a correlação amostral é o produto interno de vetores centralizados normalizados.")
    
    st.latex(r"\langle \mathbf{x}, \mathbf{y} \rangle = \mathbf{x}^{\top}\mathbf{y} = \sum_{i=1}^{n} x_i y_i")
    st.latex(r"\|\mathbf{x}\| = \sqrt{\sum_{i=1}^{n} x_i^2}")
    
    # Demonstração Analítica
    st.markdown(r"### 🧮 Demonstração: O Teorema de Pitágoras no Espaço Amostral")
    st.markdown(r"A relação de ortogonalidade reflete diretamente na decomposição da variância total:")
    
    st.latex(r"\|\mathbf{x} + \mathbf{y}\|^2 = \langle \mathbf{x} + \mathbf{y}, \mathbf{x} + \mathbf{y} \rangle")
    st.markdown(r"Ao expandir o produto, distribuímos os termos:")
    st.latex(r"\|\mathbf{x} + \mathbf{y}\|^2 = \langle \mathbf{x}, \mathbf{x} \rangle + 2\langle \mathbf{x}, \mathbf{y} \rangle + \langle \mathbf{y}, \mathbf{y} \rangle")
    st.markdown(r"Se os vetores forem ortogonais, o termo central desaparece, resultando na identidade clássica:")
    st.latex(r"\|\mathbf{x} + \mathbf{y}\|^2 = \|\mathbf{x}\|^2 + \|\mathbf{y}\|^2")
    
    # Simulador Interativo
    st.markdown(r"### 🌐 Simulador: Visualizador de Ortogonalidade")
    col1, col2 = st.columns(2)
    
    with col1:
        x1_val = st.slider(r"x1 do Vetor X", -5.0, 5.0, 1.0, key=r"x1_subtopico_4")
        y1_val = st.slider(r"y1 do Vetor X", -5.0, 5.0, 0.0, key=r"y1_subtopico_4")
    with col2:
        x2_val = st.slider(r"x2 do Vetor Y", -5.0, 5.0, 0.0, key=r"x2_subtopico_4")
        y2_val = st.slider(r"y2 do Vetor Y", -5.0, 5.0, 1.0, key=r"y2_subtopico_4")
    
    prod_int = (x1_val * x2_val) + (y1_val * y2_val)
    
    # Plotagem do Simulador
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, x1_val], y=[0, y1_val], name=r"Vetor X", line=dict(color="#1E3A8A", width=3)))
    fig.add_trace(go.Scatter(x=[0, x2_val], y=[0, y2_val], name=r"Vetor Y", line=dict(color="#10B981", width=3)))
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Visualização de Ortogonalidade (2D)</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)"),
        xaxis=dict(title=dict(text="Dimensão 1", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Dimensão 2", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True)
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")
    
    # Laudo Dinâmico
    if abs(prod_int) < 0.1:
        st.info(r"O produto interno é próximo de zero. Os vetores estão ortogonais, indicando independência linear perfeita no sistema.")
    else:
        st.warning(rf"O produto interno é {prod_int:.2f}. Os vetores não são ortogonais; existe uma correlação ou redundância informacional de {prod_int:.2f} entre as variáveis.")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática: Sensores de Medição")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Verificação de Ortogonalidade de Sensores")
        st.markdown(r"Sensores de medição fornecem erros normalizados $\mathbf{v}_1 = [1, 0]^{\top}$ e $\mathbf{v}_2 = [0, 1]^{\top}$. Verifique a ortogonalidade.")
        st.latex(r"\mathbf{v}_1 = [1, 0]^{\top}, \mathbf{v}_2 = [0, 1]^{\top}")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Passo 1: Calcular o produto interno $\langle \mathbf{v}_1, \mathbf{v}_2 \rangle = (1)(0) + (0)(1) = 0$")
        st.markdown(r"- Passo 2: A matriz de transformação $\mathbf{Q}$ é a identidade, pois $\mathbf{Q}^{\top}\mathbf{Q} = \mathbf{I}$")
        st.success(r"A ortogonalidade dos vetores de erro garante que as medições sejam independentes, validando a integridade dos dados coletados pelos sensores no sistema de monitoramento.")
    
    # Conclusão
    st.markdown(r"### 💡 Nota do Pesquisador: Inferência como Geometria")
    st.markdown(r"""
    Ao avançarmos nos capítulos sobre inferência, devemos lembrar que o teste de hipótese $H_0: \beta_1 = 0$ é, fundamentalmente, uma verificação de quanto o vetor resposta se projeta sobre o subespaço dos preditores restantes. A maestria nestes conceitos geomátricos é o que separa a aplicação mecânica de fórmulas da compreensão profunda da estrutura dos dados.
    """)

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    
    # Cabeçalho do Subtópico
    st.header(r"Formas Quadráticas e sua Classificação Definida")
    
    # Prosa Expandida - Segmentada
    st.markdown(r"""
    Sejam bem-vindos a este aprofundamento essencial em nossa jornada pela álgebra linear aplicada à estatística matemática. No estudo da inferência estatística e da análise multivariada, frequentemente nos deparamos com a necessidade de sintetizar a variabilidade de um sistema complexo em um único escalar, uma medida que capture a dispersão multidimensional de forma coesa e rigorosa.
    """)
    
    st.info(r"As formas quadráticas emergem como a estrutura fundamental sobre a qual construímos nossas noções de distância, variância e otimização. Elas mapeiam um vetor de observações para o espaço dos reais sob a égide de uma matriz de transformação.")
    
    st.markdown(r"""
    Ao trabalharmos com a forma quadrática $Q(\mathbf{x}) = \mathbf{x}^{\top}\mathbf{A}\mathbf{x}$, operamos sob premissas que garantem o rigor estatístico:
    - **Simetria:** Assumimos que $\mathbf{A} = \mathbf{A}^{\top}$, pois a parte antissimétrica anula-se no mapeamento escalar.
    - **Definitividade:** A classificação 'positiva definida' é a espinha dorsal que impede dispersões negativas em matrizes de variância-covariância.
    - **Geometria:** Estas formas modelam desde elipses até a topologia de distribuições multivariadas.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 Formalismo e Estrutura Algébrica")
    st.latex(r"Q(\mathbf{x}) = \mathbf{x}^{\top}\mathbf{A}\mathbf{x} = \sum_{i=1}^{n} \sum_{j=1}^{n} a_{ij} x_i x_j")
    
    # Demonstração Analítica
    st.markdown(r"### 🧮 O Coração Matemático: Diagonalização e Espectro")
    st.latex(r"Q(\mathbf{x}) = \mathbf{x}^{\top}\mathbf{A}\mathbf{x}")
    st.markdown(r"Considerando a decomposição espectral $\mathbf{A} = \mathbf{P}\mathbf{\Lambda}\mathbf{P}^{\top}$, onde $\mathbf{\Lambda}$ é a matriz diagonal de autovalores:")
    st.latex(r"Q(\mathbf{x}) = \mathbf{x}^{\top}(\mathbf{P}\mathbf{\Lambda}\mathbf{P}^{\top})\mathbf{x}")
    st.markdown(r"Aplicando a mudança de variáveis $\mathbf{y} = \mathbf{P}^{\top}\mathbf{x}$, simplificamos a forma quadrática para a base dos autovetores:")
    st.latex(r"Q(\mathbf{y}) = \mathbf{y}^{\top}\mathbf{\Lambda}\mathbf{y} = \sum_{i=1}^{n} \lambda_i y_i^2")
    
    # Simulador Interativo
    st.subheader(r"📈 Explorador de Formas Quadráticas")
    col1, col2 = st.columns([1, 1])
    with col1:
        a_val = st.slider(r"Parâmetro 'a' (interação x1, x2)", -4.0, 4.0, 0.0, step=0.1, key=r"a_slider_subtopico_5")
    with col2:
        b_val = st.slider(r"Parâmetro 'b' (coeficiente x2^2)", -2.0, 4.0, 1.0, step=0.1, key=r"b_slider_subtopico_5")
    
    # Geração de dados para o gráfico
    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + a_val*X*Y + b_val*Y**2
    
    fig = go.Figure(data=[go.Contour(
        z=Z, x=x, y=y,
        colorscale='RdBu',
        contours=dict(showlines=True, start=0, end=10, size=1)
    )])
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Superfície de Dispersão Q(x)</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="x1", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="x2", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_5")
    
    # Laudo Dinâmico
    det = 1 * b_val - (a_val/2)**2
    status = r"Positiva Definida" if det > 0 and 1 > 0 else (r"Indefinida" if det < 0 else r"Semidefinida")
    st.info(f"Análise Técnica: Com a configuração atual (a={a_val}, b={b_val}), o determinante da matriz é {det:.2f}. A matriz é classificada como {status}, indicando que a superfície representa um {r'elipsoide estável' if det > 0 else 'ponto de sela ou colapso dimensional'}.")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática: Análise de Erro de Monitoramento")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Erro de Monitoramento Quadrático")
        st.markdown(r"O erro de monitoramento é $Q(\mathbf{x}) = x_1^2 + 4x_1x_2 + 5x_2^2$. Encontre a matriz $\mathbf{A}$ e classifique-a.")
        st.latex(r"\mathbf{A} = \begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix}")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo do polinômio característico: $\det(\mathbf{A} - \lambda\mathbf{I}) = \lambda^2 - 6\lambda + 1 = 0$")
        st.markdown(r"- Autovalores obtidos: $\lambda_1 \approx 5.83, \lambda_2 \approx 0.17$")
        st.success(r"Conclusão: Como todos os autovalores são estritamente positivos ($\lambda_i > 0$), a matriz é positiva definida, assegurando que o sistema de monitoramento gere medidas de erro estatisticamente válidas.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDEgLSBUw7NwaWNvIDEuMTogRm9ybWFzIGVzcGVjaWFpcyBkZSB2ZXRvcmVzIGUgbWF0cml6ZXMsIGFwbGljYcOnw7VlcyBlbSBFc3RhdMOtc3RpY2FzOiBlbmZvcXVlIGNvbXB1dGFjaW9uYWwiLCAicXVlc3RvZXNfbXVsdGlwbGFfZXNjb2xoYSI6IFt7ImVudW5jaWFkbyI6ICJFbSB1bSBleHBlcmltZW50byBkZSBwcmVjaXPDo28gYWdyw61jb2xhLCBwZXNxdWlzYWRvcmVzIGNvbGV0YXJhbSBkYWRvcyBzb2JyZSA1IHBhcmNlbGFzIGRpc3RpbnRhcyBkZSB1bWEgcGxhbnRhw6fDo28uIFBhcmEgY2FkYSBwYXJjZWxhLCBmb3JhbSBtZWRpZG9zIDMgYXRyaWJ1dG9zOiBhbHR1cmEgZGEgcGxhbnRhIChlbSBjbSksIHJlbmRpbWVudG8gKGVtIGtnL23CsikgZSB0ZW9yIGRlIHVtaWRhZGUgKCUpLiBBbyBvcmdhbml6YXIgZXNzZXMgZGFkb3MgZW0gdW1hIGVzdHJ1dHVyYSBtYXRyaWNpYWwgJFxcbWF0aGJme0F9X3sobiBcXHRpbWVzIG0pfSQsIGFzc2luYWxlIGEgYWx0ZXJuYXRpdmEgcXVlIGRlc2NyZXZlIGNvcnJldGFtZW50ZSBhIGRpbWVuc8OjbyBkYSBtYXRyaXogZSBhIGludGVycHJldGHDp8OjbyBkbyBlbGVtZW50byAkYV97aWp9JC4iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgbWF0cml6IHRlbSBkaW1lbnPDo28gJFxcbWF0aGJme0F9X3soMyBcXHRpbWVzIDUpfSQsIG9uZGUgbyBlbGVtZW50byAkYV97aWp9JCByZXByZXNlbnRhIG8gdmFsb3IgZGEgdmFyacOhdmVsICRpJCBuYSBwYXJjZWxhICRqJC4iLCAiQiI6ICJBIG1hdHJpeiB0ZW0gZGltZW5zw6NvICRcXG1hdGhiZntBfV97KDUgXFx0aW1lcyAzKX0kLCBvbmRlICRuPTUkIHJlcHJlc2VudGEgYXMgb2JzZXJ2YcOnw7VlcyAocGFyY2VsYXMpIGUgJG09MyQgYXMgdmFyacOhdmVpcyAoYXRyaWJ1dG9zKS4iLCAiQyI6ICJBIG1hdHJpeiB0ZW0gZGltZW5zw6NvICRcXG1hdGhiZntBfV97KDUgXFx0aW1lcyAzKX0kLCBvbmRlIG8gZWxlbWVudG8gJGFfe2lqfSQgcmVwcmVzZW50YSBhIG3DqWRpYSBkYSB2YXJpw6F2ZWwgJGokIG5hIHBhcmNlbGEgJGkkLiIsICJEIjogIkEgbWF0cml6IHRlbSBkaW1lbnPDo28gJFxcbWF0aGJme0F9X3soMyBcXHRpbWVzIDUpfSQsIG9uZGUgJG49MyQgw6kgbyBuw7ptZXJvIGRlIHBhcmNlbGFzIGUgJG09NSQgw6kgbyBuw7ptZXJvIGRlIHZhcmnDoXZlaXMgb2JzZXJ2YWRhcy4iLCAiRSI6ICJBIG1hdHJpeiDDqSBxdWFkcmFkYSBkZSBvcmRlbSA1LCBwb2lzIHBhcmEgY2FkYSB1bWEgZGFzIDUgcGFyY2VsYXMsIGVzcGVyYS1zZSBxdWUgbyBuw7ptZXJvIGRlIHZhcmnDoXZlaXMgc2VqYSBpZ3VhbCBhbyBuw7ptZXJvIGRlIGFtb3N0cmFzLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSwgbmEgbm90YcOnw6NvIG1hdHJpY2lhbCBlc3RhdMOtc3RpY2EgcGFkcsOjbywgYXMgbGluaGFzIGRhIG1hdHJpeiByZXByZXNlbnRhbSBhcyB1bmlkYWRlcyBhbW9zdHJhaXMgKG9ic2VydmHDp8O1ZXMpIGUgYXMgY29sdW5hcyByZXByZXNlbnRhbSBhcyB2YXJpw6F2ZWlzIG91IGF0cmlidXRvcyBtZWRpZG9zLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTmEgZXN0YXTDrXN0aWNhLCBwYXJhIG9yZ2FuaXphciB1bSBiYW5jbyBkZSBkYWRvcywgZXN0YWJlbGVjZW1vcyBxdWUgJFxcbWF0aGJme0F9X3sobiBcXHRpbWVzIG0pfSQgcG9zc3VpICRuJCBsaW5oYXMgZSAkbSQgY29sdW5hcy4gQ29tbyB0ZW1vcyA1IHBhcmNlbGFzICh1bmlkYWRlcyBleHBlcmltZW50YWlzKSwgZGVmaW5pbW9zICRuPTUkLiBDb21vIHRlbW9zIDMgYXRyaWJ1dG9zIChhbHR1cmEsIHJlbmRpbWVudG8gZSB1bWlkYWRlKSwgZGVmaW5pbW9zICRtPTMkLiBMb2dvLCBhIG1hdHJpeiAkXFxtYXRoYmZ7QX0kIMOpIGRvIHRpcG8gJCg1IFxcdGltZXMgMykkLiBPIGVsZW1lbnRvICRhX3tpan0kIG5hIGludGVyc2XDp8OjbyBkYSBsaW5oYSAkaSQgZSBjb2x1bmEgJGokIHJlcHJlc2VudGEgbyB2YWxvciBkYSAkaiQtw6lzaW1hIHZhcmnDoXZlbCBwYXJhIGEgJGkkLcOpc2ltYSBwYXJjZWxhLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW0gYW5hbGlzdGEgZGUgSW9UIGVtIHVtYSBmw6FicmljYSBpbnRlbGlnZW50ZSBtb25pdG9yYSAxMDAgc2Vuc29yZXMgaW5kdXN0cmlhaXMgc2ltdWx0YW5lYW1lbnRlIGEgY2FkYSBtaW51dG8uIE8gYW5hbGlzdGEgb3JnYW5pemEgYXMgbGVpdHVyYXMgZGUgNTAgaW5zdGFudGVzIGRlIHRlbXBvIGVtIHVtYSBtYXRyaXogJFxcbWF0aGJme1h9X3sobiBcXHRpbWVzIG0pfSQuIFNlIGNhZGEgbGluaGEgY29ycmVzcG9uZGUgYSB1bSBpbnN0YW50ZSBkZSB0ZW1wbyBlIGNhZGEgY29sdW5hIGEgdW0gc2Vuc29yIGVzcGVjw61maWNvLCBxdWFsIGRhcyBhZmlybWHDp8O1ZXMgYWJhaXhvIG1lbGhvciBkZWZpbmUgYSBlc3RydXR1cmEgZG9zIHZldG9yZXMgZSBkYXMgZGltZW5zw7Vlcz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgbWF0cml6IHBvc3N1aSAkbj0xMDAkIGxpbmhhcyBlICRtPTUwJCBjb2x1bmFzLCBvbmRlIGNhZGEgY29sdW5hIMOpIHVtIHZldG9yICRcXG1hdGhiZnt4fV97KDUwIFxcdGltZXMgMSl9JCByZXByZXNlbnRhbmRvIHVtIHNlbnNvci4iLCAiQiI6ICJBIG1hdHJpeiBwb3NzdWkgJG49NTAkIGxpbmhhcyBlICRtPTEwMCQgY29sdW5hcywgb25kZSBjYWRhIGxpbmhhIMOpIHVtIHZldG9yICRcXG1hdGhiZnt4fV97KDEgXFx0aW1lcyAxMDApfSQgY29udGVuZG8gYXMgbGVpdHVyYXMgZGUgdG9kb3Mgb3Mgc2Vuc29yZXMgZW0gdW0gaW5zdGFudGUgJGkkLiIsICJDIjogIkEgbWF0cml6IHBvc3N1aSAkbj01MCQgbGluaGFzIGUgJG09MTAwJCBjb2x1bmFzLCBvbmRlIGNhZGEgY29sdW5hIMOpIHVtIHZldG9yICRcXG1hdGhiZnt4fV97KDEwMCBcXHRpbWVzIDEpfSQgY29udGVuZG8gYXMgbGVpdHVyYXMgZGUgdW0gw7puaWNvIHNlbnNvciBhbyBsb25nbyBkZSB0b2RvcyBvcyBpbnN0YW50ZXMuIiwgIkQiOiAiQSBtYXRyaXogcG9zc3VpICRuPTEwMCQgbGluaGFzIGUgJG09NTAkIGNvbHVuYXMsIGltcG9zc2liaWxpdGFuZG8gYSBhbsOhbGlzZSB2ZXRvcmlhbCBkYXMgY29sdW5hcy4iLCAiRSI6ICJBIGVzdHJ1dHVyYSBkZSBkYWRvcyBkZXZlIHNlciBvYnJpZ2F0b3JpYW1lbnRlIHVtIHZldG9yICRcXG1hdGhiZnt4fV97KDE1MCBcXHRpbWVzIDEpfSQgcGFyYSBtYW50ZXIgYSBpbnRlZ3JpZGFkZSB0ZW1wb3JhbC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIkNvbnNpZGVyZSBxdWUsIHNlIGFzIGxpbmhhcyBzw6NvIGluc3RhbnRlcyBkZSB0ZW1wbyAoJG49NTAkKSBlIGFzIGNvbHVuYXMgc8OjbyBzZW5zb3JlcyAoJG09MTAwJCksIHVtIHZldG9yIGNvbHVuYSBlc3BlY8OtZmljbyAkXFxtYXRoYmZ7eH1faiQgY29ycmVzcG9uZGVyw6EgYW9zIGRhZG9zIGRlIHVtIMO6bmljbyBzZW5zb3Igb2JzZXJ2YWRvIGFvIGxvbmdvIGRlIHRvZGFzIGFzIDUwIGxpbmhhcy4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlRlbW9zICRuPTUwJCAoaW5zdGFudGVzKSBlICRtPTEwMCQgKHNlbnNvcmVzKS4gQXNzaW0sIGEgbWF0cml6IMOpICRcXG1hdGhiZntYfV97KDUwIFxcdGltZXMgMTAwKX0kLiBVbSB2ZXRvciBjb2x1bmEgJFxcbWF0aGJme3h9X2okIChvbmRlICRqPTEsIFxcZG90cywgMTAwJCkgY29udMOpbSBhcyA1MCBvYnNlcnZhw6fDtWVzIHRlbXBvcmFpcyBkYXF1ZWxlIHNlbnNvciBlc3BlY8OtZmljbywgcmVzdWx0YW5kbyBlbSB1bSB2ZXRvciBkZSBkaW1lbnPDo28gJCg1MCBcXHRpbWVzIDEpJC4gQSBhbHRlcm5hdGl2YSBDIGRlc2NyZXZlIGV4YXRhbWVudGUgYSBkaW1lbnPDo28gZSBhIG5hdHVyZXphIGRvIHZldG9yIGNvbHVuYS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBkZSBlZmljacOqbmNpYSBob3NwaXRhbGFyLCBtb2RlbG91LXNlIG8gZmx1eG8gZGUgdHJhbnNmZXLDqm5jaWEgZGUgcGFjaWVudGVzIGVudHJlIHF1YXRybyBkZXBhcnRhbWVudG9zIChFbWVyZ8OqbmNpYSwgQ2zDrW5pY2EgTcOpZGljYSwgVVRJIGUgQ2FyZGlvbG9naWEpLiBBIG1hdHJpeiBkZSBmbHV4byAkXFxtYXRoYmZ7Rn1feyg0KX0kIGFwcmVzZW50YSB2YWxvcmVzIG9uZGUgbyBlbGVtZW50byAkZl97aWp9JCByZXByZXNlbnRhIG8gbsO6bWVybyBkZSBwYWNpZW50ZXMgdHJhbnNmZXJpZG9zIGRvIGRlcGFydGFtZW50byAkaSQgcGFyYSBvIGRlcGFydGFtZW50byAkaiQuIE9ic2Vydm91LXNlIHF1ZSAkZl97aWp9ID0gMCQgcGFyYSB0b2RvICRpIDwgaiQsIG8gcXVlIGluZGljYSBxdWUgbsOjbyBvY29ycmVtIHRyYW5zZmVyw6puY2lhcyBkZSBkZXBhcnRhbWVudG9zIGRlIG1haW9yIGNvbXBsZXhpZGFkZSBwYXJhIGRlcGFydGFtZW50b3MgZGUgbWVub3IgY29tcGxleGlkYWRlIGRlIGZvcm1hIGRpcmV0YS4gUXVhbCDDqSBhIGNsYXNzaWZpY2HDp8OjbyBnZW9tw6l0cmljYSBkZXN0YSBtYXRyaXogJFxcbWF0aGJme0Z9JD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk1hdHJpeiBEaWFnb25hbCwgcG9pcyBvIGZsdXhvIMOpIHplcm8gZm9yYSBkYSBkaWFnb25hbCBwcmluY2lwYWwuIiwgIkIiOiAiTWF0cml6IElkZW50aWRhZGUsIHBvaXMgb3MgdmFsb3JlcyBuYSBkaWFnb25hbCBwcmluY2lwYWwgc8OjbyB1bml0w6FyaW9zLiIsICJDIjogIk1hdHJpeiBUcmlhbmd1bGFyIEluZmVyaW9yLCBwb2lzIHRvZG9zIG9zIGVsZW1lbnRvcyBhY2ltYSBkYSBkaWFnb25hbCBwcmluY2lwYWwgKCRpIDwgaiQpIHPDo28gbnVsb3MuIiwgIkQiOiAiTWF0cml6IFRyaWFuZ3VsYXIgU3VwZXJpb3IsIHBvaXMgdG9kb3Mgb3MgZWxlbWVudG9zIGFiYWl4byBkYSBkaWFnb25hbCBwcmluY2lwYWwgKCRpID4gaiQpIHPDo28gbnVsb3MuIiwgIkUiOiAiTWF0cml6IEVzY2FsYXIsIHBvaXMgdG9kb3Mgb3MgZWxlbWVudG9zIGRhIGRpYWdvbmFsIHPDo28gaWd1YWlzLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiQW5hbGlzZSBhIGRlZmluacOnw6NvIGRhIHBvc2nDp8OjbyBkb3MgZWxlbWVudG9zIG51bG9zLiBTZSBvcyBlbGVtZW50b3MgYWNpbWEgZGEgZGlhZ29uYWwgcHJpbmNpcGFsICgkaSA8IGokKSBzw6NvIG51bG9zLCBhIG1hdHJpeiBndWFyZGEgc2V1cyB2YWxvcmVzIHJlbGV2YW50ZXMgYXBlbmFzIG5hIGRpYWdvbmFsIGUgYWJhaXhvIGRlbGEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQb3IgZGVmaW5pw6fDo28sIHVtYSBtYXRyaXogw6kgZGl0YSBUcmlhbmd1bGFyIEluZmVyaW9yICgkXFxtYXRoYmZ7VH1fSSQpIHF1YW5kbyB0b2RvcyBvcyBlbGVtZW50b3MgYWNpbWEgZGEgZGlhZ29uYWwgcHJpbmNpcGFsIHPDo28gaWd1YWlzIGEgemVyby4gT3Ugc2VqYSwgJHRfe2lqfSA9IDAkIHBhcmEgJGkgPCBqJC4gTm8gY2FzbyBkYSBtYXRyaXogZGUgZmx1eG8gJFxcbWF0aGJme0Z9JCwgbyBlbnVuY2lhZG8gYWZpcm1hIGV4cGxpY2l0YW1lbnRlIHF1ZSAkZl97aWp9ID0gMCQgcGFyYSAkaSA8IGokLCBjYXJhY3Rlcml6YW5kbyBleGF0YW1lbnRlIGVzc2EgZXN0cnV0dXJhLiBSZWZlcsOqbmNpYTogTHVuYSAmIEVzdGV2ZXMsIFTDs3BpY29zIGRlIE1hdHJpemVzLCBDYXAgMSwgcC4gMi4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoZGF0YT1nby5IZWF0bWFwKHo9W1sxMCwgMCwgMCwgMF0sIFs1LCA4LCAwLCAwXSwgWzIsIDMsIDcsIDBdLCBbMSwgMSwgMiwgNV1dLCBjb2xvcnNjYWxlPSdCbHVlcycsIHNob3dzY2FsZT1GYWxzZSkpOyBmaWcudXBkYXRlX2xheW91dCh0aXRsZT0nTWF0cml6IGRlIEZsdXhvIChUcmlhbmd1bGFyIEluZmVyaW9yKScsIHhheGlzPWRpY3QodGl0bGU9J0RlcGFydGFtZW50byBkZXN0aW5vJyksIHlheGlzPWRpY3QodGl0bGU9J0RlcGFydGFtZW50byBvcmlnZW0nKSkiLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgVMOzcGljb3MgZGUgTWF0cml6ZXMsIENhcCAxLCBwLiAyIn0sIHsiZW51bmNpYWRvIjogIkVtIHVtIHNpc3RlbWEgZGUgc2Vuc29yaWFtZW50byBJb1QsIGEgY2FsaWJyYcOnw6NvIGRlIHF1YXRybyBzZW5zb3JlcyDDqSByZWFsaXphZGEgYXRyYXbDqXMgZGUgdW1hIG1hdHJpeiBkZSBnYW5obyAkXFxtYXRoYmZ7R31feyg0KX0kLiBQYXJhIGV2aXRhciBpbnRlcmZlcsOqbmNpYSBjcnV6YWRhIGVudHJlIG9zIHNpbmFpcywgbyBzaXN0ZW1hIGZvaSBwcm9qZXRhZG8gZGUgdGFsIGZvcm1hIHF1ZSBhIG1hdHJpeiByZXN1bHRhbnRlIHBvc3N1aSBlbGVtZW50b3MgJGdfe2lqfSA9IDAkIHBhcmEgdG9kbyAkaSBcXG5lcSBqJC4gQWzDqW0gZGlzc28sIG9zIGdhbmhvcyBkZSBjYWxpYnJhw6fDo28gc8OjbyB0b2RvcyBhanVzdGFkb3MgcGFyYSBvIHZhbG9yIHVuaXTDoXJpbyAoJGdfe2lpfSA9IDEkKS4gQ29tbyBwb2RlbW9zIGNsYXNzaWZpY2FyIHRlY25pY2FtZW50ZSBhIG1hdHJpeiBkZSBnYW5obyAkXFxtYXRoYmZ7R31feyg0KX0kPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTWF0cml6IE51bGEsIHBvaXMgbsOjbyBow6EgaW50ZXJmZXLDqm5jaWEgZW50cmUgc2Vuc29yZXMuIiwgIkIiOiAiTWF0cml6IElkZW50aWRhZGUgJFxcbWF0aGJme0l9X3soNCl9JCwgcG9pcyDDqSB1bWEgbWF0cml6IGRpYWdvbmFsIGNvbSB0b2RvcyBvcyBlbGVtZW50b3MgZGEgZGlhZ29uYWwgaWd1YWlzIGEgMS4iLCAiQyI6ICJNYXRyaXogVHJpYW5ndWxhciBTdXBlcmlvciwgcG9pcyBhIGRpYWdvbmFsIGNvbnTDqW0gdmFsb3JlcyB1bml0w6FyaW9zLiIsICJEIjogIk1hdHJpeiBRdWFkcmFkYSBuw6NvLWRpYWdvbmFsLCBwb2lzIHBvc3N1aSBxdWF0cm8gc2Vuc29yZXMuIiwgIkUiOiAiTWF0cml6IGRlIHBvc3RvIGluY29tcGxldG8sIHBvaXMgbyBkZXRlcm1pbmFudGUgw6kgbnVsby4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgdW1hIG1hdHJpeiBxdWUgcG9zc3VpIGFwZW5hcyBlbGVtZW50b3MgbmEgZGlhZ29uYWwgcHJpbmNpcGFsIGUgZXN0ZXMgc8OjbyBpZ3VhaXMgYSAxIHJlY2ViZSB1bSBub21lIGVzcGVjw61maWNvIG5hIMOhbGdlYnJhIG1hdHJpY2lhbC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlVtYSBtYXRyaXogZGlhZ29uYWwgw6kgYXF1ZWxhIGVtIHF1ZSAkZF97aWp9ID0gMCQgcGFyYSAkaSBcXG5lcSBqJC4gUXVhbmRvLCBhZGljaW9uYWxtZW50ZSwgdG9kb3Mgb3MgZWxlbWVudG9zIGRhIGRpYWdvbmFsIHByaW5jaXBhbCBzw6NvIGlndWFpcyBhIDEgKCRkX3tpaX0gPSAxJCksIGEgbWF0cml6IMOpIGRlbm9taW5hZGEgTWF0cml6IElkZW50aWRhZGUsIGRlbm90YWRhIHBvciAkXFxtYXRoYmZ7SX1feyhuKX0kLiBPIGVudW5jaWFkbyBkZXNjcmV2ZSBleGF0YW1lbnRlIGVzc2EgY29uZGnDp8OjbyBwYXJhICRcXG1hdGhiZntHfV97KDQpfSQuIFJlZmVyw6puY2lhOiBOw612ZWEgQmlzcG8sIEF1bGEgMzogTWF0cml6ZXMsIHAuIDUuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJOw612ZWEgQmlzcG8sIE1BVEQ0MSBJbnRyb2R1w6fDo28gYW9zIE1vZGVsb3MgTGluZWFyZXMsIEF1bGEgMywgcC4gNSJ9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gZGUgb3RpbWl6YcOnw6NvIGRlIHJlZGVzIGRlIHNlbnNvcmVzIElvVCwgdW0gZW5nZW5oZWlybyBwcmVjaXNhIG1hbmlwdWxhciBhIG1hdHJpeiBkZSBjb25lY3RpdmlkYWRlICRcXG1hdGhiZntDfV97KDMgXFx0aW1lcyAzKX0kIGVudHJlIHRyw6pzIG7Ds3MgcHJpbmNpcGFpcy4gQSBtYXRyaXogw6kgZGVmaW5pZGEgY29tbyAkXFxtYXRoYmZ7Q30gPSBcXG1hdGhiZntBfSArIFxcbWF0aGJme0J9JCwgb25kZSAkXFxtYXRoYmZ7QX0gPSBcXGJlZ2lue3BtYXRyaXh9IDIgJiAxICYgMCBcXFxcIDEgJiAzICYgMSBcXFxcIDAgJiAxICYgNCBcXGVuZHtwbWF0cml4fSQgZSAkXFxtYXRoYmZ7Qn0gPSBcXGJlZ2lue3BtYXRyaXh9IDAgJiAyICYgMSBcXFxcIDIgJiAwICYgLTEgXFxcXCAxICYgLTEgJiAwIFxcZW5ke3BtYXRyaXh9JC4gQ29tIGJhc2UgbmFzIHByb3ByaWVkYWRlcyBkYXMgb3BlcmHDp8O1ZXMgbWF0cmljaWFpcywgYXNzaW5hbGUgYSBhbHRlcm5hdGl2YSBjb3JyZXRhIHNvYnJlIGEgbWF0cml6IHJlc3VsdGFudGUgJFxcbWF0aGJme0N9JCBlIHN1YSBzaW1ldHJpYS4iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgbWF0cml6ICRcXG1hdGhiZntDfSQgbsOjbyDDqSBcXHNpbcOpdHJpY2EsIHBvaXMgYSBzb21hIGRlIG1hdHJpemVzIFxcc2ltw6l0cmljYXMgJFxcbWF0aGJme0F9JCBlICRcXG1hdGhiZntCfSQgbsOjbyBnYXJhbnRlIHNpbWV0cmlhLiIsICJCIjogIkEgbWF0cml6ICRcXG1hdGhiZntDfSQgw6kgXFxzaW3DqXRyaWNhIGUgc2V1cyBlbGVtZW50b3MgZGEgZGlhZ29uYWwgcHJpbmNpcGFsIHPDo28gJGNfezExfT0yLCBjX3syMn09MywgY197MzN9PTQkLiIsICJDIjogIkEgbWF0cml6ICRcXG1hdGhiZntDfSQgcG9zc3VpIGVsZW1lbnRvcyAkY197MTJ9PTMkIGUgJGNfezIxfT0tMyQsIGxvZ28gbsOjbyDDqSBcXHNpbcOpdHJpY2EuIiwgIkQiOiAiQSBtYXRyaXogJFxcbWF0aGJme0N9JCDDqSBkaWFnb25hbCwgcG9pcyAkXFxtYXRoYmZ7QX0kIGUgJFxcbWF0aGJme0J9JCBwb3NzdWVtIGEgbWVzbWEgZXN0cnV0dXJhLiIsICJFIjogIkEgbWF0cml6ICRcXG1hdGhiZntDfSQgw6kgXFxzaW3DqXRyaWNhIGUgbyBlbGVtZW50byAkY197MjN9JCDDqSBpZ3VhbCBhICQwJC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiRSIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgc2UgJFxcbWF0aGJme0F9ID0gXFxtYXRoYmZ7QX1ee1xcdG9wfSQgZSAkXFxtYXRoYmZ7Qn0gPSBcXG1hdGhiZntCfV57XFx0b3B9JCwgZW50w6NvICQoXFxtYXRoYmZ7QX0rXFxtYXRoYmZ7Qn0pXntcXHRvcH0gPSBcXG1hdGhiZntBfV57XFx0b3B9ICsgXFxtYXRoYmZ7Qn1ee1xcdG9wfSA9IFxcbWF0aGJme0F9ICsgXFxtYXRoYmZ7Qn0kLiBDYWxjdWxlIGNhZGEgZWxlbWVudG8gJGNfe2lqfSA9IGFfe2lqfSArIGJfe2lqfSQgZSB2ZXJpZmlxdWUgc2UgJGNfe2lqfSA9IGNfe2ppfSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQcmltZWlybywgb2JzZXJ2YW1vcyBxdWUgJFxcbWF0aGJme0F9JCDDqSBcXHNpbcOpdHJpY2EgcG9pcyAkYV97MTJ9PWFfezIxfT0xJCwgJGFfezEzfT1hX3szMX09MCQgZSAkYV97MjN9PWFfezMyfT0xJC4gU2ltaWxhcm1lbnRlLCAkXFxtYXRoYmZ7Qn0kIMOpIFxcc2ltw6l0cmljYSBwb2lzICRiX3sxMn09Yl97MjF9PTIkLCAkYl97MTN9PWJfezMxfT0xJCBlICRiX3syM309Yl97MzJ9PS0xJC4gQSBzb21hICRcXG1hdGhiZntDfSA9IFxcbWF0aGJme0F9ICsgXFxtYXRoYmZ7Qn0kIHJlc3VsdGEgZW06ICRcXG1hdGhiZntDfSA9IFxcYmVnaW57cG1hdHJpeH0gMiswICYgMSsyICYgMCsxIFxcXFwgMSsyICYgMyswICYgMSsoLTEpIFxcXFwgMCsxICYgMSsoLTEpICYgNCswIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAyICYgMyAmIDEgXFxcXCAzICYgMyAmIDAgXFxcXCAxICYgMCAmIDQgXFxlbmR7cG1hdHJpeH0kLiBDb21vICRcXG1hdGhiZntDfSA9IFxcbWF0aGJme0N9XntcXHRvcH0kLCBlbGEgw6kgXFxzaW3DqXRyaWNhLiBPIGVsZW1lbnRvICRjX3syM30gPSBhX3syM30gKyBiX3syM30gPSAxICsgKC0xKSA9IDAkLiBQb3J0YW50bywgYSBhbHRlcm5hdGl2YSBFIGVzdMOhIGNvcnJldGEuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyBwcm9kdXRvIG1hdHJpY2lhbCAkXFxtYXRoYmZ7Un0gPSBcXG1hdGhiZntBfVxcbWF0aGJme0J9JCwgb25kZSAkXFxtYXRoYmZ7QX1feygyIFxcdGltZXMgMyl9ID0gXFxiZWdpbntwbWF0cml4fSAxICYgMiAmIDMgXFxcXCAwICYgMSAmIDIgXFxlbmR7cG1hdHJpeH0kIGUgJFxcbWF0aGJme0J9X3soMyBcXHRpbWVzIDIpfSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAxICYgMSBcXFxcIDIgJiAwIFxcZW5ke3BtYXRyaXh9JC4gSWRlbnRpZmlxdWUgbyB2YWxvciBkbyBlbGVtZW50byAkcl97MTJ9JCBkYSBtYXRyaXogcmVzdWx0YW50ZSAkXFxtYXRoYmZ7Un0kIGUgYSBkaW1lbnPDo28gZGEgbWF0cml6IGZpbmFsLiIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJHJfezEyfSA9IDEkIGUgYSBkaW1lbnPDo28gw6kgJCgzIFxcdGltZXMgMykkLiIsICJCIjogIiRyX3sxMn0gPSAyJCBlIGEgZGltZW5zw6NvIMOpICQoMiBcXHRpbWVzIDIpJC4iLCAiQyI6ICIkcl97MTJ9ID0gMyQgZSBhIGRpbWVuc8OjbyDDqSAkKDMgXFx0aW1lcyAyKSQuIiwgIkQiOiAiJHJfezEyfSA9IDAkIGUgYSBkaW1lbnPDo28gw6kgJCgyIFxcdGltZXMgMikkLiIsICJFIjogIiRyX3sxMn0gPSA0JCBlIGEgZGltZW5zw6NvIMOpICQoMiBcXHRpbWVzIDMpJC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk8gZWxlbWVudG8gJHJfe2lrfSQgw6kgbyBwcm9kdXRvIGVzY2FsYXIgZGEgbGluaGEgJGkkIGRlICRcXG1hdGhiZntBfSQgcGVsYSBjb2x1bmEgJGskIGRlICRcXG1hdGhiZntCfSQuIFBhcmEgJHJfezEyfSQsIHVzZSBhIHByaW1laXJhIGxpbmhhIGRlICRcXG1hdGhiZntBfSQgZSBhIHNlZ3VuZGEgY29sdW5hIGRlICRcXG1hdGhiZntCfSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGRpbWVuc8OjbyBkbyBwcm9kdXRvICRcXG1hdGhiZntSfSA9IFxcbWF0aGJme0F9X3soMiBcXHRpbWVzIDMpfSBcXG1hdGhiZntCfV97KDMgXFx0aW1lcyAyKX0kIMOpIGRhZGEgcGVsYXMgbGluaGFzIGRlICRcXG1hdGhiZntBfSQgZSBjb2x1bmFzIGRlICRcXG1hdGhiZntCfSQsIG91IHNlamEsICQoMiBcXHRpbWVzIDIpJC4gUGFyYSBlbmNvbnRyYXIgJHJfezEyfSQsIG11bHRpcGxpY2Ftb3MgYSBsaW5oYSAxIGRlICRcXG1hdGhiZntBfSQgcGVsYSBjb2x1bmEgMiBkZSAkXFxtYXRoYmZ7Qn0kOiAkcl97MTJ9ID0gKDEgXFx0aW1lcyAwKSArICgyIFxcdGltZXMgMSkgKyAoMyBcXHRpbWVzIDApID0gMCArIDIgKyAwID0gMiQuIFBvcnRhbnRvLCBhIGFsdGVybmF0aXZhIEIgw6kgYSBjb3JyZXRhLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gc2lzdGVtYSBkZSBtb25pdG9yYW1lbnRvIGRlIElvVCwgZG9pcyBzZW5zb3JlcyBjb2xldGFtIGxlaXR1cmFzIGRlIHZhcmlhw6fDo28gZGUgdGVtcGVyYXR1cmEgZW0gZG9pcyBpbnN0YW50ZXMgZGlzdGludG9zLCByZXByZXNlbnRhZG9zIHBlbG9zIHZldG9yZXMgJFxcbWF0aGJme3h9ID0gWzQsIC0yXV57XFx0b3B9JCBlICRcXG1hdGhiZnt5fSA9IFsxLCAyXV57XFx0b3B9JCBlbSAkXFxtYXRoYmJ7Un1eMiQuIENvbnNpZGVyYW5kbyBhIGRlZmluacOnw6NvIGRlIG9ydG9nb25hbGlkYWRlIGVtIGVzcGHDp29zIHZldG9yaWFpcywgcXVhbCBkYXMgYWZpcm1hw6fDtWVzIGRlc2NyZXZlIGNvcnJldGFtZW50ZSBhIHJlbGHDp8OjbyBnZW9tw6l0cmljYSBlbnRyZSBvcyB2ZXRvcmVzIGRlIGxlaXR1cmEgZG9zIHNlbnNvcmVzPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiT3MgdmV0b3JlcyBzw6NvIG9ydG9nb25haXMsIHBvaXMgc2V1IHByb2R1dG8gaW50ZXJubyAkXFxsYW5nbGUgXFxtYXRoYmZ7eH0sIFxcbWF0aGJme3l9IFxccmFuZ2xlID0gMCQuIiwgIkIiOiAiT3MgdmV0b3JlcyBzw6NvIG9ydG9nb25haXMsIHBvaXMgYSBub3JtYSBkZSBhbWJvcyDDqSBpZ3VhbCBhIDEuIiwgIkMiOiAiT3MgdmV0b3JlcyBuw6NvIHPDo28gb3J0b2dvbmFpcywgcG9pcyBzZXUgcHJvZHV0byBpbnRlcm5vICRcXGxhbmdsZSBcXG1hdGhiZnt4fSwgXFxtYXRoYmZ7eX0gXFxyYW5nbGUgPSA4IFxcbmVxIDAkLiIsICJEIjogIk9zIHZldG9yZXMgc8OjbyBvcnRvZ29uYWlzLCBwb2lzIGEgc29tYSBkZSBzZXVzIGNvbXBvbmVudGVzIMOpIHplcm8uIiwgIkUiOiAiT3MgdmV0b3JlcyBzw6NvIGxpbmVhcm1lbnRlIGRlcGVuZGVudGVzIGUsIHBvcnRhbnRvLCBwYXJhbGVsb3MuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIG8gcHJvZHV0byBpbnRlcm5vIMOpIGNhbGN1bGFkbyBjb21vIGEgc29tYSBkb3MgcHJvZHV0b3MgZG9zIGVsZW1lbnRvcyBjb3JyZXNwb25kZW50ZXM6ICRcXHN1bV97aT0xfV57bn0geF9pIHlfaSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIHZlcmlmaWNhciBhIG9ydG9nb25hbGlkYWRlLCBjYWxjdWxhbW9zIG8gcHJvZHV0byBpbnRlcm5vOiAkXFxsYW5nbGUgXFxtYXRoYmZ7eH0sIFxcbWF0aGJme3l9IFxccmFuZ2xlID0gKDQgXFx0aW1lcyAxKSArICgtMiBcXHRpbWVzIDIpID0gNCAtIDQgPSAwJC4gQ29tbyBvIHByb2R1dG8gaW50ZXJubyDDqSBleGF0YW1lbnRlIHplcm8sIG9zIHZldG9yZXMgZm9ybWFtIHVtIMOibmd1bG8gcmV0byBkZSAkOTBeXFxjaXJjJCwgYXRlbmRlbmRvIMOgIGNvbmRpw6fDo28gZGUgb3J0b2dvbmFsaWRhZGUuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVswLCA0XSwgeT1bMCwgLTJdLCBtb2RlPSdsaW5lcyttYXJrZXJzJywgbmFtZT1yJ1ZldG9yICRcXG1hdGhiZnt4fSQnLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0zKSkpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMCwgMV0sIHk9WzAsIDJdLCBtb2RlPSdsaW5lcyttYXJrZXJzJywgbmFtZT1yJ1ZldG9yICRcXG1hdGhiZnt5fSQnLCBsaW5lPWRpY3QoY29sb3I9JyMxMEI5ODEnLCB3aWR0aD0zKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nT3J0b2dvbmFsaWRhZGUgZGUgU2Vuc29yZXMnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJywgeGF4aXM9ZGljdChmaXhlZHJhbmdlPVRydWUpLCB5YXhpcz1kaWN0KGZpeGVkcmFuZ2U9VHJ1ZSkpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiU2VqYSAkXFxtYXRoYmZ7UX0kIHVtYSBtYXRyaXogJDIgXFx0aW1lcyAyJCBjdWphcyBjb2x1bmFzIGZvcm1hbSB1bWEgYmFzZSBvcnRvbm9ybWFsIHBhcmEgJFxcbWF0aGJie1J9XjIkLiBRdWFsIHByb3ByaWVkYWRlIGZ1bmRhbWVudGFsIGRhIMOhbGdlYnJhIG1hdHJpY2lhbCBkZXZlIHNlciBzYXRpc2ZlaXRhIHBvciBlc3RhIG1hdHJpej8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIiRcXG1hdGhiZntRfSArIFxcbWF0aGJme1F9XntcXHRvcH0gPSBcXG1hdGhiZnswfSQiLCAiQiI6ICIkXFxtYXRoYmZ7UX1ee1xcdG9wfVxcbWF0aGJme1F9ID0gXFxtYXRoYmZ7SX1feygyKX0kIiwgIkMiOiAiJFxcbWF0aGJme1F9XntcXHRvcH0gPSBcXG1hdGhiZntRfV57LTF9JCBhcGVuYXMgc2UgbyBkZXRlcm1pbmFudGUgZm9yIHplcm8uIiwgIkQiOiAiQSBzb21hIGRvcyBlbGVtZW50b3MgZGUgY2FkYSBsaW5oYSBkZXZlIHNlciAxLiIsICJFIjogIkEgbm9ybWEgZGUgY2FkYSBsaW5oYSBkZXZlIHNlciAwLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiVW1hIG1hdHJpeiBvcnRvZ29uYWwgcHJlc2VydmEgbyBwcm9kdXRvIGludGVybm8gZSBhIG5vcm1hLCBvIHF1ZSBpbXBsaWNhIHF1ZSBzdWFzIGNvbHVuYXMgc8OjbyB2ZXRvcmVzIHVuaXTDoXJpb3MgZSBvcnRvZ29uYWlzIGVudHJlIHNpLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUG9yIGRlZmluacOnw6NvLCB1bWEgbWF0cml6ICRcXG1hdGhiZntRfSQgw6kgb3J0b2dvbmFsIHNlIHN1YXMgY29sdW5hcyBmb3JtYW0gdW1hIGJhc2Ugb3J0b25vcm1hbC4gSXNzbyBzaWduaWZpY2EgcXVlLCBwYXJhIGNvbHVuYXMgJFxcbWF0aGJme3F9X2kkLCB0ZW1vcyAkXFxsYW5nbGUgXFxtYXRoYmZ7cX1faSwgXFxtYXRoYmZ7cX1faiBcXHJhbmdsZSA9IDEkIHNlICRpPWokIGUgJDAkIHNlICRpIFxcbmVxIGokLiBNYXRyaWNpYWxtZW50ZSwgaXNzbyDDqSBleHByZXNzbyBwZWxhIGNvbmRpw6fDo28gJFxcbWF0aGJme1F9XntcXHRvcH1cXG1hdGhiZntRfSA9IFxcbWF0aGJme0l9X3sobil9JC4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBkZSBvdGltaXphw6fDo28gZGUgcG9ydGbDs2xpbyBkZSBhdGl2b3MgZmluYW5jZWlyb3MsIHVtIGFuYWxpc3RhIG1vZGVsYSBvIHJpc2NvIHRvdGFsIGF0cmF2w6lzIGRlIHVtYSBmb3JtYSBxdWFkcsOhdGljYSAkUShcXG1hdGhiZnt4fSkgPSBcXG1hdGhiZnt4fV57XFx0b3B9XFxtYXRoYmZ7QX1cXG1hdGhiZnt4fSQsIG9uZGUgJFxcbWF0aGJme3h9JCByZXByZXNlbnRhIGFzIHByb3BvcsOnw7VlcyBhbG9jYWRhcyBlbSAkbiQgYXRpdm9zIGUgJFxcbWF0aGJme0F9JCDDqSBhIG1hdHJpeiBkZSB2YXJpw6JuY2lhcyBlIGNvdmFyacOibmNpYXMgZG9zIHJldG9ybm9zIGRvcyBhdGl2b3MuIFBhcmEgcXVlIG8gYW5hbGlzdGEgZ2FyYW50YSBxdWUgbyByaXNjbyBjYWxjdWxhZG8gc2VqYSBzZW1wcmUgbsOjbyBuZWdhdGl2byBwYXJhIHF1YWxxdWVyIGFsb2Nhw6fDo28gJFxcbWF0aGJme3h9IFxcbmVxIFxcbWF0aGJmezB9JCBlIHF1ZSBvIHNpc3RlbWEgc2VqYSBlc3TDoXZlbCAoZXZpdGFuZG8gcmV0b3Jub3MgbnVsb3MgcGFyYSBhdGl2b3MgbsOjbyBudWxvcyksIHF1YWwgY2xhc3NpZmljYcOnw6NvIGRlIGZvcm1hIHF1YWRyw6F0aWNhIGEgbWF0cml6ICRcXG1hdGhiZntBfSQgZGV2ZSBzYXRpc2ZhemVyPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTmVnYXRpdmEgRGVmaW5pZGEsIHBvaXMgb3MgcmV0b3Jub3MgZGV2ZW0gc2VyIGNvbnRpZG9zLiIsICJCIjogIlBvc2l0aXZhIERlZmluaWRhLCBnYXJhbnRpbmRvIHF1ZSAkUShcXG1hdGhiZnt4fSkgPiAwJCBwYXJhIHRvZG8gJFxcbWF0aGJme3h9IFxcbmVxIFxcbWF0aGJmezB9JC4iLCAiQyI6ICJJbmRlZmluaWRhLCBwYXJhIHBlcm1pdGlyIG9zY2lsYcOnw7VlcyBkZSBtZXJjYWRvIHBvc2l0aXZhcyBlIG5lZ2F0aXZhcy4iLCAiRCI6ICJTZW1pIFBvc2l0aXZhIERlZmluaWRhLCBwb2lzIG8gcmlzY28gcG9kZSBzZXIgbnVsbyBtZXNtbyBjb20gYXRpdm9zIGFsb2NhZG9zLiIsICJFIjogIlNlbWkgTmVnYXRpdmEgRGVmaW5pZGEsIGdhcmFudGluZG8gcXVlIG8gcmlzY28gdG90YWwgc2VqYSBzZW1wcmUgY29udHJvbGFkby4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgZW0gZXN0YXTDrXN0aWNhIG11bHRpdmFyaWFkYSwgYSBtYXRyaXogZGUgdmFyacOibmNpYXMgZSBjb3ZhcmnDom5jaWFzIGRldmUgcG9zc3VpciBwcm9wcmllZGFkZXMgcXVlIGFzc2VndXJlbSBxdWUgYSBkaXNwZXJzw6NvIHRvdGFsIG7Do28gc2VqYSBuZWdhdGl2YS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgbWF0cml6IGRlIHZhcmnDom5jaWFzIGUgY292YXJpw6JuY2lhcyAkXFxtYXRoYmZ7QX0kIGRldmUgc2VyIFBvc2l0aXZhIERlZmluaWRhLiBNYXRlbWF0aWNhbWVudGUsIGEgZm9ybWEgcXVhZHLDoXRpY2EgJFEoXFxtYXRoYmZ7eH0pID0gXFxtYXRoYmZ7eH1ee1xcdG9wfVxcbWF0aGJme0F9XFxtYXRoYmZ7eH0kIHJlcHJlc2VudGEgYSB2YXJpw6JuY2lhIGRlIHVtYSBjb21iaW5hw6fDo28gbGluZWFyIGRvcyBhdGl2b3MuIENvbW8gYSB2YXJpw6JuY2lhIGRlIHF1YWxxdWVyIGNvbWJpbmHDp8OjbyBuw6NvIHRyaXZpYWwgZGV2ZSBzZXIgZXN0cml0YW1lbnRlIHBvc2l0aXZhLCBhIGNvbmRpw6fDo28gJFEoXFxtYXRoYmZ7eH0pID4gMCQgcGFyYSB0b2RvICRcXG1hdGhiZnt4fSBcXG5lcSBcXG1hdGhiZnswfSQgZGVmaW5lIGEgbWF0cml6IGNvbW8gUG9zaXRpdmEgRGVmaW5pZGEuIFNlIGVsYSBmb3NzZSBTZW1pIFBvc2l0aXZhIERlZmluaWRhLCBleGlzdGlyaWEgdW1hIGNvbWJpbmHDp8OjbyBkZSBhdGl2b3MgY29tIHZhcmnDom5jaWEgemVybywgbyBxdWUgbsOjbyByZWZsZXRlIGEgcmVhbGlkYWRlIGRlIGF0aXZvcyBjb20gdm9sYXRpbGlkYWRlLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtYSBmb3JtYSBxdWFkcsOhdGljYSBhc3NvY2lhZGEgYSB1bSBzaXN0ZW1hIGRlIGNvbnRyb2xlIHTDqXJtaWNvIGRlIHNlbnNvcmVzIElvVCwgZGFkYSBwb3IgJFEoXFxtYXRoYmZ7eH0pID0gM3hfMV4yICsgMnhfMl4yICsgNHhfMXhfMiQsIG9uZGUgJFxcbWF0aGJme3h9ID0gW3hfMSwgeF8yXV57XFx0b3B9JC4gQW8gZXNjcmV2ZXIgZXN0YSBmb3JtYSBuYSBub3Rhw6fDo28gbWF0cmljaWFsICRcXG1hdGhiZnt4fV57XFx0b3B9XFxtYXRoYmZ7QX1cXG1hdGhiZnt4fSQsIGlkZW50aWZpcXVlIGEgbWF0cml6ICRcXG1hdGhiZntBfSQgZSBzdWEgY2xhc3NpZmljYcOnw6NvLiIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJFxcbWF0aGJme0F9ID0gXFxiZWdpbntwbWF0cml4fSAzICYgMiBcXFxcIDIgJiAyIFxcZW5ke3BtYXRyaXh9JCwgUG9zaXRpdmEgRGVmaW5pZGEuIiwgIkIiOiAiJFxcbWF0aGJme0F9ID0gXFxiZWdpbntwbWF0cml4fSAzICYgNCBcXFxcIDQgJiAyIFxcZW5ke3BtYXRyaXh9JCwgSW5kZWZpbmlkYS4iLCAiQyI6ICIkXFxtYXRoYmZ7QX0gPSBcXGJlZ2lue3BtYXRyaXh9IDMgJiAyIFxcXFwgMiAmIDIgXFxlbmR7cG1hdHJpeH0kLCBJbmRlZmluaWRhLiIsICJEIjogIiRcXG1hdGhiZntBfSA9IFxcYmVnaW57cG1hdHJpeH0gMyAmIDEgXFxcXCAxICYgMiBcXGVuZHtwbWF0cml4fSQsIFBvc2l0aXZhIERlZmluaWRhLiIsICJFIjogIiRcXG1hdGhiZntBfSA9IFxcYmVnaW57cG1hdHJpeH0gNiAmIDQgXFxcXCA0ICYgNCBcXGVuZHtwbWF0cml4fSQsIFBvc2l0aXZhIERlZmluaWRhLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBwYXJhIGEgZm9ybWEgJFEoXFxtYXRoYmZ7eH0pID0gYV97MTF9eF8xXjIgKyBhX3syMn14XzJeMiArIDJhX3sxMn14XzF4XzIkLCBhIG1hdHJpeiBcXHNpbcOpdHJpY2Egw6kgZm9ybWFkYSBwb3IgJGFfezEyfSA9IGFfezIxfSA9IFxcZnJhY3tcXHRleHR7Y29lZmljaWVudGUgY3J1emFkb319ezJ9JC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBhcmEgYSBmb3JtYSAkM3hfMV4yICsgMnhfMl4yICsgNHhfMXhfMiQsIG9zIGNvZWZpY2llbnRlcyBkaWFnb25haXMgc8OjbyAkMyQgZSAkMiQuIE8gdGVybW8gY3J1emFkbyDDqSAkNHhfMXhfMiQsIGxvZ28gJGFfezEyfSA9IGFfezIxfSA9IDQvMiA9IDIkLiBBc3NpbSwgJFxcbWF0aGJme0F9ID0gXFxiZWdpbntwbWF0cml4fSAzICYgMiBcXFxcIDIgJiAyIFxcZW5ke3BtYXRyaXh9JC4gUGFyYSB2ZXJpZmljYXIgYSBkZWZpbmnDp8OjbywgY2FsY3VsYW1vcyBvcyBtZW5vcmVzIHByaW5jaXBhaXM6ICR8M3wgPSAzID4gMCQgZSAkfFxcbWF0aGJme0F9fCA9ICgzIFxcdGltZXMgMikgLSAoMiBcXHRpbWVzIDIpID0gNiAtIDQgPSAyID4gMCQuIENvbW8gYW1ib3Mgb3MgbWVub3JlcyBzw6NvIHBvc2l0aXZvcywgYSBtYXRyaXogw6kgUG9zaXRpdmEgRGVmaW5pZGEuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKGRhdGE9W2dvLlN1cmZhY2Uoej1bWzMqeCoqMiArIDIqeSoqMiArIDQqeCp5IGZvciB4IFxcaW4gbnAubGluc3BhY2UoLTIsMiwyMCldIGZvciB5IFxcaW4gbnAubGluc3BhY2UoLTIsMiwyMCldLCB4PW5wLmxpbnNwYWNlKC0yLDIsMjApLCB5PW5wLmxpbnNwYWNlKC0yLDIsMjApKV0pOyBmaWcudXBkYXRlX2xheW91dCh0aXRsZT0nU3VwZXJmw61jaWUgZGEgRm9ybWEgUXVhZHLDoXRpY2EnLCBzY2VuZT1kaWN0KHhheGlzX3RpdGxlPSd4XzEnLCB5YXhpc190aXRsZT0neF8yJywgemF4aXNfdGl0bGU9J1EoeCknKSkiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9XSwgInF1ZXN0b2VzX2Rpc2N1cnNpdmFzIjogW3siZW51bmNpYWRvIjogIkVtIHVtIGVuc2FpbyBjbMOtbmljbywgZm9yYW0gYXZhbGlhZG9zIDQgcGFjaWVudGVzLiBQYXJhIGNhZGEgcGFjaWVudGUsIHJlZ2lzdHJvdS1zZSBhIHByZXNzw6NvIGFydGVyaWFsIChtbUhnKSwgYSBmcmVxdcOqbmNpYSBjYXJkw61hY2EgKGJwbSkgZSBhIGRvc2FnZW0gZGUgdW0gbWVkaWNhbWVudG8gKG1nKS4gT3MgZGFkb3MgY29sZXRhZG9zIGZvcmFtOiBQYWNpZW50ZSAxICgxMjAsIDcwLCA1MCksIFBhY2llbnRlIDIgKDEzMCwgNzUsIDUwKSwgUGFjaWVudGUgMyAoMTI1LCA3MiwgNzUpIGUgUGFjaWVudGUgNCAoMTQwLCA4MCwgMTAwKS4gQ29uc3RydWEgYSBtYXRyaXogZGUgZGFkb3MgJFxcbWF0aGJme0F9X3soNCBcXHRpbWVzIDMpfSQgcmVwcmVzZW50YW5kbyBlc3NhcyBvYnNlcnZhw6fDtWVzLiIsICJkaWNhIjogIk9yZ2FuaXplIGNhZGEgcGFjaWVudGUgY29tbyB1bWEgbGluaGEgZGEgbWF0cml6IGUgY2FkYSB2YXJpw6F2ZWwgY29tbyB1bWEgY29sdW5hLCByZXNwZWl0YW5kbyBhIG9yZGVtIGFwcmVzZW50YWRhIG5vIGVudW5jaWFkby4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiSWRlbnRpZmljYW1vcyBvIG7Dum1lcm8gZGUgbGluaGFzICRuID0gNCQgKHBhY2llbnRlcykgZSBjb2x1bmFzICRtID0gMyQgKHZhcmnDoXZlaXMpLiIsICJBIG1hdHJpeiByZXN1bHRhbnRlIMOpIGRhZGEgcG9yICRcXG1hdGhiZntBfV97KDQgXFx0aW1lcyAzKX0gPSBcXGJlZ2lue3BtYXRyaXh9IGFfezExfSAmIGFfezEyfSAmIGFfezEzfSBcXFxcIGFfezIxfSAmIGFfezIyfSAmIGFfezIzfSBcXFxcIGFfezMxfSAmIGFfezMyfSAmIGFfezMzfSBcXFxcIGFfezQxfSAmIGFfezQyfSAmIGFfezQzfSBcXGVuZHtwbWF0cml4fSQuIiwgIlN1YnN0aXR1aW5kbyBwZWxvcyB2YWxvcmVzIGZvcm5lY2lkb3M6ICRcXG1hdGhiZntBfV97KDQgXFx0aW1lcyAzKX0gPSBcXGJlZ2lue3BtYXRyaXh9IDEyMCAmIDcwICYgNTAgXFxcXCAxMzAgJiA3NSAmIDUwIFxcXFwgMTI1ICYgNzIgJiA3NSBcXFxcIDE0MCAmIDgwICYgMTAwIFxcZW5ke3BtYXRyaXh9JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJBIHBhcnRpciBkYSBtYXRyaXogJFxcbWF0aGJme0F9JCBjb25zdHJ1w61kYSBuYSBxdWVzdMOjbyBhbnRlcmlvciwgZXh0cmFpYSBvIHZldG9yICRcXG1hdGhiZnthfV8xJCBjb3JyZXNwb25kZW50ZSDDoCBwcmltZWlyYSB2YXJpw6F2ZWwgKHByZXNzw6NvIGFydGVyaWFsKSBlIG8gdmV0b3IgJFxcbWF0aGJme2F9XzIkIGNvcnJlc3BvbmRlbnRlIMOgIHRlcmNlaXJhIHZhcmnDoXZlbCAoZG9zYWdlbSkuIFF1YWwgYSBkaW1lbnPDo28gZGUgY2FkYSB1bSBkZXNzZXMgdmV0b3Jlcz8iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlLCBwb3IgZGVmaW5pw6fDo28sIG8gdmV0b3IgY29sdW5hICRqJCBkYSBtYXRyaXogJFxcbWF0aGJme0F9X3sobiBcXHRpbWVzIG0pfSQgw6kgdW0gc3ViY29uanVudG8gZGEgbWF0cml6IGNvbSBkaW1lbnPDo28gJChuIFxcdGltZXMgMSkkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJPIHZldG9yIGNvbHVuYSAkXFxtYXRoYmZ7YX1fMSQgY29uc2lzdGUgbm9zIGVsZW1lbnRvcyBkYSBwcmltZWlyYSBjb2x1bmEgZGEgbWF0cml6OiAkXFxtYXRoYmZ7YX1fMSA9ICgxMjAsIDEzMCwgMTI1LCAxNDApXlQkLCBjb20gZGltZW5zw6NvICQoNCBcXHRpbWVzIDEpJC4iLCAiTyB2ZXRvciBjb2x1bmEgJFxcbWF0aGJme2F9XzIkIGNvbnNpc3RlIG5vcyBlbGVtZW50b3MgZGEgdGVyY2VpcmEgY29sdW5hIGRhIG1hdHJpejogJFxcbWF0aGJme2F9XzIgPSAoNTAsIDUwLCA3NSwgMTAwKV5UJCwgY29tIGRpbWVuc8OjbyAkKDQgXFx0aW1lcyAxKSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtIGNvbmp1bnRvIGRlIGRhZG9zIGRlIHByb2R1w6fDo28gaW5kdXN0cmlhbCByZXByZXNlbnRhZG8gcG9yIHVtYSBtYXRyaXogJFxcbWF0aGJme1B9X3sobiBcXHRpbWVzIG0pfSQuIFNlIGRlY2lkaXJtb3MgYWRpY2lvbmFyIHVtYSBub3ZhIHVuaWRhZGUgZXhwZXJpbWVudGFsICh1bWEgbm92YSBmw6FicmljYSwgc2VuZG8gJG4kIGF1bWVudGEgZW0gMSkgZSB1bWEgbm92YSBtw6l0cmljYSBkZSBkZXNlbXBlbmhvICh1bSBub3ZvIGluZGljYWRvciwgc2VuZG8gJG0kIGF1bWVudGEgZW0gMSksIHF1YWwgc2Vyw6EgYSBub3ZhIGRpbWVuc8OjbyBkYSBtYXRyaXogcmVzdWx0YW50ZT8gRXhwbGlxdWUgZm9ybWFsbWVudGUgY29tbyBvIGVsZW1lbnRvIGdlbsOpcmljbyAkcF97aWp9JCDDqSBhZmV0YWRvIHBlbGEgaW5jbHVzw6NvIGRhIG5vdmEgbGluaGEuIiwgImRpY2EiOiAiUGVuc2UgbmEgZXN0cnV0dXJhIG1hdHJpY2lhbCBjb21vIHVtIHNpc3RlbWEgZGUgY29vcmRlbmFkYXM6IGF1bWVudGFyIGxpbmhhcyBpbXBsaWNhIGFkaWNpb25hciBub3ZhcyBvYnNlcnZhw6fDtWVzLCBhdW1lbnRhciBjb2x1bmFzIGltcGxpY2Egbm92YXMgdmFyacOhdmVpcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSBkaW1lbnPDo28gb3JpZ2luYWwgw6kgJChuIFxcdGltZXMgbSkkLiIsICJBZGljaW9uYXIgdW1hIG9ic2VydmHDp8OjbyBhbHRlcmEgbyBuw7ptZXJvIGRlIGxpbmhhcyBwYXJhICQobisxKSQuIiwgIkFkaWNpb25hciB1bWEgdmFyacOhdmVsIGFsdGVyYSBvIG7Dum1lcm8gZGUgY29sdW5hcyBwYXJhICQobSsxKSQuIiwgIkEgbm92YSBkaW1lbnPDo28gw6kgJCgobisxKSBcXHRpbWVzIChtKzEpKSQuIiwgIk8gZWxlbWVudG8gZ2Vuw6lyaWNvICRwX3tpan0kIG1hbnTDqW0gc3VhIGRlZmluacOnw6NvLCBwb3LDqW0gbyDDrW5kaWNlIGRlIGxpbmhhIGFnb3JhIHBvZGUgYXNzdW1pciB2YWxvcmVzIGF0w6kgJG4rMSQgZSBvIMOtbmRpY2UgZGUgY29sdW5hIGF0w6kgJG0rMSQsIHBlcm1pdGluZG8gYSBpbnNlcsOnw6NvIGRvcyBub3ZvcyBkYWRvcyBub3Mgbm92b3MgZXNwYcOnb3MgY3JpYWRvcyBuYSBncmFkZSBtYXRyaWNpYWwuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZShkYXRhPVtnby5UYWJsZShoZWFkZXI9ZGljdCh2YWx1ZXM9WydNYXRyaXogT3JpZ2luYWwnLCAnTm92YSBNYXRyaXonXSksIGNlbGxzPWRpY3QodmFsdWVzPVtbJyhuIHggbSknLCAnLi4uJ10sIFsnKChuKzEpIHggKG0rMSkpJywgJy4uLiddXSkpXSk7IGZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdFdm9sdcOnw6NvIGRhIERpbWVuc8OjbyBNYXRyaWNpYWwnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkRhZGEgYSBtYXRyaXogZGUgdmFyacOibmNpYS1jb3ZhcmnDom5jaWEgZXN0aW1hZGEgZGUgdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gcGFyYSB0csOqcyB2YXJpw6F2ZWlzLCAkXFxtYXRoYmZ7XFxTaWdtYX1feygzKX0gPSBcXGJlZ2lue3BtYXRyaXh9IDQgJiAwICYgMCBcXFxcIDAgJiA5ICYgMCBcXFxcIDAgJiAwICYgMTYgXFxlbmR7cG1hdHJpeH0kLCBleHBsaXF1ZSBwb3IgcXVlIGVzdGEgbWF0cml6IMOpIGNsYXNzaWZpY2FkYSBjb21vIGRpYWdvbmFsIGUgcXVhbCDDqSBhIGltcGxpY2HDp8OjbyBlc3RhdMOtc3RpY2EgZGUgdGVyIGVsZW1lbnRvcyBudWxvcyBmb3JhIGRhIGRpYWdvbmFsIHByaW5jaXBhbC4iLCAiZGljYSI6ICJDb25zaWRlcmUgYSBkZWZpbmnDp8OjbyBkZSBtYXRyaXogZGlhZ29uYWwgb25kZSAkZF97aWp9ID0gMCQgcGFyYSAkaSBcXG5lcSBqJCBlIG8gc2lnbmlmaWNhZG8gZGEgY292YXJpw6JuY2lhIGVudHJlIHZhcmnDoXZlaXMuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIklkZW50aWZpY2HDp8OjbzogQSBtYXRyaXogJFxcbWF0aGJme1xcU2lnbWF9X3soMyl9JCDDqSBxdWFkcmFkYSAoJDMgXFx0aW1lcyAzJCkgZSB0b2RvcyBvcyBlbGVtZW50b3MgJHNfe2lqfSQgb25kZSAkaSBcXG5lcSBqJCBzw6NvIGlndWFpcyBhIDAuIFBvcnRhbnRvLCBhdGVuZGUgw6AgY29uZGnDp8OjbyBkZSBtYXRyaXogZGlhZ29uYWwuIiwgIk5vdGHDp8OjbzogUG9kZSBzZXIgZXNjcml0YSBjb21vICRcXG1hdGhiZntcXFNpZ21hfSA9IFxcdGV4dHtkaWFnfVxcezQsIDksIDE2XFx9JC4iLCAiSW1wbGljYcOnw6NvIGVzdGF0w61zdGljYTogRW0gZXN0YXTDrXN0aWNhLCBvcyBlbGVtZW50b3MgZm9yYSBkYSBkaWFnb25hbCBwcmluY2lwYWwgZGUgdW1hIG1hdHJpeiBkZSB2YXJpw6JuY2lhLWNvdmFyacOibmNpYSByZXByZXNlbnRhbSBhIGNvdmFyacOibmNpYSBlbnRyZSBhcyB2YXJpw6F2ZWlzLiBRdWFuZG8gJHNfe2lqfSA9IDAkIHBhcmEgJGkgXFxuZXEgaiQsIHNpZ25pZmljYSBxdWUgYSBjb3ZhcmnDom5jaWEgbGluZWFyIGVudHJlIGFzIHZhcmnDoXZlaXMgJGkkIGUgJGokIMOpIG51bGEsIGluZGljYW5kbyBhdXPDqm5jaWEgZGUgYXNzb2NpYcOnw6NvIGxpbmVhciBlbnRyZSBlbGFzLiIsICJDb25jbHVzw6NvOiBBIG1hdHJpeiBkaWFnb25hbCBuZXN0ZSBjb250ZXh0byBlc3RhdMOtc3RpY28gc2ltcGxpZmljYSBhIGFuw6FsaXNlLCBwb2lzIGltcGxpY2EgcXVlIGEgdmFyacOibmNpYSB0b3RhbCBkbyB2ZXRvciBkZSBkYWRvcyDDqSBhIHNvbWEgZGFzIHZhcmnDom5jaWFzIGluZGl2aWR1YWlzLCBzZW0gZWZlaXRvcyBkZSBpbnRlcmHDp8OjbyBsaW5lYXIuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTsOtdmVhIEJpc3BvLCBNQVRENDEgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzLCBBdWxhIDMsIHAuIDUiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gc2lzdGVtYSBkZSBlcXVhw6fDtWVzIGxpbmVhcmVzICRcXG1hdGhiZntUfV9TIFxcbWF0aGJme3h9ID0gXFxtYXRoYmZ7Yn0kIHV0aWxpemFkbyBuYSBkZWNvbXBvc2nDp8OjbyBkZSBDaG9sZXNreSwgb25kZSAkXFxtYXRoYmZ7VH1fUyA9IFxcYmVnaW57cG1hdHJpeH0gMiAmIDEgJiAzIFxcXFwgMCAmIDEgJiAyIFxcXFwgMCAmIDAgJiA0IFxcZW5ke3BtYXRyaXh9JC4gUG9yIHF1ZSBhIGVzdHJ1dHVyYSBkZXN0YSBtYXRyaXogKHRyaWFuZ3VsYXIgc3VwZXJpb3IpIGZhY2lsaXRhIGNvbXB1dGFjaW9uYWxtZW50ZSBhIHNvbHXDp8OjbyBkbyBzaXN0ZW1hICRcXG1hdGhiZnt4fSQgY29tcGFyYWRhIGEgdW1hIG1hdHJpeiBnZW7DqXJpY2E/IiwgImRpY2EiOiAiUGVuc2Ugbm8gbcOpdG9kbyBkZSBzdWJzdGl0dWnDp8OjbyByZWdyZXNzaXZhIChiYWNrIHN1YnN0aXR1dGlvbikgYXBsaWNhZG8gYSBzaXN0ZW1hcyB0cmlhbmd1bGFyZXMuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkVzdHJ1dHVyYTogJFxcbWF0aGJme1R9X1MkIMOpIHVtYSBtYXRyaXogdHJpYW5ndWxhciBzdXBlcmlvciwgcG9pcyAkdF97aWp9ID0gMCQgcGFyYSAkaSA+IGokLiIsICJSZXNvbHXDp8OjbzogTyBzaXN0ZW1hIHBvZGUgc2VyIHJlc29sdmlkbyBpbmljaWFuZG8gcGVsYSDDumx0aW1hIGxpbmhhOiAkNHhfMyA9IGJfMyBcXFJpZ2h0YXJyb3cgeF8zID0gYl8zIC8gNCQuIiwgIlN1YnN0aXR1acOnw6NvOiBDb20gJHhfMyQgY29uaGVjaWRvLCBhIHNlZ3VuZGEgbGluaGEgJDF4XzIgKyAyeF8zID0gYl8yJCBwZXJtaXRlIGlzb2xhciAkeF8yJCBkaXJldGFtZW50ZS4iLCAiRWZpY2nDqm5jaWE6IEVzdGEgdMOpY25pY2EsIGNvbmhlY2lkYSBjb21vIHN1YnN0aXR1acOnw6NvIHJlZ3Jlc3NpdmEsIGV2aXRhIGEgbmVjZXNzaWRhZGUgZGUgZWxpbWluYcOnw6NvIGNvbXBsZXRhIGRlIEdhdXNzIG91IGludmVyc8OjbyBtYXRyaWNpYWwsIHJlZHV6aW5kbyBkcmFzdGljYW1lbnRlIG8gbsO6bWVybyBkZSBvcGVyYcOnw7VlcyBhcml0bcOpdGljYXMgKGZsb3BzKSBlIGdhcmFudGluZG8gbWFpb3IgZXN0YWJpbGlkYWRlIG51bcOpcmljYS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJOw612ZWEgQmlzcG8sIE1BVEQ0MSBJbnRyb2R1w6fDo28gYW9zIE1vZGVsb3MgTGluZWFyZXMsIEF1bGEgMywgcC4gNiIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbWEgbWF0cml6ICRcXG1hdGhiZntBfV97KDMpfSQgw6kgZGVmaW5pZGEgY29tbyAkXFxtYXRoYmZ7QX0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAyICYgMyBcXFxcIDQgJiA1ICYgNiBcXFxcIDcgJiA4ICYgOSBcXGVuZHtwbWF0cml4fSQuIEVsYSDDqSB1bWEgbWF0cml6IGRpYWdvbmFsLCB0cmlhbmd1bGFyIG91IGlkZW50aWRhZGU/IEp1c3RpZmlxdWUgc3VhIHJlc3Bvc3RhIG1hdGVtYXRpY2FtZW50ZSBjb20gYmFzZSBuYSB0aXBvbG9naWEgZnVuZGFtZW50YWwgZXN0dWRhZGEuIiwgImRpY2EiOiAiVmVyaWZpcXVlIGFzIGNvbmRpw6fDtWVzICRpPWokLCAkaSA+IGokIGUgJGkgPCBqJCBwYXJhIG9zIGVsZW1lbnRvcyBkYSBtYXRyaXouIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkFuw6FsaXNlIGRvcyBlbGVtZW50b3MgZm9yYSBkYSBkaWFnb25hbCBwcmluY2lwYWw6IFBhcmEgc2VyIGRpYWdvbmFsLCBwcmVjaXNhcsOtYW1vcyBxdWUgJGFfe2lqfSA9IDAkIHBhcmEgdG9kbyAkaSBcXG5lcSBqJC4gQXF1aSwgdGVtb3MgJGFfezEyfSA9IDIgXFxuZXEgMCQsIGxvZ28gbsOjbyDDqSBkaWFnb25hbC4iLCAiQW7DoWxpc2UgZGUgdHJpYW5ndWxhcmlkYWRlOiBQYXJhIHNlciBUcmlhbmd1bGFyIFN1cGVyaW9yLCBwcmVjaXNhcsOtYW1vcyBxdWUgJGFfe2lqfSA9IDAkIHBhcmEgJGkgPiBqJCAoZWxlbWVudG9zIGFiYWl4byBkYSBkaWFnb25hbCkuIFRlbW9zICRhX3syMX0gPSA0IFxcbmVxIDAkLCBsb2dvIG7Do28gw6kgdHJpYW5ndWxhciBzdXBlcmlvci4iLCAiQW7DoWxpc2UgZGUgdHJpYW5ndWxhcmlkYWRlOiBQYXJhIHNlciBUcmlhbmd1bGFyIEluZmVyaW9yLCBwcmVjaXNhcsOtYW1vcyBxdWUgJGFfe2lqfSA9IDAkIHBhcmEgJGkgPCBqJCAoZWxlbWVudG9zIGFjaW1hIGRhIGRpYWdvbmFsKS4gVGVtb3MgJGFfezEyfSA9IDIgXFxuZXEgMCQsIGxvZ28gbsOjbyDDqSB0cmlhbmd1bGFyIGluZmVyaW9yLiIsICJDb25jbHVzw6NvOiBBIG1hdHJpeiAkXFxtYXRoYmZ7QX0kIMOpIGFwZW5hcyB1bWEgbWF0cml6IHF1YWRyYWRhIGRlIGRpbWVuc8OjbyAzIGUgbsOjbyBzZSBlbnF1YWRyYSBuYXMgdGlwb2xvZ2lhcyBlc3BlY2lhaXMgKGRpYWdvbmFsIG91IHRyaWFuZ3VsYXIpLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEgJiBFc3RldmVzLCBUw7NwaWNvcyBkZSBNYXRyaXplcywgQ2FwIDEsIHAuIDExIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlNlamFtICRcXG1hdGhiZntBfSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDIgXFxcXCAzICYgNCBcXGVuZHtwbWF0cml4fSQgZSAkXFxtYXRoYmZ7Qn0gPSBcXGJlZ2lue3BtYXRyaXh9IDAgJiAxIFxcXFwgMSAmIDAgXFxlbmR7cG1hdHJpeH0kLiBWZXJpZmlxdWUgbnVtZXJpY2FtZW50ZSBhIHByb3ByaWVkYWRlIGRhIHRyYW5zcG9zdGEgZG8gcHJvZHV0bzogJChcXG1hdGhiZntBfVxcbWF0aGJme0J9KV57XFx0b3B9ID0gXFxtYXRoYmZ7Qn1ee1xcdG9wfVxcbWF0aGJme0F9XntcXHRvcH0kLiIsICJkaWNhIjogIkNhbGN1bGUgcHJpbWVpcm8gbyBwcm9kdXRvICRcXG1hdGhiZntBfVxcbWF0aGJme0J9JCwgZGVwb2lzIHRyYW5zcG9uaGEuIEVtIHNlZ3VpZGEsIGNhbGN1bGUgYXMgdHJhbnNwb3N0YXMgc2VwYXJhZGFtZW50ZSwgbXVsdGlwbGlxdWUtYXMgbmEgb3JkZW0gY29ycmV0YSBlIGNvbXBhcmUgb3MgcmVzdWx0YWRvcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogQ2FsY3VsYXIgbyBwcm9kdXRvICRcXG1hdGhiZntBfVxcbWF0aGJme0J9ID0gXFxiZWdpbntwbWF0cml4fSAxICYgMiBcXFxcIDMgJiA0IFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMCAmIDEgXFxcXCAxICYgMCBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMSgwKSsyKDEpICYgMSgxKSsyKDApIFxcXFwgMygwKSs0KDEpICYgMygxKSs0KDApIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAyICYgMSBcXFxcIDQgJiAzIFxcZW5ke3BtYXRyaXh9JC4iLCAiUGFzc28gMjogVHJhbnNwb3IgbyBwcm9kdXRvICQoXFxtYXRoYmZ7QX1cXG1hdGhiZntCfSlee1xcdG9wfSA9IFxcYmVnaW57cG1hdHJpeH0gMiAmIDQgXFxcXCAxICYgMyBcXGVuZHtwbWF0cml4fSQuIiwgIlBhc3NvIDM6IENhbGN1bGFyICRcXG1hdGhiZntCfV57XFx0b3B9ID0gXFxiZWdpbntwbWF0cml4fSAwICYgMSBcXFxcIDEgJiAwIFxcZW5ke3BtYXRyaXh9JCBlICRcXG1hdGhiZntBfV57XFx0b3B9ID0gXFxiZWdpbntwbWF0cml4fSAxICYgMyBcXFxcIDIgJiA0IFxcZW5ke3BtYXRyaXh9JC4iLCAiUGFzc28gNDogQ2FsY3VsYXIgbyBwcm9kdXRvICRcXG1hdGhiZntCfV57XFx0b3B9XFxtYXRoYmZ7QX1ee1xcdG9wfSA9IFxcYmVnaW57cG1hdHJpeH0gMCAmIDEgXFxcXCAxICYgMCBcXGVuZHtwbWF0cml4fSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAzIFxcXFwgMiAmIDQgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDAoMSkrMSgyKSAmIDAoMykrMSg0KSBcXFxcIDEoMSkrMCgyKSAmIDEoMykrMCg0KSBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMiAmIDQgXFxcXCAxICYgMyBcXGVuZHtwbWF0cml4fSQuIiwgIkNvbmNsdXPDo286IENvbW8gJFxcYmVnaW57cG1hdHJpeH0gMiAmIDQgXFxcXCAxICYgMyBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMiAmIDQgXFxcXCAxICYgMyBcXGVuZHtwbWF0cml4fSQsIGEgcHJvcHJpZWRhZGUgZXN0w6EgdmVyaWZpY2FkYS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgKEluc3BpcmFkbyBub3MgZXhlcmPDrWNpb3MgZGUgw6FsZ2VicmEgbWF0cmljaWFsIGRvIENhcCAxKSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSBtb2RlbG9zIGVzdGF0w61zdGljb3MsIGEgbWF0cml6IGRlIHZhcmnDom5jaWEtY292YXJpw6JuY2lhICRcXFNpZ21hJCBkZXZlIHNlciBcXHNpbcOpdHJpY2EuIERhZGEgYSBtYXRyaXogJFxcU2lnbWEgPSBcXGJlZ2lue3BtYXRyaXh9IDQgJiAyIFxcXFwgMiAmIDkgXFxlbmR7cG1hdHJpeH0kLCBjYWxjdWxlIGEgZm9ybWEgcXVhZHLDoXRpY2EgJFEoeCkgPSB4XntcXHRvcH1cXFNpZ21hIHgkIHBhcmEgbyB2ZXRvciAkeCA9IFxcYmVnaW57cG1hdHJpeH0gMSBcXFxcIC0xIFxcZW5ke3BtYXRyaXh9JC4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlICR4XntcXHRvcH1cXFNpZ21hIHggPSAoeF8xLCB4XzIpIFxcYmVnaW57cG1hdHJpeH0gXFxzaWdtYV97MTF9ICYgXFxzaWdtYV97MTJ9IFxcXFwgXFxzaWdtYV97MjF9ICYgXFxzaWdtYV97MjJ9IFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0geF8xIFxcXFwgeF8yIFxcZW5ke3BtYXRyaXh9JC4gU2lnYSBhIG9yZGVtIGRhIG11bHRpcGxpY2HDp8OjbzogdmV0b3IgbGluaGEgJFxcdGltZXMkIG1hdHJpeiAkXFx0aW1lcyQgdmV0b3IgY29sdW5hLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiBEZWZpbmlyIGEgb3BlcmHDp8OjbyAkeF57XFx0b3B9XFxTaWdtYSB4ID0gXFxiZWdpbntwbWF0cml4fSAxICYgLTEgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSA0ICYgMiBcXFxcIDIgJiA5IFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMSBcXFxcIC0xIFxcZW5ke3BtYXRyaXh9JC4iLCAiUGFzc28gMjogTXVsdGlwbGljYXIgbyB2ZXRvciBsaW5oYSBwZWxhIG1hdHJpejogJFxcYmVnaW57cG1hdHJpeH0gMSAmIC0xIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gNCAmIDIgXFxcXCAyICYgOSBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMSg0KSsoLTEpKDIpICYgMSgyKSsoLTEpKDkpIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAyICYgLTcgXFxlbmR7cG1hdHJpeH0kLiIsICJQYXNzbyAzOiBNdWx0aXBsaWNhciBvIHJlc3VsdGFkbyBwZWxvIHZldG9yIGNvbHVuYTogJFxcYmVnaW57cG1hdHJpeH0gMiAmIC03IFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMSBcXFxcIC0xIFxcZW5ke3BtYXRyaXh9ID0gMigxKSArICgtNykoLTEpID0gMiArIDcgPSA5JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDkuMH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBhIG1hdHJpeiBkZSBkYWRvcyAkXFxtYXRoYmZ7WH1feyhuIFxcdGltZXMgMil9JCByZXByZXNlbnRhbmRvIG9ic2VydmHDp8O1ZXMgZGUgZHVhcyB2YXJpw6F2ZWlzIGVtICRuPTMkIGluZGl2w61kdW9zOiAkXFxtYXRoYmZ7WH0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAyIFxcXFwgMSAmIDQgXFxcXCAxICYgNiBcXGVuZHtwbWF0cml4fSQuIENhbGN1bGUgYSBtYXRyaXogZGUgcHJvZHV0byAkXFxtYXRoYmZ7QX0gPSBcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0kIGUgdmVyaWZpcXVlIHNlIGVsYSDDqSBcXHNpbcOpdHJpY2EuIiwgImRpY2EiOiAiQSB0cmFuc3Bvc3RhIGRlICRcXG1hdGhiZntYfSQgc2Vyw6EgdW1hIG1hdHJpeiAkKDIgXFx0aW1lcyAzKSQuIE8gcHJvZHV0byAkXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9JCByZXN1bHRhcsOhIGVtIHVtYSBtYXRyaXogcXVhZHJhZGEgJCgyIFxcdGltZXMgMikkLiBBIHNpbWV0cmlhIMOpIHVtYSBwcm9wcmllZGFkZSBnYXJhbnRpZGEgcGFyYSBwcm9kdXRvcyBkYSBmb3JtYSAkXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogVHJhbnNwb3IgYSBtYXRyaXogJFxcbWF0aGJme1h9JDogJFxcbWF0aGJme1h9XntcXHRvcH0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxICYgMSBcXFxcIDIgJiA0ICYgNiBcXGVuZHtwbWF0cml4fSQuIiwgIlBhc3NvIDI6IENhbGN1bGFyIG8gcHJvZHV0byAkXFxtYXRoYmZ7QX0gPSBcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxICYgMSBcXFxcIDIgJiA0ICYgNiBcXGVuZHtwbWF0cml4fSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAyIFxcXFwgMSAmIDQgXFxcXCAxICYgNiBcXGVuZHtwbWF0cml4fSQuIiwgIlBhc3NvIDM6IFJlYWxpemFyIGEgbXVsdGlwbGljYcOnw6NvIGVsZW1lbnRvIGEgZWxlbWVudG86ICRhX3sxMX0gPSAoMSkoMSkrKDEpKDEpKygxKSgxKSA9IDMkOyAkYV97MTJ9ID0gKDEpKDIpKygxKSg0KSsoMSkoNikgPSAxMiQ7ICRhX3syMX0gPSAoMikoMSkrKDQpKDEpKyg2KSgxKSA9IDEyJDsgJGFfezIyfSA9ICgyKSgyKSsoNCkoNCkrKDYpKDYpID0gNCsxNiszNiA9IDU2JC4iLCAiUGFzc28gNDogTWF0cml6IHJlc3VsdGFudGUgJFxcbWF0aGJme0F9ID0gXFxiZWdpbntwbWF0cml4fSAzICYgMTIgXFxcXCAxMiAmIDU2IFxcZW5ke3BtYXRyaXh9JC4iLCAiQ29uY2x1c8OjbzogQ29tbyAkYV97MTJ9ID0gYV97MjF9ID0gMTIkLCBhIG1hdHJpeiAkXFxtYXRoYmZ7QX0kIMOpIFxcc2ltw6l0cmljYS4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKGRhdGE9Z28uSGVhdG1hcCh6PVtbMywgMTJdLCBbMTIsIDU2XV0sIHg9WydDb2x1bmEgMScsICdDb2x1bmEgMiddLCB5PVsnTGluaGEgMScsICdMaW5oYSAyJ10sIGNvbG9yc2NhbGU9J0JsdWVzJykpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nTWF0cml6IFNpbcOpdHJpY2EgJFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSQnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzLCBFeCAxLjgiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIHByb2R1dGl2aWRhZGUgYWdyw61jb2xhLCBkb2lzIGluc3Vtb3MgKGZlcnRpbGl6YW50ZSBlIGlycmlnYcOnw6NvKSBzw6NvIG1lZGlkb3MgZW0gMyB1bmlkYWRlcyBleHBlcmltZW50YWlzLCBnZXJhbmRvIG9zIHZldG9yZXMgJFxcbWF0aGJme3V9ID0gWzIsIDEsIDJdXntcXHRvcH0kIGUgJFxcbWF0aGJme3Z9ID0gWzEsIDIsIDBdXntcXHRvcH0kLiBDYWxjdWxlIG8gcHJvZHV0byBpbnRlcm5vICRcXGxhbmdsZSBcXG1hdGhiZnt1fSwgXFxtYXRoYmZ7dn0gXFxyYW5nbGUkIGUgYXMgbm9ybWFzIGV1Y2xpZGlhbmFzIGRvcyB2ZXRvcmVzICRcXHxcXG1hdGhiZnt1fVxcfCQgZSAkXFx8XFxtYXRoYmZ7dn1cXHwkLiIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBmw7NybXVsYSBkYSBub3JtYTogJFxcfFxcbWF0aGJme3h9XFx8ID0gXFxzcXJ0e1xcc3VtX3tpPTF9XntufSB4X2leMn0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiBDYWxjdWxhciBvIHByb2R1dG8gaW50ZXJubyAkXFxsYW5nbGUgXFxtYXRoYmZ7dX0sIFxcbWF0aGJme3Z9IFxccmFuZ2xlID0gKDIgXFx0aW1lcyAxKSArICgxIFxcdGltZXMgMikgKyAoMiBcXHRpbWVzIDApID0gMiArIDIgKyAwID0gNCQuIiwgIlBhc3NvIDI6IENhbGN1bGFyIGEgbm9ybWEgZGUgJFxcbWF0aGJme3V9JDogJFxcfFxcbWF0aGJme3V9XFx8ID0gXFxzcXJ0ezJeMiArIDFeMiArIDJeMn0gPSBcXHNxcnR7NCArIDEgKyA0fSA9IFxcc3FydHs5fSA9IDMkLiIsICJQYXNzbyAzOiBDYWxjdWxhciBhIG5vcm1hIGRlICRcXG1hdGhiZnt2fSQ6ICRcXHxcXG1hdGhiZnt2fVxcfCA9IFxcc3FydHsxXjIgKyAyXjIgKyAwXjJ9ID0gXFxzcXJ0ezEgKyA0ICsgMH0gPSBcXHNxcnR7NX0gXFxhcHByb3ggMi4yMzYkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogNC4wfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gdmV0b3IgJFxcbWF0aGJme2F9ID0gWzMsIC00XV57XFx0b3B9JC4gRGV0ZXJtaW5lIHVtIHZldG9yICRcXG1hdGhiZntifSQgbsOjbyBudWxvIHRhbCBxdWUgJFxcbWF0aGJme2F9JCBlICRcXG1hdGhiZntifSQgc2VqYW0gb3J0b2dvbmFpcy4gVmVyaWZpcXVlIHN1YSByZXNwb3N0YSBjYWxjdWxhbmRvIG8gcHJvZHV0byBpbnRlcm5vLiIsICJkaWNhIjogIlNlICRcXG1hdGhiZnthfSA9IFt4LCB5XV57XFx0b3B9JCwgdW0gdmV0b3Igb3J0b2dvbmFsIGEgZWxlIGVtICRcXG1hdGhiYntSfV4yJCBwb2RlIHNlciBvYnRpZG8gdHJvY2FuZG8gYXMgY29vcmRlbmFkYXMgZSBpbnZlcnRlbmRvIG8gc2luYWwgZGUgdW1hIGRlbGFzLCBjb21vICRbLXksIHhdXntcXHRvcH0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiBQYXJhICRcXG1hdGhiZnthfSA9IFszLCAtNF1ee1xcdG9wfSQsIGJ1c2NhbW9zICRcXG1hdGhiZntifSA9IFtiXzEsIGJfMl1ee1xcdG9wfSQgdGFsIHF1ZSAkM2JfMSAtIDRiXzIgPSAwJC4iLCAiUGFzc28gMjogVW1hIHNvbHXDp8OjbyBzaW1wbGVzIMOpIGVzY29saGVyICRiXzEgPSA0JCBlICRiXzIgPSAzJCwgcmVzdWx0YW5kbyBlbSAkXFxtYXRoYmZ7Yn0gPSBbNCwgM11ee1xcdG9wfSQuIiwgIlBhc3NvIDM6IFZlcmlmaWNhw6fDo286ICRcXGxhbmdsZSBcXG1hdGhiZnthfSwgXFxtYXRoYmZ7Yn0gXFxyYW5nbGUgPSAoMyBcXHRpbWVzIDQpICsgKC00IFxcdGltZXMgMykgPSAxMiAtIDEyID0gMCQuIFBvcnRhbnRvLCBvcyB2ZXRvcmVzIHPDo28gb3J0b2dvbmFpcy4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVswLCAzXSwgeT1bMCwgLTRdLCBtb2RlPSdsaW5lcycsIG5hbWU9cickXFxtYXRoYmZ7YX0kJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJykpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9WzAsIDRdLCB5PVswLCAzXSwgbW9kZT0nbGluZXMnLCBuYW1lPXInJFxcbWF0aGJme2J9JCcsIGxpbmU9ZGljdChjb2xvcj0nIzEwQjk4MScpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdPcnRvZ29uYWxpZGFkZSBlbSAyRCcsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4wfSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIHNvYiBhIMOzdGljYSBkYSBlc3RhdMOtc3RpY2EgY29tcHV0YWNpb25hbCBlIG1vZGVsb3MgZGUgcmVncmVzc8OjbywgcG9yIHF1ZSBhIG9ydG9nb25hbGlkYWRlIGVudHJlIHZhcmnDoXZlaXMgZXhwbGljYXRpdmFzICh2ZXRvcmVzIGNvbHVuYXMgZGUgdW1hIG1hdHJpeiAkXFxtYXRoYmZ7WH0kKSBzaW1wbGlmaWNhIGEgZXN0aW1hw6fDo28gZG9zIGNvZWZpY2llbnRlcyAkXFxoYXR7XFxiZXRhfV8xJC4iLCAiZGljYSI6ICJDb25zaWRlcmUgYSBtYXRyaXogJFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSQuIE8gcXVlIGFjb250ZWNlIGNvbSBlc3NhIG1hdHJpeiBzZSB0b2RhcyBhcyBzdWFzIGNvbHVuYXMgZm9yZW0gb3J0b2dvbmFpcyBlbnRyZSBzaT8iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogTm8gbW9kZWxvIGRlIHJlZ3Jlc3PDo28sIG9zIGVzdGltYWRvcmVzIGRlIG3DrW5pbW9zIHF1YWRyYWRvcyBzw6NvIGRhZG9zIHBvciAkXFxoYXR7XFxiZXRhfSA9IChcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0pXnstMX1cXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7eX0kLiIsICJQYXNzbyAyOiBTZSBvcyB2ZXRvcmVzIGNvbHVuYXMgZGUgJFxcbWF0aGJme1h9JCBzw6NvIG9ydG9nb25haXMsIG8gcHJvZHV0byAkXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9JCByZXN1bHRhIGVtIHVtYSBtYXRyaXogZGlhZ29uYWwuIiwgIlBhc3NvIDM6IEEgaW52ZXJzw6NvIGRlIHVtYSBtYXRyaXogZGlhZ29uYWwgw6kgdHJpdmlhbCAoaW52ZXJ0ZS1zZSBhcGVuYXMgb3MgZWxlbWVudG9zIGRhIGRpYWdvbmFsKSwgZWxpbWluYW5kbyBhIGNvbXBsZXhpZGFkZSBkZSBzaXN0ZW1hcyBkZSBlcXVhw6fDtWVzIGxpbmVhcmVzIGFjb3BsYWRvcyBlIGV2aXRhbmRvIGluc3RhYmlsaWRhZGVzIG51bcOpcmljYXMgY29uaGVjaWRhcyBjb21vIG11bHRpY29saW5lYXJpZGFkZS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJTZWphIGEgZm9ybWEgcXVhZHLDoXRpY2EgJFEoXFxtYXRoYmZ7eH0pID0gMnhfMV4yICsgeF8yXjIgKyAyeF8zXjIgKyAyeF8xeF8yJC4gUmVwcmVzZW50ZSBlc3RhIGZvcm1hIG1hdHJpY2lhbG1lbnRlIG5hIGZvcm1hICRRKFxcbWF0aGJme3h9KSA9IFxcbWF0aGJme3h9XntcXHRvcH1cXG1hdGhiZntBfVxcbWF0aGJme3h9JCBjb20gJFxcbWF0aGJme0F9JCBcXHNpbcOpdHJpY2EgZSBkZXRlcm1pbmUgc2UgZWxhIMOpIFBvc2l0aXZhIERlZmluaWRhIGNhbGN1bGFuZG8gb3MgbWVub3JlcyBwcmluY2lwYWlzLiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgZW0gdW1hIG1hdHJpeiAkMyBcXHRpbWVzIDMkLCBvcyBlbGVtZW50b3MgJGFfe2lqfSQgc2VndWVtIGEgZXN0cnV0dXJhIGRvcyBjb2VmaWNpZW50ZXMgZGFzIHZhcmnDoXZlaXMgJHhfaSB4X2okLiBBIG1hdHJpeiDDqSBQb3NpdGl2YSBEZWZpbmlkYSBzZSB0b2RvcyBvcyBzZXVzIG1lbm9yZXMgcHJpbmNpcGFpcyBkb21pbmFudGVzIGZvcmVtIHBvc2l0aXZvcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiSWRlbnRpZmljYcOnw6NvIGRvcyBjb2VmaWNpZW50ZXM6ICRRKFxcbWF0aGJme3h9KSA9IDJ4XzFeMiArIDF4XzJeMiArIDJ4XzNeMiArIDJ4XzF4XzIgKyAweF8xeF8zICsgMHhfMnhfMyQuIiwgIkNvbnN0cnXDp8OjbyBkYSBtYXRyaXogXFxzaW3DqXRyaWNhICRcXG1hdGhiZntBfSA9IFxcYmVnaW57cG1hdHJpeH0gMiAmIDEgJiAwIFxcXFwgMSAmIDEgJiAwIFxcXFwgMCAmIDAgJiAyIFxcZW5ke3BtYXRyaXh9JC4iLCAiTWVub3IgcHJpbmNpcGFsIGRlIG9yZGVtIDE6ICR8MnwgPSAyID4gMCQuIiwgIk1lbm9yIHByaW5jaXBhbCBkZSBvcmRlbSAyOiAkfFxcYmVnaW57cG1hdHJpeH0gMiAmIDEgXFxcXCAxICYgMSBcXGVuZHtwbWF0cml4fXwgPSAyIC0gMSA9IDEgPiAwJC4iLCAiTWVub3IgcHJpbmNpcGFsIGRlIG9yZGVtIDMgKGRldGVybWluYW50ZSBkZSBBKTogJDIgXFx0aW1lcyAoMiAtIDApIC0gMSBcXHRpbWVzICgyIC0gMCkgKyAwID0gNCAtIDIgPSAyID4gMCQuIiwgIkNvbmNsdXPDo286IENvbW8gdG9kb3Mgb3MgbWVub3JlcyBwcmluY2lwYWlzICgkMiwgMSwgMiQpIHPDo28gZXN0cml0YW1lbnRlIHBvc2l0aXZvcywgYSBtYXRyaXogw6kgUG9zaXRpdmEgRGVmaW5pZGEuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gc2lzdGVtYSBkZSB2YXJpw6JuY2lhIGRlIHVtIHByb2Nlc3NvIGluZHVzdHJpYWwgZGUgbWFudWZhdHVyYSBkYWRvIHBvciAkXFxtYXRoYmZ7QX0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAtMSBcXFxcIC0xICYgMSBcXGVuZHtwbWF0cml4fSQuIEFwbGlxdWUgYSBkZWZpbmnDp8OjbyBkZSBmb3JtYSBxdWFkcsOhdGljYSBwYXJhIGRldGVybWluYXIgYSBjbGFzc2lmaWNhw6fDo28gZGVzdGEgbWF0cml6LiIsICJkaWNhIjogIkNhbGN1bGUgJFEoXFxtYXRoYmZ7eH0pID0gXFxtYXRoYmZ7eH1ee1xcdG9wfVxcbWF0aGJme0F9XFxtYXRoYmZ7eH0kIHBhcmEgdW0gdmV0b3IgZ2Vuw6lyaWNvICRcXG1hdGhiZnt4fSA9IFt4XzEsIHhfMl1ee1xcdG9wfSQgZSB2ZXJpZmlxdWUgc2UgZXhpc3RlICRcXG1hdGhiZnt4fSBcXG5lcSBcXG1hdGhiZnswfSQgdGFsIHF1ZSAkUShcXG1hdGhiZnt4fSkgPSAwJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRXhwYW5zw6NvOiAkUSh4XzEsIHhfMikgPSBbeF8xLCB4XzJdIFxcYmVnaW57cG1hdHJpeH0gMSAmIC0xIFxcXFwgLTEgJiAxIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0geF8xIFxcXFwgeF8yIFxcZW5ke3BtYXRyaXh9JC4iLCAiQ8OhbGN1bG8gYWxnw6licmljbzogJFEoeF8xLCB4XzIpID0geF8xKDF4XzEgLSAxeF8yKSArIHhfMigtMXhfMSArIDF4XzIpID0geF8xXjIgLSAyeF8xeF8yICsgeF8yXjIkLiIsICJGYXRvcmHDp8OjbzogJFEoeF8xLCB4XzIpID0gKHhfMSAtIHhfMileMiQuIiwgIkFuw6FsaXNlOiAkKHhfMSAtIHhfMileMiBcXGdlIDAkIHBhcmEgcXVhaXNxdWVyICR4XzEsIHhfMiQuIiwgIlZlcmlmaWNhw6fDo28gZGUgbnVsaWRhZGU6IFNlICR4XzEgPSB4XzIgPSAxJCwgdGVtb3MgJFxcbWF0aGJme3h9ID0gWzEsIDFdXntcXHRvcH0gXFxuZXEgXFxtYXRoYmZ7MH0kLCBtYXMgJFEoMSwgMSkgPSAoMSAtIDEpXjIgPSAwJC4iLCAiQ29uY2x1c8OjbzogQSBtYXRyaXogw6kgU2VtaSBQb3NpdGl2YSBEZWZpbmlkYS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBtb2RlbG8gZWNvbm9tw6l0cmljbyBkZSBjb25zdW1vLCBhIGZvcm1hIHF1YWRyw6F0aWNhIGRvIGVycm8gw6kgZGFkYSBwb3IgJFEoeF8xLCB4XzIpID0gLXhfMV4yIC0gM3hfMl4yJC4gRW5jb250cmUgYSBtYXRyaXogJFxcbWF0aGJme0F9JCBhc3NvY2lhZGEgZSBkaXNjdXRhIHN1YSBjbGFzc2lmaWNhw6fDo28gYmFzZWFkYSBuYSBkZWZpbmnDp8OjbyBmb3JtYWwgZGUgZm9ybWFzIGRlZmluaWRhcy4iLCAiZGljYSI6ICJDb21wYXJlIGNvbSBhIGZvcm1hIGdlcmFsICRcXG1hdGhiZnt4fV57XFx0b3B9XFxtYXRoYmZ7QX1cXG1hdGhiZnt4fSA9IGFfezExfXhfMV4yICsgYV97MjJ9eF8yXjIgKyAyYV97MTJ9eF8xeF8yJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiSWRlbnRpZmljYcOnw6NvOiAkYV97MTF9ID0gLTEkLCAkYV97MjJ9ID0gLTMkLCAkYV97MTJ9ID0gMCQuIExvZ28sICRcXG1hdGhiZntBfSA9IFxcYmVnaW57cG1hdHJpeH0gLTEgJiAwIFxcXFwgMCAmIC0zIFxcZW5ke3BtYXRyaXh9JC4iLCAiRGVmaW5pw6fDo28gZGUgc2luYWw6ICRRKFxcbWF0aGJme3h9KSA9IC14XzFeMiAtIDN4XzJeMiQuIiwgIlBhcmEgcXVhbHF1ZXIgJFxcbWF0aGJme3h9IFxcbmVxIFxcbWF0aGJmezB9JCwgJHhfMV4yJCBlICR4XzJeMiQgc8OjbyBuw6NvIG5lZ2F0aXZvcywgc2VuZG8gcGVsbyBtZW5vcyB1bSBkZWxlcyBlc3RyaXRhbWVudGUgcG9zaXRpdm8uIiwgIkNvbnNlcXVlbnRlbWVudGUsICRRKFxcbWF0aGJme3h9KSA9IC0oeF8xXjIgKyAzeF8yXjIpIDwgMCQgcGFyYSB0b2RvICRcXG1hdGhiZnt4fSBcXG5lcSBcXG1hdGhiZnswfSQuIiwgIkNsYXNzaWZpY2HDp8OjbzogUGVsYSBkZWZpbmnDp8OjbywgYSBmb3JtYSBxdWFkcsOhdGljYSDDqSBOZWdhdGl2YSBEZWZpbmlkYS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9XX0=').decode('utf-8'))


    # Inicialização do progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do total de exercícios
    mcq_list = dados_exercicios.get("questoes_multipla_escolha", [])
    disc_list = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcq_list) + len(disc_list)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    # Barra de progresso
    if total_exercicios > 0:
        st.progress(min(1.0, acertos / total_exercicios))
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    
    st.divider()
    
    # Processamento de Questões de Múltipla Escolha
    if mcq_list:
        st.subheader("📝 Questões de Múltipla Escolha")
        for i, questao in enumerate(mcq_list):
            with st.container(border=True):
                st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
                
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                # Gráfico dinâmico (se houver)
                codigo_plot = questao.get("codigo_plotly")
                if codigo_plot:
                    try:
                        local_vars = {}
                        exec(codigo_plot, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_chart_mcq_{i}")
                    except Exception as e:
                        st.warning("Gráfico indisponível no momento.")
    
                # Alternativas
                opcoes = questao.get("alternativas", {})
                selecionado = st.radio(
                    "Escolha uma alternativa:",
                    options=list(opcoes.keys()),
                    format_func=lambda x: f"{x}) {opcoes[x]}",
                    key=f"radio_mcq_{i}"
                )
                
                # Botão de Dica
                if st.button("💡 Dica", key=f"dica_mcq_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
                
                # Botão de Verificação
                if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
                    if selecionado == questao.get("alternativa_correta"):
                        st.success("Correto! Muito bem.")
                        st.session_state.respostas_certas[f"mcq_{i}"] = True
                        st.rerun()
                    else:
                        st.error("Resposta incorreta. Tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
                
                with st.expander("✅ Ver Gabarito Comentado"):
                    st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
    
    st.divider()
    
    # Processamento de Questões Discursivas
    if disc_list:
        st.subheader("✍️ Questões Discursivas")
        for i, questao in enumerate(disc_list):
            with st.container(border=True):
                st.markdown(f"**Desafio {i+1}:** {questao.get('enunciado', '')}")
                
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                codigo_plot = questao.get("codigo_plotly")
                if codigo_plot:
                    try:
                        local_vars = {}
                        exec(codigo_plot, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_chart_disc_{i}")
                    except Exception as e:
                        st.warning("Gráfico indisponível.")
    
                # Input de Resposta
                st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
                
                # Validação Numérica se houver, senão checkbox
                resp_esp = questao.get("resposta_numerica_esperada")
                if resp_esp is not None:
                    val = st.number_input("Digite o resultado numérico calculado para validação:", key=f"num_disc_{i}")
                    if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                        if abs(val - resp_esp) <= max(0.01, 0.01 * abs(resp_esp)):
                            st.success("Resposta Numérica Correta! Excelente trabalho.")
                            st.session_state.respostas_certas[f"disc_{i}"] = True
                            st.rerun()
                        else:
                            st.error("O valor calculado difere do gabarito oficial. Tente novamente.")
                            st.session_state.respostas_certas[f"disc_{i}"] = False
                else:
                    concluido = st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}")
                    if concluido:
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                    else:
                        st.session_state.respostas_certas[f"disc_{i}"] = False
                
                if st.button("💡 Dica", key=f"dica_disc_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
                
                with st.expander("✅ Ver Resolução Detalhada"):
                    for passo in questao.get("gabarito_passo_a_passo", []):
                        st.write(f"- {passo}")
