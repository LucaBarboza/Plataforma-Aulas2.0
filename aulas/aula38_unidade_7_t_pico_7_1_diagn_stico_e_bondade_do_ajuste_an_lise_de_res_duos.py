import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDcgLSBUw7NwaWNvIDcuMTogRGlhZ27Ds3N0aWNvIGUgYm9uZGFkZSBkbyBhanVzdGU6IEFuw6FsaXNlIGRlIHJlc8OtZHVvcyIsICJyZWZlcmVuY2lhc19iaWJsaW9ncmFmaWNhc19maW5haXMiOiBbIkx1bmEgJiBFc3RldmVzLCBJbnRyb2R1w6fDo28gYW9zIE1vZGVsb3MgTGluZWFyZXMgLSBDYXAuIDIsIHBwLiA1OC02MCIsICJMdW5hICYgRXN0ZXZlcywgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzIC0gQ2FwLiAzLCBwcC4gNjgtNzAiLCAiTHVuYSAmIEVzdGV2ZXMsIEludHJvZHXDp8OjbyBhb3MgTW9kZWxvcyBMaW5lYXJlcyAtIENhcC4gNCwgcHAuIDg2LTkxLCAxMDgtMTExIiwgIkx1bmEgJiBFc3RldmVzLCBJbnRyb2R1w6fDo28gYW9zIE1vZGVsb3MgTGluZWFyZXMgLSBDYXAuIDUsIHBwLiAxMjAtMTI1IiwgIkZhcmF3YXksIExpbmVhciBNb2RlbHMgd2l0aCBSIC0gQ2FwLiA3LCBwcC4gNzItNzgsIDg4LTkxIl19').decode('utf-8'))

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
            background: linear-gradient(135deg, #0000FF 0%, #3B82F6 100%);
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
            border-top: 3px solid #0000FF !important;
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
            background: linear-gradient(90deg, #0000FF 0%, #808080 100%) !important;
            border-radius: 10px !important;
        }
        
        /* Inputs e Sliders na aula */
        div.stSlider [data-testid="stSliderTickBar"] {
            background-color: #0000FF !important;
        }
        
        /* Botões na aula */
        div.stButton > button {
            background: linear-gradient(135deg, #0000FF 0%, #3B82F6 100%) !important;
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
PRIMARY_BLUE = "#0000FF"
SECONDARY_GREEN = "#808080"
WARNING_AMBER = "#FFFFFF"
CRITICAL_RED = "#FF0000"

# Criação das Duas Grandes Abas Globais
tab_conteudo, tab_exercicios = st.tabs(["📚 Conteúdo Acadêmico Interativo", "📝 Caderno de Exercícios"])

with tab_conteudo:

    # A Geometria dos Resíduos e o Operador de Projeção - Layout Acadêmico Premium
    
    st.header(r"A Geometria dos Resíduos e o Operador de Projeção")
    
    st.markdown(r"""
    A regressão linear pode ser interpretada como um problema fundamental de geometria vetorial em espaços de dimensão $n$. Ao observarmos o vetor de respostas, tratamo-lo como um ponto flutuando em um espaço de $n$ dimensões.
    """)
    
    st.info(r"O objetivo é representar o vetor de respostas como uma combinação linear das colunas da matriz de design $X$, que definem um subespaço de dimensão $p$.")
    
    st.markdown(r"""
    Como os dados observados raramente residem perfeitamente no subespaço de design, buscamos a projeção ortogonal do vetor de respostas sobre ele.
    *   **Previsão:** O ponto resultante no subespaço.
    *   **Resíduos:** A distância entre a resposta observada e sua projeção, que deve ser perpendicular ao subespaço de design.
    *   **Mínimos Quadrados:** Essência da ortogonalidade que garante a extração da informação sistemática máxima.
    """)
    
    st.subheader(r"📐 Formalismo Matemático: A Topologia do Erro")
    
    st.latex(r"S(\beta) = (Y - X\beta)'(Y - X\beta) = \sum e_i^2")
    st.latex(r"P = X(X'X)^{-1}X'")
    st.latex(r"e = (I - P)Y")
    
    st.subheader(r"🧮 Demonstração Analítica: Derivação do Operador")
    
    st.markdown(r"A minimização da função objetivo segue o cálculo diferencial matricial:")
    st.latex(r"S(\beta) = (Y - X\beta)'(Y - X\beta) = \sum e_i^2")
    
    st.markdown(r"Expandindo a forma quadrática:")
    st.latex(r"S(\beta) = Y'Y - 2\beta'X'Y + \beta'X'X\beta")
    
    st.markdown(r"Derivando em relação a $\beta$ e igualando ao vetor nulo:")
    st.latex(r"\frac{\partial S}{\partial \beta} = -2X'Y + 2X'X\hat{\beta} = 0")
    
    st.markdown(r"Isolando o estimador de mínimos quadrados:")
    st.latex(r"X'X\hat{\beta} = X'Y \Rightarrow \hat{\beta} = (X'X)^{-1}X'Y")
    
    st.markdown(r"Definindo a projeção no espaço de design:")
    st.latex(r"\hat{Y} = X\hat{\beta} = X(X'X)^{-1}X'Y = PY")
    
    st.markdown(r"Extraindo o vetor de resíduos:")
    st.latex(r"e = Y - \hat{Y} = (I - P)Y")
    
    st.subheader(r"📈 Caso de Estudo: Ensaio Clínico de Redução de Glicose")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Análise de Dosagem")
        st.markdown(r"Em um ensaio clínico, medimos a redução de glicose (Y) de 3 pacientes em função da dosagem de um fármaco (X). Temos $Y = [10, 12, 14]'$ e a matriz de design $X$ composta por coluna de uns e dosagem.")
        
        st.latex(r"X'X = \begin{pmatrix} 3 & 6 \\ 6 & 14 \end{pmatrix}, (X'X)^{-1} = \frac{1}{6} \begin{pmatrix} 14 & -6 \\ -6 & 3 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Estimativa dos parâmetros: $\hat{\beta} = (X'X)^{-1}X'Y = [8, 2]'$")
        st.markdown(r"- Vetor de projeção: $\hat{Y} = X\hat{\beta} = [10, 12, 14]'$")
        st.markdown(r"- Vetor de resíduos: $e = Y - \hat{Y} = [0, 0, 0]'$")
        
        st.success(r"Laudo: O ajuste perfeito encontrado, com resíduos nulos, indica que o modelo capturou toda a variabilidade sistemática dos dados deste pequeno grupo amostral, servindo como base teórica para aplicações em amostras mais robustas.")
    
    st.subheader(r"💡 Perspectiva Geométrica e Intelecção")
    
    st.markdown(r"""
    A história da estatística matemática é a crônica de nossa tentativa de extrair ordem a partir do ruído. Ao concebermos $Y$ como um ponto flutuando em um espaço de $n$ dimensões, transformamos um cálculo algébrico em um problema de otimização geométrica.
    """)
    
    st.warning(r"O operador $P$ atua como um filtro idempotente: $P^2 = P$. Isso significa que, ao projetarmos o vetor de respostas no subespaço, ele já se encontra em seu destino final, e projeções subsequentes são redundantes.")
    
    st.markdown(r"""
    A ortogonalidade entre o vetor de resíduos $e$ e o subespaço gerado por $X$ é a garantia de que não restou nenhuma estrutura sistemática não explicada. 
    *   **Espaço de resíduos:** Tem dimensão $n - p$, representando os graus de liberdade remanescentes.
    *   **Diagnóstico:** A verificação visual da ortogonalidade (ou falta de padrão nos resíduos) é a missão primordial para validar as premissas do modelo.
    """)
    
    st.markdown(r"""
    Dominar essa topologia do erro permite ao pesquisador não apenas ajustar curvas, mas compreender a essência da relação entre variáveis, garantindo que o modelo seja a melhor representação possível da realidade subjacente.
    """)

    # Título do Subtópico
    st.header(r"Propriedades Estatísticas e a Estrutura de Covariância dos Resíduos")
    
    # Introdução
    st.markdown(r"""
    A análise de resíduos constitui a base do diagnóstico em modelos lineares. Após a projeção ortogonal das observações no subespaço definido pelo modelo, os resíduos representam a informação que o modelo não foi capaz de capturar. 
    
    Sob condições ideais, estes resíduos devem comportar-se como ruído aleatório. O **Teorema de Gauss-Markov** fornece as garantias fundamentais para essa interpretação:
    - **Ausência de Viés:** O erro esperado é nulo, $E[e] = 0$.
    - **Variância Constante:** A variância é homogênea, garantindo a eficiência do estimador.
    - **Independência Teórica:** Erros subjacentes não possuem correlação intrínseca.
    """)
    
    st.info(r"A matriz de covariância dos resíduos é a ferramenta diagnóstica definitiva. Padrões de heterocedasticidade ou autocorrelação indicam que o modelo necessita de refinamentos, seja na estrutura funcional ou na técnica de estimação.")
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Estrutura dos Resíduos")
    st.latex(r"E[e] = 0")
    st.latex(r"V[e] = \sigma^2 (I - P)")
    st.latex(r"QMRes = \frac{e'e}{n-p}")
    
    # Demonstração Analítica
    st.markdown(r"#### Demonstração da Estrutura de Covariância")
    st.markdown(r"A esperança matemática dos resíduos, considerando a projeção, é dada por:")
    st.latex(r"E[e] = E[(I - P)Y] = (I - P)X\beta")
    st.markdown(r"Dada a definição da matriz de projeção $P = X(X'X)^{-1}X'$, observamos que:")
    st.latex(r"(I - P)X = X - X(X'X)^{-1}X'X = X - X = 0")
    st.markdown(r"Para a variância, utilizando as propriedades da matriz de projeção idempotente:")
    st.latex(r"V[e] = (I - P)V[Y](I - P)^T = \sigma^2(I - P)(I - P)^T")
    st.latex(r"V[e] = \sigma^2(I - P)")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Estrutura de Correlação Induzida")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Modelo Linear com $n=4$")
        st.markdown(r"Desejamos calcular a matriz de covariância teórica para um sistema de 4 observações, dado um modelo de regressão linear simples com intercepto e uma variável preditora.")
        
        st.latex(r"X'X = \begin{pmatrix} 4 & 10 \\ 10 & 30 \end{pmatrix}, V[e] = I - P")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- 1. Inversão da matriz de design normalizada: $(X'X)^{-1} = \begin{pmatrix} 1.5 & -0.5 \\ -0.5 & 0.2 \end{pmatrix}$")
        st.markdown(r"- 2. Construção da matriz chapéu: $P = X(X'X)^{-1}X'$")
        st.markdown(r"- 3. Cálculo final da estrutura de erro: $V[e] = I - X(X'X)^{-1}X'$")
        
        st.success(r"Conclusão: A matriz de covariância obtida demonstra que, embora os erros populacionais sejam independentes, a estrutura dos resíduos amostrais é intrinsecamente correlacionada pela necessidade de ortogonalidade ao subespaço de design.")
    
    # Considerações Finais
    st.markdown(r"""
    ### 🔍 Reflexões sobre o Diagnóstico
    A observação da magnitude do **QMRes** é essencial para a validade estatística:
    1. **Perda de Graus de Liberdade:** O divisor $n-p$ corrige o viés de subestimação da variância populacional.
    2. **Humildade Científica:** Resíduos não aleatórios sinalizam variáveis omitidas ou formas funcionais incorretas.
    3. **Generalização:** Modelos que negligenciam a análise de covariância dos resíduos perdem a capacidade de generalização e tornam-se, essencialmente, caixas-pretas de ajuste de curvas.
    """)

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Transformações e Escalamento: Resíduos Padronizados e Studentizados")
    
    st.markdown(r"""
    A análise de resíduos no modelo de regressão linear constitui o alicerce fundamental para a validação dos pressupostos estatísticos. Historicamente, a análise limitava-se aos resíduos brutos, mas essa abordagem ignora a heterogeneidade das variâncias induzida pela matriz de desenho.
    """)
    
    st.info(r"""
    **A Geometria da Influência:** Em um modelo linear, a geometria do espaço de colunas faz com que observações com elevada alavancagem ($h_i$) exerçam uma influência desproporcional. O modelo tende a 'se aproximar' desses pontos, reduzindo artificialmente o resíduo bruto e mascarando outliers.
    """)
    
    st.markdown(r"""
    Para mitigar essa distorção, utilizamos:
    - **Resíduos Padronizados:** Equalizam a variância, tornando-os comparáveis em uma escala unitária.
    - **Resíduos Studentizados:** Removem a influência direta da observação no cálculo da variância residual, fornecendo um critério estatístico robusto.
    """)
    
    # O Coração Matemático
    st.subheader(r"📐 O Coração Matemático: Formalismo e Derivação")
    
    st.markdown(r"A variação do resíduo é dependente da alavancagem do ponto:")
    st.latex(r"V[e_i] = \sigma^2(1 - h_i)")
    
    st.markdown(r"A padronização ajusta essa variação pela estimativa do desvio padrão residual:")
    st.latex(r"r_i = \frac{e_i}{\hat{\sigma} \sqrt{1 - h_i}}")
    
    st.markdown(r"A studentização (ou resíduo jackknife) remove a contaminação da observação $i$ na variância, resultando em:")
    st.latex(r"t_i = r_i \left( \frac{n - p - 1}{n - p - r_i^2} \right)^{1/2}")
    
    # Visualizador Interativo
    st.subheader(r"📊 Visualizador de Alavancagem e Studentização")
    
    col_a, col_b = st.columns(2)
    with col_a:
        h_i = st.slider(r"Alavancagem (h_i)", 0.01, 0.99, 0.6, step=0.01, key=r"h_i_subtopico_3")
    with col_b:
        e_i = st.number_input(r"Resíduo Bruto (e_i)", -5.0, 5.0, 2.0, step=0.1, key=r"e_i_subtopico_3")
    
    # Cálculos do simulador
    sigma_hat = 1.0
    n = 10
    p = 2
    r_i = e_i / (sigma_hat * np.sqrt(1 - h_i))
    # Evitar divisao por zero ou sqrt negativo
    denom_t = (n - p - r_i**2)
    if denom_t > 0:
        t_i = r_i * np.sqrt((n - p - 1) / denom_t)
    else:
        t_i = float('inf')
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[r"Resíduo Bruto", r"Resíduo Padronizado", r"Resíduo Studentizado"], 
                         y=[e_i, r_i, t_i], marker_color=["#64748B", "#0000FF", "#FF0000"]))
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Efeito da Alavancagem nos Resíduos</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Tipo de Resíduo", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Valor Estimado", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    st.info(r"Ao aumentar a alavancagem ($h_i$), o efeito de 'puxar' o modelo causa uma redução artificial do resíduo bruto. O resíduo studentizado compensa esse efeito, expondo a verdadeira magnitude do outlier: t = " + str(round(t_i, 2)))
    
    # Casos de Aplicação
    st.subheader(r"📈 Casos de Aplicação Prática: Diagnóstico de Anomalias")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Análise de Resíduos em Amostra Pequena")
        st.markdown(r"Em uma amostra de 10 residências, avaliamos um ponto com alta alavancagem de $h=0.6$, resíduo bruto $e=2.0$ e variância estimada $\hat{\sigma}=1.0$.")
        st.latex(r"e_i=2.0, \hat{\sigma}=1.0, h_i=0.6")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Passo 1: Cálculo do resíduo padronizado: $r_i = 2.0 / (1.0 * \sqrt{1 - 0.6}) = 2.0 / 0.632 \approx 3.16$")
        st.markdown(r"- Passo 2: Avaliação crítica via transformação de Student.")
        st.success(r"Laudo: O valor de 3.16 excede o limiar crítico convencional, indicando uma observação atípica que, sem a padronização, seria subestimada pelo resíduo bruto.")
    
    st.markdown(r"""
    Em síntese, o uso dos resíduos studentizados permite que o auditor da qualidade de dados identifique anomalias que, de outra forma, permaneceriam latentes no modelo. A técnica garante que a inferência final sobre os parâmetros populacionais não esteja refém de observações extremas ou mal estruturadas.
    """)

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Diagnóstico Visual: Avaliação da Homoscedasticidade e Linearidade")
    
    # Introdução com ritmo de leitura
    st.markdown(r"""
    A jornada científica que culmina na modelagem estatística rigorosa transcende a simples computação de coeficientes. Ela reside, essencialmente, na capacidade do investigador de validar as pressuposições que dão sustentação ao arcabouço probabilístico do modelo linear.
    """)
    
    st.markdown(r"""
    Ao postularmos a relação funcional $Y = X\beta + \Delta$, aceitamos condições que garantem que nossos estimadores sejam os melhores estimadores lineares não viciados. Contudo, a aplicação cega dessas técnicas sem uma inspeção minuciosa pode conduzir a conclusões espúrias.
    """)
    
    st.subheader(r"📐 O Coração Matemático: Integridade Funcional e Variância")
    
    st.markdown(r"Para um modelo bem especificado, os resíduos devem comportar-se como ruído branco. O teste de integridade funcional baseia-se na média condicional:")
    st.latex(r"E[e_i | \hat{Y}_i] = 0")
    
    st.markdown(r"Já a premissa de variância constante, ou homoscedasticidade, é regida pelo formalismo:")
    st.latex(r"V[e_i | \hat{Y}_i] = \sigma^2(1 - h_i)")
    
    # Dedução Analítica Sequencial
    st.markdown(r"A validade destas premissas pode ser verificada pela ortogonalidade entre resíduos e valores ajustados:")
    st.latex(r"e = (I - P)\Delta")
    st.latex(r"\hat{Y} = X\beta + P\Delta")
    st.latex(r"Cov(e, \hat{Y}) = (I - P)Var(\Delta)P^T")
    st.latex(r"Cov(e, \hat{Y}) = \sigma^2(P - P^2) = 0")
    
    # Simulador de Diagnóstico
    st.subheader(r"🎛️ Simulador: Diagnóstico de Resíduos")
    
    col1, col2 = st.columns(2)
    with col1:
        curvatura = st.slider(r"Fator de Curvatura (Linearidade)", -2.0, 2.0, 0.0, step=0.1, key=r"curv_subtopico_4")
    with col2:
        hetero = st.slider(r"Fator de Heterocedasticidade (Funil)", 0.0, 2.0, 0.0, step=0.1, key=r"het_subtopico_4")
    
    # Geração de dados para o simulador
    n_obs = 100
    x_val = np.linspace(1, 10, n_obs)
    # y = beta*x + curva + erro_heterocedastico
    noise = np.random.normal(0, 1, n_obs)
    y_val = 2 * x_val + curvatura * (x_val - 5)**2 + (noise * (1 + hetero * (x_val / 5)))
    slope, intercept, _, _, _ = stats.linregress(x_val, y_val)
    y_hat = slope * x_val + intercept
    residuos = y_val - y_hat
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_hat, y=residuos, mode='markers', name=r"Resíduos", marker=dict(color="#0000FF", size=6)))
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Diagnóstico: Resíduos vs Valores Ajustados</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Valores Ajustados (\hat{Y})", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Resíduos (e)", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")
    
    # Laudo Dinâmico
    if curvatura != 0 or hetero != 0:
        st.warning(r"⚠️ Diagnóstico: Padrões sistemáticos detectados. O modelo apresenta violações de linearidade ou variância constante.")
    else:
        st.success(r"✅ Diagnóstico: Os resíduos comportam-se como ruído aleatório. Modelo validado para a amostra corrente.")
    
    st.subheader(r"📈 Casos de Aplicação Prática")
    
    # Exemplo Prático 1
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Custos Industriais")
        st.markdown(r"Em um estudo de custos industriais, observamos no gráfico de resíduos um padrão onde a dispersão aumenta com os valores preditos. Como esse comportamento afeta a validade dos intervalos de confiança?")
        st.latex(r"V[e_i] = \sigma^2 f(\hat{Y}_i)")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Identificar violação da premissa de variância constante $V[\Delta] = \sigma^2 I$.")
        st.markdown(r"- Concluir perda de eficiência do estimador devido à heterocedasticidade.")
        st.markdown(r"- Reconhecer o enviesamento dos erros padrões calculados, invalidando testes t e intervalos de confiança.")
        st.success(r"Laudo: A heterocedasticidade detectada sugere que o modelo é ineficiente para predições em faixas de alto custo, demandando transformação logarítmica ou mínimos quadrados ponderados.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Inferência sobre a Distribuição: Avaliação da Normalidade dos Resíduos")
    
    # Prosa Inicial Teórica
    st.markdown(r"""
    A validação da normalidade dos erros é vital para que os testes de significância (teste t e F) tenham validade exata. Na modelagem estatística, o pressuposto fundamental é que os erros seguem uma distribuição normal, permitindo que a incerteza associada aos parâmetros estimados seja rigorosamente mensurada.
    """)
    
    st.info(r"Quando essa suposição é violada, os testes de hipóteses perdem sua precisão exata, os p-valores deixam de ser confiáveis e a inferência torna-se apenas um artifício aritmético.")
    
    st.markdown(r"""
    O gráfico Quantil-Quantil (Q-Q plot) é a ferramenta padrão-ouro para essa verificação. Ele compara os resíduos padronizados observados com os quantis esperados de uma distribuição normal padrão.
    """)
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Normalidade dos Erros")
    st.latex(r"\Delta \sim N(0, \sigma^2 I)")
    st.latex(r"z_{(i)} = \Phi^{-1}\left(\frac{i - 0.375}{n + 0.25}\right)")
    
    # Dedução Analítica
    st.markdown(r"### 🧠 Dedução Analítica e Propriedades")
    st.markdown(r"A verificação da normalidade dos resíduos baseia-se na transformação dos resíduos brutos em resíduos padronizados, garantindo comparabilidade:")
    
    st.latex(r"r_i = \frac{e_i}{\hat{\sigma}\sqrt{1-h_i}}")
    st.markdown(r"Sob a hipótese de normalidade, estes resíduos seguem uma distribuição normal padrão:")
    st.latex(r"r_i \sim N(0, 1)")
    st.markdown(r"O gráfico é construído comparando o resíduo ordenado $r_{(i)}$ com o quantil teórico $z_{(i)}$:")
    st.latex(r"r_{(i)} \approx z_{(i)}")
    
    # Simulador Interativo
    st.markdown(r"### 📊 Simulador: Q-Q Plot Interativo")
    col1, col2 = st.columns([1, 1])
    with col1:
        kurtosis_level = st.slider(r"Nível de Curtose (Caudas)", min_value=1.0, max_value=10.0, value=3.0, step=0.5, key=r"kurtosis_subtopico_5")
    with col2:
        n_samples = st.number_input(r"Tamanho da Amostra (n)", min_value=20, max_value=500, value=100, step=10, key=r"n_subtopico_5")
    
    # Geração de dados simulados para o gráfico
    np.random.seed(42)
    data_res = stats.t.rvs(df=kurtosis_level, size=n_samples)
    sorted_res = np.sort(data_res)
    theoretical_quantiles = stats.norm.ppf(np.linspace(0.01, 0.99, n_samples))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=theoretical_quantiles, y=sorted_res, mode='markers', name=r"Resíduos", marker=dict(color="#0000FF", opacity=0.6)))
    fig.add_trace(go.Scatter(x=theoretical_quantiles, y=theoretical_quantiles, mode='lines', name=r"Linha Teórica", line=dict(color="#FF0000", dash="dash")))
    
    fig.update_layout(
        title=dict(text="<b>Q-Q Plot: Diagnóstico de Normalidade</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        xaxis=dict(title=dict(text="Quantis Teóricos", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Resíduos Observados", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_5")
    
    # Laudo Dinâmico
    if kurtosis_level < 3.5:
        st.info(r"Com a curtose próxima a 3, a distribuição se aproxima da normalidade, validando os testes de significância clássicos.")
    else:
        st.warning(rf"Com nível de curtose {kurtosis_level:.1f}, detectamos caudas pesadas. O formato em 'S' sugere leptocurtose, podendo inflar os erros padrão.")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Avaliação de Resíduos")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Identificação de Padrão 'S'")
        st.markdown(r"Um analista de sistemas observou um padrão de 'S' em um Q-Q plot de resíduos padronizados com n=30. Explique a interpretação estatística.")
        st.latex(r"Formato = 'S', n=30")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Detectar caudas mais pesadas que a normal (leptocurtose).")
        st.markdown(r"- Avaliar a violação da premissa de normalidade devido à dispersão excessiva nas extremidades.")
        st.markdown(r"- Recomendar testes de robustez ou transformações de variável dependente.")
        st.success(r"O padrão 'S' indica leptocurtose, implicando que os intervalos de confiança calculados podem estar subestimados. Recomenda-se cautela na significância das variáveis explicativas.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDcgLSBUw7NwaWNvIDcuMTogRGlhZ27Ds3N0aWNvIGUgYm9uZGFkZSBkbyBhanVzdGU6IEFuw6FsaXNlIGRlIHJlc8OtZHVvcyIsICJxdWVzdG9lc19tdWx0aXBsYV9lc2NvbGhhIjogW3siZW51bmNpYWRvIjogIkVtIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvIGxpbmVhciAkWSA9IFhcXGJldGEgKyBcXERlbHRhJCwgb25kZSAkWSBcXGluIFxcbWF0aGJie1J9Xm4kIGUgJFggXFxpbiBcXG1hdGhiYntSfV57biBcXHRpbWVzIHB9JCBwb3NzdWkgcG9zdG8gY29sdW5hIGNvbXBsZXRvLCBvIHZldG9yIGRlIHZhbG9yZXMgcHJlZGl0b3MgJFxcaGF0e1l9JCDDqSBvYnRpZG8gYXRyYXbDqXMgZGEgcHJvamXDp8OjbyBvcnRvZ29uYWwgZGUgJFkkIHNvYnJlIG8gZXNwYcOnbyBjb2x1bmEgZGUgJFgkLCBkZW5vdGFkbyBwb3IgJEMoWCkkLiBDb25zaWRlcmUgYSBtYXRyaXogY2hhcMOpdSAkUCA9IFgoWCdYKV57LTF9WCckLiBRdWFsIGRhcyBzZWd1aW50ZXMgcHJvcHJpZWRhZGVzIGRlc2NyZXZlIGNvcnJldGFtZW50ZSBvIHBhcGVsIGRhIG1hdHJpeiAkUCQgZSBkbyB2ZXRvciBkZSByZXPDrWR1b3MgJGUgPSAoSSAtIFApWSQgbm8gY29udGV4dG8gZGEgZ2VvbWV0cmlhIGRvcyByZXPDrWR1b3M/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIG1hdHJpeiAkUCQgw6kgYSBwcm9qZcOnw6NvIG5vIGVzcGHDp28gZG9zIHJlc8OtZHVvcywgZSBvIHZldG9yICRlJCBwZXJ0ZW5jZSBhbyBzdWJlc3Bhw6dvICRDKFgpJC4iLCAiQiI6ICJBIG1hdHJpeiAkUCQgcHJvamV0YSAkWSQgbm8gc3ViZXNwYcOnbyAkQyhYKSQsIGdhcmFudGluZG8gcXVlIG8gdmV0b3IgJGUkIHNlamEgb3J0b2dvbmFsIGEgcXVhbHF1ZXIgY29sdW5hIGRlICRYJC4iLCAiQyI6ICJPIHZldG9yIGRlIHJlc8OtZHVvcyAkZSQgw6kgYSBwYXJ0ZSBzaXN0ZW3DoXRpY2EgZG8gbW9kZWxvIGUgbyB2ZXRvciAkXFxoYXR7WX0kIGNvbnTDqW0gYXBlbmFzIHJ1w61kbyBhbGVhdMOzcmlvLiIsICJEIjogIkEgbWF0cml6ICRQJCDDqSB1bWEgbWF0cml6IGRlIHByb2plw6fDo28gb2Jsw61xdWEgcXVlIG1pbmltaXphIGEgbm9ybWEgZXVjbGlkaWFuYSBkbyB2ZXRvciBkZSByZXNwb3N0YXMgJFkkLiIsICJFIjogIk8gZXNwYcOnbyBkb3MgcmVzw61kdW9zIHBvc3N1aSBkaW1lbnPDo28gJHAkLCBlbnF1YW50byBvIGVzcGHDp28gZGEgbWF0cml6IGRlIGRlc2lnbiBwb3NzdWkgZGltZW5zw6NvICRuLXAkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRlIHF1ZSBhIHByb2plw6fDo28gb3J0b2dvbmFsIGJ1c2NhIG8gcG9udG8gbWFpcyBwcsOzeGltbyBubyBzdWJlc3Bhw6dvIGUgcXVlIGEgZGlmZXJlbsOnYSBlbnRyZSBvIHBvbnRvIHJlYWwgZSBhIHByb2plw6fDo28gZGVmaW5lIG8gZXJybyBvdSByZXPDrWR1by4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgbWF0cml6ICRQID0gWChYJ1gpXnstMX1YJyQgw6ksIHBvciBkZWZpbmnDp8OjbywgbyBvcGVyYWRvciBkZSBwcm9qZcOnw6NvIG9ydG9nb25hbCBzb2JyZSAkQyhYKSQuIEFzc2ltLCAkXFxoYXR7WX0gPSBQWSQgw6kgbyB2ZXRvciBkZSBwcmVkacOnw6NvLiBPIHJlc8OtZHVvICRlID0gWSAtIFxcaGF0e1l9ID0gKEkgLSBQKVkkIGRldmUgc2VyIG9ydG9nb25hbCBhbyBlc3Bhw6dvICRDKFgpJCBwYXJhIHF1ZSBhIHNvbWEgZG9zIHF1YWRyYWRvcyBkb3MgcmVzw61kdW9zIHNlamEgbWluaW1pemFkYS4gUG9ydGFudG8sICRYJ2UgPSBYJyhJLVApWSA9IChYJyAtIFgnUClZID0gKFgnIC0gWCcoWChYJ1gpXnstMX1YJykpWSA9IChYJyAtIFgnKVkgPSAwJCwgbyBxdWUgcHJvdmEgYSBvcnRvZ29uYWxpZGFkZS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEgJiBFc3RldmVzLCBNb2RlbG9zIExpbmVhcmVzLCBDYXAgNCwgcC4gODUifSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gVGVvcmVtYSBkZSBQaXTDoWdvcmFzIGFwbGljYWRvIMOgIGRlY29tcG9zacOnw6NvIGRvIHZldG9yIGRlIHJlc3Bvc3RhcyAkWSQgZW0gdW0gbW9kZWxvIGxpbmVhci4gU2FiZW5kbyBxdWUgJFNRVG90ID0gfHxZfHxeMiQsICRTUVBhciA9IHx8XFxoYXR7WX18fF4yJCBlICRTUVJlcyA9IHx8ZXx8XjIkLCBlIHF1ZSAkWSA9IFxcaGF0e1l9ICsgZSQgb25kZSAkXFxoYXR7WX0gXFxwZXJwIGUkLCBxdWFsIGRhcyBhZmlybWHDp8O1ZXMgYWJhaXhvIG1lbGhvciByZXByZXNlbnRhIGEgcmVsYcOnw6NvIGdlb23DqXRyaWNhIGVudHJlIGVzc2FzIHNvbWFzIGRlIHF1YWRyYWRvcz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIiRTUVRvdCA9IFNRUGFyIC0gU1FSZXMkLCBpbmRpY2FuZG8gcXVlIG8gcmVzw61kdW8gcmVkdXogYSB2YXJpYWJpbGlkYWRlIHRvdGFsLiIsICJCIjogIiRTUVJlcyA9IFNRVG90ICsgU1FQYXIkLCByZWZsZXRpbmRvIGEgc29tYSBkYXMgbWFnbml0dWRlcyBkb3MgdmV0b3Jlcy4iLCAiQyI6ICIkU1FUb3QgPSBTUVBhciArIFNRUmVzJCwgdsOhbGlkbyBwb3JxdWUgb3Mgc3ViZXNwYcOnb3MgZGUgJFxcaGF0e1l9JCBlICRlJCBzw6NvIG9ydG9nb25haXMuIiwgIkQiOiAiJFNRUGFyID0gU1FUb3QgKyBTUVJlcyQsIHBvaXMgYSBwcm9qZcOnw6NvIHNlbXByZSBhdW1lbnRhIGEgbWFnbml0dWRlIGRvIHZldG9yIG9yaWdpbmFsLiIsICJFIjogIk7Do28gZXhpc3RlIHJlbGHDp8OjbyBsaW5lYXIgZW50cmUgZXNzYXMgc29tYXMgZGUgcXVhZHJhZG9zLCBwb2lzIGVsYXMgZGVwZW5kZW0gZGEgZXNjYWxhIGRvcyBkYWRvcy4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIkNvbnNpZGVyZSBhIG5vcm1hIGV1Y2xpZGlhbmEgYW8gcXVhZHJhZG8gZGUgJFkgPSBcXGhhdHtZfSArIGUkIGUgYXBsaXF1ZSBhIGNvbmRpw6fDo28gZGUgb3J0b2dvbmFsaWRhZGUgJFxcaGF0e1l9J2UgPSAwJC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkRhZG8gJFkgPSBcXGhhdHtZfSArIGUkLCB0ZW1vcyAkfHxZfHxeMiA9IHx8XFxoYXR7WX0gKyBlfHxeMiA9IChcXGhhdHtZfSArIGUpJyhcXGhhdHtZfSArIGUpID0gfHxcXGhhdHtZfXx8XjIgKyB8fGV8fF4yICsgMlxcaGF0e1l9J2UkLiBDb21vICRcXGhhdHtZfSQgw6kgYSBwcm9qZcOnw6NvIGRlICRZJCBlbSAkQyhYKSQgZSAkZSQgw6kgb3J0b2dvbmFsIGEgJEMoWCkkLCB0ZW1vcyAkXFxoYXR7WX0nZSA9IDAkLiBMb2dvLCAkfHxZfHxeMiA9IHx8XFxoYXR7WX18fF4yICsgfHxlfHxeMiQsIG91IHNlamEsICRTUVRvdCA9IFNRUGFyICsgU1FSZXMkLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMCwgM10sIHk9WzAsIDRdLCBtb2RlPSdsaW5lcyttYXJrZXJzJywgbmFtZT1yJ1ZldG9yICRZJCAoJFNRVG90JCknLCBsaW5lPWRpY3QoY29sb3I9JyMwMDAwRkYnLCB3aWR0aD0zKSkpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMCwgM10sIHk9WzAsIDBdLCBtb2RlPSdsaW5lcycsIG5hbWU9cidQcm9qZcOnw6NvICRcXGhhdHtZfSQgKCRTUVBhciQpJywgbGluZT1kaWN0KGNvbG9yPScjODA4MDgwJywgd2lkdGg9MykpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9WzMsIDNdLCB5PVswLCA0XSwgbW9kZT0nbGluZXMnLCBuYW1lPXInUmVzw61kdW8gJGUkICgkU1FSZXMkKScsIGxpbmU9ZGljdChjb2xvcj0nI0ZGMDAwMCcsIHdpZHRoPTMpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdHZW9tZXRyaWEgZGEgRGVjb21wb3Npw6fDo28gZG8gVmV0b3IgUmVzcG9zdGEnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJywgeGF4aXM9ZGljdChmaXhlZHJhbmdlPVRydWUpLCB5YXhpcz1kaWN0KGZpeGVkcmFuZ2U9VHJ1ZSkpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTHVuYSAmIEVzdGV2ZXMsIE1vZGVsb3MgTGluZWFyZXMsIENhcCA0LCBwLiAxMDgifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIGNsw6Fzc2ljbyAkWSA9IFhcXGJldGEgKyBcXERlbHRhJCwgY29tICRcXERlbHRhIFxcc2ltIE4oMCwgXFxzaWdtYV4yIElfbikkLCBzZWphICRQID0gWChYJ1gpXnstMX1YJyQgYSBtYXRyaXogZGUgcHJvamXDp8OjbyBvcnRvZ29uYWwgbm8gc3ViZXNwYcOnbyBkZWZpbmlkbyBwZWxvcyBwcmVkaXRvcmVzLiBDb25zaWRlcmFuZG8gbyB2ZXRvciBkZSByZXPDrWR1b3MgZGVmaW5pZG8gcG9yICRlID0gKEkgLSBQKVkkLCBxdWFsIGRhcyBzZWd1aW50ZXMgYWZpcm1hw6fDtWVzIGRlc2NyZXZlIGNvcnJldGFtZW50ZSBhIGVzdHJ1dHVyYSBkZSBjb3ZhcmnDom5jaWEgZGVzc2VzIHJlc8OtZHVvcyBlIHN1YSBpbXBsaWNhw6fDo28gZXN0YXTDrXN0aWNhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBtYXRyaXogZGUgY292YXJpw6JuY2lhIGRvcyByZXPDrWR1b3Mgw6kgJFZbZV0gPSBcXHNpZ21hXjIgSV9uJCwgaW5kaWNhbmRvIHF1ZSBvcyBlcnJvcyBzw6NvIGluZGVwZW5kZW50ZXMgZSBwb3NzdWVtIHZhcmnDom5jaWEgY29uc3RhbnRlIGlndWFsIGEgJFxcc2lnbWFeMiQuIiwgIkIiOiAiQSBtYXRyaXogZGUgY292YXJpw6JuY2lhIMOpICRWW2VdID0gXFxzaWdtYV4yIChJIC0gUCkkLCBvIHF1ZSBpbXBsaWNhIHF1ZSBvcyByZXPDrWR1b3MgbsOjbyBzw6NvIGluZGVwZW5kZW50ZXMsIGVtYm9yYSB0ZW5oYW0gZXNwZXJhbsOnYSBtYXRlbcOhdGljYSBpZ3VhbCBhIHplcm8uIiwgIkMiOiAiTyBmYXRvIGRlICRWW2VdID0gXFxzaWdtYV4yIChJIC0gUCkkIGRlbW9uc3RyYSBxdWUgb3MgcmVzw61kdW9zIHBvc3N1ZW0gdmFyacOibmNpYSBjb25zdGFudGUgJFxcc2lnbWFeMiQgcGFyYSB0b2RhcyBhcyBvYnNlcnZhw6fDtWVzLCBpbmRlcGVuZGVudGVtZW50ZSBkYSBtYXRyaXogJFgkLiIsICJEIjogIkNvbW8gJFAkIMOpIHVtYSBtYXRyaXogaWRlbXBvdGVudGUsIGEgZXN0cnV0dXJhIGRlIGNvdmFyacOibmNpYSBkb3MgcmVzw61kdW9zIHNpbXBsaWZpY2Etc2UgcGFyYSAkVltlXSA9IDAkLCB2YWxpZGFuZG8gYSBhdXPDqm5jaWEgZGUgZXJybyBlbSBtb2RlbG9zIGRlIHBvc3RvIGNvbXBsZXRvLiIsICJFIjogIkEgY292YXJpw6JuY2lhIGVudHJlIHF1YWlzcXVlciBkb2lzIHJlc8OtZHVvcyAkZV9pJCBlICRlX2okIMOpIHNlbXByZSB6ZXJvLCBnYXJhbnRpbmRvIGEgaG9tb2NlZGFzdGljaWRhZGUgc29iIHF1YWxxdWVyIG1hdHJpeiBkZSBkZXNpZ24gJFgkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIHByb3ByaWVkYWRlICRWW0FZXSA9IEFWW1ldQSckLiBDb21vIGEgbWF0cml6IGRlIHByb2plw6fDo28gJFAkIMOpIGlkZW1wb3RlbnRlIGUgc2ltw6l0cmljYSwgYW5hbGlzZSBjb21vICRJLVAkIGludGVyYWdlIGNvbSBhIHZhcmnDom5jaWEgZGUgJFkkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBtYXRyaXogZGUgY292YXJpw6JuY2lhIGRvcyByZXPDrWR1b3Mgw6kgJFZbZV0gPSBWWyhJIC0gUClZXSA9IChJIC0gUClWW1ldKEkgLSBQKScgPSAoSSAtIFApKFxcc2lnbWFeMiBJX24pKEkgLSBQKScgPSBcXHNpZ21hXjIgKEkgLSBQKShJIC0gUCkgPSBcXHNpZ21hXjIgKEkgLSBQKSQuIENvbW8gJFAkIG7Do28gw6kgZ2VyYWxtZW50ZSBhIG1hdHJpeiBudWxhLCBvcyBlbGVtZW50b3MgZm9yYSBkYSBkaWFnb25hbCBkZSAkKEkgLSBQKSQgbsOjbyBzw6NvIG5lY2Vzc2FyaWFtZW50ZSB6ZXJvLCBvIHF1ZSBzaWduaWZpY2EgcXVlIG9zIHJlc8OtZHVvcyBhbW9zdHJhaXMgc8OjbyBjb3JyZWxhY2lvbmFkb3MgZW50cmUgc2ksIHJlZmxldGluZG8gYSByZXN0cmnDp8OjbyBpbXBvc3RhIHBlbG8gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gc29icmUgb3MgZGFkb3MuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBhbmFsaXN0YSBkZSBkYWRvcyBlc3TDoSB2YWxpZGFuZG8gdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIGUgb2JzZXJ2YSBxdWUsIGFvIHBsb3RhciBvcyByZXPDrWR1b3MgJGVfaSQgY29udHJhIG9zIHZhbG9yZXMgcHJldmlzdG9zICRcXGhhdHtZfV9pJCwgb3MgcmVzw61kdW9zIGV4aWJlbSB1bSBwYWRyw6NvIGRlICdmdW5pbCcgKHZhcmnDom5jaWEgY3Jlc2NlbnRlIGNvbmZvcm1lIG8gdmFsb3IgcHJldmlzdG8gYXVtZW50YSkuIFNlZ3VuZG8gYSB0ZW9yaWEgZGUgR2F1c3MtTWFya292IGUgYXMgcHJvcHJpZWRhZGVzIGNsw6Fzc2ljYXMgZG9zIHJlc8OtZHVvcywgY29tbyBlc3NlIGZlbsO0bWVubyBjb250cmFkaXogb3MgcHJlc3N1cG9zdG9zIGRvIG1vZGVsbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gZmVuw7RtZW5vIHZpb2xhIGEgcHJvcHJpZWRhZGUgZGUgJEVbZV0gPSAwJCwgaW5kaWNhbmRvIHF1ZSBvIG1vZGVsbyBwb3NzdWkgdmnDqXMgc2lzdGVtw6F0aWNvIGRlIHN1YmVzdGltYcOnw6NvLiIsICJCIjogIk8gZmVuw7RtZW5vIGluZGljYSBxdWUgYSBtYXRyaXogZGUgcHJvamXDp8OjbyAkUCQgbsOjbyDDqSBpZGVtcG90ZW50ZSwgaW52YWxpZGFuZG8gYSBwcm9qZcOnw6NvIG9ydG9nb25hbC4iLCAiQyI6ICJPIHBhZHLDo28gdmlvbGEgYSBwcmVzc3Vwb3Npw6fDo28gZGUgaG9tb2NlZGFzdGljaWRhZGUsIHBvaXMgYSB2YXJpw6JuY2lhIGRvcyBlcnJvcyBuw6NvIMOpIGNvbnN0YW50ZSwgbyBxdWUgaW1wbGljYSBxdWUgJFZbZV0gXFxuZXEgXFxzaWdtYV4yKEkgLSBQKSQgc2UgYXNzdW1pcm1vcyBhIGZvcm1hIGNsw6Fzc2ljYS4iLCAiRCI6ICJPIHBhZHLDo28gw6kgZXNwZXJhZG8gZW0gbW9kZWxvcyBsaW5lYXJlcyBjbMOhc3NpY29zLCB2aXN0byBxdWUgbyByZXPDrWR1byBkZXZlIGFic29ydmVyIGEgaGV0ZXJvY2VkYXN0aWNpZGFkZSBpbnRyw61uc2VjYSBkb3MgcHJlZGl0b3Jlcy4iLCAiRSI6ICJPIGZlbsO0bWVubyBwcm92YSBxdWUgbyBlc3RpbWFkb3IgZGUgbcOtbmltb3MgcXVhZHJhZG9zIG9yZGluw6FyaW9zIMOpIG8gbWFpcyBlZmljaWVudGUgKEJMVUUpLCBtZXNtbyBuYSBwcmVzZW7Dp2EgZGUgdmFyacOibmNpYSBuw6NvIGNvbnN0YW50ZS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIlBlbnNlIG5hIGRlZmluacOnw6NvIGRlIGhvbW9jZWRhc3RpY2lkYWRlIG5vIG1vZGVsbyBjbMOhc3NpY286ICRcXERlbHRhIFxcc2ltIE4oMCwgXFxzaWdtYV4yIElfbikkLiBPIHF1ZSBhY29udGVjZSBjb20gZXNzYSBtYXRyaXogZGUgY292YXJpw6JuY2lhIHNlIGEgdmFyacOibmNpYSBuw6NvIGZvciBjb25zdGFudGU/IiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJObyBtb2RlbG8gY2zDoXNzaWNvLCBhc3N1bWUtc2UgJFZbXFxEZWx0YV0gPSBcXHNpZ21hXjIgSV9uJCAoaG9tb2NlZGFzdGljaWRhZGUpLiBPIHBhZHLDo28gZGUgZnVuaWwgaW5kaWNhIGhldGVyb2NlZGFzdGljaWRhZGUsIG9uZGUgYSB2YXJpw6JuY2lhIGRvIGVycm8gZGVwZW5kZSBkZSAkXFxoYXR7WX1faSQgb3UgZG9zIHByZWRpdG9yZXMgJFgkLiBJc3NvIGNvbnRyYWRpeiBhIHByZW1pc3NhIGRlIHZhcmnDom5jaWEgY29uc3RhbnRlLCBpbnZhbGlkYW5kbyBhIGVzdHJ1dHVyYSBkZSBjb3ZhcmnDom5jaWEgJFxcc2lnbWFeMihJIC0gUCkkIGRlcml2YWRhIHBhcmEgbyBtb2RlbG8gY2zDoXNzaWNvLCBlIHN1Z2VyaW5kbyBxdWUgbyBlc3RpbWFkb3IgZGUgbcOtbmltb3MgcXVhZHJhZG9zIG9yZGluw6FyaW9zIHBlcmRlIHN1YSBlZmljacOqbmNpYSAobsOjbyDDqSBtYWlzIG8gQkxVRSkuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVsxMCwgMTUsIDIwLCAyNSwgMzAsIDM1LCA0MF0sIHk9WzIsIC0zLCA1LCAtOCwgMTAsIC0xNSwgMjBdLCBtb2RlPSdtYXJrZXJzJywgbmFtZT0nUmVzw61kdW9zJykpXG5maWcudXBkYXRlX2xheW91dCh0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJywgdGl0bGU9J0Fuw6FsaXNlIGRlIFJlc8OtZHVvczogSGV0ZXJvY2VkYXN0aWNpZGFkZScsIHhheGlzX3RpdGxlPSdWYWxvcmVzIFByZXZpc3RvcyAoJFxcaGF0e1l9X2kkKScsIHlheGlzX3RpdGxlPSdSZXPDrWR1b3MgKCRlX2kkKScsIGhlaWdodD00MDApIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTUifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIHNpbXBsZXMgJFkgPSBYXGJldGEgKyBcdGV4dHvOlH0kLCBvbmRlIGEgbWF0cml6IGRlIGRlc2lnbiAkWCQgcG9zc3VpIHVtIHBvbnRvIGNvbSB2YWxvciBkZSBhbGF2YW5jYWdlbSAkaF9pJCBtdWl0byBwcsOzeGltbyBkZSAkMSQsIGNvbW8gbyBjb21wb3J0YW1lbnRvIGRvIHJlc8OtZHVvIGJydXRvICRlX2kkIGRpZmVyZSBkbyByZXPDrWR1byBwYWRyb25pemFkbyAkcl9pJCBuYSBkZXRlY8Onw6NvIGRlIG91dGxpZXJzPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyByZXPDrWR1byBicnV0byAkZV9pJCB0ZW5kZSBhIHNlciBzdXBlcmVzdGltYWRvIGVtIHBvbnRvcyBkZSBhbHRhIGFsYXZhbmNhZ2VtLCB0b3JuYW5kbyBhIGlkZW50aWZpY2HDp8OjbyBkZSBvdXRsaWVycyDDs2J2aWEgc2VtIGEgbmVjZXNzaWRhZGUgZGUgcGFkcm9uaXphw6fDo28uIiwgIkIiOiAiTyByZXPDrWR1byBwYWRyb25pemFkbyAkcl9pJCBjb21wZW5zYSBhIHZhcmlhYmlsaWRhZGUgcmVkdXppZGEgZW0gcG9udG9zIGRlIGFsdGEgYWxhdmFuY2FnZW0gZGl2aWRpbmRvIG8gZXJybyBwb3IgJFxcaGF0e1xcc2lnbWF9XFxzcXJ0ezEgLSBoX2l9JCwgcGVybWl0aW5kbyB1bWEgY29tcGFyYcOnw6NvIGp1c3RhIGVudHJlIG9ic2VydmHDp8O1ZXMuIiwgIkMiOiAiTyByZXPDrWR1byBicnV0byAkZV9pJCDDqSBzZW1wcmUgbWFpcyBlZmljaWVudGUgcXVlIG8gcmVzw61kdW8gc3R1ZGVudGl6YWRvICR0X2kkIHBvaXMgbsOjbyBkZXBlbmRlIGRhIGVzdGltYXRpdmEgZGUgJFxcaGF0e1xcc2lnbWF9X3soaSl9JCBxdWUgb21pdGUgbyBwb250byBpLiIsICJEIjogIk7Do28gaMOhIGRpZmVyZW7Dp2EgdGXDs3JpY2EsIHBvaXMgYW1ib3MgcG9zc3VlbSB2YXJpw6JuY2lhIGNvbnN0YW50ZSBpZ3VhbCBhICRcXHNpZ21hXjIkIGluZGVwZW5kZW50ZSBkYSBwb3Npw6fDo28gbmEgbWF0cml6IGRlIGRlc2lnbiAkWCQuIiwgIkUiOiAiTyByZXPDrWR1byBzdHVkZW50aXphZG8gJHRfaSQgw6kgc2VtcHJlIG1lbm9yIHF1ZSBvIHJlc8OtZHVvIHBhZHJvbml6YWRvICRyX2kkIHBhcmEgb2JzZXJ2YcOnw7VlcyBpbmZsdWVudGVzLCBpbnZhbGlkYW5kbyBvIHVzbyBkZSAkdF9pJCBwYXJhIGRpYWduw7NzdGljby4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgJFZbZV0gPSBcXHNpZ21hXjIoSSAtIFApJC4gTyBxdWUgYWNvbnRlY2UgY29tIGEgdmFyacOibmNpYSBkZSB1bSByZXPDrWR1byBlc3BlY8OtZmljbyAkZV9pJCBxdWFuZG8gJGhfaSQgYXVtZW50YT8iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBlbGEgZGVmaW5pw6fDo28sIGEgdmFyacOibmNpYSBkbyAkaSQtw6lzaW1vIHJlc8OtZHVvIGJydXRvIMOpICRWYXIoZV9pKSA9IFxcc2lnbWFeMigxIC0gaF9pKSQuIE9ic2VydmHDp8O1ZXMgY29tIGFsdGEgYWxhdmFuY2FnZW0gKCRoX2kkIHByw7N4aW1vIGRlIDEpIGZvcsOnYW0gJFZhcihlX2kpJCBhIHNlIGFwcm94aW1hciBkZSB6ZXJvLiBJc3NvIHNpZ25pZmljYSBxdWUgbyBtb2RlbG8gc2UgYWp1c3RhIHF1YXNlIHBlcmZlaXRhbWVudGUgYSBlc3NlcyBwb250b3MsIG9jdWx0YW5kbyBwb3Nzw612ZWlzIGRlc3Zpb3MuIE8gcmVzw61kdW8gcGFkcm9uaXphZG8gJHJfaSA9IFxcZnJhY3tlX2l9e1xcaGF0e1xcc2lnbWF9IFxcc3FydHsxIC0gaF9pfX0kIGRpdmlkZSBvIHJlc8OtZHVvIHBlbG8gc2V1IGRlc3ZpbyBwYWRyw6NvIGVzdGltYWRvLCBlc2NhbG9uYW5kby1vIHBhcmEgdW1hIGVzY2FsYSBvbmRlIGEgdmFyacOibmNpYSDDqSB1bml0w6FyaWEsIHBlcm1pdGluZG8gaWRlbnRpZmljYXIgbyBvdXRsaWVyIHF1ZSBhbnRlcyBlc3RhdmEgbWFzY2FyYWRvLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gZGlhZ27Ds3N0aWNvIGRlIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvIG3Dumx0aXBsYSBjb20gJG49NTAkIG9ic2VydmHDp8O1ZXMgZSAkcD01JCBwYXLDom1ldHJvcyAoaW5jbHVpbmRvIG8gaW50ZXJjZXB0bykuIFNlIHVtIGRldGVybWluYWRvIHBvbnRvICRpJCBhcHJlc2VudGEgdW0gcmVzw61kdW8gcGFkcm9uaXphZG8gJHJfaSA9IDMkLCBxdWFsIGRhcyBhZmlybWHDp8O1ZXMgYWJhaXhvIG1lbGhvciBkZXNjcmV2ZSBvIHVzbyBkbyByZXPDrWR1byBzdHVkZW50aXphZG8gJHRfaSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIHZhbG9yIGRlICR0X2kkIHNlcsOhIG1lbm9yIHF1ZSAzLCBwb2lzIGEgZXhjbHVzw6NvIGRhIG9ic2VydmHDp8OjbyAkaSQgbm8gY8OhbGN1bG8gZGEgdmFyacOibmNpYSByZXNpZHVhbCBzZW1wcmUgcmVkdXogbyByZXPDrWR1by4iLCAiQiI6ICJPIHZhbG9yIGRlICR0X2kkIHNlcsOhIG9icmlnYXRvcmlhbWVudGUgbWFpb3IgcXVlIDMsIHVtYSB2ZXogcXVlIGEgZXN0aW1hdGl2YSAkXFxoYXR7XFxzaWdtYX1feyhpKX0kIMOpIGdlcmFsbWVudGUgbWVub3IgZG8gcXVlICRcXGhhdHtcXHNpZ21hfSQgcXVhbmRvIHVtIG91dGxpZXIgw6kgcmVtb3ZpZG8uIiwgIkMiOiAiTyB2YWxvciBkZSAkdF9pJCBzZXJpYSBpbmNhbGN1bMOhdmVsLCBwb2lzIGEgZsOzcm11bGEgZXhpZ2UgcXVlICRuIC0gcCAtIHJfaV4yID4gMCQsIG8gcXVlIG7Do28gw6kgc2F0aXNmZWl0byBhcXVpLiIsICJEIjogIk8gcmVzw61kdW8gc3R1ZGVudGl6YWRvICR0X2kkIMOpIGRlc25lY2Vzc8OhcmlvIHNlICRyX2kgPiAyJCwgYmFzdGFuZG8gdXRpbGl6YXIgYSByZWdyYSBlbXDDrXJpY2EgZGEgbm9ybWFsaWRhZGUuIiwgIkUiOiAiTyByZXPDrWR1byAkdF9pJCBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gJEYoMSwgbi1wKSQgZSDDqSB1dGlsaXphZG8gcGFyYSB0ZXN0YXIgYSBzaWduaWZpY8OibmNpYSBkbyBwYXLDom1ldHJvICRcXGJldGFfaSQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJBbmFsaXNlIGEgZsOzcm11bGEgJHRfaSA9IHJfaSBcXHNxcnR7XFxmcmFje24tcC0xfXtuLXAtcl9pXjJ9fSQuIE9ic2VydmUgY29tbyBhIHJlbW/Dp8OjbyBkZSB1bSBwb250byBpbmZsdWVudGUgYWZldGEgYSBzb21hIGRlIHF1YWRyYWRvcyBkbyBlcnJvICRTUVJlcyQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJRdWFuZG8gdW1hIG9ic2VydmHDp8OjbyDDqSB1bSBvdXRsaWVyLCBlbGEgaW5mbGEgbyAkU1FSZXMkIGdsb2JhbC4gQW8gcmVtb3bDqi1sYSwgYSBub3ZhIHZhcmnDom5jaWEgZXN0aW1hZGEgJFxcaGF0e1xcc2lnbWF9X3soaSl9XjIkIGNvc3R1bWEgc2VyIG1lbm9yIHF1ZSBhIHZhcmnDom5jaWEgb3JpZ2luYWwgJFxcaGF0e1xcc2lnbWF9XjIkLiBDb21vICR0X2kkIHV0aWxpemEgJFxcaGF0e1xcc2lnbWF9X3soaSl9JCBubyBkZW5vbWluYWRvciwgZSBlc3RlIMOpIG1lbm9yLCBvIHJlc3VsdGFkbyBkYSBkaXZpc8OjbyBhdW1lbnRhLCByZXN1bHRhbmRvIGVtIHVtIHJlc8OtZHVvIHN0dWRlbnRpemFkbyBjb20gdmFsb3IgYWJzb2x1dG8gbWFpb3IgcXVlIG8gcmVzw61kdW8gcGFkcm9uaXphZG8sIHRvcm5hbmRvIG8gb3V0bGllciBtYWlzIGV2aWRlbnRlIHBhcmEgbyBhbmFsaXN0YS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtIGVuZ2VuaGVpcm8gZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlIGVzdMOhIGFuYWxpc2FuZG8gYSByZWxhw6fDo28gZW50cmUgYSB0ZW1wZXJhdHVyYSBkZSB1bSBwcm9jZXNzbyBpbmR1c3RyaWFsICgkWF8xJCkgZSBhIHJlc2lzdMOqbmNpYSBmaW5hbCBkbyBwb2zDrW1lcm8gcHJvZHV6aWRvICgkWSQpLiBBcMOzcyBhanVzdGFyIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvIGxpbmVhciBzaW1wbGVzICRZID0gXGJldGFfMCArIFxiZXRhXzEgWF8xICsgXHRleHR7XHRleHREZWx0YX0kLCBlbGUgYW5hbGlzYSBvIGdyw6FmaWNvIGRlIHJlc8OtZHVvcyAkZV9pJCBlbSBmdW7Dp8OjbyBkb3MgdmFsb3JlcyBhanVzdGFkb3MgJFxcaGF0e1l9X2kkLiBFbGUgb2JzZXJ2YSBxdWUgb3MgcG9udG9zIGZvcm1hbSB1bSBwYWRyw6NvIGRlICdhcmNvJyBvdSAnVScgY2xhcmFtZW50ZSBkZWZpbmlkbywgY29tIG9zIHJlc8OtZHVvcyBuZWdhdGl2b3MgbmFzIGV4dHJlbWlkYWRlcyBlIHBvc2l0aXZvcyBubyBjZW50cm8gKG91IHZpY2UtdmVyc2EpLiBRdWFsIMOpIGEgY29uY2x1c8OjbyBlc3RhdMOtc3RpY2EgbWFpcyBhZGVxdWFkYSBwYXJhIGVzdGUgZGlhZ27Ds3N0aWNvIHZpc3VhbD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gbW9kZWxvIGVzdMOhIGJlbSBlc3BlY2lmaWNhZG8sIHBvaXMgb3MgcmVzw61kdW9zIGVzdMOjbyBjZW50cmFkb3MgZW0gemVyby4iLCAiQiI6ICJIw6EgZXZpZMOqbmNpYSBkZSBoZXRlcm9jZWRhc3RpY2lkYWRlLCBwb2lzIGEgdmFyacOibmNpYSBkb3MgcmVzw61kdW9zIG7Do28gw6kgY29uc3RhbnRlIGFvIGxvbmdvIGRlICRcXGhhdHtZfV9pJC4iLCAiQyI6ICJPIG1vZGVsbyBhcHJlc2VudGEgZmFsdGEgZGUgbGluZWFyaWRhZGUsIHN1Z2VyaW5kbyBxdWUgdW1hIHJlbGHDp8OjbyBuw6NvIGxpbmVhciAoZXg6IHF1YWRyw6F0aWNhKSBwb2RlIHNlciBtYWlzIGFwcm9wcmlhZGEuIiwgIkQiOiAiT3MgZGFkb3MgYXByZXNlbnRhbSBhdXRvY29ycmVsYcOnw6NvIHNlcmlhbCwgaW5kaWNhbmRvIHF1ZSBvIHByb2Nlc3NvIG7Do28gw6kgaW5kZXBlbmRlbnRlLiIsICJFIjogIk8gbW9kZWxvIMOpIHJvYnVzdG8sIHBvaXMgbyBwYWRyw6NvIGVtICdVJyDDqSBlc3BlcmFkbyBlbSBhbW9zdHJhcyBwZXF1ZW5hcy4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgbyBncsOhZmljbyBkZSByZXPDrWR1b3MgdmVyc3VzIHZhbG9yZXMgYWp1c3RhZG9zIHNlcnZlIHBhcmEgdmVyaWZpY2FyIHNlIGEgZXN0cnV0dXJhIHNpc3RlbcOhdGljYSAobyBFW1l8WF0pIGZvaSB0b3RhbG1lbnRlIGNhcHR1cmFkYSBwZWxvIG1vZGVsby4gUGFkcsO1ZXMgZ2VvbcOpdHJpY29zIGluZGljYW0gcXVlIGEgbcOpZGlhIGNvbmRpY2lvbmFsIG7Do28gw6kgemVyby4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgb2JzZXJ2YcOnw6NvIGRlIHVtIHBhZHLDo28gZW0gZm9ybWF0byBkZSBhcmNvIG91ICdVJyBubyBncsOhZmljbyBkZSByZXPDrWR1b3MgY29udHJhIHZhbG9yZXMgYWp1c3RhZG9zIMOpIHVtIGRpYWduw7NzdGljbyBjbMOhc3NpY28gZGUgZmFsdGEgZGUgbGluZWFyaWRhZGUgKG5vbi1saW5lYXJpdHkpLiBJc3NvIGluZGljYSBxdWUgYSByZWxhw6fDo28gZW50cmUgYSB2YXJpw6F2ZWwgcmVzcG9zdGEgJFkkIGUgbyBwcmVkaXRvciAkWCQgcG9zc3VpIHVtYSBjdXJ2YXR1cmEgcXVlIG7Do28gZXN0w6Egc2VuZG8gY29udGVtcGxhZGEgcGVsbyBtb2RlbG8gbGluZWFyICRZID0gXGJldGFfMCArIFxiZXRhXzEgWF8xICsgXHRleHR7XHRleHREZWx0YX0kLiBQb3J0YW50bywgbyB0ZXJtbyBkZSBlcnJvIGFwcmVzZW50YSB1bWEgZXN0cnV0dXJhIHNpc3RlbcOhdGljYSwgdmlvbGFuZG8gYSBwcmVtaXNzYSBkZSBxdWUgJEVbZV9pIHwgXHRleHR7XHRleHREZWx0YX1dID0gMCQuIEEgYWx0ZXJuYXRpdmEgQyDDqSBhIGNvcnJldGEsIHBvaXMgYXBvbnRhIGEgbmVjZXNzaWRhZGUgZGUgcmVlc3BlY2lmaWNhw6fDo28gZG8gbW9kZWxvIChjb21vIGEgaW5jbHVzw6NvIGRlIHRlcm1vcyBwb2xpbm9taWFpcykuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVsxMCwgMTUsIDIwLCAyNSwgMzAsIDM1LCA0MF0sIHk9LCBtb2RlPSdtYXJrZXJzJywgbWFya2VyPWRpY3QoY29sb3I9JyMwMDAwRkYnKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nR3LDoWZpY28gZGUgUmVzw61kdW9zIHZlcnN1cyBWYWxvcmVzIEFqdXN0YWRvcycsIHhheGlzPWRpY3QodGl0bGU9J1ZhbG9yZXMgQWp1c3RhZG9zICgkXFxoYXR7WX1faSQpJywgZml4ZWRyYW5nZT1UcnVlKSwgeWF4aXM9ZGljdCh0aXRsZT0nUmVzw61kdW9zICgkZV9pJCknLCBmaXhlZHJhbmdlPVRydWUpLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJylcbmZpZy5hZGRfc2hhcGUodHlwZT0nbGluZScsIHgwPTEwLCB5MD0wLCB4MT00MCwgeTE9MCwgbGluZT1kaWN0KGNvbG9yPScjRkYwMDAwJywgZGFzaD0nZGFzaCcpKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkZhcmF3YXksIExpbmVhciBNb2RlbHMgd2l0aCBSLCBDYXAgNywgcC4gODAtODUifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW1hIGFuw6FsaXNlIGRlIHJlZ3Jlc3PDo28gbGluZWFyIHBhcmEgcHJldmVyIGdhc3RvcyBkZSBzYcO6ZGUsIGFvIHBsb3RhciBvcyByZXPDrWR1b3MgZXN0dWRlbnRpemFkb3MgKCRlX2kkKSBjb250cmEgb3MgdmFsb3JlcyBhanVzdGFkb3MgKCRcXGhhdHtZfV9pJCksIHVtIHBlc3F1aXNhZG9yIG5vdGEgcXVlIGEgZGlzcGVyc8OjbyBkb3MgcG9udG9zIGF1bWVudGEgcHJvZ3Jlc3NpdmFtZW50ZSDDoCBtZWRpZGEgcXVlICRcXGhhdHtZfV9pJCBjcmVzY2UsIGZvcm1hbmRvIHVtIHBhZHLDo28gZGUgJ2Z1bmlsJyBvdSAnbGVxdWUnLiBPIHF1ZSBlc3RlIGNvbXBvcnRhbWVudG8gdmlzdWFsIGltcGxpY2EgcGFyYSBhcyBzdXBvc2nDp8O1ZXMgZG8gbW9kZWxvIGxpbmVhciBjbMOhc3NpY28/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIG1vZGVsbyBhdGVuZGUgcGVyZmVpdGFtZW50ZSBhb3MgcHJlc3N1cG9zdG9zIGRlIEdhdXNzLU1hcmtvdi4iLCAiQiI6ICJPIG1vZGVsbyBzb2ZyZSBkZSBoZXRlcm9jZWRhc3RpY2lkYWRlLCBpbnZhbGlkYW5kbyBhIHByZW1pc3NhIGRlIHZhcmnDom5jaWEgY29uc3RhbnRlIGRvcyBlcnJvcyAoJFxcc2lnbWFeMiQpLiIsICJDIjogIk8gbW9kZWxvIGFwcmVzZW50YSBhbHRhIGNvbGluZWFyaWRhZGUgZW50cmUgb3MgcHJlZGl0b3Jlcy4iLCAiRCI6ICJPIG1vZGVsbyDDqSBob21vY2Vkw6FzdGljbywgbWFzIG9zIHJlc8OtZHVvcyBuw6NvIHNlZ3VlbSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLiIsICJFIjogIkEgaW5jbGluYcOnw6NvIGRhIHJldGEgZGUgcmVncmVzc8OjbyBlc3TDoSBzdWJlc3RpbWFkYSwgbWFzIGEgdmFyacOibmNpYSDDqSBjb25zdGFudGUuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJDb25zaWRlcmUgYSBwcmVtaXNzYSBkZSBob21vc2NlZGFzdGljaWRhZGUgZG8gbW9kZWxvICRZID0gWFxcYmV0YSArIFx0ZXh0e1x0ZXh0RGVsdGF9JCwgb25kZSAkXFx0ZXh0e1x0ZXh0RGVsdGF9IFxcc2ltIE4oMCwgXFxzaWdtYV4yIElfbikkLiBPIHF1ZSBhY29udGVjZSBzZSBhIHZhcmnDom5jaWEgZG9zIGVycm9zIG7Do28gZm9yIGNvbnN0YW50ZT8iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgaG9tb3NjZWRhc3RpY2lkYWRlIHByZXNzdXDDtWUgcXVlICRWW1xcdGV4dHtcdGV4dERlbHRhfV9pXSA9IFxcc2lnbWFeMiQgcGFyYSB0b2RvICRpJC4gUXVhbmRvIHZpc3VhbGl6YW1vcyB1bSBlZmVpdG8gZGUgJ2Z1bmlsJyBvdSAnbGVxdWUnIG5vIGdyw6FmaWNvIGRlIHJlc8OtZHVvcyB2ZXJzdXMgdmFsb3JlcyBhanVzdGFkb3MsIG9ic2VydmFtb3MgcXVlIGEgZGlzcGVyc8OjbyBkb3MgcmVzw61kdW9zIChhIHZhcmlhYmlsaWRhZGUpIGNyZXNjZSBjb25mb3JtZSBvcyB2YWxvcmVzIGFqdXN0YWRvcyBhdW1lbnRhbS4gSXNzbyDDqSB1bSBzaW5hbCBjbGFybyBkZSBoZXRlcm9jZWRhc3RpY2lkYWRlLiBBIGhldGVyb2NlZGFzdGljaWRhZGUgdmlvbGEgYSBwcmVtaXNzYSBiw6FzaWNhIGRhIHJlZ3Jlc3PDo28gZGUgbcOtbmltb3MgcXVhZHJhZG9zIG9yZGluw6FyaW9zLCBhZmV0YW5kbyBhIHByZWNpc8OjbyBkYXMgZXN0aW1hdGl2YXMgZSBhIHZhbGlkYWRlIGRvcyB0ZXN0ZXMgZGUgaGlww7N0ZXNlcywgcG9pcyBhcyB2YXJpw6JuY2lhcyBkb3MgZXN0aW1hZG9yZXMgbsOjbyBzZXLDo28gbWFpcyDDs3RpbWFzLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMTAsIDIwLCAzMCwgNDAsIDUwLCA2MF0sIHk9WzEsIC0xLCAyLCAtMiwgMywgLTNdLCBtb2RlPSdtYXJrZXJzJywgbWFya2VyPWRpY3QoY29sb3I9JyMwMDAwRkYnKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nRGlhZ27Ds3N0aWNvIGRlIEhldGVyb2NlZGFzdGljaWRhZGUnLCB4YXhpcz1kaWN0KHRpdGxlPSdWYWxvcmVzIEFqdXN0YWRvcyAoJFxcaGF0e1l9X2kkKScsIGZpeGVkcmFuZ2U9VHJ1ZSksIHlheGlzPWRpY3QodGl0bGU9J1Jlc8OtZHVvcyAoJGVfaSQpJywgZml4ZWRyYW5nZT1UcnVlKSwgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpXG5maWcuYWRkX3NoYXBlKHR5cGU9J2xpbmUnLCB4MD0xMCwgeTA9MCwgeDE9NjAsIHkxPTAsIGxpbmU9ZGljdChjb2xvcj0nI0ZGMDAwMCcsIGRhc2g9J2Rhc2gnKSkiLCAicmVmZXJlbmNpYV9saXZybyI6ICJGYXJhd2F5LCBMaW5lYXIgTW9kZWxzIHdpdGggUiwgQ2FwIDcsIHAuIDgzLTg0In0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBkZSBvdGltaXphw6fDo28gZGUgcHJvY2Vzc29zIGluZHVzdHJpYWlzLCB1bSBlbmdlbmhlaXJvIGVzdGltb3UgdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIHBhcmEgcHJldmVyIG8gdGVtcG8gZGUgY2ljbG8gKCRcXGhhdHtZfSQpIGRlIHVtYSBtw6FxdWluYSBjb20gYmFzZSBuYSB0ZW1wZXJhdHVyYSBvcGVyYWNpb25hbCAoJFgkKS4gQXDDs3MgYSBlc3RpbWHDp8OjbywgbyBhbmFsaXN0YSBwcm9jZWRldSBjb20gYSB2ZXJpZmljYcOnw6NvIGRhIHByZW1pc3NhIGRlIG5vcm1hbGlkYWRlIGRvcyByZXPDrWR1b3MgKCRcXERlbHRhJCkgdXRpbGl6YW5kbyBvIGdyw6FmaWNvIFF1YW50aWwtUXVhbnRpbCAoUS1RIHBsb3QpLiBBbyBvYnNlcnZhciBvIGdyw6FmaWNvLCBvIGVuZ2VuaGVpcm8gbm90b3UgcXVlIG9zIHBvbnRvcyBuYXMgZXh0cmVtaWRhZGVzIGVzcXVlcmRhIGUgZGlyZWl0YSBkbyBncsOhZmljbyBzZSBkaXN0YW5jaWFtIGRhIGxpbmhhIHRlw7NyaWNhIGRlIHJlZmVyw6puY2lhLCBjdXJ2YW5kby1zZSBwYXJhIGZvcmEsIGRlIG1vZG8gcXVlIG9zIHJlc8OtZHVvcyBwYWRyb25pemFkb3MgJHJfaSQgc8OjbyBtYWlzIGV4dHJlbW9zIGRvIHF1ZSBvcyBxdWFudGlzIHRlw7NyaWNvcyAkel97KGkpfSQgZXNwZXJhZG9zIHBhcmEgdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbC4gUXVhbCDDqSBhIGludGVycHJldGHDp8OjbyBlc3RhdMOtc3RpY2EgbWFpcyBhZGVxdWFkYSBwYXJhIGVzdGUgY29tcG9ydGFtZW50byBkb3MgcmVzw61kdW9zPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiT3MgcmVzw61kdW9zIGFwcmVzZW50YW0gdW1hIGRpc3RyaWJ1acOnw6NvIGNvbSBjYXVkYXMgbWFpcyBwZXNhZGFzIChsZXB0b2PDunJ0aWNhKSBkbyBxdWUgYSBkaXN0cmlidWnDp8OjbyBub3JtYWwsIGluZGljYW5kbyB1bWEgbWFpb3IgcHJvYmFiaWxpZGFkZSBkZSBvYnNlcnZhw6fDo28gZGUgb3V0bGllcnMuIiwgIkIiOiAiTyBtb2RlbG8gZXN0w6Egc29mcmVuZG8gZGUgaGV0ZXJvY2VkYXN0aWNpZGFkZSwgcG9pcyBhIHZhcmlhw6fDo28gZG9zIHJlc8OtZHVvcyBwYWRyb25pemFkb3MgYXVtZW50YSBzaXN0ZW1hdGljYW1lbnRlIGNvbSBhIG1hZ25pdHVkZSBkb3MgcXVhbnRpcyB0ZcOzcmljb3MuIiwgIkMiOiAiT3MgcmVzw61kdW9zIHNlZ3VlbSB1bWEgZGlzdHJpYnVpw6fDo28gYXNzaW3DqXRyaWNhIHBvc2l0aXZhLCBzZW5kbyBlc3RlIG8gZGlhZ27Ds3N0aWNvIHZpc3VhbCBwYWRyw6NvIHBhcmEgYSBmYWxoYSBuYSBzdXBvc2nDp8OjbyBkZSBtw6lkaWEgemVybyBkbyB2ZXRvciBkZSBlcnJvcyAkXFxEZWx0YSQuIiwgIkQiOiAiTyBncsOhZmljbyBpbmRpY2EgcXVlIG8gdGFtYW5obyBhbW9zdHJhbCAkbiQgw6kgaW5zdWZpY2llbnRlIHBhcmEgYSBhcGxpY2HDp8OjbyBkbyB0ZW9yZW1hIGNlbnRyYWwgZG8gbGltaXRlLCBpbXBvc3NpYmlsaXRhbmRvIHF1YWxxdWVyIGNvbmNsdXPDo28gc29icmUgYSBkaXN0cmlidWnDp8OjbyBkb3MgcmVzw61kdW9zLiIsICJFIjogIkEgaW5jbGluYcOnw6NvIGRhIHJldGEgb2JzZXJ2YWRhIGluZGljYSBxdWUgYSB2YXJpw6JuY2lhIGRvcyBlcnJvcyDDqSBpZ3VhbCDDoCB1bmlkYWRlLCBjb25maXJtYW5kbyBhIG5vcm1hbGlkYWRlIGVzdHJpdGEgZG8gcHJvY2Vzc28gZXN0b2PDoXN0aWNvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBvIFEtUSBwbG90IGNvbXBhcmEgYSBkaXN0cmlidWnDp8OjbyBvYnNlcnZhZGEgY29tIGEgdGXDs3JpY2EuIERlc3Zpb3MgbmFzIGV4dHJlbWlkYWRlcyBwYXJhIGZvcmEgZGEgbGluaGEgcmV0YSBpbmRpY2FtIHF1ZSBvcyBkYWRvcyByZWFpcyAnZXN0aWNhbScgbWFpcyBkbyBxdWUgYSBub3JtYWwgbmFzIGNhdWRhcy4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIk5vIFEtUSBwbG90LCBzZSBvcyBwb250b3Mgc2UgYWZhc3RhbSBkYSByZXRhIGRlIHJlZmVyw6puY2lhIG5hcyBleHRyZW1pZGFkZXMgKGZvcm1hbmRvIHVtYSBjdXJ2YSBlbSAnUycgb3Ugc2FpbmRvIHBhcmEgZm9yYSksIGlzc28gZXZpZGVuY2lhIHF1ZSBhIGRpc3RyaWJ1acOnw6NvIGRvcyByZXPDrWR1b3MgcG9zc3VpIGNhdWRhcyBtYWlzICdwZXNhZGFzJyBxdWUgYSBub3JtYWwuIElzc28gc2lnbmlmaWNhIHF1ZSBhIGN1cnRvc2UgZGEgZGlzdHJpYnVpw6fDo28gZW1ww61yaWNhIMOpIG1haW9yIHF1ZSBhIGRhIG5vcm1hbCAobGVwdG9jdXJ0b3NlKSwgcmVzdWx0YW5kbyBlbSB1bWEgbWFpb3IgZnJlcXXDqm5jaWEgZGUgdmFsb3JlcyBleHRyZW1vcyAob3V0bGllcnMpLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHF1ZSwgcGFyYSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbywgZm9pIGNhbGN1bGFkbyBvIHZldG9yIGRlIHJlc8OtZHVvcyAkZSA9IChJIC0gUClZJCBlIHBvc3Rlcmlvcm1lbnRlIG9idGlkb3Mgb3MgcmVzw61kdW9zIHBhZHJvbml6YWRvcyAkciQuIFBhcmEgYSBjb25zdHJ1w6fDo28gZG8gUS1RIHBsb3QsIG9yZGVuYW1vcyBvcyByZXPDrWR1b3MgdGFsIHF1ZSAkcl97KDEpfSBcXGxlIHJfeygyKX0gXFxsZSBcXGRvdHMgXFxsZSByX3sobil9JCBlIGNhbGN1bGFtb3Mgb3MgcXVhbnRpcyB0ZcOzcmljb3MgJHpfeyhpKX0gPSBcXFBoaV57LTF9XFxsZWZ0KFxcZnJhY3tpIC0gMC4zNzV9e24gKyAwLjI1fVxccmlnaHQpJC4gU29icmUgYSBtZWPDom5pY2EgZSBhIGludGVycHJldGHDp8OjbyBkZXN0YSBmZXJyYW1lbnRhIGRlIGRpYWduw7NzdGljbywgYXNzaW5hbGUgYSBhbHRlcm5hdGl2YSBjb3JyZXRhOiIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyB1c28gZGEgY29ycmXDp8OjbyAkMC4zNzUkIG5vIG51bWVyYWRvciB2aXNhIHRvcm5hciBvIGPDoWxjdWxvIGRvcyBxdWFudGlzIGRlcGVuZGVudGUgZGEgdmFyacOibmNpYSBhbW9zdHJhbCAkU14yJCwgZ2FyYW50aW5kbyBxdWUgYSByZXRhIHBhc3NlIHNlbXByZSBwZWxhIG9yaWdlbS4iLCAiQiI6ICJBIGxpbmVhcmlkYWRlIG5vIFEtUSBwbG90IGVudHJlICRyX3soaSl9JCBlICR6X3soaSl9JCDDqSB1bWEgZXZpZMOqbmNpYSB2aXN1YWwgZGUgcXVlIGEgc3Vwb3Npw6fDo28gZGUgbm9ybWFsaWRhZGUgZG9zIGVycm9zICRcXERlbHRhIFxcc2ltIE4oMCwgXFxzaWdtYV4yIEkpJCDDqSByYXpvw6F2ZWwgcGFyYSBhIHZhbGlkYWRlIGRhcyBpbmZlcsOqbmNpYXMgZXN0YXTDrXN0aWNhcy4iLCAiQyI6ICJTZSBvIGdyw6FmaWNvIGFwcmVzZW50YXIgdW0gZm9ybWF0byBkZSAnYmFuYW5hJyBvdSBhcmNvLCBpc3NvIGNvbmZpcm1hIHF1ZSBhIHJlbGHDp8OjbyBlbnRyZSAkWSQgZSAkWCQgw6kgcGVyZmVpdGFtZW50ZSBsaW5lYXIsIGVsaW1pbmFuZG8gYSBuZWNlc3NpZGFkZSBkZSB0ZXN0ZXMgZm9ybWFpcyBjb21vIG8gU2hhcGlyby1XaWxrLiIsICJEIjogIkEgZnVuw6fDo28gJFxcUGhpXnstMX0kIMOpIGEgZnVuw6fDo28gZGVuc2lkYWRlIGRlIHByb2JhYmlsaWRhZGUgZGEgbm9ybWFsLCBhcGxpY2FkYSBhb3MgcmVzw61kdW9zIHBhcmEgdHJhbnNmb3Jtw6EtbG9zIGVtIHVtYSBtw6l0cmljYSBkZSBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwuIiwgIkUiOiAiTyBRLVEgcGxvdCDDqSB1bSB0ZXN0ZSBmb3JtYWwgZGUgaGlww7N0ZXNlIHF1ZSBzdWJzdGl0dWkgYSBhbsOhbGlzZSBzdWJqZXRpdmEsIGZvcm5lY2VuZG8gdW0gJHBcXHRleHR7LXZhbG9yfSQgZXhhdG8gcGFyYSBhIG5vcm1hbGlkYWRlIGRlICRcXERlbHRhJCBiYXNlYW5kby1zZSBuYSBpbmNsaW5hw6fDo28gZGEgcmV0YS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk8gUS1RIHBsb3Qgw6kgdW1hIGZlcnJhbWVudGEgZGlhZ27Ds3N0aWNhLiBQZW5zZSBubyBxdWUgbyBhbGluaGFtZW50byBsaW5lYXIgcmVwcmVzZW50YSBubyBjb250ZXh0byBkYSBkaXN0cmlidWnDp8OjbyBkZSBwcm9iYWJpbGlkYWRlIHRlw7NyaWNhIGFzc3VtaWRhIG5vIG1vZGVsbyAkWSA9IFhcXGJldGEgKyBcXERlbHRhJC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgbGluZWFyaWRhZGUgbm8gUS1RIHBsb3Qgc3VnZXJlIHF1ZSBvcyBxdWFudGlzIGRhIGFtb3N0cmEgKHJlc8OtZHVvcyBwYWRyb25pemFkb3MpIGNyZXNjZW0gbmEgbWVzbWEgcHJvcG9yw6fDo28gcXVlIG9zIHF1YW50aXMgZGEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIHRlw7NyaWNhLiBJc3NvIHZhbGlkYSBhIHByZW1pc3NhIGRlIHF1ZSBvcyBlcnJvcyAkXFxEZWx0YSQgc2VndWVtIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwsIG8gcXVlIMOpIGZ1bmRhbWVudGFsIHBhcmEgYSB2YWxpZGFkZSBkb3MgdGVzdGVzIGRlIGhpcMOzdGVzZXMgZSBpbnRlcnZhbG9zIGRlIGNvbmZpYW7Dp2EgZG9zIGNvZWZpY2llbnRlcy4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH1dLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbeyJlbnVuY2lhZG8iOiAiU2VqYSBvIG1vZGVsbyBkZSByZWdyZXNzw6NvIGxpbmVhciAkWSA9IFhcXGJldGEgKyBcXERlbHRhJCBjb20gJG49NCQgZSAkcD0yJC4gQ29uc2lkZXJlIGEgbWF0cml6IGRlIGRlc2lnbiAkWCA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgXFxcXCAxICYgMSBcXFxcIDEgJiAwIFxcXFwgMSAmIDAgXFxlbmR7cG1hdHJpeH0kIGUgbyB2ZXRvciBkZSBvYnNlcnZhw6fDtWVzICRZID0gXFxiZWdpbntwbWF0cml4fSAyIFxcXFwgMyBcXFxcIDUgXFxcXCA0IFxcZW5ke3BtYXRyaXh9JC4gQ2FsY3VsZSBhIG1hdHJpeiBkZSBwcm9qZcOnw6NvICRQID0gWChYJ1gpXnstMX1YJyQgZSBkZXRlcm1pbmUgbyB2ZXRvciBkZSByZXPDrWR1b3MgJGUgPSAoSS1QKVkkLiBWZXJpZmlxdWUgc2UgJGUkIMOpIG9ydG9nb25hbCBhbyBlc3Bhw6dvIGNvbHVuYSBkZSAkWCQuIiwgImRpY2EiOiAiQ2FsY3VsZSAkWCdYJCwgZGVwb2lzIHN1YSBpbnZlcnNhLiBNdWx0aXBsaXF1ZSBwYXJhIG9idGVyICRQJCBlIGFwbGlxdWUgJGUgPSAoSS1QKVkkLiBBIG9ydG9nb25hbGlkYWRlIMOpIHZlcmlmaWNhZGEgdGVzdGFuZG8gc2UgJFgnZSA9IDAkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiBDYWxjdWxhciAkWCdYID0gXFxiZWdpbntwbWF0cml4fSAxICYgMSAmIDEgJiAxIFxcXFwgMSAmIDEgJiAwICYgMCBcXGVuZHtwbWF0cml4fSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxIFxcXFwgMSAmIDEgXFxcXCAxICYgMCBcXFxcIDEgJiAwIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSA0ICYgMiBcXFxcIDIgJiAyIFxcZW5ke3BtYXRyaXh9JC4iLCAiUGFzc28gMjogQ2FsY3VsYXIgYSBpbnZlcnNhICQoWCdYKV57LTF9ID0gXFxmcmFjezF9ezgtNH0gXFxiZWdpbntwbWF0cml4fSAyICYgLTIgXFxcXCAtMiAmIDQgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDAuNSAmIC0wLjUgXFxcXCAtMC41ICYgMSBcXGVuZHtwbWF0cml4fSQuIiwgIlBhc3NvIDM6IE9idGVyICRQID0gWChYJ1gpXnstMX1YJyQuIFByaW1laXJvICRYKFgnWCleey0xfSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgXFxcXCAxICYgMSBcXFxcIDEgJiAwIFxcXFwgMSAmIDAgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSAwLjUgJiAtMC41IFxcXFwgLTAuNSAmIDEgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDAgJiAwLjUgXFxcXCAwICYgMC41IFxcXFwgMC41ICYgLTAuNSBcXFxcIDAuNSAmIC0wLjUgXFxlbmR7cG1hdHJpeH0kLiIsICJQYXNzbyA0OiBGaW5hbGl6YXIgJFAgPSBcXGJlZ2lue3BtYXRyaXh9IDAgJiAwLjUgXFxcXCAwICYgMC41IFxcXFwgMC41ICYgLTAuNSBcXFxcIDAuNSAmIC0wLjUgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSAxICYgMSAmIDEgJiAxIFxcXFwgMSAmIDEgJiAwICYgMCBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMC41ICYgMC41ICYgMCAmIDAgXFxcXCAwLjUgJiAwLjUgJiAwICYgMCBcXFxcIDAgJiAwICYgMC41ICYgMC41IFxcXFwgMCAmIDAgJiAwLjUgJiAwLjUgXFxlbmR7cG1hdHJpeH0kLiIsICJQYXNzbyA1OiBDYWxjdWxhciAkXFxoYXR7WX0gPSBQWSA9IFxcYmVnaW57cG1hdHJpeH0gMi41IFxcXFwgMi41IFxcXFwgNC41IFxcXFwgNC41IFxcZW5ke3BtYXRyaXh9JCBlICRlID0gWSAtIFxcaGF0e1l9ID0gXFxiZWdpbntwbWF0cml4fSAtMC41IFxcXFwgMC41IFxcXFwgMC41IFxcXFwgLTAuNSBcXGVuZHtwbWF0cml4fSQuIiwgIlBhc3NvIDY6IFZlcmlmaWNhciBvcnRvZ29uYWxpZGFkZTogJFgnZSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgJiAxICYgMSBcXFxcIDEgJiAxICYgMCAmIDAgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSAtMC41IFxcXFwgMC41IFxcXFwgMC41IFxcXFwgLTAuNSBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMCBcXFxcIDAgXFxlbmR7cG1hdHJpeH0kLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEgJiBFc3RldmVzLCBNb2RlbG9zIExpbmVhcmVzLCBDYXAgMiwgcC4gNTgiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGVtb25zdHJlIGFsZ2VicmljYW1lbnRlIHF1ZSBvIG9wZXJhZG9yICRQID0gWChYJ1gpXnstMX1YJyQgw6kgaWRlbXBvdGVudGUsIG91IHNlamEsICRQXjIgPSBQJCwgZSBleHBsaXF1ZSBvIHF1ZSBpc3NvIHNpZ25pZmljYSBnZW9tZXRyaWNhbWVudGUgZW0gdGVybW9zIGRlIHByb2plw6fDtWVzIHN1Y2Vzc2l2YXMuIiwgImRpY2EiOiAiU3Vic3RpdHVhIGEgZXhwcmVzc8OjbyBkZSAkUCQgZW0gJFAgXFx0aW1lcyBQJCBlIG9ic2VydmUgY29tbyBvcyB0ZXJtb3MgY2VudHJhaXMgc2UgY2FuY2VsYW0uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IEVzY3JldmVyICRQXjIgPSBQIFxcY2RvdCBQID0gW1goWCdYKV57LTF9WCddIFxcY2RvdCBbWChYJ1gpXnstMX1YJ10kLiIsICJQYXNzbyAyOiBBZ3J1cGFyIG9zIHRlcm1vcyBkbyBtZWlvOiAkUF4yID0gWChYJ1gpXnstMX0gKFgnWCkgKFgnWCleey0xfSBYJyQuIiwgIlBhc3NvIDM6IENvbW8gJChYJ1gpKFgnWCleey0xfSA9IEkkLCBhIGV4cHJlc3PDo28gc2ltcGxpZmljYSBwYXJhICRQXjIgPSBYKFgnWCleey0xfSBJIFgnID0gWChYJ1gpXnstMX0gWCcgPSBQJC4iLCAiUGFzc28gNDogQ29uY2x1c8OjbyBnZW9tw6l0cmljYTogQSBpZGVtcG90w6puY2lhIHNpZ25pZmljYSBxdWUgdW1hIHNlZ3VuZGEgcHJvamXDp8OjbyBkbyBwb250byBqw6EgcHJvamV0YWRvIG7Do28gYWx0ZXJhIGEgc3VhIHBvc2nDp8OjbywgY29uZmlybWFuZG8gcXVlIGVzdGFtb3MgZml4YWRvcyBubyBlc3Bhw6dvIGNvbHVuYSAkQyhYKSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTHVuYSAmIEVzdGV2ZXMsIE1vZGVsb3MgTGluZWFyZXMsIENhcCA0LCBwLiAxMTAiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXhwZXJpbWVudG8gY29tICRuPTYkIG9ic2VydmHDp8O1ZXMgZSAkcD0zJCBwYXLDom1ldHJvcywgYSBzb21hIGRvcyBxdWFkcmFkb3MgdG90YWwgw6kgJFNRVG90ID0gMTAwJCBlIGEgc29tYSBkb3MgcXVhZHJhZG9zIGRvIGVycm8gw6kgJFNRUmVzID0gMjUkLiBEZXRlcm1pbmUgYSBzb21hIGRvcyBxdWFkcmFkb3MgZXhwbGljYWRhIHBlbG8gbW9kZWxvICgkU1FQYXIkKSBlIG9zIGdyYXVzIGRlIGxpYmVyZGFkZSBhc3NvY2lhZG9zIGFvIHJlc8OtZHVvICgkZ2xfe1Jlc30kKS4iLCAiZGljYSI6ICJVc2UgYSByZWxhw6fDo28gJFNRVG90ID0gU1FQYXIgKyBTUVJlcyQgZSBhIGRlZmluacOnw6NvIGRlIGdyYXVzIGRlIGxpYmVyZGFkZSBwYXJhIG8gcmVzw61kdW8gc2VuZG8gJG4tcCQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6ICRTUVBhciA9IFNRVG90IC0gU1FSZXMgPSAxMDAgLSAyNSA9IDc1JC4iLCAiUGFzc28gMjogJGdsX3tSZXN9ID0gbiAtIHAkLiIsICJQYXNzbyAzOiAkZ2xfe1Jlc30gPSA2IC0gMyA9IDMkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEgJiBFc3RldmVzLCBNb2RlbG9zIExpbmVhcmVzLCBDYXAgNCwgcC4gMTExIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogNzUuMH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBvIG1vZGVsbyBkZSByZWdyZXNzw6NvICRZID0gWFxcYmV0YSArIFxcRGVsdGEkLCBjb20gJFggXFxpbiBcXG1hdGhiYntSfV57biBcXHRpbWVzIHB9JCBkZSBwb3N0byBjb21wbGV0byBlICRcXERlbHRhIFxcc2ltIE4oMCwgXFxzaWdtYV4yIElfbikkLiBEZW1vbnN0cmUgYWxnZWJyaWNhbWVudGUgcXVlICRFW2VdID0gMCQsIG9uZGUgJGUgPSAoSSAtIFApWSQgZSAkUCA9IFgoWCdYKV57LTF9WCckLiIsICJkaWNhIjogIlVzZSBhIHByb3ByaWVkYWRlIGRhIGVzcGVyYW7Dp2EgbGluZWFyICRFW0FZXSA9IEFFW1ldJCBlIGxlbWJyZS1zZSBxdWUgJEVbWV0gPSBYXFxiZXRhJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRGVmaW5pw6fDo28gZG8gcmVzw61kdW86ICRlID0gKEkgLSBQKVkkLiIsICJBcGxpY2FuZG8gYSBlc3BlcmFuw6dhOiAkRVtlXSA9IEVbKEkgLSBQKVldID0gKEkgLSBQKUVbWV0kLiIsICJTdWJzdGl0dWluZG8gJEVbWV0gPSBYXFxiZXRhJDogJEVbZV0gPSAoSSAtIFApWFxcYmV0YSA9IFhcXGJldGEgLSBQWFxcYmV0YSQuIiwgIlN1YnN0aXR1aW5kbyAkUCA9IFgoWCdYKV57LTF9WCckOiAkUFhcXGJldGEgPSBYKFgnWCleey0xfVgnWFxcYmV0YSQuIiwgIlNpbXBsaWZpY2FuZG86ICRYKFgnWCleey0xfShYJ1gpXFxiZXRhID0gWChJX3ApXFxiZXRhID0gWFxcYmV0YSQuIiwgIkZpbmFsaXphbmRvOiAkRVtlXSA9IFhcXGJldGEgLSBYXFxiZXRhID0gMCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjB9LCB7ImVudW5jaWFkbyI6ICJEYWRhIGEgbWF0cml6IGRlIHByb2plw6fDo28gJFAgPSBYKFgnWCleey0xfVgnJCBlbSB1bSBtb2RlbG8gY29tICRuPTEwJCBvYnNlcnZhw6fDtWVzIGUgJHA9MyQgcGFyw6JtZXRyb3MgKGluY2x1aW5kbyBvIGludGVyY2VwdG8pLCBkZXRlcm1pbmUgbyB2YWxvciBkYSBzb21hIGRvcyBlbGVtZW50b3MgZGEgZGlhZ29uYWwgcHJpbmNpcGFsIGRlICQoSSAtIFApJCwgb3Ugc2VqYSwgbyB0cmHDp28gJFRyKEkgLSBQKSQuIiwgImRpY2EiOiAiTyB0cmHDp28gZGUgdW1hIG1hdHJpeiDDqSBhIHNvbWEgZGUgc2V1cyBhdXRvdmFsb3Jlcy4gTGVtYnJlLXNlIHF1ZSAkVHIoUCkgPSByKFApID0gcCQgZSBxdWUgJFRyKEEgLSBCKSA9IFRyKEEpIC0gVHIoQikkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJTYWJlbW9zIHF1ZSAkVHIoSSAtIFApID0gVHIoSV9uKSAtIFRyKFApJC4iLCAiTyB0cmHDp28gZGEgaWRlbnRpZGFkZSAkVHIoSV9uKSA9IG4gPSAxMCQuIiwgIk8gdHJhw6dvIGRhIG1hdHJpeiBkZSBwcm9qZcOnw6NvICRUcihQKSA9IHIoUCkgPSBwID0gMyQuIiwgIlBvcnRhbnRvLCAkVHIoSSAtIFApID0gMTAgLSAzID0gNyQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTHVuYSAmIEVzdGV2ZXMsIE1vZGVsb3MgTGluZWFyZXMsIENhcCA0LCBwLiAxMTAiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiA3LjB9LCB7ImVudW5jaWFkbyI6ICJQcm92ZSBxdWUgYSBtYXRyaXogJChJIC0gUCkkIMOpIGlkZW1wb3RlbnRlLiBFbSBzZWd1aWRhLCBpbnRlcnByZXRlIG8gcXVlIGVzc2EgcHJvcHJpZWRhZGUgaW1wbGljYSBzb2JyZSBhIHByb2plw6fDo28gb3J0b2dvbmFsIGRvcyByZXPDrWR1b3Mgbm8gZXNwYcOnbyBkb3MgcmVzw61kdW9zLiIsICJkaWNhIjogIlVtYSBtYXRyaXogJEEkIMOpIGlkZW1wb3RlbnRlIHNlICRBXjIgPSBBJC4gQ2FsY3VsZSAkKEkgLSBQKShJIC0gUCkkIHNhYmVuZG8gcXVlICRQXjIgPSBQJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRXhwYW5zw6NvOiAkKEkgLSBQKShJIC0gUCkgPSBJKEkpIC0gSShQKSAtIFAoSSkgKyBQKFApJC4iLCAiU2ltcGxpZmljYcOnw6NvOiAkSSAtIFAgLSBQICsgUF4yJC4iLCAiQ29tbyAkUCQgw6kgdW1hIG1hdHJpeiBkZSBwcm9qZcOnw6NvIG9ydG9nb25hbCwgJFBeMiA9IFAkLiIsICJTdWJzdGl0dWluZG86ICRJIC0gMlAgKyBQID0gSSAtIFAkLiIsICJDb25jbHVzw6NvOiBBIG1hdHJpeiAkKEkgLSBQKSQgw6kgaWRlbXBvdGVudGUuIiwgIkludGVycHJldGHDp8OjbzogQSBpZGVtcG90w6puY2lhIGdhcmFudGUgcXVlIGFwbGljYXIgYSBwcm9qZcOnw6NvIG5vIHN1YmVzcGHDp28gZG9zIHJlc8OtZHVvcyBzdWNlc3NpdmFzIHZlemVzIG7Do28gYWx0ZXJhIG8gcmVzdWx0YWRvLCBjb25maXJtYW5kbyBxdWUgb3MgcmVzw61kdW9zIGrDoSBlc3TDo28gcGVyZmVpdGFtZW50ZSBjb250aWRvcyBubyBlc3Bhw6dvIG9ydG9nb25hbCBhICRDKFgpJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBleHBlcmltZW50byBpbmR1c3RyaWFsLCBvYnNlcnZvdS1zZSB1bSBwb250byBjb20gZXJybyBicnV0byAkZV9pID0gNC41JC4gU2FiZW5kbyBxdWUgbyBlc3RpbWFkb3IgZGEgdmFyacOibmNpYSBkbyBlcnJvIMOpICRcXGhhdHtcXHNpZ21hfV4yID0gNC4wJCBlIGEgYWxhdmFuY2FnZW0gZG8gcG9udG8gw6kgJGhfaSA9IDAuNzUkLCBjYWxjdWxlIG8gdmFsb3IgZG8gcmVzw61kdW8gcGFkcm9uaXphZG8gJHJfaSQuIERpc2N1dGEgc2UgZXNzZSB2YWxvciBpbmRpY2EgdW0gZGVzdmlvIGltcG9ydGFudGUgZG8gbW9kZWxvIHByb3Bvc3RvLiIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSAkcl9pID0gXFxmcmFje2VfaX17XFxoYXR7XFxzaWdtYX0gXFxzcXJ0ezEgLSBoX2l9fSQuIENvbnNpZGVyZSBxdWUgcmVzw61kdW9zIHBhZHJvbml6YWRvcyBzdXBlcmlvcmVzIGEgMiBvdSAzIGVtIG1hZ25pdHVkZSBzw6NvIGZyZXF1ZW50ZW1lbnRlIGNvbnNpZGVyYWRvcyBpbmTDrWNpb3MgZGUgcHJvYmxlbWFzIG5vIG1vZGVsby4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYXIgb3MgZGFkb3MgZm9ybmVjaWRvczogJGVfaSA9IDQuNSQsICRcXGhhdHtcXHNpZ21hfSA9IFxcc3FydHs0LjB9ID0gMi4wJCwgJGhfaSA9IDAuNzUkLiIsICIyLiBDYWxjdWxhciBvIHRlcm1vIGRlIGFqdXN0ZSBkZSB2YXJpw6JuY2lhOiAkXFxzcXJ0ezEgLSBoX2l9ID0gXFxzcXJ0ezEgLSAwLjc1fSA9IFxcc3FydHswLjI1fSA9IDAuNSQuIiwgIjMuIENhbGN1bGFyIG8gcmVzw61kdW8gcGFkcm9uaXphZG86ICRyX2kgPSBcXGZyYWN7NC41fXsyLjAgXFx0aW1lcyAwLjV9JC4iLCAiNC4gUmVzdWx0YWRvOiAkcl9pID0gXFxmcmFjezQuNX17MS4wfSA9IDQuNSQuIiwgIjUuIERpc2N1c3PDo286IENvbW8gJHxyX2l8ID0gNC41ID4gMyQsIG8gcG9udG8gYXByZXNlbnRhIHVtIGRlc3ZpbyBhbHRhbWVudGUgc2lnbmlmaWNhdGl2byBlbSByZWxhw6fDo28gw6AgcHJlZGnDp8OjbyBkbyBtb2RlbG8sIHN1Z2VyaW5kbyBxdWUgYSBvYnNlcnZhw6fDo28gcG9kZSBzZXIgdW0gb3V0bGllciBjcsOtdGljby4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDQuNX0sIHsiZW51bmNpYWRvIjogIlNlamEgdW0gbW9kZWxvIGNvbSAkbj0yNSQgb2JzZXJ2YcOnw7VlcyBlICRwPTMkIHBhcsOibWV0cm9zLiBVbSBwb250byBlc3BlY8OtZmljbyBwb3NzdWkgdW0gcmVzw61kdW8gcGFkcm9uaXphZG8gJHJfaSA9IDIkLiBDYWxjdWxlIG8gcmVzw61kdW8gc3R1ZGVudGl6YWRvICR0X2kkIGNvcnJlc3BvbmRlbnRlIGUgY29tcGFyZSBjb20gbyB2YWxvciBkZSAkcl9pJC4gUG9yIHF1ZSAkdF9pJCDDqSBwcmVmZXLDrXZlbCBwYXJhIGEgZGV0ZWPDp8OjbyBkZSBvdXRsaWVycz8iLCAiZGljYSI6ICJVc2UgYSBmw7NybXVsYSAkdF9pID0gcl9pIFxcc3FydHtcXGZyYWN7biAtIHAgLSAxfXtuIC0gcCAtIHJfaV4yfX0kLiBOb3RlIHF1ZSBlc3RhIGbDs3JtdWxhIMOpIHVtYSBhcGxpY2HDp8OjbyBkbyBtw6l0b2RvIGRlIHZhbGlkYcOnw6NvIGNydXphZGEgJ2xlYXZlLW9uZS1vdXQnIHBhcmEgYSB2YXJpw6JuY2lhLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBQYXLDom1ldHJvczogJG49MjUsIHA9Mywgcl9pPTIkLiIsICIyLiBDYWxjdWxhciAkbiAtIHAgLSAxID0gMjUgLSAzIC0gMSA9IDIxJC4iLCAiMy4gQ2FsY3VsYXIgJG4gLSBwIC0gcl9pXjIgPSAyNSAtIDMgLSAyXjIgPSAyMiAtIDQgPSAxOCQuIiwgIjQuIENhbGN1bGFyICR0X2kgPSAyIFxcdGltZXMgXFxzcXJ0e1xcZnJhY3syMX17MTh9fSA9IDIgXFx0aW1lcyBcXHNxcnR7MS4xNjY3fSBcXGFwcHJveCAyIFxcdGltZXMgMS4wODAxID0gMi4xNjAyJC4iLCAiNS4gQ29uY2x1c8OjbzogJHRfaSBcXGFwcHJveCAyLjE2JCwgcXVlIMOpIG1haW9yIHF1ZSAkcl9pID0gMiQuIE8gdXNvIGRlICR0X2kkIMOpIHByZWZlcsOtdmVsIHBvcnF1ZSBlbGUgcmVtb3ZlIGEgaW5mbHXDqm5jaWEgZGEgb2JzZXJ2YcOnw6NvICRpJCBuYSBlc3RpbWHDp8OjbyBkYSB2YXJpw6JuY2lhICRcXGhhdHtcXHNpZ21hfSQsIGV2aXRhbmRvIHF1ZSBvdXRsaWVycyBtYXNjYXJlbSBhIHNpIG1lc21vcyBhbyBpbmZsYXIgJFxcaGF0e1xcc2lnbWF9JC4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uQmFyKHg9WydSZXPDrWR1byBQYWRyb25pemFkbyAocl9pKScsICdSZXPDrWR1byBTdHVkZW50aXphZG8gKHRfaSknXSwgeT1bMiwgMi4xNl0sIG1hcmtlcl9jb2xvcj1bJyMwMDAwRkYnLCAnI0ZGMDAwMCddKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdDb21wYXJhw6fDo28gZGUgTcOpdHJpY2FzIGRlIFJlc8OtZHVvcycsIHhheGlzX3RpdGxlPSdNw6l0cmljYScsIHlheGlzX3RpdGxlPSdWYWxvciBNYWduaXR1ZGUnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDIuMTZ9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgcGVyc3BlY3RpdmEgZGEgbWF0cml6IGhhdCAkUCA9IFgoWCdYKV57LTF9WCckLCBwb3IgcXVlIGEgdmFyacOibmNpYSBkbyByZXPDrWR1byAkZV9pJCBuw6NvIMOpIGNvbnN0YW50ZSwgbWVzbW8gcXVlIG9zIGVycm9zICRcXERlbHRhJCBzZWphbSBob21vY2Vkw6FzdGljb3MgKCRWYXIoXFxEZWx0YSkgPSBcXHNpZ21hXjIgSV9uJCkuIENvbW8gYSBhbGF2YW5jYWdlbSAkaF9pJCBhdHVhIG5lc3NlIGNvbnRleHRvPyIsICJkaWNhIjogIkNvbnNpZGVyZSBhIHJlbGHDp8OjbyAkZSA9IChJIC0gUClZJCBlIGFwbGlxdWUgYXMgcHJvcHJpZWRhZGVzIGRlIHZhcmnDom5jaWEgZGUgdHJhbnNmb3JtYcOnw7VlcyBsaW5lYXJlcyBkZSB2ZXRvcmVzIGFsZWF0w7NyaW9zLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBEYWRhIGEgZGVmaW5pw6fDo28gZGUgcmVzw61kdW9zOiAkZSA9IChJIC0gUClZID0gKEkgLSBQKShYXFxiZXRhICsgXFxEZWx0YSkgPSAoSSAtIFApXFxEZWx0YSQgKHBvaXMgJChJLVApWCA9IDAkKS4iLCAiMi4gQSBtYXRyaXogZGUgY292YXJpw6JuY2lhIGRvcyByZXPDrWR1b3Mgw6kgJENvdihlKSA9IENvdigoSSAtIFApXFxEZWx0YSkgPSAoSSAtIFApIENvdihcXERlbHRhKSAoSSAtIFApJyQuIiwgIjMuIENvbW8gJENvdihcXERlbHRhKSA9IFxcc2lnbWFeMiBJX24kLCB0ZW1vcyAkQ292KGUpID0gXFxzaWdtYV4yIChJIC0gUCkoSSAtIFApID0gXFxzaWdtYV4yIChJIC0gUCkkIChwb2lzICRQJCDDqSBpZGVtcG90ZW50ZSBlIHNpbcOpdHJpY2EpLiIsICI0LiBBIHZhcmnDom5jaWEgZG8gJGkkLcOpc2ltbyByZXPDrWR1byAkZV9pJCDDqSBvICRpJC3DqXNpbW8gZWxlbWVudG8gZGEgZGlhZ29uYWwgZGEgbWF0cml6LCBvdSBzZWphLCAkVmFyKGVfaSkgPSBcXHNpZ21hXjIgKDEgLSBoX2kpJCwgb25kZSAkaF9pJCDDqSBvICRpJC3DqXNpbW8gZWxlbWVudG8gZGlhZ29uYWwgZGUgJFAkLiIsICI1LiBJbnRlcnByZXRhw6fDo286IENvbW8gJGhfaSQgdmFyaWEgcGFyYSBjYWRhIHBvbnRvIGRlcGVuZGVuZG8gZGEgc3VhIGRpc3TDom5jaWEgYW8gY2VudHJvIGRvcyBkYWRvcyBubyBlc3Bhw6dvICRYJCwgYSB2YXJpw6JuY2lhIGRvIHJlc8OtZHVvIGRlcGVuZGUgZGEgcG9zacOnw6NvIGRhIG9ic2VydmHDp8OjbyBubyBlc3Bhw6dvIGRlIGRlc2lnbi4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyBtb2RlbG8gJFkgPSBYXFxiZXRhICsgXFx0ZXh0e1x0ZXh0RGVsdGF9JC4gRXhwbGlxdWUgZGV0YWxoYWRhbWVudGUgY29tbyBvIHVzbyBkYSBtYXRyaXogZGUgcHJvamXDp8OjbyAkUCA9IFgoWCdYKV57LTF9WCckIGF1eGlsaWEgbmEgZGVmaW5pw6fDo28gZG8gdmV0b3IgZGUgcmVzw61kdW9zICRlID0gKEkgLSBQKVkkIGUgcG9yIHF1ZSBhIGluc3Blw6fDo28gdmlzdWFsIGRlICRlX2kkIHZlcnN1cyAkXFxoYXR7WX1faSQgw6kgY29uc2lkZXJhZGEgbyBwYWRyw6NvLW91cm8gZGUgZGlhZ27Ds3N0aWNvLCBlbSB2ZXogZGUgYXBlbmFzIGNvbmZpYXIgZW0gdGVzdGVzIGRlIGhpcMOzdGVzZXMgZm9ybWFpcyBwYXJhIGhvbW9zY2VkYXN0aWNpZGFkZT8iLCAiZGljYSI6ICJGb3F1ZSBubyBwYXBlbCBkbyBvcGVyYWRvciBkZSBwcm9qZcOnw6NvICQoSS1QKSQgcXVlICdmaWx0cmEnIGEgZXN0cnV0dXJhIHNpc3RlbcOhdGljYSBkb3MgZGFkb3MsIGRlaXhhbmRvIGFwZW5hcyBvIHJ1w61kbyByZXNpZHVhbC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSBtYXRyaXogJFAkIChoYXQtbWF0cml4KSBwcm9qZXRhIG8gdmV0b3Igb2JzZXJ2YWRvICRZJCBubyBzdWJlc3Bhw6dvIGRlZmluaWRvIHBlbGFzIGNvbHVuYXMgZGUgJFgkLCByZXN1bHRhbmRvIG5vcyB2YWxvcmVzIGFqdXN0YWRvczogJFxcaGF0e1l9ID0gUFkkLiIsICJPIHZldG9yIGRlIHJlc8OtZHVvcyDDqSBkZWZpbmlkbyBwZWxhIHByb2plw6fDo28gY29tcGxlbWVudGFyOiAkZSA9IFkgLSBcXGhhdHtZfSA9IChJIC0gUClZJC4iLCAiQ29tbyAkWSA9IFhcXGJldGEgKyBcXHRleHR7XHRleHREZWx0YX0kLCB0ZW1vcyAkZSA9IChJIC0gUCkoWFxcYmV0YSArIFxcdGV4dHtcdGV4dERlbHRhfSkgPSAoSSAtIFApWFxcYmV0YSArIChJIC0gUClcXHRleHR7XHRleHREZWx0YX0gPSAwICsgKEkgLSBQKVxcdGV4dHtcdGV4dERlbHRhfSA9IChJIC0gUClcXHRleHR7XHRleHREZWx0YX0kLiIsICJBIGluc3Blw6fDo28gdmlzdWFsIHBlcm1pdGUgZGV0ZWN0YXIgcGFkcsO1ZXMgZXN0cnV0dXJhaXMgKGN1cnZhdHVyYXMgb3UgdmFyaWHDp8O1ZXMgZGUgZXNjYWxhKSBxdWUgdGVzdGVzIGVzdGF0w61zdGljb3MgZm9ybWFpcywgbXVpdGFzIHZlemVzIGxpbWl0YWRvcyBhIGFsdGVybmF0aXZhcyBlc3BlY8OtZmljYXMgKGV4OiBhcGVuYXMgZGVzdmlvcyBsaW5lYXJlcyBkYSB2YXJpw6JuY2lhKSwgcG9kZW0gaWdub3Jhci4iLCAiTyBzaXN0ZW1hIHZpc3VhbCBodW1hbm8gw6kgYWx0YW1lbnRlIHNlbnPDrXZlbCBhIHF1ZWJyYXMgZGUgc2ltZXRyaWEgZSBwYWRyw7VlcyBuw6NvIGFsZWF0w7NyaW9zLCB0b3JuYW5kbyBvcyBncsOhZmljb3MgZGUgZGlzcGVyc8OjbyBmZXJyYW1lbnRhcyBtYWlzIHZlcnPDoXRlaXMgcGFyYSBkaWFnbsOzc3RpY28gZGUgZmFsaGFzIGRlIGVzcGVjaWZpY2HDp8Ojby4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgb25kZSAkbj0xMDAkLCB2b2PDqiBhanVzdG91IG9zIGRhZG9zIGUgb2J0ZXZlIHVtYSB2YXJpw6JuY2lhIGVzdGltYWRhIGRvcyByZXPDrWR1b3MgZGUgJFxcaGF0e1xcc2lnbWF9XjIgPSA0LjAkLiBTYWJlbmRvIHF1ZSBvICRpJC3DqXNpbW8gZWxlbWVudG8gZGlhZ29uYWwgZGEgbWF0cml6IGRlIHByb2plw6fDo28gJFAkIMOpICRoX2kgPSAwLjA1JCwgY2FsY3VsZSBhIHZhcmnDom5jaWEgdGXDs3JpY2EgZXN0aW1hZGEgZG8gJGkkLcOpc2ltbyByZXPDrWR1bywgZGFkYSBwb3IgJFxcdGV4dHtWYXJ9KGVfaSkgPSBcXHNpZ21hXjIoMSAtIGhfaSkkLiIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSAkXFx0ZXh0e1Zhcn0oZV9pKSA9IFxcc2lnbWFeMigxIC0gaF9pKSQgZm9ybmVjaWRhIG5vIGNvbnRleHRvLiBMZW1icmUtc2UgcXVlIGVtIGdyYW5kZXMgYW1vc3RyYXMsICRoX2kkIMOpIHRpcGljYW1lbnRlIHBlcXVlbm8sIG1hcyBhcXVpIHVzYXJlbW9zIG8gdmFsb3IgZXhhdG8uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgZsOzcm11bGEgZGEgdmFyacOibmNpYSBkbyByZXPDrWR1byDDqSAkXFx0ZXh0e1Zhcn0oZV9pKSA9IFxcc2lnbWFeMigxIC0gaF9pKSQuIiwgIlN1YnN0aXR1aW5kbyBvcyB2YWxvcmVzIGNvbmhlY2lkb3M6ICRcXHNpZ21hXjIgPSA0LjAkIGUgJGhfaSA9IDAuMDUkLiIsICIkXFx0ZXh0e1Zhcn0oZV9pKSA9IDQuMCBcXHRpbWVzICgxIC0gMC4wNSkkLiIsICIkXFx0ZXh0e1Zhcn0oZV9pKSA9IDQuMCBcXHRpbWVzIDAuOTUgPSAzLjgkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMy44fSwgeyJlbnVuY2lhZG8iOiAiU2UsIGFvIGFuYWxpc2FyIHVtIGdyw6FmaWNvIGRlIHJlc8OtZHVvcyBkZSB1bSBtb2RlbG8gZGUgcmVncmVzc8Ojbywgdm9jw6ogcGVyY2ViZXIgcXVlIGEgZGlzcGVyc8OjbyBkb3MgcmVzw61kdW9zIChsYXJndXJhIGRhIG51dmVtIGRlIHBvbnRvcykgw6kgbXVpdG8gbWFpb3IgZW0gdW0gZXh0cmVtbyBkbyBlaXhvICRcXGhhdHtZfSQgZG8gcXVlIG5vIG91dHJvLCBkZXNjcmV2YSBxdWFpcyBzZXJpYW0gYXMgY29uc2VxdcOqbmNpYXMgdGXDs3JpY2FzIHBhcmEgbyBlc3RpbWFkb3IgJFxcaGF0e1xcYmV0YX0kIGUgcG9yIHF1ZSBlc3NlIGRpYWduw7NzdGljbyB2aXN1YWwgc3VnZXJlIHVtYSBxdWVicmEgbmEgc3Vwb3Npw6fDo28gZGUgaG9tb3NjZWRhc3RpY2lkYWRlLiIsICJkaWNhIjogIlJlZmxpdGEgc29icmUgY29tbyBvIGVzdGltYWRvciBkZSBNw61uaW1vcyBRdWFkcmFkb3MgT3JkaW7DoXJpb3MgKE1RTykgYXRyaWJ1aSBwZXNvIHVuaWZvcm1lIGEgdG9kYXMgYXMgb2JzZXJ2YcOnw7VlcywgaW5kZXBlbmRlbnRlbWVudGUgZGEgdmFyacOibmNpYSBsb2NhbC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSBoZXRlcm9jZWRhc3RpY2lkYWRlIGltcGxpY2EgcXVlICRWW1xcdGV4dHtcdGV4dERlbHRhfV0gPSBcXHNpZ21hXjIgXFxPbWVnYSQsIG9uZGUgJFxcT21lZ2EgXFxuZXEgSSQuIiwgIk8gZXN0aW1hZG9yIGRlIE1RTyBjb250aW51YSBuw6NvIHZpY2lhZG8sIG1hcyBkZWl4YSBkZSBzZXIgbyBFc3RpbWFkb3IgTGluZWFyIE7Do28gVmljaWFkbyBkZSBWYXJpw6JuY2lhIE3DrW5pbWEgKEJMVUUpIGNvbmZvcm1lIG8gVGVvcmVtYSBkZSBHYXVzcy1NYXJrb3YuIiwgIkEgdmFyacOibmNpYSBkZSAkXFxoYXR7XFxiZXRhfSQgY2FsY3VsYWRhIHBvciAkVltcXGhhdHtcXGJldGF9XSA9IFxcc2lnbWFeMihYJ1gpXnstMX0kIHRvcm5hLXNlIGluY29ycmV0YSwgbGV2YW5kbyBhIGVycm9zIHBhZHLDo28gdmllc2Fkb3MgZSB0ZXN0ZXMgZGUgaGlww7N0ZXNlcyAoJHRfe1xcdGV4dHtjYWxjfX0kIGUgJHBcXHRleHR7LXZhbG9yfSQpIG7Do28gY29uZmnDoXZlaXMuIiwgIk8gZ3LDoWZpY28gdmlzdWFsIG1vc3RyYSBhIHF1ZWJyYSBkYSBjb25kacOnw6NvICRWW2VfaXxcXGhhdHtZfV9pXSBcXGFwcHJveCBcXHNpZ21hXjIkLCBjb25maXJtYW5kbyBxdWUgYSBwcmVjaXPDo28gZG8gbW9kZWxvIHZhcmlhIHNpc3RlbWF0aWNhbWVudGUgYXRyYXbDqXMgZG8gZG9tw61uaW8gZGUgJFxcaGF0e1l9JCwgbyBxdWUgcmVxdWVyIGFib3JkYWdlbnMgY29tbyBNw61uaW1vcyBRdWFkcmFkb3MgUG9uZGVyYWRvcyAoV0xTKS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJGYXJhd2F5LCBMaW5lYXIgTW9kZWxzIHdpdGggUiwgQ2FwIDcsIHAuIDgzIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBjb20gJG49NCQgb2JzZXJ2YcOnw7VlcywgY3Vqb3MgcmVzw61kdW9zIHBhZHJvbml6YWRvcyBvcmRlbmFkb3Mgc8OjbzogJHJfeygxKX0gPSAtMS4yJCwgJHJfeygyKX0gPSAtMC4zJCwgJHJfeygzKX0gPSAwLjQkIGUgJHJfeyg0KX0gPSAxLjEkLiBVdGlsaXphbmRvIGEgZsOzcm11bGEgdGXDs3JpY2EgJHpfeyhpKX0gPSBcXFBoaV57LTF9XFxsZWZ0KFxcZnJhY3tpIC0gMC4zNzV9e24gKyAwLjI1fVxccmlnaHQpJCwgY2FsY3VsZSBvcyB2YWxvcmVzIGRvcyBkb2lzIHByaW1laXJvcyBxdWFudGlzIHRlw7NyaWNvcyAoJHpfeygxKX0kIGUgJHpfeygyKX0kKSBlIGV4cGxpcXVlIG8gcXVlIHJlcHJlc2VudGFyaWEgdW0gZGlzdGFuY2lhbWVudG8gYWNlbnR1YWRvIGRlICRyX3soMSl9JCBlbSByZWxhw6fDo28gYSAkel97KDEpfSQgbmVzdGUgcGVxdWVubyBjb25qdW50byBkZSBkYWRvcy4iLCAiZGljYSI6ICJVc2UgJG49NCQgbmEgZsOzcm11bGEuIExlbWJyZS1zZSBxdWUgJFxcUGhpXnstMX0kIMOpIGEgaW52ZXJzYSBkYSBub3JtYWwgcGFkcsOjby4gVmFsb3JlcyBhcHJveGltYWRvcyBkZSAkXFxQaGleey0xfSgwLjEyNSkgXFxhcHByb3ggLTEuMTUkIGUgJFxcUGhpXnstMX0oMC4zNTMpIFxcYXBwcm94IC0wLjM4JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYXIgbyB0YW1hbmhvIGFtb3N0cmFsOiAkbj00JC4iLCAiMi4gQ2FsY3VsYXIgbyBkZW5vbWluYWRvciBjb25zdGFudGU6ICRuICsgMC4yNSA9IDQuMjUkLiIsICIzLiBDYWxjdWxhciAkel97KDEpfSQ6ICR6X3soMSl9ID0gXFxQaGleey0xfVxcbGVmdChcXGZyYWN7MSAtIDAuMzc1fXs0LjI1fVxccmlnaHQpID0gXFxQaGleey0xfVxcbGVmdChcXGZyYWN7MC42MjV9ezQuMjV9XFxyaWdodCkgPSBcXFBoaV57LTF9KDAuMTQ3KSQuIiwgIjQuIENhbGN1bGFyICR6X3soMil9JDogJHpfeygyKX0gPSBcXFBoaV57LTF9XFxsZWZ0KFxcZnJhY3syIC0gMC4zNzV9ezQuMjV9XFxyaWdodCkgPSBcXFBoaV57LTF9XFxsZWZ0KFxcZnJhY3sxLjYyNX17NC4yNX1cXHJpZ2h0KSA9IFxcUGhpXnstMX0oMC4zODIpJC4iLCAiNS4gSW50ZXJwcmV0YcOnw6NvOiBPIGRpc3RhbmNpYW1lbnRvIGRlICRyX3soaSl9JCBlbSByZWxhw6fDo28gYSAkel97KGkpfSQgcGFyYSB2YWxvcmVzIHBlcXVlbm9zIGRlICRuJCBpbmRpY2EgcXVlIGEgZGlzdHJpYnVpw6fDo28gZG9zIGVycm9zICRcXERlbHRhJCBkZXN2aWEgZGEgbm9ybWFsaWRhZGUsIHBvZGVuZG8gY29tcHJvbWV0ZXIgYSBjb25maWFiaWxpZGFkZSBkYXMgZXN0YXTDrXN0aWNhcyBkZSB0ZXN0ZSAoJHRfe1xcdGV4dHtjYWxjfX0kKS4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVstMS4xNSwgLTAuMzgsIDAuMzgsIDEuMTVdLCB5PVstMS4yLCAtMC4zLCAwLjQsIDEuMV0sIG1vZGU9J21hcmtlcnMrbGluZXMnLCBuYW1lPSdRLVEgUGxvdCcsIGxpbmU9ZGljdChjb2xvcj0nIzAwMDBGRicpLCBtYXJrZXI9ZGljdChzaXplPTgpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdRLVEgUGxvdCBkZSBBcG9pbycsIHhheGlzX3RpdGxlPSdRdWFudGlzIFRlw7NyaWNvcyAoJHpfeyhpKX0kKScsIHlheGlzX3RpdGxlPSdSZXPDrWR1b3MgUGFkcm9uaXphZG9zICgkcl97KGkpfSQpJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAtMS4wNX0sIHsiZW51bmNpYWRvIjogIkFuYWxpc2UgYSBpbXBvcnTDom5jaWEgdGXDs3JpY2EgZGEgcHJlbWlzc2EgZGUgbm9ybWFsaWRhZGUgZG8gdmV0b3IgZGUgZXJyb3MgJFxcRGVsdGEkIGVtIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvICRZID0gWFxcYmV0YSArIFxcRGVsdGEkLiBQb3IgcXVlIG8gZGVzY3VtcHJpbWVudG8gZGVzdGEgcHJlbWlzc2EsIHZlcmlmaWNhZG8gYXRyYXbDqXMgZGUgdW0gUS1RIHBsb3QsIHRvcm5hIGFzIG1lZGlkYXMgZGUgaW5jZXJ0ZXphIChjb21vIGludGVydmFsb3MgZGUgY29uZmlhbsOnYSBwYXJhIG9zIGNvZWZpY2llbnRlcyAkXFxiZXRhJCkgcG91Y28gY29uZmnDoXZlaXMsIG1lc21vIHF1ZSBvcyBlc3RpbWFkb3JlcyBzZWphbSBuw6NvLXZpY2lhZG9zPyIsICJkaWNhIjogIkZvcXVlIG5hIHJlbGHDp8OjbyBlbnRyZSBhIGRpc3RyaWJ1acOnw6NvIGRvcyBlcnJvcyBlIGEgZGlzdHJpYnVpw6fDo28gZGFzIGVzdGF0w61zdGljYXMgZGUgdGVzdGUgKGNvbW8gbyAkdF97XFx0ZXh0e2NhbGN9fSQpLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBBIGVzdGltYcOnw6NvIGRlIE3DrW5pbW9zIFF1YWRyYWRvcyBPcmRpbsOhcmlvcyBwcm9kdXogZXN0aW1hZG9yZXMgJFxcaGF0e1xcYmV0YX0kIG7Do28tdmljaWFkb3MgbWVzbW8gc2VtIGEgcHJlbWlzc2EgZGUgbm9ybWFsaWRhZGUgZG9zIGVycm9zLiIsICIyLiBObyBlbnRhbnRvLCBwYXJhIHJlYWxpemFyIHRlc3RlcyBkZSBoaXDDs3Rlc2VzIGUgY29uc3RydWlyIGludGVydmFsb3MgZGUgY29uZmlhbsOnYSwgcHJlY2lzYW1vcyBxdWUgYSBlc3RhdMOtc3RpY2EgZGUgdGVzdGUgKGV4OiAkdF97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3tcXGhhdHtcXGJldGF9IC0gXFxiZXRhfXtFUChcXGhhdHtcXGJldGF9KX0kKSBzaWdhIHVtYSBkaXN0cmlidWnDp8OjbyAkdChnbCkkIGVzcGVjw61maWNhLiIsICIzLiBFc3NhIGVzdGF0w61zdGljYSAkdCQgc8OzIHBvc3N1aSBkaXN0cmlidWnDp8OjbyBTdHVkZW50IHNlIG9zIGVycm9zICRcXERlbHRhJCBmb3JlbSBub3JtYWxtZW50ZSBkaXN0cmlidcOtZG9zLiIsICI0LiBTZSBvIFEtUSBwbG90IG1vc3RyYXIgZGVzdmlvcyBzZXZlcm9zLCBhIGRpc3RyaWJ1acOnw6NvIHJlYWwgZGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlIHNlcsOhIGRpZmVyZW50ZSBkYSB0YWJlbGEgJHQkLCBpbnZhbGlkYW5kbyBvcyB2YWxvcmVzIGNyw610aWNvcyAkdF97XFx0ZXh0e2NyaXR9fSQgZSwgY29uc2VxdWVudGVtZW50ZSwgbyAkcFxcdGV4dHstdmFsb3J9JCBlIG9zIGxpbWl0ZXMgZG8gJElDJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBhbmFsaXN0YSBkZSBkYWRvcyBkZSBJb1QgY29sZXRvdSAxMDAgcmVzw61kdW9zIGRlIHVtIHNpc3RlbWEgZGUgc2Vuc29yZXMuIEVsZSBkZXNlamEgdmFsaWRhciBhIG5vcm1hbGlkYWRlIHBhcmEgcHJvY2VkZXIgY29tIGluZmVyw6puY2lhcy4gRGVzY3JldmEgbyBwcm9jZWRpbWVudG8gYWxnb3LDrXRtaWNvIGNvbXBsZXRvLCBkZXNkZSBhIG9idGVuw6fDo28gZG9zIHJlc8OtZHVvcyBhdMOpIGEgaW50ZXJwcmV0YcOnw6NvIGRvIGdyw6FmaWNvLCB1dGlsaXphbmRvIGEgbm90YcOnw6NvIGZvcm1hbCBhZGVxdWFkYSAoJGUkLCAkUCQsICRyJCwgJHpfeyhpKX0kKS4iLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgcHJvamXDp8OjbyAkUCA9IFgoWCdYKV57LTF9WCckIHBhcmEgb2J0ZXIgbyB2ZXRvciAkZSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIENhbGN1bGFyIGEgbWF0cml6IGRlIHByb2plw6fDo28gJFAgPSBYKFgnWCleey0xfVgnJC4iLCAiMi4gRGV0ZXJtaW5hciBvIHZldG9yIGRlIHJlc8OtZHVvcyAkZSA9IChJIC0gUClZJC4iLCAiMy4gUGFkcm9uaXphciBvcyByZXPDrWR1b3MgcGFyYSBvYnRlciAkciQsIG9uZGUgJHJfaSQgcG9zc3VlbSBtw6lkaWEgMCBlIHZhcmnDom5jaWEgYXByb3hpbWFkYW1lbnRlIDEuIiwgIjQuIE9yZGVuYXIgb3MgdmFsb3JlcyBkZSAkciQgZW0gJHJfeygxKX0gXFxsZSByX3soMil9IFxcbGUgXFxkb3RzIFxcbGUgcl97KG4pfSQuIiwgIjUuIENhbGN1bGFyIG9zIHF1YW50aXMgdGXDs3JpY29zICR6X3soaSl9ID0gXFxQaGleey0xfVxcbGVmdChcXGZyYWN7aSAtIDAuMzc1fXtuICsgMC4yNX1cXHJpZ2h0KSQgcGFyYSBjYWRhICRpPTEgXFxkb3RzIG4kLiIsICI2LiBQbG90YXIgJHJfeyhpKX0kIG5vIGVpeG8gWSBlICR6X3soaSl9JCBubyBlaXhvIFguIEFuYWxpc2FyIGEgbGluZWFyaWRhZGUgZG9zIHBvbnRvcyBlbSByZWxhw6fDo28gw6AgcmV0YSBkZSAkNDVeXFxjaXJjJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9XX0=').decode('utf-8'))


    import plotly.graph_objects as go
    
    # Inicialização do estado da sessão para rastreamento de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo do progresso
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discursivas = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcqs) + len(discursivas)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    # Barra de progresso e placar
    st.progress(acertos / total_exercicios if total_exercicios > 0 else 0)
    st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    st.divider()
    
    # --- Seção de Questões de Múltipla Escolha ---
    if mcqs:
        st.header("🧠 Questões de Múltipla Escolha")
        for i, q in enumerate(mcqs):
            st.subheader(f"Questão {i + 1}")
            st.write(q.get("enunciado", ""))
            
            # Exibição de gráfico, se houver
            if q.get("codigo_plotly"):
                try:
                    local_vars = {"go": go}
                    exec(q["codigo_plotly"], globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True)
                except Exception as e:
                    st.warning("Não foi possível carregar o gráfico interativo.")
    
            # Alternativas
            opcoes = q.get("alternativas", {})
            selecao = st.radio(
                "Selecione sua resposta:",
                list(opcoes.keys()),
                format_func=lambda x: f"{x}: {opcoes[x]}",
                key=f"radio_mcq_{i}"
            )
            
            # Botão de Dica
            if st.button("💡 Dica", key=f"btn_dica_mcq_{i}"):
                st.info(q.get("dica", "Dica indisponível"))
    
            # Verificação
            if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
                if selecao == q.get("alternativa_correta"):
                    st.success("Correto! Muito bem.")
                    st.session_state.respostas_certas[f"mcq_{i}"] = True
                else:
                    st.error("Resposta incorreta. Tente novamente!")
                    st.session_state.respostas_certas[f"mcq_{i}"] = False
                st.rerun()
    
            # Referência e Gabarito
            if q.get("referencia_livro"):
                st.markdown(f"📖 *Referência: {q['referencia_livro']}*")
            
            with st.expander("✅ Ver Gabarito Comentado"):
                st.write(q.get("gabarito_comentado", "Gabarito indisponível"))
    
    # --- Seção de Questões Discursivas ---
    if discursivas:
        st.header("📝 Questões Discursivas")
        for i, q in enumerate(discursivas):
            st.subheader(f"Desafio {i + 1}")
            st.write(q.get("enunciado", ""))
            
            # Gráfico opcional
            if q.get("codigo_plotly"):
                try:
                    local_vars = {"go": go}
                    exec(q["codigo_plotly"], globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True)
                except Exception:
                    pass
    
            st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
            
            # Validação numérica (se aplicável)
            esperada = q.get("resposta_numerica_esperada")
            if esperada is not None:
                user_val = st.number_input("Digite o resultado numérico calculado para validação:", key=f"num_disc_{i}")
                if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                    if abs(user_val - esperada) <= max(0.01, 0.01 * abs(esperada)):
                        st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                    else:
                        st.error("O valor calculado difere do gabarito oficial. Verifique seus arredondamentos e fórmulas e tente novamente.")
                        st.session_state.respostas_certas[f"disc_{i}"] = False
                    st.rerun()
            else:
                # Validação qualitativa
                if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.session_state.respostas_certas[f"disc_{i}"] = False
    
            # Dica e Referência
            if st.button("💡 Dica", key=f"btn_dica_disc_{i}"):
                st.info(q.get("dica", "Dica indisponível"))
            if q.get("referencia_livro"):
                st.markdown(f"📖 *Referência: {q['referencia_livro']}*")
                
            with st.expander("✅ Ver Resolução Detalhada"):
                for passo in q.get("gabarito_passo_a_passo", []):
                    st.write(f"- {passo}")
