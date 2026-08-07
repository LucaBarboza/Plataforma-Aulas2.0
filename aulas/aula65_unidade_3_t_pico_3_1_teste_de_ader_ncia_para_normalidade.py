import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDMgLSBUw7NwaWNvIDMuMTogVGVzdGUgZGUgYWRlcsOqbmNpYSBwYXJhIG5vcm1hbGlkYWRlIiwgInJlZmVyZW5jaWFzX2JpYmxpb2dyYWZpY2FzX2ZpbmFpcyI6IFsiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhIC0gQ2FwLiAxNCwgcHAuIDQwMy00MDYsIDQxNS00MTYiLCAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhIC0gQ2FwLiAzLCBwcC4gNTEtNTgiLCAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhIC0gQ2FwLiAxNiwgcHAuIDQ3MCwgNDc5Il19').decode('utf-8'))

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

    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"O Problema da Aderência: Conceitos e Hipóteses de Normalidade")
    
    # Prosa Explicativa com ritmo de leitura
    st.markdown(r"""
    A validade de inúmeras técnicas estatísticas, desde intervalos de confiança até o rigoroso teste de hipóteses sobre médias, repousa sobre a premissa de que os dados seguem uma distribuição normal. No cenário prático, a forma exata da população é frequentemente desconhecida.
    """)
    
    st.info(r"A normalidade é uma hipótese de trabalho que simplifica a análise, mas sua veracidade deve ser sempre questionada para evitar conclusões espúrias.")
    
    st.markdown(r"""
    O problema da aderência surge ao questionar: será que o fenômeno em estudo realmente adere à curva gaussiana? O teste de aderência atua como um controle de qualidade estatístico para verificar se o desvio entre a distribuição teórica e os dados observados decorre de variabilidade aleatória ou de uma falha intrínseca na modelagem.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Teste de Aderência")
    
    st.markdown(r"A hipótese nula e alternativa são definidas formalmente como:")
    st.latex(r"H_{0}: F(x) = F_{0}(x), \quad \forall x \in \mathbb{R}")
    st.latex(r"H_{1}: F(x) \neq F_{0}(x), \quad \text{para pelo menos um } x \in \mathbb{R}")
    
    st.markdown(r"**Dedução Analítica:**")
    st.latex(r"\text{Seja a amostra aleatória simples } X_{1}, ..., X_{n} \text{ oriunda de uma população com f.d.a. } F(x).")
    st.latex(r"F_{e}(x) = \frac{1}{n} \sum_{i=1}^{n} I(X_{i} \le x)")
    st.latex(r"D = \max_{1 \le i \le n} |F(x_{i}) - F_{e}(x_{i})|")
    
    # Simulador Interativo
    st.subheader(r"⚙️ Simulador: Visualizador de Aderência")
    
    col1, col2 = st.columns(2)
    with col1:
        mu_val = st.slider(r"Média ($\mu$)", 450.0, 550.0, 500.0, key=r"mu_sim_subtopico_1")
    with col2:
        sigma_val = st.slider(r"Desvio Padrão ($\sigma$)", 1.0, 20.0, 10.0, key=r"sigma_sim_subtopico_1")
    
    # Gerar dados simulados
    n_pontos = 30
    data = np.random.normal(500, 10, n_pontos)
    x_sorted = np.sort(data)
    cdf_empirica = np.arange(1, n_pontos + 1) / n_pontos
    cdf_teorica = stats.norm.cdf(x_sorted, mu_val, sigma_val)
    
    # Gráfico Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_sorted, y=cdf_empirica, mode='steps-post', name=r"f.d.e. Amostral", line=dict(color="#1E3A8A")))
    fig.add_trace(go.Scatter(x=x_sorted, y=cdf_teorica, mode='lines', name=r"f.d.a. Normal", line=dict(color="#10B981")))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Comparação: Distribuição Empírica vs Teórica</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    fig.update_xaxes(title=dict(text=r"Valor da Variável", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True)
    fig.update_yaxes(title=dict(text=r"Probabilidade Acumulada", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True)
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    # Laudo dinâmico
    dist_max = np.max(np.abs(cdf_teorica - cdf_empirica))
    st.info(rf"Com os parâmetros selecionados, a distância máxima (estatística D) observada entre a curva teórica e a escada empírica é de {dist_max:.4f}. Compare este valor com o valor crítico para decidir sobre a rejeição de H0.")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Envase Industrial")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Processo de Envase")
        st.markdown(r"Em um processo industrial de envase, a massa das embalagens deve seguir uma normal com $\mu=500g$ e $\sigma^{2}=100g^{2}$.")
        st.latex(r"H_{0}: X \sim N(500, 100), \quad n=30")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Calcula-se o quantil teórico $Z_{i} = \frac{x_{i} - 500}{10}$ para cada observação.")
        st.markdown(r"- Deriva-se a f.d.a. teórica $F_{0}(x_{i}) = \Phi(Z_{i})$ e compara-se com a f.d.e. amostral $F_{e}(x_{i}) = i/n$.")
        st.success(r"Conclusão: Se a estatística $D$ superar o valor crítico tabelado, a hipótese de normalidade é rejeitada, exigindo reavaliação do processo ou métodos não-paramétricos.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Metodologia Qui-Quadrado para Testes de Aderência")
    
    # Discussão Teórica
    st.markdown(r"""
    A metodologia Qui-Quadrado adota uma abordagem de contagem em vez de uma análise contínua de distância acumulada. 
    O espectro da variável é particionado em intervalos de classe, transformando dados contínuos em frequências discretas observadas.
    """)
    
    st.info(r"Comparando estas frequências reais com as expectativas teóricas calculadas via normalidade, a estatística de teste quantifica a discrepância quadrática ponderada. É um método versátil que oferece uma métrica de desvio global robusta, validada pela convergência assintótica para a distribuição Qui-Quadrado sob a hipótese nula.")
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Estatística Qui-Quadrado")
    st.latex(r"\chi^2_{\text{calc}} = \sum_{i=1}^{k} \frac{(O_{i} - E_{i})^2}{E_{i}}")
    st.latex(r"gl = k - 1 - m")
    
    # Dedução Analítica
    st.markdown(r"A derivação da estatística fundamenta-se na discretização da densidade de probabilidade:")
    st.latex(r"P(x_{i-1} < X \le x_i) = F_0(x_i) - F_0(x_{i-1})")
    st.markdown(r"A frequência esperada $E_i$ é obtida pelo produto do tamanho amostral $n$ pela probabilidade do intervalo:")
    st.latex(r"E_i = n \cdot [F_0(x_i) - F_0(x_{i-1})]")
    st.markdown(r"Por fim, a métrica de desvio é construída sobre a soma das discrepâncias quadradas normalizadas:")
    st.latex(r"\chi^2_{\text{calc}} = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i}")
    
    # Simulador Interativo
    st.markdown(r"### 📊 Simulador de Discretização e Ajuste")
    col1, col2 = st.columns(2)
    with col1:
        bins_count = st.slider(r"Número de classes (k)", 3, 10, 5, key=r"bins_simulador_subtopico_2")
    with col2:
        n_amostras = st.number_input(r"Tamanho da amostra (n)", 50, 1000, 100, key=r"n_simulador_subtopico_2")
    
    # Lógica do Simulador (Estática/Hardcoded comportamento)
    data_sim = np.random.normal(0, 1, n_amostras)
    hist_data = np.histogram(data_sim, bins=bins_count)
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[str(i) for i in range(bins_count)], y=hist_data[0], name=r"Frequência Observada", marker_color=r"#1E3A8A"))
    
    fig.update_layout(
        template=r"plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Distribuição de Frequências Observadas</b>", font=dict(size=14, color=r"#1E293B", family=r"Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Intervalos de Classe", font=dict(size=11, color=r"#1E293B", family=r"Arial, sans-serif")), tickfont=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Contagem (O_i)", font=dict(size=11, color=r"#1E293B", family=r"Arial, sans-serif")), tickfont=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        legend=dict(orientation=r"h", yanchor=r"bottom", y=1.02, xanchor=r"right", x=1.0, font=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), bgcolor=r"rgba(255, 255, 255, 0.8)", bordercolor=r"#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor=r"#FFFFFF", font_size=12, font_color=r"#1E293B", font_family=r"Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    st.info(r"Alterar o número de classes modifica a sensibilidade da estatística $\chi^2$. Classes muito pequenas podem inflar a variância, enquanto classes muito grandes ocultam desvios locais da normalidade.")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática: Análise de Servidor")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Tempo de Resposta de Rede")
        st.markdown(r"Um servidor de rede tem seu tempo de resposta analisado. Com $n=100$ transações, os dados foram agrupados em 5 classes. A média e variância foram estimadas da amostra ($m=2$). O analista busca saber se a distribuição normal é um modelo aceitável com nível de significância $\alpha=0.05$.")
        
        st.latex(r"O_i = [10, 25, 35, 20, 10], \quad E_i = [8, 22, 40, 20, 10], \quad k=5, \quad m=2")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo dos graus de liberdade: $gl = 5 - 1 - 2 = 2$")
        st.markdown(r"- Cálculo da estatística: $\chi^2_{\text{calc}} = \frac{(10-8)^2}{8} + \frac{(25-22)^2}{22} + \frac{(35-40)^2}{40} + \frac{(20-20)^2}{20} + \frac{(10-10)^2}{10} = 1.534$")
        
        st.success(r"Com $\chi^2_{\text{calc}} = 1.534 < \chi^2_{\text{crit}}(0.05, 2) \approx 5.991$, não há evidências para rejeitar a normalidade. O servidor opera sob um tempo de resposta aderente ao modelo gaussiano, validando previsões paramétricas.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    
    # Cabeçalho do Subtópico
    st.header(r"O Teste de Kolmogorov-Smirnov como Alternativa Não-Paramétrica")
    
    # Discussão Teórica
    st.markdown(r"""
    A inferência estatística busca compreender o comportamento de fenômenos populacionais a partir de uma amostra finita, sendo um dos desafios persistentes a verificação da adequação de um modelo probabilístico aos dados. Historicamente, o teste Qui-Quadrado de aderência foi a ferramenta predominante, porém limitada pela necessidade de agrupamento de dados em classes, o que introduz um viés de quantização e sacrifica a resolução amostral.
    
    O teste de Kolmogorov-Smirnov surge como uma alternativa elegante e conceitualmente superior, operando diretamente sobre a função de distribuição empírica, $F_e(x)$. Esta abordagem preserva a integridade de cada ponto observado, permitindo detectar desvios em qualquer parte da distribuição sem a arbitrariedade de limites de classe.
    """)
    
    st.info(r"O teste de Kolmogorov-Smirnov é uma ferramenta diagnóstica distribuição-livre de alta sensibilidade, que quantifica a aderência entre uma amostra e uma distribuição teórica contínua por meio da distância máxima absoluta entre as respectivas funções de distribuição.")
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Estatística do Supremo")
    st.markdown(r"A métrica $D$ atua como um quantificador global da aderência, capturando a amplitude máxima do afastamento entre os dados e a teoria através da seguinte relação:")
    
    st.latex(r"D = \sup_{x} |F(x) - F_e(x)|")
    
    st.markdown(r"Para o cálculo computacional eficiente, utilizamos a formulação baseada nos elementos ordenados da amostra:")
    
    st.latex(r"D = \max_{1 \le i \le n} \left( \max \left( \left| \frac{i}{n} - F(X_{(i)}) \right|, \left| F(X_{(i)}) - \frac{i-1}{n} \right| \right) \right)")
    
    # Dedução Analítica
    st.markdown(r"### 🔍 Propriedades e Dedução Analítica")
    st.markdown(r"1. Considere a amostra $X_1, \dots, X_n$ ordenada: $X_{(1)} \le \dots \le X_{(n)}$.")
    st.latex(r"F_e(x) \text{ é a escada definida por saltos de } \frac{i}{n} \text{ em cada } X_{(i)}.")
    st.markdown(r"3. A distância máxima $D$ ocorre nos pontos de salto da função de distribuição empírica.")
    st.markdown(r"4. O Teorema de Kolmogorov-Smirnov garante que a distribuição de $D$ sob $H_0$ é independente da f.d.a. $F_0(x)$ para qualquer distribuição contínua.")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Teste de Aderência à Uniformidade")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Sensor em Intervalo Unitário")
        st.markdown(r"Dada uma amostra $X_{(i)} = \{0.20, 0.45, 0.60, 0.85, 0.95\}$ para $n=5$, testa-se a aderência à distribuição uniforme em $[0, 1]$, onde $F_0(x) = x$.")
        
        st.latex(r"n=5, \quad \frac{i}{n} = [0.2, 0.4, 0.6, 0.8, 1.0], \quad F_0(X_{(i)}) = [0.2, 0.45, 0.6, 0.85, 0.95]")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Para $i=1: |0.2-0.2|=0, |0.2-0|=0.2 \rightarrow D_1=0.2$")
        st.markdown(r"- Para $i=2: |0.4-0.45|=0.05, |0.45-0.2|=0.25 \rightarrow D_2=0.25$")
        st.markdown(r"- Para $i=3: |0.6-0.6|=0, |0.6-0.4|=0.2 \rightarrow D_3=0.2$")
        
        st.success(r"A estatística calculada $D=0.25$ é comparada com a tabela de Kolmogorov-Smirnov. Caso $D < D_{\text{crit}}$, não há evidência de desvio da uniformidade, validando a distribuição proposta para o sensor.")
    
    # Prosa Expandida Final
    st.markdown(r"---")
    st.markdown(r"### 💡 Reflexão sobre a Integração do Modelo")
    st.markdown(r"""
    Ao adotar o teste de Kolmogorov-Smirnov, o analista alinha-se a uma tradição de rigor que valoriza a precisão geométrica entre distribuições. A intuição pedagógica a ser retida é que a 'distância' medida não é apenas uma métrica abstrata, mas uma representação da 'saúde' do ajuste do modelo aos dados. 
    
    Diferente de testes que focam apenas em momentos da distribuição, como a média ou variância, o teste de K-S é altamente sensível a assimetrias, curtoses e comportamentos de cauda. Quando observamos uma amostra, a natureza discreta da escada empírica aproxima-se da curva teórica sob a hipótese nula; desvios significativos que elevam $D$ são, invariavelmente, evidências de que o modelo probabilístico subjacente requer uma revisão fundamental.
    """)

    import numpy as np
    import scipy.stats as stats
    import plotly.graph_objects as go
    import streamlit as st
    
    # Cabeçalho do Subtópico
    st.header(r"Análise Gráfica e Diagnóstico de Normalidade")
    
    # Introdução e Prosa Teórica
    st.markdown(r"""
    A inspeção visual é indispensável para o diagnóstico de normalidade, precedendo qualquer teste formal. O gráfico de quantis (q-q plot) é a ferramenta de diagnóstico mais refinada para identificar sistemáticas divergências da normalidade.
    """)
    
    st.info(r"Ao mapear quantis amostrais contra quantis teóricos, a linearidade resultante na reta de 45 graus atesta o ajuste. Desvios nas caudas ou concavidades sistemáticas oferecem pistas diagnósticas imediatas, como assimetria ou curtose.")
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Fundamentos do Q-Q Plot")
    st.markdown(r"A construção do gráfico baseia-se na transformação de dados empíricos em uma escala de normalidade padrão através da função inversa da f.d.a.")
    
    st.latex(r"F_{N(0,1)}(Z_i) = p_i = \frac{i - 0,5}{n}")
    st.latex(r"Z_i = \Phi^{-1}(p_i)")
    
    # Dedução Analítica
    st.markdown(r"**Passo a passo do procedimento de construção:**")
    st.latex(r"1. \text{ Ordenar os dados observados: } X_{(1)} \le X_{(2)} \le \dots \le X_{(n)}")
    st.latex(r"2. \text{ Calcular as probabilidades empíricas: } p_i = \frac{i - 0,5}{n}")
    st.latex(r"3. \text{ Determinar os quantis teóricos: } Z_i = \Phi^{-1}(p_i)")
    st.latex(r"4. \text{ Plotar o par } (Z_i, X_{(i)}) \text{ e verificar o alinhamento linear}")
    
    # Simulador Interativo
    st.markdown(r"### 🕹️ Simulador de Diagnóstico: Gerador de Q-Q Plot Dinâmico")
    
    col1, col2 = st.columns(2)
    with col1:
        skew_val = st.slider(r"Assimetria (Skewness)", -2.0, 2.0, 0.0, step=0.1, key=r"skew_subtopico_4")
    with col2:
        kurt_val = st.slider(r"Curtose (Kurtosis)", -1.0, 3.0, 0.0, step=0.1, key=r"kurt_subtopico_4")
    
    show_line = st.toggle(r"Exibir Reta de Regressão", value=True, key=r"toggle_reg_subtopico_4")
    
    # Lógica do Simulador (Geração de dados baseada nos inputs do usuário)
    data_sim = stats.skewnorm.rvs(a=skew_val, size=100) + kurt_val * np.random.normal(0, 1, 100)
    data_sorted = np.sort(data_sim)
    p_i = (np.arange(1, 101) - 0.5) / 100
    theoretical_quantiles = stats.norm.ppf(p_i)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=theoretical_quantiles, y=data_sorted, mode='markers', name='Amostra', marker=dict(color='#1E3A8A')))
    
    if show_line:
        slope, intercept, _, _, _ = stats.linregress(theoretical_quantiles, data_sorted)
        line_x = np.array([theoretical_quantiles.min(), theoretical_quantiles.max()])
        line_y = slope * line_x + intercept
        fig.add_trace(go.Scatter(x=line_x, y=line_y, mode='lines', name='Referência', line=dict(color='#991B1B', dash='dash')))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Diagnóstico Visual: Quantis Amostrais vs. Teóricos</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Quantis Teóricos", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Quantis Amostrais", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")
    
    # Laudo Dinâmico
    if abs(skew_val) > 0.5 or abs(kurt_val) > 0.5:
        st.info(r"Laudo: O gráfico apresenta desvios significativos da reta de referência, sugerindo que os dados não seguem uma distribuição normal. Considere transformações ou testes não paramétricos.")
    else:
        st.success(r"Laudo: A distribuição parece aderir satisfatoriamente à reta de normalidade. A suposição de normalidade é visualmente corroborada.")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Massa de Componentes Eletrônicos")
        st.markdown(r"Um analista industrial mede a massa de 30 componentes eletrônicos. Para justificar o uso de testes paramétricos, ele deve validar a normalidade visualmente.")
        st.latex(r"n=30, \quad p_i = \frac{i - 0.5}{30}, \quad Z_i = \Phi^{-1}(p_i)")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Calcular probabilidades $p_i$ e encontrar os quantis $Z_i$ correspondentes na tabela da normal padrão.")
        st.markdown(r"- Plotar os pares $(Z_i, X_{(i)})$ no plano cartesiano.")
        st.markdown(r"- Traçar uma reta de regressão baseada no primeiro e terceiro quartis para observar a aderência.")
        st.success(r"Conclusão: Se os pontos $(Z_i, X_{(i)})$ seguem a reta de referência com inclinação positiva, a suposição de normalidade é validada para inferência paramétrica.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDMgLSBUw7NwaWNvIDMuMTogVGVzdGUgZGUgYWRlcsOqbmNpYSBwYXJhIG5vcm1hbGlkYWRlIiwgInF1ZXN0b2VzX211bHRpcGxhX2VzY29saGEiOiBbeyJlbnVuY2lhZG8iOiAiVW0gZW5nZW5oZWlybyBkZSBjb250cm9sZSBkZSBxdWFsaWRhZGUgZXN0w6EgYW5hbGlzYW5kbyBhIGRpc3RyaWJ1acOnw6NvIGRlIHRlbnPDtWVzIGRlIHJ1cHR1cmEgZGUgdW1hIGFtb3N0cmEgZGUgJG49NjAkIGNvbXBvbmVudGVzIG1ldMOhbGljb3MuIFBhcmEgdXRpbGl6YXIgdMOpY25pY2FzIHBhcmFtw6l0cmljYXMgcXVlIHByZXNzdXDDtWVtIGEgbm9ybWFsaWRhZGUgZG9zIGRhZG9zLCBlbGUgcmVhbGl6YSB1bSB0ZXN0ZSBkZSBhZGVyw6puY2lhIG9uZGUgY29tcGFyYSBhIGZ1bsOnw6NvIGRlIGRpc3RyaWJ1acOnw6NvIGVtcMOtcmljYSAkRl9lKHgpJCBjb20gYSBmdW7Dp8OjbyBkZSBkaXN0cmlidWnDp8OjbyBhY3VtdWxhZGEgJEZfezB9KHgpJCBkZSB1bWEgJE4oXGJhcntYfSwgU14yKSQuIENvbnNpZGVyYW5kbyBvIGZvcm1hbGlzbW8gZG8gdGVzdGUgZGUgYWRlcsOqbmNpYSwgcXVhbCBkYXMgYWx0ZXJuYXRpdmFzIGFiYWl4byBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgbyBvYmpldGl2byBmdW5kYW1lbnRhbCBkZXN0YSBhbsOhbGlzZT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIlZlcmlmaWNhciBzZSBhIHZhcmnDom5jaWEgYW1vc3RyYWwgJFNeMiQgw6kgZXN0YXRpc3RpY2FtZW50ZSBpZ3VhbCBhIHplcm8gcGFyYSBnYXJhbnRpciBhIHByZWNpc8OjbyBkbyBwcm9jZXNzby4iLCAiQiI6ICJBdmFsaWFyIHNlIGEgZGlmZXJlbsOnYSBhYnNvbHV0YSBlbnRyZSAkRl9lKHgpJCBlICRGX3swfSh4KSQgw6kgc3VmaWNpZW50ZW1lbnRlIHBlcXVlbmEgZW0gdG9kbyBvIGRvbcOtbmlvICR4IFxcaW4gXFxtYXRoYmJ7Un0kLCBzdXN0ZW50YW5kbyBhIGhpcMOzdGVzZSAkSF8wOiBGKHgpID0gRl97MH0oeCkkLiIsICJDIjogIkRldGVybWluYXIgc2UgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBzZSBhcHJveGltYSBkYSBtw6lkaWEgcG9wdWxhY2lvbmFsICRcXG11JCBzb2IgYSBwcmVtaXNzYSBkZSBxdWUgb3MgZGFkb3Mgc2VndWVtIHVtYSBkaXN0cmlidWnDp8OjbyBCaW5vbWlhbC4iLCAiRCI6ICJUZXN0YXIgYSBoaXDDs3Rlc2UgYWx0ZXJuYXRpdmEgJEhfMTogRih4KSA9IEZfezB9KHgpJCwgY29uZmlybWFuZG8gcXVlIG9zIGRhZG9zIG7Do28gc2VndWVtIHVtYSBkaXN0cmlidWnDp8OjbyBOb3JtYWwuIiwgIkUiOiAiQ2FsY3VsYXIgYSBwcm9iYWJpbGlkYWRlIGRlIGVycm8gdGlwbyBJSSAoJFxcYmV0YSQpIHNlbSBjb25zaWRlcmFyIGEgZi5kLmEuIHRlw7NyaWNhIHNvYiBhIGhpcMOzdGVzZSBudWxhLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBvIHRlc3RlIGRlIGFkZXLDqm5jaWEgZm9jYSBuYSBkaXZlcmfDqm5jaWEgZW50cmUgbyBjb21wb3J0YW1lbnRvIG9ic2VydmFkbyAoYW1vc3RyYWwpIGUgbyBtb2RlbG8gdGXDs3JpY28gZXNwZXJhZG8gc29iIGEgbm9ybWFsaWRhZGUuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGFsdGVybmF0aXZhIEIgZXN0w6EgY29ycmV0YS4gTyB0ZXN0ZSBkZSBhZGVyw6puY2lhLCBubyBjb250ZXh0byBkZSBub3JtYWxpZGFkZSwgYnVzY2EgdmVyaWZpY2FyIHNlIGEgZGlzdHJpYnVpw6fDo28gYWN1bXVsYWRhIG9ic2VydmFkYSwgJEZfZSh4KSQsIGRpdmVyZ2UgZGUgZm9ybWEgZXN0YXRpc3RpY2FtZW50ZSBzaWduaWZpY2F0aXZhIGRhIGRpc3RyaWJ1acOnw6NvIGFjdW11bGFkYSB0ZcOzcmljYSwgJEZfMCh4KSQsIGRlZmluaWRhIHNvYiAkSF8wJC4gU2UgYSBkaXZlcmfDqm5jaWEgZm9yIG11aXRvIGdyYW5kZSwgYSBoaXDDs3Rlc2UgZGUgbm9ybWFsaWRhZGUgw6kgcmVqZWl0YWRhLiBBIG5vdGHDp8OjbyBmb3JtYWwgw6kgJEhfMDogRih4KSA9IEZfMCh4KSQsIGltcGxpY2FuZG8gcXVlIG8gZGVzdmlvIG3DoXhpbW8gZW50cmUgZXN0YXMgZnVuw6fDtWVzIMOpIGEgbcOpdHJpY2EgZnVuZGFtZW50YWwgcGFyYSBhIHRvbWFkYSBkZSBkZWNpc8Ojby4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9Wy0zLCAtMiwgLTEsIDAsIDEsIDIsIDNdLCB5PVswLCAwLjA1LCAwLjIsIDAuNSwgMC44LCAwLjk1LCAxXSwgbmFtZT1yXCIkRl8wKHgpJCAoVGXDs3JpY2EpXCIsIGxpbmU9ZGljdChjb2xvcj1cIiMxRTNBOEFcIiwgd2lkdGg9MykpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9Wy0zLCAtMiwgLTEsIDAsIDEsIDIsIDNdLCB5PVswLjAyLCAwLjA4LCAwLjI1LCAwLjQ1LCAwLjc1LCAwLjkyLCAxXSwgbmFtZT1yXCIkRl9lKHgpJCAoRW1ww61yaWNhKVwiLCBsaW5lPWRpY3QoY29sb3I9XCIjMTBCOTgxXCIsIHdpZHRoPTMsIGRhc2g9J1xcZG90JykpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9clwiPGI+Q29tcGFyYcOnw6NvIGVudHJlICRGXzAoeCkkIGUgJEZfZSh4KSQ8L2I+XCIsIHhheGlzX3RpdGxlPXJcIlZhbG9yIE9ic2VydmFkbyAoJHgkKVwiLCB5YXhpc190aXRsZT1yXCJQcm9iYWJpbGlkYWRlIEFjdW11bGFkYVwiLCB0ZW1wbGF0ZT1cInBsb3RseV93aGl0ZVwiKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBjbMOtbmljbyBjb20gJG49MTUwJCBwYWNpZW50ZXMsIHVtIHBlc3F1aXNhZG9yIHRlc3RhIHNlIG8gdGVtcG8gZGUgcmVjdXBlcmHDp8OjbyBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gTm9ybWFsLiBBcMOzcyByZWFsaXphciBvIHByb2NlZGltZW50byBkZSBhZGVyw6puY2lhLCBvIHNvZnR3YXJlIGVzdGF0w61zdGljbyByZXBvcnRhIHVtICRwXFx0ZXh0ey12YWxvcn0gPSAwLjAyNCQuIEFzc3VtaW5kbyB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLjA1JCwgcXVhbCDDqSBhIGludGVycHJldGHDp8OjbyBlc3RhdGlzdGljYW1lbnRlIGNvcnJldGEgcGFyYSBvIHJlc3VsdGFkbyBvYnRpZG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJDb21vICRwXFx0ZXh0ey12YWxvcn0gPCBcXGFscGhhJCwgbsOjbyByZWplaXRhbW9zICRIXzAkLCBjb25jbHVpbmRvIHF1ZSBhIG5vcm1hbGlkYWRlIMOpIHVtYSBoaXDDs3Rlc2UgYWNlaXTDoXZlbC4iLCAiQiI6ICJDb21vICRwXFx0ZXh0ey12YWxvcn0gPiBcXGFscGhhJCwgcmVqZWl0YW1vcyAkSF8wJCwgaW5kaWNhbmRvIGZvcnRlIGV2aWTDqm5jaWEgY29udHJhIGEgbm9ybWFsaWRhZGUuIiwgIkMiOiAiQ29tbyAkcFxcdGV4dHstdmFsb3J9IDwgXFxhbHBoYSQsIHJlamVpdGFtb3MgJEhfMCQsIGluZGljYW5kbyBxdWUgb3MgZGFkb3MgYXByZXNlbnRhbSBkZXN2aW9zIHNpZ25pZmljYXRpdm9zIGRhIG5vcm1hbGlkYWRlIHRlw7NyaWNhLiIsICJEIjogIk8gJHBcXHRleHR7LXZhbG9yfSQgw6kgaW5jb25jbHVzaXZvIHBvaXMgbyB0YW1hbmhvIGFtb3N0cmFsICRuPTE1MCQgZXhpZ2UgdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIG1lbm9yIHF1ZSAwLjAxLiIsICJFIjogIkEgbm9ybWFsaWRhZGUgw6kgY29uZmlybWFkYSBwb2lzICRwXFx0ZXh0ey12YWxvcn0kIGVzdMOhIGFiYWl4byBkZSAwLjA1LCBvIHF1ZSBnYXJhbnRlIGEgdmFsaWRhZGUgZG9zIHRlc3RlcyBwYXJhbcOpdHJpY29zLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiQ29tcGFyZSBvICRwXFx0ZXh0ey12YWxvcn0kIGNvbSBvICRcXGFscGhhJCBlc3RpcHVsYWRvLiBPIHF1ZSBzaWduaWZpY2EgcmVqZWl0YXIgJEhfMCQgbm8gY29udGV4dG8gZGUgYWRlcsOqbmNpYT8iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgYWx0ZXJuYXRpdmEgQyBlc3TDoSBjb3JyZXRhLiBBIHJlZ3JhIGRlIGRlY2lzw6NvIGVtIHRlc3RlcyBkZSBoaXDDs3Rlc2VzIGVzdGFiZWxlY2UgcXVlIHNlIG8gJHBcXHRleHR7LXZhbG9yfSA8IFxcYWxwaGEkLCBkZXZlbW9zIHJlamVpdGFyICRIXzAkLiBDb21vICQwLjAyNCA8IDAuMDUkLCBhIGhpcMOzdGVzZSBkZSBxdWUgYSBmdW7Dp8OjbyBkZSBkaXN0cmlidWnDp8OjbyBkYSBwb3B1bGHDp8OjbyAkRih4KSQgw6kgaWd1YWwgw6AgZGlzdHJpYnVpw6fDo28gTm9ybWFsICRGXzAoeCkkIMOpIHJlamVpdGFkYS4gSXNzbyBzaWduaWZpY2EgcXVlIGEgZXZpZMOqbmNpYSBhbW9zdHJhbCBjb250cmEgYSBub3JtYWxpZGFkZSDDqSBlc3RhdGlzdGljYW1lbnRlIHNpZ25pZmljYXRpdmEgYW8gbsOtdmVsIGRlIDUlLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXhwZXJpbWVudG8gZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlIGVtIHVtYSBsaW5oYSBkZSBwcm9kdcOnw6NvIGRlIG1pY3JvY2hpcHMsIG9ic2Vydm91LXNlIHF1ZSBvIG7Dum1lcm8gZGUgZmFsaGFzIHBvciBsb3RlIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyB0ZcOzcmljYSBlc3BlY8OtZmljYS4gUGFyYSB2YWxpZGFyIGVzc2EgaGlww7N0ZXNlLCBvIGVuZ2VuaGVpcm8gcmVzcG9uc8OhdmVsIGNvbGV0b3UgdW1hIGFtb3N0cmEgZGUgJG4gPSAyMDAkIGxvdGVzIGUgZGl2aWRpdSBvcyBkYWRvcyBlbSAkayA9IDQkIGludGVydmFsb3MgZGUgY2xhc3NlLCBvYnRlbmRvIGFzIHNlZ3VpbnRlcyBmcmVxdcOqbmNpYXMgb2JzZXJ2YWRhcyAoJE9faSQpOiAkT18xID0gNDAkLCAkT18yID0gNjAkLCAkT18zID0gNTAkIGUgJE9fNCA9IDUwJC4gU29iIGEgaGlww7N0ZXNlIG51bGEgZGUgYWRlcsOqbmNpYSBhIHVtYSBkaXN0cmlidWnDp8OjbyB0ZcOzcmljYSwgYXMgZnJlcXXDqm5jaWFzIGVzcGVyYWRhcyAoJEVfaSQpIGZvcmFtIGNhbGN1bGFkYXMgY29tbyAkRV8xID0gNTAkLCAkRV8yID0gNTAkLCAkRV8zID0gNTAkIGUgJEVfNCA9IDUwJC4gQ29uc2lkZXJhbmRvIGEgbWV0b2RvbG9naWEgUXVpLVF1YWRyYWRvIHBhcmEgdGVzdGVzIGRlIGFkZXLDqm5jaWEsIHF1YWwgw6kgbyB2YWxvciBkYSBlc3RhdMOtc3RpY2EgJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0kIGUgc3VhIGNvbmNsdXPDo28gcGFyYSB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLDA1JCAodmFsb3IgY3LDrXRpY28gJFxcY2hpXjJfe1xcdGV4dHtjcml0fX0gPSA3LDgxNSQgcGFyYSAzIGdyYXVzIGRlIGxpYmVyZGFkZSk/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSA9IDQsMCQ7IG7Do28gc2UgcmVqZWl0YSAkSF8wJCBwb2lzICQ0LDAgPCA3LDgxNSQuIiwgIkIiOiAiJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0gPSA0LDAkOyByZWplaXRhLXNlICRIXzAkIHBvaXMgJDQsMCA+IDcsODE1JC4iLCAiQyI6ICIkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSA9IDIsMCQ7IG7Do28gc2UgcmVqZWl0YSAkSF8wJCBwb2lzICQyLDAgPCA3LDgxNSQuIiwgIkQiOiAiJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0gPSA2LDAkOyBuw6NvIHNlIHJlamVpdGEgJEhfMCQgcG9pcyAkNiwwIDwgNyw4MTUkLiIsICJFIjogIiRcXGNoaV4yX3tcXHRleHR7Y2FsY319ID0gMTAsMCQ7IHJlamVpdGEtc2UgJEhfMCQgcG9pcyAkMTAsMCA+IDcsODE1JC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBmw7NybXVsYSAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSA9IFxcc3VtX3tpPTF9XntrfSBcXGZyYWN7KE9faSAtIEVfaSleMn17RV9pfSQuIENhbGN1bGUgYSBjb250cmlidWnDp8OjbyBkZSBjYWRhIGNsYXNzZSBlIHNvbWUgb3MgcmVzdWx0YWRvcy4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkFwbGljYW5kbyBhIGbDs3JtdWxhIGRhIGVzdGF0w61zdGljYSBRdWktUXVhZHJhZG86ICRcXGNoaV4yX3tcXHRleHR7Y2FsY319ID0gXFxmcmFjeyg0MC01MCleMn17NTB9ICsgXFxmcmFjeyg2MC01MCleMn17NTB9ICsgXFxmcmFjeyg1MC01MCleMn17NTB9ICsgXFxmcmFjeyg1MC01MCleMn17NTB9ID0gXFxmcmFjeygtMTApXjJ9ezUwfSArIFxcZnJhY3sxMF4yfXs1MH0gKyAwICsgMCA9IFxcZnJhY3sxMDB9ezUwfSArIFxcZnJhY3sxMDB9ezUwfSA9IDIgKyAyID0gNCwwJC4gQ29tIDQgY2xhc3Nlcywgb3MgZ3JhdXMgZGUgbGliZXJkYWRlIHPDo28gJGdsID0gayAtIDEgPSAzJC4gQ29tcGFyYW5kbyBvIHZhbG9yIGNhbGN1bGFkbyAoJDQsMCQpIGNvbSBvIHZhbG9yIGNyw610aWNvICgkNyw4MTUkKSwgdGVtb3MgcXVlICQ0LDAgPCA3LDgxNSQsIHBvcnRhbnRvLCBuw6NvIGjDoSBldmlkw6puY2lhcyBlc3RhdMOtc3RpY2FzIHBhcmEgcmVqZWl0YXIgYSBoaXDDs3Rlc2UgbnVsYSBkZSBhZGVyw6puY2lhLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLkJhcih4PVsnQ2xhc3NlIDEnLCAnQ2xhc3NlIDInLCAnQ2xhc3NlIDMnLCAnQ2xhc3NlIDQnXSwgeT1bNDAsIDYwLCA1MCwgNTBdLCBuYW1lPSdPYnNlcnZhZG8nLCBtYXJrZXJfY29sb3I9JyMxRTNBOEEnKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVsnQ2xhc3NlIDEnLCAnQ2xhc3NlIDInLCAnQ2xhc3NlIDMnLCAnQ2xhc3NlIDQnXSwgeT1bNTAsIDUwLCA1MCwgNTBdLCBuYW1lPSdFc3BlcmFkbycsIG1vZGU9J2xpbmVzK21hcmtlcnMnLCBsaW5lPWRpY3QoY29sb3I9JyM5OTFCMUInLCB3aWR0aD0zKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+Q29tcGFyYcOnw6NvIGRlIEZyZXF1w6puY2lhczogT2JzZXJ2YWRvIHZzIEVzcGVyYWRvPC9iPicsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnLCB4YXhpc190aXRsZT0nSW50ZXJ2YWxvcyBkZSBDbGFzc2UnLCB5YXhpc190aXRsZT0nRnJlcXXDqm5jaWEnKVxuZmlnLnVwZGF0ZV9sYXlvdXQobGVnZW5kPWRpY3Qob3JpZW50YXRpb249J2gnLCB5YW5jaG9yPSdib3R0b20nLCB5PTEuMDIsIHhhbmNob3I9J3JpZ2h0JywgeD0xKSkiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSB0ZXN0ZSBkZSBhZGVyw6puY2lhIHBhcmEgdmVyaWZpY2FyIHNlIHVtYSB2YXJpw6F2ZWwgYWxlYXTDs3JpYSBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsICROKFxcbXUsIFxcc2lnbWFeMikkLCB1bSBwZXNxdWlzYWRvciBlc3RpbW91ICRcXG11JCBlICRcXHNpZ21hXjIkIGEgcGFydGlyIGRvcyBkYWRvcywgcmVzdWx0YW5kbyBlbSAkbSA9IDIkIHBhcsOibWV0cm9zIGVzdGltYWRvcy4gU2UgbyBwZXNxdWlzYWRvciBkaXZpZGl1IG9zIGRhZG9zIGVtICRrID0gNiQgaW50ZXJ2YWxvcyBkZSBjbGFzc2UsIHF1YW50b3MgZ3JhdXMgZGUgbGliZXJkYWRlICgkZ2wkKSBkZXZlbSBzZXIgdXRpbGl6YWRvcyBuYSBjb25zdWx0YSBkYSB0YWJlbGEgZGEgZGlzdHJpYnVpw6fDo28gUXVpLVF1YWRyYWRvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiNSBncmF1cyBkZSBsaWJlcmRhZGUuIiwgIkIiOiAiNiBncmF1cyBkZSBsaWJlcmRhZGUuIiwgIkMiOiAiMyBncmF1cyBkZSBsaWJlcmRhZGUuIiwgIkQiOiAiNCBncmF1cyBkZSBsaWJlcmRhZGUuIiwgIkUiOiAiMiBncmF1cyBkZSBsaWJlcmRhZGUuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJBIGbDs3JtdWxhIGRvcyBncmF1cyBkZSBsaWJlcmRhZGUgcGFyYSB0ZXN0ZSBkZSBhZGVyw6puY2lhIHF1YW5kbyBwYXLDom1ldHJvcyBzw6NvIGVzdGltYWRvcyDDqSAkZ2wgPSBrIC0gMSAtIG0kLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSByZWdyYSBwYXJhIGRldGVybWluYXIgb3MgZ3JhdXMgZGUgbGliZXJkYWRlIGVtIHRlc3RlcyBkZSBhZGVyw6puY2lhIHF1YW5kbyBwYXLDom1ldHJvcyBwb3B1bGFjaW9uYWlzIHPDo28gZXN0aW1hZG9zIGEgcGFydGlyIGRhIGFtb3N0cmEgw6kgJGdsID0gayAtIDEgLSBtJCwgb25kZSAkayQgw6kgbyBuw7ptZXJvIGRlIGNsYXNzZXMgZSAkbSQgw6kgbyBuw7ptZXJvIGRlIHBhcsOibWV0cm9zIGVzdGltYWRvcy4gU3Vic3RpdHVpbmRvIG9zIHZhbG9yZXMsIHRlbW9zICRnbCA9IDYgLSAxIC0gMiA9IDMkLiBQb3J0YW50bywgYSBkaXN0cmlidWnDp8OjbyB1dGlsaXphZGEgcGFyYSBvIHRlc3RlIMOpIGEgJFxcY2hpXjIoMykkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIHNvYnJlIG8gdGVtcG8gZGUgdmlkYSAoZW0gaG9yYXMpIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyBjcsOtdGljb3MgZGUgdW0gc2lzdGVtYSBkZSBjb250cm9sZSwgdW1hIGFtb3N0cmEgZGUgdGFtYW5obyAkbj0xMCQgZm9pIGNvbGV0YWRhIGUgc3VibWV0aWRhIGEgdW1hIHZlcmlmaWNhw6fDo28gZGUgbm9ybWFsaWRhZGUgdmlhIGdyw6FmaWNvIGRlIHF1YW50aXMgKCRxIFxcdGltZXMgcSQpLiBPcyBwYXJlcyAkKFpfaSwgWF97KGkpfSkkIGZvcmFtIG1hcGVhZG9zLCBvbmRlICRYX3soaSl9JCBzw6NvIG9zIHZhbG9yZXMgb3JkZW5hZG9zIGRhIGFtb3N0cmEgZSAkWl9pJCBzw6NvIG9zIHF1YW50aXMgdGXDs3JpY29zIGRhIG5vcm1hbCBwYWRyw6NvICROKDAsMSkkLiBBbyBvYnNlcnZhciBvIGdyw6FmaWNvLCBub3RvdS1zZSBxdWUsIG5hcyBleHRyZW1pZGFkZXMgKGNhdWRhcyksIG9zIHBvbnRvcyBzZSBkZXN2aWFtIHNpc3RlbWF0aWNhbWVudGUgZGEgcmV0YSBkZSByZWZlcsOqbmNpYTogcGFyYSAkWl9pJCBtdWl0byBiYWl4b3MgKHZhbG9yZXMgbmVnYXRpdm9zKSwgb3MgcG9udG9zIHNpdHVhbS1zZSBhY2ltYSBkYSByZXRhLCBlIHBhcmEgJFpfaSQgbXVpdG8gYWx0b3MgKHZhbG9yZXMgcG9zaXRpdm9zKSwgb3MgcG9udG9zIHNpdHVhbS1zZSBhYmFpeG8gZGEgcmV0YS4gUXVhbCDDqSBhIGludGVycHJldGHDp8OjbyBlc3RhdMOtc3RpY2EgbWFpcyBhZGVxdWFkYSBwYXJhIGVzc2UgY29tcG9ydGFtZW50bz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk9zIGRhZG9zIGFwcmVzZW50YW0gY2F1ZGFzIGxldmVzIChkaXN0cmlidWnDp8OjbyBtYWlzIGNvbmNlbnRyYWRhIHF1ZSBhIG5vcm1hbCwgZGVub21pbmFkYSBwbGF0aWPDunJ0aWNhKS4iLCAiQiI6ICJPcyBkYWRvcyBhcHJlc2VudGFtIGNhdWRhcyBwZXNhZGFzIChkaXN0cmlidWnDp8OjbyBjb20gbWFpb3IgcHJvYmFiaWxpZGFkZSBuYXMgZXh0cmVtaWRhZGVzIHF1ZSBhIG5vcm1hbCwgZGVub21pbmFkYSBsZXB0b2PDunJ0aWNhKS4iLCAiQyI6ICJBIGFtb3N0cmEgcG9zc3VpIHVtYSBkaXN0cmlidWnDp8OjbyBwZXJmZWl0YW1lbnRlIG5vcm1hbCwgcG9pcyBkZXN2aW9zIG5hcyBjYXVkYXMgc8OjbyBlc3BlcmFkb3MgZGV2aWRvIGFvIHRhbWFuaG8gYW1vc3RyYWwgcmVkdXppZG8uIiwgIkQiOiAiT3MgZGFkb3MgZXN0w6NvIHNldmVyYW1lbnRlIGFzc2ltw6l0cmljb3Mgw6AgZGlyZWl0YSwgc3VnZXJpbmRvIG8gdXNvIGRlIHVtYSB0cmFuc2Zvcm1hw6fDo28gbG9nYXLDrXRtaWNhIGltZWRpYXRhLiIsICJFIjogIk9zIGRhZG9zIHBvc3N1ZW0gdW0gZXJybyBkZSBtZWRpw6fDo28gc2lzdGVtw6F0aWNvLCBwb2lzIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgbnVuY2EgYXByZXNlbnRhIGRlc3Zpb3MgbmFzIGV4dHJlbWlkYWRlcyBkZSB1bSBncsOhZmljbyAkcSBcXHRpbWVzIHEkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBvIGdyw6FmaWNvICRxIFxcdGltZXMgcSQgY29tcGFyYSBvcyBxdWFudGlzIGVtcMOtcmljb3MgY29tIG9zIHRlw7NyaWNvcy4gU2Ugb3MgZGFkb3MgcmVhaXMgKG9yZGVuYWRvcykgc8OjbyAnbWFpcyBjdXJ0b3MnIHF1ZSBvcyBlc3BlcmFkb3MgcGVsYSBub3JtYWwgKG91IHNlamEsIG9zIG1lbm9yZXMgdmFsb3JlcyBuw6NvIHPDo28gdMOjbyBwZXF1ZW5vcyBxdWFudG8gbyBlc3BlcmFkbyBlIG9zIG1haW9yZXMgdmFsb3JlcyBuw6NvIHPDo28gdMOjbyBncmFuZGVzIHF1YW50byBvIGVzcGVyYWRvKSwgaXNzbyBpbmRpY2EgdW1hIGRpc3RyaWJ1acOnw6NvIGNvbSBjYXVkYXMgbWFpcyBjdXJ0YXMuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGludGVycHJldGHDp8OjbyBkZSB1bSBncsOhZmljbyAkcSBcXHRpbWVzIHEkIHBhcmEgYSBub3JtYWxpZGFkZSDDqSBmdW5kYW1lbnRhbDogc2Ugb3MgcG9udG9zIHNlIGRlc3ZpYW0gZGEgcmV0YSBkZSBmb3JtYSBxdWUgZWxlcyAnYWNoYXRlbScgZW0gcmVsYcOnw6NvIMOgIGluY2xpbmHDp8OjbywgdGVtb3MgY2F1ZGFzIGxldmVzLiBRdWFuZG8gbyBxdWFudGlsIGVtcMOtcmljbyAoZWl4byBZKSDDqSBtZW5vciBxdWUgbyBlc3BlcmFkbyB0ZW9yaWNhbWVudGUgcGFyYSBvIGV4dHJlbW8gc3VwZXJpb3IgZSBtYWlvciBxdWUgbyBlc3BlcmFkbyBwYXJhIG8gZXh0cmVtbyBpbmZlcmlvciwgYSBkaXN0cmlidWnDp8OjbyB0ZW0gbWVub3MgbWFzc2EgbmFzIGNhdWRhcyBkbyBxdWUgYSBub3JtYWwsIGluZGljYW5kbyB1bWEgZGlzdHJpYnVpw6fDo28gZGUgY2F1ZGFzIGxldmVzIG91IHBsYXRpY8O6cnRpY2EuIFBvcnRhbnRvLCBhIGFsdGVybmF0aXZhIEEgZXN0w6EgY29ycmV0YS4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9Wy0yLCAtMSwgMCwgMSwgMl0sIHk9LCBuYW1lPSdSZXRhIFJlZmVyw6puY2lhJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJywgd2lkdGg9MiwgZGFzaD0nZGFzaCcpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVstMiwgLTEsIDAsIDEsIDJdLCB5PSwgbmFtZT0nRGFkb3MgUGxhdGljw7pydGljb3MnLCBtb2RlPSdtYXJrZXJzJywgbWFya2VyPWRpY3QoY29sb3I9JyM5OTFCMUInLCBzaXplPTgpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5HcsOhZmljbyBxeHE6IENhdWRhcyBMZXZlczwvYj4nLCB4YXhpc190aXRsZT0nUXVhbnRpcyBUZcOzcmljb3MgTigwLDEpJywgeWF4aXNfdGl0bGU9J1F1YW50aXMgRW1ww61yaWNvcycpXG5maWcudXBkYXRlX2xheW91dCh0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyBmb3JtYWxpc21vIGRvIGdyw6FmaWNvIGRlIHF1YW50aXMgJHEgXFx0aW1lcyBxJCBhcHJlc2VudGFkbyBubyBzdWJ0w7NwaWNvLCBvbmRlIG8gcGFyIMOpICQoWl9pLCBYX3soaSl9KSQgZSAkWl9pJCDDqSBjYWxjdWxhZG8gdmlhICRGX3tOKDAsMSl9KFpfaSkgPSBcXGZyYWN7aSAtIDAsNX17bn0kLiBQYXJhIHVtYSBhbW9zdHJhIGRlIHRhbWFuaG8gJG49NCQsIHF1YWlzIHNlcmlhbSBvcyB2YWxvcmVzIGRlICRwX2kkIHV0aWxpemFkb3MgcGFyYSBlbmNvbnRyYXIgb3MgcXVhbnRpcyB0ZcOzcmljb3MgJFpfaSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIwLjEyNSwgMC4zNzUsIDAuNjI1LCAwLjg3NSIsICJCIjogIjAuMjUsIDAuNTAsIDAuNzUsIDEuMDAiLCAiQyI6ICIwLjEsIDAuMywgMC41LCAwLjciLCAiRCI6ICIwLjIsIDAuNCwgMC42LCAwLjgiLCAiRSI6ICIwLjAsIDAuMjUsIDAuNSwgMC43NSJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiQXBsaXF1ZSBhIGbDs3JtdWxhICRwX2kgPSBcXGZyYWN7aSAtIDAsNX17bn0kIGNvbSAkbj00JCBwYXJhIG9zIMOtbmRpY2VzICRpID0gMSwgMiwgMywgNCQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJVdGlsaXphbmRvIGEgZsOzcm11bGEgZm9ybmVjaWRhIG5vIHRleHRvIGJhc2U6ICRwX2kgPSBcXGZyYWN7aSAtIDAsNX17NH0kLiBQYXJhICRpPTEkLCAkcF8xID0gXFxmcmFjezAsNX17NH0gPSAwLDEyNSQuIFBhcmEgJGk9MiQsICRwXzIgPSBcXGZyYWN7MSw1fXs0fSA9IDAsMzc1JC4gUGFyYSAkaT0zJCwgJHBfMyA9IFxcZnJhY3syLDV9ezR9ID0gMCw2MjUkLiBQYXJhICRpPTQkLCAkcF80ID0gXFxmcmFjezMsNX17NH0gPSAwLDg3NSQuIEEgYWx0ZXJuYXRpdmEgQSBjb250w6ltIGVzc2VzIHZhbG9yZXMuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAzLCBwLiA1OSJ9XSwgInF1ZXN0b2VzX2Rpc2N1cnNpdmFzIjogW3siZW51bmNpYWRvIjogIkV4cGxpcXVlLCBzb2IgYSDDs3RpY2EgZGEgZXN0YXTDrXN0aWNhIGluZmVyZW5jaWFsLCBwb3IgcXVlIGEgc3Vwb3Npw6fDo28gZGUgbm9ybWFsaWRhZGUgw6kgY3J1Y2lhbCBwYXJhIG8gdXNvIGRlIHRlc3RlcyBwYXJhbcOpdHJpY29zLiBDb21vIG8gZGVzdmlvIGVudHJlIGEgZnVuw6fDo28gZGUgZGlzdHJpYnVpw6fDo28gZW1ww61yaWNhICRGX2UoeCkkIGUgYSBmdW7Dp8OjbyBkZSBkaXN0cmlidWnDp8OjbyBhY3VtdWxhZGEgdGXDs3JpY2EgJEZfMCh4KSQgYXR1YSBjb21vIHVtICd0ZXJtw7RtZXRybycgcGFyYSBlc3NhIHZhbGlkYWRlPyIsICJkaWNhIjogIlBlbnNlIG5vIFRlb3JlbWEgZG8gTGltaXRlIENlbnRyYWwgZSBjb21vIGEgZGlzY3JlcMOibmNpYSBlbnRyZSBhIGZvcm1hIHRlw7NyaWNhIGRhIE5vcm1hbCAkTihcXG11LCBcXHNpZ21hXjIpJCBlIGEgZm9ybWEgZW1ww61yaWNhIGRvcyBkYWRvcyB2aW9sYSBhcyBwcmVtaXNzYXMgZG9zIHRlc3Rlcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gQSBzdXBvc2nDp8OjbyBkZSBub3JtYWxpZGFkZSBmdW5kYW1lbnRhIGEgY29uc3RydcOnw6NvIGRlIGVzdGF0w61zdGljYXMgZGUgdGVzdGUgY3VqYXMgZGlzdHJpYnVpw6fDtWVzIGFtb3N0cmFpcyBzw6NvIGNvbmhlY2lkYXMgKGV4OiAkdCQgZGUgU3R1ZGVudCkuIiwgIjIuIEZvcm1hbG1lbnRlLCAkSF8wOiBGKHgpID0gRl8wKHgpJC4gTyB0ZXN0ZSBkZSBhZGVyw6puY2lhIGNvbXBhcmEgYSBmLmQuZS4gJEZfZSh4KSQgY29tICRGXzAoeCkkLiIsICIzLiBPIGRlc3ZpbyDDqSBkZWZpbmlkbyBjb21vICREID0gXFxzdXBfeCB8Rl9lKHgpIC0gRl8wKHgpfCQsIHJlcHJlc2VudGFuZG8gYSBkaXN0w6JuY2lhIG3DoXhpbWEgZW50cmUgbyBtb2RlbG8gaWRlYWwgZSBvIG9ic2VydmFkby4iLCAiNC4gU2UgJEQkIGV4Y2VkZSB1bSB2YWxvciBjcsOtdGljbyBwcsOpLWRldGVybWluYWRvLCByZWplaXRhbW9zIGEgbm9ybWFsaWRhZGUgcG9pcyBvIGVycm8gZGUgYXByb3hpbWHDp8OjbyDDqSBncmFuZGUgZGVtYWlzLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtIGFuYWxpc3RhIGNvbGV0b3UgZGFkb3MgZGUgY29uc3VtbyBlbMOpdHJpY28gKCRuPTEwMCQpIGUgZGVzZWphIHJlYWxpemFyIHVtIHRlc3RlIGRlIGFkZXLDqm5jaWEuIFNhYmVuZG8gcXVlIG8gbW9kZWxvIHNvYiAkSF8wJCBhc3N1bWUgdW1hIGRpc3RyaWJ1acOnw6NvICROKDUwMCwgMTAwKSQsIG9uZGUgJFxcbXU9NTAwJCBlICRcXHNpZ21hXjI9MTAwJC4gU2UsIHBhcmEgdW0gdmFsb3IgZXNwZWPDrWZpY28gJHg9NTIwJCwgYSBmdW7Dp8OjbyBkZSBkaXN0cmlidWnDp8OjbyBlbXDDrXJpY2Egw6kgJEZfZSg1MjApID0gMC44NSQgZSBhIHRlw7NyaWNhIMOpICRGXzAoNTIwKSA9IDAuODQxMyQsIGNhbGN1bGUgbyBkZXN2aW8gYWJzb2x1dG8gbmVzdGUgcG9udG8gZSBkaXNjdXRhIGEgaW1wb3J0w6JuY2lhIGRlIHJlYWxpemFyIGVzc2EgY29tcGFyYcOnw6NvIHBhcmEgdsOhcmlvcyBwb250b3MgJHgkLiIsICJkaWNhIjogIk8gZGVzdmlvIGFic29sdXRvIGVtIHVtIHBvbnRvICR4JCDDqSBkYWRvIHBvciAkfEZfZSh4KSAtIEZfMCh4KXwkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBJZGVudGlmaWNhciBvcyB2YWxvcmVzOiAkRl9lKDUyMCkgPSAwLjg1JCBlICRGXzAoNTIwKSA9IDAuODQxMyQuIiwgIjIuIENhbGN1bGFyIG8gZGVzdmlvIGFic29sdXRvOiAkfDAuODUgLSAwLjg0MTN8ID0gMC4wMDg3JC4iLCAiMy4gSW50ZXJwcmV0YcOnw6NvOiBFc3RlIHZhbG9yIHJlcHJlc2VudGEgYSBkaXNjcmVww6JuY2lhIHBvbnR1YWwgZW50cmUgYSBhbW9zdHJhIGUgYSBjdXJ2YSB0ZcOzcmljYS4iLCAiNC4gQSBhbsOhbGlzZSBkZXZlIHNlciBnbG9iYWwgKHN1cHJlbW8pIHBhcmEgZ2FyYW50aXIgcXVlIGEgYWRlcsOqbmNpYSBzZWphIHbDoWxpZGEgcGFyYSB0b2RvIG8gZXNwZWN0cm8gZGEgZGlzdHJpYnVpw6fDo28uIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLkJhcih4PVsnRGlzY3JlcMOibmNpYSddLCB5PVswLjAwODddLCBtYXJrZXJfY29sb3I9JyM5OTFCMUInKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5EZXN2aW8gQWJzb2x1dG8gZW0gJHg9NTIwJDwvYj4nLCB5YXhpc190aXRsZT0nVmFsb3InLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMDA4N30sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyYW5kbyB1bSB0ZXN0ZSBkZSBhZGVyw6puY2lhIGNvbSAkbiQgb2JzZXJ2YcOnw7VlcywgYW5hbGlzZSBjb21vIG8gYXVtZW50byBkbyB0YW1hbmhvIGFtb3N0cmFsICRuJCBhZmV0YSBhIHNlbnNpYmlsaWRhZGUgZG8gdGVzdGUgYW8gcmVqZWl0YXIgYSBoaXDDs3Rlc2UgbnVsYSAkSF8wJC4gUG9yIHF1ZSBhbW9zdHJhcyBtdWl0byBncmFuZGVzIHBvZGVtIGxldmFyIMOgIHJlamVpw6fDo28gZGUgJEhfMCQgbWVzbW8gcGFyYSBkZXN2aW9zIGRlc3ByZXrDrXZlaXMgZGEgbm9ybWFsaWRhZGU/IiwgImRpY2EiOiAiQ29uc2lkZXJlIHF1ZSBhIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSBkZXBlbmRlIGRpcmV0YW1lbnRlIGRlICRuJCBlIGRhIHByZWNpc8OjbyBkYSBlc3RpbWF0aXZhIGRlICRGX2UoeCkkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBBIGYuZC5lLiAkRl9lKHgpJCBjb252ZXJnZSBwYXJhIGEgZi5kLmEuIHBvcHVsYWNpb25hbCDDoCBtZWRpZGEgcXVlICRuIFxcdG8gXFxpbmZ0eSQuIiwgIjIuIENvbSAkbiQgZWxldmFkbywgbyB0ZXN0ZSB0b3JuYS1zZSBleHRyZW1hbWVudGUgc2Vuc8OtdmVsLCBpZGVudGlmaWNhbmRvIGRpc2NyZXDDom5jaWFzIG3DrW5pbWFzIGVudHJlICRGX2UoeCkkIGUgJEZfMCh4KSQuIiwgIjMuIEVtIGdyYW5kZXMgYW1vc3RyYXMsIGRlc3Zpb3MgXFxtaW7DunNjdWxvcyBxdWUgbsOjbyBwb3NzdWVtIGltcGFjdG8gcHLDoXRpY28gcG9kZW0gcmVzdWx0YXIgZW0gdW0gJHBcXHRleHR7LXZhbG9yfSA8IFxcYWxwaGEkLiIsICI0LiBDb25jbHVzw6NvOiBFc3RhdGlzdGljYW1lbnRlIHNpZ25pZmljYXRpdm8gbmVtIHNlbXByZSBpbXBsaWNhIHRlY25pY2FtZW50ZSByZWxldmFudGUgZW0gbW9kZWxvcyBkZSBncmFuZGVzIGJhc2VzIGRlIGRhZG9zLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtYSBlbXByZXNhIGRlIFRJIHJlZ2lzdHJvdSBvIHRlbXBvIGRlIHByb2Nlc3NhbWVudG8gZGUgNDAwIHJlcXVpc2nDp8O1ZXMgZW0gc2V1IHNlcnZpZG9yLiBTb2IgYSBoaXDDs3Rlc2UgbnVsYSBkZSBxdWUgbyB0ZW1wbyBkZSBwcm9jZXNzYW1lbnRvIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwsIG8gc2Vydmlkb3IgZm9pIHBhcnRpY2lvbmFkbyBlbSA1IGludGVydmFsb3MgZGUgZnJlcXXDqm5jaWEuIE9zIGRhZG9zIG9ic2VydmFkb3MgZm9yYW06ICRPXzE9NTAsIE9fMj0xMTAsIE9fMz0xMzAsIE9fND04MCwgT181PTMwJC4gU2FiZW5kbyBxdWUgYXMgZnJlcXXDqm5jaWFzIGVzcGVyYWRhcyBzb2Igbm9ybWFsaWRhZGUgc8OjbyAkRV8xPTQwLCBFXzI9MTAwLCBFXzM9MTQwLCBFXzQ9OTAsIEVfNT0zMCQsIGNhbGN1bGUgYSBlc3RhdMOtc3RpY2EgJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0kIGUgZGV0ZXJtaW5lIHNlIGEgaGlww7N0ZXNlIGRlIG5vcm1hbGlkYWRlIGRldmUgc2VyIHJlamVpdGFkYSBhbyBuw612ZWwgZGUgJFxcYWxwaGE9MCwwNSQgKHZhbG9yIGNyw610aWNvICRcXGNoaV4yX3tcXHRleHR7Y3JpdH19ID0gOSw0ODgkIHBhcmEgNCBncmF1cyBkZSBsaWJlcmRhZGUpLiIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSA9IFxcc3VtX3tpPTF9Xns1fSBcXGZyYWN7KE9faSAtIEVfaSleMn17RV9pfSQgZSBjb21wYXJlIG8gcmVzdWx0YWRvIGZpbmFsIGNvbSBvIHZhbG9yIGNyw610aWNvIGZvcm5lY2lkby4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogQ2FsY3VsYXIgYXMgZGlmZXJlbsOnYXMgcXVhZHLDoXRpY2FzIHJlbGF0aXZhcyBwYXJhIGNhZGEgY2xhc3NlIGkuIiwgIkNsYXNzZSAxOiAkKDUwLTQwKV4yIC8gNDAgPSAxMDAgLyA0MCA9IDIsNSQuIiwgIkNsYXNzZSAyOiAkKDExMC0xMDApXjIgLyAxMDAgPSAxMDAgLyAxMDAgPSAxLDAkLiIsICJDbGFzc2UgMzogJCgxMzAtMTQwKV4yIC8gMTQwID0gMTAwIC8gMTQwIFxcYXBwcm94IDAsNzE0JC4iLCAiQ2xhc3NlIDQ6ICQoODAtOTApXjIgLyA5MCA9IDEwMCAvIDkwIFxcYXBwcm94IDEsMTExJC4iLCAiQ2xhc3NlIDU6ICQoMzAtMzApXjIgLyAzMCA9IDAkLiIsICJQYXNzbyAyOiBTb21hciBvcyB2YWxvcmVzIHBhcmEgZW5jb250cmFyICRcXGNoaV4yX3tcXHRleHR7Y2FsY319ID0gMiw1ICsgMSwwICsgMCw3MTQgKyAxLDExMSArIDAgPSA1LDMyNSQuIiwgIlBhc3NvIDM6IENvbXBhcmFyIGNvbSBvIHZhbG9yIGNyw610aWNvLiBDb21vICQ1LDMyNSA8IDksNDg4JCwgY29uY2x1w61tb3MgcXVlIG7Do28gaMOhIGV2aWTDqm5jaWFzIHBhcmEgcmVqZWl0YXIgJEhfMCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiA1LjMyNX0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCBkbyBwb250byBkZSB2aXN0YSBjb25jZWl0dWFsLCBwb3IgcXVlIGEgbm9ybWFsaXphw6fDo28gZGEgZGlmZXJlbsOnYSBwZWxhIGZyZXF1w6puY2lhIGVzcGVyYWRhICQoT19pIC0gRV9pKV4yIC8gRV9pJCDDqSBlc3NlbmNpYWwgcGFyYSBvIHRlc3RlIFF1aS1RdWFkcmFkby4gTyBxdWUgYWNvbnRlY2VyaWEgY29tIGEgZXN0YXTDrXN0aWNhIHNlIGlnbm9yw6Fzc2Vtb3MgbyBkZW5vbWluYWRvciAkRV9pJD8iLCAiZGljYSI6ICJDb25zaWRlcmUgYSBtYWduaXR1ZGUgZGFzIGZyZXF1w6puY2lhcyBlc3BlcmFkYXMuIFNlIHVtYSBjbGFzc2UgdGVtIGV4cGVjdGF0aXZhIGRlIDEuMDAwIGV2ZW50b3MgZSBvdXRyYSBkZSAxMCwgbyBtZXNtbyBkZXN2aW8gYWJzb2x1dG8gZGUgNSB1bmlkYWRlcyB0ZW0gaW1wYWN0b3MgbXVpdG8gZGlmZXJlbnRlcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSBlc3RhdMOtc3RpY2EgUXVpLVF1YWRyYWRvIHV0aWxpemEgYSByYXrDo28gJChPX2kgLSBFX2kpXjIgLyBFX2kkIHBhcmEgcmVhbGl6YXIgdW1hIHBvbmRlcmHDp8OjbyByZWxhdGl2YSBkbyBlcnJvLiIsICJTZSBpZ25vcsOhc3NlbW9zICRFX2kkLCBlc3RhcsOtYW1vcyB0cmF0YW5kbyBkZXN2aW9zIGVtIGNsYXNzZXMgY29tIGZyZXF1w6puY2lhcyBtdWl0byBiYWl4YXMgZGEgbWVzbWEgZm9ybWEgcXVlIGRlc3Zpb3MgZW0gY2xhc3NlcyBjb20gZnJlcXXDqm5jaWFzIG11aXRvIGFsdGFzLiIsICJBIGRpdmlzw6NvIHBvciAkRV9pJCBnYXJhbnRlIHF1ZSB1bWEgZmx1dHVhw6fDo28gYWxlYXTDs3JpYSBlbSB1bWEgY2xhc3NlIGVzcGVyYWRhIHBlcXVlbmEgbsOjbyBkb21pbmUgaW5qdXN0YW1lbnRlIG8gY8OhbGN1bG8gZGEgZXN0YXTDrXN0aWNhIGdsb2JhbCwgc2VuZG8gZXNzZW5jaWFsIHBhcmEgYSBlc3RhYmlsaWRhZGUgZG8gdGVzdGUgZW0gZGlmZXJlbnRlcyBtYWduaXR1ZGVzIGRlIGNvbnRhZ2VtLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtIGdlbmV0aWNpc3RhIGRlc2VqYSB0ZXN0YXIgc2UgdW0gY3J1emFtZW50byBzZWd1ZSBhIHByb3BvcsOnw6NvIGVzcGVyYWRhIGRlIDk6MzozOjEgZW0gcXVhdHJvIGZlbsOzdGlwb3MuIEVsZSBvYnTDqW0gdW1hIGFtb3N0cmEgZGUgJG4gPSAxNjAkIGluZGl2w61kdW9zIGUgb2JzZXJ2YTogJE9fMT05NSwgT18yPTI1LCBPXzM9MzAsIE9fND0xMCQuIENhbGN1bGUgYXMgZnJlcXXDqm5jaWFzIGVzcGVyYWRhcyAkRV9pJCBlIGEgZXN0YXTDrXN0aWNhICRcXGNoaV4yX3tcXHRleHR7Y2FsY319JC4iLCAiZGljYSI6ICJBcyBwcm9iYWJpbGlkYWRlcyB0ZcOzcmljYXMgc8OjbyAkcF8xID0gOS8xNiwgcF8yID0gMy8xNiwgcF8zID0gMy8xNiwgcF80ID0gMS8xNiQuIExlbWJyZS1zZSBxdWUgJEVfaSA9IG4gXFxjZG90IHBfaSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IENhbGN1bGFyIGZyZXF1w6puY2lhcyBlc3BlcmFkYXM6ICRFXzEgPSAxNjAgXFxjZG90ICg5LzE2KSA9IDkwJCwgJEVfMiA9IDE2MCBcXGNkb3QgKDMvMTYpID0gMzAkLCAkRV8zID0gMTYwIFxcY2RvdCAoMy8xNikgPSAzMCQsICRFXzQgPSAxNjAgXFxjZG90ICgxLzE2KSA9IDEwJC4iLCAiUGFzc28gMjogQ2FsY3VsYXIgYSBlc3RhdMOtc3RpY2E6ICRcXGNoaV4yX3tcXHRleHR7Y2FsY319ID0gXFxmcmFjeyg5NS05MCleMn17OTB9ICsgXFxmcmFjeygyNS0zMCleMn17MzB9ICsgXFxmcmFjeygzMC0zMCleMn17MzB9ICsgXFxmcmFjeygxMC0xMCleMn17MTB9JC4iLCAiUGFzc28gMzogUmVzb2x2ZXIgYXMgZnJhw6fDtWVzOiAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3syNX17OTB9ICsgXFxmcmFjezI1fXszMH0gKyAwICsgMCA9IDAsMjc3OCArIDAsODMzMyA9IDEsMTExMSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAxLjExMTF9LCB7ImVudW5jaWFkbyI6ICJEYWRhIHVtYSBhbW9zdHJhIGRlIHRhbWFuaG8gJG49NCQgY29tIG9zIHZhbG9yZXMgb3JkZW5hZG9zICRYX3soMSl9PTEwLCBYX3soMil9PTEyLCBYX3soMyl9PTE1LCBYX3soNCl9PTIwJCwgZGV0ZXJtaW5lIG9zIHF1YW50aXMgdGXDs3JpY29zICRaX2kkIGNvcnJlc3BvbmRlbnRlcyAodXRpbGl6YW5kbyBhIFRhYmVsYSBkYSBOb3JtYWwgUGFkcsOjbyBvdSBjb25oZWNpbWVudG8gdGXDs3JpY28pIGUgZGVzY3JldmEgY29tbyBlc3NlcyBwb250b3Mgc2VyaWFtIGRpc3Bvc3RvcyBlbSB1bSBncsOhZmljbyAkcSBcXHRpbWVzIHEkLiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgJFpfaSQgw6kgbyB2YWxvciB0YWwgcXVlICRQKFogXFxsZSBaX2kpID0gcF9pJC4gVXNlIG9zIHZhbG9yZXMgZGUgJHBfaSQgY2FsY3VsYWRvcyBuYSBxdWVzdMOjbyBhbnRlcmlvciAoMC4xMjUsIDAuMzc1LCAwLjYyNSwgMC44NzUpLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiBDYWxjdWxhciBhcyBwcm9iYWJpbGlkYWRlcyAkcF9pID0gXFxmcmFje2kgLSAwLDV9ezR9JC4gVGVtb3MgJHBfMT0wLDEyNSwgcF8yPTAsMzc1LCBwXzM9MCw2MjUsIHBfND0wLDg3NSQuIiwgIlBhc3NvIDI6IEVuY29udHJhciBvcyBxdWFudGlzIHRlw7NyaWNvcyAkWl9pJCBuYSAkTigwLDEpJC4gVXNhbmRvIHRhYmVsYXMsICRaXzEgXFxhcHByb3ggLTEsMTUkLCAkWl8yIFxcYXBwcm94IC0wLDMyJCwgJFpfMyBcXGFwcHJveCAwLDMyJCwgJFpfNCBcXGFwcHJveCAxLDE1JC4iLCAiUGFzc28gMzogT3MgcG9udG9zIGRvIGdyw6FmaWNvICRxIFxcdGltZXMgcSQgc2Vyw6NvIG9zIHBhcmVzOiAkKC0xLDE1OyAxMCksICgtMCwzMjsgMTIpLCAoMCwzMjsgMTUpLCAoMSwxNTsgMjApJC4iLCAiUGFzc28gNDogRGlzcG9zacOnw6NvOiBPYnNlcnZhLXNlIG8gYWxpbmhhbWVudG8gZGVzc2VzIHBvbnRvcyBlbSByZWxhw6fDo28gYSB1bWEgcmV0YS4gQSBpbmNsaW5hw6fDo28gZGEgcmV0YSBpbmRpY2FyaWEgbyBkZXN2aW8gcGFkcsOjbyBkYSBhbW9zdHJhLCBlbnF1YW50byBhIGludGVyY2VwdGHDp8OjbyBpbmRpY2EgYSBtw6lkaWEuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD0sIHk9WzEwLCAxMiwgMTUsIDIwXSwgbW9kZT0nbWFya2VycytsaW5lcycsIG1hcmtlcj1kaWN0KGNvbG9yPScjMUUzQThBJywgc2l6ZT0xMCkpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkdyw6FmaWNvIHF4cSBBbW9zdHJhIG49NDwvYj4nLCB4YXhpc190aXRsZT0nUXVhbnRpcyBUZcOzcmljb3MgKCRaX2kkKScsIHlheGlzX3RpdGxlPSdRdWFudGlzIEVtcMOtcmljb3MgKCRYX3soaSl9JCknKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlIGEgZGlmZXJlbsOnYSBjb25jZWl0dWFsIGVudHJlIHVzYXIgdW0gaGlzdG9ncmFtYSBlIHVtIGdyw6FmaWNvICRxIFxcdGltZXMgcSQgcGFyYSBkaWFnbm9zdGljYXIgYSBub3JtYWxpZGFkZSBkZSB1bSBjb25qdW50byBkZSBkYWRvcy4iLCAiZGljYSI6ICJDb25zaWRlcmUgcXVlIG8gaGlzdG9ncmFtYSDDqSB1bWEgZXN0aW1hdGl2YSBkZSBkZW5zaWRhZGUsIGVucXVhbnRvIG8gZ3LDoWZpY28gJHEgXFx0aW1lcyBxJCBmb2NhIG5hIGNvbXBhcmHDp8OjbyBkZSBxdWFudGlzIGFjdW11bGFkb3MuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIk8gaGlzdG9ncmFtYSBvZmVyZWNlIHVtYSB2aXPDo28gZGEgZm9ybWEgZGEgZGlzdHJpYnVpw6fDo28gKGRlbnNpZGFkZSBkZSBmcmVxdcOqbmNpYSksIHBlcm1pdGluZG8gaWRlbnRpZmljYXIgYXNzaW1ldHJpYSBlIG11bHRpbW9kYWxpZGFkZSBkZSBmb3JtYSBpbnR1aXRpdmEuIiwgIk8gZ3LDoWZpY28gJHEgXFx0aW1lcyBxJCDDqSBtYWlzIHJpZ29yb3NvLCBjb21wYXJhbmRvIGEgZGlzdHJpYnVpw6fDo28gZW1ww61yaWNhIGNvbSBhIHRlw7NyaWNhIHBvbnRvIGEgcG9udG8gKHF1YW50aWwgYSBxdWFudGlsKS4iLCAiRGVzdmlvcyBuYXMgY2F1ZGFzIHPDo28gbXVpdG8gbWFpcyBmw6FjZWlzIGRlIGRpYWdub3N0aWNhciBubyBncsOhZmljbyAkcSBcXHRpbWVzIHEkIGRvIHF1ZSBubyBoaXN0b2dyYW1hLCBvbmRlIG8gYWdydXBhbWVudG8gZGUgb2JzZXJ2YcOnw7VlcyBlbSBiYXJyYXMgcG9kZSBtYXNjYXJhciBvIGNvbXBvcnRhbWVudG8gZGEgY2F1ZGEuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTYsIHAuIDQ3MCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJTdXBvbmhhIHF1ZSwgYW8gYW5hbGlzYXIgb3MgcmVzw61kdW9zIGRlIHVtYSByZWdyZXNzw6NvIGxpbmVhciwgbyBncsOhZmljbyAkcSBcXHRpbWVzIHEkIGV4aWJhIHVtYSBjdXJ2YXR1cmEgZW0gZm9ybWEgZGUgJ1MnLiBPIHF1ZSBlc3NhIGZvcm1hIGluZGljYSBzb2JyZSBhIGRpc3RyaWJ1acOnw6NvIGRvcyByZXPDrWR1b3MgZW0gcmVsYcOnw6NvIMOgIGhpcMOzdGVzZSBkZSBub3JtYWxpZGFkZT8iLCAiZGljYSI6ICJSZWZsaXRhIHNvYnJlIGNvbW8gdmFsb3JlcyBkaXNjcmVwYW50ZXMgb3UgY29tcG9ydGFtZW50b3MgbsOjbyBsaW5lYXJlcyBuYXMgY2F1ZGFzIGFmZXRhbSBvIGFsaW5oYW1lbnRvIGRvcyBwb250b3MgZW0gcmVsYcOnw6NvIMOgIHJldGEgJHk9eCQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlVtYSBjdXJ2YXR1cmEgZW0gJ1MnIGluZGljYSBxdWUgYSBkaXN0cmlidWnDp8OjbyBkb3MgZGFkb3MgcG9zc3VpIGNhdWRhcyBtYWlzIHBlc2FkYXMgb3UgbWFpcyBsZXZlcyBkbyBxdWUgdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCAoY3VydG9zZSBleGNlc3NpdmEpLiIsICJDb25jcmV0YW1lbnRlLCBzZSBhIGN1cnZhIHNvYmUgcmFwaWRhbWVudGUgbm8gXFxpbsOtY2lvIGUgdGVybWluYSBhY2ltYSBkYSByZXRhIG5vIGZpbmFsLCBpc3NvIHNpbmFsaXphIHVtYSBkaXN0cmlidWnDp8OjbyBsZXB0b2PDunJ0aWNhIChjYXVkYXMgcGVzYWRhcykuIiwgIklzc28gdmlvbGEgYSBzdXBvc2nDp8OjbyBkZSBub3JtYWxpZGFkZSBkb3MgcmVzw61kdW9zLCBleGlnaW5kbyB1bWEgcmVhdmFsaWHDp8OjbyBkbyBtb2RlbG8sIHBvc3NpdmVsbWVudGUgYXRyYXbDqXMgZGUgdHJhbnNmb3JtYcOnw7VlcyBuYSB2YXJpw6F2ZWwgcmVzcG9zdGEuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bLTIsIC0xLCAwLCAxLCAyXSwgeT1bLTIsIC0xLCAwLCAxLCAyXSwgbmFtZT0nUmV0YSBSZWZlcsOqbmNpYScsIGxpbmU9ZGljdChjb2xvcj0nI0UyRThGMCcsIGRhc2g9J2Rhc2gnKSkpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bLTIsIC0xLCAwLCAxLCAyXSwgeT1bLTMsIC0wLjUsIDAsIDAuNSwgM10sIG1vZGU9J21hcmtlcnMnLCBuYW1lPSdSZXPDrWR1b3MgKEZvcm1hIFMpJywgbWFya2VyPWRpY3QoY29sb3I9JyNGNTlFMEInLCBzaXplPTgpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5EaWFnbsOzc3RpY28gZGUgUmVzw61kdW9zOiBDdXJ2YXR1cmEgUzwvYj4nKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH1dfQ==').decode('utf-8'))


    import plotly.graph_objects as go
    
    # Inicialização de estado global
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do progresso
    total_mcq = len(dados_exercicios.get("questoes_multipla_escolha", []))
    total_disc = len(dados_exercicios.get("questoes_discursivas", []))
    total_exercicios = total_mcq + total_disc
    
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v is True)
    
    # Barra de progresso e status
    st.markdown("### 📈 Acompanhamento do Aprendizado")
    if total_exercicios > 0:
        progresso = acertos / total_exercicios
        st.progress(progresso)
        st.markdown(f"🏆 **Seu Progresso:** {acertos} de {total_exercicios} desafios concluídos!")
    else:
        st.info("Nenhum exercício disponível no momento.")
    
    # --- Seção Múltipla Escolha ---
    if total_mcq > 0:
        st.subheader("📝 Exercícios de Múltipla Escolha")
        for i, questao in enumerate(dados_exercicios["questoes_multipla_escolha"]):
            st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
            
            # Referência (se existir)
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
                
            # Renderização de gráfico Plotly
            codigo = questao.get("codigo_plotly")
            if codigo:
                local_vars = {"go": go}
                try:
                    exec(codigo, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
                except Exception as e:
                    st.error(f"Erro ao renderizar gráfico: {e}")
            
            # Alternativas
            opcoes = questao.get("alternativas", {})
            selecao = st.radio("Escolha uma opção:", list(opcoes.values()), key=f"radio_mcq_{i}", index=None)
            
            # Dica
            if st.button("💡 Dica", key=f"btn_dica_mcq_{i}"):
                st.info(questao.get("dica", "Dica indisponível."))
                
            # Verificação
            if st.button("✅ Verificar Resposta", key=f"btn_verify_mcq_{i}"):
                correta_label = questao.get("alternativa_correta")
                if selecao == opcoes.get(correta_label):
                    st.success("Correto! Muito bem.")
                    st.session_state.respostas_certas[f"mcq_{i}"] = True
                    st.rerun()
                else:
                    st.error("Resposta incorreta. Tente novamente!")
                    st.session_state.respostas_certas[f"mcq_{i}"] = False
            
            # Gabarito Comentado
            with st.expander("✅ Ver Gabarito Comentado"):
                st.write(questao.get("gabarito_comentado", "Gabarito indisponível."))
            st.divider()
    
    # --- Seção Discursivas ---
    if total_disc > 0:
        st.subheader("✍️ Questões Discursivas")
        for i, questao in enumerate(dados_exercicios["questoes_discursivas"]):
            st.markdown(f"**Desafio {i+1}:** {questao.get('enunciado', '')}")
            
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
                
            # Plotly
            codigo = questao.get("codigo_plotly")
            if codigo:
                local_vars = {"go": go}
                try:
                    exec(codigo, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
                except Exception as e:
                    st.error(f"Erro ao renderizar gráfico: {e}")
            
            # Resposta qualitativa
            st.text_area("Sua reflexão (Prosa):", key=f"text_disc_{i}")
            
            # Validação numérica (opcional)
            valor_esperado = questao.get("resposta_numerica_esperada")
            if valor_esperado is not None:
                user_val = st.number_input("Digite o resultado numérico:", format="%.4f", key=f"num_disc_{i}")
                if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                    if abs(user_val - valor_esperado) <= max(0.01, 0.01 * abs(valor_esperado)):
                        st.success("Resposta Numérica Correta! Excelente trabalho.")
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                        st.rerun()
                    else:
                        st.error("O valor calculado difere do esperado. Revise suas fórmulas.")
                        st.session_state.respostas_certas[f"disc_{i}"] = False
            else:
                # Checkbox para progresso qualitativo
                if st.checkbox("Marque aqui após concluir a escrita", key=f"check_disc_{i}"):
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.session_state.respostas_certas[f"disc_{i}"] = False
            
            # Dica
            if st.button("💡 Dica para este desafio", key=f"btn_dica_disc_{i}"):
                st.info(questao.get("dica", "Dica indisponível."))
                
            # Gabarito detalhado
            with st.expander("✅ Ver Resolução Detalhada"):
                for passo in questao.get("gabarito_passo_a_passo", []):
                    st.write(f"- {passo}")
            st.divider()
