import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDcgLSBUw7NwaWNvIDcuMTogRGlhZ27Ds3N0aWNvIGUgYm9uZGFkZSBkbyBhanVzdGU6IEFuw6FsaXNlIGRlIHJlc8OtZHVvcyIsICJyZWZlcmVuY2lhc19iaWJsaW9ncmFmaWNhc19maW5haXMiOiBbIkJpc3BvLCBOLiAoVW5pdmVyc2lkYWRlIEZlZGVyYWwgZGEgQmFoaWEpLCBBdWxhIDEzOiBBbsOhbGlzZSBkZSBSZXPDrWR1b3Mgbm8gTVJMUywgcHAuIDItMywgNS05LCAxMS0xMy4iLCAiRmFyYXdheSwgSi4gSi4sIExpbmVhciBNb2RlbHMgd2l0aCBSLCBDYXAgNy4xLCA3LjUsIDcuOCwgcHAuIDEtMiwgNzEtNzMsIDgxLTgyLCA4OC05MS4iXX0=').decode('utf-8'))

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
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Fundamentos da Análise de Resíduos no Modelo Linear")
    
    # Seção Teórica
    st.markdown(r"""
    A modelagem estatística é um exercício de abstração onde buscamos cristalizar estruturas matemáticas sobre fenômenos estocásticos. Quando ajustamos um modelo linear, o sucesso não é definido apenas pelo coeficiente $R^2$, mas pela integridade daquilo que o modelo não consegue explicar.
    """)
    
    st.info(r"Os resíduos, longe de serem apenas 'sobras' numéricas, são as 'pegadas digitais' do processo estocástico subjacente, revelando a validade das premissas fundamentais de um modelo.")
    
    st.markdown(r"""
    Ao analisar os resíduos, buscamos verificar se o comportamento dos erros segue a hipótese de ruído branco. Abaixo, destacamos as principais condições para uma análise diagnóstica robusta:
    - **Ausência de Tendência:** Os resíduos devem estar distribuídos aleatoriamente em torno de zero.
    - **Homocedasticidade:** A variância dos resíduos deve ser constante ao longo dos valores ajustados.
    - **Normalidade:** Em inferências clássicas, os erros devem seguir uma distribuição normal para garantir a validade dos testes $t$ e $F$.
    - **Independência:** Não deve haver correlação serial entre as observações residuais.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Projeção de Resíduos")
    st.markdown(r"A geometria do espaço amostral define o vetor de resíduos como uma projeção ortogonal no complemento do espaço da matriz de design:")
    
    st.latex(r"\hat{\mathbf{e}} = \mathbf{y} - \hat{\mathbf{y}}")
    st.latex(r"\hat{\mathbf{e}} = (\mathbf{I} - \mathbf{H})\mathbf{y}")
    
    st.markdown(r"Onde $\mathbf{H}$ é a matriz chapéu (*hat matrix*). A derivação fundamental demonstra que, se o modelo estiver correto, a esperança do resíduo reflete apenas o erro aleatório:")
    
    st.latex(r"\hat{\mathbf{e}} = (\mathbf{I} - \mathbf{H})(\mathbf{X}\boldsymbol{\beta} + \boldsymbol{\\varepsilon}) = (\mathbf{I} - \mathbf{H})\boldsymbol{\\varepsilon}")
    st.latex(r"\text{Var}(\hat{\mathbf{e}}) = \sigma^2 (\mathbf{I} - \mathbf{H})")
    
    # Simulador Interativo
    st.subheader(r"🎛️ Simulador: Diagnóstico Visual de Resíduos")
    st.markdown(r"Manipule os parâmetros abaixo para observar como a variabilidade e a presença de outliers impactam a estrutura dos resíduos em uma regressão simples.")
    
    col1, col2 = st.columns(2)
    with col1:
        n_points = st.slider(r"Tamanho da Amostra", 10, 100, 30, key=r"n_points_subtopico_1")
        noise_level = st.slider(r"Nível de Ruído", 0.1, 5.0, 1.0, step=0.1, key=r"noise_subtopico_1")
    with col2:
        add_outlier = st.toggle(r"Inserir Outlier Estrutural", key=r"outlier_subtopico_1")
    
    # Lógica do Simulador
    x = np.linspace(0, 10, n_points)
    y = 2 + 1.5 * x + np.random.normal(0, noise_level, n_points)
    if add_outlier:
        y[-1] = y[-1] + 15
    
    slope, intercept, _, _, _ = stats.linregress(x, y)
    y_pred = intercept + slope * x
    residuals = y - y_pred
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Dados Observados', marker=dict(color="#1E3A8A")))
    fig.add_trace(go.Scatter(x=x, y=y_pred, mode='lines', name='Ajuste Linear', line=dict(color="#10B981", width=2)))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Regressão Linear e Resíduos</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B")),
        xaxis=dict(title=dict(text="X", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Y", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True)
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    st.info(f"O modelo atual apresenta uma inclinação de {slope:.2f}. A análise visual dos resíduos permite verificar se o ruído é aleatório (homocedástico) ou se há padrões que exigem transformação de variáveis.")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Teste de Normalidade")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Validação de Normalidade")
        st.markdown(r"Uma empresa de produção industrial ajustou um modelo para prever custos. Realizou-se o teste de Shapiro-Wilk nos resíduos para verificar a premissa de normalidade.")
        st.latex(r"n = 15, \quad W = 0,90673, \quad p\text{-valor} = 0,1207")
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- **Hipótese:** $H_0$ assume que os resíduos seguem uma distribuição normal.")
        st.markdown(r"- **Critério:** Comparar o $p$-valor com o nível de significância $\alpha = 0,05$.")
        st.success(r"Como $0,1207 > 0,05$, não há evidências estatísticas para rejeitar $H_0$. O modelo é adequado quanto à normalidade, garantindo a validade dos testes de inferência subsequentes.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Diagnóstico Visual: Inspeção Gráfica e Pressuposições")
    
    # Introdução Teórica
    st.markdown(r"""
    Na arquitetura da inferência estatística, a construção de um modelo linear não encerra o trabalho do analista no momento em que os coeficientes $\hat{\beta}$ são estimados. A fase diagnóstica é onde validamos a integridade epistemológica do modelo.
    """)
    
    st.info(r"A inspeção visual dos resíduos é o mecanismo mais sensível para detectar falhas estruturais que a álgebra formal, por vezes, oculta.")
    
    st.markdown(r"""
    Ao observarmos a dispersão dos resíduos $\hat{e}_i$ em função dos valores ajustados $\hat{y}_i$, examinamos a manifestação física do componente estocástico, buscando evidências de que o erro residual possui a natureza aleatória pura exigida pela teoria de Gauss-Markov.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Estrutura dos Resíduos")
    
    st.markdown(r"O resíduo é definido pela diferença entre a observação real e a previsão. A variância do resíduo é modulada pela matriz chapéu $H$, que reflete a influência de cada ponto de observação:")
    
    st.latex(r"\text{Var}(\hat{e}_i) = \sigma^2(1 - h_{ii})")
    
    st.markdown(r"A dedução analítica que fundamenta este diagnóstico segue estes passos:")
    st.latex(r"\hat{e}_i = y_i - \mathbf{x}_i^{\top}\hat{\boldsymbol{\beta}}")
    st.latex(r"\mathbb{E}(\hat{e}_i) = \mathbb{E}(y_i) - \mathbf{x}_i^{\top}\mathbb{E}(\hat{\boldsymbol{\beta}}) = 0")
    st.latex(r"\text{Var}(\hat{e}_i) = \sigma^2(1 - h_{ii})")
    
    # Simulador Interativo
    st.subheader(r"⚙️ Diagnostic Plot Visualizer")
    st.markdown(r"Explore como a heterocedasticidade e erros de especificação funcional alteram o comportamento visual dos resíduos.")
    
    col1, col2 = st.columns(2)
    with col1:
        hetero_factor = st.slider(r"Fator de Heterocedasticidade (Funil)", 0.0, 2.0, 0.0, step=0.1, key=r"hetero_subtopico_2")
    with col2:
        curve_factor = st.slider(r"Curvatura (Má Especificação)", -5.0, 5.0, 0.0, step=0.5, key=r"curve_subtopico_2")
    
    # Lógica do Simulador (sem sklearn)
    n_samples = 100
    x = np.linspace(0, 10, n_samples)
    y_hat = 2 * x + 5
    # Cria resíduos com dependência quadrática e variância variável
    residuals = (curve_factor * (x - 5)**2) + np.random.normal(0, 1 + hetero_factor * x, n_samples)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_hat, y=residuals, mode='markers', name=r"Resíduos", marker=dict(color="#1E3A8A")))
    fig.add_hline(y=0, line_dash="dash", line_color="#991B1B")
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Diagnóstico de Resíduos vs Valores Ajustados</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valores Ajustados", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Resíduos", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    # Laudo Dinâmico
    if curve_factor != 0 or hetero_factor > 0.1:
        st.info(r"Diagnóstico: Padrões sistemáticos detectados. A presença de curvatura ou dispersão não constante sugere a necessidade de transformar variáveis ou reespecificar a forma funcional do modelo.")
    else:
        st.success(r"Diagnóstico: Os resíduos apresentam comportamento de 'ruído branco', sugerindo que o modelo linear está bem especificado.")
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática: Logística")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Análise de Logística")
        st.markdown(r"Uma empresa de logística analisa o tempo de entrega $Y$ em função da distância $X$. O gráfico de resíduos vs. valores ajustados mostra uma curvatura parabólica.")
        st.latex(r"\text{Padrão visual: curvatura quadrática nos resíduos}")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Identificação de erro de especificação funcional.")
        st.markdown(r"- Necessidade de incluir o termo $x^2$ na regressão.")
        st.markdown(r"- Nova forma funcional: $Y = \beta_0 + \beta_1 X + \beta_2 X^2 + \varepsilon$.")
        st.success(r"O modelo linear falhou em capturar a aceleração do tempo em relação à distância. A inclusão de um termo quadrático é necessária para corrigir o vício estrutural.")

    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    import streamlit as st
    
    # --- Cabeçalho do Subtópico ---
    st.header(r"Verificação de Normalidade e Ferramentas Inferenciais")
    
    # --- Introdução Teórica ---
    st.markdown(r"""
    A fundamentação da inferência estatística, particularmente no âmbito dos modelos lineares, repousa sobre pilares axiomáticos que permitem a transição do dado observado para a conclusão populacional. Entre estas premissas, a suposição de normalidade dos erros, denotada classicamente como $\varepsilon \sim N(0, \sigma^2)$, ocupa uma posição de centralidade.
    
    Quando estruturamos um modelo de regressão, não estamos apenas ajustando uma linha; estamos postulando um mecanismo gerador de dados onde a variação residual não explicada deve comportar-se como ruído branco gaussiano.
    """)
    
    st.info(r"Sem a normalidade dos erros, especialmente em cenários de pequenas amostras, as distribuições amostrais dos estimadores perdem sua ancoragem, tornando as inferências sobre parâmetros como $\hat{\beta}_1$ desprovidas de validade teórica.")
    
    st.markdown(r"""
    ### 🔍 Diagnóstico e Robustez Estatística
    O papel da verificação de normalidade pode ser resumido em três eixos principais:
    - **Proteção contra Inferências Espúrias:** Evita a aceitação de modelos cujos erros violam a estrutura probabilística necessária para o teste $t$.
    - **Mitigação do Efeito de Pequenas Amostras:** O Teorema Central do Limite garante normalidade assintótica, mas falha quando o tamanho amostral $n$ é restrito.
    - **Validação de Intervalos de Confiança:** Garante que a distribuição $t$ de Student realmente represente o comportamento dos estimadores.
    """)
    
    # --- Formalismo Matemático ---
    st.markdown(r"### 📐 O Formalismo Analítico: Teste de Shapiro-Wilk")
    st.markdown(r"O teste de Shapiro-Wilk é o padrão-ouro para verificar a aderência à normalidade, focando na correlação entre dados e quantis esperados:")
    st.latex(r"W = \frac{(\sum_{i=1}^{n} a_i \hat{e}_{(i)})^2}{\sum_{i=1}^{n} (\hat{e}_i - \bar{\hat{e}})^2}")
    
    st.markdown(r"Os passos analíticos para a determinação desta estatística seguem a lógica:")
    st.latex(r"\hat{e}_{(1)} \le \hat{e}_{(2)} \le \dots \le \hat{e}_{(n)} \text{ (série estatística de ordem)}")
    st.latex(r"SQRes = \sum_{i=1}^{n} (\hat{e}_i - \bar{\hat{e}})^2")
    st.latex(r"W = \frac{(\sum_{i=1}^{n} a_i \hat{e}_{(i)})^2}{SQRes}")
    
    # --- Simulador Interativo ---
    st.markdown(r"### 🧪 Normality Diagnostic Lab")
    col1, col2 = st.columns(2)
    with col1:
        dist_type = st.selectbox(r"Selecione a distribuição dos resíduos", ["Normal", "t de Student (Cauda Pesada)", "Assimétrica"], key="dist_sel_subtopico_3")
        n_samples = st.slider(r"Tamanho da amostra (n)", 10, 100, 30, key="n_slider_subtopico_3")
    with col2:
        show_kde = st.toggle(r"Exibir estimativa de densidade", value=True, key="kde_toggle_subtopico_3")
    
    # Lógica de geração de dados
    if dist_type == "Normal":
        data = np.random.normal(0, 1, n_samples)
    elif dist_type == "t de Student (Cauda Pesada)":
        data = np.random.standard_t(df=3, size=n_samples)
    else:
        data = np.random.exponential(1, n_samples) - 1
    
    shapiro_stat, p_val = stats.shapiro(data)
    
    # Gráfico Plotly
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=data, name=r"Resíduos", marker_color="#1E3A8A", opacity=0.7))
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição Empírica dos Resíduos</b>", font=dict(size=14, color="#1E293B"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valor do Resíduo", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Frequência", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)")
    )
    st.plotly_chart(fig, use_container_width=True, key="plotly_chart_subtopico_3")
    
    # Laudo dinâmico
    status = "Rejeitar H0 (Não normal)" if p_val < 0.05 else "Aceitar H0 (Normal)"
    st.info(f"Resultado do Teste Shapiro-Wilk: Estatística W = {shapiro_stat:.4f} | p-valor = {p_val:.4f}. Decisão: {status}")
    
    # --- Exemplos Práticos ---
    st.markdown(r"### 📈 Casos de Aplicação Prática: Validação de Modelos")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Análise de Resíduos de Regressão")
        st.markdown(r"Dado um modelo onde a estatística $W = 0,90$ e $p\text{-valor} = 0,12$, e fixando $\alpha = 0,05$, avalie a validade das inferências sobre os coeficientes da regressão.")
        st.latex(r"p\text{-valor} = 0,12, \quad \alpha = 0,05")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Comparação do $p\text{-valor}$ com o nível de significância $\alpha$: $0,12 > 0,05$.")
        st.markdown(r"- Aceitação da hipótese nula $H_0$, indicando ausência de evidência contra a normalidade.")
        st.success(r"Como os resíduos seguem uma distribuição normal, as inferências (intervalos de confiança e testes de hipóteses) são estatisticamente válidas.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    st.header(r"Identificação de Observações Não Usuais: Outliers e Pontos de Alavanca")
    
    st.markdown(r"""
    A análise de regressão linear, em sua formulação clássica, pressupõe que as observações contribuem de maneira homogênea para a superfície de resposta. Entretanto, a geometria do espaço amostral dos preditores pode conter pontos que exercem uma influência desproporcional, distorcendo nossas estimativas de $\hat{\beta}_0$ e $\hat{\beta}_1$.
    
    Para mitigar diagnósticos equivocados, distinguimos dois tipos principais de anomalias:
    *   **Pontos de Alavanca:** Observações com valores de $X$ extremos que "forçam" a inclinação da reta de regressão.
    *   **Outliers:** Observações com resíduos de grande magnitude, apresentando valores de $Y$ discrepantes em relação ao modelo ajustado.
    """)
    
    st.info(r"A matriz hat, definida como $\mathbf{H} = \mathbf{X}(\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{X}^\top$, é a ferramenta fundamental para identificar pontos de alavanca. Seus elementos diagonais, $h_{ii}$, quantificam a distância de Mahalanobis de cada ponto em relação à média dos preditores.")
    
    st.markdown(r"### 📐 O Coração Matemático: Dedução e Propriedades")
    
    st.latex(r"\hat{\mathbf{y}} = \mathbf{H}\mathbf{y}")
    st.markdown(r"O vetor de valores ajustados é obtido pela projeção do vetor de resposta original sobre o subespaço gerado pelos preditores.")
    
    st.latex(r"\hat{y}_i = \sum_{j=1}^{n} h_{ij} y_j")
    st.markdown(r"Cada valor ajustado é uma combinação linear das observações de resposta, onde $h_{ij}$ pondera a contribuição de cada $y_j$.")
    
    st.latex(r"\text{Var}(\hat{e}_i) = \sigma^2(1 - h_{ii})")
    st.markdown(r"Esta expressão demonstra que a variabilidade do resíduo é reduzida em pontos de alavanca alta, tornando-os visualmente enganosos em gráficos de diagnóstico.")
    
    st.markdown(r"### 🔍 Critério de Diagnóstico para Alavanca")
    
    st.latex(r"h_{ii} > \frac{2(p+1)}{n}")
    
    st.markdown(r"""
    Este limite prático deriva da propriedade $\sum h_{ii} = p+1$. Quando o valor de $h_{ii}$ supera o dobro da média dos elementos da diagonal, a observação é considerada um ponto de alavanca potencialmente perigoso que exige investigação.
    """)
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Análise de Influência")
        st.markdown(r"Em um estudo com $n=20$ lotes e $p=1$ preditor, um ponto apresentou alavanca $h_{ii} = 0,35$. Verifique se este ponto é influente.")
        st.latex(r"h_{ii} = 0,35, \quad n=20, \quad p=1")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Limite teórico: $\frac{2(1+1)}{20} = \frac{4}{20} = 0,20$.")
        st.markdown(r"- Comparação: $0,35 > 0,20$.")
        st.success(r"O ponto possui alta alavanca. Recomenda-se investigação detalhada pois ele exerce influência desproporcional sobre o ajuste da reta.")
    
    st.markdown(r"### 📊 Simulador de Sensibilidade da Matriz Hat")
    
    col1, col2 = st.columns(2)
    with col1:
        n_obs = st.slider(r"Tamanho da Amostra (n)", 10, 50, 20, key=r"n_subtopico_4")
    with col2:
        p_pred = st.slider(r"Número de Preditores (p)", 1, 5, 1, key=r"p_subtopico_4")
    
    limite = (2 * (p_pred + 1)) / n_obs
    st.markdown(r"O limite de alavanca calculado para este cenário é **{:.3f}**.".format(limite))
    
    # Simulação de dados para o gráfico
    x = np.linspace(0, 10, n_obs)
    h_vals = np.linspace(0.05, 0.4, n_obs) # Valores fictícios de alavanca para visualização
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=np.arange(n_obs), y=h_vals, mode='markers', name='Alavanca Observada', marker=dict(color="#1E3A8A", size=8)))
    fig.add_hline(y=limite, line_dash="dash", line_color="#991B1B", annotation_text="Limite Crítico")
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição de Alavanca (Diagonal da Matriz Hat)</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Índice da Observação", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Valor $h_{ii}$", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")
    
    st.info(f"Com $n={n_obs}$ e $p={p_pred}$, o limiar de alavanca é {limite:.3f}. Observações acima desta linha devem ser tratadas como pontos de alavanca potenciais, capazes de enviesar as estimativas de regressão.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDcgLSBUw7NwaWNvIDcuMTogRGlhZ27Ds3N0aWNvIGUgYm9uZGFkZSBkbyBhanVzdGU6IEFuw6FsaXNlIGRlIHJlc8OtZHVvcyIsICJxdWVzdG9lc19tdWx0aXBsYV9lc2NvbGhhIjogW3siZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBkZSBlbmdlbmhhcmlhIGluZHVzdHJpYWwgc29icmUgbyB0ZW1wbyBkZSBtb250YWdlbSBkZSBjb21wb25lbnRlcyBlbGV0csO0bmljb3MgKCR5JCwgZW0gc2VndW5kb3MpIGVtIGZ1bsOnw6NvIGRhIHZvbHRhZ2VtIGRlIG9wZXJhw6fDo28gKCR4JCwgZW0gdm9sdHMpLCB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgc2ltcGxlcyAkXFxtYXRoYmZ7eX0gPSBcXG1hdGhiZntYfVxcYm9sZHN5bWJvbHtcXGJldGF9ICsgXFxib2xkc3ltYm9se1xcdmFyZXBzaWxvbn0kIGZvaSBhanVzdGFkbyBwYXJhIHVtYSBhbW9zdHJhIGRlICRuPTMwJCB1bmlkYWRlcy4gRHVyYW50ZSBhIGFuw6FsaXNlIGRlIHJlc8OtZHVvcywgdmVyaWZpY291LXNlIHF1ZSBvIGdyw6FmaWNvIGRlIHJlc8OtZHVvcyB2ZXJzdXMgdmFsb3JlcyBhanVzdGFkb3MgKCRcXGhhdHtcXG1hdGhiZnt5fX0kKSBleGliZSB1bWEgZm9ybWEgZGUgZnVuaWwsIG9uZGUgYSBkaXNwZXJzw6NvIGRvcyByZXPDrWR1b3MgYXVtZW50YSBjb25mb3JtZSBvIHZhbG9yIGFqdXN0YWRvIGNyZXNjZS4gUXVhbCBkYXMgcHJlbWlzc2FzIGZ1bmRhbWVudGFpcyBkbyBNb2RlbG8gTGluZWFyIENsw6Fzc2ljbyBmb2kgdmlvbGFkYSBlIHF1YWwgYSBjb25zZXF1w6puY2lhIGltZWRpYXRhIHBhcmEgYSBpbmZlcsOqbmNpYSBiYXNlYWRhIG5lc3RlIG1vZGVsbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgc3Vwb3Npw6fDo28gZGUgaW5kZXBlbmTDqm5jaWEgZm9pIHZpb2xhZGEsIHRvcm5hbmRvIGFzIGVzdGltYXRpdmFzIGRvcyBjb2VmaWNpZW50ZXMgJFxcaGF0e1xcYm9sZHN5bWJvbHtcXGJldGF9fSQgdmllc2FkYXMuIiwgIkIiOiAiQSBzdXBvc2nDp8OjbyBkZSBob21vY2VkYXN0aWNpZGFkZSAodmFyacOibmNpYSBjb25zdGFudGUgZG9zIGVycm9zKSBmb2kgdmlvbGFkYSwgaW52YWxpZGFuZG8gYXMgZXN0YXTDrXN0aWNhcyBkZSB0ZXN0ZSAoJHRfMCQpIGUgb3MgaW50ZXJ2YWxvcyBkZSBjb25maWFuw6dhIGhhYml0dWFpcywgcG9pcyBvcyBlcnJvcyBwYWRyw6NvIGRvcyBjb2VmaWNpZW50ZXMgdG9ybmFtLXNlIGluY29ycmV0b3MuIiwgIkMiOiAiQSBzdXBvc2nDp8OjbyBkZSBub3JtYWxpZGFkZSBmb2kgdmlvbGFkYSwgaW1wZWRpbmRvIG8gdXNvIGRvIGVzdGltYWRvciBkZSBtw61uaW1vcyBxdWFkcmFkb3MgcGFyYSBlbmNvbnRyYXIgb3MgdmFsb3JlcyBkZSAkXFxoYXR7XFxib2xkc3ltYm9se1xcYmV0YX19JC4iLCAiRCI6ICJOw6NvIGhvdXZlIHZpb2xhw6fDo28gZGUgcHJlbWlzc2FzLCBwb2lzIG8gbW9kZWxvIGxpbmVhciBzaW1wbGVzIGFkbWl0ZSBxdWFscXVlciBwYWRyw6NvIGRlIGRpc3BlcnPDo28gbm9zIHJlc8OtZHVvcy4iLCAiRSI6ICJBIG1hdHJpeiBkZSBkZXNlbmhvICRcXG1hdGhiZntYfSQgbsOjbyBwb3NzdWkgcG9zdG8gY29sdW5hIGNvbXBsZXRvLCBpbXBvc3NpYmlsaXRhbmRvIGEgb2J0ZW7Dp8OjbyBkYSBtYXRyaXogJFxcbWF0aGJme0h9JC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgbyBNUkxTIHByZXNzdXDDtWUgZXJyb3MgY29tIG3DqWRpYSB6ZXJvIGUgdmFyacOibmNpYSBjb25zdGFudGUgJFxcc2lnbWFeMiQuIE8gY29tcG9ydGFtZW50byBkZSAnZnVuaWwnIMOpIHVtYSBldmlkw6puY2lhIGdyw6FmaWNhIGNsw6Fzc2ljYSBkZSBoZXRlcm9jZWRhc3RpY2lkYWRlLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBoZXRlcm9jZWRhc3RpY2lkYWRlIG9jb3JyZSBxdWFuZG8gYSB2YXJpw6JuY2lhIGRvcyBlcnJvcyBuw6NvIMOpIGNvbnN0YW50ZSwgb3Ugc2VqYSwgJFZhcihcXHZhcmVwc2lsb25faSkgPSBcXHNpZ21hX2leMiQuIE8gcGFkcsOjbyBkZSAnZnVuaWwnIG5vIGdyw6FmaWNvIGRlIHJlc8OtZHVvcyAoJFxcaGF0e2V9X2kkKSBjb250cmEgb3MgdmFsb3JlcyBhanVzdGFkb3MgKCRcXGhhdHt5fV9pJCkgaW5kaWNhIHF1ZSBhIHZhcmnDom5jaWEgZG9zIHJlc8OtZHVvcyBjcmVzY2UgY29tIGEgbcOpZGlhLiBFbWJvcmEgbyBlc3RpbWFkb3IgZGUgbcOtbmltb3MgcXVhZHJhZG9zIGNvbnRpbnVlIHNlbmRvIG7Do28gdmljaWFkbywgZWxlIGRlaXhhIGRlIHNlciBvIG1lbGhvciBlc3RpbWFkb3IgKE1FTFYgLSBNZWxob3IgRXN0aW1hZG9yIExpbmVhciBWaWVzYWRvKSBlIGFzIGbDs3JtdWxhcyB1c3VhaXMgZGUgdmFyacOibmNpYSBkb3MgY29lZmljaWVudGVzLCBxdWUgZGVwZW5kZW0gZGEgc3Vwb3Npw6fDo28gZGUgaG9tb2NlZGFzdGljaWRhZGUgKCRWYXIoXFxib2xkc3ltYm9se1xcdmFyZXBzaWxvbn0pID0gXFxzaWdtYV4yIFxcbWF0aGJme0l9JCksIHRvcm5hbS1zZSBpbnbDoWxpZGFzLiBDb25zZXF1ZW50ZW1lbnRlLCBvcyB0ZXN0ZXMgJHRfMCQgZSBvcyBpbnRlcnZhbG9zIGRlIGNvbmZpYW7Dp2EgYmFzZWFkb3Mgbm8gZXJybyBwYWRyw6NvIGhhYml0dWFsIG7Do28gc8OjbyBjb25macOhdmVpcy4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9WzEwLCAxMiwgMTUsIDE4LCAyMCwgMjIsIDI1LCAyOCwgMzAsIDMyLCAzNSwgMzgsIDQwXSwgeT1bMSwgLTEsIDIsIC0yLCAzLCAtMywgNCwgLTQsIDUsIC01LCA2LCAtNiwgN10sIG1vZGU9J21hcmtlcnMnLCBuYW1lPSdSZXPDrWR1b3MnLCBtYXJrZXI9ZGljdChjb2xvcj0nIzFFM0E4QScsIHNpemU9OCkpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkdyw6FmaWNvIGRlIFJlc8OtZHVvcyB2cy4gVmFsb3JlcyBBanVzdGFkb3MgKEhldGVyb2NlZGFzdGljaWRhZGUpPC9iPicsIHhheGlzX3RpdGxlPSdWYWxvcmVzIEFqdXN0YWRvcyAoJFxcaGF0e3l9JCknLCB5YXhpc190aXRsZT0nUmVzw61kdW9zICgkXFxoYXR7ZX0kKScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnLCBoZWlnaHQ9NDAwLCBzaG93bGVnZW5kPUZhbHNlKVxuZmlnLnVwZGF0ZV94YXhlcyhmaXhlZHJhbmdlPVRydWUpXG5maWcudXBkYXRlX3lheGVzKGZpeGVkcmFuZ2U9VHJ1ZSkiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgbWF0cmljaWFsICRcXG1hdGhiZnt5fSA9IFxcbWF0aGJme1h9XFxib2xkc3ltYm9se1xcYmV0YX0gKyBcXGJvbGRzeW1ib2x7XFx2YXJlcHNpbG9ufSQgZSBhIG1hdHJpeiBkZSBwcm9qZcOnw6NvICRcXG1hdGhiZntIfSA9IFxcbWF0aGJme1h9KFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfVxcbWF0aGJme1h9XntcXHRvcH0kLiBBIGFsYXZhbmNhIChsZXZlcmFnZSkgZGEgJGkkLcOpc2ltYSBvYnNlcnZhw6fDo28gw6kgZGFkYSBwZWxvIGVsZW1lbnRvIGRpYWdvbmFsICRoX3tpaX0kIGRhIG1hdHJpeiAkXFxtYXRoYmZ7SH0kLiBTZSB1bWEgb2JzZXJ2YcOnw6NvIHBvc3N1aSB1bWEgYWxhdmFuY2EgbXVpdG8gcHLDs3hpbWEgZGUgMSwgbyBxdWUgcG9kZW1vcyBjb25jbHVpciBzb2JyZSBvIHJlc8OtZHVvIGNvcnJlc3BvbmRlbnRlICRcXGhhdHtlfV9pJD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gcmVzw61kdW8gJFxcaGF0e2V9X2kkIHNlcsOhIG11aXRvIGdyYW5kZSwgcG9pcyBvIG1vZGVsbyBuw6NvIGNvbnNlZ3VlIGFqdXN0YXIgYmVtIG9ic2VydmHDp8O1ZXMgY29tIGFsdGEgYWxhdmFuY2EuIiwgIkIiOiAiTyByZXPDrWR1byAkXFxoYXR7ZX1faSQgc2Vyw6EgZm9yw6dhZG8gYSBzZXIgcHLDs3hpbW8gZGUgemVybywgaW5kZXBlbmRlbnRlbWVudGUgZG8gdmFsb3IgZGUgJHlfaSQsIHBvaXMgYSBtYXRyaXogZGUgcHJvamXDp8OjbyAncHV4YScgbyB2YWxvciBhanVzdGFkbyBlbSBkaXJlw6fDo28gYW8gdmFsb3Igb2JzZXJ2YWRvLiIsICJDIjogIk8gcmVzw61kdW8gJFxcaGF0e2V9X2kkIMOpIGluZGVwZW5kZW50ZSBkYSBhbGF2YW5jYSwgZGVwZW5kZW5kbyBhcGVuYXMgZG8gZXJybyBhbGVhdMOzcmlvICRcXHZhcmVwc2lsb25faSQuIiwgIkQiOiAiQSBhbGF2YW5jYSBuw6NvIGFmZXRhIGEgdmFyacOibmNpYSBkbyByZXPDrWR1bywgYXBlbmFzIGEgdmFyacOibmNpYSBkb3MgdmFsb3JlcyBhanVzdGFkb3MuIiwgIkUiOiAiTyByZXPDrWR1byAkXFxoYXR7ZX1faSQgdGVuZGVyw6EgYSBzZXIgaWd1YWwgw6AgdmFyacOibmNpYSBwb3B1bGFjaW9uYWwgJFxcc2lnbWFeMiQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJDb25zaWRlcmUgYSBwcm9wcmllZGFkZSBkYSB2YXJpw6JuY2lhIGRvIHJlc8OtZHVvOiAkVmFyKFxcaGF0e2V9X2kpID0gXFxzaWdtYV4yKDEgLSBoX3tpaX0pJC4gTyBxdWUgYWNvbnRlY2UgY29tIGEgdmFyacOibmNpYSBxdWFuZG8gJGhfe2lpfSBcXHRvIDEkPyIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSB2YXJpw6JuY2lhIGRvIHJlc8OtZHVvIMOpIGRhZGEgcG9yICRWYXIoXFxoYXR7ZX1faSkgPSBcXHNpZ21hXjIoMSAtIGhfe2lpfSkkLiBTZSAkaF97aWl9JCBzZSBhcHJveGltYSBkZSAxLCBhIHZhcmnDom5jaWEgZG8gcmVzw61kdW8gJFxcaGF0e2V9X2kkIHNlIGFwcm94aW1hIGRlIHplcm8uIElzc28gb2NvcnJlIHBvcnF1ZSBvYnNlcnZhw6fDtWVzIGNvbSBhbHRhIGFsYXZhbmNhIHPDo28gcG9udG9zIGluZmx1ZW50ZXMgZW0gJFgkIHF1ZSAnZm9yw6dhbScgYSByZXRhIGRlIHJlZ3Jlc3PDo28gYSBwYXNzYXIgbXVpdG8gcHLDs3hpbWEgZGUgJHlfaSQuIENvbW8gcmVzdWx0YWRvLCBvIG1vZGVsbyBhanVzdGFkbyAkXFxoYXR7eX1faSQgdG9ybmEtc2UgcXVhc2UgaWd1YWwgYW8gdmFsb3Igb2JzZXJ2YWRvICR5X2kkLCBmYXplbmRvIGNvbSBxdWUgbyByZXPDrWR1byByZXN1bHRhbnRlIHNlamEgcGVxdWVubywgbWFzY2FyYW5kbyBwb3RlbmNpYWxtZW50ZSBhIHByZXNlbsOnYSBkZSB1bSBvdXRsaWVyIHZlcmRhZGVpcm8gbmEgdmFyacOhdmVsIHJlc3Bvc3RhLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiRmFyYXdheSwgSi4gSi4sIExpbmVhciBNb2RlbHMgd2l0aCBSLCAybmQgZWQuLCBwLiA3MiJ9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gZGUgZW5nZW5oYXJpYSBpbmR1c3RyaWFsIHNvYnJlIG8gdGVtcG8gZGUgdmlkYSDDunRpbCBkZSBjb21wb25lbnRlcyBlbGV0csO0bmljb3MgZW0gZnVuw6fDo28gZGEgdGVtcGVyYXR1cmEgZGUgb3BlcmHDp8OjbywgdW0gYW5hbGlzdGEgYWp1c3RvdSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgc2ltcGxlcy4gQXDDs3MgYSBvYnRlbsOnw6NvIGRvIG1vZGVsbywgbyBhbmFsaXN0YSBnZXJvdSB1bSBncsOhZmljbyBkZSBkaXNwZXJzw6NvIGRvcyByZXPDrWR1b3MgJFxcaGF0e2V9X2kkIHZlcnN1cyBvcyB2YWxvcmVzIGFqdXN0YWRvcyAkXFxoYXR7eX1faSQuIE8gZ3LDoWZpY28gYXByZXNlbnRvdSB1bSBwYWRyw6NvIG7DrXRpZG8gZGUgJ2Z1bmlsJywgb25kZSBhIGRpc3BlcnPDo28gZG9zIHJlc8OtZHVvcyBhdW1lbnRhIGNvbmZvcm1lIG9zIHZhbG9yZXMgZGUgJFxcaGF0e3l9X2kkIGNyZXNjZW0uIENvbnNpZGVyYW5kbyBvcyBwcmVzc3Vwb3N0b3MgZG8gbW9kZWxvIGxpbmVhciwgcXVhbCDDqSBhIGludGVycHJldGHDp8OjbyBjb3JyZXRhIGRlc3RlIGZlbsO0bWVubz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gbW9kZWxvIGFwcmVzZW50YSBwZXJmZWl0YSBhZGVxdWHDp8OjbywgcG9pcyBvIGF1bWVudG8gZGEgZGlzcGVyc8OjbyDDqSBhcGVuYXMgdW1hIGNhcmFjdGVyw61zdGljYSBpbmVyZW50ZSDDoCBuYXR1cmV6YSBlc3RvY8Ohc3RpY2EgZG9zIGRhZG9zLiIsICJCIjogIk8gZmVuw7RtZW5vIG9ic2VydmFkbyDDqSB1bSBpbmRpY2F0aXZvIGRlIGhldGVyb2NlZGFzdGljaWRhZGUsIHZpb2xhbmRvIG8gcHJlc3N1cG9zdG8gZGUgdmFyacOibmNpYSBjb25zdGFudGUgZG9zIGVycm9zICRcXHRleHR7VmFyfShcXHZhcmVwc2lsb25faSkgPSBcXHNpZ21hXjIkLiIsICJDIjogIk8gZ3LDoWZpY28gc3VnZXJlIHF1ZSBvIG1vZGVsbyBzb2ZyZSBkZSBhdXRvY29ycmVsYcOnw6NvLCBpbmRpY2FuZG8gcXVlIG9zIHJlc8OtZHVvcyBuw6NvIHPDo28gaW5kZXBlbmRlbnRlcyBlbnRyZSBzaS4iLCAiRCI6ICJPIHBhZHLDo28gZGUgZnVuaWwgaW5kaWNhIHF1ZSBhIHJlbGHDp8OjbyBlbnRyZSBhcyB2YXJpw6F2ZWlzIMOpIGVzdHJpdGFtZW50ZSBsaW5lYXIsIHZhbGlkYW5kbyBhIHByZW1pc3NhIGRlIGxpbmVhcmlkYWRlIGRvIG1vZGVsby4iLCAiRSI6ICJPIG1vZGVsbyBlc3TDoSBjb20gdmnDqXMgZGUgZXNwZWNpZmljYcOnw6NvLCBtYXMgbyBwcmVzc3Vwb3N0byBkZSBob21vY2VkYXN0aWNpZGFkZSBlc3TDoSBtYW50aWRvLCBkYWRvIHF1ZSBvcyByZXPDrWR1b3MgZXN0w6NvIGNlbnRyYWRvcyBlbSB6ZXJvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIHByZW1pc3NhIGRlIHF1ZSBhIHZhcmnDom5jaWEgZG9zIGVycm9zIGRldmUgc2VyIGNvbnN0YW50ZSBwYXJhIHRvZG8gbyBpbnRlcnZhbG8gZGUgdmFsb3JlcyBwcmV2aXN0b3MuIE8gcXVlIGFjb250ZWNlIGNvbSBhIGNvbmZpYWJpbGlkYWRlIGRhIHZhcmnDom5jaWEgcXVhbmRvIG8gZXJybyBtdWRhIGRlIGFtcGxpdHVkZSBjb25mb3JtZSBvIHZhbG9yIGFqdXN0YWRvPyIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBwcmVzc3Vwb3N0byBkZSBob21vY2VkYXN0aWNpZGFkZSBubyBtb2RlbG8gbGluZWFyIHByZXNzdXDDtWUgcXVlICRcXHRleHR7VmFyfShcXHZhcmVwc2lsb25faSkgPSBcXHNpZ21hXjIkIHBhcmEgdG9kYXMgYXMgb2JzZXJ2YcOnw7Vlcy4gUXVhbmRvIHBsb3RhbW9zICRcXGhhdHtlfV9pJCB2ZXJzdXMgJFxcaGF0e3l9X2kkIGUgb2JzZXJ2YW1vcyB1bSBwYWRyw6NvIGRlICdmdW5pbCcgKHZhcmlhYmlsaWRhZGUgY3Jlc2NlbnRlIG91IGRlY3Jlc2NlbnRlKSwgZXN0YW1vcyB2aXN1YWxpemFuZG8gZ3JhZmljYW1lbnRlIGEgaGV0ZXJvY2VkYXN0aWNpZGFkZS4gSXNzbyBpbXBsaWNhIHF1ZSBhIHByZWNpc8OjbyBkYXMgZXN0aW1hdGl2YXMgbsOjbyDDqSB1bmlmb3JtZSBlbSB0b2RvIG8gaW50ZXJ2YWxvIGRlIHZhbG9yZXMgZGEgdmFyacOhdmVsIHJlZ3Jlc3NvcmEsIGludmFsaWRhbmRvIGFzIGluZmVyw6puY2lhcyBjbMOhc3NpY2FzIHF1ZSBkZXBlbmRlbSBkYSBob21vZ2VuZWlkYWRlIGRhIHZhcmnDom5jaWEuIiwgImNvZGlnb19wbG90bHkiOiAiaW1wb3J0IHBsb3RseS5ncmFwaF9vYmplY3RzIGFzIGdvXG5pbXBvcnQgbnVtcHkgYXMgbnBcblxubiA9IDEwMFxueCA9IG5wLmxpbnNwYWNlKDEwLCAxMDAsIG4pXG55X2hhdCA9IDIgKiB4ICsgNVxuIyBDcmlhbmRvIHJlc8OtZHVvcyBjb20gaGV0ZXJvY2VkYXN0aWNpZGFkZSAoZnVuaWwpXG5yZXNpZHVvcyA9IG5wLnJhbmRvbS5ub3JtYWwoMCwgMC4xICogeClcblxuZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXlfaGF0LCB5PXJlc2lkdW9zLCBtb2RlPSdtYXJrZXJzJywgbWFya2VyPWRpY3QoY29sb3I9JyMxRTNBOEEnLCBvcGFjaXR5PTAuNikpKVxuZmlnLnVwZGF0ZV9sYXlvdXQoXG4gICAgdGl0bGU9clwiPGI+R3LDoWZpY28gZGUgRGlhZ27Ds3N0aWNvOiBSZXPDrWR1b3MgdnMuIFZhbG9yZXMgQWp1c3RhZG9zPC9iPlwiLFxuICAgIHhheGlzPWRpY3QodGl0bGU9clwiVmFsb3JlcyBBanVzdGFkb3MgKCRcXGhhdHt5fV9pJClcIiwgZml4ZWRyYW5nZT1UcnVlKSxcbiAgICB5YXhpcz1kaWN0KHRpdGxlPXJcIlJlc8OtZHVvcyBBbW9zdHJhaXMgKCRcXGhhdHtlfV9pJClcIiwgZml4ZWRyYW5nZT1UcnVlKSxcbiAgICB0ZW1wbGF0ZT1cInBsb3RseV93aGl0ZVwiXG4pIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW0gZWNvbm9taXN0YSBkZXNlamEgdmVyaWZpY2FyIGEgYWRlcXVhw6fDo28gZGUgdW0gbW9kZWxvIGxpbmVhciBhcGxpY2FkbyBhIGRhZG9zIHRlbXBvcmFpcy4gQXDDs3MgZXN0aW1hciBvcyBjb2VmaWNpZW50ZXMsIGVsZSBwbG90YSBvcyByZXPDrWR1b3MgJFxcaGF0e2V9X2kkIGVtIGZ1bsOnw6NvIGRhIG9yZGVtIGRlIGNvbGV0YSBkYXMgb2JzZXJ2YcOnw7VlcyAodGVtcG8pLiBBbyBhbmFsaXNhciBvIGdyw6FmaWNvLCBlbGUgb2JzZXJ2YSB1bWEgc2VxdcOqbmNpYSBjbGFyYSBkZSB2YWxvcmVzIHBvc2l0aXZvcyBzZWd1aWRhIHBvciB1bWEgc2VxdcOqbmNpYSBkZSB2YWxvcmVzIG5lZ2F0aXZvcywgY29uZmlndXJhbmRvIHVtIHBhZHLDo28gZGUgY2ljbGljaWRhZGUgb3UgdGVuZMOqbmNpYS4gQ29tIGJhc2Ugbm8gZGlhZ27Ds3N0aWNvIHZpc3VhbCwgbyBxdWUgZXN0ZSBjb21wb3J0YW1lbnRvIHN1Z2VyZSBlbSByZWxhw6fDo28gw6BzIHByZW1pc3NhcyBkbyBtb2RlbG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPcyByZXPDrWR1b3Mgc8OjbyBpbmRlcGVuZGVudGVzLCBjb25maXJtYW5kbyBhIHZhbGlkYWRlIGRvIG1vZGVsbyBwYXJhIHPDqXJpZXMgdGVtcG9yYWlzLiIsICJCIjogIk8gbW9kZWxvIGFwcmVzZW50YSB1bSBlcnJvIGRlIGVzcGVjaWZpY2HDp8OjbyBxdWUgcmVzdWx0YSBlbSBoZXRlcm9jZWRhc3RpY2lkYWRlLCBuZWNlc3NpdGFuZG8gZGUgdW1hIHRyYW5zZm9ybWHDp8OjbyBsb2dhcsOtdG1pY2EuIiwgIkMiOiAiSMOhIHVtYSBjbGFyYSB2aW9sYcOnw6NvIGRhIHN1cG9zacOnw6NvIGRlIGluZGVwZW5kw6puY2lhIGRvcyBlcnJvcywgc3VnZXJpbmRvIGEgcHJlc2Vuw6dhIGRlIGF1dG9jb3JyZWxhw6fDo28gbm9zIHJlc8OtZHVvcy4iLCAiRCI6ICJPIG1vZGVsbyDDqSBwZXJmZWl0YW1lbnRlIGFkZXF1YWRvLCBwb2lzIG8gcGFkcsOjbyBjw61jbGljbyDDqSBlc3BlcmFkbyBlbSBvYnNlcnZhw6fDtWVzIGNvbGV0YWRhcyBlbSBpbnRlcnZhbG9zIGRlIHRlbXBvIGZpeG9zLiIsICJFIjogIk9zIHJlc8OtZHVvcyBhcHJlc2VudGFtIG5vcm1hbGlkYWRlLCB2aXN0byBxdWUgbyBwYWRyw6NvIGPDrWNsaWNvIGNvbXBlbnNhIGFzIHZhcmlhw6fDtWVzIHBvc2l0aXZhcyBlIG5lZ2F0aXZhcy4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIlF1YW5kbyBvYnNlcnZhbW9zIHJlc8OtZHVvcyBxdWUgbsOjbyB2YXJpYW0gYWxlYXRvcmlhbWVudGUgZW0gdG9ybm8gZGUgemVybywgbWFzIHNpbSBmb3JtYW0gcGFkcsO1ZXMgdGVtcG9yYWlzIG91IHRlbmTDqm5jaWFzLCBvIHF1ZSBpc3NvIGRpeiBzb2JyZSBhIHJlbGHDp8OjbyBlbnRyZSBvIGVycm8gZGUgdW1hIG9ic2VydmHDp8OjbyAkaSQgZSBhIG9ic2VydmHDp8OjbyAkaSsxJD8iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgaW5kZXBlbmTDqm5jaWEgZG9zIGVycm9zIMOpIHVtYSBwcmVtaXNzYSBmdW5kYW1lbnRhbCBkbyBtb2RlbG8gbGluZWFyLiBRdWFuZG8gb3MgcmVzw61kdW9zIGV4aWJlbSBwYWRyw7VlcyBzaXN0ZW3DoXRpY29zIChjb21vIGNpY2xpY2lkYWRlLCB0ZW5kw6puY2lhIG91IHNlcXXDqm5jaWFzIGxvbmdhcyBkZSB1bSBtZXNtbyBzaW5hbCkgZW0gdW0gZ3LDoWZpY28gZGUgb3JkZW0gY3Jvbm9sw7NnaWNhLCBpc3NvIGluZGljYSBxdWUgbyBlcnJvIGRlIHVtYSBvYnNlcnZhw6fDo28gZXN0w6EgY29ycmVsYWNpb25hZG8gY29tIGEgb2JzZXJ2YcOnw6NvIGFudGVyaW9yLCBvdSBzZWphLCBow6EgYXV0b2NvcnJlbGHDp8Ojby4gSXNzbyB2aW9sYSBhIHByZW1pc3NhIGRlIGluZGVwZW5kw6puY2lhIGUgc3VnZXJlIHF1ZSBvIG1vZGVsbyBuw6NvIGNhcHR1cm91IHRvZGEgYSBlc3RydXR1cmEgZGUgZGVwZW5kw6puY2lhIGRvcyBkYWRvcy4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIk7DrXZlYSBCaXNwbywgQXVsYSAxMzogQW7DoWxpc2UgZGUgUmVzw61kdW9zIG5vIE1STFMsIERFU1QtVUZCQSAyMDI1LjEsIFNsaWRlIDYifSwgeyJlbnVuY2lhZG8iOiAiVW0gZW5nZW5oZWlybyBkZSBwcm9kdcOnw6NvIGVzdMOhIGFuYWxpc2FuZG8gYSByZWxhw6fDo28gZW50cmUgbyB0ZW1wbyBkZSBzZXR1cCAoJHgkKSBlIG8gY3VzdG8gZGUgbWFudXRlbsOnw6NvICgkeSQpIGRlIHVtYSBtw6FxdWluYSBpbmR1c3RyaWFsLiBBcMOzcyBhanVzdGFyIHVtIE1vZGVsbyBkZSBSZWdyZXNzw6NvIExpbmVhciBTaW1wbGVzIChNUkxTKSwgZWxlIGRlY2lkZSB2ZXJpZmljYXIgYSBzdXBvc2nDp8OjbyBkZSBub3JtYWxpZGFkZSBkb3MgZXJyb3MgKCRcXHZhcmVwc2lsb25faSBcXHNpbSBOKDAsIFxcc2lnbWFeMikkKS4gTyBlbmdlbmhlaXJvIGdlcmEgdW0gZ3LDoWZpY28gTm9ybWFsIFFRLXBsb3QgZG9zIHJlc8OtZHVvcyBlIGFwbGljYSBvIHRlc3RlIGRlIFNoYXBpcm8tV2lsaywgb2J0ZW5kbyB1bSAkcFxcdGV4dHstdmFsb3J9ID0gMCwwMjgkLiBDb25zaWRlcmFuZG8gdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhID0gMCwwNSQsIHF1YWwgw6kgYSBjb25jbHVzw6NvIGVzdGF0w61zdGljYSBjb3JyZXRhIHNvYnJlIG9zIHJlc8OtZHVvcyBkbyBtb2RlbG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJDb21vIG8gJHBcXHRleHR7LXZhbG9yfSA8IFxcYWxwaGEkLCByZWplaXRhbW9zICRIXzAkIGUgY29uY2x1w61tb3MgcXVlIG9zIHJlc8OtZHVvcyBzZWd1ZW0gdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbC4iLCAiQiI6ICJDb21vIG8gJHBcXHRleHR7LXZhbG9yfSA8IFxcYWxwaGEkLCBuw6NvIHJlamVpdGFtb3MgJEhfMCQgZSBvcyByZXPDrWR1b3MgYXByZXNlbnRhbSBldmlkw6puY2lhcyBkZSBub3JtYWxpZGFkZS4iLCAiQyI6ICJDb21vIG8gJHBcXHRleHR7LXZhbG9yfSA8IFxcYWxwaGEkLCByZWplaXRhbW9zICRIXzAkLCBzdWdlcmluZG8gcXVlIG9zIGVycm9zIG7Do28gc2VndWVtIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwsIG8gcXVlIHBvZGUgaW52YWxpZGFyIGFzIGluZmVyw6puY2lhcyBzb2JyZSBvcyBwYXLDom1ldHJvcy4iLCAiRCI6ICJPIHRlc3RlIGRlIFNoYXBpcm8tV2lsayDDqSBpbnN1ZmljaWVudGUgZSBhcGVuYXMgbyBRUS1wbG90IGRldmUgc2VyIGNvbnNpZGVyYWRvIHBhcmEgYSBkZWNpc8OjbywgaW5kZXBlbmRlbnRlbWVudGUgZG8gJHBcXHRleHR7LXZhbG9yfSQuIiwgIkUiOiAiTyBtb2RlbG8gw6kgcGVyZmVpdGFtZW50ZSBhanVzdGFkbywgcG9pcyB1bSAkcFxcdGV4dHstdmFsb3J9JCBiYWl4byBlbSB0ZXN0ZXMgZGUgbm9ybWFsaWRhZGUgw6kgbyBvYmpldGl2byBlc3BlcmFkbyBuYSBtb2RlbGFnZW0gbGluZWFyLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIHJlZ3JhIGRlIGRlY2lzw6NvIHBhcmEgdGVzdGVzIGRlIGhpcMOzdGVzZXM6IGNvbXBhcmUgbyBwLXZhbG9yIG9idGlkbyBjb20gbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkIGVzdGlwdWxhZG8gcGVsbyBwZXNxdWlzYWRvci4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgaGlww7N0ZXNlIG51bGEgKCRIXzAkKSBkbyB0ZXN0ZSBkZSBTaGFwaXJvLVdpbGsgw6kgcXVlIG9zIGRhZG9zIChuZXN0ZSBjYXNvLCBvcyByZXPDrWR1b3MpIHByb3bDqm0gZGUgdW1hIHBvcHVsYcOnw6NvIGNvbSBkaXN0cmlidWnDp8OjbyBub3JtYWwuIFNlICRwXFx0ZXh0ey12YWxvcn0gXFxsZSBcXGFscGhhJCwgcmVqZWl0YW1vcyAkSF8wJCBhbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkLiBBcXVpLCAkMCwwMjggPCAwLDA1JCwgcG9ydGFudG8sIHRlbW9zIGV2aWTDqm5jaWFzIGVzdGF0w61zdGljYXMgc2lnbmlmaWNhdGl2YXMgcGFyYSByZWplaXRhciBhIHN1cG9zacOnw6NvIGRlIG5vcm1hbGlkYWRlIGRvcyBlcnJvcy4gRW0gbW9kZWxvcyBkZSByZWdyZXNzw6NvLCBhIHZpb2xhw6fDo28gZGEgbm9ybWFsaWRhZGUgcG9kZSBjb21wcm9tZXRlciBhIHZhbGlkYWRlIGRvcyB0ZXN0ZXMgJHQkIGUgJEYkIHV0aWxpemFkb3MgcGFyYSBpbmZlcsOqbmNpYSBkb3MgY29lZmljaWVudGVzLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bLTIsIC0xLCAwLCAxLCAyXSwgeT0sIG1vZGU9J21hcmtlcnMnLCBuYW1lPSdSZXPDrWR1b3MgT2JzZXJ2YWRvcycsIG1hcmtlcj1kaWN0KGNvbG9yPScjMUUzQThBJykpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9Wy0yLCAyXSwgeT1bLTIsIDJdLCBtb2RlPSdsaW5lcycsIG5hbWU9J05vcm1hbCBUZcOzcmljYScsIGxpbmU9ZGljdChjb2xvcj0nIzk5MUIxQicsIGRhc2g9J2Rhc2gnKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+Tm9ybWFsIFFRLVBsb3QgZG9zIFJlc8OtZHVvczwvYj4nLCB4YXhpcz1kaWN0KHRpdGxlPSdRdWFudGlzIFRlw7NyaWNvcycpLCB5YXhpcz1kaWN0KHRpdGxlPSdRdWFudGlzIGRvcyBSZXPDrWR1b3MnKSwgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW1hIGFuw6FsaXNlIGRlIHJlc8OtZHVvcyBkZSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBwYXJhIHByZXZlciBvIGNvbnN1bW8gbWVuc2FsIGRlIGVuZXJnaWEgZWzDqXRyaWNhLCBvIFFRLXBsb3QgZXhpYmUgcG9udG9zIHF1ZSBzZSBhZmFzdGFtIHNpZ25pZmljYXRpdmFtZW50ZSBkYSBsaW5oYSBkZSByZWZlcsOqbmNpYSBuYXMgZXh0cmVtaWRhZGVzIChjYXVkYXMpIGRhIGRpc3RyaWJ1acOnw6NvLiBBZGljaW9uYWxtZW50ZSwgbyB0ZXN0ZSBkZSBTaGFwaXJvLVdpbGsgcmVzdWx0b3UgZW0gJHBcXHRleHR7LXZhbG9yfSA9IDAsMTUkLiBPIHF1ZSBhIGNvbWJpbmHDp8OjbyBkZXNzYXMgZmVycmFtZW50YXMgbm9zIGluZm9ybWEgc29icmUgbyBkaWFnbsOzc3RpY28gZG8gbW9kZWxvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiT3MgcmVzw61kdW9zIHPDo28gZXN0cml0YW1lbnRlIG5vcm1haXMsIHBvaXMgbyAkcFxcdGV4dHstdmFsb3J9JCDDqSBtdWl0byBzdXBlcmlvciBhIDAsMDUuIiwgIkIiOiAiRXhpc3RlIHVtYSB2aW9sYcOnw6NvIGNsYXJhIGRhIG5vcm1hbGlkYWRlLCBwb2lzIG8gUVEtcGxvdCBpbmRpY2EgY2F1ZGFzIHBlc2FkYXMgcXVlIG8gdGVzdGUgZXN0YXTDrXN0aWNvIG7Do28gY29uc2VndWl1IGNhcHRhci4iLCAiQyI6ICJPIGdyw6FmaWNvIGUgbyB0ZXN0ZSBhcHJlc2VudGFtIHJlc3VsdGFkb3MgY29uZmxpdGFudGVzLCBzZW5kbyBxdWUgYSBpbnRlcnByZXRhw6fDo28gdmlzdWFsIGRvIFFRLXBsb3QgZGV2ZSBzZXIgZGVzY2FydGFkYSBlbSBmYXZvciBkbyB0ZXN0ZSBmb3JtYWwuIiwgIkQiOiAiTyBtb2RlbG8gYXByZXNlbnRhIHJlc8OtZHVvcyBjb20gbm9ybWFsaWRhZGUgYWNlaXTDoXZlbCwgdmlzdG8gcXVlLCBhbyBuw612ZWwgZGUgNSUsIG7Do28gdGVtb3MgZXZpZMOqbmNpYXMgcGFyYSByZWplaXRhciAkSF8wJCwgZW1ib3JhIG8gZ3LDoWZpY28gc3VnaXJhIGNhdXRlbGEgcXVhbnRvIMOgcyBjYXVkYXMuIiwgIkUiOiAiTyBwLXZhbG9yIGRlIDAsMTUgaW5kaWNhIHF1ZSBvIG1vZGVsbyBwb3NzdWkgdW1hIHZhcmnDom5jaWEgY29uc3RhbnRlLCBtYXMgbsOjbyBmb3JuZWNlIGluZm9ybWHDp8O1ZXMgc29icmUgYSBub3JtYWxpZGFkZSBkb3MgZXJyb3MuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkQiLCAiZGljYSI6ICJQZW5zZSBzb2JyZSBvIHBvZGVyIGRvIHRlc3RlIGRlIFNoYXBpcm8tV2lsayBlbSBhbW9zdHJhcyBwZXF1ZW5hcyBlIGEgc2Vuc2liaWxpZGFkZSBkZSBkaWFnbsOzc3RpY29zIGdyw6FmaWNvcyB2ZXJzdXMgdGVzdGVzIGRlIGhpcMOzdGVzZSBmb3JtYWlzLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQW8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGRlIDUlICgkXFxhbHBoYT0wLDA1JCksIHVtICRwXFx0ZXh0ey12YWxvcn0gPSAwLDE1JCBpbXBsaWNhIHF1ZSBuw6NvIHJlamVpdGFtb3MgYSBoaXDDs3Rlc2UgbnVsYSBkZSBub3JtYWxpZGFkZS4gQ29udHVkbywgZW0gYW7DoWxpc2VzIGRlIHJlc8OtZHVvcywgw6kgY29tdW0gcXVlIGdyw6FmaWNvcyBjb21vIG8gUVEtcGxvdCByZXZlbGVtIGNvbXBvcnRhbWVudG9zIChjb21vIGNhdWRhcyBwZXNhZGFzKSBxdWUgbyB0ZXN0ZSBlc3RhdMOtc3RpY28gcG9kZSBuw6NvIGRldGVjdGFyIGRldmlkbyDDoCBzdWEgbGltaXRhw6fDo28gZGUgcG9kZXIgZW0gY2VydGFzIGNvbmRpw6fDtWVzLiBBIGNvbmNsdXPDo28gY29ycmV0YSDDqSBxdWUsIGZvcm1hbG1lbnRlLCBhIG5vcm1hbGlkYWRlIG7Do28gw6kgcmVqZWl0YWRhLCBtYXMgYSBpbnNwZcOnw6NvIGdyw6FmaWNhIHNlcnZlIGNvbW8gdW0gYXZpc28gZGUgcXVlIG9zIGVycm9zIHBvZGVtIG7Do28gc2VyIHBlcmZlaXRhbWVudGUgZ2F1c3NpYW5vcy4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvIGxpbmVhciBtw7psdGlwbGEgYWp1c3RhZG8gcGFyYSBwcmV2ZXIgYSBlZmljacOqbmNpYSBlbmVyZ8OpdGljYSBkZSBtw6FxdWluYXMgaW5kdXN0cmlhaXMgKCRuPTUwJCwgJHA9NCQgcHJlZGl0b3JlcyksIGlkZW50aWZpY291LXNlIHVtYSBvYnNlcnZhw6fDo28gcXVlIHBvc3N1aSB1bSB2YWxvciBkZSBhbGF2YW5jYSAkaF97aWl9ID0gMC40NSQuIENvbnNpZGVyYW5kbyBvIGxpbWlhciBjcsOtdGljbyBkZWZpbmlkbyBjb21vICRcZnJhY3syKHArMSl9e259JCwgY29tbyBlc3RhIG9ic2VydmHDp8OjbyBkZXZlIHNlciBjbGFzc2lmaWNhZGEgZSBxdWFsIGEgc3VhIHBvc3PDrXZlbCBpbmZsdcOqbmNpYSBubyBtb2RlbG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIG9ic2VydmHDp8OjbyBuw6NvIMOpIHVtIHBvbnRvIGRlIGFsYXZhbmNhLCBwb2lzICQwLjQ1IDwgMC4yMCQsIGUgbsOjbyBwb3NzdWkgaW5mbHXDqm5jaWEgbm8gbW9kZWxvLiIsICJCIjogIkEgb2JzZXJ2YcOnw6NvIMOpIHVtIHBvbnRvIGRlIGFsYXZhbmNhLCBwb2lzICQwLjQ1ID4gMC4yMCQsIHBvZGVuZG8gZGVzbG9jYXIgc2lnbmlmaWNhdGl2YW1lbnRlIGEgZXN0aW1hdGl2YSBkb3MgY29lZmljaWVudGVzICRcXGhhdHtcXGJldGF9X2okLiIsICJDIjogIkEgb2JzZXJ2YcOnw6NvIMOpIHVtIG91dGxpZXIgbmEgdmFyacOhdmVsIHJlc3Bvc3RhLCBtYXMgbsOjbyBwb3NzdWkgaW5mbHXDqm5jaWEgbmEgbWF0cml6IGRlIHByb2plw6fDo28gJFxcbWF0aGJme0h9JC4iLCAiRCI6ICJBIG9ic2VydmHDp8OjbyBhcHJlc2VudGEgdW1hIGFsYXZhbmNhIGFjZWl0w6F2ZWwsIHZpc3RvIHF1ZSBvIHZhbG9yIGVzdMOhIGFiYWl4byBkZSAkMC41JCwgbsOjbyByZXF1ZXJlbmRvIGludmVzdGlnYcOnw6NvIGFkaWNpb25hbC4iLCAiRSI6ICJPIGPDoWxjdWxvIGRhIGFsYXZhbmNhICRoX3tpaX0kIMOpIGluZGVwZW5kZW50ZSBkbyBuw7ptZXJvIGRlIHByZWRpdG9yZXMgJHAkLCBsb2dvLCBhIGNsYXNzaWZpY2HDp8OjbyDDqSBpbnbDoWxpZGEgcGFyYSAkcD00JC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkNhbGN1bGUgbyBsaW1pYXIgY3LDrXRpY28gJGheKiA9IFxcZnJhY3syKHArMSl9e259JCBjb20gb3MgdmFsb3JlcyBmb3JuZWNpZG9zIGUgY29tcGFyZSBjb20gJGhfe2lpfSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIGRldGVybWluYXIgc2UgYSBvYnNlcnZhw6fDo28gw6kgdW0gcG9udG8gZGUgYWxhdmFuY2EsIGNvbXBhcmFtb3Mgc2V1IHZhbG9yICRoX3tpaX0kIGNvbSBvIGxpbWlhciBjcsOtdGljbzogJCRoXiogPSBcXGZyYWN7MihwKzEpfXtufSA9IFxcZnJhY3syKDQrMSl9ezUwfSA9IFxcZnJhY3sxMH17NTB9ID0gMC4yMCQkLiBDb21vICRoX3tpaX0gPSAwLjQ1JCBlICQwLjQ1ID4gMC4yMCQsIGEgb2JzZXJ2YcOnw6NvIMOpIGNvbnNpZGVyYWRhIHVtIHBvbnRvIGRlIGFsYXZhbmNhLiBQb250b3MgZGUgYWxhdmFuY2EgZXhlcmNlbSBmb3LDp2EgZGUgYXRyYcOnw6NvIHNvYnJlIG8gaGlwZXJwbGFubyBkZSByZWdyZXNzw6NvLCBwb2RlbmRvIGRlc3ZpYXIgb3MgY29lZmljaWVudGVzIGVzdGltYWRvcyAkXFxoYXR7XFxiZXRhfV9qJCBkbyBzZXUgdmVyZGFkZWlybyB2YWxvciBwb3B1bGFjaW9uYWwuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVsxLCAyLCAzLCA0XSwgeT1bMC4xLCAwLjE1LCAwLjQ1LCAwLjA1XSwgbW9kZT0nbWFya2VycycsIG1hcmtlcj1kaWN0KHNpemU9MTIsIGNvbG9yPVsnIzFFM0E4QScsICcjMUUzQThBJywgJyM5OTFCMUInLCAnIzFFM0E4QSddKSkpIFxuZmlnLmFkZF9obGluZSh5PTAuMjAsIGxpbmVfZGFzaD1cImRhc2hcIiwgbGluZV9jb2xvcj1cIiNGNTlFMEJcIiwgYW5ub3RhdGlvbl90ZXh0PVwiTGltaWFyICgwLjIwKVwiKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9XCI8Yj5EaXN0cmlidWnDp8OjbyBkYXMgQWxhdmFuY2FzICgkaF97aWl9JCk8L2I+XCIsIHhheGlzX3RpdGxlPVwiw41uZGljZSBkYSBPYnNlcnZhw6fDo29cIiwgeWF4aXNfdGl0bGU9XCJBbGF2YW5jYSAoJGhfe2lpfSQpXCIpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQW5hbGlzZSBhIHJlbGHDp8OjbyBlbnRyZSBvcyByZXPDrWR1b3MgZSBhIHZhcmnDom5jaWEgb2JzZXJ2YWRhIGVtIHVtIGRpYWduw7NzdGljbyBkZSByZWdyZXNzw6NvLiBTZSB1bSBtb2RlbG8gYXByZXNlbnRhIHVtIGVycm8gcmVzaWR1YWwgJFxcaGF0e2V9X2kkIGN1am8gbcOpdG9kbyBkZSBzdHVkZW50aXphw6fDo28gcHJvZHV6IHVtIHZhbG9yIGFic29sdXRvIG1haW9yIHF1ZSAyLCBxdWFsIGEgaW50ZXJwcmV0YcOnw6NvIGVzdGF0w61zdGljYSBtYWlzIGFkZXF1YWRhIGRlbnRybyBkYSBhbsOhbGlzZSBkZSBvYnNlcnZhw6fDtWVzIG7Do28gdXN1YWlzPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBvYnNlcnZhw6fDo28gw6kgYXV0b21hdGljYW1lbnRlIHVtIHBvbnRvIGRlIGFsYXZhbmNhLCBpbmRlcGVuZGVudGVtZW50ZSBkZSBzdWEgcG9zacOnw6NvIGVtICRYJC4iLCAiQiI6ICJPIG1vZGVsbyBlc3TDoSBwZXJmZWl0YW1lbnRlIGFqdXN0YWRvLCBwb2lzIHJlc8OtZHVvcyBwYWRyb25pemFkb3MgbnVuY2EgZGV2ZW0gZXhjZWRlciAyLiIsICJDIjogIkEgb2JzZXJ2YcOnw6NvIMOpIHVtIHBvdGVuY2lhbCBvdXRsaWVyIG5hIHZhcmnDoXZlbCByZXNwb3N0YSwgaW5kaWNhbmRvIHVtIGRlc3ZpbyBkbyBwYWRyw6NvIGVzcGVyYWRvIHBhcmEgYXF1ZWxhIHBvc2nDp8OjbyBlbSAkWCQuIiwgIkQiOiAiTyB2YWxvciAkaF97aWl9JCBkZXN0YSBvYnNlcnZhw6fDo28gw6kgbmVjZXNzYXJpYW1lbnRlIDEsIG8gcXVlIGludmlhYmlsaXphIG8gY8OhbGN1bG8gZG8gcmVzw61kdW8uIiwgIkUiOiAiVHJhdGEtc2UgZGUgdW1hIG9ic2VydmHDp8OjbyBjb20gYWx0YSBwcmVjaXPDo28sIHBvaXMgbyByZXPDrWR1byDDqSBzaWduaWZpY2F0aXZhbWVudGUgc3VwZXJpb3Igw6AgbcOpZGlhIGRvcyByZXPDrWR1b3MuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgZGVmaW5pw6fDo28gZGUgb3V0bGllciBuYSB2YXJpw6F2ZWwgcmVzcG9zdGE6IG8gcmVzw61kdW8gJFxcaGF0e2V9X2kkIHJlcHJlc2VudGEgbyBkZXN2aW8gZW0gcmVsYcOnw6NvIGFvIHZhbG9yIHByZXZpc3RvICRcXGhhdHt5fV9pJC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgc3R1ZGVudGl6YcOnw6NvIGRvIHJlc8OtZHVvLCBxdWUgdXRpbGl6YSAkXFx0ZXh0e1Zhcn0oXFxoYXR7ZX1faSkgPSBcXHNpZ21hXjIoMSAtIGhfe2lpfSkkLCBwZXJtaXRlIGF2YWxpYXIgc2UgbyBlcnJvIGVtIHVtYSBkZXRlcm1pbmFkYSBvYnNlcnZhw6fDo28gw6kgYXRpcGljYW1lbnRlIGdyYW5kZS4gUXVhbmRvICR8XHRleHR7UmVzw61kdW8gU3R1ZGVudGl6YWRvfXwgPiAyJCwgbyBtb2RlbG8gaW5kaWNhIHF1ZSBvIHZhbG9yIG9ic2VydmFkbyAkeV9pJCBlc3TDoSBsb25nZSBkbyB2YWxvciBhanVzdGFkbyAkXFxoYXR7eX1faSQsIGNhcmFjdGVyaXphbmRvIGEgb2JzZXJ2YcOnw6NvIGNvbW8gdW0gb3V0bGllciBuYSB2YXJpw6F2ZWwgcmVzcG9zdGEsIGV4aWdpbmRvIGludmVzdGlnYcOnw6NvIHBhcmEgdmVyaWZpY2FyIHNlIGjDoSBlcnJvcyBkZSBtZWRpw6fDo28gb3Ugc2UgbyBtb2RlbG8gw6kgaW5hZGVxdWFkbyBwYXJhIGFxdWVsZSBjYXNvLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfV0sICJxdWVzdG9lc19kaXNjdXJzaXZhcyI6IFt7ImVudW5jaWFkbyI6ICJQcm92ZSBxdWUsIG5vIG1vZGVsbyBsaW5lYXIgJFxcbWF0aGJme3l9ID0gXFxtYXRoYmZ7WH1cXGJvbGRzeW1ib2x7XFxiZXRhfSArIFxcYm9sZHN5bWJvbHtcXHZhcmVwc2lsb259JCwgbyB2ZXRvciBkZSByZXPDrWR1b3MgJFxcaGF0e1xcbWF0aGJme2V9fSQgw6kgb3J0b2dvbmFsIMOgcyBjb2x1bmFzIGRhIG1hdHJpeiBkZSBkZXNlbmhvICRcXG1hdGhiZntYfSQuIE91IHNlamEsIGRlbW9uc3RyZSBxdWUgJFxcbWF0aGJme1h9XntcXHRvcH1cXGhhdHtcXG1hdGhiZntlfX0gPSBcXG1hdGhiZnswfSQuIiwgImRpY2EiOiAiVXRpbGl6ZSBhIGRlZmluacOnw6NvIGRvIHZldG9yIGRlIHJlc8OtZHVvcyAkXFxoYXR7XFxtYXRoYmZ7ZX19ID0gKFxcbWF0aGJme0l9IC0gXFxtYXRoYmZ7SH0pXFxtYXRoYmZ7eX0kIGUgbGVtYnJlLXNlIHF1ZSAkXFxtYXRoYmZ7SH0gPSBcXG1hdGhiZntYfShcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0pXnstMX1cXG1hdGhiZntYfV57XFx0b3B9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFydGltb3MgZGEgZGVmaW5pw6fDo28gZG8gdmV0b3IgZGUgcmVzw61kdW9zOiAkXFxoYXR7XFxtYXRoYmZ7ZX19ID0gXFxtYXRoYmZ7eX0gLSBcXGhhdHtcXG1hdGhiZnt5fX0gPSBcXG1hdGhiZnt5fSAtIFxcbWF0aGJme0h9XFxtYXRoYmZ7eX0gPSAoXFxtYXRoYmZ7SX0gLSBcXG1hdGhiZntIfSlcXG1hdGhiZnt5fSQuIiwgIlF1ZXJlbW9zIGNhbGN1bGFyIG8gcHJvZHV0byAkXFxtYXRoYmZ7WH1ee1xcdG9wfVxcaGF0e1xcbWF0aGJme2V9fSQ6ICRcXG1hdGhiZntYfV57XFx0b3B9XFxoYXR7XFxtYXRoYmZ7ZX19ID0gXFxtYXRoYmZ7WH1ee1xcdG9wfShcXG1hdGhiZntJfSAtIFxcbWF0aGJme0h9KVxcbWF0aGJme3l9ID0gKFxcbWF0aGJme1h9XntcXHRvcH0gLSBcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7SH0pXFxtYXRoYmZ7eX0kLiIsICJTdWJzdGl0dcOtbW9zIGEgZGVmaW5pw6fDo28gZGEgbWF0cml6ICRcXG1hdGhiZntIfSA9IFxcbWF0aGJme1h9KFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfVxcbWF0aGJme1h9XntcXHRvcH0kIG5hIGV4cHJlc3PDo286ICRcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7SH0gPSBcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9XFxtYXRoYmZ7WH1ee1xcdG9wfSQuIiwgIlNpbXBsaWZpY2FuZG8gbyBwcm9kdXRvIGRhcyBtYXRyaXplcyBpbnZlcnNhcyAkKFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSkoXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9ID0gXFxtYXRoYmZ7SX0kLCB0ZW1vczogJFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntIfSA9IFxcbWF0aGJme0l9XFxtYXRoYmZ7WH1ee1xcdG9wfSA9IFxcbWF0aGJme1h9XntcXHRvcH0kLiIsICJSZXRvcm5hbmRvIMOgIGV4cHJlc3PDo28gb3JpZ2luYWw6ICRcXG1hdGhiZntYfV57XFx0b3B9XFxoYXR7XFxtYXRoYmZ7ZX19ID0gKFxcbWF0aGJme1h9XntcXHRvcH0gLSBcXG1hdGhiZntYfV57XFx0b3B9KVxcbWF0aGJme3l9ID0gXFxtYXRoYmZ7MH1cXG1hdGhiZnt5fSA9IFxcbWF0aGJmezB9JC4iLCAiQ29uY2x1c8OjbzogQ29tbyAkXFxtYXRoYmZ7WH1ee1xcdG9wfVxcaGF0e1xcbWF0aGJme2V9fSA9IFxcbWF0aGJmezB9JCwgb3MgcmVzw61kdW9zIHPDo28gb3J0b2dvbmFpcyBhbyBlc3Bhw6dvIGNvbHVuYSBkZSAkXFxtYXRoYmZ7WH0kLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvIGxpbmVhciBzaW1wbGVzICgkcD0yJCwgaW5jbHVpbmRvIG8gaW50ZXJjZXB0bykgY29tICRuPTIwJCBvYnNlcnZhw6fDtWVzLCBjb25zaWRlcmUgdW1hIG9ic2VydmHDp8OjbyAkaSQgY29tIHZhbG9yIGRlIGFsYXZhbmNhICRoX3tpaX0gPSAwLjQ1JC4gRGFkbyBxdWUgbyBlc3RpbWFkb3IgZGEgdmFyacOibmNpYSBkbyBlcnJvIMOpICRcXGhhdHtcXHNpZ21hfV4yID0gNC4wJCwgY2FsY3VsZSBhIHZhcmnDom5jaWEgdGXDs3JpY2EgZG8gcmVzw61kdW8gJFxcaGF0e2V9X2kkIHBhcmEgZXN0YSBvYnNlcnZhw6fDo28gZSBleHBsaXF1ZSBzZSBlc3RlIHBvbnRvIGRlIGFsYXZhbmNhIHBvZGUgc2VyIGNvbnNpZGVyYWRvIGVsZXZhZG8gc2VndW5kbyBhIHJlZ3JhIGRlIG91cm8gJGhfe2lpfSA+IFxcZnJhY3sycH17bn0kLiIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSAkVmFyKFxcaGF0e2V9X2kpID0gXFxzaWdtYV4yKDEgLSBoX3tpaX0pJCBlIGFwbGlxdWUgbyBjcml0w6lyaW8gZGUgZGlhZ27Ds3N0aWNvIGRlIGFsYXZhbmNhIHN1Z2VyaWRvLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJEYWRvcyBkbyBwcm9ibGVtYTogJG49MjAkLCAkcD0yJCwgJFxcaGF0e1xcc2lnbWF9XjIgPSA0LjAkLCAkaF97aWl9ID0gMC40NSQuIiwgIkPDoWxjdWxvIGRhIHZhcmnDom5jaWEgZG8gcmVzw61kdW86ICRWYXIoXFxoYXR7ZX1faSkgPSBcXHNpZ21hXjIoMSAtIGhfe2lpfSkgPSA0LjAgXFx0aW1lcyAoMSAtIDAuNDUpID0gNC4wIFxcdGltZXMgMC41NSA9IDIuMiQuIiwgIkPDoWxjdWxvIGRvIGNyaXTDqXJpbyBkZSBhbGF2YW5jYTogJFxcZnJhY3sycH17bn0gPSBcXGZyYWN7MiBcXHRpbWVzIDJ9ezIwfSA9IFxcZnJhY3s0fXsyMH0gPSAwLjIkLiIsICJDb21wYXJhw6fDo286IENvbW8gJGhfe2lpfSA9IDAuNDUgPiAwLjIkLCBvIHBvbnRvIMOpIGNvbnNpZGVyYWRvIHVtYSBhbGF2YW5jYSBlbGV2YWRhIGUgbWVyZWNlIGludmVzdGlnYcOnw6NvIGRldGFsaGFkYS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDIuMn0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCBzb2IgYSDDs3RpY2EgZGEgYW7DoWxpc2UgZGUgcmVzw61kdW9zLCBwb3IgcXVlIGEgdmFyacOibmNpYSBkbyAkaSQtw6lzaW1vIHJlc8OtZHVvLCAkVmFyKFxcaGF0e2V9X2kpID0gXFxzaWdtYV4yKDEgLSBoX3tpaX0pJCwgbm9zIGFqdWRhIGEgZGV0ZWN0YXIgbyBwcm9ibGVtYSBkZSBoZXRlcm9jZWRhc3RpY2lkYWRlIG1lc21vIHF1ZSBvcyBlcnJvcyBvcmlnaW5haXMgKCRcXHZhcmVwc2lsb25faSQpIHRlbmhhbSB2YXJpw6JuY2lhIGNvbnN0YW50ZSAkXFxzaWdtYV4yJCBlbSB1bSBtb2RlbG8gYmVtIGVzcGVjaWZpY2Fkby4iLCAiZGljYSI6ICJSZWZsaXRhIHNvYnJlIG8gZmF0byBkZSBxdWUgYSBtYXRyaXogY2hhcMOpdSAkXFxtYXRoYmZ7SH0kIGRlcGVuZGUgZXN0cml0YW1lbnRlIGRvcyB2YWxvcmVzIGRlIGVudHJhZGEgZGEgbWF0cml6IGRlIGRlc2VuaG8gJFxcbWF0aGJme1h9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSB2YXJpw6JuY2lhIGRlIHVtIGVycm8gaW5kaXZpZHVhbCDDqSBjb25zdGFudGUsIG1hcyBhIHZhcmnDom5jaWEgZG8gcmVzw61kdW8gZGVwZW5kZSBkYSBwb3Npw6fDo28gZGEgb2JzZXJ2YcOnw6NvIG5vIGVzcGHDp28gZG9zIHJlZ3Jlc3NvcmVzICgkaF97aWl9JCkuIiwgIkEgbWF0cml6ICRcXG1hdGhiZntIfSQgbWVkZSBhIGluZmx1w6puY2lhIGRlIGNhZGEgcG9udG86ICRoX3tpaX0kIGFsdG8gb2NvcnJlIGVtIG9ic2VydmHDp8O1ZXMgZXh0cmVtYXMgZGUgJFgkLiIsICJBIGbDs3JtdWxhICRWYXIoXFxoYXR7ZX1faSkgPSBcXHNpZ21hXjIoMSAtIGhfe2lpfSkkIG1vc3RyYSBxdWUgYSBpbmNlcnRlemEgcmVzaWR1YWwgw6kgbWVub3IgZW0gcG9udG9zIGRlIGFsdGEgYWxhdmFuY2EuIiwgIlNlIG8gZ3LDoWZpY28gZGUgcmVzw61kdW9zIHBhZHJvbml6YWRvcyAob3UgbWVzbW8gb3MgYnJ1dG9zKSBtb3N0cmFyIHVtIHBhZHLDo28gcXVlIHNlZ3VlIGEgdmFyaWHDp8OjbyBkYSBhbGF2YW5jYSBvdSBkb3MgdmFsb3JlcyBkZSAkWCQsIHBvZGVtb3MgZXN0YXIgY29uZnVuZGluZG8gYSBlc3RydXR1cmEgaW50csOtbnNlY2EgZG8gZXN0aW1hZG9yIGRlIHJlc8OtZHVvcyBjb20gdW1hIHBvc3PDrXZlbCBoZXRlcm9jZWRhc3RpY2lkYWRlIHJlYWwuIiwgIlBvcnRhbnRvLCBhbyBhbmFsaXNhciByZXPDrWR1b3MsIGRldmVtb3Mgbm9ybWFsaXrDoS1sb3Mgb3UgY29uc2lkZXJhciBxdWUgYSB2YXJpYcOnw6NvIG9ic2VydmFkYSBuYSBkaXNwZXJzw6NvIGRvcyByZXPDrWR1b3MgcG9kZSBzZXIgdW1hIGNvbnNlcXXDqm5jaWEgZ2VvbcOpdHJpY2EgZGEgbWF0cml6IGRlIHByb2plw6fDo28sIGUgbsOjbyBuZWNlc3NhcmlhbWVudGUgdW1hIHZpb2xhw6fDo28gZGEgaG9tb2NlZGFzdGljaWRhZGUsIGVtYm9yYSBlbSBncmFuZGVzIGFtb3N0cmFzIGVzc2EgdmFyaWHDp8OjbyBkZSAkaF97aWl9JCB0b3JuZS1zZSBtZW5vcyBwcm9udW5jaWFkYS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJGYXJhd2F5LCBKLiBKLiwgTGluZWFyIE1vZGVscyB3aXRoIFIsIDJuZCBlZC4sIHAuIDc0IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgc2ltcGxlcyBvbmRlIG8gcGVzcXVpc2Fkb3Igc3VzcGVpdGEgZGEgdmlvbGHDp8OjbyBkYSBoaXDDs3Rlc2UgZGUgaG9tb2NlZGFzdGljaWRhZGUuIEV4cGxpcXVlLCB1dGlsaXphbmRvIG9zIGNvbmNlaXRvcyBkZSBhbsOhbGlzZSBncsOhZmljYSBkZSByZXPDrWR1b3MsIGNvbW8gYSBpbnNwZcOnw6NvIGRvIGdyw6FmaWNvIGRlICRcXGhhdHtlfV9pJCB2ZXJzdXMgJFxcaGF0e3l9X2kkIHBlcm1pdGUgaWRlbnRpZmljYXIgdGFsIHZpb2xhw6fDo28gZSBxdWFpcyBhcyBpbXBsaWNhw6fDtWVzIGRlc3NhIGRlc2NvYmVydGEgcGFyYSBhIG1hdHJpeiBkZSB2YXJpw6JuY2lhLWNvdmFyacOibmNpYSAkXFxzaWdtYV4yKFxcbWF0aGJme0l9LVxcbWF0aGJme0h9KSQuIiwgImRpY2EiOiAiQ29uc2lkZXJlIHF1ZSBhIG1hdHJpeiAkXFxtYXRoYmZ7SH0kIMOpIGEgbWF0cml6IGNoYXDDqXUgZSBxdWUgbyBwcmVzc3Vwb3N0byBkZSBob21vY2VkYXN0aWNpZGFkZSBzaW1wbGlmaWNhIGEgZXN0cnV0dXJhIGRlIHZhcmnDom5jaWEgcGFyYSB1bWEgY29uc3RhbnRlIGVzY2FsYXIgJFxcc2lnbWFeMiQuIE8gcXVlIGFjb250ZWNlIGNvbSBlc3NhIHNpbXBsaWZpY2HDp8OjbyBzZSBhIHZhcmnDom5jaWEgZG9zIHJlc8OtZHVvcyBkZXBlbmRlciBkZSAkaSQ/IiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgYW7DoWxpc2UgZ3LDoWZpY2EgZG8gZ3LDoWZpY28gJFxcaGF0e2V9X2kkIHZzLiAkXFxoYXR7eX1faSQgYnVzY2EgdmVyaWZpY2FyIHNlIGEgZGlzcGVyc8OjbyBkb3MgcG9udG9zIMOpIGNvbnN0YW50ZSBlbSB0b2RvIG8gaW50ZXJ2YWxvIGRvIGVpeG8gZGFzIGFic2Npc3Nhcy4iLCAiU2UgZm9yIG9ic2VydmFkbyB1bSBmb3JtYXRvIGRlICdmdW5pbCcgb3UgcXVhbHF1ZXIgcGFkcsOjbyBkZSB2YXJpYWJpbGlkYWRlIG7Do28gY29uc3RhbnRlLCB0ZW1vcyBpbmTDrWNpb3MgZGUgcXVlICRcXHRleHR7VmFyfShcXHZhcmVwc2lsb25faSkgPSBcXHNpZ21hX2leMiBcXG5lcSBcXHNpZ21hXjIkLiIsICJObyBtb2RlbG8gbGluZWFyIGNsw6Fzc2ljbywgYXNzdW1lLXNlIHF1ZSBhIHZhcmnDom5jaWEgZG9zIGVycm9zIMOpIGNvbnN0YW50ZSwgbyBxdWUgbm9zIGxldmEgYSAkXFx0ZXh0e1Zhcn0oXFxib2xkc3ltYm9se1xcdmFyZXBzaWxvbn0pID0gXFxzaWdtYV4yIFxcbWF0aGJme0l9JC4iLCAiQSBtYXRyaXogZGUgdmFyacOibmNpYS1jb3ZhcmnDom5jaWEgZG9zIHJlc8OtZHVvcywgc29iIGEgcHJlbWlzc2EgZGUgaG9tb2NlZGFzdGljaWRhZGUsIMOpIGRhZGEgcG9yICRcXHRleHR7VmFyfShcXGhhdHtcXG1hdGhiZntlfX0pID0gXFxzaWdtYV4yKFxcbWF0aGJme0l9LVxcbWF0aGJme0h9KSQuIiwgIlNlIGEgdmFyacOibmNpYSBuw6NvIGZvciBjb25zdGFudGUgKGhldGVyb2NlZGFzdGljaWRhZGUpLCBlc3NhIGZvcm11bGHDp8OjbyBkZWl4YSBkZSBzZXIgdsOhbGlkYSwgcG9pcyBhIHZhcmnDom5jaWEgcGFzc2EgYSBzZXIgdW1hIGZ1bsOnw6NvIGRvcyBkYWRvcyAkXFxtYXRoYmZ7eH1faSQsIHRvcm5hbmRvIGFzIGVzdGltYXRpdmFzIHBvciBNw61uaW1vcyBRdWFkcmFkb3MgT3JkaW7DoXJpb3MgKE1RTykgaW5lZmljaWVudGVzIGUgaW52YWxpZGFuZG8gb3MgdGVzdGVzIGRlIGhpcMOzdGVzZXMgdXN1YWlzIHF1ZSBkZXBlbmRlbSBkZSAkXFxzaWdtYV4yJCBjb25zdGFudGUuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTsOtdmVhIEJpc3BvLCBBdWxhIDEzOiBBbsOhbGlzZSBkZSBSZXPDrWR1b3Mgbm8gTVJMUywgREVTVC1VRkJBIDIwMjUuMSwgU2xpZGUgMyIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bWEgYW7DoWxpc2UgZGUgcmVncmVzc8OjbywgZm9pIHZlcmlmaWNhZG8gcXVlIG8gbW9kZWxvIGFwcmVzZW50YSB1bSBwYWRyw6NvIGRlIGN1cnZhdHVyYSBubyBncsOhZmljbyBkZSByZXPDrWR1b3MgJFxcaGF0e2V9X2kkIHZlcnN1cyB2YWxvcmVzIGFqdXN0YWRvcyAkXFxoYXR7eX1faSQuIEV4cGxpcXVlIHBvciBxdWUgYSBwcmVzZW7Dp2EgZGUgY3VydmF0dXJhIG5vIGdyw6FmaWNvIGRlIHJlc8OtZHVvcyBpbmRpY2EgdW0gcHJvYmxlbWEgZGUgZXNwZWNpZmljYcOnw6NvIGRvIG1vZGVsbyBlIHF1YWwgbyBpbXBhY3RvIGRpc3NvIHBhcmEgbyBwcmVzc3Vwb3N0byBkZSBsaW5lYXJpZGFkZS4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIG8gbW9kZWxvIGxpbmVhciBhc3N1bWUgJFxcbWF0aGJie0V9KFxcdmFyZXBzaWxvbl9pKSA9IDAkLiBTZSBvcyByZXPDrWR1b3MgbW9zdHJhbSB1bWEgY3VydmEsIG8gcXVlIGlzc28gaW1wbGljYSBwYXJhIG8gY29tcG9uZW50ZSBzaXN0ZW3DoXRpY28gZG8gbW9kZWxvPyIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJPIGdyw6FmaWNvIGRlIHJlc8OtZHVvcyAkXFxoYXR7ZX1faSQgdmVyc3VzICRcXGhhdHt5fV9pJCBkZXZlIGV4aWJpciB1bWEgbnV2ZW0gYWxlYXTDs3JpYSBkZSBwb250b3MgY2VudHJhZGEgZW0gemVybyBjYXNvIG8gbW9kZWxvIGVzdGVqYSBiZW0gZXNwZWNpZmljYWRvLiIsICJBIHByZXNlbsOnYSBkZSB1bWEgY3VydmF0dXJhIHNpc3RlbcOhdGljYSBpbmRpY2EgcXVlIG8gdmFsb3IgZXNwZXJhZG8gZG9zIHJlc8OtZHVvcyBuw6NvIMOpIGNvbnN0YW50ZSwgb3Ugc2VqYSwgJFxcbWF0aGJie0V9KFxcaGF0e2V9X2kpIFxuZXEgMCQgZW0gZGlmZXJlbnRlcyByZWdpw7VlcyBkZSAkXFxoYXR7eX1faSQuIiwgIklzc28gc2lnbmlmaWNhIHF1ZSBhIHJlbGHDp8OjbyBlbnRyZSBhcyB2YXJpw6F2ZWlzIG7Do28gZm9pIHRvdGFsbWVudGUgY2FwdHVyYWRhIHBlbG8gbW9kZWxvIGxpbmVhciwgdmlvbGFuZG8gbyBwcmVzc3Vwb3N0byBkZSBxdWUgJFxcbWF0aGJie0V9KFxcbWF0aGJme1l9KSA9IFxcbWF0aGJme1h9XFxib2xkc3ltYm9se1xcYmV0YX0kLiIsICJFbSB0ZXJtb3MgcHLDoXRpY29zLCBvIG1vZGVsbyBvbWl0ZSB0ZXJtb3MgKGNvbW8gdGVybW9zIHF1YWRyw6F0aWNvcyBvdSB0cmFuc2Zvcm1hw6fDtWVzIGRlIHZhcmnDoXZlaXMpIHF1ZSBkZXZlcmlhbSBjb21wb3IgYSBlc3RydXR1cmEgZGEgbcOpZGlhLCBvIHF1ZSBjYXJhY3Rlcml6YSBlcnJvIGRlIGVzcGVjaWZpY2HDp8Ojby4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJOw612ZWEgQmlzcG8sIEF1bGEgMTM6IEFuw6FsaXNlIGRlIFJlc8OtZHVvcyBubyBNUkxTLCBERVNULVVGQkEgMjAyNS4xLCBTbGlkZSA1IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIk5hIGlkZW50aWZpY2HDp8OjbyBkZSBwb250b3MgZGUgYWxhdmFuY2Egbm8gTW9kZWxvIGRlIFJlZ3Jlc3PDo28gTGluZWFyIFNpbXBsZXMgKE1STFMpLCBvIGNyaXTDqXJpbyB1dGlsaXphZG8gw6kgbyB2YWxvciBkYSBkaWFnb25hbCBkYSBtYXRyaXogJFxcbWF0aGJme0h9JCAobWF0cml6IGNoYXDDqXUpLCBkYWRvIHBvciAkaF97aWl9JC4gU2VuZG8gJGhfe2lpfSA9IFxcbGVmdCggXFxmcmFjezF9e259ICsgXFxmcmFjeyh4X2kgLSBcXGJhcnt4fSleMn17U197WFh9fSBcXHJpZ2h0KSQsIGNhbGN1bGUgbyBsaW1pdGUgdGXDs3JpY28gZGUgYWxhdmFuY2EgcGFyYSB1bWEgYW1vc3RyYSBkZSAkbj0yNSQgb2JzZXJ2YcOnw7VlcyBlbSB1bSBtb2RlbG8gY29tIHVtYSB2YXJpw6F2ZWwgcHJlZGl0b3JhLCBjb25zaWRlcmFuZG8gbyBjcml0w6lyaW8gZGUgJGhfe2lpfSA+IFxcZnJhY3syKHArMSl9e259JCwgb25kZSAkcCQgw6kgbyBuw7ptZXJvIGRlIHBhcsOibWV0cm9zIGRvIG1vZGVsbyAoaW5jbHVpbmRvIG8gaW50ZXJjZXB0bykuIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBubyBtb2RlbG8gJFkgPSBcXGJldGFfMCArIFxcYmV0YV8xIFggKyBcXHZhcmVwc2lsb24kLCB0ZW1vcyAkcCsxJCBwYXLDom1ldHJvcywgb25kZSAkcD0xJCDDqSBhIHZhcmnDoXZlbCBwcmVkaXRvcmEuIFBvcnRhbnRvLCAkcCsxID0gMiQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgZsOzcm11bGEgcGFyYSBpZGVudGlmaWNhciBwb250b3MgZGUgYWxhdmFuY2Egw6kgJGhfe2lpfSA+IFxcZnJhY3syKHArMSl9e259JC4iLCAiUGFyYSB1bSBNUkxTLCBvIG1vZGVsbyBwb3NzdWkgZG9pcyBwYXLDom1ldHJvczogaW50ZXJjZXB0byAoJFxcYmV0YV8wJCkgZSBpbmNsaW5hw6fDo28gKCRcXGJldGFfMSQpLCBsb2dvICRwKzEgPSAyJC4iLCAiQ29tICRuID0gMjUkLCBzdWJzdGl0dcOtbW9zIG5hIGbDs3JtdWxhOiAkaF97XFx0ZXh0e2xpbX19ID0gXFxmcmFjezIgXFx0aW1lcyAyfXsyNX0kLiIsICJSZWFsaXphbmRvIG8gY8OhbGN1bG86ICRoX3tcXHRleHR7bGltfX0gPSBcXGZyYWN7NH17MjV9ID0gMC4xNiQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTsOtdmVhIEJpc3BvLCBBdWxhIDEzOiBBbsOhbGlzZSBkZSBSZXPDrWR1b3Mgbm8gTVJMUywgREVTVC1VRkJBIDIwMjUuMSwgU2xpZGUgMTEiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjE2fSwgeyJlbnVuY2lhZG8iOiAiRGFkYSBhIHPDqXJpZSBkZSByZXPDrWR1b3Mgb3JkZW5hZG9zICRcXGhhdHtlfV97KGkpfSQgZGUgdW0gbW9kZWxvIGFqdXN0YWRvIGNvbSAkbj01JCBvYnNlcnZhw6fDtWVzOiAkXFxoYXR7ZX1feygxKX09LTEsNTsgXFxoYXR7ZX1feygyKX09LTAsNTsgXFxoYXR7ZX1feygzKX09MCwxOyBcXGhhdHtlfV97KDQpfT0wLDQ7IFxcaGF0e2V9X3soNSl9PTEsNSQuIFN1cG9uZG8gcXVlIGEgbcOpZGlhIGRvcyByZXPDrWR1b3MgJFxcYmFye1xcaGF0e2V9fSA9IDAkIGUgdXRpbGl6YW5kbyBvcyBjb2VmaWNpZW50ZXMgJGFfaSQgdGFiZWxhZG9zIHBhcmEgJG49NSQgY29tbyAkYV8xPTAsNjg3MiwgYV8yPTAsMTY3NywgYV8zPTAsIGFfND0tMCwxNjc3LCBhXzU9LTAsNjg3MiQsIGNhbGN1bGUgYSBlc3RhdMOtc3RpY2EgJFckIGRlIFNoYXBpcm8tV2lsay4iLCAiZGljYSI6ICJBcGxpcXVlIGEgZsOzcm11bGEgJFcgPSBcXGZyYWN7KFxcc3VtX3tpPTF9XntufSBhX2kgXFxoYXR7ZX1feyhpKX0pXjJ9e1xcc3VtX3tpPTF9XntufSAoXFxoYXR7ZX1faSAtIFxcYmFye1xcaGF0e2V9fSleMn0kLiBMZW1icmUtc2UgcXVlIG8gZGVub21pbmFkb3Igw6kgYSBzb21hIGRvcyBxdWFkcmFkb3MgZG9zIHJlc8OtZHVvcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUHJpbWVpcm8sIGNhbGN1bGFtb3MgbyBudW1lcmFkb3I6ICQoXFxzdW0gYV9pIFxcaGF0e2V9X3soaSl9KV4yID0gWygwLDY4NzIgXFx0aW1lcyAtMSw1KSArICgwLDE2NzcgXFx0aW1lcyAtMCw1KSArICgwIFxcdGltZXMgMCwxKSArICgtMCwxNjc3IFxcdGltZXMgMCw0KSArICgtMCw2ODcyIFxcdGltZXMgMSw1KV1eMiQuIiwgIlNvbWF0w7NyaW8gZG8gbnVtZXJhZG9yOiAkKC0xLDAzMDggLSAwLDA4Mzg1ICsgMCAtIDAsMDY3MDggLSAxLDAzMDgpXjIgPSAoLTIsMjEyNTMpXjIgXFxhcHByb3ggNCw4OTUzJC4iLCAiQWdvcmEsIGNhbGN1bGFtb3MgbyBkZW5vbWluYWRvciAoU29tYSBkZSBRdWFkcmFkb3MgZG9zIHJlc8OtZHVvcyk6ICRcXHN1bSBcXGhhdHtlfV9pXjIgPSAoLTEsNSleMiArICgtMCw1KV4yICsgKDAsMSleMiArICgwLDQpXjIgKyAoMSw1KV4yID0gMiwyNSArIDAsMjUgKyAwLDAxICsgMCwxNiArIDIsMjUgPSA0LDkyJC4iLCAiUG9yIGZpbSwgYSBlc3RhdMOtc3RpY2EgJFcgPSBcXGZyYWN7NCw4OTUzfXs0LDkyfSBcXGFwcHJveCAwLDk5NSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjk5NX0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlIG8gcGFwZWwgZG8gUVEtcGxvdCBuYSB2ZXJpZmljYcOnw6NvIGRlIG5vcm1hbGlkYWRlIGRvcyByZXPDrWR1b3MgZW0gbW9kZWxvcyBkZSByZWdyZXNzw6NvLiBQb3IgcXVlIG9ic2VydmFyIG8gYWxpbmhhbWVudG8gZG9zIHBvbnRvcyBlbSByZWxhw6fDo28gYSB1bWEgcmV0YSDDqSB1bSBkaWFnbsOzc3RpY28gZGUgbm9ybWFsaWRhZGU/IiwgImRpY2EiOiAiQ29uc2lkZXJlIG8gY29uY2VpdG8gZGUgcXVhbnRpcyB0ZcOzcmljb3MgZGUgdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCB2ZXJzdXMgb3MgcXVhbnRpcyBvYnNlcnZhZG9zIG5hIGFtb3N0cmEgZG9zIHJlc8OtZHVvcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiTyBRUS1wbG90IChHcsOhZmljbyBRdWFudGlsLVF1YW50aWwpIGNvbXBhcmEgb3MgcXVhbnRpcyBhbW9zdHJhaXMgZG9zIHJlc8OtZHVvcyAkXFxoYXR7ZX1feyhpKX0kIGNvbnRyYSBvcyBxdWFudGlzIHRlw7NyaWNvcyBkYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgcGFkcsOjbyAkTigwLDEpJC4iLCAiU2Ugb3MgcmVzw61kdW9zIHNlZ3VlbSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLCBlc3BlcmEtc2UgdW1hIHJlbGHDp8OjbyBsaW5lYXIgZW50cmUgb3MgcGFyZXMgb3JkZW5hZG9zICQodV9pLCBcXGhhdHtlfV97KGkpfSkkLCBvbmRlICR1X2kkIHPDo28gb3MgcXVhbnRpcyBlc3BlcmFkb3MgcGFyYSB1bWEgbm9ybWFsIHBhZHLDo28uIiwgIk8gYWxpbmhhbWVudG8gZG9zIHBvbnRvcyBhbyBsb25nbyBkYSByZXRhIGluZGljYSBxdWUgYSBmb3JtYSAoYXNzaW1ldHJpYSwgY3VydG9zZSkgZG9zIGRhZG9zIGFtb3N0cmFpcyBjb25kaXogY29tIGEgZm9ybWEgZ2F1c3NpYW5hLiIsICJEZXN2aW9zIG5hcyBleHRyZW1pZGFkZXMgaW5kaWNhbSBjYXVkYXMgcGVzYWRhcyBvdSBsZXZlcyAodmlvbGHDp8OjbyBkYSBub3JtYWxpZGFkZSksIGVucXVhbnRvIGN1cnZhdHVyYXMgc3VnZXJlbSBhc3NpbWV0cmlhLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDUiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIGNhc28gc29icmUgbyBjb25zdW1vIGRlIGVuZXJnaWEsIG8gcGVzcXVpc2Fkb3IgZW5jb250cm91IGV2aWTDqm5jaWFzIGRlIG7Do28tbm9ybWFsaWRhZGUgbm9zIHJlc8OtZHVvcyBhdHJhdsOpcyBkbyB0ZXN0ZSBkZSBTaGFwaXJvLVdpbGsgKCRwXFx0ZXh0ey12YWxvcn0gPCAwLDAxJCkuIERpc2NvcnJhIHNvYnJlIGFzIGNvbnNlcXXDqm5jaWFzIGRlc3NhIHZpb2xhw6fDo28gcGFyYSBhIHZhbGlkYWRlIGRhcyBpbmZlcsOqbmNpYXMgZG8gbW9kZWxvIGxpbmVhciAoaW50ZXJ2YWxvcyBkZSBjb25maWFuw6dhIGUgdGVzdGVzIGRlIGhpcMOzdGVzZXMpIGUgcXVhbCBjb21wb3J0YW1lbnRvIGRlIGFtb3N0cmFzIGdyYW5kZXMgdGVuZGUgYSBtaXRpZ2FyIGVzdGUgcHJvYmxlbWEuIiwgImRpY2EiOiAiUmVmbGl0YSBzb2JyZSBvIFRlb3JlbWEgQ2VudHJhbCBkbyBMaW1pdGUgZSBhIHZhbGlkYWRlIGRvcyBlc3RpbWFkb3JlcyBkZSBNw61uaW1vcyBRdWFkcmFkb3MgT3JkaW7DoXJpb3MgKE1RTykgaW5kZXBlbmRlbnRlbWVudGUgZGEgbm9ybWFsaWRhZGUuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgc3Vwb3Npw6fDo28gZGUgbm9ybWFsaWRhZGUgZG9zIGVycm9zIMOpIG5lY2Vzc8OhcmlhIHBhcmEgcXVlIG9zIHRlc3RlcyAkdCQgZSAkRiQgdGVuaGFtIGV4YXRhbWVudGUgYXMgZGlzdHJpYnVpw6fDtWVzIHQtU3R1ZGVudCBlIEYgc29iICRIXzAkIHBhcmEgcGVxdWVuYXMgYW1vc3RyYXMuIiwgIkEgbsOjby1ub3JtYWxpZGFkZSBpbnZhbGlkYSBhcyBpbmZlcsOqbmNpYXMgKGludGVydmFsb3MgZGUgY29uZmlhbsOnYSBlIHAtdmFsb3JlcykgZW0gYW1vc3RyYXMgcGVxdWVuYXMuIiwgIkVtIGFtb3N0cmFzIGdyYW5kZXMsIHBlbG8gVGVvcmVtYSBDZW50cmFsIGRvIExpbWl0ZSwgYSBkaXN0cmlidWnDp8OjbyBkb3MgZXN0aW1hZG9yZXMgJFxcaGF0e1xcYmV0YX1faiQgdGVuZGUgw6Agbm9ybWFsaWRhZGUsIGluZGVwZW5kZW50ZW1lbnRlIGRhIGRpc3RyaWJ1acOnw6NvIGRvcyBlcnJvcywgdG9ybmFuZG8gYXMgaW5mZXLDqm5jaWFzIGFzc2ludG90aWNhbWVudGUgdsOhbGlkYXMuIiwgIlBvcnRhbnRvLCBvIGltcGFjdG8gZGEgbsOjby1ub3JtYWxpZGFkZSDDqSBzZXZlcm8gZW0gcGVxdWVuYXMgYW1vc3RyYXMsIG1hcyByZWR1emlkbyBjb25mb3JtZSBvIHRhbWFuaG8gYW1vc3RyYWwgJG4kIGNyZXNjZS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gZGUgcmVncmVzc8OjbyBjb20gJG49MjAkIGUgJHA9MiQsIHVtYSBvYnNlcnZhw6fDo28gZXNwZWPDrWZpY2EgcG9zc3VpIHVtYSBhbGF2YW5jYSAkaF97aWl9ID0gMC42JC4gRGV0ZXJtaW5lIG8gbGltaWFyIGNyw610aWNvIGRlIGFsYXZhbmNhIGUgZGlzY3V0YSBzZSBlc3RhIG9ic2VydmHDp8OjbyBkZXZlIHNlciBjbGFzc2lmaWNhZGEgY29tbyB1bSBwb250byBkZSBhbGF2YW5jYS4gRW0gc2VndWlkYSwgY2FsY3VsZSBhIHZhcmnDom5jaWEgZG8gcmVzw61kdW8gcGFyYSBlc3RlIHBvbnRvLCBhc3N1bWluZG8gdW1hIHZhcmnDom5jaWEgcmVzaWR1YWwgZG8gbW9kZWxvICRcXHNpZ21hXjIgPSAxLjAkLiIsICJkaWNhIjogIlVzZSBhIGbDs3JtdWxhIGRvIGxpbWlhciAkaF4qID0gXFxmcmFjezIocCsxKX17bn0kIGUgYSBkZWZpbmnDp8OjbyBkZSB2YXJpw6JuY2lhIGRvIHJlc8OtZHVvICRcXHRleHR7VmFyfShcXGhhdHtlfV9pKSA9IFxcc2lnbWFeMigxIC0gaF97aWl9KSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IENhbGN1bGFyIG8gbGltaWFyIGNyw610aWNvOiAkJGheKiA9IFxcZnJhY3syKDIrMSl9ezIwfSA9IFxcZnJhY3s2fXsyMH0gPSAwLjMkJCIsICJQYXNzbyAyOiBDb21wYXJhw6fDo286IENvbW8gJGhfe2lpfSA9IDAuNiA+IDAuMyQsIGEgb2JzZXJ2YcOnw6NvIMOpIGNsYXNzaWZpY2FkYSBjb21vIHVtIHBvbnRvIGRlIGFsYXZhbmNhIGRlIGFsdGEgaW5mbHXDqm5jaWEuIiwgIlBhc3NvIDM6IEPDoWxjdWxvIGRhIHZhcmnDom5jaWEgZG8gcmVzw61kdW86ICQkXFx0ZXh0e1Zhcn0oXFxoYXR7ZX1faSkgPSBcXHNpZ21hXjIoMSAtIGhfe2lpfSkgPSAxLjAgXFxjZG90ICgxIC0gMC42KSA9IDAuNCQkIiwgIlBhc3NvIDQ6IEludGVycHJldGHDp8OjbzogVW1hIGFsYXZhbmNhIGFsdGEgKCQwLjYkKSByZWR1eiBhIHZhcmnDom5jaWEgZG8gcmVzw61kdW8gcGFyYSAkMC40JCwgbyBxdWUgcG9kZSBhcnRpZmljaWFsbWVudGUgdG9ybmFyIG8gcmVzw61kdW8gcGVxdWVubywgbWFzY2FyYW5kbyBhIHByZXNlbsOnYSBkZSB1bSBvdXRsaWVyLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC40fSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIGEgbWF0cml6IGRlIHByb2plw6fDo28gJFxcbWF0aGJme0h9ID0gXFxtYXRoYmZ7WH0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9XFxtYXRoYmZ7WH1ee1xcdG9wfSQuIEV4cGxpcXVlLCBhdHJhdsOpcyBkYSDDoWxnZWJyYSBtYXRyaWNpYWwsIHBvciBxdWUgYSBzb21hIGRvcyBlbGVtZW50b3MgZGEgZGlhZ29uYWwgcHJpbmNpcGFsIGRhIG1hdHJpeiAkXFxtYXRoYmZ7SH0kLCBvdSBzZWphLCAkXFxzdW0gaF97aWl9JCwgw6kgaWd1YWwgYSAkcCsxJCAoY29uc2lkZXJhbmRvIG8gaW50ZXJjZXB0bykuIE8gcXVlIGVzc2EgcHJvcHJpZWRhZGUgaW1wbGljYSBzb2JyZSBhIG3DqWRpYSBkYXMgYWxhdmFuY2FzPyIsICJkaWNhIjogIlV0aWxpemUgYSBwcm9wcmllZGFkZSBkbyB0cmHDp28gZGEgbWF0cml6LCBvbmRlICRcXHRleHR7dHJ9KFxcbWF0aGJme0F9XFxtYXRoYmZ7Qn0pID0gXFx0ZXh0e3RyfShcXG1hdGhiZntCfVxcbWF0aGJme0F9KSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IERlZmluaXIgbyB0cmHDp28gZGEgbWF0cml6ICRcXG1hdGhiZntIfSQ6ICQkXFx0ZXh0e3RyfShcXG1hdGhiZntIfSkgPSBcXHRleHR7dHJ9KFxcbWF0aGJme1h9KFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfVxcbWF0aGJme1h9XntcXHRvcH0pJCQiLCAiUGFzc28gMjogQXBsaWNhciBhIHByb3ByaWVkYWRlIGPDrWNsaWNhIGRvIHRyYcOnbzogJCRcXHRleHR7dHJ9KFxcbWF0aGJme0h9KSA9IFxcdGV4dHt0cn0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfSkgPSBcXHRleHR7dHJ9KFxcbWF0aGJme0l9X3twKzF9KSQkIiwgIlBhc3NvIDM6IE8gdHJhw6dvIGRhIG1hdHJpeiBpZGVudGlkYWRlIGRlIGRpbWVuc8OjbyAkcCsxJCDDqSBhIHNvbWEgZG9zIHNldXMgZWxlbWVudG9zIGRpYWdvbmFpczogJCRcXHN1bV97aT0xfV5uIGhfe2lpfSA9IHArMSQkIiwgIlBhc3NvIDQ6IENvbmNsdXPDo286IEEgbcOpZGlhIGRhcyBhbGF2YW5jYXMgw6kgJFxcYmFye2h9ID0gXFxmcmFje3ArMX17bn0kLiBJc3NvIGltcGxpY2EgcXVlIGFsYXZhbmNhcyBpbmRpdmlkdWFpcyBzw6NvIGRlc3Zpb3MgZW0gcmVsYcOnw6NvIGEgZXNzZSB2YWxvciBtw6lkaW8gY2VudHJhbC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBhbmFsaXN0YSBkZSBJb1QgbW9uaXRvcmEgYSB0ZW1wZXJhdHVyYSBkZSB1bSBzZXJ2aWRvci4gRW0gdW0gYWp1c3RlIGxpbmVhciwgb2J0ZXZlICRuPTEwMCQgb2JzZXJ2YcOnw7Vlcy4gVW0gcG9udG8gYXByZXNlbnRvdSByZXPDrWR1byAkXFxoYXR7ZX1faSA9IDUuMCQgZSBhbGF2YW5jYSAkaF97aWl9ID0gMC4xJC4gQWRtaXRpbmRvIHF1ZSBvIGRlc3ZpbyBwYWRyw6NvIHJlc2lkdWFsIGVzdGltYWRvIHNlamEgJHMgPSAyLjAkLCBjYWxjdWxlIG8gdmFsb3IgZG8gcmVzw61kdW8gc3R1ZGVudGl6YWRvIHBhcmEgZXN0YSBvYnNlcnZhw6fDo28gZSBhdmFsaWUgc2UgZWxhIMOpIHVtIG91dGxpZXIuIiwgImRpY2EiOiAiTyByZXPDrWR1byBzdHVkZW50aXphZG8gw6kgZGFkbyBwb3IgJHRfaSA9IFxcZnJhY3tcXGhhdHtlfV9pfXtzIFxcc3FydHsxIC0gaF97aWl9fX0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiBJZGVudGlmaWNhciBvcyBwYXLDom1ldHJvczogJFxcaGF0e2V9X2kgPSA1LjAkLCAkcyA9IDIuMCQsICRoX3tpaX0gPSAwLjEkLiIsICJQYXNzbyAyOiBDYWxjdWxhciBvIGRlc3ZpbyBwYWRyw6NvIGRvIHJlc8OtZHVvOiAkJFxcdGV4dHtEUH0oXFxoYXR7ZX1faSkgPSBzIFxcc3FydHsxIC0gaF97aWl9fSA9IDIuMCBcXHNxcnR7MSAtIDAuMX0gPSAyLjAgXFxzcXJ0ezAuOX0gXFxhcHByb3ggMi4wIFxcY2RvdCAwLjk0ODcgPSAxLjg5NzQkJCIsICJQYXNzbyAzOiBDYWxjdWxhciBvIHJlc8OtZHVvIHN0dWRlbnRpemFkbzogJCR0X2kgPSBcXGZyYWN7NS4wfXsxLjg5NzR9IFxcYXBwcm94IDIuNjM1JCQiLCAiUGFzc28gNDogQXZhbGlhw6fDo286IENvbW8gJHwyLjYzNXwgPiAyJCwgbyB2YWxvciDDqSBjb25zaWRlcmFkbyB1bSBvdXRsaWVyIGVzdGF0aXN0aWNhbWVudGUgc2lnbmlmaWNhdGl2byBuYSB2YXJpw6F2ZWwgcmVzcG9zdGEuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMCwgMi42MzVdLCB5PVswLCAwXSwgbW9kZT0nbWFya2VycycsIG1hcmtlcj1kaWN0KGNvbG9yPVwiIzk5MUIxQlwiLCBzaXplPTEyKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT1cIjxiPlJlc8OtZHVvIFN0dWRlbnRpemFkbyBDYWxjdWxhZG88L2I+XCIsIHhheGlzX3RpdGxlPVwiUmVzw61kdW8gU3R1ZGVudGl6YWRvXCIsIHlheGlzPWRpY3QodmlzaWJsZT1GYWxzZSkpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAyLjYzNX1dfQ==').decode('utf-8'))


    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo do total para barra de progresso
    total_mcq = len(dados_exercicios.get("questoes_multipla_escolha", []))
    total_disc = len(dados_exercicios.get("questoes_discursivas", []))
    total_exercicios = total_mcq + total_disc
    
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v is True)
    
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    
    st.divider()
    
    # --- Seção de Questões de Múltipla Escolha ---
    st.subheader("📝 Questões de Múltipla Escolha")
    for i, questao in enumerate(dados_exercicios.get("questoes_multipla_escolha", [])):
        st.markdown(f"**Questão {i + 1}:** {questao.get('enunciado', '')}")
        
        # Exibição de Referência
        ref = questao.get('referencia_livro')
        if ref:
            st.markdown(f"📖 *Referência: {ref}*")
        
        # Exibição de Código Plotly
        code_plotly = questao.get("codigo_plotly")
        if code_plotly:
            try:
                local_vars = {}
                exec(code_plotly, globals(), local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True)
            except Exception as e:
                st.warning("Erro ao renderizar gráfico interativo.")
    
        # Opções
        alternativas = questao.get("alternativas", {})
        escolha = st.radio(
            "Selecione a alternativa correta:", 
            options=list(alternativas.keys()), 
            format_func=lambda x: f"{x}) {alternativas[x]}",
            key=f"radio_mcq_{i}"
        )
    
        # Dica
        if st.button("💡 Dica", key=f"dica_mcq_{i}"):
            st.info(questao.get("dica", "Dica indisponível."))
    
        # Verificação
        if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
            correta = questao.get("alternativa_correta")
            if escolha == correta:
                st.success("Correto! Muito bem.")
                st.session_state.respostas_certas[f"mcq_{i}"] = True
            else:
                st.error("Resposta incorreta. Tente novamente!")
                st.session_state.respostas_certas[f"mcq_{i}"] = False
        
        # Gabarito Comentado
        with st.expander("✅ Ver Gabarito Comentado"):
            st.write(questao.get("gabarito_comentado", "Gabarito indisponível."))
        
        st.divider()
    
    # --- Seção de Questões Discursivas ---
    st.subheader("✍️ Questões Discursivas")
    for i, questao in enumerate(dados_exercicios.get("questoes_discursivas", [])):
        st.markdown(f"**Desafio {i + 1}:** {questao.get('enunciado', '')}")
        
        ref = questao.get('referencia_livro')
        if ref:
            st.markdown(f"📖 *Referência: {ref}*")
    
        # Exibição de Código Plotly
        code_plotly = questao.get("codigo_plotly")
        if code_plotly:
            try:
                local_vars = {}
                exec(code_plotly, globals(), local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True)
            except Exception as e:
                st.warning("Erro ao renderizar gráfico interativo.")
    
        st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
    
        # Lógica de Validação Numérica ou Checkbox
        valor_esperado = questao.get("resposta_numerica_esperada")
        if valor_esperado is not None:
            user_val = st.number_input("Digite o resultado numérico calculado para validação:", key=f"num_disc_{i}", format="%.4f")
            if st.button("Validar Cálculo", key=f"btn_disc_{i}"):
                if abs(user_val - valor_esperado) <= max(0.01, 0.01 * abs(valor_esperado)):
                    st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.error("O valor calculado difere do gabarito oficial. Verifique seus arredondamentos e fórmulas.")
                    st.session_state.respostas_certas[f"disc_{i}"] = False
        else:
            concluido = st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}")
            st.session_state.respostas_certas[f"disc_{i}"] = concluido
    
        # Dica
        if st.button("💡 Dica", key=f"dica_disc_{i}"):
            st.info(questao.get("dica", "Dica indisponível."))
    
        # Resolução
        with st.expander("✅ Ver Resolução Detalhada"):
            for passo in questao.get("gabarito_passo_a_passo", []):
                st.write(f"- {passo}")
        
        st.divider()
