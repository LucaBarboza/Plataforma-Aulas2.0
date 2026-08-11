import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuMzogSW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgcGFyYSBtw6lkaWEgZSBwcm9wb3LDp8OjbyB1c2FuZG8gZ3JhbmRlcyBhbW9zdHJhcyIsICJyZWZlcmVuY2lhc19iaWJsaW9ncmFmaWNhc19maW5haXMiOiBbIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSAtIENhcC4gMTAsIHBwLiAyNzctMjgxIiwgIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSAtIENhcC4gMTEsIHBwLiAzMTEtMzE2Il19').decode('utf-8'))

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
    from scipy import stats
    
    st.header(r"O Teorema do Limite Central e a Inferência Assintótica")
    
    st.markdown(r"""
    O Teorema do Limite Central (TLC) constitui o alicerce da inferência estatística moderna, oferecendo uma garantia teórica sobre o comportamento das médias amostrais. Independentemente da natureza da distribuição original na população, o TLC estabelece que a distribuição da média amostral $\bar{X}$ tende à normalidade à medida que o tamanho da amostra $n$ aumenta.
    """)
    
    st.markdown(r"""
    Este fenômeno, conhecido como normalidade assintótica, permite que pesquisadores utilizem a curva gaussiana para modelar fenômenos complexos, garantindo rigor matemático mesmo quando a distribuição subjacente é desconhecida ou assimétrica.
    """)
    
    st.info(r"Na prática, o erro padrão da média $EP(\bar{X})$ quantifica a dispersão esperada das estimativas, permitindo a construção de intervalos de confiança robustos.")
    
    st.markdown(r"""
    ### 📐 O Coração Matemático: Convergência em Distribuição
    A elegância do TLC reside na convergência em distribuição, onde a variável padronizada converge para a normal padrão:
    """)
    
    st.latex(r"Z_n = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} N(0, 1)")
    
    st.markdown(r"""
    Abaixo, a decomposição fundamental que sustenta o teorema:
    """)
    
    st.latex(r"E(\bar{X}) = E\left(\frac{1}{n} \sum_{i=1}^n X_i\right) = \mu")
    st.latex(r"Var(\bar{X}) = Var\left(\frac{1}{n} \sum_{i=1}^n X_i\right) = \frac{\sigma^2}{n}")
    st.latex(r"Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}")
    
    # Simulador de Convergência ao TLC
    st.subheader(r"📈 Simulador de Convergência ao TLC")
    col1, col2 = st.columns(2)
    with col1:
        n_samples = st.slider(r"Tamanho da amostra (n)", 10, 1000, 100, key=r"n_subtopico_1")
    with col2:
        dist_type = st.selectbox(r"Distribuição Populacional", [r"Normal", r"Uniforme", r"Exponencial"], key=r"dist_subtopico_1")
    
    # Lógica do Simulador
    n_simulations = 1000
    if dist_type == r"Normal":
        data_gen = np.random.normal(0, 1, (n_simulations, n_samples))
    elif dist_type == r"Uniforme":
        data_gen = np.random.uniform(-1, 1, (n_simulations, n_samples))
    else:
        data_gen = np.random.exponential(1, (n_simulations, n_samples))
    
    means = np.mean(data_gen, axis=1)
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=means, nbinsx=30, marker_color=r"#1E3A8A", name=r"Médias Amostrais"))
    
    fig.update_layout(
        template=r"plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Distribuição das Médias Amostrais</b>", font=dict(size=14, color=r"#1E293B", family=r"Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Valor da Média", font=dict(size=11, color=r"#1E293B")), tickfont=dict(size=9, color=r"#64748B"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Frequência", font=dict(size=11, color=r"#1E293B")), tickfont=dict(size=9, color=r"#64748B"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        legend=dict(orientation=r"h", yanchor=r"bottom", y=1.02, xanchor=r"right", x=1.0, font=dict(size=9, color=r"#64748B"), bgcolor=r"rgba(255, 255, 255, 0.8)", bordercolor=r"#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor=r"#FFFFFF", font_size=12, font_color=r"#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    # Laudo Dinâmico
    erro_padrao = 1.0 / np.sqrt(n_samples)
    st.info(f"Com n = {n_samples}, a distribuição das médias torna-se mais concentrada em torno da média populacional. O erro padrão observado é de aproximadamente {erro_padrao:.4f}, evidenciando o efeito de redução da variabilidade pela raiz quadrada de n.")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática: Logística")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Monitoramento de entregas")
        st.markdown(r"Uma empresa de logística monitora o tempo de entrega de pacotes. Dados históricos indicam média de 50 minutos e desvio padrão de 15 minutos. Com n = 100, verificamos a conformidade:")
        st.latex(r"EP(\bar{X}) = \frac{15}{\sqrt{100}} = 1.5")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo para z = 2: $\frac{53 - 50}{1.5} = 2$")
        st.markdown(r"- Cálculo para z = -2: $\frac{47 - 50}{1.5} = -2$")
        st.success(r"A probabilidade de 95,44% calculada demonstra alta estabilidade operacional, permitindo predições logísticas precisas com margem de erro de ±3 minutos.")

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Inferência para a Média Populacional ($\mu$) com Variância Desconhecida")
    
    # Prosa Inicial
    st.markdown(r"""
    Ao transitar da teoria para a prática, encontramos frequentemente a limitação de não conhecer a variância populacional $\sigma^2$. Em cenários aplicados, substituímos $\sigma$ pelo estimador amostral $S$, o desvio padrão da amostra.
    """)
    
    st.info(r"Esta substituição é assintoticamente válida para grandes amostras ($n \ge 100$), pois o erro de estimativa torna-se desprezível, permitindo a manutenção da distribuição normal no cálculo de intervalos de confiança. Este procedimento confere flexibilidade operacional sem perda significativa de precisão estatística.")
    
    # Formalismo Matemático
    st.markdown(r"### 📐 Formalismo do Intervalo de Confiança")
    st.latex(r"IC(\mu; 1-\alpha) = \left[ \bar{X} - z_{\alpha/2} \cdot \frac{S}{\sqrt{n}}, \bar{X} + z_{\alpha/2} \cdot \frac{S}{\sqrt{n}} \right]")
    
    # O Coração Matemático: Dedução Analítica
    st.markdown(r"### 🧠 O Coração Matemático: Dedução Analítica")
    
    st.markdown(r"Partimos da estatística de teste padronizada para grandes amostras:")
    st.latex(r"Z_{\text{calc}} = \frac{\bar{X} - \mu}{S / \sqrt{n}}")
    
    st.markdown(r"Estabelecemos o nível de confiança $1-\alpha$ na distribuição normal:")
    st.latex(r"P(-z_{\alpha/2} \le Z_{\text{calc}} \le z_{\alpha/2}) = 1-\alpha")
    
    st.markdown(r"Isolamos o parâmetro populacional $\mu$ através da manipulação algébrica da desigualdade:")
    st.latex(r"-z_{\alpha/2} \cdot \frac{S}{\sqrt{n}} \le \bar{X} - \mu \le z_{\alpha/2} \cdot \frac{S}{\sqrt{n}}")
    
    st.latex(r"\bar{X} - z_{\alpha/2} \cdot \frac{S}{\sqrt{n}} \le \mu \le \bar{X} + z_{\alpha/2} \cdot \frac{S}{\sqrt{n}}")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Vida Útil de Componentes")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Indústria de Eletrônicos")
        st.markdown(r"Uma indústria de componentes eletrônicos testa a vida útil de 150 processadores. A variância populacional é desconhecida. A amostra apresentou média $\bar{X} = 850$ horas e $S = 45$ horas. O objetivo é estimar a vida útil média com 95% de confiança.")
        
        st.latex(r"\bar{X} = 850, \quad S = 45, \quad n = 150, \quad z_{0,025} = 1,96")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo do Erro Padrão: $EP(\bar{X}) = 45 / \sqrt{150} \approx 3,674$")
        st.markdown(r"- Cálculo da Margem de Erro: $E = 1,96 \cdot 3,674 \approx 7,20$")
        st.markdown(r"- Definição do Intervalo: $IC = [850 - 7,20, 850 + 7,20] = [842,8, 857,2]$")
        
        st.success(r"Com 95% de confiança, a vida média real dos processadores está entre 842,8 e 857,2 horas. Este intervalo permite à engenharia balizar a garantia do produto com fundamentação probabilística.")
    
    # Prosa Longa Expandida
    with st.expander(r"📚 Aprofundamento Teórico: A Transição para a Realidade Estatística"):
        st.markdown(r"""
        Ao avançarmos na construção do edifício da inferência estatística, deparamo-nos inevitavelmente com um divisor de águas intelectual: a distinção entre o mundo puramente teórico e o mundo prático da investigação científica. Quando substituímos o parâmetro populacional $\sigma$ pelo estimador amostral $S$, estamos operando uma mudança de natureza epistemológica: passamos de uma constante fixa para uma variável aleatória.
    
        A lógica por trás desta substituição repousa sobre as propriedades assintóticas dos estimadores de dispersão. Conforme o tamanho da amostra $n$ aumenta, a variabilidade de $S$ em torno do verdadeiro valor de $\sigma$ diminui drasticamente. Em cenários de grandes amostras ($n \ge 100$), o erro inerente à estimativa torna-se estatisticamente desprezível, invocando o Teorema de Slutsky para validar o uso da distribuição normal.
        
        Historicamente, este entendimento democratizou a análise estatística, permitindo que pesquisadores evitassem a complexidade das distribuições de Student para grandes volumes de dados, sem perda de rigor, visto que a distribuição $t$ converge para a Gaussiana sob a Lei dos Grandes Números.
        """)
    
    # Simulador Interativo
    st.markdown(r"### 🎛️ Simulador de Incerteza Amostral")
    col1, col2 = st.columns(2)
    n_sim = col1.slider(r"Tamanho da amostra (n)", 100, 1000, 150, key=r"n_sim_subtopico_2")
    conf_sim = col2.select_slider(r"Nível de Confiança", options=[0.90, 0.95, 0.99], value=0.95, key=r"conf_sim_subtopico_2")
    
    # Cálculos do Simulador
    z_val = stats.norm.ppf(1 - (1 - conf_sim) / 2)
    erro_padrao = 45 / np.sqrt(n_sim)
    margem = z_val * erro_padrao
    
    # Gráfico Plotly
    fig = go.Figure()
    x_axis = np.linspace(800, 900, 500)
    y_axis = stats.norm.pdf(x_axis, 850, 45/np.sqrt(150)) # Distribuição teórica ilustrativa
    fig.add_trace(go.Scatter(x=x_axis, y=y_axis, mode='lines', name=r"Distribuição da Média", line=dict(color="#1E3A8A", width=2)))
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição da Média Amostral e Margem de Erro</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Vida Útil Média (horas)", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    # Laudo Dinâmico
    st.info(f"Ao utilizar uma amostra de n = {n_sim} e {int(conf_sim*100)}% de confiança, a margem de erro estimada é de {margem:.2f} horas. Observe que o aumento de n reduz a incerteza (erro padrão), estreitando o intervalo de confiança e aumentando a precisão da estimativa de $\mu$.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Intervalos de Confiança para Proporções Populacionais (p)")
    
    # Discussão Teórica e Fundamentos
    st.markdown(r"""
    Para atributos qualitativos, como intenções de voto ou conformidade em lotes industriais, utilizamos a proporção amostral $\hat{p}$. 
    O comportamento dessas proporções segue a lógica binomial que, para amostras grandes, aproxima-se da normal.
    """)
    
    st.info(r"A construção do intervalo de confiança para $p$ baseia-se na margem de erro ao redor de $\hat{p}$, onde a variabilidade estimada é sensível aos valores de $\hat{p}$ e $1-\hat{p}$.")
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Intervalo de Confiança para Proporções")
    st.latex(r"IC(p; 1-\alpha) = \left[ \hat{p} - z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}, \hat{p} + z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \right]")
    
    # Dedução Analítica
    st.markdown(r"A dedução segue os passos da distribuição amostral:")
    st.latex(r"\hat{p} \sim N\left(p, \frac{p(1-p)}{n}\right)")
    st.markdown(r"Aplicando o nível de confiança $1-\alpha$ na distribuição normal padrão:")
    st.latex(r"P\left(-z_{\alpha/2} \le \frac{\hat{p}-p}{\sqrt{\hat{p}(1-\hat{p})/n}} \le z_{\alpha/2}\right) = 1-\alpha")
    st.markdown(r"Isolando o parâmetro populacional $p$, obtemos os limites do intervalo:")
    st.latex(r"\hat{p} - z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \le p \le \hat{p} + z_{\alpha/2} \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}")
    
    # Simulador: Visualizador de Margem de Erro
    st.subheader(r"📊 Simulador: Visualizador de Margem de Erro")
    col1, col2 = st.columns(2)
    with col1:
        confianca = st.select_slider(r"Nível de Confiança", options=[0.90, 0.95, 0.99], value=0.95, key=r"conf_subtopico_3")
        n_amostra = st.slider(r"Tamanho da Amostra (n)", min_value=100, max_value=2000, value=500, step=50, key=r"n_subtopico_3")
    with col2:
        p_hat = st.number_input(r"Proporção Amostral (p-chapéu)", min_value=0.01, max_value=0.99, value=0.64, step=0.01, key=r"phat_subtopico_3")
    
    z_val = stats.norm.ppf(1 - (1 - confianca) / 2)
    erro_padrao = np.sqrt((p_hat * (1 - p_hat)) / n_amostra)
    margem_erro = z_val * erro_padrao
    
    # Gráfico
    fig = go.Figure()
    x_vals = np.linspace(p_hat - 4*erro_padrao, p_hat + 4*erro_padrao, 200)
    y_vals = stats.norm.pdf(x_vals, p_hat, erro_padrao)
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode=r"lines", name=r"Distribuição de p", line=dict(color=r"#1E3A8A")))
    fig.add_vrect(x0=p_hat - margem_erro, x1=p_hat + margem_erro, fillcolor=r"#10B981", opacity=0.2, line_width=0)
    fig.update_layout(
        template=r"plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Visualização da Margem de Erro</b>", font=dict(size=14, color=r"#1E293B", family=r"Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Proporção", font=dict(size=11, color=r"#1E293B")), tickfont=dict(size=9, color=r"#64748B"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Densidade", font=dict(size=11, color=r"#1E293B")), tickfont=dict(size=9, color=r"#64748B"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        legend=dict(orientation=r"h", yanchor=r"bottom", y=1.02, xanchor=r"right", x=1.0, font=dict(size=9, color=r"#64748B"), bgcolor=r"rgba(255, 255, 255, 0.8)", bordercolor=r"#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor=r"#FFFFFF", font_size=12, font_color=r"#1E293B")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    st.info(f"Com uma amostra de n={n_amostra} e confiança de {int(confianca*100)}%, a margem de erro calculada é de {margem_erro:.4f}. O intervalo resultante situa-se entre {p_hat - margem_erro:.4f} e {p_hat + margem_erro:.4f}.")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Aceitação de Interface")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Aceitação de Software")
        st.markdown(r"Uma empresa de software analisa a aceitação de uma nova interface. Em uma amostra de 500 usuários, 320 preferiram a nova versão. Deseja-se calcular o intervalo de confiança de 95% para a proporção populacional.")
        st.latex(r"n = 500, \hat{p} = 0,64, \hat{q} = 0,36, z_{0,025} = 1,96")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Erro Padrão: $EP(\hat{p}) = \sqrt{(0,64 \cdot 0,36) / 500} \approx 0,02147$")
        st.markdown(r"- Margem de Erro: $E = 1,96 \cdot 0,02147 \approx 0,0421$")
        st.success(r"Conclusão: Com 95% de confiança, a proporção de aceitação situa-se entre 59,79% e 68,21%. Como o limite inferior supera 50%, a diretoria pode implementar a interface com segurança estatística.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuMzogSW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgcGFyYSBtw6lkaWEgZSBwcm9wb3LDp8OjbyB1c2FuZG8gZ3JhbmRlcyBhbW9zdHJhcyIsICJxdWVzdG9lc19tdWx0aXBsYV9lc2NvbGhhIjogW3siZW51bmNpYWRvIjogIlVtYSBpbmTDunN0cmlhIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyB1dGlsaXphIHNlbnNvcmVzIHBhcmEgbWVkaXIgYSByZXNpc3TDqm5jaWEgZGUgcGxhY2FzLiBBIHJlc2lzdMOqbmNpYSBkZSB1bWEgw7puaWNhIHBsYWNhIMOpIHVtYSB2YXJpw6F2ZWwgYWxlYXTDs3JpYSBjb20gZGlzdHJpYnVpw6fDo28gZGVzY29uaGVjaWRhLCBtYXMgY29tIG3DqWRpYSAkXFxtdSA9IDUwXFxPbWVnYSQgZSB2YXJpw6JuY2lhICRcXHNpZ21hXjIgPSAxMDBcXE9tZWdhXjIkLiBBIGVxdWlwZSBkZSBlbmdlbmhhcmlhIGNvbGV0YSB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIGRlICRuID0gMTAwJCBwbGFjYXMgcGFyYSBjb250cm9sZSBkZSBxdWFsaWRhZGUuIFNlZ3VuZG8gbyBUZW9yZW1hIGRvIExpbWl0ZSBDZW50cmFsLCBxdWFsIGRhcyBhZmlybWHDp8O1ZXMgYWJhaXhvIG1lbGhvciBkZXNjcmV2ZSBvIGNvbXBvcnRhbWVudG8gZGEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0kIHNlZ3VpcsOhIGVzdHJpdGFtZW50ZSBhIG1lc21hIGRpc3RyaWJ1acOnw6NvIGRhIHBvcHVsYcOnw6NvIG9yaWdpbmFsLCBpbmRlcGVuZGVudGVtZW50ZSBkbyB0YW1hbmhvICRuJC4iLCAiQiI6ICJBIGRpc3RyaWJ1acOnw6NvIGRlICRcXGJhcntYfSQgc2Vyw6EgYXByb3hpbWFkYW1lbnRlIG5vcm1hbCBjb20gbcOpZGlhICRcXG11ID0gNTAkIGUgdmFyacOibmNpYSAkXFxzaWdtYV4yL24gPSAxJC4iLCAiQyI6ICJPIEVycm8gUGFkcsOjbyBkYSBNw6lkaWEgJEVQKFxcYmFye1h9KSQgc2Vyw6EgaWd1YWwgYSAkMTAwJCwgdG9ybmFuZG8gYSBlc3RpbWF0aXZhICRcXGJhcntYfSQgcG91Y28gcHJlY2lzYS4iLCAiRCI6ICJBIGRpc3RyaWJ1acOnw6NvIGRlICRcXGJhcntYfSQgdGVyw6EgbcOpZGlhICQ1MC8xMDAgPSAwLjUkIGUgdmFyacOibmNpYSAkMTAwLzEwMCA9IDEkLiIsICJFIjogIk8gVGVvcmVtYSBkbyBMaW1pdGUgQ2VudHJhbCBuw6NvIHBvZGUgc2VyIGFwbGljYWRvIHBvaXMgbsOjbyBjb25oZWNlbW9zIGEgZGlzdHJpYnVpw6fDo28gb3JpZ2luYWwgZGEgcG9wdWxhw6fDo28uIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIG8gVGVvcmVtYSBkbyBMaW1pdGUgQ2VudHJhbCBlc3RhYmVsZWNlIHF1ZSBhIGRpc3RyaWJ1acOnw6NvIGRhIG3DqWRpYSBhbW9zdHJhbCBjb252ZXJnZSBwYXJhIHVtYSBub3JtYWwgY29tIG3DqWRpYSAkXFxtdSQgZSB2YXJpw6JuY2lhICRcXHNpZ21hXjIvbiQuIENhbGN1bGUgbyB2YWxvciBkYSB2YXJpw6JuY2lhIGRhIG3DqWRpYSBhbW9zdHJhbC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBlbG8gVGVvcmVtYSBkbyBMaW1pdGUgQ2VudHJhbCwgcGFyYSAkbj0xMDAkLCBhIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0kIHRlbmRlIMOgIGRpc3RyaWJ1acOnw6NvICROKFxcbXUsIFxcc2lnbWFeMi9uKSQuIFN1YnN0aXR1aW5kbyBvcyB2YWxvcmVzOiBtw6lkaWEgPSAkXFxtdSA9IDUwJCBlIHZhcmnDom5jaWEgPSAkXFxzaWdtYV4yL24gPSAxMDAvMTAwID0gMSQuIFBvcnRhbnRvLCAkXFxiYXJ7WH0gXFxzaW0gTig1MCwgMSkkLiBBIGFsdGVybmF0aXZhIEIgZGVzY3JldmUgZXhhdGFtZW50ZSBlc3NhIHByb3ByaWVkYWRlIGRlIG5vcm1hbGlkYWRlIGFzc2ludMOzdGljYSBlIG8gY8OhbGN1bG8gZGEgbm92YSB2YXJpw6JuY2lhLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bNDcsIDUzXSwgeT1bMCwgMF0sIG1vZGU9J2xpbmVzJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJywgd2lkdGg9MiksIG5hbWU9J0Rpc3RyaWJ1acOnw6NvIE5vcm1hbCBBcHJveGltYWRhJykpXG4jIEFkaWNpb25hbmRvIHZpc3VhbGl6YcOnw6NvIGRlIGRlbnNpZGFkZSBwYXJhIE4oNTAsIDEpXG54ID0gbnAubGluc3BhY2UoNDcsIDUzLCAxMDApXG55ID0gKDEgLyBucC5cXHNxcnQoMiAqIG5wLlxccGkpKSAqIG5wLlxcZXhwKC0wLjUgKiAoeCAtIDUwKSoqMilcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgZmlsbD0ndG96ZXJveScsIGZpbGxjb2xvcj0ncmdiYSgzMCwgNTgsIDEzOCwgMC4yKScsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScpLCBuYW1lPSdEZW5zaWRhZGUgZGUgJFxcYmFye1h9JCcpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkRpc3RyaWJ1acOnw6NvIEFzc2ludMOzdGljYSBkYSBNw6lkaWEgQW1vc3RyYWw8L2I+JywgeGF4aXNfdGl0bGU9J03DqWRpYSBBbW9zdHJhbCAoJFxcYmFye1h9JCknLCB5YXhpc190aXRsZT0nRGVuc2lkYWRlJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIHRlbGVtZXRyaWEgSW9ULCBvIGNvbnN1bW8gZGUgZGFkb3MgZGUgZGlzcG9zaXRpdm9zIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyBhbHRhbWVudGUgYXNzaW3DqXRyaWNhIGNvbSAkXFxtdSA9IDIwME1CJCBlICRcXHNpZ21hID0gNDBNQiQuIFVtIGNpZW50aXN0YSBkZSBkYWRvcyBzZWxlY2lvbmEgJG49MjU2JCBkaXNwb3NpdGl2b3MuIE8gY2llbnRpc3RhIGRlc2VqYSBjYWxjdWxhciBhIHByb2JhYmlsaWRhZGUgZGEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSQgc2VyIHN1cGVyaW9yIGEgJDIwNU1CJC4gUG9yIHF1ZSDDqSBtYXRlbWF0aWNhbWVudGUganVzdGlmaWPDoXZlbCB1dGlsaXphciBhIHRhYmVsYSBkYSBub3JtYWwgcGFkcsOjbyBwYXJhIGVzdGUgY8OhbGN1bG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJQb3JxdWUgYSBhbW9zdHJhIMOpIHBlcXVlbmEgZSBxdWFscXVlciBkaXN0cmlidWnDp8OjbyB0ZW5kZSBhIHNlciBub3JtYWwgY29tICRuIDwgMzAkLiIsICJCIjogIlBvcnF1ZSBvIFRlb3JlbWEgZG8gTGltaXRlIENlbnRyYWwgZ2FyYW50ZSBhIG5vcm1hbGlkYWRlIGRlICRcXGJhcntYfSQgcGFyYSBhbW9zdHJhcyBncmFuZGVzLCBpbmRlcGVuZGVudGVtZW50ZSBkYSBhc3NpbWV0cmlhIGRhIHBvcHVsYcOnw6NvLiIsICJDIjogIlBvcnF1ZSBhIGRpc3RyaWJ1acOnw6NvIGRlIGRhZG9zIGRvIGRpc3Bvc2l0aXZvIMOpLCBwb3IgZGVmaW5pw6fDo28sIG5vcm1hbCBlbSBhbWJpZW50ZXMgZGUgYWx0YSB0ZWNub2xvZ2lhLiIsICJEIjogIlBvcnF1ZSBhIG3DqWRpYSBwb3B1bGFjaW9uYWwgw6kgbWFpb3IgcXVlIG8gZGVzdmlvIHBhZHLDo28sIG8gcXVlIGludmFsaWRhIGEgbmVjZXNzaWRhZGUgZGUgbm9ybWFsaWRhZGUuIiwgIkUiOiAiUG9ycXVlIGEgbm9ybWFsaWRhZGUgYXNzaW50w7N0aWNhIHPDsyBvY29ycmUgc2UgYSBwb3B1bGHDp8OjbyBmb3IgXFxzaW3DqXRyaWNhLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTyBwb250byBjZW50cmFsIGRvIFRlb3JlbWEgZG8gTGltaXRlIENlbnRyYWwgw6kgcXVlIGVsZSBhdHVhIGNvbW8gdW1hICdmb3LDp2EgZ3Jhdml0YWNpb25hbCcgcXVlIG5vcm1hbGl6YSBhIGRpc3RyaWJ1acOnw6NvIGRhIG3DqWRpYSBhbW9zdHJhbCBxdWFuZG8gJG4kIMOpIGdyYW5kZSwgc3VwZXJhbmRvIGEgZm9ybWEgZGEgZGlzdHJpYnVpw6fDo28gcG9wdWxhY2lvbmFsLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBUZW9yZW1hIGRvIExpbWl0ZSBDZW50cmFsIMOpIHVtYSBmZXJyYW1lbnRhIHBvZGVyb3NhIGp1c3RhbWVudGUgcG9yIHN1YSByb2J1c3RleiBmcmVudGUgw6AgZGlzdHJpYnVpw6fDo28gb3JpZ2luYWwgZG9zIGRhZG9zLiBRdWFuZG8gJG4kIMOpIHN1ZmljaWVudGVtZW50ZSBncmFuZGUgKGVtIGdlcmFsICRuIFxcZ2UgMzAkLCBlIGFxdWkgdGVtb3MgJG49MjU2JCksIGEgZGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgZGEgbcOpZGlhICRcXGJhcntYfSQgYXByb3hpbWEtc2UgZGUgdW1hIG5vcm1hbCAkTihcXG11LCBcXHNpZ21hXjIvbikkLCBtZXNtbyBxdWUgYSBwb3B1bGHDp8OjbyBvcmlnaW5hbCBuw6NvIHNlamEgbm9ybWFsIG91IHNlamEgYXNzaW3DqXRyaWNhLiBQb3J0YW50bywgYSBhbHRlcm5hdGl2YSBCIMOpIGEgw7puaWNhIHF1ZSByZWZsZXRlIGNvcnJldGFtZW50ZSBvIGVzY29wbyBkbyB0ZW9yZW1hLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIGRlIGFsdGEgcHJlY2lzw6NvIGVzdMOhIHZhbGlkYW5kbyBhIGR1cmFiaWxpZGFkZSBkZSB1bSBub3ZvIHNlbnNvci4gQ29tbyBvIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCBkYSBkdXJhYmlsaWRhZGUgKCRcXHNpZ21hJCkgw6kgZGVzY29uaGVjaWRvLCBjb2xldG91LXNlIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgZGUgJG49MTQ0JCBzZW5zb3Jlcywgb2J0ZW5kby1zZSB1bWEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSA9IDIuNTAwJCBob3JhcyBlIHVtIGRlc3ZpbyBwYWRyw6NvIGFtb3N0cmFsICRTID0gMjQwJCBob3Jhcy4gRGVzZWphLXNlIGNvbnN0cnVpciB1bSBJbnRlcnZhbG8gZGUgQ29uZmlhbsOnYSAoJElDJCkgcGFyYSBhIHZpZGEgw7p0aWwgbcOpZGlhICgkXFxtdSQpIGNvbSB1bSBuw612ZWwgZGUgY29uZmlhbsOnYSBkZSA5NSUgKCQxLVxcYWxwaGE9MCw5NSQpLiBDb25zaWRlcmFuZG8gcXVlIHBhcmEgJG49MTQ0JCwgYSBlc3RhdMOtc3RpY2EgcGFkcm9uaXphZGEgY29udmVyZ2UgcGFyYSBhIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBwYWRyw6NvLCBxdWFsIMOpIGEgYW1wbGl0dWRlIGNvcnJldGEgZG8gJElDJD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjM5LDIgaG9yYXMiLCAiQiI6ICI3OCw0IGhvcmFzIiwgIkMiOiAiMTU2LDggaG9yYXMiLCAiRCI6ICIxOSw2IGhvcmFzIiwgIkUiOiAiMzEzLDYgaG9yYXMifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgYSBhbXBsaXR1ZGUgZGUgdW0gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgcGFyYSBhIG3DqWRpYSDDqSBkYWRhIHBlbGEgZGlmZXJlbsOnYSBlbnRyZSBvcyBsaW1pdGVzIHN1cGVyaW9yIGUgaW5mZXJpb3IsIG91IHNlamEsICQyIFxcY2RvdCB6X3tcXGFscGhhLzJ9IFxcY2RvdCBcXGZyYWN7U317XFxzcXJ0e259fSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIHVtIG7DrXZlbCBkZSBjb25maWFuw6dhIGRlIDk1JSAoJDEtXFxhbHBoYT0wLDk1JCksIHRlbW9zICRcXGFscGhhPTAsMDUkIGUgJFxcYWxwaGEvMj0wLDAyNSQuIE8gdmFsb3IgY3LDrXRpY28gJHpfezAsMDI1fSQgbmEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIHBhZHLDo28gw6kgJDEsOTYkLiBPIGVycm8gcGFkcsOjbyBlc3RpbWFkbyBkYSBtw6lkaWEgw6kgJEVQKFxcYmFye1h9KSA9IFMgLyBcXHNxcnR7bn0gPSAyNDAgLyBcXHNxcnR7MTQ0fSA9IDI0MCAvIDEyID0gMjAkLiBBIG1hcmdlbSBkZSBlcnJvIMOpICRFID0gel97XFxhbHBoYS8yfSBcXGNkb3QgRVAoXFxiYXJ7WH0pID0gMSw5NiBcXGNkb3QgMjAgPSAzOSwyJC4gQSBhbXBsaXR1ZGUgdG90YWwgZG8gaW50ZXJ2YWxvIMOpICQyIFxcY2RvdCBFID0gMiBcXGNkb3QgMzksMiA9IDc4LDQkIGhvcmFzLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoMjQwMCwgMjYwMCwgMTAwKVxueSA9ICgxLygyMCpucC5cXHNxcnQoMipucC5cXHBpKSkpICogbnAuXFxleHAoLTAuNSooKHgtMjUwMCkvMjApKioyKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBuYW1lPSdEaXN0cmlidWnDp8OjbyBkYSBNw6lkaWEnLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0zKSkpXG5maWcuYWRkX3ZsaW5lKHg9MjUwMC0zOS4yLCBsaW5lX2Rhc2g9J2Rhc2gnLCBsaW5lX2NvbG9yPScjOTkxQjFCJywgbmFtZT0nTGltaXRlIEluZmVyaW9yJylcbmZpZy5hZGRfdmxpbmUoeD0yNTAwKzM5LjIsIGxpbmVfZGFzaD0nZGFzaCcsIGxpbmVfY29sb3I9JyM5OTFCMUInLCBuYW1lPSdMaW1pdGUgU3VwZXJpb3InKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0Rpc3RyaWJ1acOnw6NvIGRlIEFtb3N0cmFnZW0gZGEgTcOpZGlhICgkXFxiYXJ7WH0kKScsIHhheGlzX3RpdGxlPSdIb3JhcycsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBhbmFsaXN0YSBmaW5hbmNlaXJvIGRlc2VqYSBlc3RpbWFyIG8gZ2FzdG8gbWVuc2FsIG3DqWRpbyAoJFxcbXUkKSBjb20gYXNzaW5hdHVyYXMgZGUgc2VydmnDp29zIGRlIHN0cmVhbWluZyBwb3IgdXN1w6FyaW8gZW0gdW1hIHBsYXRhZm9ybWEuIEVsZSBzZWxlY2lvbmEgdW1hIGFtb3N0cmEgYWxlYXTDs3JpYSBkZSAkbj0xMDAkIHVzdcOhcmlvcyBlIGVuY29udHJhICRcXGJhcntYfSA9IFJcXCQgNjAsMDAgZSAkUyA9IFJcXCQgMTUsMDAuIFF1YWwgZGFzIGFmaXJtYcOnw7VlcyBhYmFpeG8gbWVsaG9yIGRlc2NyZXZlIGEgaW50ZXJwcmV0YcOnw6NvIGVzdGF0w61zdGljYSBkbyBJbnRlcnZhbG8gZGUgQ29uZmlhbsOnYSBkZSA5NSUgY29uc3RydcOtZG8gYSBwYXJ0aXIgZGVzc2VzIGRhZG9zPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiRXhpc3RlIDk1JSBkZSBwcm9iYWJpbGlkYWRlIGRlIHF1ZSBhIG3DqWRpYSBwb3B1bGFjaW9uYWwgJFxcbXUkIGVzdGVqYSBjb250aWRhIG5vIGludGVydmFsbyBjYWxjdWxhZG8uIiwgIkIiOiAiU2UgY29sZXTDoXNzZW1vcyAxMDAgYW1vc3RyYXMgZGlmZXJlbnRlcywgZXhhdGFtZW50ZSA5NSBkZWxhcyBjb250ZXJpYW0gYSBtw6lkaWEgcG9wdWxhY2lvbmFsICRcXG11JC4iLCAiQyI6ICJPIGludGVydmFsbyBjb25zdHJ1w61kbyBmb3JuZWNlIHVtYSBlc3RpbWF0aXZhIGRlIDk1JSBkZSBjb25maWFuw6dhIGRlIHF1ZSBvIHZhbG9yIGRvIHBhcsOibWV0cm8gJFxcbXUkIGVzdMOhIG5vIGludGVydmFsbyBbNTcsMDY7IDYyLDk0XS4iLCAiRCI6ICJIw6EgOTUlIGRlIGNoYW5jZSBkZSBxdWUgYSBwcsOzeGltYSBtw6lkaWEgYW1vc3RyYWwgY2FsY3VsYWRhIGVzdGVqYSBkZW50cm8gZG8gaW50ZXJ2YWxvIFs1NywwNjsgNjIsOTRdLiIsICJFIjogIk8gdmFsb3IgZGEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQgw6kgb2JyaWdhdG9yaWFtZW50ZSA2MCwwMCwgZSBvIGludGVydmFsbyBzZXJ2ZSBhcGVuYXMgcGFyYSBtZWRpciBhIHZhcmlhw6fDo28gYW1vc3RyYWwuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJPIGNvZWZpY2llbnRlIGRlIGNvbmZpYW7Dp2EgcmVmZXJlLXNlIGFvIG3DqXRvZG8gZGUgY29uc3RydcOnw6NvIGRvIGludGVydmFsbywgbsOjbyDDoCBwcm9iYWJpbGlkYWRlIGRlIHVtIHBhcsOibWV0cm8gZml4byBlc3RhciBkZW50cm8gZGUgdW0gaW50ZXJ2YWxvIGVzcGVjw61maWNvIGrDoSByZWFsaXphZG8uIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGludGVycHJldGHDp8OjbyBjb3JyZXRhIGRlIHVtIElDIGV4aWdlIGNvbXByZWVuZGVyIHF1ZSBvIHBhcsOibWV0cm8gJFxcbXUkIMOpIGZpeG8sIGVucXVhbnRvIG9zIGxpbWl0ZXMgZG8gaW50ZXJ2YWxvIHPDo28gdmFyacOhdmVpcyBhbGVhdMOzcmlhcyBiYXNlYWRhcyBuYSBhbW9zdHJhLiBBIGFsdGVybmF0aXZhIEMgcmVmbGV0ZSBjb3JyZXRhbWVudGUgbyBwcm9jZWRpbWVudG8gZGUgZXN0aW1hw6fDo28sIG9uZGUgdGVtb3MgdW0gbsOtdmVsIGRlIGNvbmZpYW7Dp2EgZGUgOTUlIGFzc29jaWFkbyBhbyBtw6l0b2RvLiBPIGPDoWxjdWxvIGRvcyBsaW1pdGVzIHBhcmEgJFxcZ2FtbWE9MCw5NSQgw6kgJDYwIFxccG0gMSw5NiBcXGNkb3QgKDE1LzEwKSA9IDYwIFxccG0gMiw5NCQsIHJlc3VsdGFuZG8gZW0gWzU3LDA2OyA2Miw5NF0uIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMSwgcC4gMzEyIn0sIHsiZW51bmNpYWRvIjogIlVtYSBhdWRpdG9yaWEgZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlIGVtIHVtYSBsaW5oYSBkZSBtb250YWdlbSBkZSBzZW5zb3JlcyBJb1QgYW5hbGlzb3UgdW1hIGFtb3N0cmEgYWxlYXTDs3JpYSBzaW1wbGVzIGRlIG49NDAwIHVuaWRhZGVzLiBJZGVudGlmaWNhcmFtLXNlIDMyIHBlw6dhcyBjb20gZmFsaGEgZGUgY29uZXjDo28uIERlc2VqYS1zZSBlc3RpbWFyIGEgcHJvcG9yw6fDo28gcG9wdWxhY2lvbmFsIHAgZGUgcGXDp2FzIGRlZmVpdHVvc2FzIGNvbSB1bSBuw612ZWwgZGUgY29uZmlhbsOnYSBkZSA5NSUuIFF1YWwgw6kgbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBjYWxjdWxhZG8gY29ycmV0YW1lbnRlIHBhcmEgYSBwcm9wb3LDp8OjbyBwb3B1bGFjaW9uYWwgcD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIklDKHA7IDAuOTUpID0gWzAuMDY1LCAwLjA5NV0iLCAiQiI6ICJJQyhwOyAwLjk1KSA9IFswLjA1MywgMC4xMDddIiwgIkMiOiAiSUMocDsgMC45NSkgPSBbMC4wNDUsIDAuMTE1XSIsICJEIjogIklDKHA7IDAuOTUpID0gWzAuMDcwLCAwLjA5MF0iLCAiRSI6ICJJQyhwOyAwLjk1KSA9IFswLjAyMCwgMC4xNDBdIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJDYWxjdWxlIHByaW1laXJvIGEgcHJvcG9yw6fDo28gYW1vc3RyYWwgXFxoYXR7cH0gZSBvIGVycm8gcGFkcsOjbyBlc3RpbWFkby4gTGVtYnJlLXNlIHF1ZSBwYXJhIDk1JSBkZSBjb25maWFuw6dhLCBaX3tcXGFscGhhLzJ9IMOpIGFwcm94aW1hZGFtZW50ZSAxLjk2LiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUGFzc28gMTogRGV0ZXJtaW5hciBcXGhhdHtwfSA9IDMyLzQwMCA9IDAuMDguIFBhc3NvIDI6IENhbGN1bGFyIG8gZXJybyBwYWRyw6NvOiBcXHNxcnR7XFxoYXR7cH0oMS1cXGhhdHtwfSkvbn0gPSBcXHNxcnR7MC4wOCgwLjkyKS80MDB9ID0gXFxzcXJ0ezAuMDczNi80MDB9ID0gXFxzcXJ0ezAuMDAwMTg0fSBcXGFwcHJveCAwLjAxMzU2LiBQYXNzbyAzOiBNYXJnZW0gZGUgZXJybyBFID0gMS45NiAqIDAuMDEzNTYgXFxhcHByb3ggMC4wMjY2LiBQYXNzbyA0OiBMaW1pdGVzIGRvIGludGVydmFsbzogMC4wOCBcXHBtIDAuMDI2NiwgcmVzdWx0YW5kbyBlbSBbMC4wNTM0LCAwLjEwNjZdLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpOyBmaWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMC4wNTM0LCAwLjEwNjZdLCB5PVsxLCAxXSwgbW9kZT0nbGluZXMrbWFya2VycycsIG5hbWU9J0ludGVydmFsbyBkZSBDb25maWFuw6dhJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJywgd2lkdGg9MykpKTsgZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkludGVydmFsbyBkZSBDb25maWFuw6dhIHBhcmEgYSBQcm9wb3LDp8OjbzwvYj4nLCB4YXhpcz1kaWN0KHRpdGxlPSdQcm9wb3LDp8OjbyBFc3RpbWFkYSAocCknLCByYW5nZT1bMCwgMC4xNV0pLCB5YXhpcz1kaWN0KHNob3d0aWNrbGFiZWxzPUZhbHNlKSwgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHF1ZSB1bSBwZXNxdWlzYWRvciBkZXNlamEgcmVmaW5hciBhIHByZWNpc8OjbyBkZSB1bSBlc3R1ZG8gc29icmUgYSBwcmVmZXLDqm5jaWEgZGUgY29uc3VtbyBlbSB1bWEgcmVkZSBkZSB2YXJlam8sIHJlZHV6aW5kbyBhIG1hcmdlbSBkZSBlcnJvIHBlbGEgbWV0YWRlLCBtYW50ZW5kbyBvIG1lc21vIG7DrXZlbCBkZSBjb25maWFuw6dhLiBDb20gYmFzZSBuYSBmw7NybXVsYSBkbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBwYXJhIGEgcHJvcG9yw6fDo28gcG9wdWxhY2lvbmFsLCBjb21vIG8gdGFtYW5obyBhbW9zdHJhbCBuIGRldmUgc2VyIGFsdGVyYWRvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyB0YW1hbmhvIGFtb3N0cmFsIG4gZGV2ZSBzZXIgcmVkdXppZG8gw6AgbWV0YWRlLiIsICJCIjogIk8gdGFtYW5obyBhbW9zdHJhbCBuIGRldmUgc2VyIG1hbnRpZG8gaW5hbHRlcmFkby4iLCAiQyI6ICJPIHRhbWFuaG8gYW1vc3RyYWwgbiBkZXZlIHNlciBkdXBsaWNhZG8uIiwgIkQiOiAiTyB0YW1hbmhvIGFtb3N0cmFsIG4gZGV2ZSBzZXIgcXVhZHJ1cGxpY2Fkby4iLCAiRSI6ICJPIHRhbWFuaG8gYW1vc3RyYWwgbiBkZXZlIHNlciBtdWx0aXBsaWNhZG8gcG9yIDguIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkQiLCAiZGljYSI6ICJPYnNlcnZlIGEgcmVsYcOnw6NvIGVudHJlIGEgbWFyZ2VtIGRlIGVycm8gRSBlIG8gZGVub21pbmFkb3IgXFxzcXJ0e259IG5hIGV4cHJlc3PDo28gZGEgbWFyZ2VtIGRlIGVycm8uIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIG1hcmdlbSBkZSBlcnJvIMOpIGRlZmluaWRhIHBvciBFID0gWl97XFxhbHBoYS8yfSAqIFxcc3FydHtcXGhhdHtwfSgxLVxcaGF0e3B9KS9ufS4gUGFyYSBxdWUgRSBzZWphIHJlZHV6aWRvIHBvciB1bSBmYXRvciBkZSAyIChFLzIpLCBvIHRlcm1vIFxcc3FydHtufSBubyBkZW5vbWluYWRvciBkZXZlIHNlciBtdWx0aXBsaWNhZG8gcG9yIDIuIENvbW8gYSByZWxhw6fDo28gw6kgY29tIGEgcmFpeiBxdWFkcmFkYSBkZSBuLCBwcmVjaXNhbW9zIG11bHRpcGxpY2FyIG4gcG9yIDJeMiA9IDQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBsYWJvcmF0w7NyaW8gZGUgZW5nZW5oYXJpYSBkZSBtYXRlcmlhaXMgbmEgVUZCQSwgZGVzZWphLXNlIGVzdGltYXIgYSByZXNpc3TDqm5jaWEgw6AgdHJhw6fDo28gZGUgdW1hIG5vdmEgbGlnYSBtZXTDoWxpY2EuIEZvcmFtIGVuc2FpYWRhcyA2NCBhbW9zdHJhcywgb2J0ZW5kby1zZSB1bSBkZXN2aW8gcGFkcsOjbyBhbW9zdHJhbCAkUyA9IDEyJCBNUGEuIEEgZXF1aXBlIGRlc2VqYSBjb25zdHJ1aXIgdW0gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgZGUgJDk1XFwlJCBwYXJhIGEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQuIENvbnNpZGVyYW5kbyBvIHZhbG9yIGNyw610aWNvICRaX3tcXGFscGhhLzJ9IFxcYXBwcm94IDEuOTYkIHBhcmEgZXN0ZSBuw612ZWwgZGUgY29uZmlhbsOnYSwgcXVhbCDDqSBhIG1hcmdlbSBkZSBlcnJvICRFJCBhc3NvY2lhZGEgYSBlc3RlIGV4cGVyaW1lbnRvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiRSA9IDEuNTAgTVBhIiwgIkIiOiAiRSA9IDIuOTQgTVBhIiwgIkMiOiAiRSA9IDMuMjUgTVBhIiwgIkQiOiAiRSA9IDAuMzc1IE1QYSIsICJFIjogIkUgPSAxLjk2IE1QYSJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgJEVQKFxcYmFye1h9KSQgw6kgZGFkbyBwb3IgJFMvXFxzcXJ0e259JC4gQSBtYXJnZW0gZGUgZXJybyDDqSBvIHByb2R1dG8gZW50cmUgbyB2YWxvciBjcsOtdGljbyAkWl97XFxhbHBoYS8yfSQgZSBvICRFUChcXGJhcntYfSkkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUGFyYSBjYWxjdWxhciBhIG1hcmdlbSBkZSBlcnJvICRFJCwgdXRpbGl6YW1vcyBhIGbDs3JtdWxhICRFID0gWl97XFxhbHBoYS8yfSBcXGNkb3QgXFxmcmFje1N9e1xcc3FydHtufX0kLiBEYWRvczogJFMgPSAxMiQsICRuID0gNjQkIGUgJFpfe1xcYWxwaGEvMn0gPSAxLjk2JC4gUHJpbWVpcm8sIGNhbGN1bGFtb3MgbyBlcnJvIHBhZHLDo286ICRcXGZyYWN7MTJ9e1xcc3FydHs2NH19ID0gXFxmcmFjezEyfXs4fSA9IDEuNSQuIEVtIHNlZ3VpZGEsIG11bHRpcGxpY2Ftb3MgcGVsbyB2YWxvciBjcsOtdGljbzogJDEuOTYgXFxjZG90IDEuNSA9IDIuOTQkLiBQb3J0YW50bywgYSBtYXJnZW0gZGUgZXJybyDDqSBkZSAkMi45NCQgTVBhLCBpbmRpY2FuZG8gcXVlIGEgcHJlY2lzw6NvIGRhIG5vc3NhIGVzdGltYXRpdmEgcG9udHVhbCBwb3NzdWkgZXNzYSBhbXBsaXR1ZGUgZGUgaW5jZXJ0ZXphLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMCwgMV0sIHk9WzAsIDBdLCBtb2RlPSdsaW5lcycsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTIpLCBuYW1lPSdNYXJnZW0gZGUgRXJybycpKVxuZmlnLmFkZF9hbm5vdGF0aW9uKHg9MC41LCB5PTAuMSwgdGV4dD1yJyRFID0gMi45NCQnLCBzaG93YXJyb3c9RmFsc2UsIGZvbnQ9ZGljdChzaXplPTEyLCBjb2xvcj0nIzFFMjkzQicpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J1Zpc3VhbGl6YcOnw6NvIGRhIE1hcmdlbSBkZSBFcnJvJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScsIHhheGlzPWRpY3QocmFuZ2U9Wy0xLCAyXSwgZml4ZWRyYW5nZT1UcnVlKSwgeWF4aXM9ZGljdChyYW5nZT1bLTEsIDFdLCBmaXhlZHJhbmdlPVRydWUpKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkFuYWxpc2UgbyBjb21wb3J0YW1lbnRvIGRhIG1hcmdlbSBkZSBlcnJvICRFJCBlbSB1bSBwcm9qZXRvIGRlIElvVCBvbmRlIHNlIG1lZGUgbyB0ZW1wbyBkZSByZXNwb3N0YSBkZSBzZW5zb3Jlcy4gU2UgYSBnZXLDqm5jaWEgZGVjaWRpciBhdW1lbnRhciBvIG7DrXZlbCBkZSBjb25maWFuw6dhIGRlICQ5MFxcJSQgcGFyYSAkOTlcXCUkLCBtYW50ZW5kbyBvIHRhbWFuaG8gZGEgYW1vc3RyYSAkbiQgZSBvIGRlc3ZpbyBwYWRyw6NvICRTJCBjb25zdGFudGVzLCBvIHF1ZSBvY29ycmVyw6EgY29tIGEgbWFyZ2VtIGRlIGVycm8gJEUkPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBtYXJnZW0gZGUgZXJybyBkaW1pbnVpcsOhLCBwb2lzIG8gcmlnb3IgZXN0YXTDrXN0aWNvIGF1bWVudGEuIiwgIkIiOiAiQSBtYXJnZW0gZGUgZXJybyBwZXJtYW5lY2Vyw6EgY29uc3RhbnRlLCBwb2lzIGRlcGVuZGUgYXBlbmFzIGRhIHZhcmlhYmlsaWRhZGUgZG9zIGRhZG9zIGUgZG8gdGFtYW5obyBhbW9zdHJhbC4iLCAiQyI6ICJBIG1hcmdlbSBkZSBlcnJvIGF1bWVudGFyw6EsIHBvaXMgbyB2YWxvciBjcsOtdGljbyAkWl97XFxhbHBoYS8yfSQgYXNzb2NpYWRvIGEgJDk5XFwlJCDDqSBtYWlvciBxdWUgbyBhc3NvY2lhZG8gYSAkOTBcXCUkLiIsICJEIjogIkEgbWFyZ2VtIGRlIGVycm8gc29mcmVyw6EgdW1hIHJlZHXDp8OjbyBwcm9wb3JjaW9uYWwgYW8gbG9nYXJpdG1vIGRhIGNvbmZpYW7Dp2EuIiwgIkUiOiAiQSBtYXJnZW0gZGUgZXJybyB0b3JuYXLDoS1zZSBpcnJlbGV2YW50ZSBwYXJhIGEgaW50ZXJwcmV0YcOnw6NvIGRvcyByZXN1bHRhZG9zLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiTyBuw612ZWwgZGUgY29uZmlhbsOnYSAkMS1cXGFscGhhJCBkaXRhIG8gdmFsb3IgZGUgJFxcYWxwaGEkLiBRdWFudG8gbWFpb3IgbyBuw612ZWwgZGUgY29uZmlhbsOnYSwgbWVub3IgbyB2YWxvciBkZSAkXFxhbHBoYSQgZSwgY29uc2VxdWVudGVtZW50ZSwgbWFpb3IgbyB2YWxvciBjcsOtdGljbyAkWl97XFxhbHBoYS8yfSQgbmEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBtYXJnZW0gZGUgZXJybyDDqSBkZWZpbmlkYSBwb3IgJEUgPSBaX3tcXGFscGhhLzJ9IFxcY2RvdCBcXGZyYWN7U317XFxzcXJ0e259fSQuIEFvIGF1bWVudGFyIG8gbsOtdmVsIGRlIGNvbmZpYW7Dp2EgZGUgJDkwXFwlJCBwYXJhICQ5OVxcJSQsIG8gdmFsb3IgZGUgJFxcYWxwaGEkIGRpbWludWkgKCQwLjEwJCBwYXJhICQwLjAxJCkuIElzc28gcmVzdWx0YSBlbSB1bSB2YWxvciBjcsOtdGljbyAkWl97XFxhbHBoYS8yfSQgbWFpcyBhZmFzdGFkbyBkYSBtw6lkaWEgKG8gJFokIHBhcmEgJDk5XFwlJCDDqSAkXFxhcHByb3ggMi41OCQsIGVucXVhbnRvIHBhcmEgJDkwXFwlJCDDqSAkXFxhcHByb3ggMS42NDUkKS4gQ29tbyAkWl97XFxhbHBoYS8yfSQgw6kgdW0gbXVsdGlwbGljYWRvciBkaXJldG8gbmEgZsOzcm11bGEsIG8gdmFsb3IgZGUgJEUkIGF1bWVudGEsIHJlZmxldGluZG8gYSBuZWNlc3NpZGFkZSBkZSB1bWEgJ2phbmVsYScgbWFpb3IgcGFyYSBnYXJhbnRpciBjb20gbWFpcyBjZXJ0ZXphIHF1ZSBvIHBhcsOibWV0cm8gJFxcbXUkIGVzdGVqYSBjb250aWRvIG5vIGludGVydmFsby4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH1dLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbeyJlbnVuY2lhZG8iOiAiVW1hIHJlZGUgZGUgc3VwZXJtZXJjYWRvcyBtb25pdG9yYSBvIHZhbG9yIGdhc3RvIHBvciBjbGllbnRlcyBlbSBjb21wcmFzLiBTYWJlLXNlIHF1ZSBhIHBvcHVsYcOnw6NvIHRlbSAkXFxtdSA9IDE1MCQgcmVhaXMgZSAkXFxzaWdtYSA9IDMwJCByZWFpcy4gU2Ugc2VsZWNpb25hcm1vcyB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIGRlICRuPTEwMCQgY2xpZW50ZXMsIGNhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRlIHF1ZSBhIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0kIGVzdGVqYSBlbnRyZSAkMTQ1JCBlICQxNTUkIHJlYWlzLiIsICJkaWNhIjogIlByaW1laXJvLCBkZXRlcm1pbmUgbyBFcnJvIFBhZHLDo28gZGEgTcOpZGlhICRFUChcXGJhcntYfSkgPSBcXHNpZ21hIC8gXFxzcXJ0e259JC4gRW0gc2VndWlkYSwgcGFkcm9uaXplIG9zIGxpbWl0ZXMgdXNhbmRvICRaID0gKFxcYmFye1h9IC0gXFxtdSkgLyBFUChcXGJhcntYfSkkIGUgdXRpbGl6ZSBhIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBwYWRyw6NvLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJJZGVudGlmaWNhw6fDo28gZG9zIHBhcsOibWV0cm9zOiAkXFxtdSA9IDE1MCQsICRcXHNpZ21hID0gMzAkLCAkbiA9IDEwMCQuIiwgIkPDoWxjdWxvIGRvIEVycm8gUGFkcsOjbyBkYSBNw6lkaWE6ICRFUChcXGJhcntYfSkgPSBcXGZyYWN7XFxzaWdtYX17XFxzcXJ0e259fSA9IFxcZnJhY3szMH17XFxzcXJ0ezEwMH19ID0gXFxmcmFjezMwfXsxMH0gPSAzJC4iLCAiUGFkcm9uaXphw6fDo28gZG8gbGltaXRlIGluZmVyaW9yICgkMTQ1JCk6ICRaXzEgPSBcXGZyYWN7MTQ1IC0gMTUwfXszfSA9IFxcZnJhY3stNX17M30gXFxhcHByb3ggLTEuNjckLiIsICJQYWRyb25pemHDp8OjbyBkbyBsaW1pdGUgc3VwZXJpb3IgKCQxNTUkKTogJFpfMiA9IFxcZnJhY3sxNTUgLSAxNTB9ezN9ID0gXFxmcmFjezV9ezN9IFxcYXBwcm94IDEuNjckLiIsICJDw6FsY3VsbyBkYSBwcm9iYWJpbGlkYWRlICRQKC0xLjY3IDwgWiA8IDEuNjcpID0gUChaIDwgMS42NykgLSBQKFogPCAtMS42NykgPSAwLjk1MjUgLSAwLjA0NzUgPSAwLjkwNSQuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTMsIDMsIDEwMClcbnkgPSAoMSAvIG5wLlxcc3FydCgyICogbnAuXFxwaSkpICogbnAuXFxleHAoLTAuNSAqIHgqKjIpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9J04oMCwxKScpKVxuZmlnLmFkZF92cmVjdCh4MD0tMS42NywgeDE9MS42NywgZmlsbGNvbG9yPScjMTBCOTgxJywgb3BhY2l0eT0wLjMsIGxheWVyPSdiZWxvdycsIGxpbmVfd2lkdGg9MClcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5Qcm9iYWJpbGlkYWRlIG5hIERpc3RyaWJ1acOnw6NvIE5vcm1hbDwvYj4nLCB4YXhpc190aXRsZT0nWicsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC45MDV9LCB7ImVudW5jaWFkbyI6ICJVbWEgZW1wcmVzYSBkZSBzb2Z0d2FyZSBkZXNlamEgZXN0aW1hciBvIHRlbXBvIG3DqWRpbyBkZSByZXNwb3N0YSBkZSBzZXVzIHNlcnZpZG9yZXMuIE8gZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsIMOpICRcXHNpZ21hID0gMjBtcyQuIFF1YW50b3Mgc2Vydmlkb3JlcyAoJG4kKSBkZXZlbSBzZXIgYW1vc3RyYWRvcyBwYXJhIHF1ZSBhIG1hcmdlbSBkZSBlcnJvICgkRSQpIGRhIG3DqWRpYSBhbW9zdHJhbCBzZWphLCBubyBtw6F4aW1vLCAkMm1zJCBjb20gOTUlIGRlIGNvbmZpYW7Dp2E/IChDb25zaWRlcmUgJFpfe1xcdGV4dHtjcml0fX0gPSAxLjk2JCBwYXJhIDk1JSBkZSBjb25maWFuw6dhKS4iLCAiZGljYSI6ICJBIG1hcmdlbSBkZSBlcnJvICRFJCDDqSBkZWZpbmlkYSBjb21vICRFID0gWl97XFx0ZXh0e2NyaXR9fSBcXGNkb3QgXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0kLiBJc29sZSBvIHRlcm1vICRuJCBuYSBlcXVhw6fDo28gcGFyYSBlbmNvbnRyYXIgbyB0YW1hbmhvIGFtb3N0cmFsIG5lY2Vzc8OhcmlvLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJGw7NybXVsYSBkYSBtYXJnZW0gZGUgZXJybzogJEUgPSBaX3tcXHRleHR7Y3JpdH19IFxcY2RvdCBcXGZyYWN7XFxzaWdtYX17XFxzcXJ0e259fSQuIiwgIklzb2xhbmRvICRuJDogJFxcc3FydHtufSA9IFpfe1xcdGV4dHtjcml0fX0gXFxjZG90IFxcZnJhY3tcXHNpZ21hfXtFfSBcXGltcGxpZXMgbiA9IFxcbGVmdCggWl97XFx0ZXh0e2NyaXR9fSBcXGNkb3QgXFxmcmFje1xcc2lnbWF9e0V9IFxccmlnaHQpXjIkLiIsICJTdWJzdGl0dWnDp8OjbyBkb3MgdmFsb3JlczogJG4gPSBcXGxlZnQoIDEuOTYgXFxjZG90IFxcZnJhY3syMH17Mn0gXFxyaWdodCleMiQuIiwgIkPDoWxjdWxvOiAkbiA9ICgxLjk2IFxcY2RvdCAxMCleMiA9IDE5LjZeMiQuIiwgIlJlc3VsdGFkbzogJG4gPSAzODQuMTYkLiBDb21vIG8gdGFtYW5obyBhbW9zdHJhbCBkZXZlIHNlciBpbnRlaXJvLCBhcnJlZG9uZGFtb3MgcGFyYSAkMzg1JCBzZXJ2aWRvcmVzLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMzg1LjB9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgw7N0aWNhIGRhIGluZmVyw6puY2lhIGFzc2ludMOzdGljYSwgbyBlZmVpdG8gZGUgcXVhZHJ1cGxpY2FyIG8gdGFtYW5obyBkYSBhbW9zdHJhICRuJCBubyBFcnJvIFBhZHLDo28gZGEgTcOpZGlhICRFUChcXGJhcntYfSkkLiBDb21vIGlzc28gYWx0ZXJhIGEgcHJlY2lzw6NvIGRhIG5vc3NhIGVzdGltYXRpdmEgcG9udHVhbCAkXFxiYXJ7WH0kIGVtIHJlbGHDp8OjbyBhbyBwYXLDom1ldHJvIHBvcHVsYWNpb25hbCAkXFxtdSQ/IiwgImRpY2EiOiAiQ29uc2lkZXJlIGEgcmVsYcOnw6NvIG1hdGVtw6F0aWNhICRFUChcXGJhcntYfSkgPSBcXHNpZ21hIC8gXFxzcXJ0e259JC4gQW5hbGlzZSBvIGRlbm9taW5hZG9yIHF1YW5kbyAkbiQgc2UgdG9ybmEgJDRuJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiU2VqYSBvIGVycm8gcGFkcsOjbyBvcmlnaW5hbCAkRVBfMSA9IFxcc2lnbWEgLyBcXHNxcnR7bn0kLiIsICJDb20gYSBub3ZhIGFtb3N0cmEgJG4nID0gNG4kLCBvIG5vdm8gZXJybyBwYWRyw6NvIMOpICRFUF8yID0gXFxmcmFje1xcc2lnbWF9e1xcc3FydHs0bn19JC4iLCAiU2ltcGxpZmljYcOnw6NvOiAkRVBfMiA9IFxcZnJhY3tcXHNpZ21hfXsyXFxzcXJ0e259fSA9IFxcZnJhY3sxfXsyfSBcXGNkb3QgRVBfMSQuIiwgIkNvbmNsdXPDo286IFF1YWRydXBsaWNhciBhIGFtb3N0cmEgcmVkdXogbyBlcnJvIHBhZHLDo28gcGVsYSBtZXRhZGUuIiwgIkltcGxpY2HDp8OjbzogVW1hIHJlZHXDp8OjbyBubyBlcnJvIHBhZHLDo28gc2lnbmlmaWNhIHF1ZSBhIGRpc3RyaWJ1acOnw6NvIGRlICRcXGJhcntYfSQgdG9ybmEtc2UgbWFpcyBjb25jZW50cmFkYSBlbSB0b3JubyBkZSAkXFxtdSQsIGF1bWVudGFuZG8gYSBwcmVjaXPDo28gZGEgZXN0aW1hdGl2YS4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbm5fdmFsdWVzID0gbnAuYXJyYXkoWzEwLCA0MCwgMTYwXSlcbmVwID0gMTAgLyBucC5cXHNxcnQobl92YWx1ZXMpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1uX3ZhbHVlcywgeT1lcCwgbW9kZT0nbGluZXMrbWFya2VycycsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTMpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5EZWNhaW1lbnRvIGRvIEVycm8gUGFkcsOjbyBjb20gbyBBdW1lbnRvIGRlICRuJDwvYj4nLCB4YXhpc190aXRsZT0nVGFtYW5obyBBbW9zdHJhbCAoJG4kKScsIHlheGlzX3RpdGxlPSdFcnJvIFBhZHLDo28gKCRFUChcXGJhcntYfSkkKScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIHNvYnJlIG8gY29uc3VtbyBkZSBjb21idXN0w612ZWwgZGUgdW0gbm92byBtb3RvciBkZSBjb21idXN0w6NvIGludGVybmEsIHVtYSBhbW9zdHJhIGRlICRuPTE2OSQgdGVzdGVzIHJldmVsb3UgdW0gY29uc3VtbyBtw6lkaW8gZGUgJFxcYmFye1h9ID0gMTIsNSQga20vbCwgY29tIHVtIGRlc3ZpbyBwYWRyw6NvIGFtb3N0cmFsICRTID0gMiw2JCBrbS9sLiBDYWxjdWxlIG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgZGUgOTklIHBhcmEgbyBjb25zdW1vIG3DqWRpbyBwb3B1bGFjaW9uYWwgJFxcbXUkLiBBcHJlc2VudGUgbyB2YWxvciBjcsOtdGljbyAkWl97XFx0ZXh0e2NyaXR9fSQgdXRpbGl6YWRvIGUganVzdGlmaXF1ZSBhIGVzY29saGEgcGVsYSBkaXN0cmlidWnDp8OjbyBub3JtYWwuIiwgImRpY2EiOiAiQ29tbyBvIHRhbWFuaG8gZGEgYW1vc3RyYSDDqSAkbj0xNjkkIChncmFuZGUsICRuIFxcZ3Ryc2ltIDEwMCQpLCB1dGlsaXphbW9zIG8gdmFsb3IgY3LDrXRpY28gZGEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIHBhZHLDo28gJFpfe1xcYWxwaGEvMn0kIHBhcmEgbyBuw612ZWwgZGUgY29uZmlhbsOnYSBzb2xpY2l0YWRvLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBJZGVudGlmaWNhciBvcyBwYXLDom1ldHJvczogJG49MTY5JCwgJFxcYmFye1h9PTEyLDUkLCAkUz0yLDYkIGUgJFxcZ2FtbWE9MCw5OSQuIiwgIjIuIE7DrXZlbCBkZSBzaWduaWZpY8OibmNpYTogJFxcYWxwaGEgPSAxIC0gMCw5OSA9IDAsMDEkLCBsb2dvICRcXGFscGhhLzIgPSAwLDAwNSQuIiwgIjMuIFZhbG9yIGNyw610aWNvOiAkel97MCwwMDV9IFxcYXBwcm94IDIsNTc2JC4iLCAiNC4gRXJybyBQYWRyw6NvOiAkRVAoXFxiYXJ7WH0pID0gUyAvIFxcc3FydHtufSA9IDIsNiAvIFxcc3FydHsxNjl9ID0gMiw2IC8gMTMgPSAwLDIkLiIsICI1LiBNYXJnZW0gZGUgRXJybzogJEUgPSAyLDU3NiBcXGNkb3QgMCwyID0gMCw1MTUyJC4iLCAiNi4gSW50ZXJ2YWxvOiAkSUMoXFxtdTsgMCw5OSkgPSBbMTIsNSAtIDAsNTE1MjsgMTIsNSArIDAsNTE1Ml0gPSBbMTEsOTg0ODsgMTMsMDE1Ml0kLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMTEuOTg0OH0sIHsiZW51bmNpYWRvIjogIlVtIHBlc3F1aXNhZG9yIGRhIMOhcmVhIGRlIHNhw7pkZSBww7pibGljYSBlc3TDoSBlc3R1ZGFuZG8gbyB0ZW1wbyBtw6lkaW8gKCRcXG11JCkgZGUgZXNwZXJhIGVtIHVtYSB1bmlkYWRlIGRlIGVtZXJnw6puY2lhLiBFbGUgZGVzZWphIHF1ZSBvIGVycm8gYW1vc3RyYWwgbcOheGltbyAoJEUkKSBuw6NvIHVsdHJhcGFzc2UgMiBtaW51dG9zLCBjb20gdW0gbsOtdmVsIGRlIGNvbmZpYW7Dp2EgZGUgOTUlLiBTYWJlbmRvIHF1ZSB1bWEgYW1vc3RyYSBwaWxvdG8gZGUgdGFtYW5obyAkbj0yNSQgYXByZXNlbnRvdSB1bSBkZXN2aW8gcGFkcsOjbyBhbW9zdHJhbCAkUz0xMCQgbWludXRvcywgZGV0ZXJtaW5lIHF1YWwgbyB0YW1hbmhvIGRhIGFtb3N0cmEgJG4kIG5lY2Vzc8OhcmlvIHBhcmEgYXRlbmRlciBhb3MgcmVxdWlzaXRvcyBkbyBlc3R1ZG8uIiwgImRpY2EiOiAiVXRpbGl6ZSBhIGbDs3JtdWxhIGRvIGVycm8gbcOheGltbyAkRSA9IHpfe1xcYWxwaGEvMn0gXFxjZG90IFxcZnJhY3tTfXtcXHNxcnR7bn19JCBwYXJhIGlzb2xhciAkbiQsIGFzc3VtaW5kbyBxdWUgJFMkIMOpIHVtYSBlc3RpbWF0aXZhIHJvYnVzdGEgZG8gZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBSZXF1aXNpdG9zOiAkRT0yJCwgJFM9MTAkLCAkel97MCwwMjV9PTEsOTYkLiIsICIyLiBGw7NybXVsYTogJG4gPSAoel97XFxhbHBoYS8yfSBcXGNkb3QgUyAvIEUpXjIkLiIsICIzLiBTdWJzdGl0dWnDp8OjbzogJG4gPSAoMSw5NiBcXGNkb3QgMTAgLyAyKV4yID0gKDEsOTYgXFxjZG90IDUpXjIkLiIsICI0LiBDw6FsY3VsbzogJG4gPSAoOSw4KV4yID0gOTYsMDQkLiIsICI1LiBDb25jbHVzw6NvOiBBcnJlZG9uZGFtb3Mgc2VtcHJlIHBhcmEgbyBwcsOzeGltbyBpbnRlaXJvIHBhcmEgZ2FyYW50aXIgbyBlcnJvIG3DoXhpbW86ICRuID0gOTckLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBDYXAgMTAsIHAuIDI4OSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDk3LjB9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgZG8gcG9udG8gZGUgdmlzdGEgZGEgaW5mZXLDqm5jaWEgZXN0YXTDrXN0aWNhLCBwb3IgcXVlIGEgc3Vic3RpdHVpw6fDo28gZGUgJFxcc2lnbWEkIChkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwpIHBvciAkUyQgKGRlc3ZpbyBwYWRyw6NvIGFtb3N0cmFsKSDDqSBjb25zaWRlcmFkYSB1bWEgZm9udGUgZGUgaW5jZXJ0ZXphIGFkaWNpb25hbCBhbyBlc3RpbWFybW9zIGEgbcOpZGlhICRcXG11JCBlbSBhbW9zdHJhcyBwZXF1ZW5hcy4gUG9yIHF1ZSBlc3NhIHByZW9jdXBhw6fDo28gw6kgYXRlbnVhZGEgcXVhbmRvICRuIFxcZ3Ryc2ltIDEwMCQ/IiwgImRpY2EiOiAiUmVmbGl0YSBzb2JyZSBhIHZhcmlhYmlsaWRhZGUgaW50csOtbnNlY2EgZGUgJFMkIGUgc3VhIGNvbnZlcmfDqm5jaWEgcGFyYSAkXFxzaWdtYSQgcGVsbyBUZW9yZW1hIExpbWl0ZSBDZW50cmFsIGUgcGVsYSBMZWkgZG9zIEdyYW5kZXMgTsO6bWVyb3MuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuICRcXHNpZ21hJCDDqSB1bSBwYXLDom1ldHJvIGZpeG8sIGVucXVhbnRvICRTJCDDqSB1bWEgdmFyacOhdmVsIGFsZWF0w7NyaWEgZGVwZW5kZW50ZSBkYSBhbW9zdHJhLiIsICIyLiBPIHVzbyBkZSAkUyQgaW50cm9kdXogdW1hIHZhcmlhYmlsaWRhZGUgZXh0cmEsIHBvaXMgJFMkIHBvZGUgZmx1dHVhciBkZSB1bWEgYW1vc3RyYSBwYXJhIG91dHJhLCBhbHRlcmFuZG8gYSBsYXJndXJhIGRvIGludGVydmFsby4iLCAiMy4gRW0gYW1vc3RyYXMgcGVxdWVuYXMsIGVzc2EgaW5jZXJ0ZXphIHJlcXVlciBvIHVzbyBkYSBkaXN0cmlidWnDp8OjbyAkdCQgZGUgU3R1ZGVudCBwYXJhIGNvbXBlbnNhciBvICdwZXNvJyBkYXMgY2F1ZGFzLiIsICI0LiBQYXJhICRuJCBncmFuZGUsIGEgTGVpIGRvcyBHcmFuZGVzIE7Dum1lcm9zIGdhcmFudGUgcXVlICRTXjIkIGNvbnZpcmphIHBhcmEgJFxcc2lnbWFeMiQsIGUgYSBlc3RhdMOtc3RpY2EgcGFkcm9uaXphZGEgYXByb3hpbWEtc2UgZGEgTm9ybWFsLCB0b3JuYW5kbyBhIGluY2VydGV6YSBtYXJnaW5hbCBkZXNwcmV6w612ZWwuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZW5zYWlvIGNsw61uaWNvIHBhcmEgdGVzdGFyIGEgZWZpY8OhY2lhIGRlIHVtIG5vdm8gZsOhcm1hY28sIGRlIHVtYSBhbW9zdHJhIGRlIG49MjAwIHBhY2llbnRlcywgMTQwIGFwcmVzZW50YXJhbSBtZWxob3JhIGNsw61uaWNhIHNpZ25pZmljYXRpdmEuIENhbGN1bGUgbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBkZSA5OSUgcGFyYSBhIHByb3BvcsOnw6NvIHBvcHVsYWNpb25hbCBwIGRlIHBhY2llbnRlcyBxdWUgYXByZXNlbnRhbSBtZWxob3JhIGNvbSBvIG5vdm8gZsOhcm1hY28uIENvbnNpZGVyZSBaX3swLjAwNX0gPSAyLjU3Ni4iLCAiZGljYSI6ICJVdGlsaXplIGEgZsOzcm11bGE6IElDKHA7IDEtXFxhbHBoYSkgPSBcXGhhdHtwfSBcXHBtIFpfe1xcYWxwaGEvMn0gXFxzcXJ0e1xcaGF0e3B9KDEtXFxoYXR7cH0pL259LiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBDYWxjdWxhbW9zIGEgcHJvcG9yw6fDo28gYW1vc3RyYWw6IFxcaGF0e3B9ID0gMTQwIC8gMjAwID0gMC43MC4iLCAiMi4gQ2FsY3VsYW1vcyBvIGNvbXBsZW1lbnRvIGRhIHByb3BvcsOnw6NvOiAxIC0gXFxoYXR7cH0gPSAwLjMwLiIsICIzLiBDYWxjdWxhbW9zIG8gZXJybyBwYWRyw6NvOiBcXHNxcnR7KDAuNzAgKiAwLjMwKSAvIDIwMH0gPSBcXHNxcnR7MC4yMSAvIDIwMH0gPSBcXHNxcnR7MC4wMDEwNX0gXFxhcHByb3ggMC4wMzI0LiIsICI0LiBDYWxjdWxhbW9zIGEgbWFyZ2VtIGRlIGVycm8gRSA9IDIuNTc2ICogMC4wMzI0IFxcYXBwcm94IDAuMDgzNS4iLCAiNS4gTyBpbnRlcnZhbG8gw6kgWzAuNzAgLSAwLjA4MzUsIDAuNzAgKyAwLjA4MzVdID0gWzAuNjE2NSwgMC43ODM1XS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuNjE2NX0sIHsiZW51bmNpYWRvIjogIlVtIGFuYWxpc3RhIGRlIG1lcmNhZG8gcHJlY2lzYSBlc3RpbWFyIGEgcHJvcG9yw6fDo28gZGUgZG9taWPDrWxpb3MgcXVlIHBvc3N1ZW0gZGlzcG9zaXRpdm9zIGRlIGNhc2EgaW50ZWxpZ2VudGUgZW0gdW1hIG1ldHLDs3BvbGUuIEVsZSBkZXNlamEgdW1hIG1hcmdlbSBkZSBlcnJvIEUgZGUgMC4wNCBjb20gOTUlIGRlIGNvbmZpYW7Dp2EuIEFzc3VtaW5kbyB1bWEgcHJvcG9yw6fDo28gY29uc2VydmFkb3JhIGRlIFxcaGF0e3B9ID0gMC41MCwgcXVhbCBkZXZlIHNlciBvIHRhbWFuaG8gYW1vc3RyYWwgbiBuZWNlc3PDoXJpbz8iLCAiZGljYSI6ICJSZW9yZ2FuaXplIGEgZsOzcm11bGEgZGEgbWFyZ2VtIGRlIGVycm8gcGFyYSBpc29sYXIgbjogRSA9IFpfe1xcYWxwaGEvMn0gXFxzcXJ0e1xcaGF0e3B9KDEtXFxoYXR7cH0pL259IFxcaW1wbGllcyBuID0gWl97XFxhbHBoYS8yfV4yICogXFxoYXR7cH0oMS1cXGhhdHtwfSkgLyBFXjIuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIElkZW50aWZpY2Ftb3Mgb3MgZGFkb3M6IEUgPSAwLjA0LCBcXGhhdHtwfSA9IDAuNTAsIFpfezAuMDI1fSA9IDEuOTYuIiwgIjIuIEFwbGljYW1vcyBhIGbDs3JtdWxhIGRlIHRhbWFuaG8gYW1vc3RyYWw6IG4gPSAoMS45Nl4yICogMC41MCAqIDAuNTApIC8gMC4wNF4yLiIsICIzLiBSZWFsaXphbW9zIG8gY8OhbGN1bG86IG4gPSAoMy44NDE2ICogMC4yNSkgLyAwLjAwMTYuIiwgIjQuIG4gPSAwLjk2MDQgLyAwLjAwMTYgPSA2MDAuMjUuIiwgIjUuIENvbW8gbyB0YW1hbmhvIGFtb3N0cmFsIGRldmUgc2VyIHVtIG7Dum1lcm8gaW50ZWlybywgYXJyZWRvbmRhbW9zIHBhcmEgY2ltYTogbiA9IDYwMS4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKCk7IGZpZy5hZGRfdHJhY2UoZ28uQmFyKHg9WydUYW1hbmhvIEFtb3N0cmFsJ10sIHk9WzYwMV0sIG1hcmtlcl9jb2xvcj0nIzEwQjk4MScpKTsgZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPlRhbWFuaG8gQW1vc3RyYWwgTmVjZXNzw6FyaW8gKG4pPC9iPicsIHlheGlzPWRpY3QodGl0bGU9J24nKSwgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiA2MDEuMH0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCBzb2IgYSBsdXogZG8gVGVvcmVtYSBkbyBMaW1pdGUgQ2VudHJhbCAoVExDKSwgcG9yIHF1ZSBhIGFwcm94aW1hw6fDo28gZGEgZGlzdHJpYnVpw6fDo28gYmlub21pYWwgcGVsYSBub3JtYWwgw6kgdsOhbGlkYSBwYXJhIGdyYW5kZXMgYW1vc3RyYXMgbmEgY29uc3RydcOnw6NvIGRlIGludGVydmFsb3MgZGUgY29uZmlhbsOnYSBwYXJhIHAgZSBxdWFpcyBzw6NvIG9zIHJpc2NvcyB0ZcOzcmljb3MgZGUgdXRpbGl6YXIgZXN0ZSBtw6l0b2RvIHF1YW5kbyBcXGhhdHtwfSBlc3TDoSBtdWl0byBwcsOzeGltbyBkZSAwIG91IDEuIiwgImRpY2EiOiAiQ29uc2lkZXJlIHF1ZSBhIHZhcmnDom5jaWEgZGEgYmlub21pYWwgbnAoMS1wKSBkZXBlbmRlIGRpcmV0YW1lbnRlIGRhIHByb3BvcsOnw6NvIHAuIE8gcXVlIGFjb250ZWNlIGNvbSBlc3NhIHZhcmnDom5jaWEgcXVhbmRvIHAgc2UgYXByb3hpbWEgZG9zIGV4dHJlbW9zPyIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBPIFRMQyBnYXJhbnRlIHF1ZSBhIHNvbWEgZGUgdmFyacOhdmVpcyBhbGVhdMOzcmlhcyBpbmRlcGVuZGVudGVzIGUgaWRlbnRpY2FtZW50ZSBkaXN0cmlidcOtZGFzIHRlbmRlIGEgdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBjb25mb3JtZSBuIGNyZXNjZS4iLCAiMi4gQ29tbyBhIHByb3BvcsOnw6NvIGFtb3N0cmFsIFxcaGF0e3B9IMOpIHVtYSBtw6lkaWEgZGUgdmFyacOhdmVpcyBkZSBCZXJub3VsbGksIHN1YSBkaXN0cmlidWnDp8OjbyBhbW9zdHJhbCB0ZW5kZSBhIE4ocCwgcCgxLXApL24pLiIsICIzLiBBIHZhbGlkYWRlIGRvIGludGVydmFsbyBkZXBlbmRlIGRhIHNpbWV0cmlhIGRhIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBlbSB0b3JubyBkZSBcXGhhdHtwfS4iLCAiNC4gUXVhbmRvIFxcaGF0e3B9IFxcYXBwcm94IDAgb3UgXFxoYXR7cH0gXFxhcHByb3ggMSwgYSBkaXN0cmlidWnDp8OjbyBiaW5vbWlhbCB0b3JuYS1zZSBhbHRhbWVudGUgYXNzaW3DqXRyaWNhLCBvIHF1ZSB2aW9sYSBhIHN1cG9zacOnw6NvIGRlIHNpbWV0cmlhIG5lY2Vzc8OhcmlhIHBhcmEgcXVlIG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgcGFkcsOjbyBkZSBXYWxkIHNlamEgcm9idXN0by4iLCAiNS4gQ29uc2VxdWVudGVtZW50ZSwgcGFyYSB2YWxvcmVzIGV4dHJlbW9zLCBvIGludGVydmFsbyBwb2RlIGFwcmVzZW50YXIgdW1hIGNvYmVydHVyYSByZWFsIGluZmVyaW9yIGFvIG7DrXZlbCBkZSBjb25maWFuw6dhIDEtXFxhbHBoYSBub21pbmFsIHByZXRlbmRpZG8uIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZW5zYWlvIGNsw61uaWNvLCBvIHRlbXBvIGRlIHJlYcOnw6NvIGEgdW0gbm92byBmw6FybWFjbyBlbSAxMDAgcGFjaWVudGVzIGFwcmVzZW50b3UgdW0gZGVzdmlvIHBhZHLDo28gYW1vc3RyYWwgJFMgPSAwLjUkIHNlZ3VuZG9zLiBDYWxjdWxlIGEgbWFyZ2VtIGRlIGVycm8gJEUkIHBhcmEgdW0gbsOtdmVsIGRlIGNvbmZpYW7Dp2EgZGUgJDk1XFwlJCAoJFpfe1xcYWxwaGEvMn0gPSAxLjk2JCkgZSBpbnRlcnByZXRlIG8gcmVzdWx0YWRvIHNvYiBhIMOzdGljYSBkYSBwcmVjaXPDo28gZGEgZXN0aW1hdGl2YS4iLCAiZGljYSI6ICJVc2UgYSBmw7NybXVsYSAkRSA9IFpfe1xcYWxwaGEvMn0gXFxjZG90IFxcZnJhY3tTfXtcXHNxcnR7bn19JC4gTyBlcnJvIHBhZHLDo28gw6kgYSBtZWRpZGEgZGUgZGlzcGVyc8OjbyBxdWUgZGl2aWRpbW9zIHBlbGEgcmFpeiBkbyB0YW1hbmhvIGFtb3N0cmFsLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJJZGVudGlmaWNhw6fDo28gZG9zIHBhcsOibWV0cm9zOiAkbiA9IDEwMCQsICRTID0gMC41JCwgJFpfe1xcYWxwaGEvMn0gPSAxLjk2JC4iLCAiQ8OhbGN1bG8gZG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYTogJEVQKFxcYmFye1h9KSA9IFxcZnJhY3tTfXtcXHNxcnR7bn19ID0gXFxmcmFjezAuNX17XFxzcXJ0ezEwMH19ID0gXFxmcmFjezAuNX17MTB9ID0gMC4wNSQuIiwgIkPDoWxjdWxvIGRhIG1hcmdlbSBkZSBlcnJvOiAkRSA9IFpfe1xcYWxwaGEvMn0gXFxjZG90IEVQKFxcYmFye1h9KSA9IDEuOTYgXFxjZG90IDAuMDUkLiIsICJSZXN1bHRhZG8gZmluYWw6ICRFID0gMC4wOTgkIHNlZ3VuZG9zLiIsICJJbnRlcnByZXRhw6fDo286IENvbSA5NSUgZGUgY29uZmlhbsOnYSwgbyBlcnJvIG3DoXhpbW8gYWNlaXTDoXZlbCBuYSBlc3RpbWF0aXZhIGRhIG3DqWRpYSBwb3B1bGFjaW9uYWwgZG8gdGVtcG8gZGUgcmVhw6fDo28gw6kgZGUgMC4wOTggc2VndW5kb3MuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjA5OH0sIHsiZW51bmNpYWRvIjogIlVtIGVuZ2VuaGVpcm8gZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlIHByZWNpc2EgcXVlIGEgbWFyZ2VtIGRlIGVycm8gJEUkIGRlIHVtIHByb2Nlc3NvIGRlIHBlc2FnZW0gc2VqYSBkZSBubyBtw6F4aW1vICQwLjIkIGdyYW1hcy4gU2FiZW5kbyBxdWUgbyBkZXN2aW8gcGFkcsOjbyBoaXN0w7NyaWNvICRTJCDDqSBkZSAkMS4wJCBncmFtYSBlIGRlc2VqYW5kbyB1bSBuw612ZWwgZGUgY29uZmlhbsOnYSBkZSAkOTVcXCUkICgkWl97XFxhbHBoYS8yfSA9IDEuOTYkKSwgZGV0ZXJtaW5lIG8gdGFtYW5obyBtw61uaW1vIGRhIGFtb3N0cmEgJG4kIG5lY2Vzc8OhcmlvIHBhcmEgYXRlbmRlciBhIGVzc2UgcmVxdWlzaXRvIGRlIHByZWNpc8Ojby4iLCAiZGljYSI6ICJJc29sZSAkbiQgbmEgZsOzcm11bGEgZGEgbWFyZ2VtIGRlIGVycm86ICRFID0gWl97XFxhbHBoYS8yfSBcXGNkb3QgXFxmcmFje1N9e1xcc3FydHtufX0gXFxSaWdodGFycm93IFxcc3FydHtufSA9IFxcZnJhY3taX3tcXGFscGhhLzJ9IFxcY2RvdCBTfXtFfSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhcnRpbmRvIGRlICRFID0gWl97XFxhbHBoYS8yfSBcXGNkb3QgXFxmcmFje1N9e1xcc3FydHtufX0kLCBpc29sYW1vcyAkbiQ6ICRcXHNxcnR7bn0gPSBcXGZyYWN7Wl97XFxhbHBoYS8yfSBcXGNkb3QgU317RX0kLiIsICJFbGV2YW5kbyBhbWJvcyBvcyBsYWRvcyBhbyBxdWFkcmFkbzogJG4gPSBcXGxlZnQoIFxcZnJhY3taX3tcXGFscGhhLzJ9IFxcY2RvdCBTfXtFfSBcXHJpZ2h0KV4yJC4iLCAiU3Vic3RpdHVpbmRvIG9zIHZhbG9yZXM6ICRuID0gXFxsZWZ0KCBcXGZyYWN7MS45NiBcXGNkb3QgMS4wfXswLjJ9IFxccmlnaHQpXjIkLiIsICJDYWxjdWxhbmRvIG8gdGVybW8gaW50ZXJubzogJFxcZnJhY3sxLjk2fXswLjJ9ID0gOS44JC4iLCAiQ8OhbGN1bG8gZmluYWw6ICRuID0gKDkuOCleMiA9IDk2LjA0JC4iLCAiQ29uY2x1c8OjbzogQ29tbyBvIHRhbWFuaG8gYW1vc3RyYWwgZGV2ZSBzZXIgdW0gbsO6bWVybyBpbnRlaXJvLCBhcnJlZG9uZGFtb3MgcGFyYSBjaW1hOiAkbiA9IDk3JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDk3LjB9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgYXRyYXbDqXMgZGEgYW7DoWxpc2UgZGEgZXhwcmVzc8OjbyAkRSA9IFpfe1xcYWxwaGEvMn0gXFxjZG90IFxcZnJhY3tTfXtcXHNxcnR7bn19JCwgY29tbyBvIHRhbWFuaG8gZGEgYW1vc3RyYSAoJG4kKSBpbmZsdWVuY2lhIGEgcHJlY2lzw6NvICgkRSQpIGRlIHVtYSBlc3RpbWF0aXZhLiBTZSBvIGVuZ2VuaGVpcm8gZGVzZWphciByZWR1emlyIGEgbWFyZ2VtIGRlIGVycm8gw6AgbWV0YWRlLCBtYW50ZW5kbyBvIG7DrXZlbCBkZSBjb25maWFuw6dhIGluYWx0ZXJhZG8sIGNvbW8gZWxlIGRldmUgYWx0ZXJhciBvIHRhbWFuaG8gYW1vc3RyYWwgJG4kPyIsICJkaWNhIjogIk9ic2VydmUgYSByZWxhw6fDo28gaW52ZXJzYSBlbnRyZSBhIG1hcmdlbSBkZSBlcnJvICRFJCBlIGEgcmFpeiBxdWFkcmFkYSBkbyB0YW1hbmhvIGFtb3N0cmFsICRcXHNxcnR7bn0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBIG1hcmdlbSBkZSBlcnJvICRFJCDDqSBpbnZlcnNhbWVudGUgcHJvcG9yY2lvbmFsIMOgIHJhaXogcXVhZHJhZGEgZGUgJG4kICgkRSBcXHByb3B0byBcXGZyYWN7MX17XFxzcXJ0e259fSQpLiIsICJTZSBkZXNlamFtb3MgcXVlICRFX3tub3ZvfSA9IFxcZnJhY3sxfXsyfSBFX3thbnRpZ299JCwgZW50w6NvICRaX3tcXGFscGhhLzJ9IFxcY2RvdCBcXGZyYWN7U317XFxzcXJ0e25fe25vdm99fX0gPSBcXGZyYWN7MX17Mn0gXFxjZG90IFpfe1xcYWxwaGEvMn0gXFxjZG90IFxcZnJhY3tTfXtcXHNxcnR7bl97YW50aWdvfX19JC4iLCAiQ2FuY2VsYW5kbyBvcyB0ZXJtb3MgY29uc3RhbnRlcyAkWl97XFxhbHBoYS8yfSQgZSAkUyQ6ICRcXGZyYWN7MX17XFxzcXJ0e25fe25vdm99fX0gPSBcXGZyYWN7MX17Mlxcc3FydHtuX3thbnRpZ299fX0kLiIsICJJbnZlcnRlbmRvIGUgZWxldmFuZG8gYW8gcXVhZHJhZG86ICRcXHNxcnR7bl97bm92b319ID0gMlxcc3FydHtuX3thbnRpZ299fSBcXFJpZ2h0YXJyb3cgbl97bm92b30gPSA0bl97YW50aWdvfSQuIiwgIkNvbmNsdXPDo286IFBhcmEgcmVkdXppciBhIG1hcmdlbSBkZSBlcnJvIMOgIG1ldGFkZSwgw6kgbmVjZXNzw6FyaW8gcXVhZHJ1cGxpY2FyIG8gdGFtYW5obyBkYSBhbW9zdHJhLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDEsIDEwMCwgMTAwKVxueSA9IDEgLyBucC5cXHNxcnQoeClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbW9kZT0nbGluZXMnLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0zKSwgbmFtZT0nTWFyZ2VtIGRlIEVycm8gKEUpJykpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nUmVsYcOnw6NvIGVudHJlIEUgZSBUYW1hbmhvIEFtb3N0cmFsIChuKScsIHhheGlzPWRpY3QodGl0bGU9J1RhbWFuaG8gQW1vc3RyYWwgKG4pJyksIHlheGlzPWRpY3QodGl0bGU9J01hcmdlbSBkZSBFcnJvIFJlbGF0aXZhIChFKScpKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH1dfQ==').decode('utf-8'))


    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    
    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo do total de exercícios
    total_mcq = len(dados_exercicios.get("questoes_multipla_escolha", []))
    total_disc = len(dados_exercicios.get("questoes_discursivas", []))
    total_exercicios = total_mcq + total_disc
    
    # Barra de Progresso
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    if total_exercicios > 0:
        progresso = acertos / total_exercicios
        st.progress(progresso)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    st.divider()
    
    # Processamento das questões de múltipla escolha
    st.subheader("📝 Questões de Múltipla Escolha")
    for i, questao in enumerate(dados_exercicios.get("questoes_multipla_escolha", [])):
        st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
        
        # Referência bibliográfica
        ref = questao.get("referencia_livro")
        if ref:
            st.markdown(f"📖 *Referência: {ref}*")
    
        # Plotly Dinâmico
        codigo_fig = questao.get("codigo_plotly")
        if codigo_fig:
            try:
                local_vars = {"go": go, "np": np}
                exec(codigo_fig, globals(), local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
            except Exception as e:
                st.error("Erro ao carregar visualização gráfica.")
    
        # Alternativas
        alternativas = questao.get("alternativas", {})
        escolha = st.radio(
            "Selecione uma opção:",
            options=list(alternativas.keys()),
            format_func=lambda x: f"{x}) {alternativas[x]}",
            key=f"radio_mcq_{i}"
        )
    
        # Botão de Dica
        if st.button("💡 Dica", key=f"dica_mcq_{i}"):
            st.info(questao.get("dica", "Dica indisponível."))
    
        # Verificação
        if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
            if escolha == questao.get("alternativa_correta"):
                st.success("Correto! Muito bem.")
                st.session_state.respostas_certas[f"mcq_{i}"] = True
            else:
                st.error("Resposta incorreta. Tente novamente!")
                st.session_state.respostas_certas[f"mcq_{i}"] = False
            st.rerun()
    
        # Gabarito Comentado
        with st.expander("✅ Ver Gabarito Comentado"):
            st.write(questao.get("gabarito_comentado", "Gabarito indisponível."))
    
    # Processamento das questões discursivas
    st.subheader("✍️ Questões Discursivas e Práticas")
    for i, questao in enumerate(dados_exercicios.get("questoes_discursivas", [])):
        st.markdown(f"**Desafio {i+1}:** {questao.get('enunciado', '')}")
        
        ref = questao.get("referencia_livro")
        if ref:
            st.markdown(f"📖 *Referência: {ref}*")
        
        # Plotly
        codigo_fig = questao.get("codigo_plotly")
        if codigo_fig:
            try:
                local_vars = {"go": go, "np": np}
                exec(codigo_fig, globals(), local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
            except Exception as e:
                st.error("Erro ao carregar visualização gráfica.")
                
        st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
        
        # Validação Numérica ou Qualitativa
        resposta_esperada = questao.get("resposta_numerica_esperada")
        if resposta_esperada is not None:
            user_val = st.number_input("Digite o resultado numérico:", format="%.4f", key=f"num_disc_{i}")
            if st.button("Validar Cálculo", key=f"val_disc_{i}"):
                if abs(user_val - resposta_esperada) <= max(0.01, 0.01 * abs(resposta_esperada)):
                    st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.error("O valor calculado difere do gabarito. Verifique suas contas.")
                    st.session_state.respostas_certas[f"disc_{i}"] = False
                st.rerun()
        else:
            if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                st.session_state.respostas_certas[f"disc_{i}"] = True
                st.rerun()
            else:
                st.session_state.respostas_certas[f"disc_{i}"] = False
    
        if st.button("💡 Dica do Exercício", key=f"dica_disc_{i}"):
            st.info(questao.get("dica", "Dica indisponível."))
            
        with st.expander("✅ Ver Resolução Detalhada"):
            for passo in questao.get("gabarito_passo_a_passo", []):
                st.write(f"- {passo}")
