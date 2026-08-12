import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJGdW5kYW1lbnRvcyBFc3RhdMOtc3RpY29zIGUgUHJvYmFiaWzDrXN0aWNvcyBkZSBMYXJnZSBMYW5ndWFnZSBNb2RlbHMgKExMTXMpIiwgInJlZmVyZW5jaWFzX2JpYmxpb2dyYWZpY2FzX2ZpbmFpcyI6IFsiTWFnYWxow6NlcywgTS4gTi4gLSBQcm9iYWJpbGlkYWRlIGUgRXN0YXTDrXN0aWNhLCBwcC4gMzEtNDAiLCAiTUFUMjI0IC0gTm90YXMgZGUgQXVsYSwgVW5pdmVyc2lkYWRlIEZlZGVyYWwgZGEgQmFoaWEsIHBwLiAxNC0yNSIsICJ5eWJzeHB5NzJodHcgLSBNQVQyMjQgUHJvYmFiaWxpZGFkZSBJSSwgVGVvcmVtYSBDZW50cmFsIGRvIExpbWl0ZSBNdWx0aXZhcmlhZG8sIHBwLiA4Ny04OCIsICJ5eWJzeHB5NzJodHcgKE1BVDIyNCAtIFByb2JhYmlsaWRhZGUgSUkgLSBVRkJBKSwgRGVzaWd1YWxkYWRlIGRlIEtvbG1vZ29yb3YgZSBMZWlzIGRvcyBHcmFuZGVzIE7Dum1lcm9zLCBwcC4gNjItNjMiXX0=').decode('utf-8'))

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
            background: linear-gradient(135deg, #0F172A 0%, #3B82F6 100%);
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
            border-top: 3px solid #0F172A !important;
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
            background: linear-gradient(90deg, #0F172A 0%, #334155 100%) !important;
            border-radius: 10px !important;
        }
        
        /* Inputs e Sliders na aula */
        div.stSlider [data-testid="stSliderTickBar"] {
            background-color: #0F172A !important;
        }
        
        /* Botões na aula */
        div.stButton > button {
            background: linear-gradient(135deg, #0F172A 0%, #3B82F6 100%) !important;
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
PRIMARY_BLUE = "#0F172A"
SECONDARY_GREEN = "#334155"
WARNING_AMBER = "#64748B"
CRITICAL_RED = "#991B1B"

# Criação das Duas Grandes Abas Globais
tab_conteudo, tab_exercicios = st.tabs(["📚 Conteúdo Acadêmico Interativo", "📝 Caderno de Exercícios"])

with tab_conteudo:

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    import pandas as pd
    
    # Título do Subtópico
    st.title(r"Arquitetura Probabilística: De Séries Aleatórias a Processos Autoregressivos")
    
    # Introdução Teórica
    st.markdown(r"""
    A transição da estatística clássica, fundamentada na suposição de variáveis aleatórias independentes e identicamente distribuídas (i.i.d.), para o estudo da arquitetura probabilística de processos estocásticos, marca a diferença fundamental entre descrever um fenômeno estático e modelar a própria dinâmica da inteligência. 
    
    Na estatística clássica, recorremos ao teorema central do limite ou à lei dos grandes números para descrever populações onde o valor observado em uma instância nada revela sobre a próxima. No entanto, ao modelar a linguagem, percebemos que essa suposição de independência é uma simplificação que ignora a estrutura sintática e semântica de tudo o que foi dito anteriormente.
    """)
    
    st.info(r"A linguagem humana não é um conjunto de tokens isolados, mas uma cadeia de dependências profundas onde o significado do termo atual é condicionado pelo histórico acumulado.")
    
    st.markdown(r"""
    É neste ponto que introduzimos os processos autoregressivos. Neles, a história do sistema atua como uma força motriz que molda as probabilidades do porvir, utilizando a filtração $\mathcal{F}_{t-1}$ para representar toda a informação acumulada até o instante $t-1$.
    """)
    
    # Formalismo Matemático
    st.subheader(r"Formalismo da Predição")
    st.latex(r"P(X_t = x_t \mid X_1 = x_1, \dots, X_{t-1} = x_{t-1}) = f(x_t; \theta, \mathcal{F}_{t-1})")
    st.latex(r"E[X_t \mid X_1, \dots, X_{t-1}] = \int x \cdot dP(X_t = x \mid X_1, \dots, X_{t-1})")
    
    # Dedução Analítica
    st.subheader(r"Dedução Analítica")
    st.markdown(r"A decomposição da verossimilhança de uma sequência é dada por:")
    st.latex(r"P(X_1, X_2, \dots, X_n) = P(X_1) \prod_{t=2}^n P(X_t \mid X_1, \dots, X_{t-1})")
    st.latex(r"\hat{X}_t = E[X_t \mid X_{1:t-1}] = \int x \cdot P(x \mid X_{1:t-1}) dx")
    
    # Exemplos Práticos
    st.subheader(r"Exemplos Práticos")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo: Processo Autoregressivo de Ordem 1 (AR(1))")
        st.markdown(r"Consideramos a relação $X_t = \phi X_{t-1} + \epsilon_t$, onde $\epsilon_t$ é ruído branco.")
        st.markdown(r"1. Aplicamos a esperança condicional: $E[X_t \mid X_{t-1}] = E[\phi X_{t-1} + \epsilon_t \mid X_{t-1}]$")
        st.markdown(r"2. Pela linearidade: $E[X_t \mid X_{t-1}] = \phi E[X_{t-1} \mid X_{t-1}] + E[\epsilon_t \mid X_{t-1}]$")
        st.markdown(r"3. Como $E[\epsilon_t] = 0$, obtemos a predição ótima: $E[X_t \mid X_{t-1}] = \phi X_{t-1}$")
        st.success(r"Laudo: O valor esperado do próximo estado é uma versão escalonada do estado anterior, provando que a memória de curto prazo é capturada pela estrutura paramétrica.")
    
    # Simulador Interativo Plotly
    st.subheader(r"Simulador de Processo Autoregressivo")
    col1, col2 = st.columns(2)
    phi = col1.slider(r"Parâmetro de persistência (phi)", -0.9, 0.9, 0.5, 0.1, key=r"phi_slider_subtopico_1")
    n_steps = col2.slider(r"Número de passos (n)", 10, 100, 50, 1, key=r"n_steps_slider_subtopico_1")
    
    # Geração de dados para o simulador
    np.random.seed(42)
    x = [0]
    for _ in range(n_steps):
        x.append(phi * x[-1] + np.random.normal(0, 0.1))
    
    df_sim = pd.DataFrame({r"Passo": range(len(x)), r"Valor": x})
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_sim[r"Passo"], y=df_sim[r"Valor"], mode=r"lines+markers", name=r"Série AR(1)", line=dict(color=r"#0F172A")))
    fig.update_layout(
        template=r"plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Simulação de Processo AR(1)</b>", font=dict(size=14, color=r"#1E293B", family=r"Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Tempo (t)", font=dict(size=11, color=r"#1E293B", family=r"Arial, sans-serif")), tickfont=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Estado (Xt)", font=dict(size=11, color=r"#1E293B", family=r"Arial, sans-serif")), tickfont=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        legend=dict(orientation=r"h", yanchor=r"bottom", y=1.02, xanchor=r"right", x=1.0, font=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), bgcolor=r"rgba(255, 255, 255, 0.8)", bordercolor=r"#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor=r"#FFFFFF", font_size=12, font_color=r"#1E293B", font_family=r"Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    st.info(f"Ao variar o parâmetro phi para {phi}, observamos que a série apresenta uma memória de curto prazo mais intensa (quando phi se aproxima de 1) ou um retorno mais rápido à média (quando phi se aproxima de 0). Este comportamento modela a dependência temporal intrínseca da linguagem.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy.stats import multivariate_normal
    
    # Título da Seção
    st.title("Mecanismos de Atenção e a Inferência em Espaços de Alta Dimensão")
    
    # Introdução
    st.markdown(r"""
    Sejam bem-vindos a esta exposição sobre a intersecção entre a inferência estatística clássica e a arquitetura dos modelos de linguagem contemporâneos. Ao nos debruçarmos sobre a estrutura interna desses modelos, somos convidados a abandonar a intuição escalar do século passado e abraçar a elegância da geometria estatística em espaços de dimensão elevada.
    """)
    
    st.markdown(r"""
    Na ciência de dados moderna, operamos com vetores densos que habitam variedades de dimensão multivariada. O mecanismo de atenção, pilar central da arquitetura Transformer, deve ser compreendido como uma operação dinâmica de reponderação de pesos que busca extrair correlações subjacentes em um oceano de dados multivariados.
    """)
    
    st.info(r"A atenção é, em última análise, um estimador de máxima verossimilhança operando sob restrições de alta dimensionalidade.")
    
    # Formalismo Matemático
    st.subheader("Formalismo da Convergência e Estrutura de Covariância")
    st.markdown(r"A estabilidade da inferência nestes sistemas é garantida pela convergência em distribuição. Definimos o comportamento assintótico das médias amostrais através da seguinte expressão:")
    
    st.latex(r"\sqrt{n}(\bar{X}_n - \mu) \xrightarrow{D} N(0, \Sigma)")
    
    st.markdown(r"Onde a matriz de covariância, que atua como o mapa de afinidades do mecanismo de atenção, é dada por:")
    
    st.latex(r"\Sigma = E[(\underline{X} - \mu)(\underline{X} - \mu)^T]")
    
    # Dedução Analítica (Hardcoded)
    st.subheader("Dedução Analítica")
    
    st.markdown(r"1. **Esperança da média amostral:**")
    st.latex(r"E[\bar{X}_n] = E[\frac{1}{n} \sum_{i=1}^n \underline{X}_i] = \mu")
    
    st.markdown(r"2. **Variância do estimador:**")
    st.latex(r"Var(\bar{X}_n) = Var(\frac{1}{n} \sum_{i=1}^n \underline{X}_i) = \frac{1}{n^2} (n \Sigma) = \frac{1}{n} \Sigma")
    
    st.markdown(r"3. **Convergência Assintótica:**")
    st.latex(r"\sqrt{n}(\bar{X}_n - \mu) \sim N(0, \Sigma) \text{ assintoticamente}")
    
    # Exemplos Práticos
    st.subheader("Exemplo Prático: Estabilidade de Embeddings")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Prático: Agrupamento em Espaço de k=2")
        st.markdown(r"Considere o embedding de uma palavra com média $\mu = [0, 0]^T$ e matriz de covariância:")
        st.latex(r"\Sigma = \begin{pmatrix} 1 & 0.5 \\ 0.5 & 1 \end{pmatrix}")
        st.markdown(r"Com $n=100$ observações, a variância da média amostral torna-se:")
        st.latex(r"Var(\bar{X}_n) = \begin{pmatrix} 0.01 & 0.005 \\ 0.005 & 0.01 \end{pmatrix}")
    
    st.success(r"Laudo: A análise revela que a variabilidade da média amostral é reduzida em um fator de 100. A correlação de 0.5 preservada entre as dimensões indica que a dependência linear persiste, sendo uma característica estrutural fundamental para o ajuste fino.")
    
    # Simulador Interativo
    st.subheader("Simulador: Convergência da Média Amostral")
    
    col1, col2 = st.columns(2)
    with col1:
        n_samples = st.slider(r"Tamanho da Amostra (n)", 10, 1000, 100, key=r"n_samples_subtopico_2")
    with col2:
        rho = st.slider(r"Correlação (\rho)", -0.9, 0.9, 0.5, key=r"rho_subtopico_2")
    
    # Lógica do Simulador
    mu = np.array([0, 0])
    cov = np.array([[1, rho], [rho, 1]])
    data_points = np.random.multivariate_normal(mu, cov, n_samples)
    sample_mean = np.mean(data_points, axis=0)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data_points[:,0], y=data_points[:,1], mode='markers', name=r"Observações", marker=dict(color="#64748B", size=4, opacity=0.5)))
    fig.add_trace(go.Scatter(x=[sample_mean[0]], y=[sample_mean[1]], mode='markers', name=r"Média Amostral", marker=dict(color="#991B1B", size=12, symbol='star')))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Convergência da Média em Espaço 2D</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Dimensão 1", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Dimensão 2", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    # Laudo Dinâmico
    st.info(f"Ao aumentar o número de observações para {n_samples}, a média amostral (estrela vermelha) converge mais estavelmente para a origem [0,0], demonstrando como o Teorema Central do Limite reduz o ruído estatístico na representação vetorial.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    
    # Título do Subtópico
    st.title(r"Estabilidade e Convergência em Modelos de Linguagem de Grande Escala")
    
    # Prosa Parte 1
    st.markdown(r"""
    A estabilidade e a convergência em Modelos de Linguagem de Grande Escala (LLMs) representam, talvez, a fronteira mais crítica entre a computação empírica e a teoria das probabilidades rigorosa. Quando observamos modelos com bilhões de parâmetros sendo treinados sobre trilhões de tokens, estamos diante de um sistema estocástico de complexidade sem precedentes.
    """)
    
    st.info(r"A intuição básica sugere que o aumento da escala dos dados e da arquitetura induz uma 'calma' estatística, conduzindo o desempenho do modelo para um estado de equilíbrio previsível.")
    
    st.markdown(r"""
    A transição para este regime de estabilidade exige que compreendamos profundamente como as flutuações amostrais — os gradientes ruidosos calculados sobre mini-batches — não desviam o modelo de um caminho de otimização ótimo. Recorremos às Leis dos Grandes Números para fundamentar essa trajetória. Enquanto a Lei Fraca nos garante a convergência da média amostral para a populacional, em cenários de treinamento dinâmico, precisamos controlar toda a trajetória.
    """)
    
    # Formalismo Matemático
    st.subheader(r"O Protocolo de Segurança Estatística")
    st.markdown(r"A estabilidade é formalizada através da desigualdade de Kolmogorov, que baliza os desvios máximos do processo de treinamento em relação à média esperada:")
    st.latex(r"P\left(\max_{1 \le k \le n} |S_k| \ge \lambda\right) \le \frac{Var(S_n)}{\lambda^2}")
    
    # Prosa Parte 2
    st.markdown(r"""
    Esta desigualdade estabelece que a probabilidade de que qualquer desvio máximo do sistema de treinamento exceda um limite $\lambda$ é inversamente proporcional ao quadrado desse limiar e diretamente limitada pela variância final do processo.
    """)
    
    st.warning(r"Na prática, reduzir a variância do processo estocástico de aprendizado — por meio de técnicas como gradient clipping — é a estratégia fundamental para garantir que o modelo não sucumba a oscilações caóticas.")
    
    # Exemplo Prático
    st.markdown(r"##### 📖 Exemplo Prático: Monitoramento de Erro Acumulado")
    with st.container(border=True):
        st.markdown(r"""
        **Contexto:** Monitoramento do erro de predição durante 100 dias.
        - **Passo 1:** Definição da variância total ($Var(S_{100}) = n \sigma^2 = 100$).
        - **Passo 2:** Aplicação do limiar $\lambda = 15$.
        - **Passo 3:** Cálculo da probabilidade de desvio: $P \le 100 / 15^2$.
        """)
        st.latex(r"P(\max_{1 \le k \le 100} |S_k| \ge 15) \le \frac{100}{225} \approx 0.444")
        st.success(r"O limite de 44,4% estabelece uma margem de segurança crítica, permitindo ajustes no learning rate para manter a convergência sob controle.")
    
    # Simulador Interativo
    st.subheader(r"Simulador: Dinâmica de Desvios (Random Walk)")
    col1, col2 = st.columns(2)
    
    n_steps = col1.slider(r"Passos (n)", 10, 500, 100, key=r"n_steps_subtopico_3")
    var_sigma = col2.slider(r"Variância ($\sigma^2$)", 0.1, 2.0, 1.0, key=r"var_sigma_subtopico_3")
    
    # Lógica interna do simulador
    np.random.seed(42)
    x = np.random.normal(0, np.sqrt(var_sigma), n_steps)
    s_k = np.cumsum(x)
    max_dev = np.maximum.accumulate(np.abs(s_k))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=s_k, mode='lines', name=r'Trajetória S_k', line=dict(color='#0F172A')))
    fig.add_trace(go.Scatter(y=max_dev, mode='lines', name=r'Desvio Máximo', line=dict(color='#991B1B', dash='dash')))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Monitoramento de Estabilidade no Treinamento</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Passos de Treinamento", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Valor Acumulado", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    st.info(f"Com {n_steps} passos e variância {var_sigma}, o modelo apresenta um desvio máximo acumulado de {max_dev[-1]:.2f}. A estabilidade estatística é mantida enquanto a trajetória se mantém contida sob o envelope de variância calculado.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    
    # Título do Subtópico
    st.markdown(r"### A Engenharia de Probabilidades: Modelagem e Distribuições de Tokens")
    
    st.markdown(r"A transição da linguagem natural para um domínio matemático rigoroso exige, primordialmente, uma abstração fundamental: a tokenização. Historicamente, a ciência da computação lidava com o texto através de representações rígidas, contudo, ao tratarmos a linguagem como um sinal estocástico, percebemos que o texto não é apenas uma sequência de símbolos, mas a manifestação observável de um processo gerador subjacente.")
    
    st.info(r"A tokenização atua como o primeiro elo desta cadeia, mapeando fragmentos de texto em índices discretos de um vocabulário de tamanho K. Este mapeamento transforma a fluidez da sintaxe humana em um espaço vetorial modelável.")
    
    st.markdown(r"Ao encararmos a tarefa de prever o próximo token, lidamos com uma variável aleatória discreta. O modelo produz um vetor de logitos, denotado como z, que representa a pontuação bruta de cada token. Para converter essas pontuações em probabilidades, empregamos a função Softmax com um parâmetro de temperatura T.")
    
    st.latex(r"p_i = \frac{\exp(z_i/T)}{\sum_{j=1}^K \exp(z_j/T)}")
    
    st.markdown(r"A incerteza inerente é quantificada pela entropia de Shannon, mas para treinar o modelo em relação a uma distribuição alvo, utilizamos a divergência de Kullback-Leibler.")
    
    st.latex(r"D_{KL}(P \parallel Q) = \sum_{i=1}^K p_i \log\left(\frac{p_i}{q_i}\right)")
    
    st.warning(r"A divergência de Kullback-Leibler mede a informação perdida quando utilizamos a distribuição Q para aproximar a distribuição alvo P. Sua minimização é o motor do aprendizado estatístico.")
    
    # Deduções Analíticas
    st.markdown(r"#### Fundamentos Estatísticos")
    st.latex(r"H(P) = -\sum p_i \log p_i")
    st.latex(r"D_{KL} = \sum p_i \log p_i - \sum p_i \log q_i")
    st.latex(r"\frac{S_n - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} N(0,1)")
    
    # Exemplo Prático
    st.markdown(r"#### 📖 Exemplo Prático: Análise de Confiança")
    with st.container(border=True):
        st.markdown(r"**Contexto:** Vocabulário de 3 tokens com logitos $z = [2.0, 1.0, 0.1]$.")
        st.latex(r"\exp(z) = [7.389, 2.718, 1.105], \quad \sum \exp(z) = 11.212")
        st.markdown(r"**Cálculo das probabilidades:**")
        st.write(r"$p_1 = 0.659, \quad p_2 = 0.242, \quad p_3 = 0.099$")
        st.latex(r"H(P) \approx 0.812")
        st.success(r"Com uma entropia de 0.812 nats e 65,9% de probabilidade atribuída ao primeiro token, o modelo apresenta uma confiança moderada-alta.")
    
    # Simulador de Temperatura
    st.markdown(r"#### Simulador de Temperatura (Softmax)")
    col1, col2 = st.columns(2)
    temp = col1.slider(r"Temperatura (T)", 0.1, 2.0, 1.0, key=r"temp_slider_subtopico_4")
    
    # Lógica de cálculo estática para o simulador
    logits = np.array([2.0, 1.0, 0.1])
    probs = np.exp(logits / temp) / np.sum(np.exp(logits / temp))
    
    fig = go.Figure(data=[go.Bar(
        x=[r"Token 1", r"Token 2", r"Token 3"], 
        y=probs,
        marker_color=r"#0F172A"
    )])
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        plot_bgcolor="white",
        paper_bgcolor="white",
        title=dict(text="<b>Distribuição de Probabilidade por Temperatura</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Tokens", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Probabilidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")
    
    if temp < 0.5:
        st.info(r"Temperatura baixa: O modelo está operando em regime de alta confiança, priorizando o token com maior logito (Greedy Decoding).")
    elif temp > 1.5:
        st.info(r"Temperatura alta: A distribuição tornou-se mais uniforme, aumentando a entropia e promovendo a exploração estocástica.")
    else:
        st.info(r"Temperatura moderada: O modelo mantém um equilíbrio entre a estrutura do corpus e a incerteza estatística.")
    
    st.markdown(r"A estabilidade das ativações nas camadas profundas, conforme regido pelo Teorema Central do Limite, garante que a rede neural mantenha a integridade do sinal, permitindo a eficácia desses cálculos probabilísticos em arquiteturas de larga escala.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJMTE1zIiwgInF1ZXN0b2VzX211bHRpcGxhX2VzY29saGEiOiBbeyJlbnVuY2lhZG8iOiAiRW0gdW0gc2lzdGVtYSBkZSBwcm9jZXNzYW1lbnRvIGRlIGxpbmd1YWdlbSBuYXR1cmFsLCB1bSBwZXNxdWlzYWRvciBtb2RlbGEgYSBzZXF1w6puY2lhIGRlIHRva2VucyBnZXJhZG9zIHBvciB1bSBtb2RlbG8gY29tbyB1bSBwcm9jZXNzbyBlc3RvY8Ohc3RpY28uIEFvIGNvbXBhcmFyIG8gbW9kZWxvIGF0dWFsIGNvbSB1bSBtb2RlbG8gYmFzZWFkbyBlc3RyaXRhbWVudGUgbmEgaGlww7N0ZXNlIGRlIHZhcmnDoXZlaXMgYWxlYXTDs3JpYXMgaW5kZXBlbmRlbnRlcyBlIGlkZW50aWNhbWVudGUgZGlzdHJpYnXDrWRhcyAoaS5pLmQuKSwgbyBwZXNxdWlzYWRvciBvYnNlcnZhIHVtYSBmYWxoYSBzaWduaWZpY2F0aXZhIG5hIGNvZXLDqm5jaWEgZG8gdGV4dG8uIFF1YWwgZGFzIHNlZ3VpbnRlcyBhbHRlcm5hdGl2YXMgZGVzY3JldmUgY29ycmV0YW1lbnRlIGEgcmF6w6NvIGVzdGF0w61zdGljYSBmdW5kYW1lbnRhbCBwYXJhIGVzc2EgZmFsaGEgZW0gY29udGV4dG9zIHNlcXVlbmNpYWlzPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBzdXBvc2nDp8OjbyBpLmkuZC4gaWdub3JhIHF1ZSwgZW0gc2VxdcOqbmNpYXMgbGluZ3XDrXN0aWNhcywgYSBlc3BlcmFuw6dhIGNvbmRpY2lvbmFsICRFW1hfdCBcXG1pZCBcXG1hdGhjYWx7Rn1fe3QtMX1dJCDDqSBuZWNlc3NhcmlhbWVudGUgY29uc3RhbnRlIHBhcmEgdG9kbyAkdCQuIiwgIkIiOiAiRW0gcHJvY2Vzc29zIGF1dG9yZWdyZXNzaXZvcywgYSB2YXJpw6JuY2lhIG1hcmdpbmFsIHRlbmRlIGEgemVybywgZW5xdWFudG8gbm8gbW9kZWxvIGkuaS5kLiBlbGEgcGVybWFuZWNlIGZpbml0YSwgaW52YWxpZGFuZG8gYSBjb21wYXJhw6fDo28uIiwgIkMiOiAiQSBlc3RydXR1cmEgZGUgbGluZ3VhZ2VtIGV4aWdlIHF1ZSBhIGRpc3RyaWJ1acOnw6NvIGNvbmRpY2lvbmFsICRQKFhfdCBcXG1pZCBcXG1hdGhjYWx7Rn1fe3QtMX0pJCBjYXB0dXJlIGEgZGVwZW5kw6puY2lhIGRvIGhpc3TDs3JpY28sIGVucXVhbnRvIG8gbW9kZWxvIGkuaS5kLiBhc3N1bWUgcXVlICRQKFhfdCBcXG1pZCBcXG1hdGhjYWx7Rn1fe3QtMX0pID0gUChYX3QpJCwgaWdub3JhbmRvIGEgbWVtw7NyaWEgZG8gc2lzdGVtYS4iLCAiRCI6ICJPIG1vZGVsbyBpLmkuZC4gZXhpZ2UgcXVlIG9zIGRhZG9zIHNlamFtIG7Do28tZXN0YWNpb27DoXJpb3MsIGVucXVhbnRvIGEgbGluZ3VhZ2VtIGh1bWFuYSDDqSBpbnRyaW5zZWNhbWVudGUgZXN0YWNpb27DoXJpYSBlIGRlIHZhcmnDom5jaWEgbnVsYS4iLCAiRSI6ICJPIGVycm8gZGVjb3JyZSBkbyB1c28gZGUgdW1hIGZ1bsOnw6NvIGRlIHZlcm9zc2ltaWxoYW7Dp2EgcXVlIGFzc3VtZSBpbmRlcGVuZMOqbmNpYSwgcXVhbmRvIG5hIHZlcmRhZGUgbyBoaXN0w7NyaWNvICRcXG1hdGhjYWx7Rn1fe3QtMX0kIHJlZHV6IGEgaW5jZXJ0ZXphIGRlICRYX3QkIGF1bWVudGFuZG8gc3VhIGVudHJvcGlhIG3DqWRpYS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIlJlZmxpdGEgc29icmUgYSBkZWZpbmnDp8OjbyBkZSBpbmRlcGVuZMOqbmNpYSB2ZXJzdXMgYSBlc3RydXR1cmEgZGUgY29uZGljaW9uYWxpZGFkZSBlbSBwcm9jZXNzb3MgZXN0b2PDoXN0aWNvcyB0ZW1wb3JhaXMuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGFsdGVybmF0aXZhIGNvcnJldGEgw6kgYSBDLiBBIGVzc8OqbmNpYSBkb3MgbW9kZWxvcyBkZSBsaW5ndWFnZW0gw6kgYSBkZXBlbmTDqm5jaWEgdGVtcG9yYWw6IGEgcHJvYmFiaWxpZGFkZSBkZSB1bSB0b2tlbiBkZXBlbmRlIGRvIGNvbnRleHRvIGFudGVyaW9yLiBPIG1vZGVsbyBpLmkuZC4gcHJlc3N1cMO1ZSBxdWUgbyBoaXN0w7NyaWNvICRcXG1hdGhjYWx7Rn1fe3QtMX0kIG7Do28gZm9ybmVjZSBpbmZvcm1hw6fDo28gYWRpY2lvbmFsIHNvYnJlICRYX3QkLCBvdSBzZWphLCAkUChYX3QgXFxtaWQgXFxtYXRoY2Fse0Z9X3t0LTF9KSA9IFAoWF90KSQuIEFzIGRlbWFpcyBhbHRlcm5hdGl2YXMgZmFsaGFtOiAoQSkgaWdub3JhIHF1ZSBhIGVzcGVyYW7Dp2EgY29uZGljaW9uYWwgdmFyaWEgY29uZm9ybWUgbyBjb250ZXh0bzsgKEIpIGludmVydGUgYSBsw7NnaWNhIGRlIHZhcmnDom5jaWE7IChEKSBpbnZlcnRlIGEgbmF0dXJlemEgZG9zIGRhZG9zIGUgKEUpIGEgZGVwZW5kw6puY2lhIHRlbXBvcmFsIHRpcGljYW1lbnRlIHJlZHV6IGEgaW5jZXJ0ZXphIChlbnRyb3BpYSkgYW8gaW52w6lzIGRlIGF1bWVudMOhLWxhLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtIHByb2Nlc3NvIGF1dG9yZWdyZXNzaXZvIGRlIHByaW1laXJhIG9yZGVtICRYX3QgPSBcXHBoaSBYX3t0LTF9ICsgXFxlcHNpbG9uX3QkLCBvbmRlICRcXGVwc2lsb25fdCQgw6kgdW0gcnXDrWRvIGJyYW5jbyAkTigwLCBcXHNpZ21hXjIpJC4gVW0gYW5hbGlzdGEgZGVzZWphIGNhbGN1bGFyIGEgZXNwZXJhbsOnYSBjb25kaWNpb25hbCBkbyBwcsOzeGltbyBlc3RhZG8gZG8gc2lzdGVtYSBkYWRhIHVtYSBvYnNlcnZhw6fDo28gcmVjZW50ZSAkWF97dC0xfSA9IHhfe3QtMX0kLiBRdWFsIGV4cHJlc3PDo28gZGVzY3JldmUgY29ycmV0YW1lbnRlIGVzc2EgZXN0aW1hdGl2YT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkVbWF90IFxcbWlkIFhfe3QtMX1dID0gXFxwaGkgeF97dC0xfSArIFxcc2lnbWEiLCAiQiI6ICJFW1hfdCBcXG1pZCBYX3t0LTF9XSA9IFxccGhpIHhfe3QtMX0iLCAiQyI6ICJFW1hfdCBcXG1pZCBYX3t0LTF9XSA9IFxccGhpIEVbWF97dC0xfV0iLCAiRCI6ICJFW1hfdCBcXG1pZCBYX3t0LTF9XSA9IHhfe3QtMX0gKyBcXHBoaSBcXHNpZ21hXjIiLCAiRSI6ICJFW1hfdCBcXG1pZCBYX3t0LTF9XSA9IDAifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkFwbGlxdWUgbyBvcGVyYWRvciBkZSBlc3BlcmFuw6dhIGNvbmRpY2lvbmFsIGVtIGFtYm9zIG9zIGxhZG9zIGRhIGVxdWHDp8OjbywgbGVtYnJhbmRvIHF1ZSAkRVtcXGVwc2lsb25fdCBcXG1pZCBYX3t0LTF9XSA9IEVbXFxlcHNpbG9uX3RdID0gMCQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGFsdGVybmF0aXZhIGNvcnJldGEgw6kgYSBCLiBVdGlsaXphbmRvIGEgbGluZWFyaWRhZGUgZGEgZXNwZXJhbsOnYTogJEVbWF90IFxcbWlkIFhfe3QtMX1dID0gRVtcXHBoaSBYX3t0LTF9ICsgXFxlcHNpbG9uX3QgXFxtaWQgWF97dC0xfV0gPSBcXHBoaSBYX3t0LTF9ICsgRVtcXGVwc2lsb25fdCBcXG1pZCBYX3t0LTF9XSQuIENvbW8gbyBydcOtZG8gJFxcZXBzaWxvbl90JCDDqSBpbmRlcGVuZGVudGUgZGUgJFhfe3QtMX0kIGUgdGVtIG3DqWRpYSB6ZXJvLCAkRVtcXGVwc2lsb25fdCBcXG1pZCBYX3t0LTF9XSA9IDAkLiBQb3J0YW50bywgJEVbWF90IFxcbWlkIFhfe3QtMX1dID0gXFxwaGkgeF97dC0xfSQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSBtb2RlbG9zIGRlIGxpbmd1YWdlbSBiYXNlYWRvcyBlbSB0cmFuc2Zvcm1hZG9yZXMsIG9zIHZldG9yZXMgZGUgcmVwcmVzZW50YcOnw6NvIChlbWJlZGRpbmdzKSBkZSBwYWxhdnJhcyByZXNpZGVtIGVtIGVzcGHDp29zIGxhdGVudGVzIGRlIGRpbWVuc8OjbyAkayA9IDUxMiQuIENvbnNpZGVyZSB1bSBleHBlcmltZW50byBvbmRlIGV4dHJhw61tb3MgJG4gPSAxMDAwJCBhbW9zdHJhcyBpbmRlcGVuZGVudGVzIGRlIHZldG9yZXMgZGUgY2FyYWN0ZXLDrXN0aWNhcyAkXFx1bmRlcmxpbmV7WH1fMSwgXFx1bmRlcmxpbmV7WH1fMiwgXFxkb3RzLCBcXHVuZGVybGluZXtYfV9uJCBkZSB1bSBjb3JwdXMgZGUgdHJlaW5hbWVudG8sIGNvbSB2ZXRvciBkZSBtw6lkaWFzIHBvcHVsYWNpb25haXMgJFxcbXUkIGUgbWF0cml6IGRlIGNvdmFyacOibmNpYSAkXFxTaWdtYSQuIERlIGFjb3JkbyBjb20gbyBUZW9yZW1hIENlbnRyYWwgZG8gTGltaXRlIE11bHRpdmFyaWFkbywgcXVhbCDDqSBvIGNvbXBvcnRhbWVudG8gYXNzaW50w7N0aWNvIGRvIHZldG9yIGRlIG3DqWRpYXMgYW1vc3RyYWlzICRcXGJhcntYfV9uID0gXFxmcmFjezF9e259IFxcc3VtX3tpPTF9Xm4gXFx1bmRlcmxpbmV7WH1faSQgcGFyYSB1bSAkbiQgZ3JhbmRlPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyB2ZXRvciBkZSBtw6lkaWFzIGFtb3N0cmFpcyBjb252ZXJnZSBwYXJhIHVtYSBkaXN0cmlidWnDp8OjbyBjb25zdGFudGUgJFxcbXUkIGNvbSB2YXJpw6JuY2lhIHplcm8uIiwgIkIiOiAiJFxcc3FydHtufShcXGJhcntYfV9uIC0gXFxtdSkgXFx4cmlnaHRhcnJvd3tEfSBOKDAsIFxcU2lnbWEpJCwgb25kZSAkTigwLCBcXFNpZ21hKSQgw6kgYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgbXVsdGl2YXJpYWRhLiIsICJDIjogIk8gdmV0b3IgZGUgbcOpZGlhcyBhbW9zdHJhaXMgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIFF1aS1RdWFkcmFkbyBjb20gJGskIGdyYXVzIGRlIGxpYmVyZGFkZS4iLCAiRCI6ICIkXFxzcXJ0e259KFxcYmFye1h9X24gLSBcXG11KSBcXHhyaWdodGFycm93e0R9IHQobi0xLCBcXFNpZ21hKSQsIGluZGljYW5kbyBxdWUgYSBjYXVkYSBkYSBkaXN0cmlidWnDp8OjbyDDqSBtYWlzIHBlc2FkYSBkZXZpZG8gw6AgYWx0YSBkaW1lbnNpb25hbGlkYWRlLiIsICJFIjogIk8gdmV0b3IgZGUgbcOpZGlhcyBhbW9zdHJhaXMgbsOjbyBjb252ZXJnZSBkZXZpZG8gw6AgbWFsZGnDp8OjbyBkYSBkaW1lbnNpb25hbGlkYWRlIGVtIGVzcGHDp29zIGRlIGFsdGEgZGltZW5zw6NvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiUmVjb3JkZSBxdWUgbyBUQ0wgTXVsdGl2YXJpYWRvIGdhcmFudGUgcXVlLCBzb2IgY29uZGnDp8O1ZXMgZGUgaW5kZXBlbmTDqm5jaWEgZSB2YXJpw6JuY2lhIGZpbml0YSwgYSBtw6lkaWEgYW1vc3RyYWwgZGV2aWRhbWVudGUgZXNjYWxvbmFkYSBjb252ZXJnZSBwYXJhIHVtYSBmb3JtYSBlc3BlY8OtZmljYSBkZSBkaXN0cmlidWnDp8OjbyBnYXVzc2lhbmEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGFsdGVybmF0aXZhIEIgZXN0w6EgY29ycmV0YS4gTyBUZW9yZW1hIENlbnRyYWwgZG8gTGltaXRlIE11bHRpdmFyaWFkbyBlc3RhYmVsZWNlIHF1ZSBwYXJhIHZldG9yZXMgYWxlYXTDs3Jpb3MgaS5pLmQuLCBhIG3DqWRpYSBhbW9zdHJhbCwgYXDDs3MgbyBlc2NhbG9uYW1lbnRvIHBlbG8gZmF0b3IgJFxcc3FydHtufSQsIGNvbnZlcmdlIGVtIGRpc3RyaWJ1acOnw6NvIHBhcmEgYSBOb3JtYWwgbXVsdGl2YXJpYWRhIGNvbSBtw6lkaWEgbnVsYSBlIG1hdHJpeiBkZSBjb3ZhcmnDom5jaWEgaWd1YWwgw6AgY292YXJpw6JuY2lhIG9yaWdpbmFsIGRvcyB2ZXRvcmVzLiBBIGFsdGVybmF0aXZhIEMgw6kgdW0gZXJybyBjb211bSwgcG9pcyBvIFF1aS1RdWFkcmFkbyBkZXNjcmV2ZSBzb21hcyBkZSBxdWFkcmFkb3MgZGUgbm9ybWFpcywgbsOjbyBhIG3DqWRpYS4gQSBhbHRlcm5hdGl2YSBEIGNvbmZ1bmRlIG8gY29tcG9ydGFtZW50byBhc3NpbnTDs3RpY28gKE5vcm1hbCkgY29tIG8gY29tcG9ydGFtZW50byBhbW9zdHJhbCBwYXJhIGFtb3N0cmFzIHBlcXVlbmFzICh0IGRlIFN0dWRlbnQpLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpOyBmaWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1ucC5yYW5kb20ubXVsdGl2YXJpYXRlX25vcm1hbChbMCwwXSwgW1sxLCAwLjVdLCBbMC41LCAxXV0sIDUwMClbOiwwXSwgeT1ucC5yYW5kb20ubXVsdGl2YXJpYXRlX25vcm1hbChbMCwwXSwgW1sxLCAwLjVdLCBbMC41LCAxXV0sIDUwMClbOiwxXSwgbW9kZT0nbWFya2VycycsIG5hbWU9J0Ftb3N0cmFzJywgbWFya2VyPWRpY3QoY29sb3I9JyMwRjE3MkEnLCBvcGFjaXR5PTAuNSkpKTsgZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0NvbnZlcmfDqm5jaWEgbm8gRXNwYcOnbyBMYXRlbnRlJywgeGF4aXNfdGl0bGU9J0RpbWVuc8OjbyAxJywgeWF4aXNfdGl0bGU9J0RpbWVuc8OjbyAyJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpOyIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIk5vIG1lY2FuaXNtbyBkZSBhdGVuw6fDo28gKCdTY2FsZWQgRG90LVByb2R1Y3QgQXR0ZW50aW9uJyksIGEgcmVsZXbDom5jaWEgZW50cmUgdG9rZW5zIMOpIGNhbGN1bGFkYSB2aWEgcHJvZHV0byBlc2NhbGFyLiBFbSBlc3Bhw6dvcyBkZSBhbHRhIGRpbWVuc8OjbywgYSBtYWduaXR1ZGUgZGVzc2UgcHJvZHV0byBlc2NhbGFyIGRlcGVuZGUgZGlyZXRhbWVudGUgZGEgZXN0cnV0dXJhIGRhIG1hdHJpeiBkZSBjb3ZhcmnDom5jaWEgJFxcU2lnbWEkIGRhcyByZXByZXNlbnRhw6fDtWVzLiBTZSBhcyBkaW1lbnPDtWVzIGRlIHVtIHZldG9yIGZvcmVtIGluZGVwZW5kZW50ZXMgZSBjb20gdmFyacOibmNpYSB1bml0w6FyaWEsIGNvbW8gc2UgY29tcG9ydGEgYSBub3JtYSBkbyBwcm9kdXRvIGVzY2FsYXIgZW50cmUgZG9pcyB2ZXRvcmVzIGRlIGRpbWVuc8OjbyAkayQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIG5vcm1hIHBlcm1hbmVjZSBjb25zdGFudGUsIGluZGVwZW5kZW50ZW1lbnRlIGRlICRrJC4iLCAiQiI6ICJBIG5vcm1hIGNyZXNjZSBwcm9wb3JjaW9uYWxtZW50ZSBhICRcXHNxcnR7a30kLCBleGlnaW5kbyB1bSBmYXRvciBkZSBlc2NhbGEgcGFyYSBldml0YXIgYSBzYXR1cmHDp8OjbyBkYXMgZnVuw6fDtWVzIGRlIGF0aXZhw6fDo28uIiwgIkMiOiAiQSBub3JtYSBkZWNyZXNjZSBleHBvbmVuY2lhbG1lbnRlIGNvbSAkayQgZGV2aWRvIMOgIGRpc3BlcnPDo28gZG9zIGRhZG9zLiIsICJEIjogIkEgbm9ybWEgdG9ybmEtc2UgbmVnYXRpdmEsIHBvaXMgb3MgdmV0b3JlcyBlbSBhbHRhIGRpbWVuc8OjbyB0ZW5kZW0gYSBzZXIgb3J0b2dvbmFpcy4iLCAiRSI6ICJBIG5vcm1hIG7Do28gw6kgZGVmaW5pZGEgcGFyYSB2ZXRvcmVzIGVtIGVzcGHDp29zIGRlIGRpbWVuc8OjbyBtYWlvciBxdWUgMTAwLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiQ29uc2lkZXJlIG8gZWZlaXRvIGRhIHNvbWEgZGUgdmFyacOhdmVpcyBhbGVhdMOzcmlhcyBpbmRlcGVuZGVudGVzIHNvYnJlIGEgdmFyacOibmNpYSB0b3RhbCBhbyBjYWxjdWxhciBvIHByb2R1dG8gZXNjYWxhciBlbSBhbHRhIGRpbWVuc8Ojby4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgYWx0ZXJuYXRpdmEgQiDDqSBhIGNvcnJldGEuIEVtIGVzcGHDp29zIGRlIGFsdGEgZGltZW5zw6NvICRrJCwgbyBwcm9kdXRvIGVzY2FsYXIgZW50cmUgZG9pcyB2ZXRvcmVzIGFsZWF0w7NyaW9zIHRlbmRlIGEgdGVyIHVtYSB2YXJpw6JuY2lhIHF1ZSBjcmVzY2UgY29tICRrJC4gU2VtIG8gZmF0b3IgZGUgZXNjYWxhIChjb211bWVudGUgJFxcZnJhY3sxfXtcXHNxcnR7ZF9rfX0kIG5vIG1lY2FuaXNtbyBkZSBhdGVuw6fDo28pLCBvcyB2YWxvcmVzIGRlIGVudHJhZGEgcGFyYSBhIGZ1bsOnw6NvIHNvZnRtYXggc2VyaWFtIGV4Y2Vzc2l2YW1lbnRlIGdyYW5kZXMsIGxldmFuZG8gbyBncmFkaWVudGUgYSByZWdpw7VlcyBkZSBzYXR1cmHDp8OjbyBvbmRlIG8gYXByZW5kaXphZG8gw6kgaW5pYmlkby4gQXMgb3V0cmFzIGFsdGVybmF0aXZhcyBpZ25vcmFtIGEgbmF0dXJlemEgZXN0YXTDrXN0aWNhIGRhIHZhcmlhYmlsaWRhZGUgZG8gcHJvZHV0byBlc2NhbGFyIGVtIGFsdGEgZGltZW5zw6NvLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRHVyYW50ZSBvIHRyZWluYW1lbnRvIGRlIHVtIG1vZGVsbyBkZSBsaW5ndWFnZW0gZW0gZXNjYWxhIG1hc3NpdmEsIG1vbml0b3JhbW9zIGEgZGlmZXJlbsOnYSBlbnRyZSBhIHBlcmRhIGRlIHRyZWluYW1lbnRvIGUgYSBwZXJkYSBkZSB2YWxpZGHDp8OjbywgZGVub3RhZGEgcG9yIHVtYSBzZXF1w6puY2lhIGRlIHZhcmnDoXZlaXMgYWxlYXTDs3JpYXMgJFhfaSQgY29tIG3DqWRpYSAkRVtYX2ldID0gMCQgZSB2YXJpw6JuY2lhIGZpbml0YSAkXFxzaWdtYV4yID0gMC4wMiQuIFBhcmEgZ2FyYW50aXIgYSBlc3RhYmlsaWRhZGUgZG8gbW9kZWxvIGFww7NzICRuID0gNTAwJCBwYXNzb3MgZGUgcHJvY2Vzc2FtZW50byBkZSB0b2tlbnMsIGRlc2VqYW1vcyBjb250cm9sYXIgYSBzb21hIGFjdW11bGFkYSAkU19rID0gXFxzdW1fe2k9MX1ee2t9IFhfaSQuIFV0aWxpemFuZG8gYSBEZXNpZ3VhbGRhZGUgZGUgS29sbW9nb3JvdiwgcXVhbCDDqSBvIGxpbWl0ZSBzdXBlcmlvciBwYXJhIGEgcHJvYmFiaWxpZGFkZSBkZSBxdWUgbyBkZXN2aW8gbcOheGltbyBhYnNvbHV0byBkYSBzb21hIGFjdW11bGFkYSBleGNlZGEgbyBsaW1pYXIgJFxcbGFtYmRhID0gNCQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIwLjEyNSIsICJCIjogIjAuMjUwIiwgIkMiOiAiMC41MDAiLCAiRCI6ICIwLjYyNSIsICJFIjogIjAuMDYyNSJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJEIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBhIHZhcmnDom5jaWEgZGEgc29tYSBkZSB2YXJpw6F2ZWlzIGluZGVwZW5kZW50ZXMgJFNfbiQgw6kgYSBzb21hIGRhcyB2YXJpw6JuY2lhcywgb3Ugc2VqYSwgJFZhcihTX24pID0gblxcc2lnbWFeMiQuIEFwbGlxdWUgYSBmw7NybXVsYSBkYSBEZXNpZ3VhbGRhZGUgZGUgS29sbW9nb3JvdjogJFAoXFxtYXggfFNfa3wgXFxnZSBcXGxhbWJkYSkgXFxsZSBcXGZyYWN7VmFyKFNfbil9e1xcbGFtYmRhXjJ9JC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgRGVzaWd1YWxkYWRlIGRlIEtvbG1vZ29yb3YgZXN0YWJlbGVjZSBxdWUgJFAoXFxtYXhfezEgXFxsZSBrIFxcbGUgbn0gfFNfa3wgXFxnZSBcXGxhbWJkYSkgXFxsZSBcXGZyYWN7VmFyKFNfbil9e1xcbGFtYmRhXjJ9JC4gRGFkbyBxdWUgJG4gPSA1MDAkIGUgJFxcc2lnbWFeMiA9IDAuMDIkLCB0ZW1vcyAkVmFyKFNfbikgPSA1MDAgXFx0aW1lcyAwLjAyID0gMTAkLiBDb20gJFxcbGFtYmRhID0gNCQsIG8gbGltaXRlIMOpICRcXGZyYWN7MTB9ezReMn0gPSBcXGZyYWN7MTB9ezE2fSA9IDAuNjI1JC4gQWx0ZXJuYXRpdmEgQSBjb25mdW5kZSBvIGRlbm9taW5hZG9yOyBCIGlnbm9yYSBvIHRhbWFuaG8gZGEgYW1vc3RyYTsgQyDDqSB1bSBlcnJvIGRlIGPDoWxjdWxvIGVzY2FsYXIgY29tdW0uIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVsxLCAyLCAzLCA0XSwgeT1bMSwgMC41LCAwLjI1LCAwLjYyNV0sIG1vZGU9J2xpbmVzK21hcmtlcnMnLCBuYW1lPSdMaW1pdGUgS29sbW9nb3JvdicpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0xpbWl0ZSBkZSBFc3RhYmlsaWRhZGUnLCB4YXhpc190aXRsZT0nTGltaWFyIChcXGxhbWJkYSknLCB5YXhpc190aXRsZT0nUHJvYmFiaWxpZGFkZSBMaW1pdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkEgTGVpIGRvcyBHcmFuZGVzIE7Dum1lcm9zIChMR04pIMOpIGZ1bmRhbWVudGFsIHBhcmEgYSBjb252ZXJnw6puY2lhIGRlIGRlc2VtcGVuaG8gZW0gTExNcy4gU2UgYSBtw6lkaWEgYW1vc3RyYWwgZGUgdW0gaW5kaWNhZG9yIGRlIGRlc2VtcGVuaG8gKGNvbW8gYSBwZXJwbGV4aWRhZGUpIGNvbnZlcmdlIHBhcmEgYSBtw6lkaWEgcG9wdWxhY2lvbmFsIMOgIG1lZGlkYSBxdWUgbyBuw7ptZXJvIGRlIHRva2VucyBwcm9jZXNzYWRvcyBhdW1lbnRhLCBxdWUgdGlwbyBkZSBjb252ZXJnw6puY2lhIGVzdGFtb3Mgb2JzZXJ2YW5kbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkNvbnZlcmfDqm5jaWEgZW0gZGlzdHJpYnVpw6fDo28sIGdhcmFudGluZG8gcXVlIGEgbcOpZGlhIHNlamEgZXhhdGFtZW50ZSBhIG3DqWRpYSBwb3B1bGFjaW9uYWwgcGFyYSBxdWFscXVlciBuLiIsICJCIjogIkNvbnZlcmfDqm5jaWEgZW0gcHJvYmFiaWxpZGFkZSwgb25kZSBhIHByb2JhYmlsaWRhZGUgZGUgbyBkZXN2aW8gZGEgbcOpZGlhIGFtb3N0cmFsIHNlciBtYWlvciBxdWUgcXVhbHF1ZXIgJFxcZXBzaWxvbiA+IDAkIHRlbmRlIGEgemVyby4iLCAiQyI6ICJDb252ZXJnw6puY2lhIHF1YXNlIGNlcnRhLCBxdWUgw6kgbWFpcyBmcmFjYSBxdWUgYSBjb252ZXJnw6puY2lhIGVtIHByb2JhYmlsaWRhZGUuIiwgIkQiOiAiQ29udmVyZ8OqbmNpYSBlbSBtw6lkaWEgcXVhZHLDoXRpY2EsIHF1ZSBhcGVuYXMgb2NvcnJlIHNlIGEgdmFyacOibmNpYSBmb3IgaW5maW5pdGEuIiwgIkUiOiAiQ29udmVyZ8OqbmNpYSBlbSB2YXJpw6JuY2lhLCBxdWUgZGVzY3JldmUgY29tbyBvIGVycm8gYXVtZW50YSBsaW5lYXJtZW50ZSBjb20gbi4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkEgTGVpIEZyYWNhIGRvcyBHcmFuZGVzIE7Dum1lcm9zIGFmaXJtYSBxdWUgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBjb252ZXJnZSBlbSBwcm9iYWJpbGlkYWRlIHBhcmEgYSBtw6lkaWEgcG9wdWxhY2lvbmFsICRcXG11JC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgTGVpIEZyYWNhIGRvcyBHcmFuZGVzIE7Dum1lcm9zIGVzdGFiZWxlY2UgcXVlIHBhcmEgdG9kbyAkXFxlcHNpbG9uID4gMCQsICRQKHxcXGJhcntYfSAtIFxcbXV8IFxcZ2UgXFxlcHNpbG9uKSBcXHRvIDAkIGNvbmZvcm1lICRuIFxcdG8gXFxpbmZ0eSQuIEEgYWx0ZXJuYXRpdmEgQSBlc3TDoSBpbmNvcnJldGEgcG9pcyBhIGRpc3RyaWJ1acOnw6NvIG7Do28gcHJlY2lzYSBzZXIgYSBtZXNtYTsgQyBlc3TDoSBlcnJhZGEgcG9ycXVlIGEgY29udmVyZ8OqbmNpYSBxdWFzZSBjZXJ0YSDDqSBtYWlzIGZvcnRlLCBuw6NvIG1haXMgZnJhY2E7IEQgZXN0w6EgZXJyYWRhIHBvaXMgcmVxdWVyIHZhcmnDom5jaWEgZmluaXRhOyBFIMOpIGNvbmNlaXR1YWxtZW50ZSBvcG9zdGEgYW8gb2JqZXRpdm8gZGUgZXN0YWJpbGlkYWRlLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gbW9kZWxvIGRlIGxpbmd1YWdlbSByZWR1emlkbywgbyB2b2NhYnVsw6FyaW8gJFYkIGNvbnTDqW0gJEs9MyQgdG9rZW5zIChBLCBCLCBDKS4gQXDDs3MgbyBwcm9jZXNzYW1lbnRvIGRhIGNhbWFkYSBkZW5zYSwgb3MgbG9naXRzIGRlIHNhw61kYSBwYXJhIGEgcHLDs3hpbWEgcG9zacOnw6NvIHPDo28gJHpfMT0yLjAkLCAkel8yPTEuMCQgZSAkel8zPTAuMCQuIENvbnNpZGVyYW5kbyBxdWUgYSBwcm9iYWJpbGlkYWRlIGRlIGNhZGEgdG9rZW4gw6kgZGVmaW5pZGEgcGVsYSBmdW7Dp8OjbyBzb2Z0bWF4ICRwX2kgPSBcXGZyYWN7XFxleHAoel9pKX17XFxzdW1fe2o9MX1eMyBcXGV4cCh6X2opfSQsIHF1YWwgw6kgbyB2YWxvciBhcHJveGltYWRvIGRhIHByb2JhYmlsaWRhZGUgZGUgb2NvcnLDqm5jaWEgZG8gdG9rZW4gQT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjAuMzMiLCAiQiI6ICIwLjY2IiwgIkMiOiAiMC4yNCIsICJEIjogIjAuNzEiLCAiRSI6ICIwLjEwIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJDYWxjdWxlIGEgZXhwb25lbmNpYWwgZGUgY2FkYSBsb2dpdCBwcmltZWlybyBlIGRlcG9pcyBub3JtYWxpemUgcGVsbyBzb21hdMOzcmlvIHRvdGFsIGRhcyBleHBvbmVuY2lhaXMuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGZ1bsOnw6NvIHNvZnRtYXggw6kgZGFkYSBwb3IgJHBfaSA9IFxcZnJhY3tlXnt6X2l9fXtcXHN1bSBlXnt6X2p9fSQuIENhbGN1bGFuZG8gb3MgdmFsb3JlczogJGVeezIuMH0gXFxhcHByb3ggNy4zODkkLCAkZV57MS4wfSBcXGFwcHJveCAyLjcxOCQgZSAkZV57MC4wfSA9IDEuMCQuIE8gc29tYXTDs3JpbyDDqSAkNy4zODkgKyAyLjcxOCArIDEuMCA9IDExLjEwNyQuIEEgcHJvYmFiaWxpZGFkZSBwYXJhIG8gdG9rZW4gQSDDqSAkcF8xID0gNy4zODkgLyAxMS4xMDcgXFxhcHByb3ggMC42NjUkLiBBbHRlcm5hdGl2YXMgaW5jb3JyZXRhcyBjb21vIEMgKDAuMjQpIHJlc3VsdGFtIGRlIGVycm9zIG5hIG5vcm1hbGl6YcOnw6NvIG91IGVycm8gZGUgY8OhbGN1bG8gbmEgc29tYSBkYXMgZXhwb25lbmNpYWlzLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZShkYXRhPVtnby5CYXIoeD1bJ0EnLCAnQicsICdDJ10sIHk9WzAuNjY1LCAwLjI0NSwgMC4wOTBdLCBtYXJrZXJfY29sb3I9JyMwRjE3MkEnKV0pXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nRGlzdHJpYnVpw6fDo28gZGUgUHJvYmFiaWxpZGFkZSB2aWEgU29mdG1heCcsIHhheGlzX3RpdGxlPSdUb2tlbnMnLCB5YXhpc190aXRsZT0nUHJvYmFiaWxpZGFkZSAoJHBfaSQpJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJBIGVudHJvcGlhIGRlIFNoYW5ub24gJEgoWCkkIG1lZGUgYSBpbmNlcnRlemEgZXNwZXJhZGEgZGUgdW1hIHZhcmnDoXZlbCBhbGVhdMOzcmlhIGRpc2NyZXRhLiBEYWRvIHVtIG1vZGVsbyBjb20gZGlzdHJpYnVpw6fDo28gY2F0ZWfDs3JpY2EgZGUgNCB0b2tlbnMgY29tIHByb2JhYmlsaWRhZGVzICRwID0gWzAuNSwgMC4yNSwgMC4xMjUsIDAuMTI1XSQsIGRldGVybWluZSBvIHZhbG9yIGRlICRIKFgpID0gLVxcc3VtX3tpPTF9XksgcF9pIFxcbG9nXzIocF9pKSQgZW0gYml0cy4iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjEuNzUgYml0cyIsICJCIjogIjIuMDAgYml0cyIsICJDIjogIjEuNTAgYml0cyIsICJEIjogIjEuMjUgYml0cyIsICJFIjogIjAuNzUgYml0cyJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSAkXFxsb2dfMih4KSQgw6kgbyBsb2dhcml0bW8gbmEgYmFzZSAyLiBDYWxjdWxlICQtXFxzdW0gcF9pIFxcbG9nXzIocF9pKSQgdGVybW8gYSB0ZXJtby4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIiRIKFgpID0gLSgwLjUgXFxjZG90IFxcbG9nXzIoMC41KSArIDAuMjUgXFxjZG90IFxcbG9nXzIoMC4yNSkgKyAwLjEyNSBcXGNkb3QgXFxsb2dfMigwLjEyNSkgKyAwLjEyNSBcXGNkb3QgXFxsb2dfMigwLjEyNSkpJC4gQ29tbyAkXFxsb2dfMigwLjUpPS0xJCwgJFxcbG9nXzIoMC4yNSk9LTIkIGUgJFxcbG9nXzIoMC4xMjUpPS0zJDogJEgoWCkgPSAtKDAuNSBcXGNkb3QgLTEgKyAwLjI1IFxcY2RvdCAtMiArIDAuMTI1IFxcY2RvdCAtMyArIDAuMTI1IFxcY2RvdCAtMykgPSAtKC0wLjUgLSAwLjUgLSAwLjM3NSAtIDAuMzc1KSA9IDEuNzUkIGJpdHMuIEFsdGVybmF0aXZhcyBpbmNvcnJldGFzIGRlY29ycmVtIGRlIGVycm9zIGRlIGFyaXRtw6l0aWNhIG5vIHNvbWF0w7NyaW8gZG9zIGxvZ3MgcG9uZGVyYWRvcy4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH1dLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbeyJlbnVuY2lhZG8iOiAiRW0gdW1hIHPDqXJpZSB0ZW1wb3JhbCBkZSBzZW5zb3JlcyBpbmR1c3RyaWFpcywgb2JzZXJ2YS1zZSBxdWUgYSB0ZW1wZXJhdHVyYSAkWF90JCBzZWd1ZSB1bSBwcm9jZXNzbyBhdXRvcmVncmVzc2l2byAkWF90ID0gMC44IFhfe3QtMX0gKyBcXGVwc2lsb25fdCQsIGNvbSAkXFxlcHNpbG9uX3QgXFxzaW0gTigwLCAwLjI1KSQuIChhKSBEZWZpbmEgYSBlc3BlcmFuw6dhIGNvbmRpY2lvbmFsICRFW1hfdCBcXG1pZCBYX3t0LTF9XSQuIChiKSBTZSBubyBpbnN0YW50ZSAkdC0xJCBvIHNlbnNvciBtYXJjb3UgJDEwLjBee1xcY2lyY31DJCwgcXVhbCDDqSBhIHByZXZpc8OjbyBwYXJhIG8gcHLDs3hpbW8gaW5zdGFudGUgJHQkPyAoYykgRGlzY3V0YSBjb21vIGEgdmFyacOibmNpYSBkbyBydcOtZG8gaW5mbHVlbmNpYSBhIGluY2VydGV6YSBkYSBwcmV2aXPDo28uIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGxpbmVhcmlkYWRlIGRhIGVzcGVyYW7Dp2EgZSBxdWUgYSBwcmV2aXPDo28gw7N0aW1hIGVtIG1vZGVsb3MgbGluZWFyZXMgw6kgYSBlc3BlcmFuw6dhIGNvbmRpY2lvbmFsLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBIGVzcGVyYW7Dp2EgY29uZGljaW9uYWwgw6kgJEVbWF90IFxcbWlkIFhfe3QtMX1dID0gRVswLjggWF97dC0xfSArIFxcZXBzaWxvbl90IFxcbWlkIFhfe3QtMX1dID0gMC44IFhfe3QtMX0gKyBFW1xcZXBzaWxvbl90XSQuIiwgIkNvbW8gJEVbXFxlcHNpbG9uX3RdID0gMCQsIHRlbW9zICRFW1hfdCBcXG1pZCBYX3t0LTF9XSA9IDAuOCBYX3t0LTF9JC4iLCAiUGFyYSAkWF97dC0xfSA9IDEwLjAkLCBhIHByZXZpc8OjbyDDqSAkMC44IFxcdGltZXMgMTAuMCA9IDguMF57XFxjaXJjfUMkLiIsICJBIGluY2VydGV6YSDDqSBkYWRhIHBlbGEgdmFyacOibmNpYSBjb25kaWNpb25hbCAkVmFyW1hfdCBcXG1pZCBYX3t0LTF9XSA9IFZhcltcXGVwc2lsb25fdF0gPSAwLjI1JC4gUXVhbnRvIG1haW9yIGEgdmFyacOibmNpYSBkbyBydcOtZG8sIG1haW9yIG8gaW50ZXJ2YWxvIGRlIHByZWRpw6fDo28gZW0gdG9ybm8gZGEgbcOpZGlhLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueF92YWxzID0gbnAubGluc3BhY2UoMCwgMjAsIDEwMClcbnlfdmFscyA9IDAuOCAqIHhfdmFsc1xuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eF92YWxzLCB5PXlfdmFscywgbmFtZT1yJ1ByZXZpc8OjbyBFW1hfdCB8IFhfe3QtMX1dJywgbGluZT1kaWN0KGNvbG9yPScjMEYxNzJBJywgd2lkdGg9MykpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J1ByZXZpc8OjbyBMaW5lYXIgZG8gU2Vuc29yJywgeGF4aXNfdGl0bGU9J1RlbXBlcmF0dXJhIFhfe3QtMX0nLCB5YXhpc190aXRsZT0nUHJldmlzw6NvIEVbWF90XScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogOC4wfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtIG1vZGVsbyBhdXRvcmVncmVzc2l2byAkWF90ID0gXFxwaGkgWF97dC0xfSArIFxcZXBzaWxvbl90JC4gKGEpIERlZHV6YSBhIHZhcmnDom5jaWEgZGUgJFhfdCQgYXNzdW1pbmRvIGVzdGFjaW9uYXJpZGFkZSAoJFZhcltYX3RdID0gVmFyW1hfe3QtMX1dID0gXFxzaWdtYV9YXjIkKS4gKGIpIFNlICRcXHBoaSA9IDAuNSQgZSAkXFxzaWdtYV97XFxlcHNpbG9ufV4yID0gMC43NSQsIGNhbGN1bGUgJFxcc2lnbWFfWF4yJC4iLCAiZGljYSI6ICJVc2UgYSBwcm9wcmllZGFkZSAkVmFyKGFYICsgWSkgPSBhXjIgVmFyKFgpICsgVmFyKFkpJCBwYXJhIHZhcmnDoXZlaXMgaW5kZXBlbmRlbnRlcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFydGluZG8gZGEgZXN0YWNpb25hcmlkYWRlLCAkVmFyKFhfdCkgPSBWYXIoXFxwaGkgWF97dC0xfSArIFxcZXBzaWxvbl90KSA9IFxccGhpXjIgVmFyKFhfe3QtMX0pICsgVmFyKFxcZXBzaWxvbl90KSQuIiwgIlN1YnN0aXR1aW5kbyAkXFxzaWdtYV9YXjIgPSBcXHBoaV4yIFxcc2lnbWFfWF4yICsgXFxzaWdtYV97XFxlcHNpbG9ufV4yJC4iLCAiSXNvbGFuZG8gYSB2YXJpw6JuY2lhOiAkXFxzaWdtYV9YXjIgKDEgLSBcXHBoaV4yKSA9IFxcc2lnbWFfe1xcZXBzaWxvbn1eMiBcXGltcGxpZXMgXFxzaWdtYV9YXjIgPSBcXGZyYWN7XFxzaWdtYV97XFxlcHNpbG9ufV4yfXsxIC0gXFxwaGleMn0kLiIsICJTdWJzdGl0dWluZG8gb3MgdmFsb3JlczogJFxcc2lnbWFfWF4yID0gXFxmcmFjezAuNzV9ezEgLSAwLjVeMn0gPSBcXGZyYWN7MC43NX17MSAtIDAuMjV9ID0gXFxmcmFjezAuNzV9ezAuNzV9ID0gMS4wJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDEuMH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGNlbsOhcmlvIGRlIG1vZGVsYWdlbSBkZSBsaW5ndWFnZW0sIG8gb2JqZXRpdm8gw6kgbWF4aW1pemFyIGEgdmVyb3NzaW1pbGhhbsOnYSBkZSB1bWEgc2VxdcOqbmNpYSAkeF8xLCBcXGRvdHMsIHhfbiQuIChhKSBFc2NyZXZhIGEgcHJvYmFiaWxpZGFkZSBjb25qdW50YSBkYSBzZXF1w6puY2lhIGNvbW8gcHJvZHV0byBkZSBjb25kaWNpb25haXMgJFAoWF8xLCBcXGRvdHMsIFhfbikgPSBcXHByb2QgUChYX3QgXFxtaWQgXFxtYXRoY2Fse0Z9X3t0LTF9KSQuIChiKSBTZSBvIG1vZGVsbyBmb3IgaS5pLmQuLCBjb21vIGVzc2EgZXhwcmVzc8OjbyBzZSBzaW1wbGlmaWNhPyAoYykgRXhwbGlxdWUgcG9yIHF1ZSBhIGRlcGVuZMOqbmNpYSBkZSAkXFxtYXRoY2Fse0Z9X3t0LTF9JCDDqSBjcnVjaWFsIHBhcmEgY2FwdHVyYXIgYSBncmFtw6F0aWNhLiIsICJkaWNhIjogIlV0aWxpemUgYSByZWdyYSBkYSBjYWRlaWEgcGFyYSBkaXN0cmlidWnDp8O1ZXMgY29uanVudGFzLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQZWxhIHJlZ3JhIGRhIGNhZGVpYTogJFAoWF8xLCBcXGRvdHMsIFhfbikgPSBQKFhfMSkgUChYXzIgXFxtaWQgWF8xKSBQKFhfMyBcXG1pZCBYXzEsIFhfMikgXFxkb3RzIFAoWF9uIFxcbWlkIFhfMSwgXFxkb3RzLCBYX3tuLTF9KSQuIiwgIlNlIGZvciBpLmkuZC4sICRQKFhfdCBcXG1pZCBYXzEsIFxcZG90cywgWF97dC0xfSkgPSBQKFhfdCkkLCBsb2dvICRQKFhfMSwgXFxkb3RzLCBYX24pID0gXFxwcm9kX3t0PTF9Xm4gUChYX3QpJC4iLCAiQSBkZXBlbmTDqm5jaWEgZGUgJFxcbWF0aGNhbHtGfV97dC0xfSQgw6kgY3J1Y2lhbCBwb2lzIGEgZ3JhbcOhdGljYSDDqSB1bWEgZXN0cnV0dXJhIHNlcXVlbmNpYWwgb25kZSBhIHBvc2nDp8OjbyBlIG8gc2lnbmlmaWNhZG8gZG8gdG9rZW4gYXR1YWwgZGVwZW5kZW0gZXN0cml0YW1lbnRlIGRvIGNvbnRleHRvIHByZWNlZGVudGUgKHN1amVpdG8sIHZlcmJvLCBjb25jb3Jkw6JuY2lhKS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgdW0gc2lzdGVtYSBkZSBwcm9jZXNzYW1lbnRvIGRlIGxpbmd1YWdlbSBvbmRlIG9zIHZldG9yZXMgZGUgaW5wdXQgJFxcdW5kZXJsaW5le1h9JCBzZWd1ZW0gdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBtdWx0aXZhcmlhZGEgJE4oXFxtdSwgXFxTaWdtYSkkIGVtICRrPTEyOCQgZGltZW5zw7Vlcy4gKGEpIERlZmluYSBtYXRlbWF0aWNhbWVudGUgYSBtYXRyaXogZGUgY292YXJpw6JuY2lhICRcXFNpZ21hJCBlbSB0ZXJtb3MgZGUgZXNwZXJhbsOnYS4gKGIpIFNlIHJlYWxpemFybW9zICRuPTQwMCQgb2JzZXJ2YcOnw7VlcywgcXVhbCBhIGludGVycHJldGHDp8OjbyBlc3RhdMOtc3RpY2EgZGEgZXN0YXTDrXN0aWNhICRcXHNxcnR7bn0oXFxiYXJ7WH1fbiAtIFxcbXUpJCBubyBjb250ZXh0byBkZSBpbmZlcsOqbmNpYT8gKGMpIEV4cGxpcXVlIGNvbW8gYSBtYWduaXR1ZGUgZGUgJFxcU2lnbWEkIGluZmx1ZW5jaWEgYSBjYXBhY2lkYWRlIGRvIG1vZGVsbyBlbSBkaXN0aW5ndWlyIGNvbnRleHRvcyBkaXN0aW50b3MuIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGRlZmluacOnw6NvIGRlIGNvdmFyacOibmNpYSAkRVsoXFx1bmRlcmxpbmV7WH0gLSBcXG11KShcXHVuZGVybGluZXtYfSAtIFxcbXUpXlRdJCBlIGRvIHBhcGVsIGRhIGRpc3BlcnPDo28gbmEgc2VwYXJhYmlsaWRhZGUgZG9zIGRhZG9zLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBIG1hdHJpeiBkZSBjb3ZhcmnDom5jaWEgw6kgZGVmaW5pZGEgY29tbyAkXFxTaWdtYSA9IEVbKFxcdW5kZXJsaW5le1h9IC0gXFxtdSkoXFx1bmRlcmxpbmV7WH0gLSBcXG11KV5UXSQuIiwgIlBhcmEgYSBtw6lkaWEgYW1vc3RyYWwsIG8gVENMIE11bHRpdmFyaWFkbyBpbmRpY2EgcXVlICRcXHNxcnR7bn0oXFxiYXJ7WH1fbiAtIFxcbXUpIFxcYXBwcm94IE4oMCwgXFxTaWdtYSkkLiIsICJFbSB0ZXJtb3MgcHLDoXRpY29zLCBlc3RhIGVzdGF0w61zdGljYSBwZXJtaXRlIGNvbnN0cnVpciBlbGlwc29pZGVzIGRlIGNvbmZpYW7Dp2EgcGFyYSBhIG3DqWRpYSBkb3MgdmV0b3JlcyBvYnNlcnZhZG9zLCBvbmRlICRcXFNpZ21hJCBkZXRlcm1pbmEgYSBmb3JtYSBlIGEgb3JpZW50YcOnw6NvIGRvIGVsaXBzb2lkZSBubyBlc3Bhw6dvIGRlIGFsdGEgZGltZW5zw6NvLiIsICJTZSBhIG1hdHJpeiAkXFxTaWdtYSQgcG9zc3VpIGF1dG92YWxvcmVzIG11aXRvIGRpc3RpbnRvcywgbyBtb2RlbG8gZW5jb250cmFyw6EgZGlyZcOnw7VlcyBkZSB2YXJpw6JuY2lhIChjb21wb25lbnRlcyBwcmluY2lwYWlzKSBvbmRlIGEgZGlmZXJlbmNpYcOnw6NvIGRlIGNvbnRleHRvcyDDqSBtYWlzIGNsYXJhLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtIHBlc3F1aXNhZG9yIGVzdMOhIGFuYWxpc2FuZG8gYSBlc3RhYmlsaWRhZGUgZGUgdW0gbW9kZWxvIGRlIGF0ZW7Dp8Ojby4gRWxlIG9ic2VydmEgcXVlIHBhcmEgdW0gYmF0Y2ggZGUgdGFtYW5obyAkbj0xMDAkLCBhIHZhcmnDom5jaWEgYW1vc3RyYWwgZGEgbcOpZGlhIGRvIHZldG9yIGRlIGF0ZW7Dp8OjbyByZXN1bHRvdSBlbSB1bSB2YWxvciBlc2NhbGFyICRWID0gMC4yNSQgcGFyYSB1bWEgZGltZW5zw6NvIGVzcGVjw61maWNhLiAoYSkgQ2FsY3VsZSBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgJEVQKFxcYmFye1h9KSQgcGFyYSBlc3RhIGRpbWVuc8Ojby4gKGIpIFNhYmVuZG8gcXVlIGEgZGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgw6kgYXByb3hpbWFkYW1lbnRlIG5vcm1hbCwgY2FsY3VsZSBvIGludGVydmFsbyBkZSBjb25maWFuw6dhIGRlIDk1JSBwYXJhIGEgbcOpZGlhIGRlc3RhIGRpbWVuc8OjbyAoZGFkbyAkWl97Y3JpdH0gPSAxLjk2JCkuIiwgImRpY2EiOiAiTyBlcnJvIHBhZHLDo28gw6kgZGFkbyBwb3IgJEVQKFxcYmFye1h9KSA9IFxcc3FydHtcXGZyYWN7U14yfXtufX0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJJZGVudGlmaWNhbW9zIGEgdmFyacOibmNpYSBhbW9zdHJhbCAkU14yID0gMC4yNSQgZSAkbiA9IDEwMCQuIiwgIk8gZXJybyBwYWRyw6NvIMOpICRFUChcXGJhcntYfSkgPSBcXHNxcnR7XFxmcmFjezAuMjV9ezEwMH19ID0gXFxzcXJ0ezAuMDAyNX0gPSAwLjA1JC4iLCAiTyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSDDqSBjYWxjdWxhZG8gY29tbyAkXFxiYXJ7WH0gXFxwbSBaX3tjcml0fSBcXHRpbWVzIEVQKFxcYmFye1h9KSQuIiwgIkFzc2ltLCAkSUMgPSBbXFxiYXJ7WH0gLSAxLjk2IFxcdGltZXMgMC4wNSwgXFxiYXJ7WH0gKyAxLjk2IFxcdGltZXMgMC4wNV0gPSBbXFxiYXJ7WH0gLSAwLjA5OCwgXFxiYXJ7WH0gKyAwLjA5OF0kLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKTsgZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9WzAuMDVdLCB5PVswXSwgbW9kZT0nbWFya2VycycsIG1hcmtlcj1kaWN0KHNpemU9MTAsIGNvbG9yPScjMEYxNzJBJyksIG5hbWU9J0Vycm8gUGFkcsOjbycpKTsgZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J1Zpc3VhbGl6YcOnw6NvIGRvIEVycm8gUGFkcsOjbycsIHhheGlzX3RpdGxlPSdWYWxvcicsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnKTsiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMDV9LCB7ImVudW5jaWFkbyI6ICJBbmFsaXNlIG8gaW1wYWN0byBkYSBkaW1lbnNpb25hbGlkYWRlICRrJCBuYSBpbmZlcsOqbmNpYSBlc3RhdMOtc3RpY2EgZG9zIHBlc29zIGRlIHVtIG1vZGVsby4gKGEpIFNlIG8gbsO6bWVybyBkZSBwYXLDom1ldHJvcyAocGVzb3MpICRwJCBhdW1lbnRhIGVtIHJlbGHDp8OjbyBhbyBuw7ptZXJvIGRlIG9ic2VydmHDp8O1ZXMgJG4kLCBvIHF1ZSBvY29ycmUgY29tIGEgdmFyacOibmNpYSBkb3MgZXN0aW1hZG9yZXM/IChiKSBEaXNjdXRhIGEgcmVsYcOnw6NvIGVudHJlIGEgZXN0aW1hdGl2YSBkZSBtw6F4aW1hIHZlcm9zc2ltaWxoYW7Dp2EgZSBhIHJlZ3VsYXJpemHDp8OjbyAoZXg6IEwyIG91IFdlaWdodCBEZWNheSkgbmVzc2UgZXNwYcOnby4gKGMpIFBvciBxdWUgYSBub3JtYWxpemHDp8OjbyDDqSBjcnVjaWFsIGFudGVzIGRvIGPDoWxjdWxvIGRhIGF0ZW7Dp8Ojbz8iLCAiZGljYSI6ICJDb25zaWRlcmUgbyB0cmFkZS1vZmYgZW50cmUgdmnDqXMgZSB2YXJpw6JuY2lhIGVtIG1vZGVsb3MgZGUgYWx0YSBkaW1lbnPDo28uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkNvbSAkcCQgcHLDs3hpbW8gZGUgJG4kLCBhIHZhcmnDom5jaWEgZG9zIGVzdGltYWRvcmVzIGRlIG3DoXhpbWEgdmVyb3NzaW1pbGhhbsOnYSB0ZW5kZSBhIGV4cGxvZGlyLCBsZXZhbmRvIGFvIHNvYnJlYWp1c3RlIChvdmVyZml0dGluZykuIiwgIkEgcmVndWxhcml6YcOnw6NvIGltcMO1ZSB1bWEgcGVuYWxpZGFkZSAocHJpb3IgZ2F1c3NpYW5hKSwgcmVkdXppbmRvIGEgdmFyacOibmNpYSBkbyBlc3RpbWFkb3IgYW8gY3VzdG8gZGUgaW50cm9kdXppciB1bSBwZXF1ZW5vIHZpw6lzLiIsICJBIG5vcm1hbGl6YcOnw6NvIChMYXllck5vcm0pIGdhcmFudGUgcXVlIG9zIGlucHV0cyBkbyBtZWNhbmlzbW8gZGUgYXRlbsOnw6NvIHBvc3N1YW0gbcOpZGlhIGUgdmFyacOibmNpYSBlc3TDoXZlaXMsIHBlcm1pdGluZG8gcXVlIG8gcHJvZHV0byBlc2NhbGFyIG7Do28gc2VqYSBkb21pbmFkbyBwb3IgcG91Y2FzIGRpbWVuc8O1ZXMgY29tIG1hZ25pdHVkZSBlbGV2YWRhLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtYSByZWRlIG5ldXJhbCBkZSBsYXJnYSBlc2NhbGEsIG8gZXJybyBkZSBwcmVkacOnw6NvICRYX2kkIGFww7NzIG8gcHJvY2Vzc2FtZW50byBkbyBpLcOpc2ltbyBsb3RlIGRlIGRhZG9zIHRlbSBtw6lkaWEgemVybyBlIGRlc3ZpbyBwYWRyw6NvICRcXHNpZ21hID0gMC4xJC4gKGEpIERlZmluYSBhIHZhcmnDom5jaWEgZGEgc29tYSBhY3VtdWxhZGEgJFNfbiQgYXDDs3MgJG4gPSAxMDAwJCBsb3Rlcy4gKGIpIFV0aWxpemFuZG8gYSBEZXNpZ3VhbGRhZGUgZGUgS29sbW9nb3JvdiwgY2FsY3VsZSBvIGxpbWl0ZSBzdXBlcmlvciBwYXJhIGEgcHJvYmFiaWxpZGFkZSBkZSBvIGVycm8gYWN1bXVsYWRvIGV4Y2VkZXIgJFxcbGFtYmRhID0gNSQuIChjKSBJbnRlcnByZXRlIG8gcmVzdWx0YWRvIGVtIHRlcm1vcyBkZSBlc3RhYmlsaWRhZGUgZG8gbW9kZWxvLiIsICJkaWNhIjogIkNhbGN1bGUgcHJpbWVpcm8gYSB2YXJpw6JuY2lhIGFjdW11bGFkYSAkblxcc2lnbWFeMiQgZSBzdWJzdGl0dWEgbmEgZsOzcm11bGEgZGEgZGVzaWd1YWxkYWRlLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyBhOiAkVmFyKFNfbikgPSBuXFxzaWdtYV4yID0gMTAwMCBcXHRpbWVzICgwLjEpXjIgPSAxMDAwIFxcdGltZXMgMC4wMSA9IDEwJC4iLCAiUGFzc28gYjogQXBsaWNhbmRvIEtvbG1vZ29yb3Y6ICRQKFxcbWF4IHxTX2t8IFxcZ2UgNSkgXFxsZSBcXGZyYWN7VmFyKFNfbil9e1xcbGFtYmRhXjJ9ID0gXFxmcmFjezEwfXs1XjJ9ID0gXFxmcmFjezEwfXsyNX0gPSAwLjQkLiIsICJQYXNzbyBjOiBPIGxpbWl0ZSBkZSAwLjQgaW5kaWNhIHVtYSBwcm9iYWJpbGlkYWRlIG3DoXhpbWEgZGUgNDAlIGRlIGRlc3ZpbywgbyBxdWUgc3VnZXJlIHVtYSBlc3RhYmlsaWRhZGUgbW9kZXJhZGEgZHVyYW50ZSBvIHRyZWluYW1lbnRvLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKTsgZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9bnAubGluc3BhY2UoMCwgMTAsIDEwMCksIHk9MTAvbnAubGluc3BhY2UoMC4xLCAxMCwgMTAwKSoqMiwgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJykpKTsgZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0xpbWl0ZSBTdXBlcmlvciBQcm9iYWJpbMOtc3RpY28nLCB4YXhpc190aXRsZT0nTGltaWFyIFxcbGFtYmRhJywgeWF4aXNfdGl0bGU9J1AoTWF4IFNfayA+PSBcXGxhbWJkYSknKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC40fSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIHNvYiBhIMOzdGljYSBlc3RhdMOtc3RpY2EsIHBvciBxdWUgYSBEZXNpZ3VhbGRhZGUgZGUgS29sbW9nb3JvdiDDqSBzdXBlcmlvciDDoCBEZXNpZ3VhbGRhZGUgZGUgQ2hlYnlzaGV2IHF1YW5kbyBhbmFsaXNhbW9zIHByb2Nlc3NvcyBlc3RvY8Ohc3RpY29zIGRlIHRyZWluYW1lbnRvIGRlIG1vZGVsb3MgZGUgbGluZ3VhZ2VtLiIsICJkaWNhIjogIlJlZmxpdGEgc29icmUgbyBxdWUgY2FkYSBkZXNpZ3VhbGRhZGUgbGltaXRhOiB1bWEgbGltaXRhIG8gZGVzdmlvIGVtIHVtIGluc3RhbnRlIGZpeG8gKCRuJCksIGEgb3V0cmEgbGltaXRhIG8gZGVzdmlvIG3DoXhpbW8gYWJzb2x1dG8gc29icmUgdG9kbyBvIGNhbWluaG8gZGEgc29tYSAoJDEgXFxsZSBrIFxcbGUgbiQpLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBDaGVieXNoZXYgZm9ybmVjZSB1bWEgY290YSBwYXJhIG8gZGVzdmlvIGRlIHVtYSB2YXJpw6F2ZWwgYWxlYXTDs3JpYSBlbSB1bSBwb250byBlc3BlY8OtZmljbyBkbyB0ZW1wbzogJFAofFNfbiAtIFxcbXVfbnwgXFxnZSBcXGxhbWJkYSkgXFxsZSBcXGZyYWN7VmFyKFNfbil9e1xcbGFtYmRhXjJ9JC4iLCAiMi4gS29sbW9nb3JvdiBmb2NhIG5hIHRyYWpldMOzcmlhIGNvbXBsZXRhOiAkUChcXG1heF97MSBcXGxlIGsgXFxsZSBufSB8U19rfCBcXGdlIFxcbGFtYmRhKSBcXGxlIFxcZnJhY3tWYXIoU19uKX17XFxsYW1iZGFeMn0kLiIsICIzLiBFbSBMTE1zLCDDqSBtYWlzIGNyw610aWNvIGdhcmFudGlyIHF1ZSBvIG1vZGVsbyBuw6NvIGRpdmlyamEgZW0gbmVuaHVtIG1vbWVudG8gZHVyYW50ZSBvIHRyZWlubyAodHJhamV0w7NyaWEpIGRvIHF1ZSBhcGVuYXMgZW0gdW0gcG9udG8gZmluYWwsIGxvZ28gS29sbW9nb3JvdiBvZmVyZWNlIHVtIGNvbnRyb2xlIGRlIHNlZ3VyYW7Dp2EgbWFpcyByb2J1c3RvIHBhcmEgdG9kbyBvIHByb2Nlc3NvIGRlIGNvbnZlcmfDqm5jaWEuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHF1ZSBhIHZhcmnDom5jaWEgZGUgdW0gcHJvY2Vzc28gZGUgYWp1c3RlIGRlIGhpcGVycGFyw6JtZXRyb3MgZGVjcmVzY2Ugw6AgbWVkaWRhIHF1ZSBvIG7Dum1lcm8gZGUgaXRlcmHDp8O1ZXMgJG4kIGF1bWVudGEsIHNlZ3VpbmRvIGEgcmVsYcOnw6NvICRWYXIoU19uKSA9IDEwMCAvIG4kLiBDYWxjdWxlIG8gbGltaXRlIGRlIEtvbG1vZ29yb3YgcGFyYSAkbiA9IDQwMCQgZSAkXFxsYW1iZGEgPSAwLjUkLiIsICJkaWNhIjogIlByaW1laXJvIGNhbGN1bGUgYSB2YXJpw6JuY2lhIHRvdGFsIG5vIHBhc3NvICRuPTQwMCQgdXNhbmRvIGEgZsOzcm11bGEgZGFkYSwgZGVwb2lzIGFwbGlxdWUgbyBsaW1pdGUgZGUgS29sbW9nb3Jvdi4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gVmFyacOibmNpYSBlbSAkbj00MDAkOiAkVmFyKFNfezQwMH0pID0gMTAwIC8gNDAwID0gMC4yNSQuIiwgIjIuIExpbWlhciAkXFxsYW1iZGEgPSAwLjUkLCBsb2dvICRcXGxhbWJkYV4yID0gMC4yNSQuIiwgIjMuIExpbWl0ZSBkZSBLb2xtb2dvcm92OiAkUChcXG1heCB8U19rfCBcXGdlIDAuNSkgXFxsZSBcXGZyYWN7VmFyKFNfezQwMH0pfXtcXGxhbWJkYV4yfSA9IFxcZnJhY3swLjI1fXswLjI1fSA9IDEuMCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAxLjB9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgcXVlIHVtIG1vZGVsbyBkZSBsaW5ndWFnZW0gcG9zc3VpIHVtYSBzb21hIGxhdGVudGUgJFNfbiQgZGUgJG49MTAwJCBhdGl2YcOnw7VlcyBpbmRlcGVuZGVudGVzIGRlIG5ldXLDtG5pb3MsIGNhZGEgdW1hIHNlZ3VpbmRvIHVtYSBkaXN0cmlidWnDp8OjbyBjb20gbcOpZGlhICRcXG11ID0gMC41JCBlIHZhcmnDom5jaWEgJFxcc2lnbWFeMiA9IDAuMDEkLiAoYSkgU2VndW5kbyBvIFRlb3JlbWEgQ2VudHJhbCBkbyBMaW1pdGUsIHF1YWwgYSBkaXN0cmlidWnDp8OjbyBhcHJveGltYWRhIGRlICRTX24kPyAoYikgQ2FsY3VsZSBhIHByb2JhYmlsaWRhZGUgJFAoU19uID4gNTUpJC4iLCAiZGljYSI6ICJPIFRlb3JlbWEgQ2VudHJhbCBkbyBMaW1pdGUgZXN0YWJlbGVjZSBxdWUgJFNfbiBcXGFwcHJveCBOKG5cXG11LCBuXFxzaWdtYV4yKSQuIENvbnZlcnRhIHBhcmEgYSBub3JtYWwgcGFkcsOjbyAkWiA9IFxcZnJhY3tTX24gLSBFW1Nfbl19e1xcc3FydHtWYXIoU19uKX19JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiSWRlbnRpZmljYW1vcyBxdWUgJEVbU19uXSA9IG5cXG11ID0gMTAwIFxcY2RvdCAwLjUgPSA1MCQuIiwgIklkZW50aWZpY2Ftb3MgcXVlICRWYXIoU19uKSA9IG5cXHNpZ21hXjIgPSAxMDAgXFxjZG90IDAuMDEgPSAxJC4gUG9ydGFudG8sIG8gZGVzdmlvIHBhZHLDo28gw6kgJFxcc3FydHsxfSA9IDEkLiIsICJBIGRpc3RyaWJ1acOnw6NvIGFwcm94aW1hZGEgw6kgJFNfbiBcXHNpbSBOKDUwLCAxKSQuIiwgIlBhcmEgY2FsY3VsYXIgJFAoU19uID4gNTUpJCwgcGFkcm9uaXphbW9zOiAkWiA9IFxcZnJhY3s1NSAtIDUwfXsxfSA9IDUkLiIsICJQZWxhIHRhYmVsYSBub3JtYWwsICRQKFogPiA1KSBcXGFwcHJveCAwJCAodmFsb3IgZXh0cmVtYW1lbnRlIGJhaXhvLCBkYWRvIHF1ZSA1IGRlc3Zpb3MgcGFkcsO1ZXMgcmVwcmVzZW50YW0gdW0gZXZlbnRvIHF1YXNlIG51bG8pLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDQ1LCA1NSwgMTAwKVxueSA9ICgxLyhucC5cXHNxcnQoMipucC5cXHBpKSkpICogbnAuXFxleHAoLTAuNSAqICgoeC01MCkvMSkqKjIpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG1vZGU9J2xpbmVzJywgbmFtZT0nRGlzdHJpYnVpw6fDo28gJE4oNTAsIDEpJCcpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0Rpc3RyaWJ1acOnw6NvIGRlIFNvbWFzIExhdGVudGVzICRTX24kJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMH0sIHsiZW51bmNpYWRvIjogIlVtIG1vZGVsbyBMTE0gcHJldsOqIGEgZGlzdHJpYnVpw6fDo28gZGUgdG9rZW5zICRQID0gWzAuNiwgMC40XSQsIGVucXVhbnRvIGEgZGlzdHJpYnVpw6fDo28gcmVhbCBvYnNlcnZhZGEgbm8gY29ycHVzIGRlIHRyZWluYW1lbnRvIMOpICRRID0gWzAuNywgMC4zXSQuIENhbGN1bGUgYSBEaXZlcmfDqm5jaWEgZGUgS3VsbGJhY2stTGVpYmxlciAkRF97S0x9KFAgXFxwYXJhbGxlbCBRKSQgZW50cmUgZXN0YXMgZGlzdHJpYnVpw6fDtWVzLiIsICJkaWNhIjogIlVzZSBhIGbDs3JtdWxhICREX3tLTH0oUCBcXHBhcmFsbGVsIFEpID0gXFxzdW0gcF9pIFxcbG9nXFxsZWZ0KFxcZnJhY3twX2l9e3FfaX1cXHJpZ2h0KSQuIFV0aWxpemUgbG9nYXJpdG1vIG5hdHVyYWwuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkRlZmluaW1vcyAkRF97S0x9ID0gcF8xIFxcbG4ocF8xL3FfMSkgKyBwXzIgXFxsbihwXzIvcV8yKSQuIiwgIlN1YnN0aXR1w61tb3Mgb3MgdmFsb3JlczogJDAuNiBcXGxuKDAuNiAvIDAuNykgKyAwLjQgXFxsbigwLjQgLyAwLjMpJC4iLCAiQ2FsY3VsYW1vcyBvcyB0ZXJtb3M6ICQwLjYgXFxsbigwLjg1NzEpIFxcYXBwcm94IDAuNiBcXGNkb3QgKC0wLjE1NDEpID0gLTAuMDkyNSQuIiwgIkNhbGN1bGFtb3MgbyBzZWd1bmRvIHRlcm1vOiAkMC40IFxcbG4oMS4zMzMzKSBcXGFwcHJveCAwLjQgXFxjZG90ICgwLjI4NzcpID0gMC4xMTUxJC4iLCAiU29tYW1vcyBvcyB2YWxvcmVzOiAkRF97S0x9ID0gLTAuMDkyNSArIDAuMTE1MSA9IDAuMDIyNiQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjAyMjZ9LCB7ImVudW5jaWFkbyI6ICJTZWphIHVtIG1vZGVsbyBkZSBsaW5ndWFnZW0gcXVlIHByZXbDqiB1bWEgZGlzdHJpYnVpw6fDo28gdW5pZm9ybWUgc29icmUgOCB0b2tlbnMsICRQID0gWzEvOCwgXFxkb3RzLCAxLzhdJC4gQ2FsY3VsZSBhIGVudHJvcGlhIGRlIFNoYW5ub24gZGVzdGEgZGlzdHJpYnVpw6fDo28gZSBleHBsaXF1ZSBvIHNpZ25pZmljYWRvIGbDrXNpY28gZGVzdGUgcmVzdWx0YWRvIG5vIGNvbnRleHRvIGRlIGluY2VydGV6YSBkbyBtb2RlbG8uIiwgImRpY2EiOiAiQSBlbnRyb3BpYSBkZSB1bWEgZGlzdHJpYnVpw6fDo28gdW5pZm9ybWUgJFUoSykkIMOpICRIKFgpID0gXFxsb2dfMihLKSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgZGlzdHJpYnVpw6fDo28gdW5pZm9ybWUgcG9zc3VpICRLPTgkIGVzdGFkb3MgZXF1aXByb3bDoXZlaXMuIiwgIkEgZW50cm9waWEgw6kgJEgoWCkgPSAtIFxcc3VtX3tpPTF9XjggXFxmcmFjezF9ezh9IFxcbG9nXzIoXFxmcmFjezF9ezh9KSQuIiwgIkNvbW8gJFxcbG9nXzIoMS84KSA9IC0zJCwgdGVtb3MgJEgoWCkgPSAtICg4IFxcY2RvdCBcXGZyYWN7MX17OH0gXFxjZG90IC0zKSA9IDMkLiIsICJPIHJlc3VsdGFkbyDDqSAzIGJpdHMuIElzc28gaW5kaWNhIHF1ZSBvIG1vZGVsbyBwb3NzdWkgbcOheGltYSBpbmNlcnRlemEsIHBvaXMgbsOjbyBjb25zZWd1ZSBkaXN0aW5ndWlyIGVudHJlIG9zIDggdG9rZW5zIHBvc3PDrXZlaXMsIGV4aWdpbmRvIDMgYml0cyBkZSBpbmZvcm1hw6fDo28gcGFyYSBlc3BlY2lmaWNhciBvIHByw7N4aW1vIHRva2VuLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMy4wfV19').decode('utf-8'))


    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    
    # Inicialização do estado de controle de gamificação
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dos totais para o painel de progresso
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discursivas = dados_exercicios.get("questoes_discursivas", [])
    total_ex = len(mcqs) + len(discursivas)
    acertos = sum(1 for v in st.session_state.respostas_certas.values() if v is True)
    
    # Exibição do Placar
    if total_ex > 0:
        st.progress(acertos / total_ex)
        st.info(f"🏆 **Seu Placar de Aprendizado:** {acertos} de {total_ex} desafios concluídos com sucesso!")
    
    # --- Renderização de Questões de Múltipla Escolha ---
    for i, questao in enumerate(mcqs):
        with st.container(border=True):
            st.markdown(f"#### Questão {i+1} (Múltipla Escolha)")
            st.markdown(questao["enunciado"])
            
            if questao.get("referencia_livro"):
                st.markdown(f"📖 *Referência RAG: {questao['referencia_livro']}*")
            
            # Execução segura de código Plotly
            if questao.get("codigo_plotly"):
                local_vars = {"st": st, "go": go, "np": np}
                try:
                    exec(questao["codigo_plotly"], globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"fig_mcq_{i}")
                except Exception as e:
                    st.error(f"Erro ao renderizar gráfico: {e}")
    
            # Renderização das alternativas
            opcoes = questao["alternativas"]
            lista_opcoes = [f"{k}: {v}" for k, v in opcoes.items()]
            escolha = st.radio("Escolha uma alternativa:", lista_opcoes, key=f"radio_mcq_{i}")
            
            if st.button("💡 Dica", key=f"hint_mcq_{i}"):
                st.info(questao.get("dica"))
                
            if st.button("✅ Confirmar Resposta", key=f"btn_mcq_{i}"):
                letra_escolhida = escolha.split(":")[0]
                if letra_escolhida == questao["alternativa_correta"]:
                    st.success("🎉 Correto! Resposta excelente.")
                    st.session_state.respostas_certas[f"mcq_{i}"] = True
                    st.rerun()
                else:
                    st.error("❌ Resposta Incorreta. Reveja os conceitos e tente novamente!")
                    st.session_state.respostas_certas[f"mcq_{i}"] = False
                    st.rerun()
            
            with st.expander("🔍 Ver Gabarito Comentado e Explicação"):
                st.write(questao["gabarito_comentado"])
    
    # --- Renderização de Questões Discursivas ---
    for i, questao in enumerate(discursivas):
        with st.container(border=True):
            st.markdown(f"#### Questão {i+1} (Discursiva de Cálculo / Análise)")
            st.markdown(questao["enunciado"])
            
            if questao.get("referencia_livro"):
                st.markdown(f"📖 *Referência RAG: {questao['referencia_livro']}*")
                
            if questao.get("codigo_plotly"):
                local_vars = {"st": st, "go": go, "np": np}
                try:
                    exec(questao["codigo_plotly"], globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plot_disc_{i}")
                except Exception as e:
                    st.error(f"Erro ao renderizar gráfico: {e}")
    
            st.text_area("Sua Resposta em Prosa / Raciocínio:", key=f"text_disc_{i}")
            
            # Validação automática se for numérica
            esperado = questao.get("resposta_numerica_esperada")
            if esperado is not None:
                valor_aluno = st.number_input("Digite o resultado numérico exato:", format="%.4f", key=f"num_disc_{i}")
                if st.button("Validar Cálculo Numérico", key=f"val_disc_{i}"):
                    tol = max(0.01, 0.01 * abs(float(esperado)))
                    if abs(valor_aluno - float(esperado)) <= tol:
                        st.success("🎉 Resultado Numérico Correto! Cálculo impecável.")
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                        st.rerun()
                    else:
                        st.error("❌ O valor calculado difere do gabarito oficial.")
                        st.session_state.respostas_certas[f"disc_{i}"] = False
            else:
                # Validação qualitativa via check
                if st.checkbox("Marque aqui após estudar e responder este desafio", key=f"check_disc_{i}"):
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.session_state.respostas_certas[f"disc_{i}"] = False
    
            with st.expander("✅ Ver Resolução Detalhada Passo a Passo"):
                for passo in questao.get("gabarito_passo_a_passo", []):
                    st.markdown(f"* {passo}")
