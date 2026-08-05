import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4xOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogQXMgaGlww7N0ZXNlcyBlc3RhdMOtc3RpY2FzIiwgInJlZmVyZW5jaWFzX2JpYmxpb2dyYWZpY2FzX2ZpbmFpcyI6IFsiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhIC0gQ2FwLiAxMiwgcHAuIDMzMS0zMzkiLCAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhIC0gQ2FwLiAxMiwgcHAuIDM0NS0zNDgiLCAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhIC0gQ2FwLiAxMiwgcHAuIDMzMS0zNDQiXX0=').decode('utf-8'))

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
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    # Cabeçalho do subtópico
    st.header(r"A Estrutura Lógica do Teste de Hipóteses: Conceitos Fundamentais")
    
    # Introdução Teórica
    st.markdown(r"""
    O teste de hipóteses é a espinha dorsal da inferência estatística, funcionando como um tribunal científico onde confrontamos afirmações sobre a realidade com evidências extraídas de dados amostrais. Ao considerar um parâmetro populacional desconhecido, frequentemente representado por $\theta$, buscamos verificar a veracidade de uma alegação inicial sobre seu valor.
    
    Este processo é análogo a um julgamento jurídico, onde partimos de uma presunção de veracidade da hipótese nula ($H_0$). Os pilares que sustentam esta lógica são:
    """)
    
    st.markdown(r"""
    - **Presunção Inicial:** Assumimos que $H_0$ é verdadeira até que se prove o contrário.
    - **Distribuição de Referência:** Sob a vigência de $H_0$, os dados devem seguir uma distribuição probabilística conhecida.
    - **Evidência Amostral:** Calculamos um estimador, como a média amostral $\bar{X}$, para confrontar a realidade observada com a esperança teórica.
    - **Regra de Decisão:** Caso a divergência seja estatisticamente rara, rejeitamos $H_0$ em favor da hipótese alternativa ($H_1$).
    """)
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Formalismo do Teste")
    st.latex(r"H_0: \theta = \theta_0 \quad \text{vs} \quad H_1: \theta \neq \theta_0")
    st.latex(r"\alpha = P(\text{rejeitar } H_0 | H_0 \text{ é verdadeira}) = P(\hat{\theta} \in RC | \theta = \theta_0)")
    
    st.info(r"O nível de significância $\alpha$ é o nosso limiar de tolerância ao erro. Ele define o tamanho da Região Crítica (RC), onde resultados são tão improváveis que a hipótese nula torna-se insustentável.")
    
    # Seção do Simulador
    st.markdown(r"### 📊 Simulador de Região Crítica")
    
    col1, col2 = st.columns(2)
    with col1:
        alfa_slider = st.slider(r"Nível de Significância ($\alpha$)", 0.01, 0.10, 0.05, step=0.01, key=r"alfa_subtopico_1")
    with col2:
        n_slider = st.slider(r"Tamanho da Amostra ($n$)", 10, 100, 25, step=5, key=r"n_subtopico_1")
    
    # Cálculo do simulador estático mas reativo aos inputs
    mu_0 = 155
    sigma = 20
    ep = sigma / np.sqrt(n_slider)
    z_crit = norm.ppf(alfa_slider / 2)
    limite_inf = mu_0 + (z_crit * ep)
    limite_sup = mu_0 - (z_crit * ep)
    
    x = np.linspace(140, 170, 500)
    y = norm.pdf(x, mu_0, ep)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Distribuição Normal sob H0', line=dict(color='#1E3A8A')))
    fig.add_vrect(x0=140, x1=limite_inf, fillcolor="#991B1B", opacity=0.3, line_width=0)
    fig.add_vrect(x0=limite_sup, x1=170, fillcolor="#991B1B", opacity=0.3, line_width=0)
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Região Crítica e Distribuição da Média Amostral</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valores de \bar{X}", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    st.markdown(f"**Análise Dinâmica:** Com $\\alpha = {alfa_slider:.2f}$ e $n = {n_slider}$, o erro padrão é de {ep:.4f}. A região crítica é definida por valores abaixo de {limite_inf:.2f} ou acima de {limite_sup:.2f}.")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática: Controle de Qualidade")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Inspeção de Parafusos")
        st.markdown(r"Uma indústria produz parafusos com média $\mu = 155$ kg e $\sigma = 20$ kg. Com $n = 25$, testamos se o novo lote é mais frágil ($\mu < 155$) ao nível $\alpha = 5\%$.")
        st.latex(r"\mu_0 = 155, \quad \sigma = 20, \quad n = 25, \quad EP = 4")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- $H_0: \mu = 155, \quad H_1: \mu < 155$")
        st.markdown(r"- $Z_{crit} = \Phi^{-1}(0,05) \approx -1,645$")
        st.markdown(r"- $\bar{x}_c = 155 + (-1,645 \cdot 4) = 148,42$")
        st.success(r"Laudo: A região crítica para rejeição de $H_0$ são médias amostrais inferiores a 148,42 kg. Se a amostra for menor, o lote deve ser descartado.")
    
    # Deduções Analíticas
    st.markdown(r"### 🔍 Refinamento Analítico")
    st.latex(r"H_0: \theta = \theta_0 \quad \text{vs} \quad H_1: \theta \neq \theta_0")
    st.latex(r"\alpha = P(\hat{\theta} \in RC | \theta = \theta_0)")
    st.latex(r"RC = \{ \bar{X} : \bar{X} < \bar{x}_{c1} \quad \text{ou} \quad \bar{X} > \bar{x}_{c2} \}")
    st.latex(r"P(\text{Erro II}) = \beta = P(\bar{X} \in RA | H_1)")

    # Arquitetura do Erro: Erros Tipo I e Tipo II - Layout Acadêmico Luxo
    import numpy as np
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    st.header(r"Arquitetura do Erro: Erros Tipo I e Tipo II")
    
    st.markdown(r"""
    A estatística inferencial não é uma disciplina de certezas absolutas, mas uma ciência da gestão do risco sob incerteza. Ao realizarmos inferências sobre parâmetros populacionais a partir de amostras finitas de tamanho $n$, operamos dentro de uma arquitetura de erros inerentes.
    """)
    
    st.info(r"A decisão estatística baseia-se na dicotomia entre a hipótese nula $H_0$ (status quo) e a hipótese alternativa $H_1$ (desvio a ser detectado). O risco de incorrer em decisões equivocadas é quantificado pelas probabilidades $\alpha$ e $\beta$.")
    
    st.markdown(r"### 📐 O Coração Matemático: Definição dos Erros")
    
    st.latex(r"\alpha = P(\text{rejeitar } H_0 | H_0 \text{ é verdadeira})")
    st.markdown(r"O **Erro Tipo I ($\alpha$)** representa o falso alarme. É a probabilidade de rejeitar um processo que, na realidade, está operando corretamente.")
    
    st.latex(r"\beta = P(\text{não rejeitar } H_0 | H_1 \text{ é verdadeira})")
    st.markdown(r"O **Erro Tipo II ($\beta$)** representa a falha de detecção. É a probabilidade de um processo defeituoso continuar operando sem intervenção.")
    
    st.latex(r"\pi(\theta) = 1 - \beta = P(\text{rejeitar } H_0 | H_1 \text{ é verdadeira})")
    st.markdown(r"O **Poder do Teste ($\pi$)** é a medida de sensibilidade. Um teste robusto maximiza a probabilidade de detectar um efeito quando ele realmente existe.")
    
    st.markdown(r"---")
    st.subheader(r"🎛️ Simulador: Conflito entre Erros I e II")
    st.markdown(r"Observe como o ajuste do critério de decisão (ponto crítico) altera simultaneamente o risco de falsos positivos e a sensibilidade do teste.")
    
    col1, col2 = st.columns(2)
    with col1:
        alfa_slider = st.slider(r"Nível de Significância ($\alpha$)", 0.01, 0.20, 0.05, step=0.01, key=r"alfa_simulador_subtopico_2")
    with col2:
        n_slider = st.slider(r"Tamanho da Amostra ($n$)", 30, 200, 64, step=1, key=r"n_simulador_subtopico_2")
    
    # Lógica do Simulador
    mu0 = 500
    mu1 = 490
    sigma = 40
    se = sigma / np.sqrt(n_slider)
    z_crit = norm.ppf(1 - alfa_slider)
    crit_val = mu0 - (z_crit * se)
    
    x = np.linspace(470, 520, 500)
    y0 = norm.pdf(x, mu0, se)
    y1 = norm.pdf(x, mu1, se)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y0, name=r"H0 (Status Quo)", line=dict(color="#1E3A8A", width=2)))
    fig.add_trace(go.Scatter(x=x, y=y1, name=r"H1 (Efeito Real)", line=dict(color="#10B981", width=2)))
    fig.add_vline(x=crit_val, line_dash="dash", line_color="#991B1B", annotation_text=r"Ponto Crítico")
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição de Erros I e II</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Parâmetro", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    beta_calc = norm.cdf(crit_val, mu1, se)
    st.info(r"Com $\alpha = " + str(alfa_slider) + r"$ e $n = " + str(n_slider) + r"$, o valor crítico é " + str(round(crit_val, 2)) + r". A probabilidade de erro Tipo II ($\beta$) é de aproximadamente " + str(round(beta_calc * 100, 2)) + r"%.")
    
    st.markdown(r"### 📈 Casos de Aplicação Prática: Controle de Qualidade Industrial")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Degradação de Processo")
        st.markdown(r"Fabricante de componentes com $\mu = 500$ e $\sigma = 40$. Amostra $n = 64$. O controle de qualidade testa se $\mu$ caiu para 490 com $\alpha = 5\%$.")
        st.latex(r"\mu_0 = 500, \quad \mu_1 = 490, \quad \sigma = 40, \quad n = 64, \quad \alpha = 0.05, \quad EP = 5")
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- O valor crítico Z para 5% é -1.645.")
        st.markdown(r"- Calculamos o limite amostral: $500 - (1.645 \cdot 5) = 491.775$.")
        st.markdown(r"- Calculamos $\beta$ como a probabilidade de a média amostral ser maior que 491.775 dado que a média real é 490.")
        st.success(r"Conclusão: Sob o cenário onde a média real é 490, a probabilidade de falha em detectar a degradação (Erro Tipo II) é de 36.13%, resultando em um poder de teste de 63.87%.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    # Cabeçalho do Subtópico
    st.header(r"Construção da Regra de Decisão e Regiões Críticas")
    
    # Prosa Inicial e Contextualização
    st.markdown(r"""
    A transição da estimação estatística para a teoria da decisão marca o momento em que a inferência assume um caráter pragmático. Não buscamos apenas a melhor estimativa para um parâmetro $\theta$, mas uma diretriz binária sobre a veracidade de uma hipótese.
    """)
    
    st.warning(r"A regra de decisão divide o espaço amostral em dois subconjuntos disjuntos e exaustivos: a Região de Aceitação ($RA$) e a Região Crítica ($RC$).")
    
    st.markdown(r"""
    Esta fronteira protege o pesquisador contra a interpretação subjetiva de flutuações aleatórias, funcionando como um mecanismo de controle rigoroso contra o erro de tipo I.
    *   **Região de Aceitação ($RA$):** Onde as variações observadas são atribuídas ao acaso.
    *   **Região Crítica ($RC$):** Onde a evidência estatística é considerada robusta o suficiente para a refutação da hipótese nula $H_0$.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Rigor Matemático: Estrutura da Regra de Decisão")
    st.markdown(r"A construção do limiar crítico é fundamentada na distribuição amostral do estimador $\hat{\theta}$ sob a condição de validade de $H_0$.")
    
    st.latex(r"P(\hat{\theta} \in RC | H_0) = \alpha")
    
    st.markdown(r"Dependendo da natureza da hipótese alternativa $H_1$, definimos a região crítica da seguinte forma:")
    
    st.latex(r"RC = \begin{cases} \{ \hat{\theta} < \hat{\theta}_c \} & H_1: \theta < \theta_0 \\ \{ \hat{\theta} > \hat{\theta}_c \} & H_1: \theta > \theta_0 \\ \{ \hat{\theta} < \hat{\theta}_{c1} \cup \hat{\theta} > \hat{\theta}_{c2} \} & H_1: \theta \neq \theta_0 \end{cases}")
    
    # Demonstração Analítica
    st.markdown(r"A dedução do valor crítico segue uma lógica de inversão da função de distribuição acumulada:")
    st.latex(r"P(\hat{\theta} \in RC | H_0) = \alpha")
    st.latex(r"\int_{RC} f(\hat{\theta} | \theta_0) d\hat{\theta} = \alpha")
    st.latex(r"\hat{\theta}_c = F^{-1}(\alpha)")
    
    # Exemplo Prático
    st.subheader(r"📈 Caso de Aplicação: Controle de Qualidade de Processadores")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Teste de Proporção de Falhas")
        st.markdown(r"Uma fabricante afirma que sua taxa de falha é $p = 0,05$. Com uma amostra de $n = 400$, testamos $H_0: p = 0,05$ contra $H_1: p > 0,05$ ao nível $\alpha = 0,05$.")
        
        st.latex(r"EP(\hat{p}) = \sqrt{\frac{0,05 \cdot 0,95}{400}} \approx 0,0109")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Identificação do valor crítico Z para $\alpha=0,05$: $Z_{crit} = 1,645$.")
        st.markdown(r"- Cálculo do limiar: $\hat{p}_c = 0,05 + (1,645 \cdot 0,0109) = 0,0679$.")
        
        st.success(r"Conclusão: Rejeita-se a hipótese nula se a proporção amostral exceder 6,79%. Este valor atua como o limiar objetivo para identificar falhas sistemáticas.")
    
    # Simulador Interativo
    st.subheader(r"🎛️ Simulador: Geometria das Regiões Críticas")
    
    col1, col2 = st.columns(2)
    with col1:
        alfa_input = st.slider(r"Nível de Significância ($\alpha$)", 0.01, 0.10, 0.05, step=0.01, key=r"alfa_subtopico_3")
    with col2:
        tipo_teste = st.selectbox(r"Tipo de Teste", [r"Unilateral Direita", r"Unilateral Esquerda", r"Bilateral"], key=r"tipo_teste_subtopico_3")
    
    # Lógica do gráfico
    x = np.linspace(-4, 4, 1000)
    y = norm.pdf(x, 0, 1)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=r"Distribuição Nula", line=dict(color="#1E3A8A")))
    
    if tipo_teste == r"Unilateral Direita":
        z_crit = norm.ppf(1 - alfa_input)
        fill_x = x[x > z_crit]
        fig.add_vline(x=z_crit, line_dash="dash", line_color="#991B1B")
    elif tipo_teste == r"Unilateral Esquerda":
        z_crit = norm.ppf(alfa_input)
        fill_x = x[x < z_crit]
        fig.add_vline(x=z_crit, line_dash="dash", line_color="#991B1B")
    else:
        z_c1 = norm.ppf(alfa_input / 2)
        z_c2 = norm.ppf(1 - alfa_input / 2)
        fill_x = x[(x < z_c1) | (x > z_c2)]
        fig.add_vline(x=z_c1, line_dash="dash", line_color="#991B1B")
        fig.add_vline(x=z_c2, line_dash="dash", line_color="#991B1B")
    
    fig.add_trace(go.Scatter(x=fill_x, y=norm.pdf(fill_x, 0, 1), fill='tozeroy', fillcolor='rgba(153, 27, 27, 0.3)', mode='none', name=r"Região Crítica ($RC$)"))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Geometria da Região Crítica</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Escore Z", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    # Laudo dinâmico
    st.info(r"Ao ajustar o nível de significância para " + str(alfa_input) + r", observamos que a área da Região Crítica se expande ou contrai, refletindo diretamente a sensibilidade do nosso critério de decisão em relação ao risco de erro tipo I.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4xOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogQXMgaGlww7N0ZXNlcyBlc3RhdMOtc3RpY2FzIiwgInF1ZXN0b2VzX211bHRpcGxhX2VzY29saGEiOiBbeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIGFmaXJtYSBxdWUgYSB2aWRhIMO6dGlsIG3DqWRpYSBkZSB1bSBtaWNyb3Byb2Nlc3NhZG9yIMOpIGRlICRcXG11ID0gNTAwMCQgaG9yYXMuIFVtIGVuZ2VuaGVpcm8gZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlLCBkZXNjb25maWFkbyBkYSBhbGVnYcOnw6NvLCBjb2xldGEgdW1hIGFtb3N0cmEgYWxlYXTDs3JpYSBkZSAkbiA9IDEwMCQgcHJvY2Vzc2Fkb3JlcyBlIGRlc2VqYSByZWFsaXphciB1bSB0ZXN0ZSBkZSBoaXDDs3Rlc2VzLiBFbGUgZGVmaW5lICRIXzA6IFxcbXUgPSA1MDAwJCBjb250cmEgJEhfMTogXFxtdSBcXG5lcSA1MDAwJCBjb20gdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGRlICRcXGFscGhhID0gMC4wNSQuIFNlIG8gZW5nZW5oZWlybyBlc3RhYmVsZWNlIHF1ZSBhIHJlZ2nDo28gY3LDrXRpY2Egw6kgJFJDID0gXFx7IFxcYmFye1h9IDogfFxcYmFye1h9IC0gNTAwMHwgPiAxNTAgXFx9JCwgbyBxdWUgc2lnbmlmaWNhIG8gZXJybyBkbyBUaXBvIEkgbmVzdGUgY29udGV4dG8gcHLDoXRpY28/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgYSBoaXDDs3Rlc2UgZGUgcXVlIGEgdmlkYSBtw6lkaWEgw6kgNTAwMCBob3JhcywgcXVhbmRvIG5hIHJlYWxpZGFkZSBhIHZpZGEgbcOpZGlhIMOpIGV4YXRhbWVudGUgNTAwMCBob3Jhcy4iLCAiQiI6ICJBIHByb2JhYmlsaWRhZGUgZGUgYWNlaXRhciBxdWUgYSB2aWRhIG3DqWRpYSDDqSA1MDAwIGhvcmFzLCBxdWFuZG8gbmEgdmVyZGFkZSBhIG3DqWRpYSDDqSBpbmZlcmlvciBhIDUwMDAgaG9yYXMuIiwgIkMiOiAiQSBwcm9iYWJpbGlkYWRlIGRlIHF1ZSBhIG3DqWRpYSBhbW9zdHJhbCBvYnNlcnZhZGEgZXN0ZWphIGZvcmEgZG8gaW50ZXJ2YWxvIGRlIDE1MCBob3JhcyBlbSByZWxhw6fDo28gw6AgbcOpZGlhIHBvcHVsYWNpb25hbC4iLCAiRCI6ICJPIHBvZGVyIGRvIHRlc3RlLCBvdSBzZWphLCBhIGNhcGFjaWRhZGUgZG8gZW5nZW5oZWlybyBkZSBkZXRlY3RhciBxdWUgYSBtw6lkaWEgw6kgZGlmZXJlbnRlIGRlIDUwMDAgaG9yYXMgcXVhbmRvIGVsYSByZWFsbWVudGUgw6kuIiwgIkUiOiAiQSBjaGFuY2UgZGUgbyBlbmdlbmhlaXJvIGVycmFyIGFvIGNvbmNsdWlyIHF1ZSBvIHByb2Nlc3NvIGVzdMOhIHNvYiBjb250cm9sZSwgcXVhbmRvIG8gZGVzZ2FzdGUgZG9zIGNvbXBvbmVudGVzIMOpIG1haW9yIGRvIHF1ZSBvIGVzcGVjaWZpY2Fkby4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBkZWZpbmnDp8OjbyBmdW5kYW1lbnRhbCBkZSAkXFxhbHBoYSQ6IGEgcHJvYmFiaWxpZGFkZSBkZSB0b21hciB1bWEgZGVjaXPDo28gZGUgcmVqZWnDp8OjbyBpbmNvcnJldGEsIGJhc2VhZGEgbm8gcHJlc3N1cG9zdG8gZGUgcXVlICRIXzAkIMOpIHZlcmRhZGVpcmEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJPIGVycm8gZG8gVGlwbyBJLCBkZW5vdGFkbyBwb3IgJFxcYWxwaGEkLCBvY29ycmUgcXVhbmRvIHJlamVpdGFtb3MgJEhfMCQgc2VuZG8gZXN0YSB2ZXJkYWRlaXJhLiBObyBlbnVuY2lhZG8sICRIXzA6IFxcbXUgPSA1MDAwJCAoYSBhZmlybWHDp8OjbyBkbyBmYWJyaWNhbnRlKS4gUG9ydGFudG8sIG8gZXJybyBUaXBvIEkgcmVwcmVzZW50YSBhIHByb2JhYmlsaWRhZGUgZGUgY29uY2x1aXIgcXVlIGEgdmlkYSDDunRpbCBtw6lkaWEgw6kgZGlmZXJlbnRlIGRlIDUwMDAgaG9yYXMsIHF1YW5kbyBvIGZhYnJpY2FudGUgZXN0w6EgZGl6ZW5kbyBhIHZlcmRhZGUgZSBhIG3DqWRpYSDDqSBleGF0YW1lbnRlIDUwMDAgaG9yYXMuIEVtIHRlcm1vcyB0w6ljbmljb3MsICRcXGFscGhhID0gUChcXGJhcntYfSBcXGluIFJDIHwgXFxtdSA9IDUwMDApJC4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDQ1MDAsIDU1MDAsIDEwMDApXG55ID0gc3RhdHMubm9ybS5wZGYoeCwgNTAwMCwgNzUpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9J0Rpc3RyaWJ1acOnw6NvIHNvYiBIMCcsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTIpKSlcbmZpZy5hZGRfdnJlY3QoeDA9NTE1MCwgeDE9NTUwMCwgZmlsbGNvbG9yPScjOTkxQjFCJywgb3BhY2l0eT0wLjMsIGxpbmVfd2lkdGg9MCwgbmFtZT0nUkMnKVxuZmlnLmFkZF92cmVjdCh4MD00NTAwLCB4MT00ODUwLCBmaWxsY29sb3I9JyM5OTFCMUInLCBvcGFjaXR5PTAuMywgbGluZV93aWR0aD0wLCBuYW1lPSdSQycpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+UmVnacOjbyBDcsOtdGljYSAoUkMpIGUgRGlzdHJpYnVpw6fDo28gc29iIEgwPC9iPicsIHhheGlzX3RpdGxlPXInTcOpZGlhIEFtb3N0cmFsICgkXFxiYXJ7WH0kKScsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtIGVuc2FpbyBjbMOtbmljbyBhdmFsaWEgdW0gbm92byBmw6FybWFjbyBwYXJhIHJlZHV6aXIgYSBwcmVzc8OjbyBhcnRlcmlhbC4gU2FiZS1zZSBxdWUgbyBlZmVpdG8gbnVsbyDDqSAkXFxtdSA9IDAkIChuZW5odW1hIHJlZHXDp8OjbykuIE8gcGVzcXVpc2Fkb3IgdGVzdGEgJEhfMDogXFxtdSA9IDAkIHZlcnN1cyAkSF8xOiBcXG11ID4gMCQuIENvbnNpZGVyZSBxdWUgbyBwb2RlciBkbyB0ZXN0ZSBwYXJhIHVtIGRlc3ZpbyBkZSAkXFxtdSA9IDUkIG1tSGcgw6kgZGUgJDAuODUkLiBDb21vIGVzdGUgcG9kZXIgZGUgJDAuODUkIGRldmUgc2VyIGludGVycHJldGFkbyBjb3JyZXRhbWVudGUgbm8gZGVzZW5obyBkbyBleHBlcmltZW50bz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIsOJIGEgcHJvYmFiaWxpZGFkZSBkZSBvIGbDoXJtYWNvIG7Do28gZnVuY2lvbmFyLCBkYWRvIHF1ZSBvIHRlc3RlIGZvaSBzaWduaWZpY2F0aXZvLiIsICJCIjogIsOJIGEgcHJvYmFiaWxpZGFkZSBkZSBvIHBlc3F1aXNhZG9yIHJlamVpdGFyIGNvcnJldGFtZW50ZSAkSF8wJCBxdWFuZG8sIG5hIHZlcmRhZGUsIGEgcmVkdcOnw6NvIHJlYWwgZGEgcHJlc3PDo28gYXJ0ZXJpYWwgw6kgZGUgNSBtbUhnLiIsICJDIjogIsOJIGEgcHJvYmFiaWxpZGFkZSBkZSBvIHBlc3F1aXNhZG9yIGNvbWV0ZXIgdW0gZXJybyBkbyBUaXBvIEkgZGUgMTUlLiIsICJEIjogIsOJIGEgcHJvYmFiaWxpZGFkZSBkZSBhY2VpdGFyICRIXzAkIHF1YW5kbyBhIHJlZHXDp8OjbyByZWFsIMOpIGRlIDUgbW1IZy4iLCAiRSI6ICLDiSBhIGNvbmZpYW7Dp2EgZXN0YXTDrXN0aWNhIHF1ZSBvIHBlc3F1aXNhZG9yIHRlbSBkZSBxdWUgYSBtw6lkaWEgcG9wdWxhY2lvbmFsIMOpIGV4YXRhbWVudGUgNS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk8gcG9kZXIgZG8gdGVzdGUgKCQxLVxcYmV0YSQpIMOpIGEgbWVkaWRhIGRlICdzZW5zaWJpbGlkYWRlJyBkbyB0ZXN0ZSBwYXJhIGRldGVjdGFyIHVtIGVmZWl0byByZWFsIGVzcGVjw61maWNvLiBSZWxlaWEgYSBkZWZpbmnDp8OjbyBmb3JtYWwgZGFkYSBubyBlbnVuY2lhZG8gZG8gcHJvYmxlbWEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJPIHBvZGVyIGRvIHRlc3RlIMOpIGRlZmluaWRvIGNvbW8gJDEgLSBcXGJldGEgPSBQKFxcdGV4dHtyZWplaXRhciB9IEhfMCB8IEhfMSBcXHRleHR7IMOpIHZlcmRhZGVpcmF9KSQuIFF1YW5kbyBmaXhhbW9zIHVtYSBhbHRlcm5hdGl2YSBlc3BlY8OtZmljYSAobmVzdGUgY2FzbywgcXVlIGEgbcOpZGlhIHJlYWwgw6kgJFxcbXUgPSA1JCksIG8gcG9kZXIgbm9zIGRpeiBhIHByb2JhYmlsaWRhZGUgZGUgcXVlIG8gdGVzdGUgZXN0YXTDrXN0aWNvIGRldGVjdGUgZXNzZSBlZmVpdG8sIG91IHNlamEsIGNhaWEgbmEgcmVnacOjbyBkZSByZWplacOnw6NvICRSQyQuIEFzc2ltLCAwLjg1IGluZGljYSBxdWUsIHNlIG8gZWZlaXRvIGZvciBkZSA1IG1tSGcsIHRlbW9zIDg1JSBkZSBjaGFuY2UgZGUgbyB0ZXN0ZSBpZGVudGlmaWNhciBxdWUgYSBoaXDDs3Rlc2UgbnVsYSDDqSBmYWxzYS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtYSBsaW5oYSBkZSBtb250YWdlbSBkZSBzZW5zb3JlcyBJb1QgZGUgYWx0YSBwcmVjaXPDo28sIG8gcHJvY2Vzc28gw6kgY29uc2lkZXJhZG8gZXN0w6F2ZWwgcXVhbmRvIGEgdmFyaWFiaWxpZGFkZSBkYSBtZWRpw6fDo28gZGUgdGVtcGVyYXR1cmEgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBjb20gbcOpZGlhICRcXG11ID0gMjVee1xcY2lyY31DJCBlIHZhcmnDom5jaWEgJFxcc2lnbWFeMiA9IDQkLiBVbWEgZXF1aXBlIGRlIGVuZ2VuaGFyaWEgZGVzZWphIHRlc3RhciBhIGhpcMOzdGVzZSAkSF8wOiBcXG11ID0gMjUkIGNvbnRyYSAkSF8xOiBcXG11IFxcbmVxIDI1JC4gQ2FzbyBvIHZhbG9yIG9ic2VydmFkbyBkYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBkZSAkbj0xNiQgc2Vuc29yZXMgY2FpYSBmb3JhIGRhIHJlZ2nDo28gY3LDrXRpY2EgJFJDID0gXFx7XFxiYXJ7WH0gXFxpbiBcXG1hdGhiYntSfSB8IFxcYmFye1h9IDwgMjR+IFx0ZXh0e291fX4gXGJhcntYfSA+IDI2XFx9JCwgYSBoaXDDs3Rlc2UgbnVsYSBuw6NvIMOpIHJlamVpdGFkYS4gQ29uc2lkZXJhbmRvIGVzdGUgY2Vuw6FyaW8sIHF1YWwgw6kgYSBkZWZpbmnDp8OjbyBjb3JyZXRhIGRvIEVycm8gVGlwbyBJICgkXFxhbHBoYSQpIG5lc3RlIGNvbnRleHRvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBwcm9iYWJpbGlkYWRlIGRlIGNvbmNsdWlyIHF1ZSBhIG3DqWRpYSBkZSB0ZW1wZXJhdHVyYSBkb3Mgc2Vuc29yZXMgw6kgZGlmZXJlbnRlIGRlIDI1wrBDLCBxdWFuZG8sIG5hIHZlcmRhZGUsIGVsYSDDqSBleGF0YW1lbnRlIDI1wrBDLiIsICJCIjogIkEgcHJvYmFiaWxpZGFkZSBkZSBuw6NvIGRldGVjdGFyIHVtYSBmYWxoYSBuYSBjYWxpYnJhw6fDo28sIHF1YW5kbyBhIG3DqWRpYSByZWFsIGRvcyBzZW5zb3JlcyDDqSwgZGUgZmF0bywgZGlmZXJlbnRlIGRlIDI1wrBDLiIsICJDIjogIkEgcHJvYmFiaWxpZGFkZSBkZSBhIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0kIGVzdGFyIGNvbnRpZGEgbm8gaW50ZXJ2YWxvICRbMjQsIDI2XSQsIGRhZG8gcXVlIGEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQgw6kgMjXCsEMuIiwgIkQiOiAiQSBtZWRpZGEgZG8gcG9kZXIgZG8gdGVzdGUsIHJlcHJlc2VudGFkYSBwb3IgJFxccGkoXFxtdSkgPSAxIC0gXFxiZXRhJCwgcGFyYSBxdWFscXVlciB2YWxvciBkZSAkXFxtdSQgZGlmZXJlbnRlIGRlIDI1wrBDLiIsICJFIjogIkEgcHJvYmFiaWxpZGFkZSBkZSByZWplaXRhciBhIGhpcMOzdGVzZSBhbHRlcm5hdGl2YSBxdWFuZG8gYSBoaXDDs3Rlc2UgbnVsYSDDqSBmYWxzYS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBkZWZpbmnDp8OjbyBmdW5kYW1lbnRhbDogbyBFcnJvIFRpcG8gSSBvY29ycmUgcXVhbmRvIHRvbWFtb3MgdW1hIGRlY2lzw6NvIGRlIHJlamVpw6fDo28gYmFzZWFkYSBlbSBldmlkw6puY2lhIGFtb3N0cmFsIHF1ZSBub3MgaW5kdXogYSBhYmFuZG9uYXIgdW1hIGhpcMOzdGVzZSBudWxhIHF1ZSDDqSwgbmEgcmVhbGlkYWRlLCBhIGRlc2NyacOnw6NvIGNvcnJldGEgZGEgcG9wdWxhw6fDo28uIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJPIEVycm8gVGlwbyBJICgkXFxhbHBoYSQpIMOpIGRlZmluaWRvIGNvbW8gYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIHF1YW5kbyAkSF8wJCDDqSB2ZXJkYWRlaXJhLiBObyBlbnVuY2lhZG8sIHRlbW9zICRIXzA6IFxcbXUgPSAyNSQuIFJlamVpdGFtb3MgJEhfMCQgcXVhbmRvICRcXGJhcntYfSA8IDI0JCBvdSAkXFxiYXJ7WH0gPiAyNiQuIFBvcnRhbnRvLCAkXFxhbHBoYSA9IFAoXFxiYXJ7WH0gPCAyNCB8IFxcbXUgPSAyNSkgKyBQKFxcYmFye1h9ID4gMjYgfCBcXG11ID0gMjUpJC4gQSBhbHRlcm5hdGl2YSBBIGRlc2NyZXZlIGV4YXRhbWVudGUgbyBjb25jZWl0byBlc3RhdMOtc3RpY28gZGUgZmFsc28gcG9zaXRpdm8gZW0gdW0gdGVzdGUgZGUgaGlww7N0ZXNlcy4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDIyLCAyOCwgNTAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgsIDI1LCAyL25wLlxcc3FydCgxNikpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9XCJEaXN0cmlidWnDp8OjbyBzb2IgJEhfMCRcIiwgbGluZT1kaWN0KGNvbG9yPVwiIzFFM0E4QVwiLCB3aWR0aD0zKSkpXG5maWcuYWRkX3ZyZWN0KHgwPTIyLCB4MT0yNCwgZmlsbGNvbG9yPVwiIzk5MUIxQlwiLCBvcGFjaXR5PTAuMywgbGluZV93aWR0aD0wLCBuYW1lPVwiUkNcIilcbmZpZy5hZGRfdnJlY3QoeDA9MjYsIHgxPTI4LCBmaWxsY29sb3I9XCIjOTkxQjFCXCIsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTAsIG5hbWU9XCJSQ1wiKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9XCI8Yj5SZWdpw6NvIGRlIFJlamVpw6fDo28gZSBFcnJvIFRpcG8gSTwvYj5cIiwgeGF4aXNfdGl0bGU9clwiJFxcYmFye1h9JFwiLCB5YXhpc190aXRsZT1cIkRlbnNpZGFkZVwiKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVuc2FpbyBjbMOtbmljbyBwYXJhIHRlc3RhciBhIGVmaWPDoWNpYSBkZSB1bSBub3ZvIGbDoXJtYWNvLCBhIGhpcMOzdGVzZSBudWxhICRIXzAkIGVzdGFiZWxlY2UgcXVlIG8gZsOhcm1hY28gbsOjbyBhcHJlc2VudGEgZWZlaXRvIHN1cGVyaW9yIGFvIHBsYWNlYm8uIE8gcGVzcXVpc2Fkb3IgZGVjaWRlIGZpeGFyIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhID0gMCwwNSQuIEFvIGFuYWxpc2FyIG9zIHJlc3VsdGFkb3MsIG8gcGVzcXVpc2Fkb3Igb2JzZXJ2YSBxdWUgbyB0ZXN0ZSBmYWxob3UgZW0gcmVqZWl0YXIgJEhfMCQsIGVtYm9yYSwgbmEgcmVhbGlkYWRlLCBvIGbDoXJtYWNvIHBvc3N1YSB1bSBlZmVpdG8gdGVyYXDDqnV0aWNvIHJlbGV2YW50ZS4gUXVhbCBlcnJvIGVzdGF0w61zdGljbyBmb2kgY29tZXRpZG8gZSBjb21vIGVsZSBzZSByZWxhY2lvbmEgY29tIG8gcG9kZXIgZG8gdGVzdGU/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJFcnJvIFRpcG8gSTsgYSBwcm9iYWJpbGlkYWRlIGRlIG9jb3Jyw6puY2lhIGRlc3RlIGVycm8gw6kgYXVtZW50YWRhIHBlbG8gYXVtZW50byBkbyBwb2RlciBkbyB0ZXN0ZSAoJDEgLSBcXGJldGEkKS4iLCAiQiI6ICJFcnJvIFRpcG8gSUk7IGVzdGUgZXJybyBvY29ycmUgY29tIHByb2JhYmlsaWRhZGUgJFxcYmV0YSQgZSBlc3TDoSBpbnZlcnNhbWVudGUgcmVsYWNpb25hZG8gYW8gcG9kZXIgZG8gdGVzdGUuIiwgIkMiOiAiRXJybyBUaXBvIEk7IGVzdGUgZXJybyDDqSBpbXBvc3PDrXZlbCBkZSBvY29ycmVyIGRhZG8gcXVlIG8gcGVzcXVpc2Fkb3IgZml4b3UgJFxcYWxwaGEgPSAwLDA1JC4iLCAiRCI6ICJFcnJvIFRpcG8gSUk7IGVzdGUgZXJybyBwb2RlIHNlciByZWR1emlkbyBhdW1lbnRhbmRvIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCBkZSBmb3JtYSBhcmJpdHLDoXJpYS4iLCAiRSI6ICJFcnJvIGRlIGVzdGltYXRpdmE7IG9jb3JyZSBxdWFuZG8gYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBzZSBkZXN2aWEgZGEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQgZGV2aWRvIGFvIGVycm8gYW1vc3RyYWwgYWxlYXTDs3Jpby4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk8gRXJybyBUaXBvIElJIG9jb3JyZSBxdWFuZG8gZmFsaGFtb3MgZW0gcmVqZWl0YXIgdW1hIGhpcMOzdGVzZSBudWxhIGZhbHNhLiBPIHBvZGVyIGRvIHRlc3RlLCAkMSAtIFxcYmV0YSQsIMOpIGp1c3RhbWVudGUgYSBjYXBhY2lkYWRlIGRlIGlkZW50aWZpY2FyIHF1ZSBhIGhpcMOzdGVzZSBudWxhIMOpIGZhbHNhLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBFcnJvIFRpcG8gSUkgKCRcXGJldGEkKSBvY29ycmUgcXVhbmRvIG7Do28gcmVqZWl0YW1vcyAkSF8wJCBkYWRvIHF1ZSAkSF8xJCDDqSB2ZXJkYWRlaXJhLiBPIGVudW5jaWFkbyBkZXNjcmV2ZSBleGF0YW1lbnRlIGVzc2Egc2l0dWHDp8OjbzogbyBmw6FybWFjbyB0ZW0gZWZlaXRvICgkSF8xJCB2ZXJkYWRlaXJhKSwgbWFzIG8gdGVzdGUgbsOjbyByZWplaXRvdSBvIHBsYWNlYm8gKCRIXzAkKS4gQ29tbyAkXFxwaShcdGhldGEpID0gMSAtIFxcYmV0YSQsIGV4aXN0ZSB1bWEgcmVsYcOnw6NvIGludmVyc2EgZXN0cml0YTogcXVhbnRvIG1haW9yIG8gcG9kZXIgZG8gdGVzdGUsIG1lbm9yIGEgcHJvYmFiaWxpZGFkZSBkZSBjb21ldGVyIHVtIGVycm8gZG8gVGlwbyBJSS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtYSBpbmTDunN0cmlhIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyBvcGVyYSBjb20gdW0gcHJvY2Vzc28gZGUgcHJvZHXDp8OjbyBvbmRlIG8gdGVtcG8gZGUgdmlkYSDDunRpbCBtw6lkaW8gw6kgZGUgJFxcbXVfMCA9IDUwMCQgaG9yYXMsIGNvbSBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgY29uaGVjaWRvIGRlICRcXHNpZ21hID0gMjAkIGhvcmFzLiBQYXJhIG1vbml0b3JhciBvIHByb2Nlc3NvLCB1bSBlbmdlbmhlaXJvIGNvbGV0YSB1bWEgYW1vc3RyYSBkZSAkbiA9IDY0JCBjb21wb25lbnRlcy4gRGVzZWphbmRvIHJlYWxpemFyIHVtIHRlc3RlIGJpbGF0ZXJhbCBwYXJhIHZlcmlmaWNhciBzZSBhIG3DqWRpYSByZWFsIGRvIHByb2Nlc3NvICRcXG11JCBhaW5kYSDDqSAkNTAwJCBob3JhcywgYW8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGRlICRcXGFscGhhID0gMCwwNSQsIHF1YWwgZGFzIGFsdGVybmF0aXZhcyBhYmFpeG8gZGVzY3JldmUgY29ycmV0YW1lbnRlIGEgUmVnacOjbyBDcsOtdGljYSAoJFJDJCkgZW0gdGVybW9zIGRhIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0kPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiUkMgPSB7IFxcYmFye1h9IDogXFxiYXJ7WH0gPCA0OTUsMSBcXGN1cCBcXGJhcntYfSA+IDUwNCw5IH0iLCAiQiI6ICJSQyA9IHsgXFxiYXJ7WH0gOiBcXGJhcntYfSA8IDQ5NiwwOCBcXGN1cCBcXGJhcntYfSA+IDUwMyw5MiB9IiwgIkMiOiAiUkMgPSB7IFxcYmFye1h9IDogXFxiYXJ7WH0gPiA1MDQsOSB9IiwgIkQiOiAiUkMgPSB7IFxcYmFye1h9IDogXFxiYXJ7WH0gPCA0OTcsMiB9IiwgIkUiOiAiUkMgPSB7IFxcYmFye1h9IDogXFxiYXJ7WH0gPCA0OTgsNCBcXGN1cCBcXGJhcntYfSA+IDUwMSw2IH0ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUsIGVtIHVtIHRlc3RlIGJpbGF0ZXJhbCwgYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpw6fDo28gJFxcYWxwaGEkIMOpIGRpdmlkaWRhIGlndWFsbWVudGUgZW50cmUgYXMgZHVhcyBjYXVkYXMuIE8gdmFsb3IgY3LDrXRpY28gJFpfe1xcdGV4dHtjcml0fX0kIHBhcmEgJFxcYWxwaGEgPSAwLDA1JCDDqSAkMSw5NiQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIHVtIHRlc3RlIGJpbGF0ZXJhbCBzb2JyZSBhIG3DqWRpYSBjb20gJFxcc2lnbWEkIGNvbmhlY2lkbywgdXRpbGl6YW1vcyBhIGVzdGF0w61zdGljYSAkWiA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXVfMH17XFxzaWdtYSAvIFxcc3FydHtufX0kLiBBIHJlZ2nDo28gY3LDrXRpY2Egw6kgZGVmaW5pZGEgcG9yICR8WnwgPiBaX3tcXHRleHR7Y3JpdH19JC4gUGFyYSAkXFxhbHBoYSA9IDAsMDUkLCAkWl97XFx0ZXh0e2NyaXR9fSA9IDEsOTYkLiBBc3NpbSwgYSBmcm9udGVpcmEgw6kgZGFkYSBwb3IgJFxcYmFye1h9ID0gXFxtdV8wIFxccG0gWl97XFx0ZXh0e2NyaXR9fSBcXGNkb3QgXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0kLiBDYWxjdWxhbmRvOiAkXFxiYXJ7WH1fYyA9IDUwMCBcXHBtIDEsOTYgXFxjZG90IFxcZnJhY3syMH17XFxzcXJ0ezY0fX0gPSA1MDAgXFxwbSAxLDk2IFxcY2RvdCAyLDUgPSA1MDAgXFxwbSA0LDkkLiBQb3J0YW50bywgYSAkUkMgPSB7IFxcYmFye1h9IDogXFxiYXJ7WH0gPCA0OTUsMSBcXGN1cCBcXGJhcntYfSA+IDUwNCw5IH0kLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXFxueCA9IG5wLmxpbnNwYWNlKDQ5MCwgNTEwLCA1MDApXFxueSA9ICgxIC8gKDIuNSAqIG5wLlxcc3FydCgyICogbnAuXFxwaSkpKSAqIG5wLlxcZXhwKC0wLjUgKiAoKHggLSA1MDApIC8gMi41KSoqMilcXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTIpLCBuYW1lPSdEaXN0cmlidWnDp8OjbyAkXFxcXGJhcntYfSQnKSlcXG5maWcuYWRkX3ZyZWN0KHgwPTQ5NS4xLCB4MT00OTAsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTAsIG5hbWU9J1JDIEVzcXVlcmRhJylcXG5maWcuYWRkX3ZyZWN0KHgwPTUwNC45LCB4MT01MTAsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTAsIG5hbWU9J1JDIERpcmVpdGEnKVxcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdSZWdpw7VlcyBDcsOtdGljYXMgcGFyYSBvIFRlc3RlIEJpbGF0ZXJhbCcsIHhheGlzX3RpdGxlPSdNw6lkaWEgQW1vc3RyYWwgKCRcXGJhcntYfSQpJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTEsIHAuIDI4NSJ9LCB7ImVudW5jaWFkbyI6ICJVbSBnZXN0b3IgZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlIGRlc2VqYSB0ZXN0YXIgc2UgYSBwcm9wb3LDp8OjbyBkZSBwZcOnYXMgZGVmZWl0dW9zYXMgZW0gdW1hIGxpbmhhIGRlIHByb2R1w6fDo28gdWx0cmFwYXNzb3UgbyBwYWRyw6NvIGhpc3TDs3JpY28gZGUgJHBfMCA9IDAsMDQkLiBPIHRlc3RlIMOpIGZvcm11bGFkbyBjb21vICRIXzA6IHAgPSAwLDA0JCB2cyAkSF8xOiBwID4gMCwwNCQuIFNlIG8gZ2VzdG9yIGRlY2lkaXIgcmVkdXppciBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgZGUgJDAsMDUkIHBhcmEgJDAsMDEkLCBxdWFsIMOpIGEgY29uc2VxdcOqbmNpYSBkaXJldGEgbmEgY29uc3RydcOnw6NvIGRhIFJlZ2nDo28gQ3LDrXRpY2EgKCRSQyQpPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSAkUkMkIHRvcm5hLXNlIG1haXMgYW1wbGEsIGZhY2lsaXRhbmRvIGEgcmVqZWnDp8OjbyBkZSAkSF8wJC4iLCAiQiI6ICJBICRSQyQgZGVzbG9jYS1zZSBwYXJhIGEgZXNxdWVyZGEsIHRvcm5hbmRvIG8gdGVzdGUgbWFpcyBzZW5zw612ZWwuIiwgIkMiOiAiQSAkUkMkIHRvcm5hLXNlIG1haXMgcmVzdHJpdGEsIGRlc2xvY2FuZG8gbyB2YWxvciBjcsOtdGljbyBwYXJhIHZhbG9yZXMgbWFpb3Jlcy4iLCAiRCI6ICJOw6NvIGjDoSBhbHRlcmHDp8OjbyBuYSAkUkMkLCBhcGVuYXMgbmEgcHJvYmFiaWxpZGFkZSBkbyBFcnJvIFRpcG8gSUkuIiwgIkUiOiAiTyB2YWxvciBjcsOtdGljbyBkaW1pbnVpLCBleGlnaW5kbyBtZW5vcyBldmlkw6puY2lhIHBhcmEgcmVqZWl0YXIgJEhfMCQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJSZWR1emlyICRcXGFscGhhJCBzaWduaWZpY2EgdG9ybmFyIGEgZXhpZ8OqbmNpYSBwYXJhIHJlamVpdGFyICRIXzAkIG1haXMgcmlnb3Jvc2EgKG1lbm9yIHRvbGVyw6JuY2lhIGFvIGVycm8gZG8gVGlwbyBJKS4gUGVuc2UgbmEgcG9zacOnw6NvIGRvIHZhbG9yIGNyw610aWNvIG5hIGNhdWRhIGRhIGRpc3RyaWJ1acOnw6NvLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiRW0gdW0gdGVzdGUgdW5pbGF0ZXJhbCDDoCBkaXJlaXRhLCBhIFJlZ2nDo28gQ3LDrXRpY2Egw6kgZG8gdGlwbyAkUkMgPSB7IFxcaGF0e3B9IDogXFxoYXR7cH0gPiBcXGhhdHtwfV9jIH0kLiBBbyByZWR1emlyICRcXGFscGhhJCBkZSAkMCwwNSQgKHF1ZSBjb3JyZXNwb25kZSBhIHVtIHZhbG9yIGNyw610aWNvICRaIFxcYXBwcm94IDEsNjQ1JCkgcGFyYSAkMCwwMSQgKHF1ZSBjb3JyZXNwb25kZSBhIHVtIHZhbG9yIGNyw610aWNvICRaIFxcYXBwcm94IDIsMzMkKSwgbyBsaW1pdGUgZGEgcmVnacOjbyBkZSByZWplacOnw6NvIHNlIG1vdmUgcGFyYSBhIGRpcmVpdGEgKHZhbG9yZXMgbWFpb3JlcyBkZSAkXFxoYXR7cH0kKS4gQXNzaW0sIGEgcmVnacOjbyBkZSByZWplacOnw6NvIGZpY2EgbWFpcyByZXN0cml0YSwgdG9ybmFuZG8gbWFpcyBkaWbDrWNpbCByZWplaXRhciBhIGhpcMOzdGVzZSBudWxhIHF1YW5kbyBlbGEgw6kgdmVyZGFkZWlyYSwgbyBxdWUgZGltaW51aSBhIHByb2JhYmlsaWRhZGUgZGUgdW0gRXJybyBUaXBvIEkuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9XSwgInF1ZXN0b2VzX2Rpc2N1cnNpdmFzIjogW3siZW51bmNpYWRvIjogIkVtIHVtIHByb2Nlc3NvIGRlIGVudmFzZSBkZSBiZWJpZGFzLCBhIG3DoXF1aW5hIGRldmUgZGVwb3NpdGFyICRcXG11ID0gNjAwJCBtbC4gTyBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgw6kgY29uaGVjaWRvIGNvbW8gJFxcc2lnbWEgPSAxMCQgbWwuIE8gZ2VyZW50ZSBkZWNpZGUgcmVqZWl0YXIgJEhfMDogXFxtdSA9IDYwMCQgc2UgYSBtw6lkaWEgZGUgdW1hIGFtb3N0cmEgZGUgJG4gPSAyNSQgZ2FycmFmYXMgZm9yICRcXGJhcntYfSA+IDYwNCQgbWwuIENhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRvIEVycm8gVGlwbyBJICgkXFxhbHBoYSQpIHBhcmEgZXN0ZSB0ZXN0ZS4iLCAiZGljYSI6ICJVdGlsaXplIGEgZGlzdHJpYnVpw6fDo28gZGEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSBcXHNpbSBOKFxcbXUsIFxcZnJhY3tcXHNpZ21hXjJ9e259KSQuIENhbGN1bGUgbyB2YWxvciAkWl97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXV9e1xcc2lnbWEgLyBcXHNxcnR7bn19JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYXIgYSBkaXN0cmlidWnDp8OjbyBzb2IgJEhfMCQ6ICRcXGJhcntYfSBcXHNpbSBOKDYwMCwgXFxmcmFjezEwXjJ9ezI1fSkgPSBOKDYwMCwgNCkkLiIsICIyLiBPIGRlc3ZpbyBwYWRyw6NvIGRhIG3DqWRpYSAoRXJybyBQYWRyw6NvKSDDqSAkRVAoXFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0gPSBcXGZyYWN7MTB9e1xcc3FydHsyNX19ID0gXFxmcmFjezEwfXs1fSA9IDIkLiIsICIzLiBEZWZpbmlyIG8gJFxcYWxwaGEkIGNvbW8gJFAoXFxiYXJ7WH0gPiA2MDQgfCBcXG11ID0gNjAwKSQuIiwgIjQuIFBhZHJvbml6YXIgYSB2YXJpw6F2ZWwgcGFyYSBvYnRlciAkWl97XFx0ZXh0e2NhbGN9fSQ6ICRaID0gXFxmcmFjezYwNCAtIDYwMH17Mn0gPSBcXGZyYWN7NH17Mn0gPSAyJC4iLCAiNS4gQSBwcm9iYWJpbGlkYWRlIGNvcnJlc3BvbmRlbnRlIGEgJFogPiAyJCBuYSB0YWJlbGEgZGEgbm9ybWFsIHBhZHLDo28gw6kgJDEgLSBcXFBoaSgyKSA9IDEgLSAwLjk3NzIgPSAwLjAyMjgkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4wMjI4fSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUgYSByZWxhw6fDo28gbWF0ZW3DoXRpY2EgZSBjb25jZWl0dWFsIGVudHJlIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCBlIG8gcG9kZXIgZG8gdGVzdGUgJDEtXFxiZXRhJC4gQ29tbyBvIGF1bWVudG8gZG8gdGFtYW5obyBhbW9zdHJhbCAkbiQgYWZldGEgc2ltdWx0YW5lYW1lbnRlIGVzdGFzIGR1YXMgbcOpdHJpY2FzPyIsICJkaWNhIjogIkNvbnNpZGVyZSBvIGNvbXBvcnRhbWVudG8gZGFzIGRpc3RyaWJ1acOnw7VlcyBkZSBwcm9iYWJpbGlkYWRlIHNvYiAkSF8wJCBlICRIXzEkIGNvbmZvcm1lICRuJCBhdW1lbnRhIChvIGVycm8gcGFkcsOjbyBkaW1pbnVpKS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gJFxcYWxwaGEkIMOpIGEgw6FyZWEgZGUgcmVqZWnDp8OjbyBzb2IgYSBkaXN0cmlidWnDp8OjbyBkYSBoaXDDs3Rlc2UgbnVsYSAkSF8wJC4iLCAiMi4gJFxcYmV0YSQgw6kgYSDDoXJlYSBkZSBuw6NvIHJlamVpw6fDo28gc29iIGEgZGlzdHJpYnVpw6fDo28gZGEgaGlww7N0ZXNlIGFsdGVybmF0aXZhICRIXzEkLiIsICIzLiBBbyBhdW1lbnRhciAkbiQsIG8gZXJybyBwYWRyw6NvICRFUChcXGJhcntYfSkgPSBcXHNpZ21hL1xcc3FydHtufSQgZGltaW51aSwgdG9ybmFuZG8gYXMgZGlzdHJpYnVpw6fDtWVzIGRlICRcXGJhcntYfSQgbWFpcyBlc3RyZWl0YXMgKG1lbm9yIHZhcmlhYmlsaWRhZGUpLiIsICI0LiBDb20gZGlzdHJpYnVpw6fDtWVzIG1haXMgJ3BvbnR1ZGFzJywgYSBzb2JyZXBvc2nDp8OjbyBlbnRyZSBhcyBkaXN0cmlidWnDp8O1ZXMgc29iICRIXzAkIGUgJEhfMSQgZGltaW51aS4iLCAiNS4gQ29uc2VxdWVudGVtZW50ZSwgcGFyYSB1bSBtZXNtbyBjcml0w6lyaW8gZGUgZGVjaXPDo28sIHBvZGVtb3MgcmVkdXppciAkXFxiZXRhJCAoYXVtZW50YW5kbyBvIHBvZGVyICQxLVxcYmV0YSQpIHNlbSBuZWNlc3NhcmlhbWVudGUgYXVtZW50YXIgJFxcYWxwaGEkLCBvdSByZWR1emlyIGFtYm9zIG1hbnRlbmRvIG8gZXF1aWzDrWJyaW8uIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoNTgwLCA2MjAsIDEwMDApXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLm5vcm0ucGRmKHgsIDYwMCwgMiksIG5hbWU9J0Rpc3RyaWJ1acOnw6NvIHNvYiBIMCcsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9c3RhdHMubm9ybS5wZGYoeCwgNjA1LCAyKSwgbmFtZT0nRGlzdHJpYnVpw6fDo28gc29iIEgxJywgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJykpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkVmZWl0byBkbyBBdW1lbnRvIGRlIG4gbmEgU29icmVwb3Npw6fDo288L2I+JywgeGF4aXNfdGl0bGU9cidNw6lkaWEgQW1vc3RyYWwgKCRcXGJhcntYfSQpJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiU2VqYSB1bSB0ZXN0ZSBwYXJhIGEgbcOpZGlhIHBvcHVsYWNpb25hbCBjb20gJEhfMDogXFxtdSA9IDEwMCQgZSAkSF8xOiBcXG11IDwgMTAwJC4gU2FiZW5kbyBxdWUgbyB2YWxvciBjcsOtdGljbyBwYXJhICRcXGFscGhhID0gMC4wNSQgw6kgJFpfe1xcdGV4dHtjcml0fX0gPSAtMS42NDUkLCBlIGEgZXN0YXTDrXN0aWNhIGNhbGN1bGFkYSBhIHBhcnRpciBkZSB1bWEgYW1vc3RyYSDDqSAkWl97XFx0ZXh0e2NhbGN9fSA9IC0xLjgyJCwgZGVzY3JldmEgbyBwcm9jZWRpbWVudG8gZGUgZGVjaXPDo28gZSBvIHNpZ25pZmljYWRvIHByw6F0aWNvIGRvIHAtdmFsb3Igc2VyIGluZmVyaW9yIGEgJDAuMDUkLiIsICJkaWNhIjogIkNvbXBhcmUgJFpfe1xcdGV4dHtjYWxjfX0kIGNvbSAkWl97XFx0ZXh0e2NyaXR9fSQgZGVudHJvIGRhIHJlZ2nDo28gY3LDrXRpY2EgZGVmaW5pZGEgcGFyYSAkSF8xOiBcXG11IDwgMTAwJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gQSByZWdpw6NvIGNyw610aWNhIHBhcmEgbyB0ZXN0ZSB1bmlsYXRlcmFsIMOgIGVzcXVlcmRhIMOpICRSQyA9IFxceyBaIDogWiA8IFpfe1xcdGV4dHtjcml0fX0gXFx9JC4iLCAiMi4gVGVtb3MgJFpfe1xcdGV4dHtjYWxjfX0gPSAtMS44MiQgZSAkWl97XFx0ZXh0e2NyaXR9fSA9IC0xLjY0NSQuIiwgIjMuIENvbW8gJC0xLjgyIDwgLTEuNjQ1JCwgYSBlc3RhdMOtc3RpY2EgY2FpIGRlbnRybyBkYSByZWdpw6NvIGNyw610aWNhLiIsICI0LiBBIHJlZ3JhIGRlIGRlY2lzw6NvIMOpIHJlamVpdGFyICRIXzAkLiIsICI1LiBPIHAtdmFsb3IgcmVwcmVzZW50YSBhIHByb2JhYmlsaWRhZGUgZGUgb2J0ZXIgdW0gdmFsb3IgdMOjbyBleHRyZW1vIHF1YW50byAtMS44MiBhc3N1bWluZG8gcXVlICRIXzAkIMOpIHZlcmRhZGVpcmE7IHNlICRwXFx0ZXh0ey12YWxvcn0gPCAwLjA1JCwgYSBldmlkw6puY2lhIGNvbnRyYSAkSF8wJCDDqSBlc3RhdGlzdGljYW1lbnRlIHNpZ25pZmljYXRpdmEgbm8gbsOtdmVsIDUlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSBwcm9jZXNzbyBkZSBwcm9kdcOnw6NvIG9uZGUgYSByZXNpc3TDqm5jaWEgw6AgdHJhw6fDo28gZGUgcGXDp2FzIHNlZ3VlICROKFxcbXUsIDEwMCkkLiBRdWVyZW1vcyB0ZXN0YXIgJEhfMDogXFxtdSA9IDUwJCBjb250cmEgJEhfMTogXFxtdSA9IDYwJC4gQ29tIHVtYSBhbW9zdHJhIGRlIHRhbWFuaG8gJG49MjUkLCBkZWZpbmltb3MgYSByZWdyYSBkZSBkZWNpc8OjbzogcmVqZWl0YXIgJEhfMCQgc2UgJFxcYmFye1h9ID4gNTQkLiBDYWxjdWxlIGEgcHJvYmFiaWxpZGFkZSBkbyBFcnJvIFRpcG8gSUkgKCRcXGJldGEkKSBlIG8gUG9kZXIgZG8gVGVzdGUgKCQxIC0gXFxiZXRhJCkuIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBzb2IgJEhfMSQsICRcXGJhcntYfSBcdGhpY2tzaW0gTig2MCwgXFxzaWdtYV4yL24pJC4gTyBlcnJvIHRpcG8gSUkgw6kgYSBwcm9iYWJpbGlkYWRlIGRlIG7Do28gcmVqZWl0YXIgJEhfMCQgKCRcXGJhcntYfSBcXGxlIDU0JCkgZGFkbyBxdWUgJEhfMSQgw6kgdmVyZGFkZWlyYS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiSWRlbnRpZmljYW1vcyBhIGRpc3RyaWJ1acOnw6NvIGRlICRcXGJhcntYfSQgc29iICRIXzEkOiAkXFxiYXJ7WH0gXFx0aGlja3NpbSBOKDYwLCAxMDAvMjUpID0gTig2MCwgNCkkLiIsICJPIGVycm8gVGlwbyBJSSDDqSAkXFxiZXRhID0gUChcXGJhcntYfSBcXGxlIDU0IHwgXFxtdSA9IDYwKSQuIiwgIlBhZHJvbml6YW1vcyBhIHZhcmnDoXZlbDogJFogPSBcXGZyYWN7XFxiYXJ7WH0gLSA2MH17XFxzcXJ0ezR9fSA9IFxcZnJhY3tcXGJhcntYfSAtIDYwfXsyfSQuIiwgIkNhbGN1bGFtb3M6ICRcXGJldGEgPSBQKFogXFxsZSBcXGZyYWN7NTQgLSA2MH17Mn0pID0gUChaIFxcbGUgLTMpIFxcYXBwcm94IDAsMDAxMzUkLiIsICJPIFBvZGVyIGRvIFRlc3RlIMOpICQxIC0gXFxiZXRhID0gMSAtIDAsMDAxMzUgPSAwLDk5ODY1JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuOTk4NjV9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgcGVyc3BlY3RpdmEgZGEgJ0FycXVpdGV0dXJhIGRvIEVycm8nLCBvIHF1ZSBhY29udGVjZSBjb20gYXMgcHJvYmFiaWxpZGFkZXMgJFxcYWxwaGEkIGUgJFxcYmV0YSQgcXVhbmRvIG8gdGFtYW5obyBhbW9zdHJhbCAkbiQgYXVtZW50YSwgbWFudGVuZG8tc2UgYSByZWdpw6NvIGNyw610aWNhICRSQyQgZml4YS4gUG9yIHF1ZSBpc3NvIMOpIHVtIGRlc2FmaW8gbm8gZGVzaWduIGRlIGV4cGVyaW1lbnRvcz8iLCAiZGljYSI6ICJDb25zaWRlcmUgbyBlZmVpdG8gZG8gYXVtZW50byBkZSAkbiQgc29icmUgbyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhLCAkRVAoXFxiYXJ7WH0pID0gXFxzaWdtYSAvIFxcc3FydHtufSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIsOAIG1lZGlkYSBxdWUgJG4kIGF1bWVudGEsIG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSAkRVAoXFxiYXJ7WH0pID0gXFxzaWdtYSAvIFxcc3FydHtufSQgZGltaW51aS4iLCAiQ29tIGEgcmVkdcOnw6NvIGRhIGRpc3BlcnPDo28gZGEgZGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgZGUgJFxcYmFye1h9JCwgYSBzb2JyZXBvc2nDp8OjbyBlbnRyZSBhcyBkaXN0cmlidWnDp8O1ZXMgc29iICRIXzAkIGUgJEhfMSQgZGltaW51aS4iLCAiTWFudGVuZG8gYSByZWdpw6NvIGNyw610aWNhICRSQyQgZml4YSwgYSBjYXVkYSBkYSBkaXN0cmlidWnDp8OjbyBzb2IgJEhfMCQgcXVlIGNhaSBuYSByZWdpw6NvIGRlIHJlamVpw6fDo28gZGltaW51aSwgcmVkdXppbmRvICRcXGFscGhhJC4iLCAiU2ltdWx0YW5lYW1lbnRlLCBhIGNhdWRhIGRhIGRpc3RyaWJ1acOnw6NvIHNvYiAkSF8xJCBxdWUgcGVybWFuZWNlIGZvcmEgZGEgcmVnacOjbyBkZSByZWplacOnw6NvIHRhbWLDqW0gZGltaW51aSwgcmVkdXppbmRvICRcXGJldGEkLiIsICJDb25jbHVzw6NvOiBPIGF1bWVudG8gZGUgJG4kIG1lbGhvcmEgYSBwcmVjaXPDo28gZG8gdGVzdGUsIHBlcm1pdGluZG8gcmVkdXppciBhbWJvcyBvcyBlcnJvcyBzaW11bHRhbmVhbWVudGUsIG8gcXVlIGF1bWVudGEgbyBwb2RlciBkbyB0ZXN0ZS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bWEgYW5hbG9naWEganVkaWNpYWwsICRIXzAkIHJlcHJlc2VudGEgJ1LDqXUgSW5vY2VudGUnIGUgJEhfMSQgcmVwcmVzZW50YSAnUsOpdSBDdWxwYWRvJy4gQSBSZWdpw6NvIENyw610aWNhICRSQyQgw6kgbyBjb25qdW50byBkZSBwcm92YXMgcXVlIGxldmEgw6AgY29uZGVuYcOnw6NvLiBEZWZpbmEgbyBFcnJvIFRpcG8gSSBlIFRpcG8gSUkgbmVzdGEgYW5hbG9naWEgZSBkaXNjdXRhIGNvbW8gbyBzaXN0ZW1hIGp1csOtZGljbyBsaWRhIGNvbSBvIGRlc2VqbyBkZSBtaW5pbWl6YXIgbyBFcnJvIFRpcG8gSS4iLCAiZGljYSI6ICJPIEVycm8gVGlwbyBJIHNlcmlhIGNvbmRlbmFyIGFsZ3XDqW0gcXVlIMOpIGlub2NlbnRlLiBPIEVycm8gVGlwbyBJSSBzZXJpYSBhYnNvbHZlciBhbGd1w6ltIHF1ZSDDqSBjdWxwYWRvLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJFcnJvIFRpcG8gSTogQ29uZGVuYXIgdW0gcsOpdSBpbm9jZW50ZS4gw4kgY29uc2lkZXJhZG8gdW0gZXJybyBcXGdyYXZlIHF1ZSBvIHNpc3RlbWEgdGVudGEgbWluaW1pemFyIGF0cmF2w6lzIGRvIHByaW5jw61waW8gJ1xcaW4gZHViaW8gcHJvIHJlbycuIiwgIkVycm8gVGlwbyBJSTogQWJzb2x2ZXIgdW0gcsOpdSBjdWxwYWRvLiDDiSBvIGVycm8gZGUgcGVybWl0aXIgcXVlIHVtIGN1bHBhZG8gcmV0b3JuZSDDoCBzb2NpZWRhZGUuIiwgIk8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCBuYSBlc3RhdMOtc3RpY2EgZXF1aXZhbGUgYW8gcmlnb3IgZG8gcGFkcsOjbyBwcm9iYXTDs3JpbyBleGlnaWRvIChleDogJ2Fsw6ltIGRlIHF1YWxxdWVyIGTDunZpZGEgcmF6b8OhdmVsJykuIiwgIkFvIGVsZXZhciBvIHJpZ29yIHByb2JhdMOzcmlvIChkaW1pbnVpciAkXFxhbHBoYSQpLCBvIHNpc3RlbWEganVyw61kaWNvIGluZXJlbnRlbWVudGUgYWNlaXRhIHVtIGF1bWVudG8gcG90ZW5jaWFsIG5hIHByb2JhYmlsaWRhZGUgZGUgRXJybyBUaXBvIElJIChhYnNvbHZlciBjdWxwYWRvcyksIHByaW9yaXphbmRvIGEgcHJvdGXDp8OjbyBkbyBpbm9jZW50ZSBzb2JyZSBhIGNvbmRlbmHDp8OjbyBkbyBjdWxwYWRvLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSBwcm9jZXNzbyBkZSBlbnZhc2UgZGUgYmViaWRhcyBjb20gdm9sdW1lIGFsdm8gZGUgJFxcbXUgPSA2MDAkIG1sIGUgdmFyacOibmNpYSBjb25oZWNpZGEgJFxcc2lnbWFeMiA9IDEwMCQuIFVtYSBhbW9zdHJhIGRlICRuID0gMjUkIHVuaWRhZGVzIMOpIGNvbGV0YWRhLiBEZWZpbmUtc2UgbyB0ZXN0ZSAkSF8wOiBcXG11ID0gNjAwJCBjb250cmEgJEhfMTogXFxtdSBcXG5lcSA2MDAkLiBEZXRlcm1pbmUgYW5hbGl0aWNhbWVudGUgYSBSZWdpw6NvIENyw610aWNhICgkUkMkKSBwYXJhIHVtIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBkZSAkXFxhbHBoYSA9IDAsMDUkLiIsICJkaWNhIjogIlV0aWxpemUgYSBlc3RhdMOtc3RpY2EgJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11XzB9e1xcc2lnbWEvXFxzcXJ0e259fSQgZSBjb25zaWRlcmUgcXVlLCBlbSB1bSB0ZXN0ZSBiaWxhdGVyYWwsIGEgcHJvYmFiaWxpZGFkZSDDqSBkaXN0cmlidcOtZGEgbmFzIGR1YXMgY2F1ZGFzOiAkXFxhbHBoYS8yID0gMCwwMjUkIGVtIGNhZGEuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIElkZW50aWZpY2HDp8OjbyBkb3MgcGFyw6JtZXRyb3M6ICRcXG11XzAgPSA2MDAkLCAkXFxzaWdtYSA9IFxcc3FydHsxMDB9ID0gMTAkLCAkbiA9IDI1JCwgJFxcYWxwaGEgPSAwLDA1JC4iLCAiMi4gQ8OhbGN1bG8gZG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYTogJEVQKFxcYmFye1h9KSA9IFxcZnJhY3tcXHNpZ21hfXtcXHNxcnR7bn19ID0gXFxmcmFjezEwfXtcXHNxcnR7MjV9fSA9IFxcZnJhY3sxMH17NX0gPSAyJC4iLCAiMy4gRGVmaW5pw6fDo28gZG8gdmFsb3IgY3LDrXRpY286IFBhcmEgJFxcYWxwaGEgPSAwLDA1JCBlIHRlc3RlIGJpbGF0ZXJhbCwgYnVzY2Ftb3MgJFpfe1xcdGV4dHtjcml0fX0kIHRhbCBxdWUgJFAofFp8ID4gWl97XFx0ZXh0e2NyaXR9fSkgPSAwLDA1JC4gTG9nbywgJFpfe1xcdGV4dHtjcml0fX0gPSAxLDk2JC4iLCAiNC4gQ8OhbGN1bG8gZG9zIGxpbWl0ZXMgZGUgJFxcYmFye1h9X2MkOiAkXFxiYXJ7WH1fe2N9ID0gXFxtdV8wIFxccG0gWl97XFx0ZXh0e2NyaXR9fSBcXGNkb3QgRVAoXFxiYXJ7WH0pID0gNjAwIFxccG0gMSw5NiBcXGNkb3QgMiQuIiwgIjUuIExpbWl0ZSBpbmZlcmlvcjogJFxcYmFye1h9X3tjMX0gPSA2MDAgLSAzLDkyID0gNTk2LDA4JC4iLCAiNi4gTGltaXRlIHN1cGVyaW9yOiAkXFxiYXJ7WH1fe2MyfSA9IDYwMCArIDMsOTIgPSA2MDMsOTIkLiIsICI3LiBDb25jbHVzw6NvOiAkUkMgPSB7IFxcYmFye1h9IDogXFxiYXJ7WH0gPCA1OTYsMDggXFxjdXAgXFxiYXJ7WH0gPiA2MDMsOTIgfSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIHRveGljb2xvZ2lhLCBhIGNvbmNlbnRyYcOnw6NvIG3DqWRpYSBkZSB1bSBjb250YW1pbmFudGUgJFxcbXUkIGVtIG1pbGlncmFtYXMgcG9yIGxpdHJvIGRldmUgc2VyIGlndWFsIGEgJDEwJCBtZy9MLiBVbWEgYW1vc3RyYSBkZSAkMTYkIG1lZGnDp8O1ZXMgcmVzdWx0b3UgZW0gdW1hIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0gPSAxMiQgbWcvTCwgY29tIGRlc3ZpbyBwYWRyw6NvIGFtb3N0cmFsICRTID0gMiw0JCBtZy9MLiBDb25zaWRlcmFuZG8gYSBkaXN0cmlidWnDp8OjbyAkdCQgZGUgU3R1ZGVudCBjb20gJG4tMSQgZ3JhdXMgZGUgbGliZXJkYWRlLCBtb250ZSBhIHJlZ3JhIGRlIGRlY2lzw6NvIHBhcmEgdW0gdGVzdGUgdW5pbGF0ZXJhbCDDoCBkaXJlaXRhICgkSF8xOiBcXG11ID4gMTAkKSBjb20gJFxcYWxwaGEgPSAwLDA1JC4iLCAiZGljYSI6ICJPIHZhbG9yIGNyw610aWNvICR0X3tcXHRleHR7Y3JpdH19JCBkZXZlIHNlciBidXNjYWRvIG5hIHRhYmVsYSAkdCQgY29tICRnbCA9IG4tMSA9IDE1JCBncmF1cyBkZSBsaWJlcmRhZGUgZSDDoXJlYSBkZSAkMCwwNSQgbmEgY2F1ZGEgc3VwZXJpb3IuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIEhpcMOzdGVzZXM6ICRIXzA6IFxcbXUgPSAxMCQsICRIXzE6IFxcbXUgPiAxMCQuIiwgIjIuIFBhcsOibWV0cm9zOiAkbj0xNiwgXFxiYXJ7WH09MTIsIFxcbXVfMD0xMCwgUz0yLDQsIGdsPTE1JC4iLCAiMy4gRXN0YXTDrXN0aWNhIGRlIHRlc3RlOiAkdF97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXVfMH17Uy9cXHNxcnR7bn19ID0gXFxmcmFjezEyIC0gMTB9ezIsNC9cXHNxcnR7MTZ9fSA9IFxcZnJhY3syfXsyLDQvNH0gPSBcXGZyYWN7Mn17MCw2fSA9IDMsMzMkLiIsICI0LiBSZWdyYSBkZSBkZWNpc8OjbzogJFJDID0geyB0IDogdCA+IHRfe1xcdGV4dHtjcml0fX0gfSQuIiwgIjUuIFZhbG9yIGNyw610aWNvICR0X3tcXHRleHR7Y3JpdH19JCBwYXJhICRnbD0xNSwgXFxhbHBoYT0wLDA1JDogJHRfe1xcdGV4dHtjcml0fX0gXFxhcHByb3ggMSw3NTMkLiIsICI2LiBEZWNpc8OjbzogQ29tbyAkMywzMyA+IDEsNzUzJCwgbyB2YWxvciBjYWkgbmEgJFJDJC4gUmVqZWl0YS1zZSAkSF8wJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDMuMzN9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgZG8gcG9udG8gZGUgdmlzdGEgZGEgZ2VzdMOjbyBkZSByaXNjb3MsIHBvciBxdWUgYSBlc2NvbGhhIGRhIFJlZ2nDo28gQ3LDrXRpY2EgKCRSQyQpIGVtIHVtIHRlc3RlIGRlIGhpcMOzdGVzZXMgw6kgZnVuZGFtZW50YWwgcGFyYSB1bSBlbmdlbmhlaXJvIGRlIGNvbnRyb2xlIGRlIHByb2Nlc3Nvcy4gQ29tbyBhIGFsdGVyYcOnw6NvIG5hIGxvY2FsaXphw6fDo28gZG8gdmFsb3IgY3LDrXRpY28gJFxcaGF0e1xcdGhldGF9X2MkIGltcGFjdGEgYSByZWxhw6fDo28gZW50cmUgb3MgZXJyb3MgZG8gdGlwbyBJIGUgSUk/IiwgImRpY2EiOiAiQ29uc2lkZXJlIG8gY29uY2VpdG8gZGUgY29tcHJvbWlzc28gKHRyYWRlLW9mZikgZW50cmUgb3MgZXJyb3MgZSBhIG5hdHVyZXphIGRhIFJlZ2nDo28gZGUgUmVqZWnDp8OjbyBjb21vIHpvbmEgZGUgYcOnw6NvIGludGVydmVudGl2YS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gTyB2YWxvciBjcsOtdGljbyAkXFxoYXR7XFx0aGV0YX1fYyQgYXR1YSBjb21vIG8gZ2F0aWxobyBvcGVyYWNpb25hbCBxdWUgZGVmaW5lIHF1YW5kbyB1bSBwcm9jZXNzbyDDqSBpbnRlcnJvbXBpZG8gcGFyYSBpbnRlcnZlbsOnw6NvLiIsICIyLiBBdW1lbnRhciBhICRSQyQgKHRvcm5hbmRvIG8gdGVzdGUgbWFpcyBsaWJlcmFsKSBkaW1pbnVpIGEgcHJvYmFiaWxpZGFkZSBkbyBFcnJvIFRpcG8gSUkgKCRcXGJldGEkKSwgYXVtZW50YW5kbyBvIFBvZGVyIGRvIFRlc3RlICgkMS1cXGJldGEkKSwgbWFzIGFtcGxpYSBvIEVycm8gVGlwbyBJICgkXFxhbHBoYSQpLCBnZXJhbmRvIG1haXMgaW50ZXJ2ZW7Dp8O1ZXMgZGVzbmVjZXNzw6FyaWFzLiIsICIzLiBEaW1pbnVpciBhICRSQyQgKHRvcm5hbmRvIG8gdGVzdGUgbWFpcyBjb25zZXJ2YWRvcikgcHJvdGVnZSBvIHByb2Nlc3NvIGRlIGludGVydmVuw6fDtWVzIGRlc25lY2Vzc8OhcmlhcywgcmVkdXppbmRvICRcXGFscGhhJCwgbWFzIGF1bWVudGEgbyByaXNjbyBkZSBuw6NvIGRldGVjdGFyIHVtIHByb2JsZW1hIHJlYWwgKCRcYlxcZXRhJCkuIiwgIjQuIEEgZXNjb2xoYSDDs3RpbWEgZGUgJFxcaGF0e1xcdGhldGF9X2MkIGRlcGVuZGUgZG8gY3VzdG8gcmVsYXRpdm8gZW50cmUgcmVhbGl6YXIgdW1hIG1hbnV0ZW7Dp8OjbyBwcmV2ZW50aXZhIChmYWxzbyBwb3NpdGl2bykgZSBuw6NvIGRldGVjdGFyIHVtYSBmYWxoYSBubyBzaXN0ZW1hIChmYWxzbyBuZWdhdGl2bykuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfV19').decode('utf-8'))


    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo do progresso
    total_mcq = len(dados_exercicios.get("questoes_multipla_escolha", []))
    total_disc = len(dados_exercicios.get("questoes_discursivas", []))
    total_exercicios = total_mcq + total_disc
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    # Interface de progresso
    st.markdown("### 🎯 Desafios de Aprendizagem")
    if total_exercicios > 0:
        progresso = acertos / total_exercicios
        st.progress(progresso)
        st.markdown(f"🏆 **Seu Progresso:** {acertos} de {total_exercicios} desafios concluídos!")
    st.divider()
    
    # Processamento das Questões de Múltipla Escolha
    for i, questao in enumerate(dados_exercicios.get("questoes_multipla_escolha", [])):
        st.markdown(f"**Questão {i + 1}:** {questao.get('enunciado', '')}")
        
        # Referência (se existir)
        if questao.get("referencia_livro"):
            st.markdown(f"📖 *Referência: {questao.get('referencia_livro')}*")
        
        # Plotly Dinâmico (se existir)
        if questao.get("codigo_plotly"):
            try:
                local_vars = {"go": go, "np": np, "stats": stats}
                exec(questao["codigo_plotly"], globals(), local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True)
            except Exception as e:
                st.error(f"Erro ao renderizar gráfico: {e}")
    
        # Alternativas
        opcoes = questao.get("alternativas", {})
        escolha = st.radio(
            "Selecione uma alternativa:",
            list(opcoes.values()),
            key=f"radio_mcq_{i}",
            index=None
        )
    
        # Dica
        with st.expander("💡 Precisa de uma dica?"):
            st.info(questao.get("dica", "Dica indisponível"))
    
        # Botão de verificação
        if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
            if escolha == opcoes.get(questao.get("alternativa_correta")):
                st.success("Correto! Muito bem.")
                st.session_state.respostas_certas[f"mcq_{i}"] = True
            else:
                st.error("Resposta incorreta. Tente novamente!")
                st.session_state.respostas_certas[f"mcq_{i}"] = False
            st.rerun()
    
        # Gabarito
        with st.expander("✅ Ver Gabarito Comentado"):
            st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
        st.divider()
    
    # Processamento das Questões Discursivas
    for i, questao in enumerate(dados_exercicios.get("questoes_discursivas", [])):
        st.markdown(f"**Desafio {i + 1}:** {questao.get('enunciado', '')}")
        
        if questao.get("referencia_livro"):
            st.markdown(f"📖 *Referência: {questao.get('referencia_livro')}*")
    
        st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
    
        # Plotly Dinâmico (se existir)
        if questao.get("codigo_plotly"):
            try:
                local_vars = {"go": go, "np": np, "stats": stats}
                exec(questao["codigo_plotly"], globals(), local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True)
            except Exception as e:
                st.error(f"Erro ao renderizar gráfico: {e}")
    
        # Validação Numérica ou Qualitativa
        resposta_esperada = questao.get("resposta_numerica_esperada")
        if resposta_esperada is not None:
            user_val = st.number_input("Digite o resultado numérico calculado para validação:", key=f"num_disc_{i}", format="%.4f")
            if st.button("Validar Cálculo", key=f"btn_disc_val_{i}"):
                if abs(user_val - resposta_esperada) <= max(0.01, 0.01 * abs(resposta_esperada)):
                    st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.error("O valor calculado difere do gabarito. Verifique seus arredondamentos e fórmulas.")
                    st.session_state.respostas_certas[f"disc_{i}"] = False
                st.rerun()
        else:
            if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                st.session_state.respostas_certas[f"disc_{i}"] = True
            else:
                st.session_state.respostas_certas[f"disc_{i}"] = False
    
        # Dica e Resolução
        with st.expander("💡 Dica"):
            st.info(questao.get("dica", "Dica indisponível"))
        
        with st.expander("✅ Ver Resolução Detalhada"):
            for passo in questao.get("gabarito_passo_a_passo", []):
                st.write(f"- {passo}")
        st.divider()
