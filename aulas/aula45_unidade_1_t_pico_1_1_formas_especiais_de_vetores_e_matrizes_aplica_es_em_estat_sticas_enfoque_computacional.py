import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDEgLSBUw7NwaWNvIDEuMTogRm9ybWFzIGVzcGVjaWFpcyBkZSB2ZXRvcmVzIGUgbWF0cml6ZXMsIGFwbGljYcOnw7VlcyBlbSBFc3RhdMOtc3RpY2FzOiBlbmZvcXVlIGNvbXB1dGFjaW9uYWwiLCAicmVmZXJlbmNpYXNfYmlibGlvZ3JhZmljYXNfZmluYWlzIjogWyJMdW5hICYgRXN0ZXZlcywgTW9kZWxvcyBMaW5lYXJlcyAtIENhcC4gMSwgcHAuIDEtMiwgOS0xMSwgMTUtMjYiLCAiQm95ZCAmIFZhbmRlbmJlcmdoZSwgSW50cm9kdWN0aW9uIHRvIEFwcGxpZWQgTGluZWFyIEFsZ2VicmEgLSBDYXAuIDYuMSwgcHAuIDExMS0xMTIiXX0=').decode('utf-8'))

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

    # Capítulo: Vetores e Matrizes: Estruturas Fundamentais e Notação Matricial
    
    st.header(r"Vetores e Matrizes: Estruturas Fundamentais e Notação Matricial")
    
    st.markdown(r"""
    A transição da análise estatística univariada para a complexidade da estatística computacional exige uma mudança fundamental na forma como estruturamos o pensamento matemático. Quando nos deparamos com conjuntos de dados que transcendem a simples observação isolada, a notação algébrica convencional torna-se um obstáculo.
    """)
    
    st.info(r"A álgebra linear não é apenas uma conveniência, mas o idioma indispensável da ciência de dados moderna, transformando cálculos exaustivos em operações algorítmicas robustas.")
    
    st.markdown(r"""
    ### 🏛️ Contexto Histórico e Lógica de Organização
    Historicamente, o desenvolvimento das matrizes foi uma resposta à necessidade de representar a simultaneidade em sistemas de equações.
    - **Evolução:** Desde a matemática babilônica até a formalização rigorosa de Cayley e Sylvester no século XIX.
    - **Objetivo:** Superar métodos de resolução exaustivos, permitindo que vastos conjuntos de dados sejam tratados como entidades únicas.
    - **Eficiência:** O uso dessa notação é o pilar do processamento vetorizado, permitindo que algoritmos modernos executem cálculos em paralelo com precisão absoluta.
    """)
    
    st.subheader(r"📐 O Formalismo Matemático das Estruturas Matriciais")
    
    st.markdown(r"""
    Para representar uma amostra de $n$ unidades com $m$ variáveis, utilizamos a matriz $A_{(m \times n)}$. Esta estrutura organiza cada observação em linhas e cada característica em colunas, permitindo uma manipulação eficiente de dados multivariados.
    """)
    
    st.latex(r"A_{(m \times n)} = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{pmatrix}")
    
    st.markdown(r"A definição formal da matriz segue a organização dos índices $i$ e $j$:")
    st.latex(r"A_{(m \times n)} = [a_{ij}] \text{ para } i \in \{1, \dots, m\}, j \in \{1, \dots, n\}")
    st.latex(r"VetorColuna = A_{(m \times 1)}")
    st.latex(r"VetorLinha = A_{(1 \times n)}")
    
    st.subheader(r"📈 Casos de Aplicação Prática: Vetores e Matrizes no Âmbito Clínico")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Estruturação de Dados Laboratoriais")
        st.markdown(r"Em um estudo clínico, quatro pacientes são submetidos a três exames laboratoriais. O objetivo é organizar os dados para análise posterior, estruturando a informação em uma matriz de dados brutos que possibilite o processamento vetorizado.")
        
        st.latex(r"X_{(4 \times 3)} = \begin{pmatrix} 10 & 20 & 30 \\ 15 & 25 & 35 \\ 12 & 22 & 32 \\ 18 & 28 & 38 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Identificação:** O elemento $a_{11} = 10$ representa o primeiro exame do primeiro paciente.")
        st.markdown(r"- **Vetorização de Variáveis:** Podemos extrair o vetor de resultados do primeiro paciente como $l_1 = (10, 20, 30)$.")
        st.markdown(r"- **Vetorização de Colunas:** O vetor $c_1 = (10, 15, 12, 18)^T$ isola o desempenho do primeiro exame em toda a amostra.")
        
        st.success(r"A organização na matriz $X$ de dimensão (4x3) permite a aplicação imediata de funções de agregação, como o cálculo da média por paciente ou por exame, essencial para diagnósticos automatizados.")
    
    st.markdown(r"""
    ---
    ### 💡 Considerações Finais
    Ao consolidarmos estes conceitos, devemos olhar para a matriz como um mapa da nossa amostra. Cada valor $a_{ij}$ é uma peça do quebra-cabeça que, em conjunto, revela a estrutura latente de um processo estocástico. Este rigor notacional será o alicerce para nossas futuras discussões sobre Regressão Linear e Inferência Estatística.
    """)

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    
    # --- CABEÇALHO DO SUBTÓPICO ---
    st.header(r"Operações Matriciais Básicas: Álgebra e Propriedades")
    
    # --- PROSA TEÓRICA ---
    st.markdown(r"""
    A manipulação de estruturas matriciais constitui o alicerce sobre o qual reside a estatística multivariada contemporânea e a econometria avançada. Para o estudante de estatística, a transição do pensamento escalar para o matricial é o passo decisivo rumo à compreensão da modelagem de dados complexos.
    """)
    
    st.info(r"As matrizes não são meros arranjos retangulares; elas funcionam como operadores matemáticos capazes de representar transformações lineares, encapsular correlações e consolidar observações em objetos manipuláveis.")
    
    st.markdown(r"""
    ### ⚙️ A Mecânica da Multiplicação Matricial e sua Intuição Geométrica
    A operação de multiplicação matricial, formalmente definida pelo produto interno entre linhas e colunas, representa a essência da composição de transformações:
    
    - **Processo de Filtragem:** Ao multiplicar uma matriz de dados por um vetor de pesos, projeta-se o dado em uma nova base.
    - **Composição de Efeitos:** Permite tratar sistemas completos de observações como uma unidade atômica.
    - **Intuição Geométrica:** Atua como um mapa que transforma vetores em espaços euclidianos, realizando rotações ou projeções.
    """)
    
    st.latex(r"C = AB \implies c_{ik} = \sum_{j=1}^{n} a_{ij}b_{jk}")
    
    st.markdown(r"""
    ### 🔄 A Transposição como Alternativa de Perspectiva
    A transposição, denotada por $A^T$, é uma mudança na perspectiva analítica. Se a matriz $A$ organiza observações por linhas e variáveis por colunas, a transposta reorienta o objeto para que as variáveis passem a ocupar o eixo das linhas. Este mecanismo é a chave para:
    
    1. Alternar entre a visão de 'observação' e 'atributo'.
    2. Construir matrizes de covariância amostral.
    3. Superar barreiras dimensionais em algoritmos como PCA (Análise de Componentes Principais).
    """)
    
    st.latex(r"A^T = [a_{ji}]")
    
    st.markdown(r"""
    ### 🛡️ O Papel da Matriz Identidade como Elemento Estabilizador
    No universo das matrizes, a matriz identidade $I_n$ cumpre o papel do número 1 na aritmética escalar. Ela é definida pela delta de Kronecker, atuando como o elemento neutro essencial para a inversibilidade.
    """)
    
    st.latex(r"I_n = [\delta_{ij}], \text{ onde } \delta_{ij} = 1 \text{ se } i=j, \text{ senão } 0")
    
    st.warning(r"A busca por sistemas não-singulares (que admitem inversa) garante que um modelo estatístico tenha uma solução única e interpretável. A ausência de inversa sinaliza colinearidade perfeita, ou seja, redundância informacional.")
    
    # --- DEDUÇÕES ANALÍTICAS ---
    st.markdown(r"### 📐 O Coração Matemático: Álgebra de Matrizes")
    
    st.markdown(r"Abaixo, consolidamos a fundamentação algébrica da multiplicação e a preservação de propriedades através da transposição:")
    
    st.latex(r"C_{(m \times p)} = A_{(m \times n)} B_{(n \times p)} \implies c_{ik} = \sum_{j=1}^n a_{ij}b_{jk}")
    
    st.markdown(r"A neutralidade da identidade é confirmada pela soma dos produtos:")
    st.latex(r"I_n A = A \implies \sum_{j=1}^n \delta_{ij} a_{jk} = a_{ik}")
    
    st.markdown(r"A propriedade da transposição do produto reflete a reversão na ordem dos fatores:")
    st.latex(r"(AB)^T = [c_{ki}] = [\sum_{j=1}^n a_{kj}b_{ji}] = B^T A^T")
    
    # --- EXEMPLOS PRÁTICOS ---
    st.markdown(r"### 📈 Casos de Aplicação Prática: Transformações Lineares")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Reflexão de Vetores")
        st.markdown(r"Para uma transformação de escala em um experimento, aplica-se a matriz $A$ sobre o vetor $x$. Verificamos a simetria da matriz de transformação.")
        
        st.latex(r"x = \begin{pmatrix} 2 \\ 3 \end{pmatrix}, A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Multiplicação do operador pela amostra: $Ax = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 2 \\ 3 \end{pmatrix}$")
        st.markdown(r"- Resultado do produto escalar por linha: $Ax = \begin{pmatrix} (1)(2) + (0)(3) \\ (0)(2) + (-1)(3) \end{pmatrix} = \begin{pmatrix} 2 \\ -3 \end{pmatrix}$")
        
        st.success(r"O vetor transformado é (2, -3)^T. A igualdade A = A^T confirma que a matriz de transformação é simétrica, o que garante a preservação de propriedades ortogonais no espaço de coordenadas após a reflexão.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Estruturas Especiais de Matrizes e Particionamento")
    
    # Introdução e Contexto Teórico
    st.markdown(r"""
    A Álgebra Linear, em sua essência aplicada à estatística, não é apenas um conjunto de ferramentas operacionais, mas a linguagem que descreve a estrutura da incerteza e da dependência entre variáveis. Quando lidamos com matrizes estruturadas, estamos observando reflexos geométricos de fenômenos estatísticos.
    """)
    
    st.info(r"A simetria, no contexto de uma matriz de variância-covariância, traduz matematicamente a reciprocidade intrínseca da dependência: a influência de uma variável $X_i$ na variabilidade de $X_j$ é idêntica à influência de $X_j$ sobre $X_i$.")
    
    st.markdown(r"""
    ### 📐 Propriedades da Simetria e Eficiência
    A condição de simetria $A = A^T$ oferece ganhos significativos no processamento estatístico:
    * **Redução Computacional:** Algoritmos como a Decomposição de Cholesky exploram a redundância da matriz, operando apenas na metade dos elementos.
    * **Otimização de Memória:** O armazenamento é otimizado ao negligenciar a replicação de elementos fora da diagonal.
    * **Estrutura da Variância:** A diagonal principal mantém o locus das variâncias individuais ($\sigma^2$), enquanto os elementos fora da diagonal quantificam a estrutura de dependência linear ($\sigma_{ij}$).
    """)
    
    st.latex(r"A = A^T \iff a_{ij} = a_{ji}")
    
    # Demonstração Analítica (Exibição sequencial direta, não em expanders)
    st.markdown(r"### 🛠️ O Formalismo da Decomposição Matricial")
    st.markdown(r"A representação de uma matriz simétrica particionada em blocos segue a estrutura:")
    st.latex(r"A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}")
    
    st.markdown(r"Ao multiplicar tais blocos, operamos segundo a lógica de blocos:")
    st.latex(r"AB = \begin{pmatrix} A_{11}B_{11} + A_{12}B_{21} & A_{11}B_{12} + A_{12}B_{22} \\ A_{21}B_{11} + A_{22}B_{21} & A_{21}B_{12} + A_{22}B_{22} \end{pmatrix}")
    
    # Exemplo Prático de Particionamento
    st.markdown(r"### 📈 Casos de Aplicação: Estimação em Múltiplas Etapas")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Particionamento de Equações Normais")
        st.markdown(r"No modelo $y = X_1\theta_1 + X_2\theta_2 + e$, isolamos o parâmetro $\theta_2$ através do particionamento do sistema $X^T X \theta = X^T y$.")
        
        st.latex(r"\begin{pmatrix} X_1^T X_1 & X_1^T X_2 \\ X_2^T X_1 & X_2^T X_2 \end{pmatrix} \begin{pmatrix} \theta_1 \\ \theta_2 \end{pmatrix} = \begin{pmatrix} X_1^T y \\ X_2^T y \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Definimos o projetor $P_1 = X_1 (X_1^T X_1)^{-1} X_1^T$")
        st.markdown(r"- Após operações de isolamento, reduzimos o sistema para a forma projetada.")
        st.latex(r"X_2^T (I - P_1) X_2 \theta_2 = X_2^T (I - P_1) y")
        
        st.success(r"A solução final para $\theta_2$ demonstra que o particionamento permite o isolamento de efeitos específicos em modelos de grande escala, reduzindo drasticamente a carga computacional.")
    
    # Adendo: Visualização de Particionamento (Simulação de Blocos)
    st.markdown(r"### 🖥️ Simulador: Visualização de Particionamento de Variância")
    col1, col2 = st.columns(2)
    with col1:
        diag_val = st.slider(r"Variância (Diagonal)", 1.0, 5.0, 2.0, step=0.1, key=r"diag_val_subtopico_3")
    with col2:
        cov_val = st.slider(r"Covariância (Off-diagonal)", 0.0, 1.0, 0.5, step=0.05, key=r"cov_val_subtopico_3")
    
    # Criação de gráfico Plotly para representar o conceito
    matrix_data = np.array([[diag_val, cov_val], [cov_val, diag_val]])
    fig = go.Figure(data=go.Heatmap(
        z=matrix_data,
        colorscale=[[0, "#F8FAFC"], [1, "#1E3A8A"]],
        showscale=False
    ))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        plot_bgcolor="white",
        paper_bgcolor="white",
        title=dict(text=r"<b>Estrutura de Covariância 2x2</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Variável j", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Variável i", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    st.info(f"Ao ajustar a variância para {diag_val} e a covariância para {cov_val}, a matriz simétrica reflete o grau de dependência entre os dois componentes particionados do seu sistema linear.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    
    # Cabeçalho do Subtópico
    st.header(r"Formas Escalonadas e o Posto (Rank) de Matrizes")
    
    # Introdução e Contexto
    st.markdown(r"""
    O conceito de posto de uma matriz, frequentemente denotado como $r(A)$, representa a espinha dorsal sobre a qual construímos toda a teoria de modelos lineares e inferência estatística multivariada. 
    Em termos matemáticos, o posto corresponde à dimensão do espaço vetorial gerado por suas colunas, ou pela dimensão do espaço gerado por suas linhas.
    
    Para o estatístico, essa definição é a métrica fundamental que nos informa sobre a verdadeira dimensão da informação contida em um conjunto de dados. Quando observamos uma matriz de dados, onde cada coluna representa uma variável e cada linha uma observação, o posto nos revela a independência real das variáveis.
    """)
    
    st.info(r"Se o posto for inferior ao número de colunas, estamos diante de um cenário de redundância: a variabilidade observada pode ser explicada por um subespaço de dimensão menor do que o original.")
    
    st.markdown(r"""
    ### 📐 O Coração Matemático: Posto e Espaços Fundamentais
    A relação formal entre as dimensões dos espaços fundamentais é estabelecida pela identidade abaixo:
    """)
    
    st.latex(r"r(A) = \dim(C(A)) = \dim(L(A))")
    st.latex(r"r(A) = \# \text{ linhas não nulas na forma escalonada}")
    
    st.markdown(r"""
    A eliminação de Gauss introduziu uma metodologia determinística para purificar a matriz, transformando-a em sua forma escalonada. Este processo revela a base do espaço vetorial, permitindo identificar a estrutura subjacente da informação sem alterar as relações de dependência linear.
    """)
    
    # Dedução Analítica (Estática)
    st.markdown(r"**Processo de Identificação do Posto:**")
    st.latex(r"A_{(m \times n)} \xrightarrow{\text{operações elementares}} H_{(m \times n)}")
    st.markdown(r"Onde $H$ é a forma escalonada. A invariância do posto garante que:")
    st.latex(r"r(A) = r(H)")
    st.markdown(r"O número de linhas não nulas, ou pivôs, em $H$ define precisamente o posto da matriz.")
    
    # Casos de Aplicação Prática
    st.markdown(r"### 📈 Casos de Aplicação Prática: Avaliação de Redundância")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Testes Laboratoriais para 4 Pacientes")
        st.markdown(r"Dada a matriz de delineamento $X$ referente a dois testes aplicados em 4 pacientes, avaliamos a redundância:")
        st.latex(r"X = \begin{pmatrix} 1 & 1 \\ 1 & 1 \\ 1 & 0 \\ 1 & 0 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- $R_2 - R_1 \to R_2, \quad R_3 - R_1 \to R_3, \quad R_4 - R_1 \to R_4$")
        st.markdown(r"- Identificação dos pivôs e eliminação sistemática resulta em:")
        st.latex(r"H = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \\ 0 & 0 \end{pmatrix}")
        
        st.success(r"A matriz escalonada $H$ apresenta 2 linhas não nulas, logo $r(X) = 2$. A matriz possui posto coluna completo, indicando independência total entre os testes.")
    
    # Simulador de Posto Matricial
    st.markdown(r"### 🎛️ Simulador: Visualizador de Posto Matricial")
    st.markdown(r"Altere os valores da matriz abaixo para observar como a dependência linear afeta o posto calculado em tempo real.")
    
    # Inicialização do editor
    df_inicial = pd.DataFrame([[1, 1], [1, 1], [1, 0], [1, 0]], columns=["Var A", "Var B"])
    matriz_editada = st.data_editor(df_inicial, use_container_width=True, key=r"data_editor_subtopico_4")
    
    # Cálculo do posto
    matriz_np = matriz_editada.to_numpy()
    posto = np.linalg.matrix_rank(matriz_np)
    
    # Lógica de Laudo Dinâmico
    if posto < min(matriz_np.shape):
        st.error(f"Posto Deficiente: r(A) = {posto}. Foram detectadas dependências lineares (redundância).")
    else:
        st.success(f"Posto Completo: r(A) = {posto}. As colunas formam uma base independente.")
    
    # Gráfico de visualização das colunas (Representação 2D)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, matriz_np[0,0]], y=[0, matriz_np[0,1]], mode='lines+markers', name='Vet. Coluna 1', line=dict(color="#1E3A8A")))
    fig.add_trace(go.Scatter(x=[0, matriz_np[0,1]], y=[0, matriz_np[1,1]], mode='lines+markers', name='Vet. Coluna 2', line=dict(color="#10B981")))
    
    fig.update_layout(
        title=dict(text="<b>Representação Vetorial das Variáveis</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        xaxis=dict(title=dict(text="Dimensão 1", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Dimensão 2", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    
    # Cabeçalho do Subtópico
    st.header(r"Matrizes Especiais e Decomposição Espectral")
    
    # Introdução Teorica
    st.markdown(r"""
    A análise de matrizes, sob a lente da Estatística Matemática, transcende a simples manipulação de arranjos numéricos bidimensionais; ela constitui a própria infraestrutura sobre a qual assentamos a inferência multivariada, a teoria de modelos lineares e a redução de dimensionalidade.
    """)
    
    st.info(r"A decomposição espectral atua como um 'exame de DNA' matricial, revelando as direções principais de variabilidade através de autovetores e a magnitude dessas variações via autovalores. Este conceito é a pedra angular da Análise de Componentes Principais (ACP).")
    
    st.markdown(r"""
    Quando trabalhamos com uma matriz de covariância, os autovetores nos indicam as direções ortogonais no espaço de características onde a variabilidade é maximizada, enquanto os autovalores associados quantificam a magnitude dessa variação.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 Estrutura Formal: Decomposição Espectral e Idempotência")
    st.latex(r"A = U \text{diag}(\lambda_1, \dots, \lambda_n) U^T = \sum_{i=1}^n \lambda_i u_i u_i^T")
    st.latex(r"A^2 = A \text{ (Propriedade das Matrizes Idempotentes)}")
    
    # Simulador: Decomposição Espectral Dinâmica
    st.subheader(r"⚙️ Simulador: Decomposição Espectral Dinâmica")
    col1, col2 = st.columns(2)
    with col1:
        l1 = st.slider(r"Autovalor $\lambda_1$", 0.1, 5.0, 3.0, key=r"l1_subtopico_5")
    with col2:
        l2 = st.slider(r"Autovalor $\lambda_2$", 0.1, 5.0, 1.0, key=r"l2_subtopico_5")
    
    theta = np.linspace(0, 2*np.pi, 100)
    x = np.sqrt(l1) * np.cos(theta)
    y = np.sqrt(l2) * np.sin(theta)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode=r"lines", name=r"Variabilidade (Elipsoide)", line=dict(color=r"#1E3A8A", width=2)))
    fig.update_layout(
        template=r"plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Visualização da Dispersão via Autovalores</b>", font=dict(size=14, color=r"#1E293B", family=r"Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Componente Principal 1", font=dict(size=11, color=r"#1E293B")), tickfont=dict(size=9, color=r"#64748B"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Componente Principal 2", font=dict(size=11, color=r"#1E293B")), tickfont=dict(size=9, color=r"#64748B"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        legend=dict(orientation=r"h", yanchor=r"bottom", y=1.02, xanchor=r"right", x=1.0, font=dict(size=9, color=r"#64748B"), bgcolor=r"rgba(255, 255, 255, 0.8)", bordercolor=r"#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor=r"#FFFFFF", font_size=12, font_color=r"#1E293B")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_5")
    
    st.info(rf"Com autovalores $\lambda_1 = {l1}$ e $\lambda_2 = {l2}$, o elipsoide de variabilidade reflete a dominância da primeira componente, que captura { (l1/(l1+l2))*100:.1f}% da variância total do sistema.")
    
    # Dedução Analítica
    st.subheader(r"🔍 O Coração Matemático: Propriedades dos Operadores")
    st.latex(r"Au_i = \lambda_i u_i")
    st.markdown(r"A ação de uma matriz sobre seu autovetor resulta apenas em um escalonamento linear.")
    st.latex(r"AU = U\Lambda")
    st.markdown(r"A forma compacta da diagonalização de operadores simétricos.")
    st.latex(r"A = U\Lambda U^T")
    st.markdown(r"A representação espectral que nos permite descartar ruído em direções de baixa variância.")
    st.latex(r"\text{Tr}(A) = \sum \lambda_i = r(A) \text{ para } A^2=A")
    
    # Exemplo Prático
    st.subheader(r"📈 Caso de Aplicação Prática: Decomposição de Covariância")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Identificação de Posto em Matriz de Covariância")
        st.markdown(r"Dada a matriz de covariância simétrica $A$, identifique seus autovalores e a estrutura de sua decomposição.")
        st.latex(r"A = \begin{pmatrix} 4 & 2 & 2 \\ 2 & 2 & 0 \\ 2 & 0 & 2 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Determinação do polinômio característico: $|A - \lambda I| = -\lambda(\lambda^2 - 8\lambda + 12) = 0$")
        st.markdown(r"- Autovalores encontrados: $\lambda_1 = 6, \lambda_2 = 2, \lambda_3 = 0$")
        st.markdown(r"- Estrutura: $A = 6u_1u_1^T + 2u_2u_2^T + 0u_3u_3^T$")
        
        st.success(r"A matriz A é semipositiva definida (posto 2). A ausência de valor em $\lambda_3$ indica que a terceira direção de variabilidade é nula, confirmando uma estrutura de dados de posto reduzido.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDEgLSBUw7NwaWNvIDEuMTogRm9ybWFzIGVzcGVjaWFpcyBkZSB2ZXRvcmVzIGUgbWF0cml6ZXMsIGFwbGljYcOnw7VlcyBlbSBFc3RhdMOtc3RpY2FzOiBlbmZvcXVlIGNvbXB1dGFjaW9uYWwiLCAicXVlc3RvZXNfbXVsdGlwbGFfZXNjb2xoYSI6IFt7ImVudW5jaWFkbyI6ICJFbSB1bSBzaXN0ZW1hIGRlIG1vbml0b3JhbWVudG8gZXN0cnV0dXJhbCBkZSBwb250ZXMgdXRpbGl6YW5kbyBJb1QsIHNlbnNvcmVzIGNvbGV0YW0gZGFkb3MgZGUgYWNlbGVyYcOnw6NvIGVtIGRpZmVyZW50ZXMgcG9udG9zIGFvIGxvbmdvIGRvIHRlbXBvLiBTdXBvbmhhIHF1ZSBvIHNpc3RlbWEgbW9uaXRvcmUgJG0gPSAxMCQgcG9udG9zIGRpc3RpbnRvcyBkYSBlc3RydXR1cmEgZSByZWdpc3RyZSAkbiA9IDUwJCBpbnRlcnZhbG9zIGRlIHRlbXBvLiBPcyBkYWRvcyBzw6NvIG9yZ2FuaXphZG9zIGVtIHVtYSBtYXRyaXogJEEkIG9uZGUgY2FkYSBsaW5oYSByZXByZXNlbnRhIHVtIHBvbnRvIGRlIG1vbml0b3JhbWVudG8gZSBjYWRhIGNvbHVuYSByZXByZXNlbnRhIHVtIGluc3RhbnRlIGRlIHRlbXBvLiBRdWFsIMOpIGEgZGltZW5zw6NvIGNvcnJldGEgZGEgbWF0cml6ICRBJCBlIGNvbW8gZGVub3RhbW9zIG8gZWxlbWVudG8gJGFfe2lqfSQgcXVlIHJlcHJlc2VudGEgYSBsZWl0dXJhIGRvIHNlbnNvciAkaSQgbm8gaW5zdGFudGUgJGokPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBtYXRyaXogdGVtIGRpbWVuc8OjbyAkKDUwIFxcdGltZXMgMTApJCwgb25kZSAkaSQgdmFyaWEgZGUgJDEkIGEgJDUwJCBlICRqJCB2YXJpYSBkZSAkMSQgYSAkMTAkLiIsICJCIjogIkEgbWF0cml6IHRlbSBkaW1lbnPDo28gJCgxMCBcXHRpbWVzIDUwKSQsIG9uZGUgJGkkIGRlbm90YSBhIGxpbmhhIChzZW5zb3IpIGUgJGokIGRlbm90YSBhIGNvbHVuYSAoaW5zdGFudGUgZGUgdGVtcG8pLiIsICJDIjogIkEgbWF0cml6IHRlbSBkaW1lbnPDo28gJCgxMCBcXHRpbWVzIDUwKSQsIHNlbmRvICRhX3tpan0kIGEgbGVpdHVyYSBkbyBpbnN0YW50ZSAkaSQgbm8gc2Vuc29yICRqJC4iLCAiRCI6ICJBIG1hdHJpeiB0ZW0gZGltZW5zw6NvICQoNTAgXFx0aW1lcyAxMCkkLCBvbmRlICRhX3tpan0kIHJlcHJlc2VudGEgYSBtw6lkaWEgZGFzIGxlaXR1cmFzIG5vIHRlbXBvICRpJC4iLCAiRSI6ICJBIG1hdHJpeiB0ZW0gZGltZW5zw6NvICQoMTAsIDEwKSQsIHBvaXMgbyBuw7ptZXJvIGRlIHNlbnNvcmVzIGRldmUgc2VyIGlndWFsIGFvIG7Dum1lcm8gZGUgaW5zdGFudGVzIGRlIG1lZGnDp8OjbyBwYXJhIHZpYWJpbGl6YXIgYSBhbsOhbGlzZS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBkZWZpbmnDp8OjbyBkZSBkaW1lbnPDo28gJChtIFxcdGltZXMgbikkIGNvbW8gKG7Dum1lcm8gZGUgbGluaGFzICRcXHRpbWVzJCBuw7ptZXJvIGRlIGNvbHVuYXMpLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBtYXRyaXogJEEkIMOpIGRlZmluaWRhIHBlbG8gYXJyYW5qbyByZXRhbmd1bGFyIGRlICRtJCBsaW5oYXMgZSAkbiQgY29sdW5hcy4gTmVzdGUgcHJvYmxlbWEsIHRlbW9zICRtID0gMTAkIGxpbmhhcyAocG9udG9zIGRlIG1vbml0b3JhbWVudG8pIGUgJG4gPSA1MCQgY29sdW5hcyAoaW5zdGFudGVzIGRlIHRlbXBvKS4gUG9ydGFudG8sIGEgZGltZW5zw6NvIMOpICQoMTAgXFx0aW1lcyA1MCkkLiBPIGVsZW1lbnRvICRhX3tpan0kIHJlZmVyZS1zZSwgcG9yIGNvbnZlbsOnw6NvIG1hdHJpY2lhbCwgw6AgaW50ZXJzZcOnw6NvIGRhIGxpbmhhICRpJCBjb20gYSBjb2x1bmEgJGokLiBBc3NpbSwgYSBhbHRlcm5hdGl2YSBCIMOpIGEgY29ycmV0YSBhbyBkZXNjcmV2ZXIgYWRlcXVhZGFtZW50ZSBhIGRpbWVuc8OjbyBlIGEgbm90YcOnw6NvIGRvcyDDrW5kaWNlcy4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoZGF0YT1bZ28uVGFibGUoaGVhZGVyPWRpY3QodmFsdWVzPVsnU2Vuc29yIChMaW5oYSBpKScsICdJbnN0YW50ZSAxJywgJ0luc3RhbnRlIDInLCAnLi4uJ10pLCBjZWxscz1kaWN0KHZhbHVlcz1bWydTMScsICdTMicsICcuLi4nXSwgWydhMTEnLCAnYTIxJywgJy4uLiddLCBbJ2ExMicsICdhMjInLCAnLi4uJ10sIFsnLi4uJywgJy4uLicsICcuLi4nXV0pKV0pXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nUmVwcmVzZW50YcOnw6NvIFZpc3VhbCBkYSBNYXRyaXogZGUgU2Vuc29yZXMnKVxuZmlnLnNob3coKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVuc2FpbyBjbMOtbmljbywgb3MgcmVzdWx0YWRvcyBkZSAkbiQgcGFjaWVudGVzIHPDo28gcmVnaXN0cmFkb3MuIFBhcmEgY2FkYSBwYWNpZW50ZSwgb2JzZXJ2YW1vcyBhcyBzZWd1aW50ZXMgdmFyacOhdmVpczogaWRhZGUsIHByZXNzw6NvIGFydGVyaWFsIHNpc3TDs2xpY2EgZSBmcmVxdcOqbmNpYSBjYXJkw61hY2EuIFNlIGRlc2VqYW1vcyByZXByZXNlbnRhciBvcyBkYWRvcyBkZSB1bSDDum5pY28gcGFjaWVudGUgJGskIGNvbW8gdW0gdmV0b3IsIHF1YWwgc2VyaWEgYSBlc3RydXR1cmEgZGltZW5zaW9uYWwgbWFpcyBhcHJvcHJpYWRhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiVW0gdmV0b3IgY29sdW5hIGRlIGRpbWVuc8OjbyAkKDMgXFx0aW1lcyAxKSQsIG9uZGUgY2FkYSBsaW5oYSBjb3JyZXNwb25kZSBhIHVtYSB2YXJpw6F2ZWwgb2JzZXJ2YWRhLiIsICJCIjogIlVtIHZldG9yIGxpbmhhIGRlIGRpbWVuc8OjbyAkKG4gXFx0aW1lcyAzKSQsIHBvaXMgbyBwYWNpZW50ZSDDqSB1bWEgb2JzZXJ2YcOnw6NvIMO6bmljYS4iLCAiQyI6ICJVbWEgbWF0cml6IGRlIGRpbWVuc8OjbyAkKDEgXFx0aW1lcyAzKSQsIHNlbmRvIG8gbsO6bWVybyBkZSBjb2x1bmFzIGlndWFsIGFvIG7Dum1lcm8gZGUgcGFjaWVudGVzLiIsICJEIjogIlVtIHZldG9yIGNvbHVuYSBkZSBkaW1lbnPDo28gJCgxIFxcdGltZXMgMykkLCB0cmF0YW5kbyBhcyB2YXJpw6F2ZWlzIGNvbW8gY29sdW5hcy4iLCAiRSI6ICJVbSBlc2NhbGFyLCB2aXN0byBxdWUgdG9kYXMgYXMgbWVkaWRhcyBzZSByZWZlcmVtIGEgdW0gw7puaWNvIGluZGl2w61kdW8uIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJDb25zaWRlcmUgcXVlLCBwYXJhIHVtIMO6bmljbyBpbmRpdsOtZHVvLCBxdWVyZW1vcyBhZ3J1cGFyIDMgdmFyacOhdmVpcyBkaXN0aW50YXMgZW0gdW1hIGVzdHJ1dHVyYSB2ZXJ0aWNhbC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlVtIHZldG9yIGNvbHVuYSDDqSB1bWEgbWF0cml6IGRlIGRpbWVuc8OjbyAkKG0gXFx0aW1lcyAxKSQuIENvbW8gdGVtb3MgMyB2YXJpw6F2ZWlzIChpZGFkZSwgcHJlc3PDo28sIGZyZXF1w6puY2lhKSBwYXJhIHVtIHBhY2llbnRlLCBvcmdhbml6YW1vcyBlc3NhcyAzIG1lZGlkYXMgZW0gMyBsaW5oYXMgZGUgdW1hIMO6bmljYSBjb2x1bmEsIHJlc3VsdGFuZG8gZW0gdW1hIGVzdHJ1dHVyYSAkKDMgXFx0aW1lcyAxKSQuIEVzdGEgbm90YcOnw6NvIMOpIG8gcGFkcsOjbyBwYXJhIHJlcHJlc2VudGFyIGNhcmFjdGVyw61zdGljYXMgKHZhcmnDoXZlaXMpIGRlIHVtIMO6bmljbyBvYmpldG8gZGUgZXN0dWRvIChvIHBhY2llbnRlKSBuYSDDoWxnZWJyYSBsaW5lYXIgYXBsaWNhZGEgw6AgZXN0YXTDrXN0aWNhLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gc2lzdGVtYSBkZSBtb25pdG9yYW1lbnRvIGRlIHNlbnNvcmVzIElvVCAoSW50ZXJuZXQgb2YgVGhpbmdzKSwgdGVtb3MgdW1hIG1hdHJpeiAkQV97KDIgXHRpbWVzIDMpfSQgY29udGVuZG8gYXMgbGVpdHVyYXMgZGUgdHLDqnMgc2Vuc29yZXMgZW0gZG9pcyBtb21lbnRvcyBkaWZlcmVudGVzLCBlIHVtYSBtYXRyaXogZGUgcGVzb3MgJEJfeygzIFx0aW1lcyAyKX0kIHF1ZSBhanVzdGEgYSBpbXBvcnTDom5jaWEgZGUgY2FkYSBzZW5zb3IgcGFyYSBkb2lzIGluZGljYWRvcmVzIGRlIGRlc2VtcGVuaG8gZGlzdGludG9zLiBPIHByb2R1dG8gJEMgPSBBQiQgcmVzdWx0YSBuYSBtYXRyaXogZGUgaW5kaWNhZG9yZXMuIFNlIG8gZWxlbWVudG8gJGFfezEyfSA9IDAuNSQgKGxlaXR1cmEgZG8gc2Vuc29yIDIgbm8gdGVtcG8gMSkgZSBvIHBlc28gY29ycmVzcG9uZGVudGUgcGFyYSBvIGluZGljYWRvciAxIMOpICRiX3syMX0gPSAwLjgkLCBxdWFsIG8gcGFwZWwgZG8gc29tYXTDs3JpbyBubyBjw6FsY3VsbyBkbyBlbGVtZW50byAkY197MTF9ID0gXFxzdW1fe2o9MX1eezN9IGFfezFqfWJfe2oxfSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJFbGUgcmVwcmVzZW50YSBhcGVuYXMgYSBtw6lkaWEgYXJpdG3DqXRpY2EgZGFzIGxlaXR1cmFzIGRvcyBzZW5zb3Jlcy4iLCAiQiI6ICJFbGUgY3VtcHJlIGEgZnVuw6fDo28gZGUgaW50ZWdyYXIgYXMgaW5mb3JtYcOnw7VlcyBkZSB0b2RvcyBvcyBzZW5zb3JlcywgcG9uZGVyYW5kbyBjYWRhIGxlaXR1cmEgcGVsbyBzZXUgcGVzbyBlc3BlY8OtZmljbyBwYXJhIG8gaW5kaWNhZG9yIDEuIiwgIkMiOiAiRWxlIGluZGljYSBxdWUgYXMgbGVpdHVyYXMgc8OjbyBpbmRlcGVuZGVudGVzIGVudHJlIHNpIGUgbyByZXN1bHRhZG8gw6kgYXBlbmFzIG8gcHJvZHV0byBlc2NhbGFyIGRvIHNlbnNvciAyLiIsICJEIjogIkVsZSByZWFsaXphIGEgdHJhbnNwb3Npw6fDo28gZGEgbWF0cml6IGRlIGxlaXR1cmEsIGdhcmFudGluZG8gcXVlIG8gdGVtcG8gbsOjbyBpbmZsdWVuY2llIG8gaW5kaWNhZG9yIGZpbmFsLiIsICJFIjogIkVsZSBkZWZpbmUgYSBtYXRyaXogaWRlbnRpZGFkZSBkbyBzaXN0ZW1hLCBpc29sYW5kbyBhIGluZmx1w6puY2lhIGRvIHNlbnNvciAxIG5vIHJlc3VsdGFkbyBmaW5hbC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBkZWZpbmnDp8OjbyBkYSBvcGVyYcOnw6NvIGRlIHByb2R1dG8gbWF0cmljaWFsOiBjYWRhIGVudHJhZGEgZGEgbWF0cml6IHJlc3VsdGFudGUgw6kgbyBwcm9kdXRvIGludGVybm8gZGUgdW1hIGxpbmhhIGRlIEEgcG9yIHVtYSBjb2x1bmEgZGUgQi4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgZGVmaW5pw6fDo28gZG8gZWxlbWVudG8gJGNfe2lrfSA9IFxcc3VtX3tqPTF9XntufSBhX3tpan1iX3tqa30kIG1vc3RyYSBxdWUsIHBhcmEgY2FsY3VsYXIgbyBpbmRpY2Fkb3IgbmEgbGluaGEgMSBlIGNvbHVuYSAxLCBkZXZlbW9zIG11bHRpcGxpY2FyIGNhZGEgZWxlbWVudG8gZGEgbGluaGEgMSBkZSBBIHBlbG9zIHJlc3BlY3Rpdm9zIGVsZW1lbnRvcyBkYSBjb2x1bmEgMSBkZSBCIGUgc29tw6EtbG9zLiBJc3NvIGVmZXRpdmFtZW50ZSBjb21iaW5hIGFzIGluZm9ybWHDp8O1ZXMgZGUgdG9kb3Mgb3Mgc2Vuc29yZXMgKGo9MSwgMiwgMykgcG9uZGVyYWRvcyBwZWxvcyBwZXNvcyBkYSBjb2x1bmEgMSBkZSBCLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtYSBtYXRyaXogZGUgZGFkb3MgJFhfeyhuIFx0aW1lcyBwKX0kIG9uZGUgJG4kIMOpIG8gbsO6bWVybyBkZSBvYnNlcnZhw6fDtWVzIGUgJHAkIMOpIG8gbsO6bWVybyBkZSB2YXJpw6F2ZWlzLiBFbSBhbsOhbGlzZXMgZGUgZXN0YXTDrXN0aWNhIG11bHRpdmFyaWFkYSwgZnJlcXVlbnRlbWVudGUgdHJhYmFsaGFtb3MgY29tIGEgdHJhbnNwb3N0YSAkWF5UJC4gUXVhbCBkYXMgcHJvcHJpZWRhZGVzIGFiYWl4byBzb2JyZSBhIHRyYW5zcG9zacOnw6NvIGUgYSBtYXRyaXogaWRlbnRpZGFkZSAkSSQgw6kgbWF0ZW1hdGljYW1lbnRlIGNvcnJldGE/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIHRyYW5zcG9zacOnw6NvIGRlIHVtYSBtYXRyaXogcHJlc2VydmEgYSBvcmRlbSBvcmlnaW5hbCBkYXMgZGltZW5zw7VlcywgbG9nbyAkKFheVClfeyhuIFxcdGltZXMgcCl9ID0gWF97KG4gXFx0aW1lcyBwKX0kLiIsICJCIjogIk8gcHJvZHV0byBkZSB1bWEgbWF0cml6ICRYX3sobiBcXHRpbWVzIHApfSQgcGVsYSBtYXRyaXogaWRlbnRpZGFkZSAkSV9wJCByZXN1bHRhIGVtIHVtYSBtYXRyaXogbnVsYSAkMF97KG4gXFx0aW1lcyBwKX0kLiIsICJDIjogIkEgbWF0cml6IHRyYW5zcG9zdGEgJFheVCQgdGVtIGRpbWVuc8O1ZXMgJChwIFxcdGltZXMgbikkIGUgaW52ZXJ0ZSBhIHBvc2nDp8OjbyBkb3MgZWxlbWVudG9zIHRhbCBxdWUgJChYXlQpX3tqaX0gPSB4X3tpan0kLiIsICJEIjogIkEgbWF0cml6IGlkZW50aWRhZGUgJElfbiQgbXVsdGlwbGljYWRhIHBvciAkWF97KG4gXFx0aW1lcyBwKX0kIGFsdGVyYSBvcyB2YWxvcmVzIGRvcyBkYWRvcyBvcmlnaW5haXMgY29uZm9ybWUgbyB2YWxvciBkZSAkXFxkZWx0YV97aWp9JC4iLCAiRSI6ICJBIHRyYW5zcG9zacOnw6NvIGRlIHVtYSBtYXRyaXogc8OzIMOpIHBvc3PDrXZlbCBzZSBvIG7Dum1lcm8gZGUgbGluaGFzIGZvciBpZ3VhbCBhbyBuw7ptZXJvIGRlIGNvbHVuYXMgKG1hdHJpemVzIHF1YWRyYWRhcykuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJBbmFsaXNlIGEgZGVmaW5pw6fDo28gZGEgdHJhbnNwb3N0YTogZWxhIHRyb2NhIGxpbmhhcyBwb3IgY29sdW5hcywgYWx0ZXJhbmRvIGEgZXN0cnV0dXJhIGRlIGFybWF6ZW5hbWVudG8gZG9zIGRhZG9zLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBkZWZpbmnDp8OjbyBmb3JtYWwgZGUgdHJhbnNwb3N0YSBlc3RhYmVsZWNlIHF1ZSBhIGxpbmhhICRpJCBkYSBtYXRyaXogb3JpZ2luYWwgdG9ybmEtc2UgYSBjb2x1bmEgJGkkIGRhIG1hdHJpeiB0cmFuc3Bvc3RhLiBQb3J0YW50bywgdW1hIG1hdHJpeiBkZSAkKG4gXFx0aW1lcyBwKSQgdG9ybmEtc2UgJChwIFxcdGltZXMgbikkLCBjb20gbyBlbGVtZW50byBvcmlnaW5hbCBuYSBwb3Npw6fDo28gJChpLCBqKSQgbWlncmFuZG8gcGFyYSBhIHBvc2nDp8OjbyAkKGosIGkpJCwgY29uZm9ybWUgYSByZWdyYSAkKEFeVClfe2ppfSA9IGFfe2lqfSQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gZGUgb3RpbWl6YcOnw6NvIGRlIHBvcnRmw7NsaW8gZGUgaW52ZXN0aW1lbnRvcyBuYSBib2xzYSBkZSB2YWxvcmVzLCB2b2PDqiBkaXNww7VlIGRhIG1hdHJpeiBkZSB2YXJpw6JuY2lhLWNvdmFyacOibmNpYSAkXFxTaWdtYSQgcGFyYSB0csOqcyBhdGl2b3MgZmluYW5jZWlyb3MsIGRlc2NyaXRhIGNvbW86ICRcXFNpZ21hID0gXFxiZWdpbntwbWF0cml4fSAwLjA0ICYgMC4wMSAmIDAuMDIgXFxcXCAwLjAxICYgMC4wOSAmIDAuMDMgXFxcXCAwLjAyICYgMC4wMyAmIDAuMTYgXFxlbmR7cG1hdHJpeH0kLiBDb25zaWRlcmFuZG8gYXMgcHJvcHJpZWRhZGVzIGRhcyBlc3RydXR1cmFzIGVzcGVjaWFpcyBkZSBtYXRyaXplcyBlc3RhdMOtc3RpY2FzLCBxdWFsIMOpIGEgY2xhc3NpZmljYcOnw6NvIGNvcnJldGEgcGFyYSBhIG1hdHJpeiAkXFxTaWdtYSQgZSBzdWEgaW1wbGljYcOnw6NvIGNvbXB1dGFjaW9uYWw/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIG1hdHJpeiDDqSBlc3RyaXRhbWVudGUgdHJpYW5ndWxhciBzdXBlcmlvciwgbyBxdWUgZmFjaWxpdGEgbyBjw6FsY3VsbyBkbyBkZXRlcm1pbmFudGUuIiwgIkIiOiAiQSBtYXRyaXogw6kgXFxzaW3DqXRyaWNhICgkXFxTaWdtYSA9IFxcU2lnbWFeVCQpLCByZWR1emluZG8gbyBuw7ptZXJvIGRlIGVsZW1lbnRvcyDDum5pY29zIGRlICRuXjIkIHBhcmEgJG4obisxKS8yJC4iLCAiQyI6ICJBIG1hdHJpeiBuw6NvIHBvc3N1aSBzaW1ldHJpYSwgZXhpZ2luZG8gYSBkZWNvbXBvc2nDp8OjbyBjb21wbGV0YSBlbSAkbl4yJCBvcGVyYcOnw7VlcyBkZSBpbnZlcnPDo28uIiwgIkQiOiAiQSBtYXRyaXogw6kgZGlhZ29uYWwsIGluZGljYW5kbyBxdWUgdG9kb3Mgb3MgYXRpdm9zIHBvc3N1ZW0gY292YXJpw6JuY2lhIG51bGEgZW50cmUgc2kuIiwgIkUiOiAiQSBtYXRyaXogw6kgc2luZ3VsYXIsIGludmlhYmlsaXphbmRvIHF1YWxxdWVyIGPDoWxjdWxvIGRlIG90aW1pemHDp8OjbyBkZSByaXNjby4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk9ic2VydmUgYSBkaWFnb25hbCBwcmluY2lwYWwgZSB2ZXJpZmlxdWUgc2UgYSB0cmFuc3Bvc2nDp8OjbyBkYSBtYXRyaXogcmVzdWx0YSBuYSBwcsOzcHJpYSBtYXRyaXogb3JpZ2luYWwuIExlbWJyZS1zZSBkYSBlY29ub21pYSBkZSBtZW3Ds3JpYSBlbSBlc3RhdMOtc3RpY2EgY29tcHV0YWNpb25hbC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgbWF0cml6IGRlIHZhcmnDom5jaWEtY292YXJpw6JuY2lhICRcXFNpZ21hJCDDqSBkZWZpbmlkYSBjb21vIFxcc2ltw6l0cmljYSwgcG9pcyBhIGNvdmFyacOibmNpYSBlbnRyZSBvIGF0aXZvICRpJCBlIG8gYXRpdm8gJGokIMOpIGlndWFsIMOgIGNvdmFyacOibmNpYSBlbnRyZSBvIGF0aXZvICRqJCBlIG8gYXRpdm8gJGkkICgkXFxzaWdtYV97aWp9ID0gXFxzaWdtYV97aml9JCkuIE5hIHByw6F0aWNhLCBpc3RvIGltcGxpY2EgcXVlICRcXFNpZ21hID0gXFxTaWdtYV5UJC4gQSBzaW1ldHJpYSByZWR1eiBhIHJlZHVuZMOibmNpYSBkZSBkYWRvcyBkZSAkbl4yJCBwYXJhICRuKG4rMSkvMiQsIGVjb25vbWl6YW5kbyBtZW3Ds3JpYSBlIGFjZWxlcmFuZG8gYWxnb3JpdG1vcyBkZSBkZWNvbXBvc2nDp8OjbyBtYXRyaWNpYWwsIGNvbW8gYSBkZWNvbXBvc2nDp8OjbyBkZSBDaG9sZXNreSwgZnJlcXVlbnRlbWVudGUgdXNhZGEgZW0gZmluYW7Dp2FzLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQW8gcmVhbGl6YXIgdW1hIGFuw6FsaXNlIGRlIHJlZ3Jlc3PDo28gbcO6bHRpcGxhLCBvIHBlc3F1aXNhZG9yIGRlY2lkZSBwYXJ0aWNpb25hciBhIG1hdHJpeiBkZSBkYWRvcyAkWCQgKGRlIGRpbWVuc8OjbyAkbiBcXHRpbWVzIGskKSBlbSBkb2lzIGJsb2Nvcywgc2VwYXJhbmRvIGEgY29sdW5hIGRvIGludGVyY2VwdG8gZGFzIHZhcmnDoXZlaXMgZXhwbGljYXRpdmFzLiBTZWphICRYID0gW1xcbWF0aGJmezF9IFxcbWlkIFhfMV0kLCBvbmRlICRcXG1hdGhiZnsxfSQgw6kgdW0gdmV0b3IgZGUgZGltZW5zw6NvICRuIFxcdGltZXMgMSQgZSAkWF8xJCDDqSB1bWEgbWF0cml6IGRlICRuIFxcdGltZXMgKGstMSkkLiBRdWFsIGRhcyBzZWd1aW50ZXMgY29uZGnDp8O1ZXMgw6kgZXN0cml0YW1lbnRlIG5lY2Vzc8OhcmlhIHBhcmEgcXVlIGEgcGFydGnDp8OjbyBkZSBibG9jb3MgZSBhIHN1YnNlcXVlbnRlIG11bHRpcGxpY2HDp8OjbyBtYXRyaWNpYWwgJFheVCBYJCBzZWphbSBtYXRlbWF0aWNhbWVudGUgY29uc2lzdGVudGVzPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQXMgc3VibWF0cml6ZXMgZGV2ZW0gc2VyIHF1YWRyYWRhcywgaW5kZXBlbmRlbnRlbWVudGUgZG8gbsO6bWVybyB0b3RhbCBkZSBvYnNlcnZhw6fDtWVzICRuJC4iLCAiQiI6ICJPIG7Dum1lcm8gZGUgY29sdW5hcyBkYSBzdWJtYXRyaXogw6AgZXNxdWVyZGEgZGV2ZSBzZXIgaWd1YWwgYW8gbsO6bWVybyBkZSBsaW5oYXMgZGEgc3VibWF0cml6IMOgIGRpcmVpdGEgbm8gcHJvZHV0by4iLCAiQyI6ICJBcyBkaW1lbnPDtWVzIGRhcyBzdWJtYXRyaXplcyBkZXZlbSBzZXIgY29tcGF0w612ZWlzIGNvbSBhIMOhbGdlYnJhIGRlIGJsb2Nvcywgb25kZSBvIG7Dum1lcm8gZGUgY29sdW5hcyBkbyBwcmltZWlybyBibG9jbyBkZXZlIGlndWFsYXIgbyBuw7ptZXJvIGRlIGxpbmhhcyBkbyBibG9jbyBxdWUgbyBzdWNlZGUgZW0gbXVsdGlwbGljYcOnw7Vlcy4iLCAiRCI6ICJBIHBhcnRpw6fDo28gZGV2ZSByZXN1bHRhciBhcGVuYXMgZW0gbWF0cml6ZXMgZGlhZ29uYWlzIHBhcmEgZ2FyYW50aXIgYSByZXZlcnNpYmlsaWRhZGUgZG8gc2lzdGVtYS4iLCAiRSI6ICJBIG1hdHJpeiBvcmlnaW5hbCAkWCQgZGV2ZSBzZXIgb2JyaWdhdG9yaWFtZW50ZSBxdWFkcmFkYSAoJG49ayQpIHBhcmEgcGVybWl0aXIgbyBwYXJ0aWNpb25hbWVudG8uIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJQZW5zZSBuYXMgcmVncmFzIGRlIGNvbmZvcm1pZGFkZSBkaW1lbnNpb25hbCBkYSBtdWx0aXBsaWNhw6fDo28gZGUgbWF0cml6ZXMgYXBsaWNhZGFzIGEgY2FkYSBibG9jbyBpbmRpdmlkdWFsbWVudGUuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIG8gcGFydGljaW9uYW1lbnRvIGRlIGJsb2NvcyBlbSAkWF5UIFgkLCBhIMOhbGdlYnJhIG1hdHJpY2lhbCBleGlnZSBxdWUgYSBkaW1lbnPDo28gZGFzIHN1Ym1hdHJpemVzIHNlamEgcmVzcGVpdGFkYS4gQW8gcGFydGljaW9uYXIgJFggPSBbQSBccnZlcnQgQl0kLCBvIHByb2R1dG8gJFheVCBYJCByZXN1bHRhIGVtICRcXGJlZ2lue3BtYXRyaXh9IEFeVCBBICYgQV5UIEIgXFxcXCBCXlQgQSAmIEJeVCBCIFxcZW5ke3BtYXRyaXh9JC4gQSBjb25zaXN0w6puY2lhIGV4aWdlIHF1ZSBvIG7Dum1lcm8gZGUgY29sdW5hcyBkZSAkQV5UJCBjb2luY2lkYSBjb20gbyBuw7ptZXJvIGRlIGxpbmhhcyBkZSAkQSQsIGUgYXNzaW0gcG9yIGRpYW50ZS4gRXNzYSB0w6ljbmljYSDDqSBmdW5kYW1lbnRhbCBwYXJhIGFsZ29yaXRtb3MgZGUgY29tcHV0YcOnw6NvIGVzdGF0w61zdGljYSAnZGl2aWRpciBwYXJhIGNvbnF1aXN0YXInLCB0cmF0YW5kbyBzdWJjb25qdW50b3MgZGUgdmFyacOhdmVpcyBzZXBhcmFkYW1lbnRlLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gc2lzdGVtYSBkZSBtb25pdG9yYW1lbnRvIGRlIElvVCBlbSB1bWEgbGluaGEgZGUgbW9udGFnZW0sIHZvY8OqIGNvbGV0YSBkYWRvcyBkZSA0IHNlbnNvcmVzIGRlIHRlbXBlcmF0dXJhICgkVF8xLCBUXzIsIFRfMywgVF80JCkgcXVlIG9wZXJhbSBuYSBtZXNtYSBjw6JtYXJhIHTDqXJtaWNhLiBBcMOzcyBhIGFuw6FsaXNlIGluaWNpYWwgZG9zIGRhZG9zIGFtb3N0cmFpcywgdm9jw6ogY29uc3Ryw7NpIHVtYSBtYXRyaXogZGUgb2JzZXJ2YcOnw7VlcyAkQSQgZGUgb3JkZW0gJDQgXHRpbWVzIDMkLCBvbmRlIGNhZGEgbGluaGEgcmVwcmVzZW50YSB1bWEgbGVpdHVyYSB0ZW1wb3JhbCBlIGFzIGNvbHVuYXMgcmVwcmVzZW50YW0gb3Mgc2Vuc29yZXMuIEFvIGFwbGljYXIgbyBlc2NhbG9uYW1lbnRvLCBhIGZvcm1hIGVzY2Fsb25hZGEgY2Fuw7RuaWNhIGRhIG1hdHJpeiAkQSQgcmVzdWx0b3UgZW06ICQkIFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgJiAyIFxcXFwgMCAmIDEgJiAtMSBcXFxcIDAgJiAwICYgMCBcXFxcIDAgJiAwICYgMCBcXGVuZHtwbWF0cml4fSAkJCBDb25zaWRlcmFuZG8gbyBjb25jZWl0byBkZSBwb3N0byAocmFuaykgYXBsaWNhZG8gw6AgcmVkdW5kw6JuY2lhIGRlIGRhZG9zLCBxdWFsIMOpIGEgZGltZW5zw6NvIGVmZXRpdmEgZGUgaW5mb3JtYcOnw6NvIGNvbnRpZGEgbmVzdGVzIHNlbnNvcmVzPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyBwb3N0byDDqSA0LCBpbmRpY2FuZG8gcXVlIHRvZG9zIG9zIDQgc2Vuc29yZXMgZm9ybmVjZW0gaW5mb3JtYcOnw7VlcyBsaW5lYXJtZW50ZSBpbmRlcGVuZGVudGVzLiIsICJCIjogIk8gcG9zdG8gw6kgMywgaW5kaWNhbmRvIHF1ZSBhIG1hdHJpeiBwb3NzdWkgcG9zdG8gY29tcGxldG8gZSBuw6NvIGjDoSByZWR1bmTDom5jaWEuIiwgIkMiOiAiTyBwb3N0byDDqSAyLCBpbmRpY2FuZG8gcXVlIGV4aXN0ZW0gYXBlbmFzIDIgZGltZW5zw7VlcyBkZSBpbmZvcm1hw6fDo28gaW5kZXBlbmRlbnRlIGUgcmVkdW5kw6JuY2lhIGVudHJlIG9zIHNlbnNvcmVzLiIsICJEIjogIk8gcG9zdG8gw6kgMCwgcG9pcyBhIG1hdHJpeiBwb3NzdWkgZHVhcyBsaW5oYXMgbnVsYXMgYXDDs3MgbyBlc2NhbG9uYW1lbnRvLiIsICJFIjogIk8gcG9zdG8gw6kgMSwgcG9pcyBhcGVuYXMgYSBwcmltZWlyYSBjb2x1bmEgw6kgbGluZWFybWVudGUgaW5kZXBlbmRlbnRlIGRhcyBkZW1haXMuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIG8gcG9zdG8gJHIoQSkkIMOpIGRlZmluaWRvIHBlbG8gbsO6bWVybyBkZSBsaW5oYXMgbsOjbyBudWxhcyBuYSBmb3JtYSBlc2NhbG9uYWRhIGRhIG1hdHJpei4gUXVhbnRhcyBsaW5oYXMgbsOjbyBudWxhcyByZXN0YXJhbSBubyBzZXUgZXNjYWxvbmFtZW50bz8iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIk8gcG9zdG8gZGUgdW1hIG1hdHJpeiDDqSBkZWZpbmlkbyBwZWxhIGRpbWVuc8OjbyBkbyBzZXUgZXNwYcOnbyBkYXMgbGluaGFzIG91IGNvbHVuYXMsIHF1ZSBjb3JyZXNwb25kZSBhbyBuw7ptZXJvIGRlIHBpdsO0cyBvdSBsaW5oYXMgbsOjbyBudWxhcyBuYSBzdWEgZm9ybWEgZXNjYWxvbmFkYSByZWR1emlkYS4gTm8gY2FzbyBhcHJlc2VudGFkbywgYXDDs3MgYXMgb3BlcmHDp8O1ZXMgZWxlbWVudGFyZXMsIGEgbWF0cml6IHJlc3VsdGFudGUgcG9zc3VpIGV4YXRhbWVudGUgZHVhcyBsaW5oYXMgbsOjbyBudWxhcy4gTG9nbywgJHIoQSkgPSAyJC4gSXNzbyBzaWduaWZpY2EgcXVlLCBlbWJvcmEgdGVuaGFtb3MgNCBzZW5zb3JlcyAobGluaGFzKSBvdSAzIHZhcmnDoXZlaXMgKGNvbHVuYXMpLCBhIGluZm9ybWHDp8OjbyBjb250aWRhIG5lc3RlcyBkYWRvcyBlc3TDoSByZXN0cml0YSBhIHVtIHBsYW5vIGJpZGltZW5zaW9uYWwuIEV4aXN0ZSByZWR1bmTDom5jaWEsIHBvaXMgYSB0ZXJjZWlyYSB2YXJpw6F2ZWwgcG9kZSBzZXIgZXNjcml0YSBjb21vIHVtYSBjb21iaW5hw6fDo28gbGluZWFyIGRhcyBkdWFzIHByaW1laXJhcyAoJENfMyA9IDJDXzEgLSAxQ18yJCkuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlbnNhaW8gY2zDrW5pY28sIHBlc3F1aXNhZG9yZXMgb3JnYW5pemFyYW0gdW1hIG1hdHJpeiBkZSBkYWRvcyAkRCQgY29tIGRpbWVuc8OjbyAkMyBcdGltZXMgMyQgcmVmZXJlbnRlIGEgdHLDqnMgbWFyY2Fkb3JlcyBiaW9sw7NnaWNvcyBlbSB0csOqcyBwYWNpZW50ZXMgZGlzdGludG9zLiBBbyBjYWxjdWxhciBvIHBvc3RvIGRlc3RhIG1hdHJpeiwgb3MgcGVzcXVpc2Fkb3JlcyBkZXNjb2JyaXJhbSBxdWUgJHIoRCkgPCAzJC4gTyBxdWUgZXNzYSBjYXJhY3RlcsOtc3RpY2EgZXN0YXTDrXN0aWNhIGltcGxpY2EgbmEgaW50ZXJwcmV0YcOnw6NvIGRvcyBkYWRvcz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgbWF0cml6ICREJCBwb3NzdWkgZGV0ZXJtaW5hbnRlIG7Do28gbnVsbywgbG9nbywgb3MgbWFyY2Fkb3JlcyBzw6NvIHRvZG9zIGxpbmVhcm1lbnRlIGluZGVwZW5kZW50ZXMuIiwgIkIiOiAiQSBtYXRyaXogJEQkIMOpIHNpbmd1bGFyLCBpbmRpY2FuZG8gcXVlIHBlbG8gbWVub3MgdW0gZG9zIG1hcmNhZG9yZXMgYmlvbMOzZ2ljb3Mgw6kgdW1hIGNvbWJpbmHDp8OjbyBsaW5lYXIgZG9zIG91dHJvcyBkb2lzLCByZWR1emluZG8gYSB2YXJpYWJpbGlkYWRlIMO6bmljYSBjYXB0dXJhZGEuIiwgIkMiOiAiT3MgZGFkb3MgY29sZXRhZG9zIHBvc3N1ZW0gZXJyb3MgZGUgbWVkacOnw6NvLCBwb2lzIG8gcG9zdG8gZGUgdW1hIG1hdHJpeiBkZSBkYWRvcyByZWFpcyBkZXZlIHNlciBzZW1wcmUgaWd1YWwgYW8gbsO6bWVybyBkZSBjb2x1bmFzLiIsICJEIjogIk8gdGFtYW5obyBhbW9zdHJhbCAkbj0zJCDDqSBzdWZpY2llbnRlIHBhcmEgZ2FyYW50aXIgcXVlIG8gcG9zdG8gc2VqYSBzZW1wcmUgbcOheGltby4iLCAiRSI6ICJBIG1hdHJpeiAkRCQgw6kgb3J0b2dvbmFsLCBwb2lzIHNldSBwb3N0byDDqSBtZW5vciBxdWUgYSBkaW1lbnPDo28gbcOheGltYS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIlJlZmxpdGEgc29icmUgYSByZWxhw6fDo28gZW50cmUgbyBwb3N0byBkZSB1bWEgbWF0cml6IHF1YWRyYWRhIGUgYSBzdWEgaW52ZXJ0aWJpbGlkYWRlLiBPIHF1ZSBzaWduaWZpY2EgdW1hIG1hdHJpeiBuw6NvIHBvc3N1aXIgcG9zdG8gY29tcGxldG8/IiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIHVtYSBtYXRyaXogcXVhZHJhZGEgZGUgb3JkZW0gJG4gXHRpbWVzIG4kLCB0ZXIgcG9zdG8gY29tcGxldG8gc2lnbmlmaWNhICRyKEQpID0gbiQuIFF1YW5kbyAkcihEKSA8IG4kLCBhIG1hdHJpeiDDqSBkaXRhIHNpbmd1bGFyIG91IG7Do28gaW52ZXJzw612ZWwuIEVzdGF0aXN0aWNhbWVudGUsIGlzc28gaW1wbGljYSBxdWUgb3MgdmV0b3JlcyBsaW5oYSBvdSBjb2x1bmEgc8OjbyBsaW5lYXJtZW50ZSBkZXBlbmRlbnRlcy4gRW0gdGVybW9zIGRlIGVuc2Fpb3MgY2zDrW5pY29zLCBpc3NvIHNpZ25pZmljYSBxdWUgdW0gbWFyY2Fkb3IgYmlvbMOzZ2ljbyBuw6NvIGVzdMOhIHRyYXplbmRvIGluZm9ybWHDp8OjbyBub3ZhLCBzZW5kbyByZWR1bmRhbnRlIGVtIHJlbGHDp8OjbyBhb3MgZGVtYWlzIGrDoSBtZWRpZG9zLCBvIHF1ZSBhZmV0YSBhIGFuw6FsaXNlIG11bHRpdmFyaWFkYSBlIGEgZXN0YWJpbGlkYWRlIGRlIGVzdGltYWRvcmVzIGNvbW8gbyBkZSByZWdyZXNzw6NvLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gbW9kZWxvcyBsaW5lYXJlcywgZnJlcXVlbnRlbWVudGUgdXRpbGl6YW1vcyBhIG1hdHJpeiBkZSBwcm9qZcOnw6NvICRQID0gWChYJ1gpXnstMX1YJyQgcGFyYSBwcm9qZXRhciB2ZXRvcmVzIG9ic2VydmFkb3Mgbm8gZXNwYcOnbyBjb2x1bmEgZGUgJFgkLiBTYWJlbmRvIHF1ZSBlc3RhIG1hdHJpeiAkUCQgw6kgaWRlbXBvdGVudGUsIHF1YWwgZGFzIGFsdGVybmF0aXZhcyBhYmFpeG8gZGVzY3JldmUgY29ycmV0YW1lbnRlIG8gY29tcG9ydGFtZW50byBkb3MgYXV0b3ZhbG9yZXMgJFxcbGFtYmRhJCBhc3NvY2lhZG9zIGEgcXVhbHF1ZXIgbWF0cml6IGlkZW1wb3RlbnRlPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiT3MgYXV0b3ZhbG9yZXMgZGUgdW1hIG1hdHJpeiBpZGVtcG90ZW50ZSBwb2RlbSBhc3N1bWlyIHF1YWxxdWVyIHZhbG9yIHJlYWwsIGRlcGVuZGVuZG8gZGEgZGltZW5zw6NvIGRhIG1hdHJpei4iLCAiQiI6ICJPcyBhdXRvdmFsb3JlcyBkZSB1bWEgbWF0cml6IGlkZW1wb3RlbnRlIHPDo28gZXN0cml0YW1lbnRlIG1haW9yZXMgcXVlIDEuIiwgIkMiOiAiT3MgYXV0b3ZhbG9yZXMgZGUgdW1hIG1hdHJpeiBpZGVtcG90ZW50ZSBzw6NvIG9icmlnYXRvcmlhbWVudGUgMCBvdSAxLiIsICJEIjogIk9zIGF1dG92YWxvcmVzIGRlIHVtYSBtYXRyaXogaWRlbXBvdGVudGUgc8OjbyBzZW1wcmUgaWd1YWlzIMOgIHN1YSBtw6lkaWEgYXJpdG3DqXRpY2EuIiwgIkUiOiAiT3MgYXV0b3ZhbG9yZXMgZGUgdW1hIG1hdHJpeiBpZGVtcG90ZW50ZSBkZXZlbSBzZXIgbmVnYXRpdm9zLCBwb2lzIHJlcHJlc2VudGFtIHVtYSBjb250cmHDp8OjbyBlc3BhY2lhbC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIkNvbnNpZGVyZSBhIGRlZmluacOnw6NvIGRlIGF1dG92YWxvciAkQXYgPSBcXGxhbWJkYSB2JCBlIGEgcHJvcHJpZWRhZGUgJEFeMiA9IEEkLiBPIHF1ZSBhY29udGVjZSBxdWFuZG8gdm9jw6ogYXBsaWNhICRBJCBkdWFzIHZlemVzIGFvIHZldG9yIGF1dG92ZXRvciAkdiQ/IiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQZWxhIGRlZmluacOnw6NvIGRlIGF1dG92YWxvciwgdGVtb3MgJFB2ID0gXFxsYW1iZGEgdiQuIENvbW8gYSBtYXRyaXogw6kgaWRlbXBvdGVudGUsICRQXjIgPSBQJC4gUG9ydGFudG8sICRQKFB2KSA9IFB2JCwgbyBxdWUgaW1wbGljYSAkUChcXGxhbWJkYSB2KSA9IFxcbGFtYmRhIHYkLiBTdWJzdGl0dWluZG8sICRcXGxhbWJkYSAoUHYpID0gXFxsYW1iZGEgdiQsIG91IHNlamEsICRcXGxhbWJkYV4yIHYgPSBcXGxhbWJkYSB2JC4gSXNzbyByZXN1bHRhIG5hIGVxdWHDp8OjbyBhbGfDqWJyaWNhICRcXGxhbWJkYV4yIC0gXFxsYW1iZGEgPSAwJCwgY3VqYXMgcmHDrXplcyBzw6NvICRcXGxhbWJkYSA9IDAkIG91ICRcXGxhbWJkYSA9IDEkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGFkYSB1bWEgbWF0cml6IFxcc2ltw6l0cmljYSAkQV97KG4pfSQsIGEgZGVjb21wb3Npw6fDo28gZXNwZWN0cmFsIHBlcm1pdGUgZXNjcmV2w6otbGEgY29tbyAkQSA9IFxcc3VtX3tpPTF9Xm4gXFxsYW1iZGFfaSB1X2kgdV9pJyQuIFNlIGVzdGEgbWF0cml6IHJlcHJlc2VudGEgdW1hIG1hdHJpeiBkZSBjb3ZhcmnDom5jaWEgZGUgdW0gY29uanVudG8gZGUgZGFkb3MsIHF1YWwgw6kgYSBpbnRlcnByZXRhw6fDo28gZ2VvbcOpdHJpY2EgZG9zIGF1dG92ZXRvcmVzICR1X2kkIG5hIGFuw6FsaXNlIGVzdGF0w61zdGljYT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk9zIGF1dG92ZXRvcmVzIHJlcHJlc2VudGFtIGEgbWFnbml0dWRlIHRvdGFsIGRhIHZhcmnDom5jaWEgZXhwbGljYWRhIHBlbG9zIGNvbXBvbmVudGVzLiIsICJCIjogIk9zIGF1dG92ZXRvcmVzIGRlZmluZW0gYXMgZGlyZcOnw7VlcyBwcmluY2lwYWlzIChlaXhvcyBvcnRvZ29uYWlzKSBkbyBzaXN0ZW1hIGRlIGRhZG9zIG5vIGVzcGHDp28gbXVsdGlkaW1lbnNpb25hbC4iLCAiQyI6ICJPcyBhdXRvdmV0b3JlcyBzw6NvIHNlbXByZSB2ZXRvcmVzIHVuaXTDoXJpb3MgcXVlIG7Do28gYWZldGFtIGEgZ2VvbWV0cmlhIGRhIGRpc3BlcnPDo28gZG9zIGRhZG9zLiIsICJEIjogIk9zIGF1dG92ZXRvcmVzIGluZGljYW0gYSBjb3JyZWxhw6fDo28gbcOpZGlhIGVudHJlIHRvZGFzIGFzIHZhcmnDoXZlaXMgb2JzZXJ2YWRhcy4iLCAiRSI6ICJPcyBhdXRvdmV0b3JlcyBjb2luY2lkZW0gY29tIG9zIHJlc8OtZHVvcyBkZSB1bWEgcmVncmVzc8OjbyBsaW5lYXIgc2ltcGxlcy4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIlBlbnNlIG5vIHByb2Nlc3NvIGRlIHJvdGHDp8OjbyBkZSBlaXhvcy4gQSBkZWNvbXBvc2nDp8OjbyBlc3BlY3RyYWwgZWZldHVhIHVtYSBtdWRhbsOnYSBkZSBiYXNlIHBhcmEgdW0gc2lzdGVtYSBvbmRlIGEgbWF0cml6IHNlIHRvcm5hIGRpYWdvbmFsLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTmEgZGVjb21wb3Npw6fDo28gZXNwZWN0cmFsICRBID0gVSBcXHRleHR7ZGlhZ30oXFxsYW1iZGEpIFUnJCwgYSBtYXRyaXogJFUkIMOpIHVtYSBtYXRyaXogb3J0b2dvbmFsIGN1amFzIGNvbHVuYXMgc8OjbyBvcyBhdXRvdmV0b3JlcyAkdV9pJC4gRXNzZXMgdmV0b3JlcyBmb3JtYW0gdW1hIGJhc2Ugb3J0b25vcm1hbCBxdWUsIHF1YW5kbyBhcGxpY2FkYSBhb3MgZGFkb3Mgb3JpZ2luYWlzLCByb3RhY2lvbmEgbyBzaXN0ZW1hIGRlIGNvb3JkZW5hZGFzIHBhcmEgb3MgZWl4b3MgcHJpbmNpcGFpcyBkZSBtw6F4aW1hIHZhcmlhYmlsaWRhZGUsIG9uZGUgYSB2YXJpw6JuY2lhIMOpIGRhZGEgcGVsb3MgYXV0b3ZhbG9yZXMgJFxcbGFtYmRhX2kkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfV0sICJxdWVzdG9lc19kaXNjdXJzaXZhcyI6IFt7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgYSBtYXRyaXogZGUgZGFkb3MgJFhfeygzIFxcdGltZXMgMil9JCBhYmFpeG8sIHF1ZSBjb250w6ltIGFzIG5vdGFzIGRlIDMgYWx1bm9zIGVtIDIgcHJvdmFzIGRpc3RpbnRhczogJCRYID0gXFxiZWdpbntwbWF0cml4fSA3LjUgJiA4LjAgXFxcXCA2LjAgJiA5LjUgXFxcXCA5LjAgJiA3LjAgXFxlbmR7cG1hdHJpeH0kJCBFeHBsaXF1ZSwgdXRpbGl6YW5kbyBhIG5vdGHDp8OjbyBtYXRyaWNpYWwgJGFfe2lqfSQsIHF1YWwgbyB2YWxvciBkYSBub3RhIG5hIHByb3ZhIDIgZG8gYWx1bm8gMiBlIGNhbGN1bGUgYSBzb21hIGRlIHRvZGFzIGFzIG5vdGFzIGNvbnRpZGFzIG5hIG1hdHJpei4iLCAiZGljYSI6ICJPIGFsdW5vIDIgY29ycmVzcG9uZGUgw6AgbGluaGEgJGk9MiQuIEEgcHJvdmEgMiBjb3JyZXNwb25kZSDDoCBjb2x1bmEgJGo9MiQuIFV0aWxpemUgYSBub3Rhw6fDo28gZGUgc29tYXTDs3JpbyAkXFxzdW1fe2k9MX1eezN9IFxcc3VtX3tqPTF9XnsyfSBhX3tpan0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBJZGVudGlmaWNhw6fDo28gZG8gZWxlbWVudG86IE8gYWx1bm8gMiBlc3TDoSBuYSBzZWd1bmRhIGxpbmhhICgkaT0yJCkgZSBhIHByb3ZhIDIgZXN0w6EgbmEgc2VndW5kYSBjb2x1bmEgKCRqPTIkKS4gTG9nbywgbyBlbGVtZW50byDDqSAkYV97MjJ9ID0gOS41JC4iLCAiMi4gQ8OhbGN1bG8gZGEgc29tYTogRGV2ZW1vcyBzb21hciB0b2RvcyBvcyBlbGVtZW50b3MgZGEgbWF0cml6OiAkJFMgPSA3LjUgKyA4LjAgKyA2LjAgKyA5LjUgKyA5LjAgKyA3LjAkJCIsICIzLiBSZWFsaXphw6fDo28gZGEgYXJpdG3DqXRpY2E6ICQ3LjUgKyA4LjAgPSAxNS41JDsgJDYuMCArIDkuNSA9IDE1LjUkOyAkOS4wICsgNy4wID0gMTYuMCQuIiwgIjQuIFJlc3VsdGFkbyBmaW5hbDogJDE1LjUgKyAxNS41ICsgMTYuMCA9IDQ3LjAkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogNDcuMH0sIHsiZW51bmNpYWRvIjogIkRhZGEgYSBkZWZpbmnDp8OjbyBkZSB1bWEgbWF0cml6ICRBX3sobSBcXHRpbWVzIG4pfSQsIGRlbW9uc3RyZSBmb3JtYWxtZW50ZSBhIGRpZmVyZW7Dp2EgZW50cmUgdW0gdmV0b3IgbGluaGEgJHZfTCQgZGUgZGltZW5zw6NvICQoMSBcXHRpbWVzIDMpJCBlIHVtIHZldG9yIGNvbHVuYSAkdl9DJCBkZSBkaW1lbnPDo28gJCgzIFxcdGltZXMgMSkkLCB1dGlsaXphbmRvIHVtYSBtYXRyaXogZ2Vuw6lyaWNhIGRlIDMgZWxlbWVudG9zICR4XzEsIHhfMiwgeF8zJC4iLCAiZGljYSI6ICJDb25zaWRlcmUgbyBhcnJhbmpvIGRvcyBlbGVtZW50b3MgbmFzIHBvc2nDp8O1ZXMgJGFfezFqfSQgcGFyYSBvIHZldG9yIGxpbmhhIGUgJGFfe2kxfSQgcGFyYSBvIHZldG9yIGNvbHVuYS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gVmV0b3IgbGluaGE6IFBvc3N1aSBhcGVuYXMgdW1hIGxpbmhhIGUgdHLDqnMgY29sdW5hcy4gTm90YcOnw6NvOiAkdl9MID0gXFxiZWdpbntwbWF0cml4fSB4XzEgJiB4XzIgJiB4XzMgXFxlbmR7cG1hdHJpeH0kLiIsICIyLiBWZXRvciBjb2x1bmE6IFBvc3N1aSB0csOqcyBsaW5oYXMgZSBhcGVuYXMgdW1hIGNvbHVuYS4gTm90YcOnw6NvOiAkdl9DID0gXFxiZWdpbntwbWF0cml4fSB4XzEgXFxcXCB4XzIgXFxcXCB4XzMgXFxlbmR7cG1hdHJpeH0kLiIsICIzLiBDb25jbHVzw6NvOiBFbnF1YW50byBvIHZldG9yIGxpbmhhIGVzdGVuZGUtc2UgaG9yaXpvbnRhbG1lbnRlICgkbj0zJCksIG8gdmV0b3IgY29sdW5hIGVzdGVuZGUtc2UgdmVydGljYWxtZW50ZSAoJG09MyQpLiBNYXRlbWF0aWNhbWVudGUsIGVzdGFzIGVzdHJ1dHVyYXMgc8OjbyBkaXN0aW50YXMgbWVzbW8gY29udGVuZG8gb3MgbWVzbW9zIGVzY2FsYXJlcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBleHBlcmltZW50byBkZSBvdGltaXphw6fDo28gZGUgcHJvY2Vzc28gaW5kdXN0cmlhbCwgdGVtb3MgNCBsb3RlcyBkZSBwcm9kdcOnw6NvLiBQYXJhIGNhZGEgbG90ZSwgbWVkaW1vcyBhIGVmaWNpw6puY2lhICh2YXJpw6F2ZWwgMSkgZSBvIGN1c3RvICh2YXJpw6F2ZWwgMikuIENvbnN0cnVhIGEgbWF0cml6ICRNJCBxdWUgcmVwcmVzZW50YSBlc3NlcyBkYWRvcywgc2FiZW5kbyBxdWUgb3MgdmFsb3JlcyBzw6NvOiBMb3RlIDEgKDkwLCAxMDApLCBMb3RlIDIgKDg1LCAxMTApLCBMb3RlIDMgKDk1LCA5NSkgZSBMb3RlIDQgKDg4LCAxMDUpLiBFbSBzZWd1aWRhLCBhcHJlc2VudGUgYSBkaW1lbnPDo28gZGVzc2EgbWF0cml6LiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgY2FkYSBsb3RlIGRldmUgb2N1cGFyIHVtYSBsaW5oYSBkYSBtYXRyaXouIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIE1vbnRhZ2VtIGRhcyBsaW5oYXM6IENhZGEgbG90ZSByZXByZXNlbnRhIHVtYSBsaW5oYSBkYSBtYXRyaXogJE0kLiIsICIyLiBPcmdhbml6YcOnw6NvIGRvcyBlbGVtZW50b3M6ICQkTSA9IFxcYmVnaW57cG1hdHJpeH0gOTAgJiAxMDAgXFxcXCA4NSAmIDExMCBcXFxcIDk1ICYgOTUgXFxcXCA4OCAmIDEwNSBcXGVuZHtwbWF0cml4fSQkIiwgIjMuIERlZmluacOnw6NvIGRhIGRpbWVuc8OjbzogQSBtYXRyaXogcG9zc3VpIDQgbGluaGFzICgkbT00JCkgZSAyIGNvbHVuYXMgKCRuPTIkKS4gUG9ydGFudG8sIGEgZGltZW5zw6NvIMOpICQoNCBcXHRpbWVzIDIpJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJTZWphIGEgbWF0cml6IGRlIGN1c3RvcyBkZSBwcm9kdcOnw6NvICRBX3soMiBcdGltZXMgMyl9JCBlIGEgbWF0cml6IGRlIGRlbWFuZGEgZGUgaW5zdW1vcyAkQl97KDMgXHRpbWVzIDIpfSQgZGVmaW5pZGFzIHBvcjogJEEgPSBcXGJlZ2lue3BtYXRyaXh9IDIgJiAxICYgMyBcXFxcIDEgJiAwICYgMiBcXGVuZHtwbWF0cml4fSQgZSAkQiA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAyICYgMSBcXFxcIDAgJiAxIFxcZW5ke3BtYXRyaXh9JC4gQ2FsY3VsZSBvIHByb2R1dG8gbWF0cmljaWFsICRDID0gQUIkIGUgaW50ZXJwcmV0ZSBvIHF1ZSBvIGVsZW1lbnRvICRjX3sxMX0kIHJlcHJlc2VudGEgbm8gY29udGV4dG8gZGUgw6FsZ2VicmEgbWF0cmljaWFsLiIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSAkY197aWt9ID0gXFxzdW1fe2o9MX1eezN9IGFfe2lqfWJfe2prfSQgcGFyYSBjYWRhIHBvc2nDp8OjbyBkYSBtYXRyaXogcmVzdWx0YW50ZSAkQ197KDIgXHRpbWVzIDIpfSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhcmEgbyBlbGVtZW50byAkY197MTF9JDogJCgyIFxcdGltZXMgMSkgKyAoMSBcXHRpbWVzIDIpICsgKDMgXFx0aW1lcyAwKSA9IDIgKyAyICsgMCA9IDQkLiIsICJQYXJhIG8gZWxlbWVudG8gJGNfezEyfSQ6ICQoMiBcXHRpbWVzIDApICsgKDEgXFx0aW1lcyAxKSArICgzIFxcdGltZXMgMSkgPSAwICsgMSArIDMgPSA0JC4iLCAiUGFyYSBvIGVsZW1lbnRvICRjX3syMX0kOiAkKDEgXFx0aW1lcyAxKSArICgwIFxcdGltZXMgMikgKyAoMiBcXHRpbWVzIDApID0gMSArIDAgKyAwID0gMSQuIiwgIlBhcmEgbyBlbGVtZW50byAkY197MjJ9JDogJCgxIFxcdGltZXMgMCkgKyAoMCBcXHRpbWVzIDEpICsgKDIgXFx0aW1lcyAxKSA9IDAgKyAwICsgMiA9IDIkLiIsICJBIG1hdHJpeiByZXN1bHRhbnRlIMOpICRDID0gXFxiZWdpbntwbWF0cml4fSA0ICYgNCBcXFxcIDEgJiAyIFxcZW5ke3BtYXRyaXh9JC4iLCAiTyBlbGVtZW50byAkY197MTF9PTQkIMOpIGEgc29tYSBwb25kZXJhZGEgZGEgcHJpbWVpcmEgbGluaGEgZGUgQSBwZWxhIHByaW1laXJhIGNvbHVuYSBkZSBCLCByZXByZXNlbnRhbmRvIGEgaW50ZXJhw6fDo28gZGlyZXRhIGVudHJlIG9zIGN1c3RvcyBkbyBwcmltZWlybyB0aXBvIGUgYSBkZW1hbmRhIGRvIHByaW1laXJvIGdydXBvLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBxdWUgZW0gdW0gZXhwZXJpbWVudG8gZGUgZWNvbm9taWEsIHZvY8OqIHBvc3N1aSB1bSB2ZXRvciBkZSBwcmXDp29zICRQX3soMSBcdGltZXMgMyl9ID0gWzEwLCA1LCAyXSQgZSB1bSB2ZXRvciBkZSBxdWFudGlkYWRlcyAkUV97KDMgXHRpbWVzIDEpfSA9IFsyLCA0LCAxMF1eVCQuIERlbW9uc3RyZSBtYXRlbWF0aWNhbWVudGUsIHV0aWxpemFuZG8gbyBmb3JtYWxpc21vIGRlIHRyYW5zcG9zacOnw6NvIGUgcHJvZHV0byBtYXRyaWNpYWwsIGNvbW8gY2FsY3VsYXIgbyBjdXN0byB0b3RhbCAkViA9IFBRJC4iLCAiZGljYSI6ICJPIGN1c3RvIHRvdGFsIMOpIHVtIGVzY2FsYXIuIE5vdGUgcXVlICRQJCDDqSAkKDEgXFx0aW1lcyAzKSQgZSAkUSQgw6kgJCgzIFxcdGltZXMgMSkkLiBPIHByb2R1dG8gcmVzdWx0YXLDoSBlbSB1bWEgbWF0cml6ICQoMSBcXHRpbWVzIDEpJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRGVmaW5pbW9zICRQID0gWzEwLCA1LCAyXSQgZSAkUSA9IFxcYmVnaW57cG1hdHJpeH0gMiBcXFxcIDQgXFxcXCAxMCBcXGVuZHtwbWF0cml4fSQuIiwgIk8gcHJvZHV0byBtYXRyaWNpYWwgJFYgPSBQUSQgw6kgY2FsY3VsYWRvIGNvbW86ICRWID0gKDEwIFxcdGltZXMgMikgKyAoNSBcXHRpbWVzIDQpICsgKDIgXFx0aW1lcyAxMCkkLiIsICJDYWxjdWxhbmRvIG9zIHByb2R1dG9zOiAkViA9IDIwICsgMjAgKyAyMCQuIiwgIlJlc3VsdGFkbyBmaW5hbDogJFYgPSA2MCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiA2MC4wfSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIHNvYiBhIMOzdGljYSBkYSDDoWxnZWJyYSBtYXRyaWNpYWwsIHBvciBxdWUgYSBtdWx0aXBsaWNhw6fDo28gZGUgdW1hIG1hdHJpeiAkQV97KG4gXFx0aW1lcyBuKX0kIHBlbGEgbWF0cml6IGlkZW50aWRhZGUgJElfbiQgcmVzdWx0YSBuYSBwcsOzcHJpYSBtYXRyaXogJEEkLiBVdGlsaXplIGEgZGVmaW5pw6fDo28gZG8gJFxcZGVsdGEkIGRlIEtyb25lY2tlciBwYXJhIGp1c3RpZmljYXIuIiwgImRpY2EiOiAiQ29uc2lkZXJlIG8gcHJvZHV0byAkQyA9IEFJX24kIG9uZGUgJGNfe2lrfSA9IFxcc3VtX3tqPTF9XntufSBhX3tpan0gXFxkZWx0YV97amt9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSBkZWZpbmnDp8OjbyBkYSBpZGVudGlkYWRlIMOpICRJX24gPSBbXFxkZWx0YV97amt9XSQsIG9uZGUgJFxcZGVsdGFfe2prfSA9IDEkIHNlICRqPWskIGUgJDAkIGNhc28gY29udHLDoXJpby4iLCAiTyBwcm9kdXRvICRDID0gQUkkIHRlbSBlbGVtZW50b3MgJGNfe2lrfSA9IFxcc3VtX3tqPTF9XntufSBhX3tpan0gXFxkZWx0YV97amt9JC4iLCAiQ29tbyAkXFxkZWx0YV97amt9JCDDqSB6ZXJvIHBhcmEgdG9kbyAkaiBcXG5lcSBrJCwgbyBzb21hdMOzcmlvIGNvbGFwc2EgYXBlbmFzIHBhcmEgbyB0ZXJtbyBvbmRlICRqPWskLiIsICJBc3NpbSwgJGNfe2lrfSA9IGFfe2lrfSBcXHRpbWVzIDEgPSBhX3tpa30kLiIsICJDb21vICRjX3tpa30gPSBhX3tpa30kIHBhcmEgdG9kbyAkaSwgayQsIGNvbmNsdcOtbW9zIHF1ZSAkQUkgPSBBJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgYSBtYXRyaXogJEEgPSBcXGJlZ2lue3BtYXRyaXh9IDIgJiAxICYgNCBcXFxcIDEgJiAzICYgNSBcXFxcIDQgJiA1ICYgNiBcXGVuZHtwbWF0cml4fSQuIFZlcmlmaXF1ZSBzZSBhIG1hdHJpeiAkQSQgw6kgXFxzaW3DqXRyaWNhLiBFbSBzZWd1aWRhLCBjYWxjdWxlIGEgbWF0cml6IHRyYW5zcG9zdGEgJEFeVCQgZSBleHBsaXF1ZSBxdWFsIHByb3ByaWVkYWRlIGdhcmFudGUgcXVlICRBID0gQV5UJCBuZXN0ZSBjYXNvLCByZWxhY2lvbmFuZG8gYW9zIGVsZW1lbnRvcyAkYV97aWp9JCBlICRhX3tqaX0kLiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgdW1hIG1hdHJpeiDDqSBcXHNpbcOpdHJpY2Egc2UsIHBhcmEgdG9kbyAkaSQgZSAkaiQsICRhX3tpan0gPSBhX3tqaX0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXJhIHZlcmlmaWNhciBhIHNpbWV0cmlhLCBjYWxjdWxhbW9zIGEgdHJhbnNwb3N0YSAkQV5UJCB0cm9jYW5kbyBhcyBsaW5oYXMgcGVsYXMgY29sdW5hcy4iLCAiQSBwcmltZWlyYSBsaW5oYSAoMiwgMSwgNCkgdG9ybmEtc2UgYSBwcmltZWlyYSBjb2x1bmEgZGUgJEFeVCQuIiwgIkEgc2VndW5kYSBsaW5oYSAoMSwgMywgNSkgdG9ybmEtc2UgYSBzZWd1bmRhIGNvbHVuYSBkZSAkQV5UJC4iLCAiQSB0ZXJjZWlyYSBsaW5oYSAoNCwgNSwgNikgdG9ybmEtc2UgYSB0ZXJjZWlyYSBjb2x1bmEgZGUgJEFeVCQuIiwgIlJlc3VsdGFuZG8gZW06ICRBXlQgPSBcXGJlZ2lue3BtYXRyaXh9IDIgJiAxICYgNCBcXFxcIDEgJiAzICYgNSBcXFxcIDQgJiA1ICYgNiBcXGVuZHtwbWF0cml4fSQuIiwgIkNvbW8gJEEgPSBBXlQkLCBjb25maXJtYW1vcyBxdWUgYSBtYXRyaXogw6kgXFxzaW3DqXRyaWNhIHBvaXMgJGFfezEyfT1hX3syMX09MSQsICRhX3sxM309YV97MzF9PTQkIGUgJGFfezIzfT1hX3szMn09NSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiU2VqYSBhIG1hdHJpeiAkTSQgcGFydGljaW9uYWRhIGVtIGJsb2NvczogJE0gPSBcXGJlZ2lue3BtYXRyaXh9IEEgJiBCIFxcXFwgQyAmIEQgXFxlbmR7cG1hdHJpeH0kLCBvbmRlICRBID0gXFxiZWdpbntwbWF0cml4fSAxICYgMiBcXGVuZHtwbWF0cml4fSQsICRCID0gXFxiZWdpbntwbWF0cml4fSAzIFxcZW5ke3BtYXRyaXh9JCwgJEMgPSBcXGJlZ2lue3BtYXRyaXh9IDQgXFxlbmR7cG1hdHJpeH0kIGUgJEQgPSBcXGJlZ2lue3BtYXRyaXh9IDUgXFxlbmR7cG1hdHJpeH0kLiBTZSBtdWx0aXBsaWNhcm1vcyAkTSQgcG9yIHVtIHZldG9yIGNvbHVuYSAkdiQgcGFydGljaW9uYWRvIGRlIGZvcm1hIGNvbXBhdMOtdmVsICR2ID0gXFxiZWdpbntwbWF0cml4fSB2XzEgXFxcXCB2XzIgXFxlbmR7cG1hdHJpeH0kLCBvbmRlICR2XzEkIHRlbSBkaW1lbnPDo28gMiBlICR2XzIkIHRlbSBkaW1lbnPDo28gMSwgZGVzY3JldmEgbyByZXN1bHRhZG8gZGEgbXVsdGlwbGljYcOnw6NvICRNdiQgZW0gdGVybW9zIGRvcyBibG9jb3MgJEEsIEIsIEMsIEQkLiIsICJkaWNhIjogIlV0aWxpemUgYSByZWdyYSBkZSBtdWx0aXBsaWNhw6fDo28gZGUgbWF0cml6ZXMgcGFydGljaW9uYWRhczogJE12ID0gXFxiZWdpbntwbWF0cml4fSBBdl8xICsgQnZfMiBcXFxcIEN2XzEgKyBEdl8yIFxcZW5ke3BtYXRyaXh9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGVsYSByZWdyYSBkZSBtdWx0aXBsaWNhw6fDo28gZGUgYmxvY29zLCBvIHJlc3VsdGFkbyDDqSB1bSB2ZXRvciBwYXJ0aWNpb25hZG8gZW0gZG9pcyBzdWJ2ZXRvcmVzLiIsICJPIHByaW1laXJvIGNvbXBvbmVudGUgw6kgZGFkbyBwb3IgJEF2XzEgKyBCdl8yID0gXFxiZWdpbntwbWF0cml4fSAxICYgMiBcXGVuZHtwbWF0cml4fSB2XzEgKyBcXGJlZ2lue3BtYXRyaXh9IDMgXFxlbmR7cG1hdHJpeH0gdl8yJC4iLCAiTyBzZWd1bmRvIGNvbXBvbmVudGUgw6kgZGFkbyBwb3IgJEN2XzEgKyBEdl8yID0gXFxiZWdpbntwbWF0cml4fSA0IFxcZW5ke3BtYXRyaXh9IHZfMSArIFxcYmVnaW57cG1hdHJpeH0gNSBcXGVuZHtwbWF0cml4fSB2XzIkLiIsICJTZW5kbyAkdl8xJCBkZSBkaW1lbnPDo28gMiAoJHZfMSA9IFt4LCB5XV5UJCkgZSAkdl8yJCBkZSBkaW1lbnPDo28gMSAoJHokKSwgdGVtb3M6ICRNdiA9IFxcYmVnaW57cG1hdHJpeH0gMXggKyAyeSArIDN6IFxcXFwgNHggKyA1eiBcXGVuZHtwbWF0cml4fSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gbW9kZWxvcyBlc3RhdMOtc3RpY29zLCDDqSBjb211bSBwcm92YXIgcXVlIGEgbWF0cml6IGRlIHByb2R1dG8gJEFeVCBBJCDDqSBzZW1wcmUgXFxzaW3DqXRyaWNhLCBpbmRlcGVuZGVudGVtZW50ZSBkYSBtYXRyaXogJEEkIG9yaWdpbmFsIHNlciBxdWFkcmFkYSBvdSBuw6NvLiBEZW1vbnN0cmUgYWxnZWJyaWNhbWVudGUsIHVzYW5kbyBhIHByb3ByaWVkYWRlIGRhIHRyYW5zcG9zdGEgJChBQileVCA9IEJeVCBBXlQkLCBxdWUgJChBXlQgQSleVCA9IEFeVCBBJC4iLCAiZGljYSI6ICJBcGxpcXVlIGEgcHJvcHJpZWRhZGUgZGEgdHJhbnNwb3N0YSBkbyBwcm9kdXRvIGRlIGR1YXMgbWF0cml6ZXM6ICQoTU4pXlQgPSBOXlQgTV5UJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRGVmaW5pbW9zIGEgbWF0cml6ICRNID0gQV5UIEEkLiBRdWVyZW1vcyB2ZXJpZmljYXIgc2UgJE1eVCA9IE0kLiIsICJBcGxpY2FuZG8gYSB0cmFuc3Bvc3RhIGVtIGFtYm9zIG9zIGxhZG9zOiAkKEFeVCBBKV5UJC4iLCAiUGVsYSBwcm9wcmllZGFkZSBkYSB0cmFuc3Bvc3RhIGRvIHByb2R1dG86ICQoQV5UIEEpXlQgPSBBXlQgKEFeVCleVCQuIiwgIlNhYmVuZG8gcXVlIGEgdHJhbnNwb3N0YSBkYSB0cmFuc3Bvc3RhIMOpIGEgcHLDs3ByaWEgbWF0cml6LCAkKEFeVCleVCA9IEEkLiIsICJQb3J0YW50bywgJChBXlQgQSleVCA9IEFeVCBBJC4iLCAiQ29uY2x1c8OjbzogQSBpZ3VhbGRhZGUgZGVtb25zdHJhIHF1ZSAkTV5UID0gTSQsIGxvZ28gJEFeVCBBJCDDqSBcXHNpbcOpdHJpY2EuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGFkYSBhIG1hdHJpeiBkZSBkYWRvcyBkZSBwcm9kdcOnw6NvICRBID0gXFxiZWdpbntwbWF0cml4fSAxICYgMiAmIDEgXFxcXCAyICYgNCAmIDIgXFxcXCAzICYgNiAmIDQgXFxlbmR7cG1hdHJpeH0kLCBjYWxjdWxlIG8gcG9zdG8gZGVzdGEgbWF0cml6IHV0aWxpemFuZG8gbyBtw6l0b2RvIGRlIGVzY2Fsb25hbWVudG8gcG9yIG9wZXJhw6fDtWVzIGVsZW1lbnRhcmVzIGRlIGxpbmhhLiIsICJkaWNhIjogIlRyYW5zZm9ybWUgYSBtYXRyaXogZW0gdW1hIGZvcm1hIGVzY2Fsb25hZGEgdXRpbGl6YW5kbyBvcGVyYcOnw7VlcyBjb21vICRMXzIgXFxsZWZ0YXJyb3cgTF8yIC0gMkxfMSQgZSAkTF8zIFxcbGVmdGFycm93IExfMyAtIDNMXzEkLiBPIHBvc3RvIHNlcsOhIG8gbsO6bWVybyBkZSBsaW5oYXMgbsOjbyBudWxhcyBhbyBmaW5hbC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogRXNjcmV2ZW1vcyBhIG1hdHJpeiAkQSQgZSBpbmljaWFtb3MgbyBlc2NhbG9uYW1lbnRvLiAkJCBcXGJlZ2lue3BtYXRyaXh9IDEgJiAyICYgMSBcXFxcIDIgJiA0ICYgMiBcXFxcIDMgJiA2ICYgNCBcXGVuZHtwbWF0cml4fSAkJCIsICJQYXNzbyAyOiBSZWFsaXphbW9zICRMXzIgXFxsZWZ0YXJyb3cgTF8yIC0gMkxfMSQgZSAkTF8zIFxcbGVmdGFycm93IExfMyAtIDNMXzEkLiBOb3RlIHF1ZSBhIHNlZ3VuZGEgbGluaGEgc2UgdG9ybmFyw6EgbnVsYSwgcG9pcyDDqSBvIGRvYnJvIGRhIHByaW1laXJhLiAkJCBcXGJlZ2lue3BtYXRyaXh9IDEgJiAyICYgMSBcXFxcIDAgJiAwICYgMCBcXFxcIDAgJiAwICYgMSBcXGVuZHtwbWF0cml4fSAkJCIsICJQYXNzbyAzOiBUcm9jYW1vcyAkTF8yJCBjb20gJExfMyQgcGFyYSBvcmRlbmFyIGFzIGxpbmhhcyBuw6NvIG51bGFzLiAkJCBcXGJlZ2lue3BtYXRyaXh9IDEgJiAyICYgMSBcXFxcIDAgJiAwICYgMSBcXFxcIDAgJiAwICYgMCBcXGVuZHtwbWF0cml4fSAkJCIsICJQYXNzbyA0OiBDb250YW1vcyBhcyBsaW5oYXMgbsOjbyBudWxhcyBkYSBmb3JtYSBlc2NhbG9uYWRhLiBUZW1vcyAyIGxpbmhhcyBuw6NvIG51bGFzLCBwb3J0YW50byBvIHBvc3RvICRyKEEpID0gMiQuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZShkYXRhPVtnby5UYWJsZShoZWFkZXI9ZGljdCh2YWx1ZXM9WydDb2wgMScsICdDb2wgMicsICdDb2wgMyddKSwgY2VsbHM9ZGljdCh2YWx1ZXM9W1sxLCAyLCAzXSwgWzIsIDQsIDZdLCBbMSwgMiwgNF1dKSldKTsgZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J01hdHJpeiBkZSBQcm9kdcOnw6NvICRBJCcpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAyLjB9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgw7N0aWNhIGRhIMOhbGdlYnJhIGxpbmVhciBwYXJhIG1vZGVsb3MgZXN0YXTDrXN0aWNvcywgcG9yIHF1ZSB1bWEgbWF0cml6IGRlIHZhcmnDom5jaWEtY292YXJpw6JuY2lhIHF1ZSBuw6NvIHBvc3N1aSBwb3N0byBjb21wbGV0byAoc2luZ3VsYXIpIGltcGVkZSBvIGPDoWxjdWxvIGRvcyBlc3RpbWFkb3JlcyBkZSBtw61uaW1vcyBxdWFkcmFkb3Mgb3JkaW7DoXJpb3MgdmlhIGludmVyc8OjbyBkaXJldGEgZGEgbWF0cml6IGRlIGluZm9ybWHDp8Ojby4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIG8gZXN0aW1hZG9yIGRlIG3DrW5pbW9zIHF1YWRyYWRvcyBkZXBlbmRlIGRlICQoWF5UIFgpXnstMX0kLiBPIHF1ZSBhY29udGVjZSBjb20gYSBpbnZlcnNhIGRlIHVtYSBtYXRyaXogcXVhbmRvIHNldSBwb3N0byBuw6NvIMOpIG3DoXhpbW8/IiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgbWF0cml6IGRlIG1vbWVudG9zICRYXlQgWCQgw6kgZnVuZGFtZW50YWwgbmEgZXN0aW1hdGl2YSBkZSBwYXLDom1ldHJvcyBkbyBtb2RlbG8gZGUgcmVncmVzc8Ojby4iLCAiU2UgYSBtYXRyaXogJFgkIG7Do28gcG9zc3VpIHBvc3RvIGNvbXBsZXRvLCBlbnTDo28gJHIoWCkgPCBrJCAob25kZSAkayQgw6kgbyBuw7ptZXJvIGRlIGNvbHVuYXMpLiIsICJDb25zZXF1ZW50ZW1lbnRlLCBhIG1hdHJpeiAkWF5UIFgkIHNlcsOhIHNpbmd1bGFyLCBvIHF1ZSBzaWduaWZpY2EgcXVlIHNldSBkZXRlcm1pbmFudGUgw6kgaWd1YWwgYSB6ZXJvICgkfFheVCBYfCA9IDAkKS4iLCAiVW1hIG1hdHJpeiBjb20gZGV0ZXJtaW5hbnRlIG51bG8gbsOjbyBwb3NzdWkgaW52ZXJzYSBkZWZpbmlkYSwgbG9nbywgbsOjbyDDqSBwb3Nzw612ZWwgY2FsY3VsYXIgb3MgZXN0aW1hZG9yZXMgJFxcaGF0e1xcYmV0YX0gPSAoWF5UIFgpXnstMX0gWF5UIFkkLCB0b3JuYW5kbyBvIG1vZGVsbyBuw6NvIGlkZW50aWZpY8OhdmVsLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlNlamEgJEEkIHVtYSBtYXRyaXogJDMgXFx0aW1lcyA0JCBjb20gJHIoQSkgPSAyJC4gU2UgYWRpY2lvbmFybW9zIHVtYSBub3ZhIGxpbmhhICRMXzQkIMOgIG1hdHJpeiAkQSQgcXVlIMOpIHVtYSBjb21iaW5hw6fDo28gbGluZWFyIGRhcyBsaW5oYXMgZXhpc3RlbnRlcywgcXVhbCBzZXLDoSBvIG5vdm8gcG9zdG8gZGEgbWF0cml6IHJlc3VsdGFudGUgJEEnJCBkZSBvcmRlbSAkNCBcXHRpbWVzIDQkPyBKdXN0aWZpcXVlLiIsICJkaWNhIjogIk8gcG9zdG8gZGUgdW1hIG1hdHJpeiDDqSBvIG7Dum1lcm8gZGUgdmV0b3JlcyBsaW5lYXJtZW50ZSBpbmRlcGVuZGVudGVzLiBTZSBhIG5vdmEgbGluaGEgZm9yIHVtYSBjb21iaW5hw6fDo28gbGluZWFyLCBlbGEgYWRpY2lvbmEgYWxndW1hIG5vdmEgZGltZW5zw6NvIGFvIGVzcGHDp28gZ2VyYWRvPyIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJPIHBvc3RvIGRlIHVtYSBtYXRyaXogJHIoQSkkIHJlcHJlc2VudGEgYSBkaW1lbnPDo28gZG8gZXNwYcOnbyBkYXMgbGluaGFzICRMKEEpJC4iLCAiQW8gYWRpY2lvbmFyIHVtYSBub3ZhIGxpbmhhICRMXzQkIHF1ZSDDqSB1bWEgY29tYmluYcOnw6NvIGxpbmVhciBkYXMgbGluaGFzIGrDoSBleGlzdGVudGVzIGVtICRBJCwgZXNzYSBsaW5oYSBuw6NvIGV4cGFuZGUgbyBlc3Bhw6dvIGRhcyBsaW5oYXMgb3JpZ2luYWwuIiwgIk1hdGVtYXRpY2FtZW50ZSwgaXNzbyBzaWduaWZpY2EgcXVlICRMXzQgXFxpbiBMKEEpJC4iLCAiQ29tbyBhIGRpbWVuc8OjbyBkbyBlc3Bhw6dvIG7Do28gZm9pIGFsdGVyYWRhIHBlbGEgYWRpw6fDo28gZGUgdW0gdmV0b3IgbGluZWFybWVudGUgZGVwZW5kZW50ZSwgbyBwb3N0byBwZXJtYW5lY2UgY29uc3RhbnRlLiIsICJQb3J0YW50bywgJHIoQScpID0gcihBKSA9IDIkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMi4wfSwgeyJlbnVuY2lhZG8iOiAiU2VqYSBhIG1hdHJpeiAkQSA9IFxcYmVnaW57cG1hdHJpeH0gMC41ICYgMC41IFxcXFwgMC41ICYgMC41IFxcZW5ke3BtYXRyaXh9JC4gRGVtb25zdHJlIG1hdGVtYXRpY2FtZW50ZSBzZSBlc3RhIG1hdHJpeiDDqSBpZGVtcG90ZW50ZSBlIGRldGVybWluZSBzdWEgY2FyYWN0ZXLDrXN0aWNhIHByaW5jaXBhbCBhdHJhdsOpcyBkYSB2ZXJpZmljYcOnw6NvIGRhIHByb3ByaWVkYWRlIGRlIHByb2plw6fDo28uIiwgImRpY2EiOiAiVW1hIG1hdHJpeiDDqSBpZGVtcG90ZW50ZSBzZSAkQV4yID0gQSQuIFJlYWxpemUgYSBtdWx0aXBsaWNhw6fDo28gbWF0cmljaWFsICRBIFxcdGltZXMgQSQgcGFzc28gYSBwYXNzby4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRGVmaW5pbW9zICRBXjIgPSBBIFxcdGltZXMgQSA9IFxcYmVnaW57cG1hdHJpeH0gMC41ICYgMC41IFxcXFwgMC41ICYgMC41IFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMC41ICYgMC41IFxcXFwgMC41ICYgMC41IFxcZW5ke3BtYXRyaXh9JCIsICJDYWxjdWxhbmRvIG8gZWxlbWVudG8gKDEsMSk6ICQoMC41IFxcdGltZXMgMC41KSArICgwLjUgXFx0aW1lcyAwLjUpID0gMC4yNSArIDAuMjUgPSAwLjUkIiwgIkNhbGN1bGFuZG8gbyBlbGVtZW50byAoMSwyKTogJCgwLjUgXFx0aW1lcyAwLjUpICsgKDAuNSBcXHRpbWVzIDAuNSkgPSAwLjI1ICsgMC4yNSA9IDAuNSQiLCAiQ29tbyB0b2RvcyBvcyBlbGVtZW50b3MgcmVzdWx0YW50ZXMgc8OjbyAwLjUsIHRlbW9zICRBXjIgPSBcXGJlZ2lue3BtYXRyaXh9IDAuNSAmIDAuNSBcXFxcIDAuNSAmIDAuNSBcXGVuZHtwbWF0cml4fSA9IEEkLiIsICJDb25jbHVzw6NvOiBDb21vICRBXjIgPSBBJCwgYSBtYXRyaXogw6kgY29uZmlybWFkYSBjb21vIGlkZW1wb3RlbnRlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlBhcmEgYSBtYXRyaXogXFxzaW3DqXRyaWNhICRBID0gXFxiZWdpbntwbWF0cml4fSAyICYgMSBcXFxcIDEgJiAyIFxcZW5ke3BtYXRyaXh9JCwgZW5jb250cmUgb3MgYXV0b3ZhbG9yZXMgJFxcbGFtYmRhXzEkIGUgJFxcbGFtYmRhXzIkIHJlc29sdmVuZG8gYSBlcXVhw6fDo28gY2FyYWN0ZXLDrXN0aWNhICR8QSAtIFxcbGFtYmRhIEl8ID0gMCQuIiwgImRpY2EiOiAiQSBlcXVhw6fDo28gY2FyYWN0ZXLDrXN0aWNhIMOpIG8gZGV0ZXJtaW5hbnRlIGRhIG1hdHJpeiByZXN1bHRhbnRlIGRhIHN1YnRyYcOnw6NvIGRlICRcXGxhbWJkYSQgZGEgZGlhZ29uYWwgcHJpbmNpcGFsIGRlICRBJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiTW9udGFyIGEgbWF0cml6ICRBIC0gXFxsYW1iZGEgSSA9IFxcYmVnaW57cG1hdHJpeH0gMi1cXGxhbWJkYSAmIDEgXFxcXCAxICYgMi1cXGxhbWJkYSBcXGVuZHtwbWF0cml4fSQiLCAiQ2FsY3VsYXIgbyBkZXRlcm1pbmFudGU6ICQoMi1cXGxhbWJkYSkoMi1cXGxhbWJkYSkgLSAoMSBcXHRpbWVzIDEpID0gMCQiLCAiRXhwYW5kaXI6ICQ0IC0gNFxcbGFtYmRhICsgXFxsYW1iZGFeMiAtIDEgPSAwJCIsICJTaW1wbGlmaWNhcjogJFxcbGFtYmRhXjIgLSA0XFxsYW1iZGEgKyAzID0gMCQiLCAiUmVzb2x2ZXIgYSBlcXVhw6fDo28gcXVhZHLDoXRpY2E6ICQoXFxsYW1iZGEgLSAzKShcXGxhbWJkYSAtIDEpID0gMCQiLCAiUG9ydGFudG8sIG9zIGF1dG92YWxvcmVzIHPDo28gJFxcbGFtYmRhXzEgPSAzJCBlICRcXGxhbWJkYV8yID0gMSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAzLjB9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgcXVlIHVtIHZldG9yICR4JCDDqSBwcm9qZXRhZG8gc29icmUgbyBlc3Bhw6dvIGdlcmFkbyBwZWxvIGF1dG92ZXRvciAkdV8xJCBkZSB1bWEgbWF0cml6IFxcc2ltw6l0cmljYSAkQSQuIFNlICRBID0gXFxsYW1iZGFfMSB1XzEgdV8xJyArIFxcbGFtYmRhXzIgdV8yIHVfMickLCBlIGRhZG8gcXVlICR1XzEkIGUgJHVfMiQgc8OjbyBvcnRvbm9ybWFpcyAoJHVfaSd1X2ogPSAwJCBwYXJhICRpIFxcbmVxIGokIGUgJHVfaSd1X2kgPSAxJCksIGRldGVybWluZSBvIHJlc3VsdGFkbyBkZSAkQXgkIHF1YW5kbyAkeCA9IHVfMSQuIiwgImRpY2EiOiAiVXRpbGl6ZSBhIHByb3ByaWVkYWRlIGRhIGRlY29tcG9zacOnw6NvIGVzcGVjdHJhbCAkQSA9IFxcc3VtIFxcbGFtYmRhX2kgdV9pIHVfaSckIGUgbXVsdGlwbGlxdWUgcGVsbyB2ZXRvciAkdV8xJC4gTGVtYnJlLXNlIGRhIG9ydG9nb25hbGlkYWRlLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJFeHBhbmRpciBhIG9wZXJhw6fDo286ICRBeCA9IChcXGxhbWJkYV8xIHVfMSB1XzEnICsgXFxsYW1iZGFfMiB1XzIgdV8yJyl1XzEkIiwgIkRpc3RyaWJ1aXIgbyB2ZXRvciAkdV8xJDogJEF4ID0gXFxsYW1iZGFfMSB1XzEgKHVfMSd1XzEpICsgXFxsYW1iZGFfMiB1XzIgKHVfMid1XzEpJCIsICJBcGxpY2FyIGEgb3J0b25vcm1hbGlkYWRlOiBDb21vICR1XzEndV8xID0gMSQgZSAkdV8yJ3VfMSA9IDAkLCB0ZW1vczoiLCAiJEF4ID0gXFxsYW1iZGFfMSB1XzEgKDEpICsgXFxsYW1iZGFfMiB1XzIgKDApJCIsICJSZXN1bHRhZG8gZmluYWw6ICRBeCA9IFxcbGFtYmRhXzEgdV8xJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9XX0=').decode('utf-8'))


    import plotly.graph_objects as go
    
    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do progresso
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discursivas = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcqs) + len(discursivas)
    acertos = sum(1 for v in st.session_state.respostas_certas.values() if v)
    
    # Interface de Progresso
    if total_exercicios > 0:
        progresso = acertos / total_exercicios
        st.progress(progresso)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    st.divider()
    
    # Renderização de Questões de Múltipla Escolha
    for i, questao in enumerate(mcqs):
        with st.container():
            st.subheader(f"Questão de Seleção {i + 1}")
            st.write(questao.get("enunciado", ""))
            
            # Referência (se existir)
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
    
            # Gráfico (se existir)
            code = questao.get("codigo_plotly")
            if code:
                try:
                    local_vars = {"go": go}
                    exec(code, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True)
                except Exception as e:
                    st.warning("O gráfico não pôde ser renderizado.")
    
            # Alternativas
            alternativas = questao.get("alternativas", {})
            escolha = st.radio(
                "Escolha uma alternativa:",
                options=list(alternativas.keys()),
                format_func=lambda x: f"{x}) {alternativas[x]}",
                key=f"radio_mcq_{i}"
            )
    
            # Dica
            if st.button("💡 Dica", key=f"btn_dica_mcq_{i}"):
                st.info(questao.get("dica", "Dica indisponível"))
    
            # Verificação
            if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
                if escolha == questao.get("alternativa_correta"):
                    st.success("Correto! Muito bem.")
                    st.session_state.respostas_certas[f"mcq_{i}"] = True
                    st.rerun()
                else:
                    st.error("Resposta incorreta. Tente novamente!")
                    st.session_state.respostas_certas[f"mcq_{i}"] = False
                    st.rerun()
    
            # Gabarito
            with st.expander("✅ Ver Gabarito Comentado"):
                st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
            
            st.divider()
    
    # Renderização de Questões Discursivas
    for i, questao in enumerate(discursivas):
        with st.container():
            st.subheader(f"Questão Discursiva {i + 1}")
            st.write(questao.get("enunciado", ""))
            
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
                
            # Gráfico (se existir)
            code = questao.get("codigo_plotly")
            if code:
                try:
                    local_vars = {"go": go}
                    exec(code, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True)
                except Exception as e:
                    st.warning("O gráfico não pôde ser renderizado.")
    
            st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
    
            # Validação Numérica ou Checkbox
            esperada = questao.get("resposta_numerica_esperada")
            if esperada is not None:
                user_val = st.number_input("Digite o resultado numérico calculado para validação:", key=f"num_disc_{i}", step=0.01)
                if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                    if abs(user_val - esperada) <= max(0.01, 0.01 * abs(esperada)):
                        st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                        st.rerun()
                    else:
                        st.error("O valor calculado difere do gabarito oficial. Verifique seus arredondamentos e fórmulas e tente novamente.")
                        st.session_state.respostas_certas[f"disc_{i}"] = False
                        st.rerun()
            else:
                if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.session_state.respostas_certas[f"disc_{i}"] = False
    
            # Dica e Gabarito
            if st.button("💡 Dica", key=f"btn_dica_disc_{i}"):
                st.info(questao.get("dica", "Dica indisponível"))
                
            with st.expander("✅ Ver Resolução Detalhada"):
                for passo in questao.get("gabarito_passo_a_passo", []):
                    st.write(f"- {passo}")
            
            st.divider()
