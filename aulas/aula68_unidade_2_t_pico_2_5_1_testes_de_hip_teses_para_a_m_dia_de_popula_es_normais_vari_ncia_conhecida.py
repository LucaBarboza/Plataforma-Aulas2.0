import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNS4xOiBUZXN0ZXMgZGUgaGlww7N0ZXNlcyBwYXJhIGEgbcOpZGlhIGRlIHBvcHVsYcOnw7VlcyBOb3JtYWlzIChWYXJpw6JuY2lhIGNvbmhlY2lkYSkiLCAicmVmZXJlbmNpYXNfYmlibGlvZ3JhZmljYXNfZmluYWlzIjogWyJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDEyLCBwcC4gMzM4LTM0MSIsICJDYXJvbGluYSBDLiBNLiBQYXJhw61iYSwgTUFURDM4IEVzdGF0w61zdGljYSBCw6FzaWNhIEIgLSBVbmlkYWRlIDIsIHBwLiA5LTEzIl19').decode('utf-8'))

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
            background: linear-gradient(135deg, #064E3B 0%, #3B82F6 100%);
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
            border-top: 3px solid #064E3B !important;
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
            background: linear-gradient(90deg, #064E3B 0%, #10B981 100%) !important;
            border-radius: 10px !important;
        }
        
        /* Inputs e Sliders na aula */
        div.stSlider [data-testid="stSliderTickBar"] {
            background-color: #064E3B !important;
        }
        
        /* Botões na aula */
        div.stButton > button {
            background: linear-gradient(135deg, #064E3B 0%, #3B82F6 100%) !important;
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
PRIMARY_BLUE = "#064E3B"
SECONDARY_GREEN = "#10B981"
WARNING_AMBER = "#34D399"
CRITICAL_RED = "#991B1B"

# Criação das Duas Grandes Abas Globais
tab_conteudo, tab_exercicios = st.tabs(["📚 Conteúdo Acadêmico Interativo", "📝 Caderno de Exercícios"])

with tab_conteudo:

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # --- Seção 1: Introdução Teórica ---
    st.markdown(r"### A Estrutura Lógica do Teste de Hipóteses Paramétrico")
    
    st.markdown(r"""
    O teste de hipóteses paramétrico é um procedimento de decisão estatística que permite avaliar a veracidade de uma afirmação sobre um parâmetro populacional desconhecido utilizando evidências amostrais. Em processos industriais, como o enchimento de pacotes, a necessidade de verificar a conformidade com padrões de qualidade exige que confrontemos o status quo, representado pela hipótese nula (H0), com uma hipótese alternativa (H1) que descreve um desvio de interesse.
    """)
    
    st.info(r"Como a inferência é baseada em amostras, introduzimos o conceito de nível de significância (alpha), que limita a probabilidade de rejeitar incorretamente uma hipótese nula verdadeira.")
    
    st.markdown(r"""
    O teste de hipóteses não deve ser encarado apenas como um conjunto de algoritmos, mas como uma disciplina intelectual que medeia o conflito entre a realidade populacional inobservável e a finitude das evidências. Quando um engenheiro de qualidade observa o enchimento, ele está engajado em um processo de conformidade onde a média real do processo ($\mu$) encontra-se sob o manto da variabilidade estocástica.
    """)
    
    # --- Seção 2: Formalismo Matemático ---
    st.markdown(r"#### Formalismo do Teste")
    
    col1, col2 = st.columns(2)
    with col1:
        st.latex(r"H_0: \mu = \mu_0 \quad \text{vs.} \quad H_1: \mu \neq \mu_0")
    with col2:
        st.latex(r"Z_{\text{calc}} = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}")
    
    st.markdown(r"A decisão é tomada comparando a estatística calculada com a região crítica (RC):")
    st.latex(r"\text{Região Crítica (RC): } |Z_{\text{calc}}| > Z_{\text{crit}}")
    
    # --- Seção 3: Dedução Analítica ---
    st.markdown(r"#### Dedução Analítica")
    st.markdown(r"- **Passo 1:** Definição da distribuição sob a hipótese nula:")
    st.latex(r"Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0,1) \text{ sob } H_0: \mu = \mu_0")
    st.markdown(r"- **Passo 2:** Nível de significância como limiar de erro Tipo I:")
    st.latex(r"\alpha = P(|Z_{\text{calc}}| > Z_{\text{crit}} \mid H_0)")
    st.markdown(r"- **Passo 3:** Critério de decisão:")
    st.latex(r"\text{Se } |Z_{\text{calc}}| > Z_{\text{crit}}, \text{ rejeita-se } H_0")
    
    # --- Seção 4: Exemplo Prático ---
    st.markdown(r"#### Exemplo Prático: Indústria Alimentícia")
    with st.container(border=True):
        st.markdown(r"**Contexto:** Uma máquina de envase está configurada para 500g ($\sigma^2=400$). Amostra de 16 pacotes resulta em 492g. Nível de significância $\alpha = 0.01$.")
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(r"- $\mu_0 = 500$")
            st.markdown(r"- $\sigma = 20$")
        with col_b:
            st.markdown(r"- $n = 16$")
            st.markdown(r"- $\bar{X} = 492$")
            
        st.markdown(r"**Desenvolvimento:**")
        st.latex(r"EP(\bar{X}) = \frac{20}{\sqrt{16}} = 5")
        st.latex(r"Z_{\text{calc}} = \frac{492 - 500}{5} = -1.6")
        
        st.success(r"Laudo: Como $|Z_{\text{calc}}| = 1.6 < Z_{0.005} = 2.58$, não há evidência suficiente para rejeitar $H_0$. O processo permanece sob controle.")
    
    # --- Seção 5: Simulador Interativo ---
    st.markdown(r"#### Simulador de Região Crítica")
    col_s1, col_s2 = st.columns(2)
    n_val = col_s1.slider(r"Tamanho da Amostra (n)", 5, 100, 16, key=r"n_val_subtopico_1")
    alpha_val = col_s2.selectbox(r"Nível de Significância ($\alpha$)", [0.01, 0.05, 0.10], key=r"alpha_val_subtopico_1")
    
    z_crit = stats.norm.ppf(1 - alpha_val/2)
    x = np.linspace(-4, 4, 100)
    y = stats.norm.pdf(x, 0, 1)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Distribuição N(0,1)', line=dict(color='#064E3B')))
    fig.add_vline(x=z_crit, line_dash="dash", line_color="#991B1B", annotation_text="Z_crit")
    fig.add_vline(x=-z_crit, line_dash="dash", line_color="#991B1B", annotation_text="-Z_crit")
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Regiões de Aceitação e Rejeição</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B")),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    fig.update_xaxes(title=dict(text="Z-score", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True)
    fig.update_yaxes(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True)
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    st.info(rf"Com $\alpha = {alpha_val}$, o valor crítico é $\pm {z_crit:.2f}$. Qualquer valor de Z fora desse intervalo implica em rejeição da hipótese de normalidade/estabilidade.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    # --- Cabeçalho Acadêmico ---
    st.header(r"Critérios de Decisão: Testes Bilaterais e Unilaterais")
    
    st.markdown(r"""
    A formulação de um teste de hipóteses é guiada pelo objetivo investigativo, que dita a escolha entre testes bilaterais e unilaterais. 
    Enquanto o teste bilateral verifica se o parâmetro desviou da média esperada em qualquer direção, os testes unilaterais são desenhados 
    para capturar mudanças direcionais, como um incremento ou decremento no consumo de recursos ou na eficácia de tratamentos. 
    """)
    
    st.info(r"A escolha estratégica amplia a sensibilidade do teste para hipóteses específicas, alterando a alocação da região de rejeição nas caudas da distribuição normal padrão.")
    
    # --- Seção de Formalismo ---
    st.subheader(r"Formalismo Estatístico")
    st.latex(r"Z_{\text{calc}} = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(r"**Bilateral**")
        st.latex(r"|Z_{\text{calc}}| > Z_{\frac{\alpha}{2}}")
    with col2:
        st.markdown(r"**Unilateral Superior**")
        st.latex(r"Z_{\text{calc}} > Z_{1-\alpha}")
    with col3:
        st.markdown(r"**Unilateral Inferior**")
        st.latex(r"Z_{\text{calc}} < Z_{\alpha}")
    
    # --- Dedução Analítica ---
    st.subheader(r"Dedução da Estatística de Teste")
    st.markdown(r"1. Consideramos a distribuição da média amostral: $\bar{X} \sim N(\mu_0, \sigma^2/n)$")
    st.markdown(r"2. Padronizamos a variável para a distribuição normal padrão: $Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}} \sim N(0,1)$")
    st.markdown(r"3. Definimos o valor crítico $Z_{\text{crit}}$ tal que $P(Z > Z_{\text{crit}}) = \alpha$")
    st.markdown(r"4. A decisão é tomada comparando a estatística $Z_{\text{calc}}$ com os quantis da Normal Padrão.")
    
    # --- Simulador Interativo ---
    st.subheader(r"Visualizador de Regiões de Rejeição")
    col_s1, col_s2 = st.columns(2)
    tipo_teste = col_s1.selectbox(r"Tipo de Teste", ["Bilateral", "Unilateral Superior", "Unilateral Inferior"], key="tipo_teste_subtopico_2")
    alpha = col_s2.slider(r"Nível de Significância (alpha)", 0.01, 0.10, 0.05, 0.01, key="alpha_subtopico_2")
    
    x = np.linspace(-4, 4, 200)
    y = norm.pdf(x, 0, 1)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Distribuição Normal', line=dict(color='#064E3B')))
    
    if tipo_teste == "Bilateral":
        z_crit = norm.ppf(1 - alpha/2)
        fig.add_vrect(x0=z_crit, x1=4, fillcolor="#991B1B", opacity=0.3, line_width=0)
        fig.add_vrect(x0=-4, x1=-z_crit, fillcolor="#991B1B", opacity=0.3, line_width=0)
    elif tipo_teste == "Unilateral Superior":
        z_crit = norm.ppf(1 - alpha)
        fig.add_vrect(x0=z_crit, x1=4, fillcolor="#991B1B", opacity=0.3, line_width=0)
    else:
        z_crit = norm.ppf(alpha)
        fig.add_vrect(x0=-4, x1=z_crit, fillcolor="#991B1B", opacity=0.3, line_width=0)
    
    fig.update_layout(
        template="plotly_white", height=420, margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Distribuição Normal e Regiões de Rejeição</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Valor de Z", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Densidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    st.info(r"O gráfico acima exibe a região de rejeição (vermelha) baseada no tipo de teste e nível de significância escolhidos. Qualquer $Z_{\text{calc}}$ nesta região leva à rejeição da hipótese nula.")
    
    # --- Exemplo Prático ---
    st.subheader(r"Aplicação Prática: Fábrica de Café")
    with st.container(border=True):
        st.markdown(r"##### 📖 Enunciado: Análise de Subdosagem")
        st.write(r"Gestor analisa se pacotes de café estão abaixo de 500g. Dados: $\mu_0 = 500, \sigma = 20, n = 16, \bar{X} = 492, \alpha = 0.05$.")
        
        st.write(r"**Cálculos:**")
        st.latex(r"EP(\bar{X}) = \frac{20}{\sqrt{16}} = 5")
        st.latex(r"Z_{\text{calc}} = \frac{492 - 500}{5} = -1.6")
        st.latex(r"Z_{\text{crit}} = z_{0.05} = -1.645")
        
        st.warning(r"Como $Z_{\text{calc}} (-1.6) > Z_{\text{crit}} (-1.645)$, não rejeitamos a hipótese nula.")
        st.success(r"Conclusão: Não há evidências estatísticas suficientes ao nível de 5% para afirmar que a máquina opera com subdosagem.")
    
    # --- Prosa Expandida ---
    st.subheader(r"Perspectiva Teórica")
    st.markdown(r"""
    A inferência estatística, em sua essência, não é apenas um exercício de cálculo numérico, mas um rigoroso protocolo de tomada de decisão sob incerteza. 
    Quando nos deparamos com a necessidade de inferir propriedades sobre uma população, a formulação do teste de hipóteses atua como o alicerce metodológico 
    que nos protege contra conclusões espúrias. 
    
    A dicotomia entre testes bilaterais e unilaterais transcende a matemática: no bilateral, buscamos imparcialidade ante qualquer desvio; no unilateral, 
    aplicamos uma ferramenta de precisão direcionada à expectativa de mudança do pesquisador. Ignorar essa distinção em favor da 'pesca' de significância 
    é um vício intelectual que compromete a integridade da investigação científica.
    """)

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    # --- Cabeçalho e Introdução ---
    st.header(r"Aplicações Inferenciais e Interpretação de Resultados")
    st.markdown(r"A etapa final do teste de hipóteses envolve a síntese dos resultados amostrais para inferir sobre a população. A interpretação vai além da simples rejeição ou aceitação de $H_0$; ela engloba o entendimento profundo do erro tipo II e do poder do teste.")
    
    st.info(r"O poder do teste ($1 - \beta$) é crucial para avaliar a eficácia do procedimento em detectar desvios reais quando a hipótese nula é efetivamente falsa, sendo influenciado pelo tamanho da amostra e pela magnitude do desvio.")
    
    # --- Formalismo Matemático ---
    st.subheader(r"Formalismo Teórico")
    st.latex(r"H_0: \mu = \mu_0 \quad \text{vs.} \quad H_1: \mu \neq \mu_0")
    st.latex(r"Z_{\text{calc}} = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}")
    st.latex(r"1 - \beta = P(\text{Rejeitar } H_0 \mid \mu = \mu_a)")
    
    # --- Dedução Analítica ---
    with st.expander(r"Dedução Analítica do Poder do Teste"):
        st.markdown(r"Abaixo, a sequência de derivação para o cálculo da probabilidade de erro tipo II ($\beta$):")
        st.latex(r"Z_{\text{calc}} = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}")
        st.latex(r"\beta = P(-Z_{\text{crit}} < Z_{\text{calc}} < Z_{\text{crit}} \mid \mu = \mu_a)")
        st.latex(r"\beta = P\left( \frac{\mu_0 - \mu_a}{\sigma / \sqrt{n}} - Z_{\text{crit}} < Z < \frac{\mu_0 - \mu_a}{\sigma / \sqrt{n}} + Z_{\text{crit}} \right)")
        st.latex(r"1 - \beta = P\left( Z > Z_{\text{crit}} - \frac{\mu_a - \mu_0}{\sigma/\sqrt{n}} \right) + P\left( Z < -Z_{\text{crit}} - \frac{\mu_a - \mu_0}{\sigma/\sqrt{n}} \right)")
    
    # --- Exemplo Prático ---
    st.subheader(r"Aplicação em Controle de Qualidade")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Prático: Resistores de Precisão")
        st.markdown(r"Uma fábrica afirma que a resistência média é $100\Omega$, com $\sigma = 2\Omega$. Com $n=25$, observou-se $\bar{X} = 100,8\Omega$. Testamos a $5\%$ de significância.")
        
        col_dados1, col_dados2 = st.columns(2)
        col_dados1.metric(label=r"Média Amostral", value=r"100.8")
        col_dados2.metric(label=r"Erro Padrão", value=r"0.4")
        
        st.markdown(r"**Desenvolvimento:**")
        st.latex(r"Z_{\text{calc}} = \frac{100.8 - 100}{0.4} = 2.0")
        st.markdown(r"Como $2.0 > 1.96$, rejeitamos $H_0$.")
        
        st.success(r"Laudo: Há evidências estatísticas suficientes para afirmar que a resistência média difere de $100\Omega$. Recomenda-se calibração no processo de fabricação.")
    
    # --- Simulador Interativo ---
    st.subheader(r"Simulador de Poder do Teste")
    col1, col2 = st.columns(2)
    mu_a = col1.slider(r"Média Alternativa ($\mu_a$)", 100.0, 105.0, 102.0, step=0.1, key=r"mu_a_subtopico_3")
    n_sample = col2.slider(r"Tamanho da Amostra ($n$)", 10, 100, 25, step=5, key=r"n_subtopico_3")
    
    # Lógica Plotly
    x = np.linspace(95, 105, 500)
    y_h0 = norm.pdf(x, 100, 2/np.sqrt(n_sample))
    y_ha = norm.pdf(x, mu_a, 2/np.sqrt(n_sample))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y_h0, name=r"Distribuição H0", line=dict(color="#064E3B")))
    fig.add_trace(go.Scatter(x=x, y=y_ha, name=r"Distribuição HA", line=dict(color="#10B981")))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Poder do Teste e Sobreposição de Distribuições</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Resistência", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    # Laudo Reativo
    st.info(rf"Com $\mu_a = {mu_a}$ e $n = {n_sample}$, a sobreposição entre as curvas diminui conforme a amostra aumenta, elevando o poder do teste ($1-\beta$) e tornando a distinção entre as hipóteses mais nítida.")
    
    # --- Conclusão Final ---
    st.markdown(r"A jornada através da inferência estatística culmina no confronto entre construções teóricas e a realidade empírica. O estatístico maduro compreende que um teste de hipóteses é uma aposta calculada contra a incerteza do mundo.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNS4xOiBUZXN0ZXMgZGUgaGlww7N0ZXNlcyBwYXJhIGEgbcOpZGlhIGRlIHBvcHVsYcOnw7VlcyBOb3JtYWlzIChWYXJpw6JuY2lhIGNvbmhlY2lkYSkiLCAicXVlc3RvZXNfbXVsdGlwbGFfZXNjb2xoYSI6IFt7ImVudW5jaWFkbyI6ICJVbWEgaW5kw7pzdHJpYSBkZSBsYXRpY8OtbmlvcyB1dGlsaXphIHVtYSBtw6FxdWluYSBkZSBlbnZhc2UgYXV0b23DoXRpY2EgY29uZmlndXJhZGEgcGFyYSBkZXBvc2l0YXIgMTAwMGcgZGUgbGVpdGUgZW0gY2FkYSBlbWJhbGFnZW0uIE8gZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsIGRvIHByb2Nlc3NvIMOpIGNvbmhlY2lkbyBlIHZhbGUgJFxcc2lnbWEgPSAxNWckLiBBcMOzcyB1bWEgbWFudXRlbsOnw6NvIGNvcnJldGl2YSwgbyBjb250cm9sZSBkZSBxdWFsaWRhZGUgZGVzZWphIHZlcmlmaWNhciBzZSBhIG3DqWRpYSBkZSBlbnZhc2UgJFxcbXUkIHBlcm1hbmVjZSBlbSAxMDAwZy4gVW1hIGFtb3N0cmEgYWxlYXTDs3JpYSBkZSAkbiA9IDM2JCBlbWJhbGFnZW5zIGFwcmVzZW50b3UgdW1hIG3DqWRpYSBhbW9zdHJhbCBkZSAkXFxiYXJ7WH0gPSAxMDA1ZyQuIEFvIGFkb3RhciB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgZGUgJFxcYWxwaGEgPSAwLjA1JCwgcXVhbCDDqSBhIGNvbmNsdXPDo28gY29ycmV0YSBiYXNlYWRhIG5vIHRlc3RlIGRlIGhpcMOzdGVzZXMgcGFyYW3DqXRyaWNvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiUmVqZWl0YS1zZSAkSF8wJCwgcG9pcyBvIHZhbG9yIGNhbGN1bGFkbyAkWl97XHRleHR7Y2FsY319ID0gMi4wMCQgw6kgc3VwZXJpb3IgYW8gdmFsb3IgY3LDrXRpY28gJFpfe1x0ZXh0e2NyaXR9fSA9IDEuOTYkLiIsICJCIjogIk7Do28gc2UgcmVqZWl0YSAkSF8wJCwgcG9pcyBvIHZhbG9yIGNhbGN1bGFkbyAkWl97XHRleHR7Y2FsY319ID0gMC4zMyQgw6kgaW5mZXJpb3IgYW8gdmFsb3IgY3LDrXRpY28gJFpfe1x0ZXh0e2NyaXR9fSA9IDEuOTYkLiIsICJDIjogIlJlamVpdGEtc2UgJEhfMCQsIHBvaXMgbyB2YWxvciBjYWxjdWxhZG8gJFpfe1x0ZXh0e2NhbGN9fSA9IDIuMDAkIMOpIG1lbm9yIHF1ZSBvIHZhbG9yIGNyw610aWNvLCBtYXMgYWluZGEgc2lnbmlmaWNhdGl2by4iLCAiRCI6ICJOw6NvIHNlIHJlamVpdGEgJEhfMCQsIHBvaXMgbyB2YWxvciBjYWxjdWxhZG8gJFpfe1x0ZXh0e2NhbGN9fSA9IDEuMzMkIMOpIGluZmVyaW9yIGFvIHZhbG9yIGNyw610aWNvICRaX3tcdGV4dHtjcml0fX0gPSAxLjk2JC4iLCAiRSI6ICJPIHRlc3RlIMOpIGluY29uY2x1c2l2bywgcG9pcyBvIHRhbWFuaG8gZGEgYW1vc3RyYSAkbj0zNiQgw6kgaW5zdWZpY2llbnRlIHBhcmEgYXByb3hpbWFyIGEgZGlzdHJpYnVpw6fDo28gZGEgbcOpZGlhIMOgIG5vcm1hbC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIkxlbWJyZS1zZSBkZSBjYWxjdWxhciBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWE6ICRFUChcXGJhcntYfSkgPSBcXHNpZ21hIC8gXFxzcXJ0e259JC4gTyB2YWxvciBkZSAkWl97XFx0ZXh0e2NhbGN9fSQgY29tcGFyYSBhIGRpZmVyZW7Dp2EgZW50cmUgYSBtw6lkaWEgb2JzZXJ2YWRhIGUgYSBub21pbmFsIGVtIHVuaWRhZGVzIGRlIGVycm8gcGFkcsOjby4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBhcmEgcmVhbGl6YXIgbyB0ZXN0ZSwgZGVmaW5pbW9zICRIXzA6IFxcbXUgPSAxMDAwJCBlICRIXzE6IFxcbXUgXFxuZXEgMTAwMCQuIENhbGN1bGFtb3MgJFpfe1x0ZXh0e2NhbGN9fSA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXVfMH17XFxzaWdtYSAvIFxcc3FydHtufX0gPSBcXGZyYWN7MTAwNSAtIDEwMDB9ezE1IC8gXFxzcXJ0ezM2fX0gPSBcXGZyYWN7NX17MTUgLyA2fSA9IFxcZnJhY3s1fXsyLjV9ID0gMi4wMCQuIFBhcmEgJFxcYWxwaGEgPSAwLjA1JCBlbSB1bSB0ZXN0ZSBiaWxhdGVyYWwsIG8gdmFsb3IgY3LDrXRpY28gJFpfe1x0ZXh0e2NyaXR9fSQgw6kgMS45Ni4gQ29tbyAkfFpfe1x0ZXh0e2NhbGN9fXwgPiAxLjk2JCwgcmVqZWl0YW1vcyAkSF8wJC4gRXJyb3MgY29tdW5zOiAoQikgb2NvcnJlIHNlIG8gYWx1bm8gZXNxdWVjZXIgZGUgZXh0cmFpciBhIHJhaXogcXVhZHJhZGEgZGUgJG4kOyAoRCkgb2NvcnJlIHNlIG8gYWx1bm8gZGl2aWRpciBwb3IgJG4kIGVtIHZleiBkZSAkXFxzcXJ0e259JC4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKTsgeCA9IG5wLmxpbnNwYWNlKC00LCA0LCAxMDApOyB5ID0gKDEgLyBucC5cXHNxcnQoMiAqIG5wLlxccGkpKSAqIG5wLlxcZXhwKC0wLjUgKiB4KioyKTsgZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBsaW5lPWRpY3QoY29sb3I9JyMwNjRFM0InLCB3aWR0aD0yKSwgbmFtZT0nTigwLDEpJykpOyB4X2NyaXRfcG9zID0gbnAubGluc3BhY2UoMS45NiwgNCwgNTApOyB5X2NyaXRfcG9zID0gKDEgLyBucC5cXHNxcnQoMiAqIG5wLlxccGkpKSAqIG5wLlxcZXhwKC0wLjUgKiB4X2NyaXRfcG9zKioyKTsgZmlnLmFkZF90cmFjZShnby5GaWxsKHg9bnAuY29uY2F0ZW5hdGUoW3hfY3JpdF9wb3MsIFs0LCAxLjk2XV0pLCB5PW5wLmNvbmNhdGVuYXRlKFt5X2NyaXRfcG9zLCBbMCwgMF1dKSwgZmlsbD0ndG9zZWxmJywgZmlsbGNvbG9yPScjOTkxQjFCJywgbmFtZT0nUkMgKEFscGhhLzIpJykpOyBmaWcuYWRkX3ZsaW5lKHg9Mi4wLCBsaW5lX2Rhc2g9J2Rhc2gnLCBsaW5lX2NvbG9yPScjMUUyOTNCJywgYW5ub3RhdGlvbl90ZXh0PSdaX2NhbGMgPSAyLjAwJyk7IGZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5EaXN0cmlidWnDp8OjbyBOb3JtYWwgZSBSZWdpw6NvIENyw610aWNhPC9iPicsIHhheGlzX3RpdGxlPSdaJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIHRlc3RlIGRlIGhpcMOzdGVzZXMgcGFyYW3DqXRyaWNvLCBvIHBlc3F1aXNhZG9yIGRlZmluZSBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSA9IDAuMDEkLiBRdWFsIGRhcyBhbHRlcm5hdGl2YXMgZGVzY3JldmUgY29ycmV0YW1lbnRlIG8gc2lnbmlmaWNhZG8gZXN0YXTDrXN0aWNvIGRlc3RhIGRlY2lzw6NvIG5hIGVzdHJ1dHVyYSBsw7NnaWNhIGRvIHRlc3RlPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBwcm9iYWJpbGlkYWRlIGRlIHF1ZSAkSF8wJCBzZWphIHZlcmRhZGVpcmEgw6kgZGUgYXBlbmFzIDElLiIsICJCIjogIk8gcGVzcXVpc2Fkb3IgYWNlaXRhIHVtIHJpc2NvIGRlIDElIGRlIHJlamVpdGFyICRIXzAkIHF1YW5kbyBlc3RhIMOpLCBuYSB2ZXJkYWRlLCB2ZXJkYWRlaXJhIChFcnJvIFRpcG8gSSkuIiwgIkMiOiAiTyBwb2RlciBkbyB0ZXN0ZSDDqSBnYXJhbnRpZG8gY29tbyBzZW5kbyBkZSA5OSUsIGluZGVwZW5kZW50ZSBkbyB0YW1hbmhvIGRhIGFtb3N0cmEuIiwgIkQiOiAiQSBwcm9iYWJpbGlkYWRlIGRlIGNvbWV0ZXIgdW0gRXJybyBUaXBvIElJIMOpIGV4YXRhbWVudGUgMC4wMS4iLCAiRSI6ICJPIHZhbG9yLXAgc2Vyw6Egc2VtcHJlIG1haW9yIHF1ZSAwLjAxIHNlICRIXzAkIGZvciByZWplaXRhZGEuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJPIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAoJFxcYWxwaGEkKSDDqSB1bWEgaW1wb3Npw6fDo28gZG8gcGVzcXVpc2Fkb3Igc29icmUgbyByaXNjbyBkZSBmYWxzbyBwb3NpdGl2byBhbnRlcyBkZSBvbGhhciBvcyBkYWRvcy4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIk8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCByZXByZXNlbnRhIGEgcHJvYmFiaWxpZGFkZSBkZSBjb21ldGVyIG8gRXJybyBUaXBvIEkgKHJlamVpdGFyIHVtYSBoaXDDs3Rlc2UgbnVsYSB2ZXJkYWRlaXJhKS4gQSBhbHRlcm5hdGl2YSAoQSkgw6kgdW0gZXJybyBjb211bSBkZSBpbnRlcnByZXRhw6fDo28gZG8gcC12YWxvcjsgKEMpIGVzdMOhIGluY29ycmV0YSBwb2lzIG8gcG9kZXIgZGVwZW5kZSBkZSAkbiQgZSBkbyBkZXN2aW87IChEKSBjb25mdW5kZSAkXFxhbHBoYSQgY29tICRcXGJldGEkOyAoRSkgZXN0w6EgZXJyYWRhIHBvaXMsIHBhcmEgcmVqZWl0YXIgJEhfMCQsIG8gcC12YWxvciBkZXZlIHNlciAkXFxsZXEgXFxhbHBoYSQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbWEgaW5kw7pzdHJpYSBkZSBiZWJpZGFzIHV0aWxpemEgbcOhcXVpbmFzIGF1dG9tw6F0aWNhcyBwYXJhIGVudmFzZSBkZSByZWZyaWdlcmFudGVzLCBjb25maWd1cmFkYXMgcGFyYSB1bWEgbcOpZGlhIHBvcHVsYWNpb25hbCBkZSAkXFxtdSA9IDUwMCQgbWwuIFBvciBxdWVzdMO1ZXMgZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlIGUgaGlzdMOzcmljbyBkZSBtYW51dGVuw6fDo28sIG8gZGVzdmlvIHBhZHLDo28gZG8gcHJvY2Vzc28gw6kgcmlnb3Jvc2FtZW50ZSBjb25oZWNpZG8gY29tbyAkXFxzaWdtYSA9IDEwJCBtbCwgZSBhIGRpc3RyaWJ1acOnw6NvIGRvIHZvbHVtZSBkZSBlbmNoaW1lbnRvIHNlZ3VlIHVtYSBub3JtYWwuIFBhcmEgbW9uaXRvcmFyIG8gcHJvY2Vzc28sIHVtIGVuZ2VuaGVpcm8gY29sZXRhIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgZGUgJG4gPSAyNSQgZ2FycmFmYXMuIFF1YWwgw6kgbyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhLCAkXFxzaWdtYV97XFxiYXJ7WH19JCwgcXVlIGRldmUgc2VyIHV0aWxpemFkbyBwYXJhIGNhbGN1bGFyIGEgZXN0YXTDrXN0aWNhICRaX3tcXHRleHR7Y2FsY319JCBlIGF2YWxpYXIgYSBjb25mb3JtaWRhZGUgZGEgcHJvZHXDp8Ojbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjAsNCBtbCIsICJCIjogIjIsMCBtbCIsICJDIjogIjIsNSBtbCIsICJEIjogIjEwLDAgbWwiLCAiRSI6ICI1MCwwIG1sIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJPIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgcmVwcmVzZW50YSBhIGRpc3BlcnPDo28gZGFzIG3DqWRpYXMgYW1vc3RyYWlzIGVtIHRvcm5vIGRhIG3DqWRpYSBwb3B1bGFjaW9uYWwgcmVhbDsgbGVtYnJlLXNlIGRhIGbDs3JtdWxhICRcXGZyYWN7XFxzaWdtYX17XFxzcXJ0e259fSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJPIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgw6kgZGFkbyBwZWxhIHJlbGHDp8OjbyBlbnRyZSBvIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCBlIGEgcmFpeiBxdWFkcmFkYSBkbyB0YW1hbmhvIGRhIGFtb3N0cmE6ICRcXHNpZ21hX3tcXGJhcntYfX0gPSBcXGZyYWN7XFxzaWdtYX17XFxzcXJ0e259fSQuIFN1YnN0aXR1aW5kbyBvcyB2YWxvcmVzLCB0ZW1vcyAkXFxzaWdtYV97XFxiYXJ7WH19ID0gXFxmcmFjezEwfXtcXHNxcnR7MjV9fSA9IFxcZnJhY3sxMH17NX0gPSAyLDAkIG1sLiBBIGFsdGVybmF0aXZhIEEgb2NvcnJlIHNlIG8gYWx1bm8gZXNxdWVjZXIgYSByYWl6IHF1YWRyYWRhIG91IGRpdmlkaXIgJFxcc2lnbWEkIHBvciAkbiQgZGlyZXRhbWVudGUuIEEgYWx0ZXJuYXRpdmEgQyByZXN1bHRhIGRlIGRpdmlkaXIgJFxcc2lnbWEkIHBvciA0LiBBIGFsdGVybmF0aXZhIEQgw6kgbyBwcsOzcHJpbyBkZXN2aW8gcGFkcsOjbywgaWdub3JhbmRvIGEgYW1vc3RyYSwgZSBhIEUgw6kgdW0gZXJybyBkZSBlc2NhbGEgZ3Jvc3NlaXJvLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM0MCJ9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSB0ZXN0ZSBkZSBoaXDDs3Rlc2VzIGJpbGF0ZXJhbCBwYXJhIGEgbcOpZGlhIHBvcHVsYWNpb25hbCwgY29tIHZhcmnDom5jaWEgY29uaGVjaWRhLCBhIHJlZ2nDo28gZGUgcmVqZWnDp8OjbyAoJFJDJCkgcGFyYSB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgZGUgJFxcYWxwaGEgPSAwLDA1JCBmb2kgZGVmaW5pZGEuIFNlIG8gdmFsb3IgZGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlIGNhbGN1bGFkYSDDqSAkWl97XFx0ZXh0e2NhbGN9fSA9IC0yLDEwJCwgcXVhbCBkYXMgY29uY2x1c8O1ZXMgYWJhaXhvIGVzdMOhIGNvcnJldGEgc29icmUgYSBkZWNpc8OjbyBlc3RhdMOtc3RpY2E/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJDb21vICR8Wl97XFx0ZXh0e2NhbGN9fXwgPCAxLDk2JCwgbsOjbyByZWplaXRhbW9zICRIXzAkLiIsICJCIjogIkNvbW8gJHxaX3tcXHRleHR7Y2FsY319fCA+IDEsOTYkLCByZWplaXRhbW9zICRIXzAkIGFvIG7DrXZlbCBkZSA1JS4iLCAiQyI6ICJDb21vICRaX3tcXHRleHR7Y2FsY319JCDDqSBuZWdhdGl2bywgYSBoaXDDs3Rlc2UgbnVsYSDDqSBhY2VpdGEgYXV0b21hdGljYW1lbnRlLiIsICJEIjogIk8gdGVzdGUgw6kgaW5jb25jbHVzaXZvLCBwb2lzIG5lY2Vzc2l0YXLDrWFtb3MgZG8gcC12YWxvciBleGF0byBwYXJhIHRvbWFyIHF1YWxxdWVyIGRlY2lzw6NvLiIsICJFIjogIlJlamVpdGFtb3MgJEhfMCQgYXBlbmFzIHNlICRaX3tcXHRleHR7Y2FsY319JCBmb3IgbWFpb3IgcXVlIDIsNTguIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJFbSB1bSB0ZXN0ZSBiaWxhdGVyYWwgY29tICRcXGFscGhhID0gMCwwNSQsIG9zIHZhbG9yZXMgY3LDrXRpY29zIGRhIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBwYWRyw6NvIHPDo28gJFxccG0gMSw5NiQuIENvbXBhcmUgbyB2YWxvciBhYnNvbHV0byBkYSBlc3RhdMOtc3RpY2EgY29tIGVzdGUgbGltaWFyLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUGFyYSB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgZGUgJFxcYWxwaGEgPSAwLDA1JCBlbSB1bSB0ZXN0ZSBiaWxhdGVyYWwgKCRIXzE6IFxcbXUgXFxuZXEgXFxtdV8wJCksIGEgcmVnacOjbyBkZSByZWplacOnw6NvIHNpdHVhLXNlIG5hcyBjYXVkYXMgZGEgZGlzdHJpYnVpw6fDo28gJE4oMCwxKSQsIGRlbGltaXRhZGFzIHBlbG9zIHZhbG9yZXMgY3LDrXRpY29zICRcXHBtIFpfe1xcdGV4dHtjcml0fX0gPSBcXHBtIDEsOTYkLiBDb21vICR8Wl97XFx0ZXh0e2NhbGN9fXwgPSB8LTIsMTB8ID0gMiwxMCQsIHF1ZSDDqSBzdXBlcmlvciBhICQxLDk2JCwgbyB2YWxvciBhbW9zdHJhbCBjYWkgbmEgcmVnacOjbyBkZSByZWplacOnw6NvLCBsZXZhbmRvIMOgIHJlamVpw6fDo28gZGUgJEhfMCQuIEVycm9zIGNvbXVucyBpbmNsdWVtIGNvbmZ1bmRpciBvcyBsaW1pdGVzIGNyw610aWNvcyBkbyB0ZXN0ZSBiaWxhdGVyYWwgY29tIG9zIGRvIHVuaWxhdGVyYWwsIG91IGVzcXVlY2VyIG8gbcOzZHVsbyBhbyBjb21wYXJhci4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAyMDApXG55ID0gc3RhdHMubm9ybS5wZGYoeClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbW9kZT0nbGluZXMnLCBuYW1lPSdOKDAsMSknLCBsaW5lPWRpY3QoY29sb3I9JyMwNjRFM0InKSkpXG4jIFJlZ2nDo28gQ3LDrXRpY2FcbmZpZy5hZGRfdnJlY3QoeDA9MS45NiwgeDE9NCwgZmlsbGNvbG9yPScjOTkxQjFCJywgb3BhY2l0eT0wLjMsIGxpbmVfd2lkdGg9MClcbmZpZy5hZGRfdnJlY3QoeDA9LTQsIHgxPS0xLjk2LCBmaWxsY29sb3I9JyM5OTFCMUInLCBvcGFjaXR5PTAuMywgbGluZV93aWR0aD0wKVxuZmlnLmFkZF92bGluZSh4PS0yLjEwLCBsaW5lPWRpY3QoY29sb3I9JyM5OTFCMUInLCBkYXNoPSdkYXNoJyksIG5hbWU9J1pfY2FsYycpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+RGlzdHJpYnVpw6fDo28gTm9ybWFsIGUgUmVnacOjbyBDcsOtdGljYSAoYWxmYT0wLjA1KTwvYj4nLCB4YXhpc190aXRsZT0nWicsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNDAifSwgeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgZGUgcHJvY2Vzc2FtZW50byBkZSBsZWl0ZSBhdXRvbWF0aXphZGEgY2FsaWJyYSBzdWFzIG3DoXF1aW5hcyBwYXJhIHF1ZSBvIHZvbHVtZSBtw6lkaW8gZGUgZW52YXNlIHNlamEgZGUgJDUwMCQgbWwsIGNvbSB1bSBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgJFxcc2lnbWEgPSA1JCBtbC4gQXDDs3MgdW1hIG1hbnV0ZW7Dp8OjbyBjb3JyZXRpdmEsIG8gZW5nZW5oZWlybyBkZSBxdWFsaWRhZGUgc3VzcGVpdGEgcXVlIGEgbcOhcXVpbmEgZXN0ZWphIG9wZXJhbmRvIGNvbSB1bSBkZXN2aW8gcGFyYSBtYWlzLCByZXN1bHRhbmRvIGVtIGRlc3BlcmTDrWNpbyBkZSBwcm9kdXRvLiBQYXJhIHZlcmlmaWNhciBlc3NhIHN1c3BlaXRhLCBlbGUgY29sZXRhIHVtYSBhbW9zdHJhIGRlICRuPTEwMCQgZ2FycmFmYXMgZSBvYnTDqW0gdW1hIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0gPSA1MDEsMiQgbWwuIENvbnNpZGVyYW5kbyB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgZGUgJFxcYWxwaGEgPSAwLDA1JCwgcXVhbCDDqSBhIGZvcm11bGHDp8OjbyBjb3JyZXRhIGRhcyBoaXDDs3Rlc2VzIGUgYSBjb25jbHVzw6NvIGVzdGF0w61zdGljYSBhZGVxdWFkYSBwYXJhIGVzc2UgdGVzdGUgZGUgaGlww7N0ZXNlPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJEhfMDogXFxtdSA9IDUwMCQgdnMgJEhfMTogXFxtdSBcXG5lcSA1MDAkLiBDb21vICRaX3tcXHRleHR7Y2FsY319ID0gMiw0MCA+IFpfezAsOTc1fSA9IDEsOTYkLCByZWplaXRhbW9zICRIXzAkLiIsICJCIjogIiRIXzA6IFxcbXUgXFxsZSA1MDAkIHZzICRIXzE6IFxcbXUgPiA1MDAkLiBDb21vICRaX3tcXHRleHR7Y2FsY319ID0gMiw0MCA+IFpfezAsOTV9ID0gMSw2NDUkLCByZWplaXRhbW9zICRIXzAkLiIsICJDIjogIiRIXzA6IFxcbXUgXFxnZSA1MDAkIHZzICRIXzE6IFxcbXUgPCA1MDAkLiBDb21vICRaX3tcXHRleHR7Y2FsY319ID0gMiw0MCA+IFpfezAsMDV9ID0gLTEsNjQ1JCwgbsOjbyByZWplaXRhbW9zICRIXzAkLiIsICJEIjogIiRIXzA6IFxcbXUgXFxsZSA1MDAkIHZzICRIXzE6IFxcbXUgPiA1MDAkLiBDb21vICRaX3tcXHRleHR7Y2FsY319ID0gMCwyNCA8IFpfezAsOTV9ID0gMSw2NDUkLCBuw6NvIHJlamVpdGFtb3MgJEhfMCQuIiwgIkUiOiAiJEhfMDogXFxtdSA9IDUwMCQgdnMgJEhfMTogXFxtdSBcXG5lcSA1MDAkLiBDb21vICRaX3tcXHRleHR7Y2FsY319ID0gMCwyNCA8IFpfezAsOTc1fSA9IDEsOTYkLCBuw6NvIHJlamVpdGFtb3MgJEhfMCQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJPIGVuZ2VuaGVpcm8gc3VzcGVpdGEgZXNwZWNpZmljYW1lbnRlIGRlIHVtIGRlc3ZpbyBwYXJhICdtYWlzJy4gSXNzbyBkaXRhIG8gc2VudGlkbyBkYSBkZXNpZ3VhbGRhZGUgbmEgaGlww7N0ZXNlIGFsdGVybmF0aXZhLCBjb25maWd1cmFuZG8gdW0gdGVzdGUgdW5pbGF0ZXJhbC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkNhbGN1bGFtb3MgYSBlc3RhdMOtc3RpY2EgJFpfe1xcdGV4dHtjYWxjfX0kOiAkJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11XzB9e1xcc2lnbWEgLyBcXHNxcnR7bn19ID0gXFxmcmFjezUwMSwyIC0gNTAwfXs1IC8gXFxzcXJ0ezEwMH19ID0gXFxmcmFjezEsMn17MCw1fSA9IDIsNDAkJCBDb21vIGEgc3VzcGVpdGEgw6kgZGUgYXVtZW50bywgdXRpbGl6YW1vcyB1bSB0ZXN0ZSB1bmlsYXRlcmFsIHN1cGVyaW9yICgkSF8xOiBcXG11ID4gNTAwJCkuIE8gdmFsb3IgY3LDrXRpY28gcGFyYSAkXFxhbHBoYT0wLDA1JCDDqSAkWl97MCw5NX0gPSAxLDY0NSQuIENvbW8gJDIsNDAgPiAxLDY0NSQsIHJlamVpdGFtb3MgJEhfMCQuIEEgYWx0ZXJuYXRpdmEgQSBlc3TDoSBpbmNvcnJldGEgcG9pcyB1dGlsaXphIHVtIHRlc3RlIGJpbGF0ZXJhbCBkZXNuZWNlc3PDoXJpbzsgYSBDIGludmVydGUgYSBkaXJlw6fDo28gZGEgaGlww7N0ZXNlOyBhIEQgdXRpbGl6YSBlcnJvIGRlIGPDoWxjdWxvIG5hIGVzdGF0w61zdGljYSBaOyBlIGEgRSBmYWxoYSBhbyB1c2FyIG8gdGVzdGUgYmlsYXRlcmFsLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTQsIDQsIDIwMClcbnkgPSBzdGF0cy5ub3JtLnBkZih4LCAwLCAxKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBuYW1lPSdEaXN0cmlidWnDp8OjbyBOKDAsMSknLCBsaW5lPWRpY3QoY29sb3I9JyMwNjRFM0InLCB3aWR0aD0yKSkpXG56X2NyaXQgPSAxLjY0NVxueF9maWxsID0gbnAubGluc3BhY2Uoel9jcml0LCA0LCAxMDApXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1ucC5jb25jYXRlbmF0ZSgoW3pfY3JpdF0sIHhfZmlsbCwgWzRdKSksIHk9bnAuY29uY2F0ZW5hdGUoKFswXSwgc3RhdHMubm9ybS5wZGYoeF9maWxsLCAwLCAxKSwgWzBdKSksIGZpbGw9J3Rvc2VsZicsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG5hbWU9J1JDIChBbHBoYT0wLjA1KScsIGxpbmU9ZGljdChjb2xvcj0ncmdiYSgwLDAsMCwwKScpKSlcbmZpZy5hZGRfdmxpbmUoeD0yLjQwLCBsaW5lPWRpY3QoY29sb3I9JyMxRTI5M0InLCBkYXNoPSdkYXNoJyksIG5hbWU9J1pfY2FsYz0yLjQwJylcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdUZXN0ZSBVbmlsYXRlcmFsIFN1cGVyaW9yIChSZWplacOnw6NvKScsIHhheGlzX3RpdGxlPSdaJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBjbMOtbmljbywgYXZhbGlhLXNlIHNlIHVtIG5vdm8gZsOhcm1hY28gYWx0ZXJhIGEgcHJlc3PDo28gYXJ0ZXJpYWwgc2lzdMOzbGljYSBtw6lkaWEgZGUgcGFjaWVudGVzLiBTYWJlLXNlIHF1ZSBhIHBvcHVsYcOnw6NvIHBvc3N1aSBkZXN2aW8gcGFkcsOjbyAkXFxzaWdtYSA9IDEwJCBtbUhnLiBBIG3DqWRpYSBwb3B1bGFjaW9uYWwgc29iIGNvbnRyb2xlIMOpICRcXG11XzAgPSAxMjAkIG1tSGcuIFVtYSBhbW9zdHJhIGRlICRuPTY0JCBwYWNpZW50ZXMgYXByZXNlbnRhIG3DqWRpYSAkXFxiYXJ7WH0gPSAxMjIsNSQgbW1IZy4gQW8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGRlICRcXGFscGhhID0gMCwwNSQsIGF2YWxpZSBhIHZhbGlkYWRlIGRvIHRlc3RlIGVzdGF0w61zdGljbyBlIGEgdG9tYWRhIGRlIGRlY2lzw6NvLiIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiVGVzdGUgYmlsYXRlcmFsOiAkWl97XFx0ZXh0e2NhbGN9fSA9IDIsMCQsIHJlamVpdGFtb3MgJEhfMCQgcG9pcyAkMiwwID4gMSw5NiQuIiwgIkIiOiAiVGVzdGUgYmlsYXRlcmFsOiAkWl97XFx0ZXh0e2NhbGN9fSA9IDIsMCQsIG7Do28gcmVqZWl0YW1vcyAkSF8wJCBwb2lzICQyLDAgPCAyLDU3NiQuIiwgIkMiOiAiVGVzdGUgdW5pbGF0ZXJhbCBzdXBlcmlvcjogJFpfe1xcdGV4dHtjYWxjfX0gPSAyLDAkLCByZWplaXRhbW9zICRIXzAkIHBvaXMgJDIsMCA+IDEsNjQ1JC4iLCAiRCI6ICJUZXN0ZSB1bmlsYXRlcmFsIGluZmVyaW9yOiAkWl97XFx0ZXh0e2NhbGN9fSA9IDIsMCQsIHJlamVpdGFtb3MgJEhfMCQgcG9pcyAkMiwwIDwgLTEsNjQ1JCDDqSBmYWxzby4iLCAiRSI6ICJUZXN0ZSBiaWxhdGVyYWw6ICRaX3tcXHRleHR7Y2FsY319ID0gMCwyJCwgbsOjbyByZWplaXRhbW9zICRIXzAkIHBvaXMgJDAsMiA8IDEsOTYkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTyBlbnVuY2lhZG8gZGl6IHF1ZSBvIGbDoXJtYWNvICdhbHRlcmEnIGEgcHJlc3PDo28sIHNlbSBlc3BlY2lmaWNhciBzZSBhdW1lbnRhIG91IGRpbWludWkuIFF1YWwgbyB0aXBvIGRlIHRlc3RlIGluZGljYWRvPyIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiJCRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFjezEyMiw1IC0gMTIwfXsxMCAvIFxcc3FydHs2NH19ID0gXFxmcmFjezIsNX17MTAgLyA4fSA9IFxcZnJhY3syLDV9ezEsMjV9ID0gMiwwJCQuIENvbW8gYSBxdWVzdMOjbyBidXNjYSAnYWx0ZXJhw6fDo28nLCBvIHRlc3RlIMOpIGJpbGF0ZXJhbC4gUGFyYSAkXFxhbHBoYT0wLDA1JCwgbyB2YWxvciBjcsOtdGljbyDDqSAkWl97XFx0ZXh0e2NyaXR9fSA9IFxccG0gMSw5NiQuIENvbW8gJHxaX3tcXHRleHR7Y2FsY319fCA9IDIsMCA+IDEsOTYkLCByZWplaXRhbW9zICRIXzAkLiBBcyBkZW1haXMgYWx0ZXJuYXRpdmFzIGZhbGhhbSBhbyBlc2NvbGhlciBvIHRlc3RlIHVuaWxhdGVyYWwgb3UgZXJyYXIgbyBjw6FsY3Vsby9jcml0w6lyaW8gZGUgcmVqZWnDp8Ojby4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAyMDApXG55ID0gc3RhdHMubm9ybS5wZGYoeCwgMCwgMSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbmFtZT0nTigwLDEpJywgbGluZT1kaWN0KGNvbG9yPScjMDY0RTNCJykpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9bnAubGluc3BhY2UoLTQsIC0xLjk2LCA1MCksIHk9c3RhdHMubm9ybS5wZGYobnAubGluc3BhY2UoLTQsIC0xLjk2LCA1MCksIDAsIDEpLCBmaWxsPSd0b3plcm95JywgZmlsbGNvbG9yPScjOTkxQjFCJywgbmFtZT0nUkMgKEVzcSknKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PW5wLmxpbnNwYWNlKDEuOTYsIDQsIDUwKSwgeT1zdGF0cy5ub3JtLnBkZihucC5saW5zcGFjZSgxLjk2LCA0LCA1MCksIDAsIDEpLCBmaWxsPSd0b3plcm95JywgZmlsbGNvbG9yPScjOTkxQjFCJywgbmFtZT0nUkMgKERpciknKSlcbmZpZy5hZGRfdmxpbmUoeD0yLjAsIGxpbmU9ZGljdChjb2xvcj0nIzFFMjkzQicsIGRhc2g9J2Rhc2gnKSwgbmFtZT0nWl9jYWxjPTIuMCcpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nVGVzdGUgQmlsYXRlcmFsIChaPTIuMCknLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbWEgaW5kw7pzdHJpYSBhdXRvbW90aXZhIHV0aWxpemEgdW0gcHJvY2Vzc28gZGUgc29sZGFnZW0gcm9ib3RpemFkYSBjdWphIHJlc2lzdMOqbmNpYSDDoCB0cmHDp8OjbyBkb3MgY29tcG9uZW50ZXMgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCAkTihcXG11LCBcXHNpZ21hXjIpJCwgY29tIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCBjb25oZWNpZG8gZGUgJFxcc2lnbWEgPSA4JCBrZ2YuIEhpc3RvcmljYW1lbnRlLCBhIG3DoXF1aW5hIGZvaSByZWd1bGFkYSBwYXJhIHByb2R1emlyIGNvbXBvbmVudGVzIGNvbSByZXNpc3TDqm5jaWEgbcOpZGlhIGRlICRcXG11XzAgPSAyNTAkIGtnZi4gRHVyYW50ZSB1bWEgaW5zcGXDp8OjbyBkZSBxdWFsaWRhZGUsIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgZGUgJG4gPSA2NCQgY29tcG9uZW50ZXMgYXByZXNlbnRvdSB1bWEgcmVzaXN0w6puY2lhIG3DqWRpYSBkZSAkXFxiYXJ7WH0gPSAyNDckIGtnZi4gQ29uc2lkZXJhbmRvIHVtIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBkZSAkXFxhbHBoYSA9IDAsMDUkIHBhcmEgdW0gdGVzdGUgYmlsYXRlcmFsLCBxdWFsIMOpIGEgY29uY2x1c8OjbyBlc3RhdMOtc3RpY2Egc29icmUgYSBjYWxpYnJhw6fDo28gZGEgbcOhcXVpbmE/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJSZWplaXRhLXNlIEgwLCBwb2lzIHxaX2NhbGN8ID0gMywwMCA+IFpfY3JpdCA9IDEsOTYuIiwgIkIiOiAiTsOjbyBzZSByZWplaXRhIEgwLCBwb2lzIHxaX2NhbGN8ID0gMSw1MCA8IFpfY3JpdCA9IDEsOTYuIiwgIkMiOiAiTsOjbyBzZSByZWplaXRhIEgwLCBwb2lzIHxaX2NhbGN8ID0gMywwMCA8IFpfY3JpdCA9IDEsOTYuIiwgIkQiOiAiUmVqZWl0YS1zZSBIMCwgcG9pcyB8Wl9jYWxjfCA9IDEsNTAgPiBaX2NyaXQgPSAxLDk2LiIsICJFIjogIk8gdGVzdGUgw6kgaW5jb25jbHVzaXZvLCBwb2lzIG8gdGFtYW5obyBkYSBhbW9zdHJhIG49NjQgw6kgaW5zdWZpY2llbnRlIHBhcmEgYSBub3JtYWxpZGFkZS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkNhbGN1bGUgcHJpbWVpcm8gbyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhOiBFUChYX2JhcnJhKSA9IFxcc2lnbWEgLyBcXHNxcnQobikuIEVtIHNlZ3VpZGEsIGRldGVybWluZSBhIGVzdGF0w61zdGljYSBaX2NhbGMgZSBjb21wYXJlLWEgY29tIG8gdmFsb3IgY3LDrXRpY28gZGEgbm9ybWFsIHBhZHLDo28gcGFyYSBcXGFscGhhID0gMCwwNS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlRlbW9zIEgwOiBcXG11ID0gMjUwIHZzIEgxOiBcXG11ICE9IDI1MC4gTyBlcnJvIHBhZHLDo28gw6kgRVAoWF9iYXJyYSkgPSA4IC8gXFxzcXJ0KDY0KSA9IDggLyA4ID0gMS4gQSBlc3RhdMOtc3RpY2EgWl9jYWxjID0gKDI0NyAtIDI1MCkgLyAxID0gLTMgLyAxID0gLTMuIEVtIHZhbG9yIGFic29sdXRvLCB8Wl9jYWxjfCA9IDMuIE8gdmFsb3IgY3LDrXRpY28gWl9jcml0IHBhcmEgXFxhbHBoYSA9IDAsMDUgKGJpbGF0ZXJhbCkgw6kgMSw5Ni4gRXJybyBjb211bTogYWxndW5zIGFsdW5vcyBlc3F1ZWNlbSBkZSBkaXZpZGlyIHBlbG8gZXJybyBwYWRyw6NvIChcXHNpZ21hL3JhaXogZGUgbikgb3UgY29tcGFyYW0gaW5jb3JyZXRhbWVudGUgY29tIG8gdmFsb3IgY3LDrXRpY28uIENvbW8gfC0zfCA+IDEsOTYsIGEgY29uY2x1c8OjbyBjb3JyZXRhIHNlcmlhIHJlamVpdGFyIEgwLiAqTm90YSBkZSBjb3JyZcOnw6NvKjogQW5hbGlzYW5kbyBub3ZhbWVudGUgb3MgZGFkb3MsIHxaX2NhbGN8ID0gMyDDqSBtYWlvciBxdWUgMSw5NiwgbG9nbyBhIGFsdGVybmF0aXZhIGNvcnJldGEgw6kgYSBBLiBBanVzdGFuZG8gbyBnYWJhcml0bzogQSBhbHRlcm5hdGl2YSBjb3JyZXRhIMOpIEEuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgtNCwgNCwgMTAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9J04oMCwxKScsIGxpbmU9ZGljdChjb2xvcj0nIzA2NEUzQicpKSlcbmZpZy5hZGRfc2hhcGUodHlwZT0nbGluZScsIHgwPS0xLjk2LCB5MD0wLCB4MT0tMS45NiwgeTE9MC40LCBsaW5lPWRpY3QoY29sb3I9JyM5OTFCMUInLCBkYXNoPSdkYXNoJykpXG5maWcuYWRkX3NoYXBlKHR5cGU9J2xpbmUnLCB4MD0xLjk2LCB5MD0wLCB4MT0xLjk2LCB5MT0wLjQsIGxpbmU9ZGljdChjb2xvcj0nIzk5MUIxQicsIGRhc2g9J2Rhc2gnKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdEaXN0cmlidWnDp8OjbyBOb3JtYWwgUGFkcsOjbyBlIFJlZ2nDtWVzIENyw610aWNhcycsIHhheGlzX3RpdGxlPSdaJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIifSwgeyJlbnVuY2lhZG8iOiAiVW0gYW5hbGlzdGEgZGUgcmlzY28gZGVzZWphIHRlc3RhciBzZSBvIHJlbmRpbWVudG8gbcOpZGlvIGRpw6FyaW8gZGUgdW0gZnVuZG8gZGUgaW52ZXN0aW1lbnRvLCBxdWUgaGlzdG9yaWNhbWVudGUgb3BlcmEgY29tIG3DqWRpYSAkXFxtdV8wID0gMCw1XFwlJCBlIGRlc3ZpbyBwYWRyw6NvICRcXHNpZ21hID0gMCwyXFwlJCwgc29mcmV1IGFsdGVyYcOnw6NvLiBFbGUgY29sZXRhIHVtYSBhbW9zdHJhIGRlICRuID0gMjUkIGRpYXMgZSBlbmNvbnRyYSAkXFxiYXJ7WH0gPSAwLDQ1XFwlJC4gQW8gdGVzdGFyICRIXzA6IFxcbXUgPSAwLDUkIGNvbnRyYSAkSF8xOiBcXG11IFxcbmVxIDAsNSQgY29tICRcXGFscGhhID0gMCwxMCQsIG8gYW5hbGlzdGEgY2FsY3VsYSBhIGVzdGF0w61zdGljYSBkZSB0ZXN0ZS4gUXVhbCBvIHZhbG9yIGRlICRaX3tcXHRleHR7Y2FsY319JCBlIGEgZGVjaXPDo28gY29ycmV0YT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIlpfY2FsYyA9IC0xLDI1OyBOw6NvIHJlamVpdGEgSDAuIiwgIkIiOiAiWl9jYWxjID0gLTAsMjU7IE7Do28gcmVqZWl0YSBIMC4iLCAiQyI6ICJaX2NhbGMgPSAtMSwyNTsgUmVqZWl0YSBIMC4iLCAiRCI6ICJaX2NhbGMgPSAtNiwyNTsgUmVqZWl0YSBIMC4iLCAiRSI6ICJaX2NhbGMgPSAxLDI1OyBOw6NvIHJlamVpdGEgSDAuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIFpfY2FsYyA9IChYX2JhcnJhIC0gXFxtdTApIC8gKFxcc2lnbWEgLyBcXHNxcnQobikpLiBPIGVycm8gcGFkcsOjbyDDqSAwLDIgLyA1ID0gMCwwNC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkPDoWxjdWxvOiBaX2NhbGMgPSAoMCw0NSAtIDAsNSkgLyAoMCwyIC8gXFxzcXJ0KDI1KSkgPSAtMCwwNSAvICgwLDIgLyA1KSA9IC0wLDA1IC8gMCwwNCA9IC0xLDI1LiBQYXJhIFxcYWxwaGEgPSAwLDEwIChiaWxhdGVyYWwpLCBaX2NyaXQgPSAxLDY0NS4gQ29tbyB8LTEsMjV8IDwgMSw2NDUsIG7Do28gcmVqZWl0YW1vcyBIMC4gRXJyb3MgY29tdW5zOiBjb25mdW5kaXIgbyB2YWxvciBkZSBcXGFscGhhIHBhcmEgdGVzdGVzIGJpbGF0ZXJhaXMgKHVzYW5kbyAwLDA1IGVtIHZleiBkZSAwLDEwKSBvdSBlcnJhciBhIHJhaXogcXVhZHJhZGEgZG8gdGFtYW5obyBhbW9zdHJhbC4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH1dLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbeyJlbnVuY2lhZG8iOiAiVW1hIGVtcHJlc2EgZGUgXFxsb2fDrXN0aWNhIG1vbml0b3JhIG8gdGVtcG8gbcOpZGlvIGRlIGVudHJlZ2EgZGUgc2V1cyBwcm9kdXRvcywgcXVlIGhpc3RvcmljYW1lbnRlIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgY29tIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCAkXFxzaWdtYSA9IDEyJCBtaW51dG9zLiBPIG9iamV0aXZvIGF0dWFsIMOpIHZlcmlmaWNhciBzZSBhIG3DqWRpYSBkZSBlbnRyZWdhIG11ZG91IGVtIHJlbGHDp8OjbyBhbyBwYWRyw6NvIGRlICRcXG11XzAgPSA0NSQgbWludXRvcy4gVW1hIGFtb3N0cmEgZGUgJG4gPSA2NCQgZW50cmVnYXMgcmVzdWx0b3UgZW0gdW1hIG3DqWRpYSBhbW9zdHJhbCBkZSAkXFxiYXJ7WH0gPSA0OCQgbWludXRvcy4gKGEpIEZvcm11bGUgYXMgaGlww7N0ZXNlcyAkSF8wJCBlICRIXzEkLiAoYikgQ2FsY3VsZSBhIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSAkWl97XHRleHR7Y2FsY319JCBwYXJhICRcXGFscGhhID0gMC4wNSQuIChjKSBBcHJlc2VudGUgYSBkZWNpc8OjbyBlc3RhdMOtc3RpY2EgZSBhIGNvbmNsdXPDo28gcHLDoXRpY2EuIiwgImRpY2EiOiAiQ29uc2lkZXJlIG8gdGVzdGUgYmlsYXRlcmFsLiBDYWxjdWxlIG8gZXJybyBwYWRyw6NvICRFUChcXGJhcntYfSkgPSBcXHNpZ21hIC8gXFxzcXJ0e259JCBwcmltZWlyby4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiKGEpICRIXzA6IFxcbXUgPSA0NSQgdmVyc3VzICRIXzE6IFxcbXUgXFxuZXEgNDUkLiIsICIoYikgJEVQKFxcYmFye1h9KSA9IDEyIC8gXFxzcXJ0ezY0fSA9IDEyIC8gOCA9IDEuNSQuIiwgIiRaX3tcdGV4dHtjYWxjfX0gPSAoNDggLSA0NSkgLyAxLjUgPSAzIC8gMS41ID0gMi4wMCQuIiwgIihjKSBQYXJhICRcXGFscGhhID0gMC4wNSQsICRaX3tcdGV4dHtjcml0fX0gPSAxLjk2JC4gQ29tbyAkfDIuMDB8ID4gMS45NiQsIHJlamVpdGFtb3MgJEhfMCQgYW8gbsOtdmVsIGRlIDUlLiBDb25jbHVpLXNlIHF1ZSBvIHRlbXBvIG3DqWRpbyBkZSBlbnRyZWdhIMOpIGVzdGF0aXN0aWNhbWVudGUgZGlmZXJlbnRlIGRlIDQ1IG1pbnV0b3MuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpOyB4ID0gbnAubGluc3BhY2UoLTQsIDQsIDEwMCk7IHkgPSAoMSAvIG5wLlxcc3FydCgyICogbnAuXFxwaSkpICogbnAuXFxleHAoLTAuNSAqIHgqKjIpOyBmaWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIGxpbmU9ZGljdChjb2xvcj0nIzA2NEUzQicsIHdpZHRoPTIpKSk7IGZpZy5hZGRfdmxpbmUoeD0xLjk2LCBsaW5lX2NvbG9yPScjOTkxQjFCJyk7IGZpZy5hZGRfdmxpbmUoeD0tMS45NiwgbGluZV9jb2xvcj0nIzk5MUIxQicpOyBmaWcuYWRkX3ZsaW5lKHg9Mi4wMCwgbGluZV9kYXNoPSdkYXNoJywgbGluZV9jb2xvcj0nIzFFMjkzQicpOyBmaWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+RXN0YXTDrXN0aWNhIGRlIFRlc3RlIHZzIFZhbG9yIENyw610aWNvPC9iPicsIHhheGlzX3RpdGxlPSdaJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAyLjB9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gZmFybWFjw6p1dGljbywgdW0gbm92byBjb21wb3N0byB2aXNhIHJlZHV6aXIgYSBwcmVzc8OjbyBhcnRlcmlhbC4gU2FiZS1zZSBxdWUgYSB2YXJpYWJpbGlkYWRlIGRhIHBvcHVsYcOnw6NvIMOpIGNvbnN0YW50ZSBjb20gJFxcc2lnbWEgPSAxMCQgbW1IZy4gQSBtw6lkaWEgZGUgcmVmZXLDqm5jaWEgw6kgJFxcbXVfMCA9IDEyMCQgbW1IZy4gQ29tIHVtYSBhbW9zdHJhIGRlICRuID0gMTAwJCBwYWNpZW50ZXMsIG9idGV2ZS1zZSAkXFxiYXJ7WH0gPSAxMTgkIG1tSGcuIEFvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSA9IDAuMDEkLCBkZXRlcm1pbmUgbyB2YWxvci1wIChhcHJveGltYWRvKSBkbyB0ZXN0ZSBlIGF2YWxpZSBzZSBow6EgZXZpZMOqbmNpYSBzaWduaWZpY2F0aXZhIHBhcmEgYWZpcm1hciBxdWUgYSBwcmVzc8OjbyBtw6lkaWEgw6kgZGlmZXJlbnRlIGRlIDEyMCBtbUhnLiIsICJkaWNhIjogIlVzZSBhIGbDs3JtdWxhICRaX3tcdGV4dHtjYWxjfX0gPSAoXFxiYXJ7WH0gLSBcXG11XzApIC8gKFxcc2lnbWEgLyBcXHNxcnR7bn0pJC4gTyBwLXZhbG9yIHBhcmEgdGVzdGUgYmlsYXRlcmFsIMOpICQyIFxcdGltZXMgUChaID4gfFpfe1x0ZXh0e2NhbGN9fXwpJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiJEVQKFxcYmFye1h9KSA9IDEwIC8gXFxzcXJ0ezEwMH0gPSAxLjAkLiIsICIkWl97XHRleHR7Y2FsY319ID0gKDExOCAtIDEyMCkgLyAxLjAgPSAtMi4wMCQuIiwgIiRwXFx0ZXh0ey12YWxvcn0gPSAyIFxcdGltZXMgUChaIDwgLTIuMDApIFxcYXBwcm94IDIgXFx0aW1lcyAwLjAyMjggPSAwLjA0NTYkLiIsICJDb21vICRwXFx0ZXh0ey12YWxvcn0gPSAwLjA0NTYgPiAwLjAxJCwgbsOjbyBow6EgZXZpZMOqbmNpYSBzdWZpY2llbnRlIHBhcmEgcmVqZWl0YXIgJEhfMCQgYW8gbsOtdmVsIGRlIDElLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4wNDU2fSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIGRvIHBvbnRvIGRlIHZpc3RhIGRhIGVzdHJ1dHVyYSBsw7NnaWNhIGRvIHRlc3RlIGRlIGhpcMOzdGVzZXMsIG8gcXVlIGFjb250ZWNlcmlhIGNvbSBhIGxhcmd1cmEgZGEgcmVnacOjbyBkZSByZWplacOnw6NvIHNlIHJlZHV6w61zc2Vtb3MgbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkIGRlIDAuMDUgcGFyYSAwLjAxIG1hbnRlbmRvIG8gbWVzbW8gdGFtYW5obyBkZSBhbW9zdHJhICRuJC4gQ29tbyBpc3NvIGFmZXRhIG8gRXJybyBUaXBvIElJPyIsICJkaWNhIjogIkEgcmVnacOjbyBkZSByZWplacOnw6NvIMOpIGRlZmluaWRhIHBlbG9zIHZhbG9yZXMgY3LDrXRpY29zIHF1ZSBkZXBlbmRlbSBkYSBjYXVkYSBkYSBkaXN0cmlidWnDp8Ojby4gTGVtYnJlLXNlIGRhIHJlbGHDp8OjbyBlbnRyZSAkXFxhbHBoYSQgZSAkXFxiZXRhJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSByZWR1w6fDo28gZGUgJFxcYWxwaGEkIGltcGxpY2EgZW0gdW0gY3JpdMOpcmlvIG1haXMgcmlnb3Jvc28gcGFyYSByZWplaXRhciAkSF8wJC4iLCAiTyB2YWxvciBjcsOtdGljbyAkWl97XFx0ZXh0e2NyaXR9fSQgcGFyYSAkXFxhbHBoYSA9IDAuMDUkIMOpIDEuOTYsIGVucXVhbnRvIHBhcmEgJFxcYWxwaGEgPSAwLjAxJCBlbGUgYXVtZW50YSBwYXJhIDIuNTguIiwgIkEgcmVnacOjbyBkZSByZWplacOnw6NvIHRvcm5hLXNlIG1haXMgZXN0cmVpdGEsIGRpbWludWluZG8gYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIGluY29ycmV0YW1lbnRlLiIsICJDb250dWRvLCBlc3NhIHJlZHXDp8OjbyBubyBlcnJvIHRpcG8gSSBhdW1lbnRhIG8gcmlzY28gZGUgY29tZXRlciB1bSBlcnJvIHRpcG8gSUkgKCRcXGJldGEkKSwgcG9pcyB0b3JuYSBvIHRlc3RlIG1haXMgY29uc2VydmFkb3IgZSBtZW5vcyBwcm9wZW5zbyBhIGRldGVjdGFyIGVmZWl0b3MgcmVhaXMuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIGFmaXJtYSBxdWUgYSB2aWRhIMO6dGlsIG3DqWRpYSBkZSBzZXVzIGNhcGFjaXRvcmVzIMOpIGRlIDIwMDAgaG9yYXMsIGNvbSB1bSBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgY29uaGVjaWRvIGRlICRcXHNpZ21hID0gMTUwJCBob3Jhcy4gVW0gZGVwYXJ0YW1lbnRvIGRlIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSB0ZXN0YSB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIGRlIDM2IGNhcGFjaXRvcmVzLCBvYnRlbmRvIHVtYSBtw6lkaWEgYW1vc3RyYWwgZGUgJFxcYmFye1h9ID0gMTk1MCQgaG9yYXMuIChhKSBGb3JtdWxlIGFzIGhpcMOzdGVzZXMgJEhfMCQgZSAkSF8xJCBwYXJhIHZlcmlmaWNhciBzZSBhIHZpZGEgbcOpZGlhIMOpIG1lbm9yIHF1ZSBhIGRlY2xhcmFkYS4gKGIpIENhbGN1bGUgYSBlc3RhdMOtc3RpY2EgJFpfe1x0ZXh0e2NhbGN9fSQuIChjKSBDb20gJFxcYWxwaGEgPSAwLDA1JCwgdG9tZSBhIGRlY2lzw6NvIGVzdGF0w61zdGljYSBlIGludGVycHJldGUgbyBsYXVkbyBwYXJhIGEgZ2VzdMOjby4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlLCBwYXJhIHRlc3RlcyB1bmlsYXRlcmFpcyDDoCBlc3F1ZXJkYSwgYSByZWdpw6NvIGRlIHJlamVpw6fDo28gZXN0w6EgYXBlbmFzIG5hIGNhdWRhIGluZmVyaW9yLiBVdGlsaXplICRaX3tcdGV4dHtjcml0fX0gPSAtMSw2NDUkIHBhcmEgJFxcYWxwaGEgPSAwLDA1JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gKGEpOiBIaXDDs3Rlc2VzOiAkSF8wOiBcXG11ID0gMjAwMCQgdnMgJEhfMTogXFxtdSA8IDIwMDAkLiIsICJQYXNzbyAoYik6IEPDoWxjdWxvIGRvIGVycm8gcGFkcsOjbzogJFxcc2lnbWFfe1xcYmFye1h9fSA9IFxcZnJhY3sxNTB9e1xcc3FydHszNn19ID0gXFxmcmFjezE1MH17Nn0gPSAyNSQuIiwgIlBhc3NvIChjKTogRXN0YXTDrXN0aWNhIGRlIHRlc3RlOiAkWl97XHRleHR7Y2FsY319ID0gXFxmcmFjezE5NTAgLSAyMDAwfXsyNX0gPSBcXGZyYWN7LTUwfXsyNX0gPSAtMiwwMCQuIiwgIlBhc3NvIChkKTogRGVjaXPDo286IENvbW8gJFpfe1x0ZXh0e2NhbGN9fSA9IC0yLDAwIDwgWl97XHRleHR7Y3JpdH19ID0gLTEsNjQ1JCwgcmVqZWl0YW1vcyAkSF8wJC4gSMOhIGV2aWTDqm5jaWFzIHNpZ25pZmljYXRpdmFzIGFvIG7DrXZlbCBkZSA1JSBkZSBxdWUgYSB2aWRhIG3DqWRpYSDDqSBpbmZlcmlvciBhIDIwMDAgaG9yYXMuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTQsIDQsIDIwMClcbnkgPSBzdGF0cy5ub3JtLnBkZih4KVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBtb2RlPSdsaW5lcycsIG5hbWU9J0RlbnNpZGFkZSBOKDAsMSknLCBsaW5lPWRpY3QoY29sb3I9JyMwNjRFM0InKSkpXG5maWcuYWRkX3ZyZWN0KHgwPS00LCB4MT0tMS42NDUsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTApXG5maWcuYWRkX3ZsaW5lKHg9LTIuMDAsIGxpbmU9ZGljdChjb2xvcj0nIzk5MUIxQicsIHdpZHRoPTMpLCBuYW1lPSdaX2NhbGMgPSAtMi4wMCcpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+VGVzdGUgVW5pbGF0ZXJhbCDDoCBFc3F1ZXJkYSAoYWxmYT0wLjA1KTwvYj4nKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogLTIuMH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBkZSBlZmljacOqbmNpYSBlbmVyZ8OpdGljYSwgYSB0ZW1wZXJhdHVyYSBkZSBkZXNjYXJnYSBkZSB1bWEgdXNpbmEgZGV2ZSBzZXIsIGVtIG3DqWRpYSwgZGUgMTAwwrBGLiBTYWJlLXNlIHF1ZSBvIGRlc3ZpbyBwYWRyw6NvIMOpICRcXHNpZ21hID0gMsKwRiQuIEVtIDkgZGlhcyBkZSBvYnNlcnZhw6fDo28sIG9idGV2ZS1zZSB1bWEgdGVtcGVyYXR1cmEgbcOpZGlhIGRlIDk4wrBGLiAoYSkgQ29uc3RydWEgbyB0ZXN0ZSBkZSBoaXDDs3Rlc2VzIGFkZXF1YWRvIGNvbSAkXFxhbHBoYSA9IDAsMDEkIHBhcmEgdmVyaWZpY2FyIHNlIGEgdGVtcGVyYXR1cmEgw6kgZGlmZXJlbnRlIGRlIDEwMMKwRi4gKGIpIFJlYWxpemUgbyBjw6FsY3VsbyBhbGfDqWJyaWNvLiAoYykgQ29uY2x1YSBzb2JyZSBhIGVzdGFiaWxpZGFkZSB0w6lybWljYSBkbyBzaXN0ZW1hLiIsICJkaWNhIjogIk8gdmFsb3IgY3LDrXRpY28gJFpfe1x0ZXh0e2NyaXR9fSQgcGFyYSAkXFxhbHBoYSA9IDAsMDEkIG51bSB0ZXN0ZSBiaWxhdGVyYWwgw6kgJFxccG0gMiw1NzYkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAoYSk6ICRIXzA6IFxcbXUgPSAxMDAkIHZzICRIXzE6IFxcbXUgXFxuZXEgMTAwJC4iLCAiUGFzc28gKGIpOiBFcnJvIHBhZHLDo286ICRcXHNpZ21hX3tcXGJhcntYfX0gPSBcXGZyYWN7Mn17XFxzcXJ0ezl9fSA9IFxcZnJhY3syfXszfSBcXGFwcHJveCAwLDY2NjckLiIsICJQYXNzbyAoYyk6IEVzdGF0w61zdGljYSBkZSB0ZXN0ZTogJFpfe1x0ZXh0e2NhbGN9fSA9IFxcZnJhY3s5OCAtIDEwMH17MCw2NjY3fSA9IFxcZnJhY3stMn17MCw2NjY3fSA9IC0zLDAwJC4iLCAiUGFzc28gKGQpOiBEZWNpc8OjbzogQ29tbyAkfC0zLDAwfCA+IDIsNTc2JCwgcmVqZWl0YW1vcyAkSF8wJCBlIGNvbmNsdcOtbW9zIHF1ZSBhIHRlbXBlcmF0dXJhIG3DqWRpYSBkaWZlcmUgc2lnbmlmaWNhdGl2YW1lbnRlIGRlIDEwMMKwRi4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IC0zLjB9LCB7ImVudW5jaWFkbyI6ICJVbWEgZW1wcmVzYSBkZSB0cmFuc3BvcnRlIFxcbG9nw61zdGljbyBhZmlybWEgcXVlIG8gY3VzdG8gbcOpZGlvIGRlIG1hbnV0ZW7Dp8OjbyBkZSBzZXVzIGNhbWluaMO1ZXMgw6kgZGUgUiQgNS4wMDAsMDAgcG9yIHNlbWVzdHJlLCBjb20gJFxcc2lnbWEgPSBSJCA0MDAsMDAuIEFuYWxpc2FuZG8gdW1hIGFtb3N0cmEgZGUgMTYgdmXDrWN1bG9zLCBvYnRldmUtc2UgJFxcYmFye1h9ID0gUiQgNS4xNTAsMDAuIChhKSBUZXN0ZSBhIGhpcMOzdGVzZSBkZSBxdWUgbyBjdXN0byBhdW1lbnRvdSAoJFxcYWxwaGEgPSAwLDA1JCkuIChiKSBDYWxjdWxlIG8gdmFsb3IgJFpfe1x0ZXh0e2NhbGN9fSQuIChjKSBPIHF1ZSBhIGVtcHJlc2EgZGV2ZSBjb25jbHVpcj8iLCAiZGljYSI6ICJFc3RlIMOpIHVtIHRlc3RlIHVuaWxhdGVyYWwgw6AgZGlyZWl0YSwgcG9pcyBhIHN1c3BlaXRhIMOpIGRlIGF1bWVudG8uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIChhKTogJEhfMDogXFxtdSA9IDUwMDAkIHZzICRIXzE6IFxcbXUgPiA1MDAwJC4iLCAiUGFzc28gKGIpOiBFcnJvIHBhZHLDo286ICRcXHNpZ21hX3tcXGJhcntYfX0gPSBcXGZyYWN7NDAwfXtcXHNxcnR7MTZ9fSA9IDEwMCQuIiwgIlBhc3NvIChjKTogRXN0YXTDrXN0aWNhIGRlIHRlc3RlOiAkWl97XHRleHR7Y2FsY319ID0gXFxmcmFjezUxNTAgLSA1MDAwfXsxMDB9ID0gMSw1MCQuIiwgIlBhc3NvIChkKTogRGVjaXPDo286IE8gdmFsb3IgY3LDrXRpY28gcGFyYSAkXFxhbHBoYSA9IDAsMDUkIMOpICQxLDY0NSQuIENvbW8gJDEsNTAgPCAxLDY0NSQsIG7Do28gcmVqZWl0YW1vcyAkSF8wJC4gTsOjbyBow6EgZXZpZMOqbmNpYSBlc3RhdMOtc3RpY2EgZGUgYXVtZW50byBub3MgY3VzdG9zIGFvIG7DrXZlbCBkZSA1JS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDEuNX0sIHsiZW51bmNpYWRvIjogIlVtIGZhYnJpY2FudGUgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIGFmaXJtYSBxdWUgYSB2aWRhIMO6dGlsIG3DqWRpYSBkZSBzZXVzIGNhcGFjaXRvcmVzIMOpIGRlICQxLjAwMCQgaG9yYXMuIEVuZ2VuaGVpcm9zIGRlIHVtIGNsaWVudGUgc3VzcGVpdGFtIHF1ZSBhIGR1cmFiaWxpZGFkZSDDqSBpbmZlcmlvciBhbyBhbnVuY2lhZG8uIFBhcmEgdGVzdGFyLCBjb2xldGFtIHVtYSBhbW9zdHJhIGRlICRuPTQwMCQgY2FwYWNpdG9yZXMsIGVuY29udHJhbmRvIHVtYSBtw6lkaWEgZGUgJFxcYmFye1h9ID0gOTkyJCBob3Jhcy4gU2FiZS1zZSBxdWUgJFxcc2lnbWEgPSA0MCQgaG9yYXMuIChhKSBGb3JtdWxlIGFzIGhpcMOzdGVzZXMgJEhfMCQgZSAkSF8xJC4gKGIpIENhbGN1bGUgYSBlc3RhdMOtc3RpY2EgJFpfe1xcdGV4dHtjYWxjfX0kLiAoYykgQ29tICRcXGFscGhhID0gMCwwMSQsIGNvbmNsdWEgbyB0ZXN0ZS4iLCAiZGljYSI6ICJPIGVudW5jaWFkbyBzdWdlcmUgcXVlIGEgZHVyYWJpbGlkYWRlIHBvZGUgc2VyICdpbmZlcmlvcicuIEVzY29saGEgdW0gdGVzdGUgdW5pbGF0ZXJhbCBpbmZlcmlvci4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiKGEpIEhpcMOzdGVzZXM6ICRIXzA6IFxcbXUgXFxnZSAxLjAwMCQgdnMgJEhfMTogXFxtdSA8IDEuMDAwJC4iLCAiKGIpIEPDoWxjdWxvIGRlICRaX3tcXHRleHR7Y2FsY319JDogJCRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFjezk5MiAtIDEuMDAwfXs0MCAvIFxcc3FydHs0MDB9fSA9IFxcZnJhY3stOH17NDAgLyAyMH0gPSBcXGZyYWN7LTh9ezJ9ID0gLTQsMDAkJC4iLCAiKGMpIERlY2lzw6NvOiBQYXJhICRcXGFscGhhID0gMCwwMSQsIG8gdmFsb3IgY3LDrXRpY28gw6kgJFpfe1xcdGV4dHtjcml0fX0gPSAtMiwzMyQuIENvbW8gJFpfe1xcdGV4dHtjYWxjfX0gPSAtNCwwMCA8IC0yLDMzJCwgcmVqZWl0YW1vcyAkSF8wJCBhbyBuw612ZWwgZGUgMSUgZGUgc2lnbmlmaWPDom5jaWEuIEV4aXN0ZSBldmlkw6puY2lhIGVzdGF0w61zdGljYSBkZSBxdWUgYSB2aWRhIMO6dGlsIMOpIGluZmVyaW9yIGEgMS4wMDAgaG9yYXMuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAtNC4wfSwgeyJlbnVuY2lhZG8iOiAiTyBjdXN0byBvcGVyYWNpb25hbCBkacOhcmlvIGRlIHVtYSBmcm90YSBkZSBjYW1pbmjDtWVzIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgY29tIGRlc3ZpbyBwYWRyw6NvIGNvbmhlY2lkbyAkXFxzaWdtYSA9IDUwJCByZWFpcy4gQSBtw6lkaWEgaGlzdMOzcmljYSDDqSAkXFxtdV8wID0gODAwJCByZWFpcy4gVW1hIG5vdmEgZXN0cmF0w6lnaWEgZGUgXFxsb2fDrXN0aWNhIGZvaSBpbXBsZW1lbnRhZGEgZSwgZW0gdW1hIGFtb3N0cmEgZGUgJG49MjUkIGRpYXMsIG9idGV2ZS1zZSBtw6lkaWEgJFxcYmFye1h9ID0gODMwJCByZWFpcy4gKGEpIFRlc3RlIGEgaGlww7N0ZXNlIGRlIHF1ZSBvIGN1c3RvIHBlcm1hbmVjZSBpZ3VhbCwgY29udHJhIGEgaGlww7N0ZXNlIGRlIHF1ZSBlbGUgc2UgYWx0ZXJvdSwgY29tICRcXGFscGhhID0gMCwwNSQuIChiKSBBcHJlc2VudGUgbyBjw6FsY3VsbyBlIGEgY29uY2x1c8Ojby4iLCAiZGljYSI6ICJUZXN0ZSBiaWxhdGVyYWwuIENvbXBhcmUgJHxaX3tcXHRleHR7Y2FsY319fCQgY29tICRaX3swLDk3NX0gPSAxLDk2JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiKGEpIEhpcMOzdGVzZXM6ICRIXzA6IFxcbXUgPSA4MDAkIHZzICRIXzE6IFxcbXUgXFxuZXEgODAwJC4iLCAiKGIpIEPDoWxjdWxvOiAkJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7ODMwIC0gODAwfXs1MCAvIFxcc3FydHsyNX19ID0gXFxmcmFjezMwfXs1MCAvIDV9ID0gXFxmcmFjezMwfXsxMH0gPSAzLDAwJCQuIiwgIihjKSBEZWNpc8OjbzogQ29tcGFyYW5kbyBjb20gbyB2YWxvciBjcsOtdGljbyBkZSAkMSw5NiQgcGFyYSB1bSB0ZXN0ZSBiaWxhdGVyYWwsICR8MywwMHwgPiAxLDk2JC4gUmVqZWl0YW1vcyAkSF8wJC4gSMOhIGV2aWTDqm5jaWEgZGUgcXVlIG9zIGN1c3RvcyBzZSBhbHRlcmFyYW0uIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAzLjB9LCB7ImVudW5jaWFkbyI6ICJFbSB1bWEgdXNpbmEgZGUgYmVuZWZpY2lhbWVudG8gZGUgXFxtaW7DqXJpbywgYSBjb25jZW50cmHDp8OjbyBkZSB1bSBtaW5lcmFsIGRldmUgc2VyIG1hbnRpZGEuIE8gdmFsb3IgZXNwZXJhZG8gw6kgJDEyLDBcXCUkLiBTdXNwZWl0YS1zZSBxdWUgbyBwcm9jZXNzbyBhdHVhbCBlc3RlamEgZ2VyYW5kbyB1bSBlbnJpcXVlY2ltZW50byBuw6NvIHBsYW5lamFkby4gRW0gJG49MTAwJCBhbW9zdHJhcywgb2J0ZXZlLXNlICRcXGJhcntYfSA9IDEyLDNcXCUkLiBDb20gJFxcc2lnbWEgPSAxLDVcXCUkLCBjb25kdXphIG8gdGVzdGUgdW5pbGF0ZXJhbCBzdXBlcmlvciBwYXJhICRcXGFscGhhID0gMCwwNSQuIiwgImRpY2EiOiAiVGVzdGUgdW5pbGF0ZXJhbCBzdXBlcmlvcjogcmVqZWl0ZSAkSF8wJCBzZSAkWl97XFx0ZXh0e2NhbGN9fSA+IFpfezAsOTV9ID0gMSw2NDUkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIoYSkgSGlww7N0ZXNlczogJEhfMDogXFxtdSBcXGxlIDEyLDAkIHZzICRIXzE6IFxcbXUgPiAxMiwwJC4iLCAiKGIpIEVzdGF0w61zdGljYTogJCRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFjezEyLDMgLSAxMiwwfXsxLDUgLyBcXHNxcnR7MTAwfX0gPSBcXGZyYWN7MCwzfXsxLDUgLyAxMH0gPSBcXGZyYWN7MCwzfXswLDE1fSA9IDIsMDAkJC4iLCAiKGMpIENvbmNsdXPDo286IENvbW8gJFpfe1xcdGV4dHtjYWxjfX0gPSAyLDAwID4gMSw2NDUkLCByZWplaXRhbW9zICRIXzAkLiBDb25jbHVpLXNlIHF1ZSBhIGNvbmNlbnRyYcOnw6NvIMOpIHN1cGVyaW9yIGEgMTIlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMi4wfSwgeyJlbnVuY2lhZG8iOiAiVW1hIGVtcHJlc2EgZGUgXFxsb2fDrXN0aWNhIGludmVzdGlnYSBvIHRlbXBvIG3DqWRpbyBkZSBlbnRyZWdhIGRlIGVuY29tZW5kYXMuIFNhYmUtc2UgcXVlIG8gdGVtcG8gc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBjb20gZGVzdmlvIHBhZHLDo28gJFxcc2lnbWEgPSAxMCQgbWludXRvcy4gQSBtZXRhIGRhIGVtcHJlc2Egw6kgcXVlIGEgbcOpZGlhIHNlamEgJFxcbXVfMCA9IDYwJCBtaW51dG9zLiAoYSkgRGVmaW5hIGFzIGhpcMOzdGVzZXMgZXN0YXTDrXN0aWNhcyBwYXJhIHVtIHRlc3RlIGJpbGF0ZXJhbC4gKGIpIFNlIHVtYSBhbW9zdHJhIGRlICRuID0gMjUkIGVudHJlZ2FzIGFwcmVzZW50b3UgbcOpZGlhICRcXGJhcntYfSA9IDY1JCBtaW51dG9zLCBjYWxjdWxlICRaX3tcXHRleHR7Y2FsY319JC4gKGMpIENvbSAkXFxhbHBoYSA9IDAsMDUkLCBhIGVtcHJlc2EgZGV2ZSBjb25zaWRlcmFyIHF1ZSBvIHRlbXBvIG3DqWRpbyBkZSBlbnRyZWdhIG11ZG91PyIsICJkaWNhIjogIlVzZSBhIGVzdGF0w61zdGljYSBaIHBhcmEgcG9wdWxhw6fDo28gbm9ybWFsIGNvbSB2YXJpw6JuY2lhIGNvbmhlY2lkYS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiKGEpIEgwOiBcXG11ID0gNjAgdnMgSDE6IFxcbXUgIT0gNjAuIiwgIihiKSBFUChYX2JhcnJhKSA9IDEwIC8gXFxzcXJ0KDI1KSA9IDEwIC8gNSA9IDIuIFpfY2FsYyA9ICg2NSAtIDYwKSAvIDIgPSA1IC8gMiA9IDIsNS4iLCAiKGMpIFpfY3JpdCBwYXJhIFxcYWxwaGEgPSAwLDA1IMOpIDEsOTYuIENvbW8gfDIsNXwgPiAxLDk2LCByZWplaXRhbW9zIEgwLiBFeGlzdGUgZXZpZMOqbmNpYSBkZSBtdWRhbsOnYSBubyB0ZW1wbyBtw6lkaW8uIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIENhcCAxMiIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDIuNX0sIHsiZW51bmNpYWRvIjogIlVtIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBkZSB1bWEgZsOhYnJpY2EgZGUgbMOibXBhZGFzIHRlc3RhIGEgdmlkYSDDunRpbCBtw6lkaWEuIEEgZXNwZWNpZmljYcOnw6NvIHTDqWNuaWNhIGRpeiBxdWUgYSB2aWRhIMO6dGlsIMOpICRcXG11ID0gMTAwMCQgaG9yYXMgY29tICRcXHNpZ21hID0gMTAwJCBob3Jhcy4gVW1hIGFtb3N0cmEgZGUgJG4gPSAxNiQgbMOibXBhZGFzIHJldmVsb3UgJFxcYmFye1h9ID0gOTUwJCBob3Jhcy4gKGEpIFRlc3RlIGEgaGlww7N0ZXNlIGRlIHF1ZSBhIHZpZGEgbcOpZGlhIGRpbWludWl1ICgkSF8xOiBcXG11IDwgMTAwMCQpIGEgdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGRlICRcXGFscGhhID0gMCwwMSQuIChiKSBDYWxjdWxlIG8gdmFsb3IgZGEgZXN0YXTDrXN0aWNhIFogZSBjb21wYXJlIGNvbSBvIHZhbG9yIGNyw610aWNvIHBhcmEgZXN0ZSB0ZXN0ZSB1bmlsYXRlcmFsLiIsICJkaWNhIjogIlBhcmEgdGVzdGVzIHVuaWxhdGVyYWlzIMOgIGVzcXVlcmRhLCBhIHJlZ2nDo28gZGUgcmVqZWnDp8OjbyBmaWNhIG5hIGNhdWRhIGluZmVyaW9yIGRhIGN1cnZhIG5vcm1hbC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiKGEpIEgwOiBcXG11ID49IDEwMDAgdnMgSDE6IFxcbXUgPCAxMDAwLiIsICIoYikgRVAoWF9iYXJyYSkgPSAxMDAgLyBcXHNxcnQoMTYpID0gMTAwIC8gNCA9IDI1LiBaX2NhbGMgPSAoOTUwIC0gMTAwMCkgLyAyNSA9IC01MCAvIDI1ID0gLTIsMC4iLCAiKGMpIFpfY3JpdCBwYXJhIFxcYWxwaGEgPSAwLDAxICh1bmlsYXRlcmFsKSDDqSAtMiwzMy4gQ29tbyAtMiwwID4gLTIsMzMsIG7Do28gcmVqZWl0YW1vcyBIMC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IC0yLjB9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyBwcm9ibGVtYSBkbyByZW5kaW1lbnRvIGRlIGHDp8O1ZXM6IGEgbcOpZGlhIGhpc3TDs3JpY2Egw6kgMjQlIGNvbSBkZXN2aW8gcGFkcsOjbyBkZSA1JS4gRW0gdW1hIGFtb3N0cmEgZGUgMTYgZW1wcmVzYXMsIG9idGV2ZS1zZSByZW5kaW1lbnRvIG3DqWRpbyAkXFxiYXJ7WH0gPSAyNlxcJSQuIChhKSBGb3JtdWxlIG8gdGVzdGUgcGFyYSB2ZXJpZmljYXIgc2UgbyByZW5kaW1lbnRvIG3DqWRpbyBhdW1lbnRvdS4gKGIpIENhbGN1bGUgJFpfe1xcdGV4dHtjYWxjfX0kLiAoYykgQ29tICRcXGFscGhhID0gMCwwNSQsIHF1YWwgw6kgYSBjb25jbHVzw6NvIGVzdGF0w61zdGljYT8iLCAiZGljYSI6ICJPIHRlc3RlIMOpIHVuaWxhdGVyYWwgw6AgZGlyZWl0YS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiKGEpIEgwOiBcXG11IDw9IDI0IHZzIEgxOiBcXG11ID4gMjQuIiwgIihiKSBFUChYX2JhcnJhKSA9IDUgLyBcXHNxcnQoMTYpID0gNSAvIDQgPSAxLDI1LiBaX2NhbGMgPSAoMjYgLSAyNCkgLyAxLDI1ID0gMiAvIDEsMjUgPSAxLDYuIiwgIihjKSBaX2NyaXQgcGFyYSBcXGFscGhhID0gMCwwNSAodW5pbGF0ZXJhbCDDoCBkaXJlaXRhKSDDqSAxLDY0NS4gQ29tbyAxLDYgPCAxLDY0NSwgbsOjbyByZWplaXRhbW9zIEgwLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBDYXAgMTIiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAxLjZ9XX0=').decode('utf-8'))


    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    from scipy import stats
    
    # Inicialização do controle de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dos totais
    lista_mcq = dados_exercicios.get("questoes_multipla_escolha", [])
    lista_disc = dados_exercicios.get("questoes_discursivas", [])
    total_ex = len(lista_mcq) + len(lista_disc)
    acertos = sum(1 for v in st.session_state.respostas_certas.values() if v is True)
    
    # Interface de Gamificação
    st.markdown("### 🎯 Painel de Exercícios")
    if total_ex > 0:
        st.progress(acertos / total_ex)
        st.info(f"🏆 **Seu Placar de Aprendizado:** {acertos} de {total_ex} desafios concluídos com sucesso!")
    
    # Seção de Questões de Múltipla Escolha
    if lista_mcq:
        st.subheader("📝 Questões de Múltipla Escolha")
        for i, q in enumerate(lista_mcq):
            with st.container(border=True):
                st.markdown(f"#### Questão {i+1}")
                st.markdown(q["enunciado"])
                
                if q.get("referencia_livro"):
                    st.markdown(f"📖 *Referência: {q['referencia_livro']}*")
                
                # Execução segura de Plotly se existir
                if q.get("codigo_plotly"):
                    try:
                        local_vars = {"go": go, "np": np, "stats": stats}
                        exec(q["codigo_plotly"], globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True)
                    except Exception as e:
                        st.warning("Visualização indisponível.")
    
                opcoes = q["alternativas"]
                escolha = st.radio(
                    "Escolha uma alternativa:",
                    options=list(opcoes.keys()),
                    format_func=lambda x: f"{x}: {opcoes[x]}",
                    key=f"radio_mcq_{i}"
                )
                
                if st.button("💡 Dica", key=f"dica_mcq_{i}"):
                    st.info(q.get("dica"))
                
                if st.button("✅ Confirmar Resposta", key=f"btn_mcq_{i}"):
                    if escolha == q["alternativa_correta"]:
                        st.success("🎉 Correto! Resposta excelente.")
                        st.session_state.respostas_certas[f"mcq_{i}"] = True
                    else:
                        st.error("❌ Resposta Incorreta. Reveja os conceitos e tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
                
                with st.expander("🔍 Ver Gabarito Comentado"):
                    st.write(q.get("gabarito_comentado"))
    
    # Seção de Questões Discursivas
    if lista_disc:
        st.subheader("💡 Questões Discursivas e Práticas")
        for i, q in enumerate(lista_disc):
            with st.container(border=True):
                st.markdown(f"#### Questão {i+1}")
                st.markdown(q["enunciado"])
                
                if q.get("referencia_livro"):
                    st.markdown(f"📖 *Referência: {q['referencia_livro']}*")
                
                # Plotly para discursivas
                if q.get("codigo_plotly"):
                    try:
                        local_vars = {"go": go, "np": np, "stats": stats}
                        exec(q["codigo_plotly"], globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True)
                    except Exception:
                        pass
                
                st.text_area("Sua análise ou raciocínio:", key=f"text_disc_{i}")
                
                # Validação
                if q.get("resposta_numerica_esperada") is not None:
                    val_aluno = st.number_input("Resultado numérico:", format="%.4f", key=f"num_disc_{i}")
                    if st.button("Validar Cálculo", key=f"btn_val_{i}"):
                        esperado = q["resposta_numerica_esperada"]
                        if abs(val_aluno - esperado) <= max(0.01, 0.05 * abs(esperado)):
                            st.success("🎉 Resultado Numérico Correto!")
                            st.session_state.respostas_certas[f"disc_{i}"] = True
                        else:
                            st.error("❌ Valor incorreto. Confira seus cálculos!")
                            st.session_state.respostas_certas[f"disc_{i}"] = False
                else:
                    if st.checkbox("Marque aqui após concluir sua reflexão", key=f"check_disc_{i}"):
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                    else:
                        st.session_state.respostas_certas[f"disc_{i}"] = False
                
                with st.expander("✅ Ver Resolução Detalhada"):
                    for passo in q.get("gabarito_passo_a_passo", []):
                        st.markdown(f"- {passo}")
