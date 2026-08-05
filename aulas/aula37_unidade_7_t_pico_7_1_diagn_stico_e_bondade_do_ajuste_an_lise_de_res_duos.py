import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDcgLSBUw7NwaWNvIDcuMTogRGlhZ27Ds3N0aWNvIGUgYm9uZGFkZSBkbyBhanVzdGU6IEFuw6FsaXNlIGRlIHJlc8OtZHVvcyIsICJyZWZlcmVuY2lhc19iaWJsaW9ncmFmaWNhc19maW5haXMiOiBbIkx1bmEgJiBFc3RldmVzLCBNb2RlbG9zIExpbmVhcmVzIC0gQ2FwLiA0LCBwcC4gODYtMTE4IiwgIlNlYmVyLCBMaW5lYXIgUmVncmVzc2lvbiBBbmFseXNpcyAtIENhcC4gMiAmIDMsIHBwLiAxOC00OCIsICJGYXJhd2F5LCBMaW5lYXIgTW9kZWxzIHdpdGggUiAtIENhcC4gNywgcHAuIDcyLTg0Il19').decode('utf-8'))

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

    import streamlit as st
    import numpy as np
    import pandas as pd
    
    # Cabeçalho do Subtópico
    st.header(r"A Natureza Geométrica e Algébrica dos Resíduos no Modelo Linear")
    
    # Introdução e Contexto Teórico
    st.markdown(r"""
    A modelagem estatística, em sua essência mais profunda, é um exercício intelectual de redução de complexidade. Quando analisamos observações empíricas em um espaço de dimensão $n$, buscamos uma estrutura subjacente que governe o fenômeno.
    """)
    
    st.info(r"""
    Ao postularmos um modelo linear, realizamos uma escolha topológica: restringimos nossa representação a um subespaço de dimensão $p$, o espaço coluna da matriz de design $X$. O vetor resposta $y$ é, portanto, decomposto entre a sua projeção no modelo ($\hat{y}$) e o componente de erro ($e$).
    """)
    
    st.markdown(r"""
    ### 🧩 Pilares da Decomposição Geométrica
    Para compreender o papel dos resíduos, devemos destacar os fundamentos deste arcabouço:
    - **Espaço do Modelo:** Definido pelo espaço coluna de $X$, onde reside a nossa expectativa teórica.
    - **Operador de Projeção:** A matriz chapéu $H = X(X^TX)^{-1}X^T$ projeta as observações brutas no espaço do modelo.
    - **Complemento Ortogonal:** O vetor de resíduos $e = (I - H)y$ reside no espaço ortogonal, contendo a informação não explicada.
    - **Independência de Informação:** A ortogonalidade entre $X$ e $e$ garante que a sinalização explicativa não se misture com o ruído residual.
    """)
    
    # Formalismo Matemático
    st.markdown(r"### 🧮 Formalismo Matemático: A Estrutura do Erro")
    st.latex(r"y = X\beta + \Delta \quad \text{onde} \quad e = (I - H)y \quad \text{com} \quad H = X(X^TX)^{-1}X^T")
    
    # Dedução Analítica
    st.markdown(r"### 📐 O Coração Matemático: Derivação do Estimador")
    st.write(r"A derivação do estimador de mínimos quadrados parte da minimização da soma de quadrados dos resíduos:")
    st.latex(r"S(\hat{e}) = \hat{e}'\hat{e} = (y - X\hat{\beta})'(y - X\hat{\beta})")
    st.latex(r"S(\hat{\beta}) = y'y - 2\hat{\beta}'X'y + \hat{\beta}'X'X\hat{\beta}")
    st.write(r"Ao derivarmos em relação a $\hat{\beta}$ e igualarmos a zero, obtemos as equações normais:")
    st.latex(r"\frac{\partial S}{\partial \hat{\beta}} = -2X'y + 2X'X\hat{\beta} = 0 \implies X'X\hat{\beta} = X'y")
    st.latex(r"\hat{\beta} = (X'X)^{-1}X'y")
    st.write(r"A partir daqui, definimos os valores ajustados e o resíduo:")
    st.latex(r"\hat{y} = X\hat{\beta} = X(X'X)^{-1}X'y = Hy")
    st.latex(r"e = y - \hat{y} = (I - H)y")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Análise de Resíduos em 4 Observações")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Modelo com Preditores Categóricos")
        st.markdown(r"""
        Considere um experimento com $n=4$ observações. O objetivo é calcular a projeção $\hat{y}$ e os resíduos $e$ dado:
        $y = [2, 3, 5, 4]'$ e a matriz de design $X$ com intercepto e dummy de categoria.
        """)
        
        st.latex(r"X'X = \begin{bmatrix} 4 & 2 & 2 \\ 2 & 2 & 0 \\ 2 & 0 & 2 \end{bmatrix}, \quad X'y = [14, 5, 9]'")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Resolvemos o sistema $X'X\hat{\beta} = X'y$ para encontrar os coeficientes $\hat{\beta} = [3, -0.5, -0.5]'$.")
        st.markdown(r"- Calculamos a projeção $\hat{y} = X\hat{\beta} = [2.5, 2.5, 2.5, 2.5]'$.")
        st.markdown(r"- Derivamos o resíduo $e = y - \hat{y} = [-0.5, 0.5, 2.5, 1.5]'$.")
        
        st.success(r"Conclusão: O vetor de resíduos é $e = [-0.5, 0.5, 2.5, 1.5]'$. A soma dos resíduos é zero, confirmando que o modelo captura a média global e isola as variações aleatórias.")
    
    # Nota Final
    st.divider()
    st.caption(r"A elegância do modelo linear reside nesta separação ortogonal: a geometria dos dados reflete a precisão da nossa teoria científica.")

    # Cabeçalho do Subtópico
    st.header(r"Propriedades Estatísticas e Estrutura de Covariância dos Resíduos")
    
    # Introdução e Fundamentos Teóricos
    st.markdown(r"""
    A análise dos resíduos constitui o pilar crítico para a validação de modelos de regressão linear. Quando construímos um modelo, supomos que a relação entre as variáveis é mediada por uma estrutura de erro latente $\Delta$, representando a variabilidade estocástica que o modelo não consegue explicar. Teoricamente, estes erros são independentes e identicamente distribuídos.
    """)
    
    st.info(r"Nota Técnica: O processo de estimação por mínimos quadrados ordinários impõe uma geometria específica que altera a natureza dos resíduos amostrais $e$ em relação aos erros populacionais $\Delta$.")
    
    st.markdown(r"""
    Alguns aspectos fundamentais sobre o comportamento dos resíduos incluem:
    - **Ortogonalidade:** O vetor de resíduos é, por definição, ortogonal ao espaço gerado pela matriz de desenho $X$.
    - **Esperança Nula:** O método garante $E[e] = 0$, assegurando a ausência de viés sistemático na tendência central.
    - **Estrutura de Variância:** A dispersão dos resíduos não é constante, sendo condicionada pela matriz chapéu $H$.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 A Geometria da Incerteza: O Operador de Projeção $H$")
    st.markdown(r"A estrutura de variância dos resíduos revela que a variabilidade é restringida pela geometria do espaço amostral:")
    st.latex(r"E[e] = 0 \quad \text{e} \quad Var[e] = \sigma^2(I - H)")
    
    st.warning(r"Esta estrutura indica que, independentemente da independência original dos erros $\Delta$, os resíduos exibem, por definição, uma estrutura de correlação intrínseca e variabilidade heterogênea.")
    
    # Demonstração Analítica
    st.subheader(r"🧮 Formalismo e Demonstração da Estrutura de Covariância")
    st.markdown(r"Considerando $e = (I - H)y$, derivamos as propriedades estatísticas através do operador de projeção:")
    
    st.latex(r"e = (I - H)y")
    st.markdown(r"A esperança matemática demonstra a ortogonalidade:")
    st.latex(r"E[e] = (I - H)E[y] = (I - H)X\theta = X\theta - H X\theta = X\theta - X\theta = 0")
    
    st.markdown(r"A estrutura de covariância é obtida através da álgebra de variâncias:")
    st.latex(r"Var[e] = Var[(I - H)y] = (I - H)Var[y](I - H)^T")
    st.latex(r"Var[e] = \sigma^2 (I - H)I(I - H)^T = \sigma^2 (I - H)(I - H) = \sigma^2(I - H)")
    
    # Exemplos Práticos
    st.subheader(r"📈 Caso de Estudo: Estrutura de Dependência em Duas Observações")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Modelo de Média Global")
        st.markdown(r"Considere um modelo linear simples com duas observações onde $y_1 = \mu + \Delta_1$ e $y_2 = \mu + \Delta_2$. A matriz de design é $X = [1, 1]^T$.")
        
        st.latex(r"X = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad X^TX = 2, \quad H = \begin{bmatrix} 0.5 & 0.5 \\ 0.5 & 0.5 \end{bmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Primeiro, calculamos a matriz complementar $I - H$:")
        st.latex(r"I - H = \begin{bmatrix} 0.5 & -0.5 \\ -0.5 & 0.5 \end{bmatrix}")
        st.markdown(r"- Observamos o vetor resultante $e$:")
        st.latex(r"e = (I - H)y = \begin{bmatrix} 0.5(y_1 - y_2) \\ 0.5(y_2 - y_1) \end{bmatrix}")
        
        st.success(r"Conclusão: A estrutura de variância $Var[e] = \sigma^2 \begin{bmatrix} 0.5 & -0.5 \\ -0.5 & 0.5 \end{bmatrix}$ demonstra que os resíduos não são independentes. A correlação negativa entre $e_1$ e $e_2$ é a assinatura geométrica da restrição de média global.")
    
    # Considerações Finais
    st.markdown(r"""
    ---
    A transição da intuição sobre o erro populacional para o formalismo dos resíduos marca a fronteira da estatística rigorosa. Compreender que $Var[e] = \sigma^2(I - H)$ permite que o pesquisador diferencie violações reais de pressupostos (como heteroscedasticidade) dos efeitos geométricos esperados pela arquitetura do design amostral.
    """)

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho
    st.header(r"Padronização e Studentização: Técnicas de Escalonamento de Erros")
    
    # Prosa Teórica
    st.markdown(r"""
    A análise de regressão linear clássica pressupõe que os erros são independentes e possuem variância constante. Contudo, observações com alta alavancagem ($h_i$) distorcem essa premissa. O modelo, ao minimizar a soma dos quadrados, aproxima-se desproporcionalmente de pontos extremos, reduzindo artificialmente seus resíduos brutos.
    """)
    
    st.info(r"**Por que a normalização é vital?** A magnitude absoluta de um resíduo é enganosa. Sem corrigir pelo efeito da alavancagem, outliers influentes podem passar despercebidos, pois eles próprios 'puxam' o ajuste do modelo, reduzindo a variância estimada localmente.")
    
    st.markdown(r"""
    ### 📐 O Coração Matemático: Escalonamento de Resíduos
    
    A padronização e a studentização corrigem a heterocedasticidade induzida pela geometria do conjunto de dados, permitindo uma comparação honesta entre erros.
    """)
    
    # Deduções Analíticas
    st.latex(r"Var[\Delta_i] = \sigma^2(1 - h_i)")
    st.markdown(r"A padronização ajusta o resíduo para ter variância unitária:")
    st.latex(r"r_i = \frac{\Delta_i}{\hat{\sigma} \sqrt{1 - h_i}}")
    st.markdown(r"A studentização externa remove a influência do ponto $i$ no cálculo da variância residual ($\hat{\sigma}_{(i)}$):")
    st.latex(r"t_i = r_i \sqrt{\frac{n - p - 1}{n - p - r_i^2}}")
    
    # Simulador Interativo
    st.subheader(r"📈 Simulador de Diagnóstico de Resíduos")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write(r"Edite os dados para observar o impacto no diagnóstico:")
        df_inicial = np.array([[1.0, 2.1], [2.0, 3.9], [3.0, 6.2], [4.0, 8.1], [10.0, 25.0]])
        df_editor = st.data_editor(df_inicial, num_rows="dynamic", key=r"data_editor_subtopico_3")
    
    with col2:
        exibir_regressao = st.toggle(r"Exibir Reta de Regressão", value=True, key=r"toggle_reg_subtopico_3")
        
    # Processamento do Simulador
    X = df_editor[:, 0]
    Y = df_editor[:, 1]
    slope, intercept, _, _, _ = stats.linregress(X, Y)
    y_pred = slope * X + intercept
    residuos = Y - y_pred
    
    # Configuração do gráfico
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=X, y=Y, mode='markers', name=r"Observações", marker=dict(color="#0000FF")))
    if exibir_regressao:
        fig.add_trace(go.Scatter(x=X, y=y_pred, mode='lines', name=r"Modelo", line=dict(color="#808080")))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Análise de Resíduos vs Alavancagem</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Preditor X", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Resíduo", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    # Laudo dinâmico
    max_res = np.max(np.abs(residuos))
    st.info(r"O valor máximo de resíduo observado é de " + str(round(max_res, 3)) + r". Pontos com resíduos normalizados acima de 2.0 ou 3.0 indicam anomalias estruturais.")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática: Identificação de Outliers")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Eficiência Industrial")
        st.markdown(r"Em um estudo de eficiência com $n=20$ e $p=3$, observou-se para um ponto: $\Delta_i = 2.0$, $h_i = 0.4$ e $\hat{\sigma} = 1.0$.")
        st.latex(r"n=20, p=3, \Delta_i = 2.0, h_i = 0.4, \hat{\sigma} = 1.0")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo do resíduo padronizado: $r_i = \frac{2.0}{1.0 \sqrt{1 - 0.4}} \approx 2.582$")
        st.markdown(r"- Cálculo do resíduo studentizado: $t_i = 2.582 \sqrt{\frac{20 - 3 - 1}{20 - 3 - 2.582^2}} \approx 3.214$")
        st.success(r"O valor $t_i \approx 3.214$ excede os limiares críticos, confirmando que a observação é um outlier influente que compromete o ajuste.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Diagnóstico de Homocedasticidade e Linearidade através de Análise Visual")
    
    # Prosa Teórica - Parte 1
    st.markdown(r"""
    A análise visual de resíduos versus valores ajustados permanece como a ferramenta intuitiva mais eficaz para o diagnóstico de modelos lineares. Sob as premissas do modelo ideal, espera-se que a nuvem de resíduos esteja distribuída de forma aleatória em torno do eixo zero.
    """)
    
    st.info(r"Desvios sistemáticos, como o 'efeito funil', sinalizam a violação da homocedasticidade, enquanto curvaturas sugerem falhas na especificação funcional do modelo.")
    
    # Prosa Expandida e Estruturada
    st.markdown(r"""
    ### 🔍 A Essência do Diagnóstico de Resíduos
    A análise de resíduos transcende a verificação de pressupostos; ela é o "olho clínico" do modelador. Ao examinarmos os resíduos $\Delta_i = Y_i - \hat{Y}_i$, investigamos a essência da informação que o modelo foi incapaz de capturar.
    
    Em um modelo perfeitamente especificado, o resíduo deve comportar-se como **ruído branco**:
    *   **Média Condicional Nula:** $E[\Delta_i | \hat{Y}_i] = 0$
    *   **Variância Estável:** $Var[\Delta_i | \hat{Y}_i] \approx \sigma^2$
    """)
    
    # Formalismo Matemático
    st.latex(r"E[e_i | \hat{y}_i] = 0 \quad \text{e} \quad Var[e_i | \hat{y}_i] \approx \sigma^2")
    
    # Dedução Analítica (Sequencial)
    st.markdown(r"### 📐 O Rigor Matemático: Fundamentos dos Resíduos")
    st.write(r"A estrutura dos resíduos pode ser decomposta via matriz de projeção $P = X(X^TX)^{-1}X^T$:")
    st.latex(r"\mathbf{e} = (I - P)\mathbf{y}")
    st.write(r"Dada a natureza do modelo, a esperança dos resíduos resulta em:")
    st.latex(r"E[\mathbf{e}] = (I - P)X\theta = 0")
    st.write(r"Por fim, a variância de cada resíduo é influenciada pelo 'leverage' (alavancagem) $h_i$:")
    st.latex(r"Var[e_i] = \sigma^2(1 - h_i)")
    
    # Simulador de Diagnóstico Visual
    st.markdown(r"### 🎮 Simulador: Diagnóstico Visual de Resíduos")
    col1, col2 = st.columns(2)
    curvatura = col1.slider(r"Nível de Não-Linearidade (Curvatura)", 0.0, 2.0, 0.0, step=0.1, key=r"curv_subtopico_4")
    hetero = col2.slider(r"Nível de Heterocedasticidade (Funil)", 0.0, 2.0, 0.0, step=0.1, key=r"hetero_subtopico_4")
    
    # Geração de dados para o simulador
    n = 100
    x = np.linspace(0, 10, n)
    y_ideal = 2 + 1.5 * x
    residuos = np.random.normal(0, 1 + hetero * x, n) + curvatura * (x - 5)**2
    y_ajustado = 2 + 1.5 * x # Modelo linear simples ignorando curvatura
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_ajustado, y=residuos, mode='markers', name=r"Resíduos", marker=dict(color=r"#0000FF")))
    fig.add_hline(y=0, line_dash="dash", line_color=r"#64748B")
    
    fig.update_layout(
        template=r"plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Análise Visual de Resíduos vs Ajustados</b>", font=dict(size=14, color=r"#1E293B", family=r"Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Valores Ajustados", font=dict(size=11, color=r"#1E293B")), tickfont=dict(size=9, color=r"#64748B"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Resíduos", font=dict(size=11, color=r"#1E293B")), tickfont=dict(size=9, color=r"#64748B"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        legend=dict(orientation=r"h", yanchor=r"bottom", y=1.02, xanchor=r"right", x=1.0, font=dict(size=9, color=r"#64748B"), bgcolor=r"rgba(255, 255, 255, 0.8)", bordercolor=r"#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor=r"#FFFFFF", font_size=12, font_color=r"#1E293B")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")
    
    # Laudo Dinâmico do Simulador
    laudo = r"Análise: "
    if curvatura > 0.5: laudo += r"Foi detectada uma curvatura sistemática, indicando subespecificação do modelo. "
    if hetero > 0.5: laudo += r"O padrão de funil sugere heterocedasticidade latente."
    if curvatura <= 0.5 and hetero <= 0.5: laudo += r"O modelo apresenta um comportamento estável e sem padrões evidentes nos resíduos."
    st.info(laudo)
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Monitoramento de Frota")
        st.markdown(r"Durante o monitoramento de uma frota, o gráfico de resíduos vs. valores ajustados exibiu uma tendência parabólica em 'U' e um padrão de alargamento da dispersão (funil).")
        st.latex(r"Pattern: U-shape, \text{Heteroscedasticity}")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Identificada a tendência em U: $E[e|\hat{y}] \neq 0$. Necessária inclusão de termo quadrático $x^2$.")
        st.markdown(r"- Identificado efeito funil: $Var[e|\hat{y}]$ não constante. Necessária transformação logarítmica $\log(y)$.")
        st.success(r"O modelo está mal especificado. Recomenda-se a reespecificação para incluir termos não-lineares e aplicação de log-transformação na variável resposta.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do subtópico
    st.header(r"Inferência sobre a Normalidade e Pressupostos dos Erros")
    
    # Discussão Teórica com ritmo de leitura
    st.markdown(r"""
    A hipótese de normalidade dos erros é a pedra angular para a validade das estatísticas $t$ e $F$ de inferência. Sem essa pressuposição, os intervalos de confiança e testes de hipóteses dependem estritamente do Teorema do Limite Central, o que pode não ser adequado para amostras pequenas.
    """)
    
    st.info(r"A suposição de normalidade, denotada através do termo estocástico $\Delta$, não é uma conveniência matemática, mas a fundação da inferência paramétrica clássica. Ela postula que as flutuações ao redor da linha de regressão são simétricas e possuem variância constante $\sigma^2$.")
    
    st.markdown(r"""
    Ao assumirmos que os erros seguem uma distribuição normal, garantimos que nossas estimativas de mínimos quadrados respeitam a lógica gaussiana. Isso nos permite quantificar a incerteza com precisão, tornando os testes de significância robustos. Entre os pontos cruciais desta fundamentação, destacamos:
    - **Simetria dos Erros:** As flutuações acima e abaixo da linha de regressão devem se cancelar em média (média zero).
    - **Homocedasticidade:** A dispersão da incerteza deve permanecer estável ao longo de todo o domínio das variáveis explicativas.
    - **Validade Inferencial:** A utilização das distribuições $t$ de Student e $F$ de Snedecor exige que a distribuição dos erros seja normal para que os níveis de confiança sejam exatos.
    """)
    
    # O Coração Matemático
    st.markdown(r"### 📐 O Coração Matemático: Distribuição da Variância Residual")
    st.markdown(r"A relação estatística fundamental que permite inferir sobre a variância populacional $\sigma^2$ a partir da soma dos quadrados dos erros (SQE) é dada pela distribuição qui-quadrado:")
    
    st.latex(r"\frac{SQE}{\sigma^2} \sim \chi^2(n - p)")
    
    st.markdown(r"A dedução deste formalismo segue a decomposição da variabilidade residual:")
    
    st.latex(r"\frac{SQE}{\sigma^2} = \frac{\mathbf{e}^T \mathbf{e}}{\sigma^2}")
    st.latex(r"\frac{SQE}{\sigma^2} = \frac{\Delta^T (I - P) \Delta}{\sigma^2}")
    
    st.markdown(r"Sendo a matriz $(I - P)$ idempotente com posto $n-p$, a forma quadrática resultante segue, por definição, a distribuição $\chi^2$ com $n-p$ graus de liberdade.")
    
    # Ferramentas de Diagnóstico
    st.markdown(r"### 🔍 Diagnóstico Visual: O Gráfico Quantil-Quantil (Q-Q Plot)")
    st.markdown(r"""
    Para validar a normalidade, o Q-Q Plot compara os quantis empíricos dos resíduos padronizados contra os quantis teóricos. 
    - **Alinhamento:** Se os pontos seguem a reta de 45 graus, a hipótese de normalidade é suportada.
    - **Desvios nas extremidades:** Caudas pesadas ou assimetrias indicam que o modelo pode estar falhando em capturar a estrutura do ruído.
    """)
    
    # Casos de Aplicação Prática
    st.markdown(r"### 📈 Casos de Aplicação Prática: Inferência sobre a Variância")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Teste de Aderência da Variância")
        st.markdown(r"Em um teste de qualidade industrial com $n=15$ amostras e $p=3$ parâmetros estimados, obteve-se uma Soma dos Quadrados do Erro (SQE) de $28.5$. Deseja-se testar, ao nível de significância de $5\%$, se a variância populacional pode ser considerada $\sigma^2 = 2.0$.")
        
        st.latex(r"\chi^2_{\text{calc}} = \frac{SQE}{\sigma^2} = \frac{28.5}{2.0} = 14.25")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Determinação dos graus de liberdade: $gl = n - p = 15 - 3 = 12$.")
        st.markdown(r"- Valor crítico na tabela $\chi^2$ para $12$ graus de liberdade e $\alpha=0.05$: $\chi^2_{0.05, 12} \approx 21.03$.")
        st.markdown(r"- Comparação: $14.25 < 21.03$.")
        
        st.success(r"Conclusão: Como a estatística calculada é inferior ao valor crítico, não há evidência estatística suficiente para rejeitar a hipótese de que a variância é $2.0$. O modelo apresenta conformidade com a pressuposição de normalidade para este nível de significância.")
    
    # Conclusão Reflexiva
    st.markdown(r"---")
    st.markdown(r"**Nota do Especialista:** A inferência sobre a normalidade não é uma burocracia, mas um teste de integridade. Violar esta premissa em modelos de pequena escala é um erro de julgamento que pode inflar o erro Tipo I. Sempre priorize a verificação rigorosa dos resíduos antes de validar a significância dos coeficientes.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDcgLSBUw7NwaWNvIDcuMTogRGlhZ27Ds3N0aWNvIGUgYm9uZGFkZSBkbyBhanVzdGU6IEFuw6FsaXNlIGRlIHJlc8OtZHVvcyIsICJxdWVzdG9lc19tdWx0aXBsYV9lc2NvbGhhIjogW3siZW51bmNpYWRvIjogIkVtIHVtIGV4cGVyaW1lbnRvIGRlIGNhbGlicmHDp8OjbyBkZSBzZW5zb3JlcyBJb1QsIHVtIGVuZ2VuaGVpcm8gYWp1c3RhIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvIGxpbmVhciBzaW1wbGVzICR5ID0gWFx0aGV0YSArIFx0ZXh0e2Vycm9yfSQgY29tICRuPTMwJCBvYnNlcnZhw6fDtWVzLiBBbyBhbmFsaXNhciBhIGVzdHJ1dHVyYSBkb3MgcmVzw61kdW9zICRlID0gKEktUCl5JCwgb25kZSAkUCA9IFgoWF5UWCleey0xfVheVCQgw6kgYSBtYXRyaXogZGUgcHJvamXDp8OjbywgbyBlbmdlbmhlaXJvIGJ1c2NhIHZhbGlkYXIgc2UgbyBtb2RlbG8gY2FwdHVyb3UgYSBlc3RydXR1cmEgc2lzdGVtw6F0aWNhIGRvcyBkYWRvcy4gQ29uc2lkZXJlIGFzIHByb3ByaWVkYWRlcyBnZW9tw6l0cmljYXMgZGVzc2EgcHJvamXDp8Ojby4gUXVhbCBkYXMgYWx0ZXJuYXRpdmFzIGFiYWl4byBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgYSByZWxhw6fDo28gZW50cmUgbyB2ZXRvciBkZSB2YWxvcmVzIGFqdXN0YWRvcyAkXFxoYXR7eX0kIGUgbyB2ZXRvciBkZSByZXPDrWR1b3MgJGUkPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyB2ZXRvciBkZSByZXPDrWR1b3MgJGUkIMOpIGNvbGluZWFyIGFvIHZldG9yIGRlIHZhbG9yZXMgYWp1c3RhZG9zICRcXGhhdHt5fSQsIGluZGljYW5kbyBxdWUgbyBtb2RlbG8gw6kgY2FwYXogZGUgZXhwbGljYXIgcGVyZmVpdGFtZW50ZSB0b2RhIGEgdmFyaWHDp8OjbyBkb3MgZGFkb3MuIiwgIkIiOiAiTyBwcm9kdXRvIGludGVybm8gZW50cmUgbyB2ZXRvciBkZSB2YWxvcmVzIGFqdXN0YWRvcyBlIG8gdmV0b3IgZGUgcmVzw61kdW9zIMOpIHNlbXByZSBpZ3VhbCDDoCBzb21hIGRvcyBxdWFkcmFkb3MgZG8gZXJybyAoU1FSZXMpLCB2YWxpZGFuZG8gYSBlZmljacOqbmNpYSBkbyBlc3RpbWFkb3IuIiwgIkMiOiAiTyB2ZXRvciBkZSByZXPDrWR1b3MgJGUkIMOpIG9ydG9nb25hbCBhbyBlc3Bhw6dvIGNvbHVuYSBkZSAkWCQsIGdhcmFudGluZG8gcXVlICRcXGhhdHt5fV5UIGUgPSAwJCBwYXJhIHF1YWxxdWVyIHZldG9yIGRlIG9ic2VydmHDp8O1ZXMgJHkkLiIsICJEIjogIkEgdmFyacOibmNpYSBkb3MgcmVzw61kdW9zIMOpIGRhZGEgcG9yICRWYXJbZV0gPSBcXHNpZ21hXjIgSSQsIG8gcXVlIGltcGxpY2EgcXVlIG9zIHJlc8OtZHVvcyBzw6NvIGluZGVwZW5kZW50ZXMgZW50cmUgc2ksIGluZGVwZW5kZW50ZW1lbnRlIGRhIG1hdHJpeiBkZSBkZXNpZ24gJFgkLiIsICJFIjogIkEgcHJvamXDp8OjbyAkUCQgbsOjbyBhbHRlcmEgYSBkaW1lbnPDo28gZG8gZXNwYcOnbyBvcmlnaW5hbCwgcG9ydGFudG8gJGUkIHNlbXByZSBwb3NzdWkgYSBtZXNtYSBkaW1lbnPDo28gcXVlICR5JCBlIMOpIGluZGVwZW5kZW50ZSBkYSBtYXRyaXogJFgkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSAkUCQgw6kgdW1hIG1hdHJpeiBkZSBwcm9qZcOnw6NvIHNpbcOpdHJpY2EgZSBpZGVtcG90ZW50ZSAoJFBeMiA9IFAkKS4gQW5hbGlzZSBvIHByb2R1dG8gJFxcaGF0e3l9XlQgZSA9IChQeSleVCAoSS1QKXkkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBtYXRyaXogZGUgcHJvamXDp8OjbyAkUCQgdGVtIGEgcHJvcHJpZWRhZGUgZGUgcHJvamV0YXIgbyB2ZXRvciAkeSQgbm8gZXNwYcOnbyBjb2x1bmEgZGUgJFgkLiBPIHZldG9yIGRlIHJlc8OtZHVvcyAkZSA9IChJLVApeSQgcmVwcmVzZW50YSBhIGNvbXBvbmVudGUgZGUgJHkkIHF1ZSDDqSBvcnRvZ29uYWwgYW8gZXNwYcOnbyBjb2x1bmEgZGUgJFgkLiBDb21vICRcXGhhdHt5fSA9IFB5JCwgdGVtb3MgJFxcaGF0e3l9XlQgZSA9IChQeSleVCAoSS1QKXkgPSB5XlQgUF5UIChJLVApIHkgPSB5XlQgKFAgLSBQXjIpIHkkLiBDb21vICRQXjIgPSBQJCwgcmVzdWx0YSAkeV5UKFAtUCl5ID0gMCQsIGRlbW9uc3RyYW5kbyBhIG9ydG9nb25hbGlkYWRlLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpOyBmaWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMCwgMV0sIHk9WzAsIDBdLCBtb2RlPSdsaW5lcycsIGxpbmU9ZGljdChjb2xvcj0nIzAwMDBGRicsIHdpZHRoPTIpLCBuYW1lPXInRXNwYcOnbyBkZSBYJykpOyBmaWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMCwgMF0sIHk9WzAsIDFdLCBtb2RlPSdsaW5lcycsIGxpbmU9ZGljdChjb2xvcj0nI0ZGMDAwMCcsIHdpZHRoPTIpLCBuYW1lPXInRXNwYcOnbyBkb3MgUmVzw61kdW9zJykpOyBmaWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+T3J0b2dvbmFsaWRhZGU6IFByb2plw6fDo28gZSBSZXPDrWR1b3M8L2I+JywgeGF4aXM9ZGljdCh0aXRsZT0nVmFsb3JlcyBBanVzdGFkb3MgKFxcaGF0e3l9KScsIGZpeGVkcmFuZ2U9VHJ1ZSksIHlheGlzPWRpY3QodGl0bGU9J1Jlc8OtZHVvcyAoZSknLCBmaXhlZHJhbmdlPVRydWUpLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBhbmFsaXN0YSBkZSBkYWRvcyBlc3R1ZGEgYSBlc3RydXR1cmEgZGUgY292YXJpw6JuY2lhIGRvcyByZXPDrWR1b3MgcGFyYSB2ZXJpZmljYXIgYSB2YWxpZGFkZSBkYXMgcHJlbWlzc2FzIGRlIHVtIG1vZGVsbyBsaW5lYXIgYXBsaWNhZG8gYSBjdXN0b3MgbG9nw61zdGljb3MuIFNhYmUtc2UgcXVlIGEgbWF0cml6IGRlIGNvdmFyacOibmNpYSBkb3MgcmVzw61kdW9zIMOpIGRhZGEgcG9yICRWYXJbZV0gPSBcXHNpZ21hXjIgKEkgLSBQKSQuIENvbSBiYXNlIG5lc3NhIGVzdHJ1dHVyYSwgY29tbyBwb2RlbW9zIGludGVycHJldGFyIGNvcnJldGFtZW50ZSBvIGltcGFjdG8gZGEgbWF0cml6IGRlIGRlc2lnbiAkWCQgbmEgdmFyaWFiaWxpZGFkZSBkb3MgcmVzw61kdW9zIG9ic2VydmFkb3M/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIG1hdHJpeiAkKEktUCkkIMOpIHBvc2l0aXZhIGRlZmluaWRhLCBwb3J0YW50byBhIHZhcmnDom5jaWEgZGUgY2FkYSByZXPDrWR1byAkZV9pJCDDqSBzZW1wcmUgaWd1YWwgYSAkXFxzaWdtYV4yJCwgZ2FyYW50aW5kbyBob21vY2VkYXN0aWNpZGFkZS4iLCAiQiI6ICJBIHNvbWEgZGEgdmFyacOibmNpYSBkb3MgcmVzw61kdW9zLCBkYWRhIHBvciAkVHIoVmFyW2VdKSA9IFxcc2lnbWFeMiAobiAtIHApJCwgaW5kaWNhIHF1ZSBhIHZhcmlhYmlsaWRhZGUgdG90YWwgZG8gZXJybyBkaW1pbnVpIGNvbmZvcm1lIGF1bWVudGFtb3MgbyBuw7ptZXJvIGRlIHBhcsOibWV0cm9zICRwJCBkbyBtb2RlbG8uIiwgIkMiOiAiQSBlc3RydXR1cmEgZGUgY292YXJpw6JuY2lhIGRvcyByZXPDrWR1b3Mgw6kgaW5kZXBlbmRlbnRlIGRlICRYJCBlIGRlcGVuZGUgYXBlbmFzIGRvIG7Dum1lcm8gZGUgb2JzZXJ2YcOnw7VlcyAkbiQuIiwgIkQiOiAiQSBtYXRyaXogJChJLVApJCBwb3NzdWkgcG9zdG8gbcOheGltbyAkbiQsIHRvcm5hbmRvIGEgdmFyacOibmNpYSBkb3MgcmVzw61kdW9zIHVtYSBtYXRyaXogZGlhZ29uYWwgZGUgaWRlbnRpZGFkZSBkaW1lbnNpb25hZGEuIiwgIkUiOiAiQSBjb3ZhcmnDom5jaWEgZW50cmUgZG9pcyByZXPDrWR1b3MgZGlzdGludG9zICRlX2kkIGUgJGVfaiQgw6kgc2VtcHJlIHplcm8sIG1lc21vIHBhcmEgYW1vc3RyYXMgZmluaXRhcyBlIG1hdHJpemVzICRYJCBhcmJpdHLDoXJpYXMuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJDb25zaWRlcmUgbyB0cmHDp28gZGEgbWF0cml6ICQoSS1QKSQuIE8gdHJhw6dvIGRlIHVtYSBtYXRyaXogZGUgcHJvamXDp8OjbyAkUCQgw6kgaWd1YWwgYW8gc2V1IHBvc3RvLCBxdWUgw6kgJHAkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSB2YXJpw6JuY2lhIHRvdGFsIGRvcyByZXPDrWR1b3Mgw6kgYSBzb21hIGRhcyB2YXJpw6JuY2lhcyBpbmRpdmlkdWFpcywgcXVlIMOpIG8gdHJhw6dvIGRhIG1hdHJpeiBkZSBjb3ZhcmnDom5jaWE6ICRUcihWYXJbZV0pID0gVHIoXFxzaWdtYV4yKEktUCkpID0gXFxzaWdtYV4yIChUcihJKSAtIFRyKFApKSQuIENvbW8gJFRyKEkpID0gbiQgZSAkVHIoUCkgPSByYW5rKFgpID0gcCQsIHRlbW9zICRcXHNpZ21hXjIgKG4gLSBwKSQuIElzc28gbW9zdHJhIHF1ZSBvIG7Dum1lcm8gZGUgZ3JhdXMgZGUgbGliZXJkYWRlIHBhcmEgbyBlcnJvIMOpICRuLXAkLCBpbXBhY3RhbmRvIGEgZXN0aW1hdGl2YSBkYSB2YXJpw6JuY2lhIHJlc2lkdWFsLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIG3Dumx0aXBsYSwgbyBkaWFnbsOzc3RpY28gZGUgcmVzw61kdW9zIMOpIGVzc2VuY2lhbCBwYXJhIGdhcmFudGlyIGEgdmFsaWRhZGUgZGFzIHByZW1pc3Nhcy4gQ29uc2lkZXJlIHF1ZSwgYW8gYW5hbGlzYXIgYSBpbmZsdcOqbmNpYSBkZSB1bSBjb25qdW50byBkZSBkYWRvcywgdm9jw6ogaWRlbnRpZmljb3UgcXVlIHVtYSBvYnNlcnZhw6fDo28gZXNwZWPDrWZpY2EgcG9zc3VpIHVtIHZhbG9yIGRlIGFsYXZhbmNhZ2VtICRoX2kgPSAwLjg1JCBlbSB1bSBjb25qdW50byBjb20gJG49MjAkIG9ic2VydmHDp8O1ZXMgZSAkcD0zJCBwYXLDom1ldHJvcy4gU29icmUgYSBpbnRlcnByZXRhw6fDo28gZG9zIHJlc8OtZHVvcyBzdHVkZW50aXphZG9zIGludGVybm9zICgkcl9pJCkgZSBleHRlcm5vcyAoJHRfaSQpLCBhc3NpbmFsZSBhIGFsdGVybmF0aXZhIGNvcnJldGE6IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIHZhbG9yIGRlIGFsYXZhbmNhZ2VtICRoX2k9MC44NSQgaW5kaWNhIHF1ZSBlc3RhIG9ic2VydmHDp8OjbyB0ZW0gaW5mbHXDqm5jaWEgbcOtbmltYSBzb2JyZSBhIHJldGEgZGUgcmVncmVzc8OjbyBhanVzdGFkYS4iLCAiQiI6ICJSZXPDrWR1b3Mgc3R1ZGVudGl6YWRvcyBpbnRlcm5vcyAoJHJfaSQpIHBvc3N1ZW0gc2VtcHJlIHZhcmnDom5jaWEgdW5pdMOhcmlhLCBpbmRlcGVuZGVudGVtZW50ZSBkYSBhbGF2YW5jYWdlbSAkaF9pJCBkYSBvYnNlcnZhw6fDo28uIiwgIkMiOiAiTyByZXPDrWR1byBzdHVkZW50aXphZG8gZXh0ZXJubyAoJHRfaSQpIMOpIHByZWZlcsOtdmVsIHBhcmEgZGV0ZWN0YXIgb3V0bGllcnMsIHBvaXMgZWxlIHV0aWxpemEgJFxcaGF0e1xcc2lnbWF9X3soaSl9JCwgcXVlIG9taXRlIGEgb2JzZXJ2YcOnw6NvICRpJCBkbyBjw6FsY3VsbywgZXZpdGFuZG8gcXVlIG8gb3V0bGllciBvY3VsdGUgc3VhIHByw7NwcmlhIG1hZ25pdHVkZS4iLCAiRCI6ICJPIHJlc8OtZHVvIHN0dWRlbnRpemFkbyBpbnRlcm5vICgkcl9pJCkgZSBvIGV4dGVybm8gKCR0X2kkKSBzw6NvIGlkw6pudGljb3MgZW0gdG9kb3Mgb3MgY2Fzb3MsIHRvcm5hbmRvIGEgZGlzdGluw6fDo28gYXBlbmFzIHRlw7NyaWNhLiIsICJFIjogIkEgYWxhdmFuY2FnZW0gJGhfaSQgbsOjbyBhZmV0YSBhIHZhcmnDom5jaWEgZG8gZXJybyAkXFxEZWx0YV9pJCwgcG9ydGFudG8gYSBzdHVkZW50aXphw6fDo28gw6kgZGVzbmVjZXNzw6FyaWEgZW0gbW9kZWxvcyBjb20gJGhfaSA+IDAuNSQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJMZW1icmUtc2UgZGUgcXVlIGEgdmFyacOibmNpYSBkbyByZXPDrWR1byBicnV0byAkXFxEZWx0YV9pJCBkZXBlbmRlIGRlICQoMS1oX2kpJC4gUXVhbmRvICRoX2kkIMOpIGFsdG8sIGEgdmFyacOibmNpYSDDqSByZWR1emlkYSwgZm9yw6dhbmRvIG8gcmVzw61kdW8gYSBzZXIgcGVxdWVuby4gTyByZXPDrWR1byAnamFja2tuaWZlJyB0ZW50YSBtaXRpZ2FyIGVzc2UgZWZlaXRvIGRlICdtYXNjYXJhbWVudG8nLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBhbHRlcm5hdGl2YSBDIGVzdMOhIGNvcnJldGEuIEEgYWxhdmFuY2FnZW0gJGhfaSQgbWVkZSBvIHF1w6NvIGRpc3RhbnRlIG8gcG9udG8gJHhfaSQgZXN0w6EgZG8gY2VudHJvIGRvIGVzcGHDp28gZG9zIHJlZ3Jlc3NvcmVzLiBVbSB2YWxvciAkaF9pPTAuODUkIGVtIHVtIG1vZGVsbyBjb20gJG49MjAsIHA9MyQgKG9uZGUgbyB2YWxvciBtw6lkaW8gZGUgJGhfaSQgw6kgJHAvbiA9IDAuMTUkKSDDqSBleHRyZW1hbWVudGUgYWx0bywgaW5kaWNhbmRvIGFsdGEgaW5mbHXDqm5jaWEuIE8gcmVzw61kdW8gaW50ZXJubyAkcl9pJCBkaXZpZGUgJFxcRGVsdGFfaSQgcG9yIHVtYSBlc3RpbWF0aXZhIGRlIGRlc3ZpbyBwYWRyw6NvIHF1ZSBpbmNsdWkgYSBwcsOzcHJpYSBvYnNlcnZhw6fDo28sIG8gcXVlIHBvZGUgcmVkdXppciBvIHJlc8OtZHVvIGNhc28gbyBvdXRsaWVyIHRlbmhhICdwdXhhZG8nIG8gYWp1c3RlIHBhcmEgcGVydG8gZGUgc2kuIE8gcmVzw61kdW8gZXh0ZXJubyAob3UgamFja2tuaWZlKSAkdF9pJCBjb3JyaWdlIGlzc28gYW8gdXNhciAkXFxoYXR7XFxzaWdtYX1feyhpKX0kLCB0b3JuYW5kby1vIHVtYSBtZWRpZGEgbWFpcyByb2J1c3RhIHBhcmEgZGV0ZWPDp8OjbyBkZSBhbm9tYWxpYXMgWzEuNV0uIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVswLjEsIDAuNSwgMC44NV0sIHk9LCBtb2RlPSdtYXJrZXJzJywgbmFtZT0nSW1wYWN0byBkZSBoX2knLCBtYXJrZXI9ZGljdChzaXplPTEyLCBjb2xvcj0nIzAwMDBGRicpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdFZmVpdG8gZGEgQWxhdmFuY2FnZW0gbmEgVmFyacOibmNpYSBkbyBSZXPDrWR1bycsIHhheGlzX3RpdGxlPSdBbGF2YW5jYWdlbSAoaF9pKScsIHlheGlzX3RpdGxlPSdWYXJpYWJpbGlkYWRlJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAibm1vZzR6YTZhcHFhLCBDYXAgNywgcC4gNzQtNzUifSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvIG9uZGUgYSB2YXJpw6JuY2lhIGRvICRpJC3DqXNpbW8gcmVzw61kdW8gYnJ1dG8gJFxcRGVsdGFfaSQgw6kgZGFkYSBwb3IgJFZhcltcXERlbHRhX2ldID0gXFxzaWdtYV4yKDEtaF9pKSQuIFNlIGVzdGl2ZXJtb3MgdXRpbGl6YW5kbyBvIHJlc8OtZHVvIHN0dWRlbnRpemFkbyBpbnRlcm5vICRyX2kgPSBcXERlbHRhX2kgLyAoXFxoYXR7XFxzaWdtYX0gXFxzcXJ0ezEtaF9pfSkkLCBxdWFsIMOpIG8gb2JqZXRpdm8gZnVuZGFtZW50YWwgZGUgdGFsIHTDqWNuaWNhIGRlIGVzY2Fsb25hbWVudG8gZW0gdW0gY29udGV4dG8gZGUgZGlhZ27Ds3N0aWNvIGRlIHJlZ3Jlc3PDo28/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBdW1lbnRhciBhIG1hZ25pdHVkZSBkb3MgcmVzw61kdW9zIHBhcmEgZmFjaWxpdGFyIGEgbGVpdHVyYSB2aXN1YWwgZW0gZ3LDoWZpY29zIGRlIGRpc3BlcnPDo28uIiwgIkIiOiAiR2FyYW50aXIgcXVlIHRvZG9zIG9zIHJlc8OtZHVvcyBzdHVkZW50aXphZG9zIHBvc3N1YW0gdmFyacOibmNpYSBhcHJveGltYWRhbWVudGUgY29uc3RhbnRlIChob21vY2VkYXN0aWNpZGFkZSB0ZcOzcmljYSksIHBlcm1pdGluZG8gYSBjb21wYXJhw6fDo28gZGlyZXRhIGRlIHN1YSBtYWduaXR1ZGUgaW5kZXBlbmRlbnRlbWVudGUgZGEgcG9zacOnw6NvIGRlICR4X2kkLiIsICJDIjogIlRyYW5zZm9ybWFyIGEgZGlzdHJpYnVpw6fDo28gZG9zIHJlc8OtZHVvcyBlbSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLCBpbmRlcGVuZGVudGVtZW50ZSBkYSBkaXN0cmlidWnDp8OjbyBvcmlnaW5hbCBkb3MgZXJyb3MuIiwgIkQiOiAiRWxpbWluYXIgYSBuZWNlc3NpZGFkZSBkZSB0ZXN0YXIgYSBzaWduaWZpY8OibmNpYSBkb3MgY29lZmljaWVudGVzICRcXGhhdHtcXGJldGF9X2okLiIsICJFIjogIkZvcsOnYXIgYSBtw6lkaWEgZG9zIHJlc8OtZHVvcyBzdHVkZW50aXphZG9zIGEgc2VyIGlndWFsIGFvIHZhbG9yIGRhIGluY2xpbmHDp8OjbyAkXFxoYXR7XFxiZXRhfV8xJC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk9ic2VydmUgYSBmw7NybXVsYSBkYSB2YXJpw6JuY2lhLiBDb21vICRWYXJbXFxEZWx0YV9pXSQgZGVwZW5kZSBkZSAkaF9pJCwgb3MgcmVzw61kdW9zIGJydXRvcyBuw6NvIHBvc3N1ZW0gdmFyacOibmNpYSBjb25zdGFudGUuIE8gZGVub21pbmFkb3IgJFxcc3FydHsxLWhfaX0kIGF0dWEgcGFyYSBub3JtYWxpemFyIGVzc2EgZGlzcGVyc8Ojby4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgYWx0ZXJuYXRpdmEgQiBlc3TDoSBjb3JyZXRhLiBFbSBtb2RlbG9zIGxpbmVhcmVzLCBvcyByZXPDrWR1b3MgYnJ1dG9zICRcXERlbHRhX2kgPSB5X2kgLSBcXGhhdHt5fV9pJCBwb3NzdWVtIHZhcmnDom5jaWFzIGRpZmVyZW50ZXMsIHBvaXMgJFZhcltcXERlbHRhX2ldID0gXFxzaWdtYV4yKDEtaF9pKSQuIENvbW8gJGhfaSQgdmFyaWEgY29uZm9ybWUgYSBvYnNlcnZhw6fDo28sIGEgdmFyaWFiaWxpZGFkZSBkb3MgcmVzw61kdW9zIGJydXRvcyDDqSBoZXRlcm9nw6puZWEuIEEgc3R1ZGVudGl6YcOnw6NvIGludGVybmEsIGFvIGRpdmlkaXIgcGVsbyBmYXRvciAkXFxzcXJ0ezEtaF9pfSQsIHJlbW92ZSBlc3NhIGRlcGVuZMOqbmNpYSBkYSBhbGF2YW5jYWdlbSwgY29sb2NhbmRvIHRvZG9zIG9zIHJlc8OtZHVvcyBlbSB1bWEgZXNjYWxhIGNvbXBhcsOhdmVsIChhZGltZW5zaW9uYWwpIGNvbSB2YXJpw6JuY2lhIHVuaXTDoXJpYSBzb2IgYXMgcHJlbWlzc2FzIGRvIG1vZGVsby4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIm5tb2c0emE2YXBxYSwgQ2FwIDcsIHAuIDczIn0sIHsiZW51bmNpYWRvIjogIlVtIGVuZ2VuaGVpcm8gZGUgcHJvY2Vzc29zIGluZHVzdHJpYWlzIGFqdXN0b3UgdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIHNpbXBsZXMgcGFyYSBwcmV2ZXIgYSBwcmVzc8OjbyBpbnRlcm5hIGRlIHVtIHNpc3RlbWEgZW0gZnVuw6fDo28gZGEgdGVtcGVyYXR1cmEgZGUgb3BlcmHDp8Ojby4gQXDDs3MgbyBhanVzdGUsIGVsZSBwbG90b3Ugb3MgcmVzw61kdW9zICgkZV9pJCkgY29udHJhIG9zIHZhbG9yZXMgYWp1c3RhZG9zICgkXFxoYXR7eX1faSQpLiBPIGdyw6FmaWNvIHJlc3VsdGFudGUgZXhpYml1IHVtIHBhZHLDo28gZGUgJ2Z1bmlsJyBjbGFybywgY29tIGEgZGlzcGVyc8OjbyBkb3MgcmVzw61kdW9zIGF1bWVudGFuZG8gw6AgbWVkaWRhIHF1ZSBvcyB2YWxvcmVzIGRlICRcXGhhdHt5fV9pJCBjcmVzY2VtLiBRdWFsIMOpIGEgY29uY2x1c8OjbyBlc3RhdMOtc3RpY2EgY29ycmV0YSBzb2JyZSBhIHZhbGlkYWRlIGRvIG1vZGVsbywgY29uc2lkZXJhbmRvIG9zIHByZXNzdXBvc3RvcyBkZSBHYXVzcy1NYXJrb3Y/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIG1vZGVsbyDDqSBwZXJmZWl0YW1lbnRlIGFkZXF1YWRvLCBwb2lzIG8gcGFkcsOjbyBkZSBmdW5pbCDDqSBlc3BlcmFkbyBlbSBxdWFscXVlciBhbW9zdHJhIGRlIGRhZG9zIHJlYWlzLiIsICJCIjogIk8gbW9kZWxvIGFwcmVzZW50YSBldmlkw6puY2lhcyBkZSBoZXRlcm9jZWRhc3RpY2lkYWRlLCB2aW9sYW5kbyBhIHByZW1pc3NhIGRlIHZhcmnDom5jaWEgY29uc3RhbnRlICgkVmFyW2VfaSB8IFxcaGF0e3l9X2ldID0gXFxzaWdtYV4yJCkuIiwgIkMiOiAiTyBncsOhZmljbyBpbmRpY2EgdW0gZXJybyBkZSBlc3BlY2lmaWNhw6fDo28gZnVuY2lvbmFsIGRvIHRpcG8gbsOjbyBsaW5lYXJpZGFkZSwgZGV2ZW5kby1zZSB1dGlsaXphciB1bSBtb2RlbG8gbG9nYXLDrXRtaWNvIHBhcmEgYWp1c3RhciBvIGludGVyY2VwdG8uIiwgIkQiOiAiTyBwYWRyw6NvIG9ic2VydmFkbyBuw6NvIHBvc3N1aSBzaWduaWZpY2FkbyBlc3RhdMOtc3RpY28sIGJhc3RhbmRvIHZlcmlmaWNhciBvIGNvZWZpY2llbnRlIGRlIGRldGVybWluYcOnw6NvICgkUl4yJCkgcGFyYSB2YWxpZGFyIGEgcHJlY2lzw6NvLiIsICJFIjogIkV4aXN0ZSB1bWEgY29ycmVsYcOnw6NvIHBvc2l0aXZhIHBlcmZlaXRhIGVudHJlIG9zIHJlc8OtZHVvcyBlIGFzIHZhcmnDoXZlaXMgZXhwbGljYXRpdmFzLCBpbnZhbGlkYW5kbyBvIHVzbyBkbyBtw6l0b2RvIGRlIG3DrW5pbW9zIHF1YWRyYWRvcyBvcmRpbsOhcmlvcyBwZXJtYW5lbnRlbWVudGUuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgZG8gc2lnbmlmaWNhZG8gZ2VvbcOpdHJpY28gZG9zIHJlc8OtZHVvcyBlIGRhIGRlZmluacOnw6NvIGRlIEdhdXNzLU1hcmtvdiBwYXJhIGEgdmFyacOibmNpYSBkbyBlcnJvIG5vIG1vZGVsbyAkXFxtYXRoYmZ7eX0gPSBcXG1hdGhiZntYfVxcYm9sZHN5bWJvbHtcXHRoZXRhfSArIFxcYm9sZHN5bWJvbHtcXERlbHRhfSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGFuw6FsaXNlIHZpc3VhbCBkZSByZXPDrWR1b3MgY29udHJhIHZhbG9yZXMgYWp1c3RhZG9zIMOpIGEgZmVycmFtZW50YSBkaWFnbsOzc3RpY2EgcHJpbcOhcmlhIHBhcmEgYSBoZXRlcm9jZWRhc3RpY2lkYWRlLiBBIGZvcm1hIGRlICdmdW5pbCcgaW5kaWNhIHF1ZSAkVmFyW2VfaSB8IFxcaGF0e3l9X2ldJCBuw6NvIMOpIGNvbnN0YW50ZSwgbWFzIGRlcGVuZGUgZG8gdmFsb3IgcHJldmlzdG8sIHZpb2xhbmRvIHVtIGRvcyBwcmVzc3Vwb3N0b3MgZnVuZGFtZW50YWlzIGRvIFRlb3JlbWEgZGUgR2F1c3MtTWFya292LiBRdWFuZG8gJFZhcltlX2kgfCBcXGhhdHt5fV9pXSBcXG5lcSBcXHNpZ21hXjIkLCBvcyBlc3RpbWFkb3JlcyBkZSBtw61uaW1vcyBxdWFkcmFkb3MgZGVpeGFtIGRlIHNlciBvcyBkZSB2YXJpw6JuY2lhIG3DrW5pbWEsIGV4aWdpbmRvIGNvcnJlw6fDtWVzIG91IHRyYW5zZm9ybWHDp8O1ZXMuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PW5wLmxpbnNwYWNlKDEwLCAxMDAsIDUwKSwgeT1ucC5yYW5kb20ubm9ybWFsKDAsIG5wLmxpbnNwYWNlKDEsIDEwLCA1MCkpLCBtb2RlPSdtYXJrZXJzJywgbmFtZT0nUmVzw61kdW9zJywgbWFya2VyPWRpY3QoY29sb3I9JyMwMDAwRkYnKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nR3LDoWZpY28gZGUgUmVzw61kdW9zIChFdmlkw6puY2lhIGRlIEhldGVyb2NlZGFzdGljaWRhZGUpJywgeGF4aXNfdGl0bGU9J1ZhbG9yZXMgQWp1c3RhZG9zICgkXFxoYXR7eX1faSQpJywgeWF4aXNfdGl0bGU9J1Jlc8OtZHVvcyAoJGVfaSQpJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpXG5maWcuYWRkX2hsaW5lKHk9MCwgbGluZV9kYXNoPSdkYXNoJywgbGluZV9jb2xvcj0nI0ZGMDAwMCcpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQW8gYW5hbGlzYXIgdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gcGFyYSBhIGRlbWFuZGEgZGUgZW5lcmdpYSBkZSB1bWEgY2lkYWRlLCB2b2PDqiBvYnNlcnZhIHF1ZSBvIGdyw6FmaWNvIGRvcyByZXPDrWR1b3MgKCRlX2kkKSB2ZXJzdXMgb3MgdmFsb3JlcyBwcmV2aXN0b3MgKCRcXGhhdHt5fV9pJCkgZXhpYmUgdW1hIGN1cnZhdHVyYSBwYXJhYsOzbGljYSBhY2VudHVhZGEuIE8gcXVlIGVzdGUgY29tcG9ydGFtZW50byB2aXN1YWwgc3VnZXJlIHNvYnJlIGEgYWRlcXVhw6fDo28gZG8gbW9kZWxvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyBtb2RlbG8gZXN0w6Egc29mcmVuZG8gZGUgaGV0ZXJvY2VkYXN0aWNpZGFkZSBzZXZlcmEsIGluZGljYW5kbyBxdWUgYSB2YXJpw6JuY2lhIGRvIGVycm8gYXVtZW50YSBjb20gYSBtw6lkaWEuIiwgIkIiOiAiQSBjdXJ2YXR1cmEgaW5kaWNhIHF1ZSBvIG1vZGVsbyBsaW5lYXIgw6kgYWRlcXVhZG8sIG1hcyBvcyBkYWRvcyBwb3NzdWVtIG11aXRvcyB2YWxvcmVzIGF0w61waWNvcyAob3V0bGllcnMpLiIsICJDIjogIk8gbW9kZWxvIGFwcmVzZW50YSBzaW5haXMgZGUgbsOjbyBsaW5lYXJpZGFkZSBzaXN0ZW3DoXRpY2EsIHN1Z2VyaW5kbyBxdWUgYSByZWxhw6fDo28gcmVhbCBlbnRyZSAkWCQgZSAkWSQgcG9kZSBleGlnaXIgdGVybW9zIHBvbGlub21pYWlzIG91IHRyYW5zZm9ybWHDp8O1ZXMgZnVuY2lvbmFpcy4iLCAiRCI6ICJBIGRpc3RyaWJ1acOnw6NvIGRvcyByZXPDrWR1b3Mgw6kgcGVyZmVpdGFtZW50ZSBub3JtYWwsIG8gcXVlIGdhcmFudGUgcXVlIG8gbW9kZWxvIHRlbSBhbHRhIGNhcGFjaWRhZGUgcHJlZGl0aXZhLiIsICJFIjogIk8gZ3LDoWZpY28gZGVtb25zdHJhIHF1ZSBvIGludGVyY2VwdG8gJFxcaGF0e1xcYmV0YX1fMCQgZXN0w6EgaW5jb3JyZXRhbWVudGUgY2FsY3VsYWRvIGUgZGV2ZSBzZXIgcmVtb3ZpZG8gZG8gbW9kZWxvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiUmVmbGl0YSBzb2JyZSBvIHF1ZSBzaWduaWZpY2EgYSBleHBlY3RhdGl2YSBjb25kaWNpb25hbCBkb3MgcmVzw61kdW9zICgkRVtlX2kgfCBcXGhhdHt5fV9pXSA9IDAkKSBlbSByZWxhw6fDo28gYSBwYWRyw7VlcyBnZW9tw6l0cmljb3Mgc2lzdGVtw6F0aWNvcy4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgcHJlbWlzc2EgYsOhc2ljYSBkbyBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgw6kgcXVlIGEgcmVsYcOnw6NvIHNpc3RlbcOhdGljYSBmb2kgY2FwdHVyYWRhLiBRdWFuZG8gb2JzZXJ2YW1vcyB1bWEgY3VydmF0dXJhIHNpc3RlbcOhdGljYSAocGFkcsOjbyBkZSBhcmNvKSBubyBncsOhZmljbyBkZSByZXPDrWR1b3MsIGlzc28gaW1wbGljYSBxdWUgJEVbZV9pIHwgXFxoYXR7eX1faV0gXFxuZXEgMCQgZW0gZGlmZXJlbnRlcyByZWdpw7VlcyBkYSB2YXJpw6F2ZWwgcHJlZGl0b3JhLCBzaW5hbGl6YW5kbyBxdWUgYSBmb3JtYSBmdW5jaW9uYWwgKGxpbmVhcikgbsOjbyDDqSBjYXBheiBkZSBkZXNjcmV2ZXIgYWRlcXVhZGFtZW50ZSBhIGN1cnZhdHVyYSBwcmVzZW50ZSBuYSByZWxhw6fDo28gcmVhbCBlbnRyZSBhcyB2YXJpw6F2ZWlzLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTUsIDUsIDEwMClcbnkgPSAtMC41ICogKHgqKjIpICsgbnAucmFuZG9tLm5vcm1hbCgwLCAxLCAxMDApXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG1vZGU9J21hcmtlcnMnLCBuYW1lPSdSZXPDrWR1b3MnLCBtYXJrZXI9ZGljdChjb2xvcj0nIzAwMDBGRicpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdHcsOhZmljbyBkZSBSZXPDrWR1b3MgKEV2aWTDqm5jaWEgZGUgTsOjbyBMaW5lYXJpZGFkZSknLCB4YXhpc190aXRsZT0nVmFsb3JlcyBBanVzdGFkb3MgKCRcXGhhdHt5fV9pJCknLCB5YXhpc190aXRsZT0nUmVzw61kdW9zICgkZV9pJCknLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJylcbmZpZy5hZGRfaGxpbmUoeT0wLCBsaW5lX2Rhc2g9J2Rhc2gnLCBsaW5lX2NvbG9yPScjRkYwMDAwJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBlbmdlbmhlaXJvIGRlIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBlbSB1bWEgcGxhbnRhIGRlIG1hbnVmYXR1cmEgYXV0b21vdGl2YSBhanVzdGEgdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIHBhcmEgcHJldmVyIG8gZGVzZ2FzdGUgZGUgcm9sYW1lbnRvcyAoZW0gbWljcsO0bWV0cm9zKSBjb20gYmFzZSBuYSB2ZWxvY2lkYWRlIGRlIG9wZXJhw6fDo28gKGVtIFJQTSkuIEFww7NzIGFqdXN0YXIgbyBtb2RlbG8gJFxcbWF0aGJme3l9ID0gXFxtYXRoYmZ7WH1cXGJvbGRzeW1ib2x7XFx0aGV0YX0gKyBcXGJvbGRzeW1ib2x7XFxEZWx0YX0kLCBlbGUgcmVhbGl6YSB1bWEgYW7DoWxpc2UgZGlhZ27Ds3N0aWNhIGRvcyByZXPDrWR1b3MgJFxcbWF0aGJme2V9JCB1dGlsaXphbmRvIG8gZ3LDoWZpY28gcXVhbnRpbC1xdWFudGlsIG5vcm1hbCAoUS1RIFBsb3QpLiBBbyBvYnNlcnZhciBvIGdyw6FmaWNvLCBlbGUgbm90YSBxdWUgb3MgcG9udG9zIHNlIGFmYXN0YW0gc2lzdGVtYXRpY2FtZW50ZSBkYSBsaW5oYSBkaWFnb25hbCBlbSBhbWJhcyBhcyBleHRyZW1pZGFkZXMsIGZvcm1hbmRvIHVtYSBjdXJ2YXR1cmEgcXVlIHN1Z2VyZSBxdWUgb3MgcmVzw61kdW9zIHBvc3N1ZW0gY2F1ZGFzIG1haXMgcGVzYWRhcyBkbyBxdWUgYXMgcHJldmlzdGFzIHBvciB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIHRlw7NyaWNhLiBDb20gYmFzZSBuYSB0ZW9yaWEgZGEgaW5mZXLDqm5jaWEgc29icmUgYSBub3JtYWxpZGFkZSBkb3MgZXJyb3MsIHF1YWwgw6kgYSBpbXBsaWNhw6fDo28gcHLDoXRpY2EgbWFpcyBkaXJldGEgZGVzc2UgY29tcG9ydGFtZW50byBvYnNlcnZhZG8gcGFyYSBvIHByb2Nlc3NvIGRlIHRvbWFkYSBkZSBkZWNpc8Ojbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgdmlvbGHDp8OjbyBkYSBub3JtYWxpZGFkZSBpbmRpY2EgcXVlIG9zIGVzdGltYWRvcmVzIGRlIG3DrW5pbW9zIHF1YWRyYWRvcyBwZXJkZXJhbSBhIHByb3ByaWVkYWRlIGRlIHNlcmVtIG9zIG1lbGhvcmVzIGVzdGltYWRvcmVzIGxpbmVhcmVzIG7Do28gdmljaWFkb3MgKEJMVUUpLiIsICJCIjogIkEgaW5mZXLDqm5jaWEgZXN0YXTDrXN0aWNhIGJhc2VhZGEgbmFzIGRpc3RyaWJ1acOnw7VlcyAkdCQgZGUgU3R1ZGVudCBlICRGJCwgY29tbyBhIGNvbnN0cnXDp8OjbyBkZSBpbnRlcnZhbG9zIGRlIGNvbmZpYW7Dp2EgZSB0ZXN0ZXMgZGUgc2lnbmlmaWPDom5jaWEgZG9zIGNvZWZpY2llbnRlcywgdG9ybmEtc2UgY29tcHJvbWV0aWRhLCBwb2lzIGFzIGVzdGF0w61zdGljYXMgY2FsY3VsYWRhcyBuw6NvIHNlZ3VlbSBhcyBkaXN0cmlidWnDp8O1ZXMgdGXDs3JpY2FzIGVzcGVyYWRhcy4iLCAiQyI6ICJPIG1vZGVsbyBlc3TDoSBzb2ZyZW5kbyBkZSBoZXRlcm9jZWRhc3RpY2lkYWRlIHNldmVyYSwgbyBxdWUgaW52YWxpZGEgY29tcGxldGFtZW50ZSBxdWFscXVlciB0ZW50YXRpdmEgZGUgcHJlZGnDp8Ojbywgc2VuZG8gbmVjZXNzw6FyaWEgYSBzdWJzdGl0dWnDp8OjbyBpbWVkaWF0YSBkbyBtb2RlbG8gcG9yIHVtIG1vZGVsbyBuw6NvIGxpbmVhci4iLCAiRCI6ICJPIGdyw6FmaWNvIFEtUSBQbG90IGluZGljYSBxdWUgYSBzb21hIGRlIHF1YWRyYWRvcyBkb3MgcmVzw61kdW9zICgkU1FSZXMkKSBuw6NvIMOpIG1haXMgdW1hIGVzdGltYXRpdmEgbsOjbyB2aWNpYWRhIGRhIHZhcmnDom5jaWEgcG9wdWxhY2lvbmFsICRcXHNpZ21hXjIkLCBpbnZhbGlkYW5kbyBvIFRlb3JlbWEgZGUgQ29jaHJhbiBwYXJhIHF1YWxxdWVyIHRhbWFuaG8gYW1vc3RyYWwuIiwgIkUiOiAiQSBhc3NpbWV0cmlhIG9ic2VydmFkYSBuYXMgY2F1ZGFzIGltcGxpY2EgbmVjZXNzYXJpYW1lbnRlIHF1ZSBvIHZldG9yIGRlIHJlc8OtZHVvcyAkXFxtYXRoYmZ7ZX0kIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyAkdCQgZGUgU3R1ZGVudCBjb20gcG91Y29zIGdyYXVzIGRlIGxpYmVyZGFkZSwgcGVybWl0aW5kbyBvIHVzbyBkaXJldG8gZGUgdGFiZWxhcyBjb3JyaWdpZGFzLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBvIFRlb3JlbWEgZGUgQ29jaHJhbiBlIGEgdmFsaWRhZGUgZG9zIHRlc3RlcyBlc3RhdMOtc3RpY29zIGNsw6Fzc2ljb3MgZW0gcmVncmVzc8OjbyAoY29tbyBvcyB0ZXN0ZXMgcGFyYSAkXFxiZXRhX2kkKSBkZXBlbmRlbSBjcml0aWNhbWVudGUgZGEgc3Vwb3Npw6fDo28gZGUgbm9ybWFsaWRhZGUgbXVsdGl2YXJpYWRhIGRvcyBlcnJvcyAkXFxib2xkc3ltYm9se1xcRGVsdGF9IFxcc2ltIE4oXFxtYXRoYmZ7MH0sIFxcc2lnbWFeMiBcXG1hdGhiZntJfSkkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBzdXBvc2nDp8OjbyBkZSBub3JtYWxpZGFkZSBkb3MgZXJyb3Mgw6kgZnVuZGFtZW50YWwgcGFyYSBxdWUgYXMgZXN0YXTDrXN0aWNhcyBkZSB0ZXN0ZSAoJHRfe1xcdGV4dHtjYWxjfX0kIGUgJEZfe1xcdGV4dHtjYWxjfX0kKSBzaWdhbSBhcyBkaXN0cmlidWnDp8O1ZXMgdGXDs3JpY2FzICR0JCBkZSBTdHVkZW50IGUgJEYkIGRlIFNuZWRlY29yLiBRdWFuZG8gbyBRLVEgUGxvdCByZXZlbGEgY2F1ZGFzIHBlc2FkYXMgKGN1cnRvc2UgZXhjZXNzaXZhKSwgYSBkaXN0cmlidWnDp8OjbyBkb3MgZXJyb3Mgc2UgZGVzdmlhIGRhIEdhdXNzaWFuYS4gQ29uc2VxdWVudGVtZW50ZSwgYXMgcHJvYmFiaWxpZGFkZXMgY2FsY3VsYWRhcyBwYXJhIHAtdmFsb3JlcyBlIG9zIGxpbWl0ZXMgZGUgY29uZmlhbsOnYSB0b3JuYW0tc2UgaW1wcmVjaXNvcywgcG9pcyBhIGRpc3RyaWJ1acOnw6NvIGFtb3N0cmFsIGRhIGVzdGF0w61zdGljYSBkZWl4YSBkZSBjb3JyZXNwb25kZXIgw6AgZGlzdHJpYnVpw6fDo28gdGXDs3JpY2Egc29iIGEgaGlww7N0ZXNlIG51bGEuIEEgb3DDp8OjbyBBIGVzdMOhIGluY29ycmV0YSBwb3JxdWUsIHBlbG8gVGVvcmVtYSBkZSBHYXVzcy1NYXJrb3YsIG9zIGVzdGltYWRvcmVzIGRlIG3DrW5pbW9zIHF1YWRyYWRvcyBwZXJtYW5lY2VtIEJMVUUgbWVzbW8gc2VtIG5vcm1hbGlkYWRlOyBhIG5vcm1hbGlkYWRlIMOpIGV4aWdpZGEgcGFyYSBhIGluZmVyw6puY2lhICh0ZXN0ZXMpLCBuw6NvIHBhcmEgYSBwcm9wcmllZGFkZSBkZSBzZXIgbyBtZWxob3IgZXN0aW1hZG9yIGxpbmVhci4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9Wy0yLCAyXSwgeT1bLTIsIDJdLCBtb2RlPSdsaW5lcycsIGxpbmU9ZGljdChjb2xvcj0nIzAwMDBGRicsIGRhc2g9J2Rhc2gnKSwgbmFtZT0nVGXDs3JpY2EnKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PSwgeT0sIG1vZGU9J21hcmtlcnMnLCBtYXJrZXI9ZGljdChjb2xvcj0nIzFFMjkzQicpLCBuYW1lPSdSZXPDrWR1b3MnKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5RLVEgUGxvdCBjb20gQ2F1ZGFzIFBlc2FkYXM8L2I+JywgeGF4aXNfdGl0bGU9J1F1YW50aXMgVGXDs3JpY29zJywgeWF4aXNfdGl0bGU9J1F1YW50aXMgQW1vc3RyYWlzICgkZV97KGkpfSQpJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScsIGhlaWdodD00MjApIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtIGVzdHVkbyBiaW9sw7NnaWNvIG9uZGUgc2UgYXZhbGlhIGEgZWZpY8OhY2lhIGRlIHF1YXRybyB0aXBvcyBkZSBmZXJ0aWxpemFudGVzIG5vIGNyZXNjaW1lbnRvIGRlIHBsYW50YXMuIEFvIHJlYWxpemFyIHVtYSBBTk9WQSwgbyBwZXNxdWlzYWRvciBhc3N1bWUgcXVlIG9zIGVycm9zICRcXGJvbGRzeW1ib2x7XFxEZWx0YX0kIHNlZ3VlbSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsICROKFxcbWF0aGJmezB9LCBcXHNpZ21hXjIgXFxtYXRoYmZ7SX0pJC4gRGUgYWNvcmRvIGNvbSBvIFRlb3JlbWEgZGUgQ29jaHJhbiBlIGFzIHByb3ByaWVkYWRlcyBkYXMgZm9ybWFzIHF1YWRyw6F0aWNhcyBzb2IgYSBwcmVtaXNzYSBkZSBub3JtYWxpZGFkZSwgcXVhbCDDqSBhIGNvbmRpw6fDo28gbmVjZXNzw6FyaWEgcXVlIGdhcmFudGUgcXVlICRcXGZyYWN7U1FUcmF0Ln17XFxzaWdtYV4yfSQgZSAkXFxmcmFje1NRUmVzLn17XFxzaWdtYV4yfSQgc2VqYW0gaW5kZXBlbmRlbnRlcyBlIHNpZ2FtIGRpc3RyaWJ1acOnw7VlcyBRdWktUXVhZHJhZG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPcyBlcnJvcyBkZXZlbSBzZXIgZXN0cml0YW1lbnRlIGNvbnN0YW50ZXMgZSBhIG3DqWRpYSBkb3MgcmVzw61kdW9zIGRldmUgc2VyIG9icmlnYXRvcmlhbWVudGUgaWd1YWwgYSB1bS4iLCAiQiI6ICJBIG1hdHJpeiBkZSBwcm9qZcOnw6NvICRQJCBlIGEgbWF0cml6ICQoSS1QKSQgZGV2ZW0gc2VyIG9ydG9nb25haXMgZW50cmUgc2ksIG91IHNlamEsICRQKEktUCkgPSBcXGVtcHR5c2V0JCwgZ2FyYW50aW5kbyBhIGRlY29tcG9zacOnw6NvIGRhIHNvbWEgZGUgcXVhZHJhZG9zIGVtIGNvbXBvbmVudGVzIGluZGVwZW5kZW50ZXMuIiwgIkMiOiAiTyBuw7ptZXJvIGRlIG9ic2VydmHDp8O1ZXMgJG4kIGRldmUgc2VyIGluZmluaXRvIHBhcmEgc2F0aXNmYXplciBvIFRlb3JlbWEgZG8gTGltaXRlIENlbnRyYWwsIHRvcm5hbmRvIGEgc3Vwb3Npw6fDo28gZGUgbm9ybWFsaWRhZGUgaXJyZWxldmFudGUuIiwgIkQiOiAiTyB2YWxvciBlc3BlcmFkbyBkb3MgZXJyb3MgJFxcYm9sZHN5bWJvbHtcXERlbHRhfSQgZGV2ZSBzZXIgaWd1YWwgYSAkXFxzaWdtYV4yIEkkLCBnYXJhbnRpbmRvIHF1ZSBhIG1hdHJpeiBkZSB2YXJpw6JuY2lhLWNvdmFyacOibmNpYSBzZWphIGlkZW50aWRhZGUuIiwgIkUiOiAiTyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkIGRldmUgc2VyIGlndWFsIGEgemVybyBwYXJhIGdhcmFudGlyIHF1ZSBuw6NvIGhhamEgZXJyb3MgbmEgcmVqZWnDp8OjbyBkYSBoaXDDs3Rlc2UgbnVsYS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkFuYWxpc2UgYSBlc3RydXR1cmEgYWxnw6licmljYSBkYSBkZWNvbXBvc2nDp8OjbyBkYSBzb21hIGRlIHF1YWRyYWRvczogJHkneSA9IHknUHkgKyB5JyhJLVApeSQuIE8gVGVvcmVtYSBkZSBDb2NocmFuIGJhc2VpYS1zZSBuYSBwcm9wcmllZGFkZSBkZSBpZGVtcG90w6puY2lhIGUgb3J0b2dvbmFsaWRhZGUgZGVzc2FzIGZvcm1hcyBxdWFkcsOhdGljYXMuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJPIFRlb3JlbWEgZGUgQ29jaHJhbiBlc3RhYmVsZWNlIHF1ZSwgc2UgJFxcbWF0aGJme3l9IFxcc2ltIE4oXFxtYXRoYmZ7WH1cXGJvbGRzeW1ib2x7XFx0aGV0YX0sIFxcc2lnbWFeMiBcXG1hdGhiZntJfSkkLCBlbnTDo28gYSBkZWNvbXBvc2nDp8OjbyBkYSBzb21hIGRlIHF1YWRyYWRvcyBlbSBmb3JtYXMgcXVhZHLDoXRpY2FzIGluZGVwZW5kZW50ZXMgZGVwZW5kZSBkYSBvcnRvZ29uYWxpZGFkZSBlIGlkZW1wb3TDqm5jaWEgZGFzIG1hdHJpemVzIGFzc29jaWFkYXMuIEVzcGVjaWZpY2FtZW50ZSwgJFAgPSBcXG1hdGhiZntYfShcXG1hdGhiZntYfSdcXG1hdGhiZntYfSleey19XFxtYXRoYmZ7WH0nJCDDqSB1bWEgbWF0cml6IGlkZW1wb3RlbnRlIGRlIHBvc3RvICRyKFgpJCwgZSAkKEktUCkkIMOpIHVtYSBtYXRyaXogaWRlbXBvdGVudGUgZGUgcG9zdG8gJG4tcihYKSQuIEEgY29uZGnDp8OjbyAkUChJLVApID0gXFxlbXB0eXNldCQgZ2FyYW50ZSBxdWUgYXMgZm9ybWFzIHF1YWRyw6F0aWNhcyBjb3JyZXNwb25kZW50ZXMgKCRTUVRyYXQkIGUgJFNRUmVzJCkgc2VqYW0gaW5kZXBlbmRlbnRlcyBlIHBvc3N1YW0gZGlzdHJpYnVpw6fDtWVzICRcXGNoaV4yJCBjZW50cmFsIGUgbsOjby1jZW50cmFsIChkZXBlbmRlbmRvIGRhIGhpcMOzdGVzZSksIHBlcm1pdGluZG8gbyB1c28gZGEgZGlzdHJpYnVpw6fDo28gJEYkIHBhcmEgbyB0ZXN0ZSBkZSBoaXDDs3Rlc2VzLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTHVuYSwgSi4gRy4gJiBFc3RldmVzLCBELiBNLiwgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzLCBDYXAgMywgcC4gNzUifV0sICJxdWVzdG9lc19kaXNjdXJzaXZhcyI6IFt7ImVudW5jaWFkbyI6ICJQcm92ZSBmb3JtYWxtZW50ZSwgdXRpbGl6YW5kbyBhcyBwcm9wcmllZGFkZXMgZGEgbWF0cml6IGRlIHByb2plw6fDo28gJFAgPSBYKFheVFgpXnstMX1YXlQkLCBxdWUgbyB2ZXRvciBkZSB2YWxvcmVzIGFqdXN0YWRvcyAkXFxoYXR7eX0kIGUgbyB2ZXRvciBkZSByZXPDrWR1b3MgJGUkIHPDo28gb3J0b2dvbmFpcy4gRXhwbGljaXRlIGNhZGEgcGFzc28gZGEgw6FsZ2VicmEgbWF0cmljaWFsLiIsICJkaWNhIjogIlV0aWxpemUgYSBwcm9wcmllZGFkZSAkUF4yID0gUCQgZSAkKEFCKV5UID0gQl5UIEFeVCQuIExlbWJyZS1zZSBxdWUgJGUgPSAoSS1QKXkkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJEZWZpbmltb3MgJFxcaGF0e3l9ID0gUHkkIGUgJGUgPSAoSS1QKXkkLiIsICJPIHByb2R1dG8gaW50ZXJubyDDqSBkYWRvIHBvciAkXFxoYXR7eX1eVCBlID0gKFB5KV5UIChJLVApeSQuIiwgIkFwbGljYW5kbyBhIHRyYW5zcG9zdGE6ICRcXGhhdHt5fV5UIGUgPSB5XlQgUF5UIChJLVApeSQuIiwgIkNvbW8gJFAkIMOpIHNpbcOpdHJpY2EgKCRQXlQgPSBQJCk6ICRcXGhhdHt5fV5UIGUgPSB5XlQgUCAoSS1QKXkkLiIsICJEaXN0cmlidWluZG8gbyBwcm9kdXRvOiAkXFxoYXR7eX1eVCBlID0geV5UIChQIC0gUF4yKXkkLiIsICJDb21vICRQJCDDqSBpZGVtcG90ZW50ZSAoJFBeMiA9IFAkKTogJFxcaGF0e3l9XlQgZSA9IHleVCAoUCAtIFApeSA9IHleVCAoMCkgeSA9IDAkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4wfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtIG1vZGVsbyBsaW5lYXIgb25kZSAkbj0yMCQgZSAkcD0zJC4gU2FiZW5kbyBxdWUgYSB2YXJpw6JuY2lhIGRvIGVycm8gYWxlYXTDs3JpbyDDqSAkXFxzaWdtYV4yID0gNCQsIGNhbGN1bGUgbyB2YWxvciBlc3BlcmFkbyBkYSBzb21hIGRvcyBxdWFkcmFkb3MgZG9zIHJlc8OtZHVvcywgZGVmaW5pZGEgY29tbyAkRVtTUVJlc10gPSBFW2VeVCBlXSQuIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSAkZV5UIGUgPSB5XlQgKEktUCleVCAoSS1QKSB5ID0geV5UIChJLVApIHkkLiBVc2UgYSBwcm9wcmllZGFkZSBkYSBmb3JtYSBxdWFkcsOhdGljYSAkRVt4XlQgQSB4XSA9IFRyKEEgXFxTaWdtYSkgKyBcXG11XlQgQSBcXG11JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSBzb21hIGRvcyBxdWFkcmFkb3MgZG9zIHJlc8OtZHVvcyDDqSAkU1FSZXMgPSBlXlQgZSA9IHleVCAoSS1QKV4yIHkgPSB5XlQgKEktUCkgeSQuIiwgIk8gdmFsb3IgZXNwZXJhZG8gw6kgJEVbeV5UIChJLVApIHldID0gVHIoKEktUClWYXJbeV0pICsgKEVbeV0pXlQgKEktUCkgKEVbeV0pJC4iLCAiQ29tbyAkRVt5XSA9IFhcXHRoZXRhJCBlICQoSS1QKVggPSAoWCAtIFgoWF5UWCleey0xfVheVFgpID0gWCAtIFggPSAwJCwgbyBzZWd1bmRvIHRlcm1vIMOpIHplcm8uIiwgIlBvcnRhbnRvLCAkRVtTUVJlc10gPSBUcigoSS1QKVxcc2lnbWFeMiBJKSA9IFxcc2lnbWFeMiBUcihJLVApID0gXFxzaWdtYV4yIChuLXApJC4iLCAiU3Vic3RpdHVpbmRvOiAkRVtTUVJlc10gPSA0IFxcdGltZXMgKDIwIC0gMykgPSA0IFxcdGltZXMgMTcgPSA2OCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiA2OC4wfSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIGRvIHBvbnRvIGRlIHZpc3RhIGRhIHRlb3JpYSBkZSByZWdyZXNzw6NvLCBwb3IgcXVlIGEgbWF0cml6IGRlIGNvdmFyacOibmNpYSBkb3MgcmVzw61kdW9zICRWYXJbZV0gPSBcXHNpZ21hXjIgKEkgLSBQKSQgbsOjbyDDqSB1bWEgbWF0cml6IGRpYWdvbmFsLCBtZXNtbyBxdWFuZG8gYXNzdW1pbW9zIHF1ZSBvcyBlcnJvcyBvcmlnaW5haXMgJFxcRGVsdGEkIHBvc3N1ZW0gdmFyacOibmNpYSBjb25zdGFudGUgJFxcc2lnbWFeMiBJJC4gTyBxdWUgaXNzbyBpbXBsaWNhIHNvYnJlIGEgaW5kZXBlbmTDqm5jaWEgZG9zIHJlc8OtZHVvcz8iLCAiZGljYSI6ICJPYnNlcnZlIGEgZXN0cnV0dXJhIGRlICRQJC4gUGVuc2Ugc2UgYSBwcm9qZcOnw6NvIGludHJvZHV6IGRlcGVuZMOqbmNpYSBlbnRyZSBhcyBvYnNlcnZhw6fDtWVzIGFww7NzIG8gYWp1c3RlLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBIG1hdHJpeiBkZSBjb3ZhcmnDom5jaWEgZG9zIGVycm9zIG9yaWdpbmFpcyDDqSAkVmFyW1xcRGVsdGFdID0gXFxzaWdtYV4yIEkkLCBvIHF1ZSBpbXBsaWNhIGluZGVwZW5kw6puY2lhIGUgdmFyacOibmNpYSBjb25zdGFudGUuIiwgIkFww7NzIG8gYWp1c3RlIGRvIG1vZGVsbywgb3MgcmVzw61kdW9zIHPDo28gY2FsY3VsYWRvcyBjb21vICRlID0gKEktUClcXERlbHRhJC4iLCAiQSBjb3ZhcmnDom5jaWEgZG9zIHJlc8OtZHVvcyDDqSAkVmFyW2VdID0gKEktUClWYXJbXFxEZWx0YV0oSS1QKV5UID0gXFxzaWdtYV4yIChJLVApKEktUCleVCA9IFxcc2lnbWFeMiAoSS1QKSQuIiwgIkNvbW8gJFAkIGdlcmFsbWVudGUgbsOjbyDDqSBhIG1hdHJpeiBudWxhLCBvcyBlbGVtZW50b3MgZm9yYSBkYSBkaWFnb25hbCBkZSAkKEktUCkkIG7Do28gc8OjbyB6ZXJvLiIsICJDb25jbHVzw6NvOiBPcyByZXPDrWR1b3Mgc8OjbyBsaW5lYXJtZW50ZSBkZXBlbmRlbnRlcywgcG9pcyBhIHJlc3RyacOnw6NvIGRlIGVzdGltYcOnw6NvIGRvcyAkcCQgcGFyw6JtZXRyb3MgaW1ww7VlIHVtYSBlc3RydXR1cmEgZGUgZGVwZW5kw6puY2lhIHNvYnJlIG9zICRuJCBlcnJvcyBvYnNlcnZhZG9zLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtYSBhbsOhbGlzZSBkZSByZWdyZXNzw6NvLCBmb2kgdmVyaWZpY2FkbyBxdWUgcGFyYSB1bWEgb2JzZXJ2YcOnw6NvICRpJCwgbyByZXPDrWR1byBicnV0byDDqSAkXFxEZWx0YV9pID0gMi41JCwgbyBkZXN2aW8gcGFkcsOjbyBnbG9iYWwgZXN0aW1hZG8gw6kgJFxcaGF0e1xcc2lnbWF9ID0gMS4yJCBlIGEgYWxhdmFuY2FnZW0gw6kgJGhfaSA9IDAuNjQkLiBDYWxjdWxlIG8gcmVzw61kdW8gc3R1ZGVudGl6YWRvIGludGVybm8gJHJfaSQgZGVzdGEgb2JzZXJ2YcOnw6NvLiBTZSBvIG7Dum1lcm8gZGUgb2JzZXJ2YcOnw7VlcyBmb3IgJG49MjAkIGUgbyBuw7ptZXJvIGRlIHBhcsOibWV0cm9zICRwPTMkLCB1dGlsaXplIGEgZsOzcm11bGEgZGUgY29udmVyc8OjbyBwYXJhIGVuY29udHJhciBvIHJlc8OtZHVvIHN0dWRlbnRpemFkbyBleHRlcm5vICR0X2kkLiIsICJkaWNhIjogIkxlbWJyZS1zZTogJHJfaSA9IFxcRGVsdGFfaSAvIChcXGhhdHtcXHNpZ21hfSBcXHNxcnR7MSAtIGhfaX0pJCBlICR0X2kgPSByX2kgXFxzcXJ0eyhuIC0gcCAtIDEpIC8gKG4gLSBwIC0gcl9pXjIpfSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IENhbGN1bGFyIG8gZGVub21pbmFkb3IgZGEgc3R1ZGVudGl6YcOnw6NvIGludGVybmE6ICRcXHNxcnR7MSAtIGhfaX0gPSBcXHNxcnR7MSAtIDAuNjR9ID0gXFxzcXJ0ezAuMzZ9ID0gMC42JC4iLCAiUGFzc28gMjogQ2FsY3VsYXIgbyByZXPDrWR1byBzdHVkZW50aXphZG8gaW50ZXJubzogJHJfaSA9IDIuNSAvICgxLjIgXFx0aW1lcyAwLjYpID0gMi41IC8gMC43MiBcXGFwcHJveCAzLjQ3MiQuIiwgIlBhc3NvIDM6IENhbGN1bGFyIG8gdGVybW8gZGEgcmFpeiBxdWFkcmFkYSBwYXJhIG8gcmVzw61kdW8gZXh0ZXJubzogJFxcc3FydHsoMjAgLSAzIC0gMSkgLyAoMjAgLSAzIC0gKDMuNDcyKV4yKX0gPSBcXHNxcnR7MTYgLyAoMTcgLSAxMi4wNTUpfSA9IFxcc3FydHsxNiAvIDQuOTQ1fSBcXGFwcHJveCBcXHNxcnR7My4yMzV9IFxcYXBwcm94IDEuNzk4JC4iLCAiUGFzc28gNDogQ2FsY3VsYXIgbyByZXPDrWR1byBzdHVkZW50aXphZG8gZXh0ZXJubzogJHRfaSA9IDMuNDcyIFxcdGltZXMgMS43OTggXFxhcHByb3ggNi4yNDMkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogNi4yNH0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCBzb2IgYSDDs3RpY2EgZGEgbWF0cml6IGNoYXDDqXUgJEggPSBYKFheVFgpXnstMX1YXlQkLCBwb3IgcXVlIG9zIGVycm9zIGJydXRvcyAkXFxEZWx0YV9pJCBuw6NvIHBvc3N1ZW0gdmFyacOibmNpYSBjb25zdGFudGUgZW0gdW1hIHJlZ3Jlc3PDo28gbGluZWFyIHNpbXBsZXMsIG1lc21vIHF1YW5kbyBhc3N1bWltb3MgcXVlIG9zIGVycm9zIGRvIG1vZGVsbyBvcmlnaW5hbCAkXFxlcHNpbG9uX2kkIHPDo28gaS5pLmQuICROKDAsIFxcc2lnbWFeMikkLiIsICJkaWNhIjogIkNvbnNpZGVyZSBxdWUgJFxcaGF0e3l9ID0gSHkkIGUgcXVlIG9zIHJlc8OtZHVvcyBzw6NvIGRhZG9zIHBvciAkXFxEZWx0YSA9IChJIC0gSCl5JC4gQ2FsY3VsZSBhIHZhcmnDom5jaWEgZGUgJFxcRGVsdGEkIHV0aWxpemFuZG8gcHJvcHJpZWRhZGVzIGRlIMOhbGdlYnJhIG1hdHJpY2lhbC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSByZWxhw6fDo28gZW50cmUgbyB2ZXRvciBkZSByZXPDrWR1b3MgZSBvcyBlcnJvcyDDqSBkYWRhIHBvciAkXFxEZWx0YSA9IChJIC0gSClcXGVwc2lsb24kLiIsICJBIG1hdHJpeiBkZSBjb3ZhcmnDom5jaWEgZG9zIHJlc8OtZHVvcyDDqSAkVmFyW1xcRGVsdGFdID0gVmFyWyhJIC0gSClcXGVwc2lsb25dID0gKEkgLSBIKSBWYXJbXFxlcHNpbG9uXSAoSSAtIEgpXlQkLiIsICJDb21vICRWYXJbXFxlcHNpbG9uXSA9IFxcc2lnbWFeMiBJJCwgdGVtb3MgJFZhcltcXERlbHRhXSA9IFxcc2lnbWFeMiAoSSAtIEgpKEkgLSBIKV5UJC4iLCAiQ29tbyAkSCQgw6kgdW1hIG1hdHJpeiBzaW3DqXRyaWNhIGUgaWRlbXBvdGVudGUsICQoSSAtIEgpJCB0YW1iw6ltIMOpIHNpbcOpdHJpY2EgZSBpZGVtcG90ZW50ZSwgbG9nbyAkKEkgLSBIKV4yID0gSSAtIEgkLiIsICJQb3J0YW50bywgJFZhcltcXERlbHRhXSA9IFxcc2lnbWFeMiAoSSAtIEgpJC4iLCAiTyBlbGVtZW50byAkaSQgZGEgZGlhZ29uYWwgcHJpbmNpcGFsLCBxdWUgcmVwcmVzZW50YSBhIHZhcmnDom5jaWEgZG8gJGkkLcOpc2ltbyBlcnJvLCDDqSAkVmFyW1xcRGVsdGFfaV0gPSBcXHNpZ21hXjIoMSAtIGhfaSkkLCBvbmRlICRoX2kkIMOpIG8gJGkkLcOpc2ltbyBlbGVtZW50byBkaWFnb25hbCBkZSAkSCQuIiwgIkNvbW8gJGhfaSQgdmFyaWEgZGUgYWNvcmRvIGNvbSBvIHJlZ3Jlc3NvciAkeF9pJCwgYSB2YXJpw6JuY2lhIGRvIGVycm8gbsOjbyDDqSBjb25zdGFudGUuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAibm1vZzR6YTZhcHFhLCBDYXAgNywgcC4gNzItNzMiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGNsw61uaWNvLCB0ZW1vcyB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBjb20gJG49MzAkIGUgJHA9NCQuIE8gYW5hbGlzdGEgZW5jb250cm91IHVtYSBvYnNlcnZhw6fDo28gY29tIHJlc8OtZHVvIHN0dWRlbnRpemFkbyBpbnRlcm5vICRyX2kgPSAyLjAkLiBDb20gYmFzZSBubyBmb3JtYWxpc21vIGVzdGF0w61zdGljbyBkZSByZXPDrWR1b3Mgc3R1ZGVudGl6YWRvcyBleHRlcm5vcywgZGV0ZXJtaW5lIG8gdmFsb3IgZG8gcmVzw61kdW8gJHRfaSQuIE8gcXVlIGVzc2UgdmFsb3IgaW5kaWNhIHNvYnJlIG8gYWp1c3RlIGRvIG1vZGVsbyBwYXJhIGVzc2Egb2JzZXJ2YcOnw6NvPyIsICJkaWNhIjogIlVzZSBhIHJlbGHDp8OjbyBkaXJldGEgJHRfaSA9IHJfaSBcXHNxcnR7KG4gLSBwIC0gMSkgLyAobiAtIHAgLSByX2leMil9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiSWRlbnRpZmljYXIgb3MgcGFyw6JtZXRyb3M6ICRuPTMwJCwgJHA9NCQsICRyX2kgPSAyLjAkLiIsICJTdWJzdGl0dWlyIG5hIGbDs3JtdWxhOiAkdF9pID0gMi4wIFxcdGltZXMgXFxzcXJ0eygzMCAtIDQgLSAxKSAvICgzMCAtIDQgLSAoMi4wKV4yKX0kLiIsICJDYWxjdWxhciBvIG51bWVyYWRvcjogJG4gLSBwIC0gMSA9IDMwIC0gNCAtIDEgPSAyNSQuIiwgIkNhbGN1bGFyIG8gZGVub21pbmFkb3I6ICRuIC0gcCAtIHJfaV4yID0gMjYgLSA0ID0gMjIkLiIsICJDYWxjdWxhciBhIHJhaXo6ICRcXHNxcnR7MjUvMjJ9ID0gXFxzcXJ0ezEuMTM2fSBcXGFwcHJveCAxLjA2NiQuIiwgIkZpbmFsaXphcjogJHRfaSA9IDIuMCBcXHRpbWVzIDEuMDY2ID0gMi4xMzIkLiIsICJJbnRlcnByZXRhw6fDo286IENvbW8gJHRfaSQgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvICR0JCBkZSBTdHVkZW50IGNvbSAkbi1wLTE9MjUkIGdyYXVzIGRlIGxpYmVyZGFkZSwgdW0gdmFsb3IgZGUgJDIuMTMyJCBpbmRpY2EgdW1hIG9ic2VydmHDp8OjbyBxdWUgc2UgZGVzdmlhIGRlIGZvcm1hIG5vdMOhdmVsIGRvIG1vZGVsbyAodmFsb3IgcHLDs3hpbW8gYW8gcXVhbnRpbCBjcsOtdGljbyBkZSB1bWEgZGlzdHJpYnVpw6fDo28gdCBjb20gMjUgZ2wgcGFyYSAkXFxhbHBoYT0wLjA1JCkuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMSwgMiwgM10sIHk9WzEuMDUsIDIuMTMsIDMuNV0sIG1vZGU9J2xpbmVzK21hcmtlcnMnLCBuYW1lPSdSZXPDrWR1byB0X2knLCBsaW5lPWRpY3QoY29sb3I9JyMwMDAwRkYnKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nVHJhbnNmb3JtYcOnw6NvIGRlIFJlc8OtZHVvcycsIHhheGlzX3RpdGxlPSdSZXPDrWR1byBJbnRlcm5vJywgeWF4aXNfdGl0bGU9J1Jlc8OtZHVvIEV4dGVybm8nLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDIuMTN9LCB7ImVudW5jaWFkbyI6ICJEYWRvIG8gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyICRcXG1hdGhiZnt5fSA9IFxcbWF0aGJme1h9XFxib2xkc3ltYm9se1xcdGhldGF9ICsgXFxib2xkc3ltYm9se1xcRGVsdGF9JCwgZGlzY3V0YSBmb3JtYWxtZW50ZSBjb21vIGEgYW7DoWxpc2UgZG8gZ3LDoWZpY28gZGUgZGlzcGVyc8OjbyBkb3MgcmVzw61kdW9zICQoXFxoYXR7eX1faSwgZV9pKSQgcGVybWl0ZSBkaWFnbm9zdGljYXIgYSB2aW9sYcOnw6NvIGRvIHByZXNzdXBvc3RvIGRlIGhvbW9jZWRhc3RpY2lkYWRlLiBVdGlsaXplIG9zIHPDrW1ib2xvcyBub3RhY2lvbmFpcyBlc3RyaXRvcyBleGlnaWRvcy4iLCAiZGljYSI6ICJDb21wYXJlIG8gY29tcG9ydGFtZW50byBlc3BlcmFkbyBkYSB2YXJpw6JuY2lhIGRvcyByZXPDrWR1b3Mgc29iIGhvbW9jZWRhc3RpY2lkYWRlIGNvbSBvIHF1ZSBzZXJpYSBvYnNlcnZhZG8gbm8gZ3LDoWZpY28gZW0gdW0gY2Vuw6FyaW8gZGUgaGV0ZXJvY2VkYXN0aWNpZGFkZS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gU29iIG9zIHByZXNzdXBvc3RvcyBkZSBHYXVzcy1NYXJrb3YsIG8gdGVybW8gZGUgZXJybyAkXFxib2xkc3ltYm9se1xcRGVsdGF9JCBkZXZlIHBvc3N1aXIgdmFyacOibmNpYSBjb25zdGFudGUsIG91IHNlamEsICRWYXJbXFxEZWx0YV9pXSA9IFxcc2lnbWFeMiQgcGFyYSB0b2RvICRpJC4iLCAiMi4gQ29tbyAkZV9pID0gKEktUCl5X2kkLCBhIHZhcmnDom5jaWEgZG8gcmVzw61kdW8gw6kgJFZhcltlX2ldID0gXFxzaWdtYV4yKDEgLSBoX2kpJCwgb25kZSAkaF9pJCDDqSBvIGVsZW1lbnRvIGRpYWdvbmFsIGRhIG1hdHJpeiBkZSBwcm9qZcOnw6NvICRQJC4iLCAiMy4gRW0gYW1vc3RyYXMgZ3JhbmRlcywgJGhfaSQgw6kgcGVxdWVubyBlICRWYXJbZV9pXSBcXGFwcHJveCBcXHNpZ21hXjIkLiBQb3J0YW50bywgZ3JhZmljYW1lbnRlLCBvcyByZXPDrWR1b3MgZGV2ZW0gYXByZXNlbnRhciB1bWEgZGlzcGVyc8OjbyB1bmlmb3JtZSBhbyBsb25nbyBkbyBlaXhvIGhvcml6b250YWwgKHZhbG9yZXMgYWp1c3RhZG9zICRcXGhhdHt5fV9pJCkuIiwgIjQuIFNlIG8gZ3LDoWZpY28gJChcXGhhdHt5fV9pLCBlX2kpJCBtb3N0cmFyIHVtIHBhZHLDo28gb25kZSBhIGRpc3BlcnPDo28gZGUgJGVfaSQgbXVkYSBjb25mb3JtZSAkXFxoYXR7eX1faSQgYXVtZW50YSBvdSBkaW1pbnVpIChjb21vIHVtIGZ1bmlsKSwgaXNzbyBpbmRpY2EgcXVlICRWYXJbZV9pIHwgXFxoYXR7eX1faV0gXFxuZXEgXFx0ZXh0e2NvbnN0YW50ZX0kLCBldmlkZW5jaWFuZG8gYSBoZXRlcm9jZWRhc3RpY2lkYWRlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlIGEgZGlmZXJlbsOnYSBjb25jZWl0dWFsIGUgZGlhZ27Ds3N0aWNhIGVudHJlIGVuY29udHJhciBoZXRlcm9jZWRhc3RpY2lkYWRlIGUgZW5jb250cmFyIG7Do28gbGluZWFyaWRhZGUgYW8gYW5hbGlzYXIgdW0gZ3LDoWZpY28gZGUgcmVzw61kdW9zLiBDb21vIGNhZGEgZmVuw7RtZW5vIGltcGFjdGEgbyB2YWxvciBlc3BlcmFkbyBkb3MgcmVzw61kdW9zPyIsICJkaWNhIjogIkNvbnNpZGVyZSBhIHJlbGHDp8OjbyAkRVtlX2kgfCBcXGhhdHt5fV9pXSQgZSAkVmFyW2VfaSB8IFxcaGF0e3l9X2ldJCBwYXJhIGRpZmVyZW5jaWFyIG9zIGRvaXMgcHJvYmxlbWFzLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBOw6NvIGxpbmVhcmlkYWRlIG9jb3JyZSBxdWFuZG8gJEVbZV9pIHwgXFxoYXR7eX1faV0gXFxuZXEgMCQuIElzc28gZ2VyYSBwYWRyw7VlcyBzaXN0ZW3DoXRpY29zIGdlb23DqXRyaWNvcyAoY3VydmFzKSBubyBncsOhZmljbywgaW5kaWNhbmRvIHF1ZSBvIG1vZGVsbyBsaW5lYXIgbsOjbyBjYXB0dXJvdSB0b2RhIGEgZXN0cnV0dXJhIGRhIHJlbGHDp8Ojby4iLCAiMi4gSGV0ZXJvY2VkYXN0aWNpZGFkZSBvY29ycmUgcXVhbmRvICRWYXJbZV9pIHwgXFxoYXR7eX1faV0gXFxuZXEgXFxzaWdtYV4yJC4gSXNzbyBnZXJhIHBhZHLDtWVzIGRlIG11ZGFuw6dhIG5hIGRpc3BlcnPDo28gKGZ1bmlzIG91IGFiZXJ0dXJhcyksIGluZGljYW5kbyB2YXJpYWJpbGlkYWRlIG7Do28gY29uc3RhbnRlIG5vcyBlcnJvcy4iLCAiMy4gRW5xdWFudG8gYSBuw6NvIGxpbmVhcmlkYWRlIHN1Z2VyZSB1bWEgZmFsaGEgbmEgZm9ybWEgZnVuY2lvbmFsIGRhIG3DqWRpYSBjb25kaWNpb25hbCwgYSBoZXRlcm9jZWRhc3RpY2lkYWRlIHN1Z2VyZSB1bWEgZmFsaGEgbmEgcHJlbWlzc2EgZGUgY29uc3TDom5jaWEgZGEgdmFyacOibmNpYSBkbyBydcOtZG8uIiwgIjQuIEFtYmFzIHZpb2xhbSBwcmVzc3Vwb3N0b3MgZGUgR2F1c3MtTWFya292IGUgZXhpZ2VtIGRpYWduw7NzdGljb3MgZGlzdGludG9zOiB0cmFuc2Zvcm1hw6fDtWVzIGZ1bmNpb25haXMgcGFyYSBuw6NvIGxpbmVhcmlkYWRlIGUgbcOpdG9kb3MgZGUgZXN0aW1hw6fDo28gcm9idXN0b3Mgb3UgdHJhbnNmb3JtYcOnw7VlcyBkZSBlc2NhbGEgcGFyYSBoZXRlcm9jZWRhc3RpY2lkYWRlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBxdWUgZW0gdW0gZXN0dWRvIGRlIHJlZ3Jlc3PDo28sIGFww7NzIG8gYWp1c3RlIGRvIG1vZGVsbywgbyByZXPDrWR1byAkZV9pJCBwYXJhIHVtYSBvYnNlcnZhw6fDo28gZXNwZWPDrWZpY2Egw6kgY2FsY3VsYWRvIGNvbW8gYSBkaWZlcmVuw6dhIGVudHJlIG8gdmFsb3IgcmVhbCAkWV9pJCBlIG8gcHJldmlzdG8gJFxcaGF0e1l9X2kkLiBTZSBvYnNlcnZhcm1vcyBxdWUsIHBhcmEgdmFsb3JlcyBlbGV2YWRvcyBkZSAkXFxoYXR7WX1faSQsIGEgbcOpZGlhIGRvcyByZXPDrWR1b3Mgc2UgZGVzdmlhIGNvbnNpc3RlbnRlbWVudGUgZGUgemVybywgbyBxdWUgaXNzbyBpbXBsaWNhIHBhcmEgYSB2YWxpZGFkZSBkbyBhanVzdGU/IEp1c3RpZmlxdWUgdXNhbmRvIG8gZm9ybWFsaXNtbyBkZSAkRVtlX2kgfCBcXGhhdHt5fV9pXSQuIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGNvbmRpw6fDo28gZGUgb3J0b2dvbmFsaWRhZGUgZG9zIHJlc8OtZHVvcyBlbSBtb2RlbG9zIGxpbmVhcmVzIGFqdXN0YWRvcyBwb3IgbcOtbmltb3MgcXVhZHJhZG9zLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBPIG1vZGVsbyDDqSBkZWZpbmlkbyBwb3IgJFxcbWF0aGJme3l9ID0gXFxtYXRoYmZ7WH1cXGJvbGRzeW1ib2x7XFx0aGV0YX0gKyBcXGJvbGRzeW1ib2x7XFxEZWx0YX0kLiIsICIyLiBBIGNvbmRpw6fDo28gZGUgYWp1c3RlIHBvciBtw61uaW1vcyBxdWFkcmFkb3MgZ2FyYW50ZSBxdWUgJFxcc3VtIGVfaSA9IDAkLCBvdSBzZWphLCAkRVtlX2ldID0gMCQuIiwgIjMuIFNlICRFW2VfaSB8IFxcaGF0e3l9X2ldIFxcbmVxIDAkIHBhcmEgdW0gc3ViY29uanVudG8gZGUgZGFkb3MgKHZhbG9yZXMgZWxldmFkb3MgZGUgJFxcaGF0e3l9X2kkKSwgaXNzbyBkZW1vbnN0cmEgcXVlIGEgbcOpZGlhIGNvbmRpY2lvbmFsIGRvcyBlcnJvcyBuw6NvIMOpIG51bGEuIiwgIjQuIElzc28gdmlvbGEgYSBwcmVtaXNzYSBkZSBxdWUgYSByZWxhw6fDo28gc2lzdGVtw6F0aWNhICRFW3l8eF0gPSB4XlRcXHRoZXRhJCBmb2kgY29ycmV0YW1lbnRlIGVzcGVjaWZpY2FkYS4iLCAiNS4gQ29uY2x1aS1zZSwgcG9ydGFudG8sIHF1ZSBleGlzdGUgdW0gdmnDqXMgZXN0cnV0dXJhbCBubyBtb2RlbG8gZGV2aWRvIMOgIG3DoSBlc3BlY2lmaWNhw6fDo28gZGEgZm9ybWEgZnVuY2lvbmFsLCBleGlnaW5kbyB1bWEgcmVhdmFsaWHDp8OjbyBkYSBlc3RydXR1cmEgZG8gbW9kZWxvLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIG1vZGVsbyBsaW5lYXIgJFxcbWF0aGJme3l9ID0gXFxtYXRoYmZ7WH1cXGJvbGRzeW1ib2x7XFx0aGV0YX0gKyBcXGJvbGRzeW1ib2x7XFxEZWx0YX0kIGNvbSAkbj0xMCQgb2JzZXJ2YcOnw7VlcywgbyB2ZXRvciBkZSByZXPDrWR1b3MgY2FsY3VsYWRvIMOpICRcXG1hdGhiZntlfSA9IChJIC0gUClcXG1hdGhiZnt5fSQuIENvbnNpZGVyYW5kbyBhIHN1cG9zacOnw6NvIGRlIG5vcm1hbGlkYWRlIGRvcyBlcnJvcyAkXFxib2xkc3ltYm9se1xcRGVsdGF9IFxcc2ltIE4oXFxtYXRoYmZ7MH0sIFxcc2lnbWFeMiBcXG1hdGhiZntJfSkkLCBkZW1vbnN0cmUgbWF0ZW1hdGljYW1lbnRlIHF1ZSBhIGZvcm1hIHF1YWRyw6F0aWNhICRcXGZyYWN7U1FSZXN9e1xcc2lnbWFeMn0gPSBcXGZyYWN7XFxtYXRoYmZ7ZX0nXFxtYXRoYmZ7ZX19e1xcc2lnbWFeMn0kIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyBxdWktcXVhZHJhZG8gJFxcY2hpXjIobi1yKFgpKSQuIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIHByb3ByaWVkYWRlIGRhIG1hdHJpeiAkTSA9IChJIC0gUCkkLiBWZXJpZmlxdWUgc2UgZWxhIMOpIHNpbcOpdHJpY2EgZSBpZGVtcG90ZW50ZSwgZSB1dGlsaXplIG8gdGVvcmVtYSBkZSBxdWUgc2UgJFxcbWF0aGJme3p9IFxcc2ltIE4oXFxtYXRoYmZ7MH0sIEkpJCwgZW50w6NvICRcXG1hdGhiZnt6fSdcXG1hdGhiZntBfVxcbWF0aGJme3p9IFxcc2ltIFxcY2hpXjIocihBKSkkIHNlICRcXG1hdGhiZntBfSQgZm9yIGlkZW1wb3RlbnRlLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJEZWZpbmltb3MgbyB2ZXRvciBkZSByZXPDrWR1b3MgY29tbyAkXFxtYXRoYmZ7ZX0gPSAoSSAtIFApXFxtYXRoYmZ7eX0kLCBvbmRlICRQID0gWChYJ1gpXnstfVgnJC4iLCAiQSBzb21hIGRlIHF1YWRyYWRvcyBkbyBlcnJvIMOpICRTUVJlcyA9IFxcbWF0aGJme2V9J1xcbWF0aGJme2V9ID0gXFxtYXRoYmZ7eX0nKEkgLSBQKScoSSAtIFApXFxtYXRoYmZ7eX0kLiIsICJDb21vICRQJCDDqSBzaW3DqXRyaWNhIGUgaWRlbXBvdGVudGUgKCRQXjIgPSBQJCksIHRlbW9zICQoSSAtIFApJyhJIC0gUCkgPSAoSSAtIFApKEkgLSBQKSA9IEkgLSAyUCArIFBeMiA9IEkgLSBQJC4iLCAiUG9ydGFudG8sICRTUVJlcyA9IFxcbWF0aGJme3l9JyhJIC0gUClcXG1hdGhiZnt5fSQuIiwgIkRhZG8gcXVlICRcXG1hdGhiZnt5fSBcXHNpbSBOKFhcXGJvbGRzeW1ib2x7XFx0aGV0YX0sIFxcc2lnbWFeMiBJKSQsIG5vcm1hbGl6YW1vcyBvIHZldG9yOiAkXFxtYXRoYmZ7en0gPSBcXGZyYWN7XFxtYXRoYmZ7eX0gLSBYXFxib2xkc3ltYm9se1xcdGhldGF9fXtcXHNpZ21hfSBcXHNpbSBOKFxcbWF0aGJmezB9LCBJKSQuIiwgIkEgZm9ybWEgcXVhZHLDoXRpY2EgcG9kZSBzZXIgZXNjcml0YSBjb21vOiAkXFxmcmFje1xcbWF0aGJme3l9JyhJIC0gUClcXG1hdGhiZnt5fX17XFxzaWdtYV4yfSQuIiwgIkNvbW8gJChJIC0gUClYID0gWCAtIFBYID0gWCAtIFggPSBcXGVtcHR5c2V0JCwgbyB0ZXJtbyBlbnZvbHZlbmRvIGEgbcOpZGlhIGRlc2FwYXJlY2UgbmEgZm9ybWEgcXVhZHLDoXRpY2E6ICQoWFxcYm9sZHN5bWJvbHtcXHRoZXRhfSknKEkgLSBQKShYXFxib2xkc3ltYm9se1xcdGhldGF9KSA9IFxcYm9sZHN5bWJvbHtcXHRoZXRhfSdYJyhJIC0gUClYXFxib2xkc3ltYm9se1xcdGhldGF9ID0gMCQuIiwgIkNvbmNsdcOtbW9zIHF1ZSAkXFxmcmFje1NRUmVzfXtcXHNpZ21hXjJ9IFxcc2ltIFxcY2hpXjIocihJLVApKSQsIG9uZGUgJHIoSS1QKSA9IFRyKEktUCkgPSBuIC0gcihYKSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTHVuYSwgSi4gRy4gJiBFc3RldmVzLCBELiBNLiwgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzLCBDYXAgMywgcC4gNzItNzYiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiU3Vwb25oYSBxdWUsIGFvIGFuYWxpc2FyIG9zIHJlc8OtZHVvcyBkZSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBwYXJhIHByZXZlciBvIGNvbnN1bW8gZGUgZW5lcmdpYSwgdm9jw6ogZW5jb250cm91IG9zIHNlZ3VpbnRlcyB2YWxvcmVzIG9yZGVuYWRvczogJGVfeygxKX0gPSAtMi41LCBlX3soMil9ID0gLTEuMiwgZV97KDMpfSA9IC0wLjUsIGVfeyg0KX0gPSAwLjMsIGVfeyg1KX0gPSAxLjEsIGVfeyg2KX0gPSAyLjgkLiBDb20gJG49NiQsIGNhbGN1bGUgb3MgZG9pcyBwcmltZWlyb3MgcXVhbnRpcyB0ZcOzcmljb3MgZGEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIHBhZHLDo28gJHVfaSA9IFxcUGhpXnstMX0oXFxmcmFje2kgLSAwLjV9e259KSQgbmVjZXNzw6FyaW9zIHBhcmEgYSBjb25zdHJ1w6fDo28gZG8gUS1RIFBsb3QuIEV4cGxpcXVlIG8gcXVlIGVzc2VzIHZhbG9yZXMgcmVwcmVzZW50YW0gbm8gZ3LDoWZpY28uIiwgImRpY2EiOiAiVXRpbGl6ZSBhIGbDs3JtdWxhIGRvcyBxdWFudGlzIHRlw7NyaWNvcyBmb3JuZWNpZGEgbm8gc3VidMOzcGljbzogJFxcUGhpXnstMX0oXFxmcmFje2ktMC41fXtufSkkLiBWb2PDqiBwb2RlIGFwcm94aW1hciBvcyB2YWxvcmVzIHVzYW5kbyBhIHRhYmVsYSBaIHBhZHLDo28gb3UgYSBsw7NnaWNhIGRlIHNpbWV0cmlhLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXJhICRuPTYkLCBvcyBxdWFudGlzIHPDo28gY2FsY3VsYWRvcyBwYXJhICRpPTEkIGUgJGk9MiQuIiwgIlBhcmEgJGk9MSQ6ICR1XzEgPSBcXFBoaV57LTF9KFxcZnJhY3sxIC0gMC41fXs2fSkgPSBcXFBoaV57LTF9KDAuMDgzMykkLiBDb25zdWx0YW5kbyBhIHRhYmVsYSBaLCAkXFxQaGleey0xfSgwLjA4MzMpIFxcYXBwcm94IC0xLjM4JC4iLCAiUGFyYSAkaT0yJDogJHVfMiA9IFxcUGhpXnstMX0oXFxmcmFjezIgLSAwLjV9ezZ9KSA9IFxcUGhpXnstMX0oMC4yNSkkLiBDb25zdWx0YW5kbyBhIHRhYmVsYSBaLCAkXFxQaGleey0xfSgwLjI1KSBcXGFwcHJveCAtMC42NyQuIiwgIkVzc2VzIHZhbG9yZXMgcmVwcmVzZW50YW0gYXMgY29vcmRlbmFkYXMgaG9yaXpvbnRhaXMgKGVpeG8gWCkgbm8gUS1RIFBsb3QgcGFyYSBvcyBxdWFpcyBvcyByZXPDrWR1b3Mgb2JzZXJ2YWRvcyAoJGVfeyhpKX0kKSBkZXZlbSBlc3RhciBhbGluaGFkb3MgY2FzbyBzaWdhbSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9Wy0xLjM4LCAtMC42N10sIHk9Wy0yLjUsIC0xLjJdLCBtb2RlPSdtYXJrZXJzJywgbmFtZT0nUG9udG9zIEluaWNpYWlzJykpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+Q29uc3RydcOnw6NvIGRvIFEtUSBQbG90IChQYXNzbyAxKTwvYj4nLCB4YXhpc190aXRsZT0nUXVhbnRpcyBUZcOzcmljb3MgKCR1X2kkKScsIHlheGlzX3RpdGxlPSdSZXPDrWR1b3MgT3JkZW5hZG9zICgkZV97KGkpfSQpJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScsIGhlaWdodD00MjApIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAtMi4wNX0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGV4cGVyaW1lbnRvIGRlIEVuZ2VuaGFyaWEgZGUgTWF0ZXJpYWlzLCBkZXNlamEtc2UgdGVzdGFyIGEgaGlww7N0ZXNlICRIXzA6IFxcYmV0YV8xID0gMCQgZW0gdW1hIHJlZ3Jlc3PDo28gbGluZWFyIHNpbXBsZXMuIEV4cGxpcXVlIGNvbW8gYSB2aW9sYcOnw6NvIGRhIG5vcm1hbGlkYWRlIGRvcyBlcnJvcyBhZmV0YSBhIHZhbGlkYWRlIGRvIHRlc3RlICR0JCB1dGlsaXphZG8gcGFyYSBlc3RlIGNvZWZpY2llbnRlIGVtIGFtb3N0cmFzIHBlcXVlbmFzICgkbiA8IDIwJCkuIiwgImRpY2EiOiAiQ29uc2lkZXJlIHF1ZSBhIGVzdGF0w61zdGljYSAkdCA9IFxcZnJhY3tcXGhhdHtcXGJldGF9XzF9e0VQKFxcaGF0e1xcYmV0YX1fMSl9JCBkZXBlbmRlIGRhIGRpc3RyaWJ1acOnw6NvIGRvIGVzdGltYWRvciBzb2IgYSBoaXDDs3Rlc2UgZGUgZXJyb3Mgbm9ybWFpcyBlIHF1ZSBhIGluZGVwZW5kw6puY2lhIGVudHJlIG8gZXN0aW1hZG9yIGUgYSB2YXJpw6JuY2lhIHJlc2lkdWFsIGVzdGltYWRhICgkc14yJCkgw6kgZ2FyYW50aWRhIHBlbG8gVGVvcmVtYSBkZSBDb2NocmFuLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJPIHRlc3RlICR0JCDDqSBjb25zdHJ1w61kbyBzb2IgYSBwcmVtaXNzYSBkZSBxdWUgJFxcZnJhY3tcXGhhdHtcXGJldGF9XzEgLSBcXGJldGFfMX17RVAoXFxoYXR7XFxiZXRhfV8xKX0gXFxzaW0gdChuLXApJC4iLCAiU2Ugb3MgZXJyb3MgbsOjbyBzw6NvIG5vcm1haXMsIGEgZGlzdHJpYnVpw6fDo28gZGUgJFxcaGF0e1xcYmV0YX1fMSQgcG9kZSBuw6NvIHNlciBub3JtYWwgKGVzcGVjaWFsbWVudGUgZW0gYW1vc3RyYXMgcGVxdWVuYXMpLCBwb2lzIG7Do28gaMOhIGEgYXBsaWNhw6fDo28gZG8gVGVvcmVtYSBkbyBMaW1pdGUgQ2VudHJhbCBwYXJhIGNvbXBlbnNhciBhIGRpc3RyaWJ1acOnw6NvIG7Do28gbm9ybWFsIGRvcyBlcnJvcy4iLCAiQWzDqW0gZGlzc28sIGEgaW5kZXBlbmTDqm5jaWEgZW50cmUgJFxcaGF0e1xcYmV0YX1fMSQgZSAkc14yJCAobyBxdWFkcmFkbyBtw6lkaW8gZG8gcmVzw61kdW8pIMOpIHVtYSBwcm9wcmllZGFkZSBxdWUgZGVjb3JyZSBlc3RyaXRhbWVudGUgZGEgbm9ybWFsaWRhZGUgbXVsdGl2YXJpYWRhIGRvcyBlcnJvcyAoVGVvcmVtYSBkZSBGaXNoZXItQ29jaHJhbikuIiwgIlNlbSBlc3NhIGluZGVwZW5kw6puY2lhIGUgc2VtIGEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIGRvcyByZXPDrWR1b3MsIGEgZXN0YXTDrXN0aWNhICR0JCBkZWl4YSBkZSBzZWd1aXIgYSBkaXN0cmlidWnDp8OjbyAkdCQgZGUgU3R1ZGVudCwgdG9ybmFuZG8gbyBwLXZhbG9yIG9idGlkbyBlIGEgZGVjaXPDo28gZGUgcmVqZWnDp8OjbyBvdSBuw6NvIGRlICRIXzAkIGVzdGF0aXN0aWNhbWVudGUgaW52w6FsaWRvcyBvdSwgbm8gbcOtbmltbywgbsOjbyBjb25macOhdmVpcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJubW9nNHphNmFwcWEsIHAuIDg4LTg5IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH1dfQ==').decode('utf-8'))


    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dos totais para a barra de progresso
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discursivas = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcqs) + len(discursivas)
    acertos = sum(1 for v in st.session_state.respostas_certas.values() if v is True)
    
    # Cabeçalho de Gamificação
    st.markdown("### 🎯 Painel de Desafios da Unidade")
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso:** {acertos} de {total_exercicios} desafios concluídos!")
    st.divider()
    
    # Loop para Questões de Múltipla Escolha
    for i, questao in enumerate(mcqs):
        with st.container():
            st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
            
            # Renderização de gráfico se houver
            if questao.get("codigo_plotly"):
                try:
                    local_vars = {"go": go, "np": np}
                    exec(questao["codigo_plotly"], globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
                except Exception as e:
                    st.warning("Não foi possível renderizar o gráfico desta questão.")
    
            # Alternativas
            opcoes = questao.get("alternativas", {})
            selecao = st.radio(
                "Escolha uma alternativa:",
                options=list(opcoes.keys()),
                format_func=lambda x: f"{x}) {opcoes[x]}",
                key=f"radio_mcq_{i}"
            )
    
            # Referência
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
    
            # Botões de Ação
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button("✅ Verificar", key=f"btn_mcq_{i}"):
                    if selecao == questao.get("alternativa_correta"):
                        st.success("Correto! Muito bem.")
                        st.session_state.respostas_certas[f"mcq_{i}"] = True
                        st.rerun()
                    else:
                        st.error("Incorreto. Tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
            with col2:
                if st.button("💡 Dica", key=f"hint_mcq_{i}"):
                    st.info(questao.get("dica", "Dica indisponível."))
    
            # Gabarito
            with st.expander("✅ Ver Gabarito Comentado"):
                st.write(questao.get("gabarito_comentado", "Gabarito indisponível."))
        st.divider()
    
    # Loop para Questões Discursivas
    for i, questao in enumerate(discursivas):
        with st.container():
            st.markdown(f"**Desafio Discursivo {i+1}:** {questao.get('enunciado', '')}")
            
            # Gráfico opcional
            if questao.get("codigo_plotly"):
                try:
                    local_vars = {"go": go, "np": np}
                    exec(questao["codigo_plotly"], globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
                except Exception as e:
                    st.warning("Não foi possível renderizar o gráfico.")
    
            st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
    
            # Validação numérica ou manual
            esperada = questao.get("resposta_numerica_esperada")
            if esperada is not None:
                val_user = st.number_input("Digite o resultado numérico calculado:", format="%.4f", key=f"num_disc_{i}")
                if st.button("Validar Cálculo", key=f"val_disc_{i}"):
                    if abs(val_user - esperada) <= max(0.01, 0.01 * abs(esperada)):
                        st.success("Correto! Excelente trabalho.")
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                        st.rerun()
                    else:
                        st.error("Valor incorreto. Revise seus cálculos.")
                        st.session_state.respostas_certas[f"disc_{i}"] = False
            else:
                if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.session_state.respostas_certas[f"disc_{i}"] = False
    
            # Referência e Dica
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
            
            if st.button("💡 Dica", key=f"hint_disc_{i}"):
                st.info(questao.get("dica", "Sem dica disponível."))
    
            # Resolução
            with st.expander("✅ Ver Resolução Detalhada"):
                for passo in questao.get("gabarito_passo_a_passo", []):
                    st.write(f"- {passo}")
        st.divider()
