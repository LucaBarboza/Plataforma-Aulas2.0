import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDcgLSBUw7NwaWNvIDcuMTogRGlhZ27Ds3N0aWNvIGUgYm9uZGFkZSBkbyBhanVzdGU6IEFuw6FsaXNlIGRlIHJlc8OtZHVvcyIsICJyZWZlcmVuY2lhc19iaWJsaW9ncmFmaWNhc19maW5haXMiOiBbIkJpc3BvLCBOLiwgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzIC0gQ2FwLiAxMSwgcHAuIDcgZSBDYXAuIDEzLCBwcC4gMy0xMyIsICJGYXJhd2F5LCBKLiBKLiwgTGluZWFyIE1vZGVscyB3aXRoIFIgLSBDYXAuIDcuOCwgcHAuIDg4LTkxIl19').decode('utf-8'))

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
    
    # --- Cabeçalho do Subtópico ---
    st.header(r"Propriedades Estatísticas dos Resíduos e a Matriz Chapéu")
    
    # --- Prosa Teórica - Ritmo de Leitura ---
    st.markdown(r"""
    No vasto domínio da inferência estatística, particularmente no estudo dos modelos lineares, a transição entre a mera estimativa de parâmetros e a validação profunda da integridade do modelo marca o amadurecimento do analista de dados. 
    
    A regressão linear não busca apenas ajustar uma linha ou hiperplano que minimiza a soma dos quadrados dos erros; ela busca uma projeção geométrica que preserva a estrutura informacional contida na matriz de desenho $\mathbf{X}$.
    """)
    
    st.info(r"O vetor de resíduos, definido como $e_i = y_i - \hat{y}_i$, atua como um termômetro da adequação do modelo. Sua análise formal é operacionalizada através da matriz chapéu, que projeta as observações no espaço coluna do modelo.")
    
    st.markdown(r"""
    ### 📐 A Natureza Geométrica da Matriz Chapéu
    A designação "matriz chapéu" deriva de sua função primordial: transformar o vetor de observações $\mathbf{y}$ no vetor de preditos $\hat{\mathbf{y}}$. Algumas propriedades fundamentais incluem:
    
    - **Projeção Ortogonal:** A matriz $\mathbf{H}$ projeta $\mathbf{y}$ sobre o espaço coluna de $\mathbf{X}$.
    - **Idempotência:** A propriedade $\mathbf{H}^2 = \mathbf{H}$ garante que projeções sucessivas não alteram o resultado.
    - **Simetria:** $\mathbf{H} = \mathbf{H}^{\top}$, reforçando sua natureza de projetor ortogonal.
    """)
    
    # --- Formalismo e Dedução ---
    st.markdown(r"### 🧮 O Coração Matemático: Derivação dos Resíduos")
    
    st.latex(r"\mathbf{H} = \mathbf{X}(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}^{\top}")
    st.latex(r"\mathbf{e} = (\mathbf{I} - \mathbf{H})\mathbf{y}")
    
    st.markdown(r"Ao derivar as propriedades dos resíduos, observamos a relação estatística fundamental:")
    
    st.latex(r"\mathbb{E}(\mathbf{e}) = (\mathbf{I} - \mathbf{H})\mathbf{X}\beta = \mathbf{0}")
    st.latex(r"\text{Var}(\mathbf{e}) = \sigma^2(\mathbf{I} - \mathbf{H})")
    
    st.markdown(r"Este formalismo revela que, embora os erros populacionais sejam independentes, os resíduos apresentam uma estrutura de covariância determinada pela configuração de $\mathbf{X}$.")
    
    # --- Simulador Interativo ---
    st.subheader(r"📈 Visualizador de Matriz Chapéu e Influência")
    
    col1, col2 = st.columns(2)
    n_obs = col1.slider(r"Número de observações (n)", 10, 100, 30, key=r"n_obs_subtopico_1")
    alavanca_pos = col2.slider(r"Posição do ponto de alavanca (x)", 1, n_obs, n_obs, key=r"alavanca_pos_subtopico_1")
    
    # Cálculo interno para o simulador
    x_vals = np.linspace(0, 10, n_obs)
    y_vals = 2 * x_vals + np.random.normal(0, 2, n_obs)
    y_vals[alavanca_pos-1] = 30 # Introduzindo outlier de alavanca
    
    # Ajuste linear simples
    slope, intercept, _, _, _ = stats.linregress(x_vals, y_vals)
    y_pred = slope * x_vals + intercept
    residuos = y_vals - y_pred
    
    # Plotagem
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='markers', name=r"Observações", marker=dict(color="#1E3A8A")))
    fig.add_trace(go.Scatter(x=x_vals, y=y_pred, mode='lines', name=r"Modelo Ajustado", line=dict(color="#10B981", width=2)))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Influência da Alavancagem no Modelo</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Variável Preditora", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Resposta", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    st.info(f"Ao manipular o ponto de alavancagem em x={x_vals[alavanca_pos-1]:.1f}, observamos como a matriz chapéu redistribui a influência. O resíduo neste ponto é {residuos[alavanca_pos-1]:.2f}, demonstrando a sensibilidade estrutural do estimador.")
    
    # --- Exemplos Práticos ---
    st.markdown(r"### 📈 Casos de Aplicação Prática")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Cálculo de Variância Residual")
        st.markdown(r"Considere um conjunto de dados de pequena escala com n=4 observações onde se busca entender a influência estrutural na regressão.")
        st.latex(r"\mathbf{H} = \begin{pmatrix} 0.5 & 0.2 & 0.1 & 0.2 \\ 0.2 & 0.4 & 0.3 & 0.1 \\ 0.1 & 0.3 & 0.4 & 0.2 \\ 0.2 & 0.1 & 0.2 & 0.5 \end{pmatrix}")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Identificação da alavancagem $h_{11} = 0,5$.")
        st.markdown(r"- Cálculo da variância: $\text{Var}(e_1) = \sigma^2(1 - h_{11})$.")
        st.markdown(r"- Substituição: $\text{Var}(e_1) = 1 \cdot (1 - 0,5) = 0,5$.")
        st.success(r"O valor calculado da variância residual para a primeira observação é 0,5. Este resultado indica que o modelo confia moderadamente na precisão desta observação.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # --- Cabeçalho do Subtópico ---
    st.header(r"Diagnóstico Visual e Verificação das Suposições do Modelo")
    
    # --- Introdução Teórica ---
    st.markdown(r"""
    A estatística inferencial, em sua essência, não se encerra no momento em que os parâmetros de um modelo linear são estimados. O ajuste de um modelo é apenas o prelúdio para um processo crítico: a validação dos pressupostos teóricos. Quando postulamos um modelo linear da forma $\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$, assumimos que os erros possuem propriedades de não-viesagem, consistência e eficiência.
    
    O diagnóstico visual de resíduos emerge como a ferramenta primordial para verificar se a estrutura do modelo condiz com a realidade. Ao ignorar estes pressupostos, corremos o risco de invalidar estimativas pontuais, intervalos de confiança e testes de hipóteses.
    """)
    
    st.markdown(r"""
    **Os Três Pilares da Validação de Resíduos:**
    - **Linearidade:** A relação funcional entre variáveis deve ser capturada pelo modelo; curvaturas nos resíduos indicam falhas de especificação.
    - **Homocedasticidade:** A variância do erro deve ser constante. Padrões de "funil" nos resíduos revelam falhas nesta premissa.
    - **Normalidade:** Essencial para a validade dos testes de significância em amostras pequenas, verificada através da análise de caudas.
    """)
    
    # --- Formalismo Matemático ---
    st.subheader(r"📐 O Coração Matemático: Definição e Variância")
    st.latex(r"e_i = Y_i - \hat{Y}_i")
    st.latex(r"\text{Var}(e_i) = \sigma^2(1 - h_{ii})")
    st.info(r"Nota técnica: O valor $h_{ii}$ representa a alavancagem da observação. Observações extremas no espaço dos previsores possuem resíduos com menor variância, o que pode mascarar problemas de heterocedasticidade.")
    
    # --- Simulador Interativo ---
    st.subheader(r"🔍 Simulador: Diagnóstico de Resíduos")
    col_ctrl1, col_ctrl2 = st.columns(2)
    with col_ctrl1:
        n_pontos = st.slider(r"Tamanho da Amostra (n)", 20, 200, 50, key=r"n_subtopico_2")
        hetero_toggle = st.toggle(r"Ativar Heterocedasticidade", key=r"hetero_subtopico_2")
    with col_ctrl2:
        ruido_base = st.slider(r"Intensidade do Ruído", 0.1, 5.0, 1.0, step=0.1, key=r"ruido_subtopico_2")
    
    # Geração de dados para o simulador
    x_sim = np.linspace(0, 10, n_pontos)
    if hetero_toggle:
        erro = np.random.normal(0, ruido_base * (x_sim / 5))
    else:
        erro = np.random.normal(0, ruido_base, n_pontos)
    y_sim = 2 * x_sim + 5 + erro
    slope, intercept, _, _, _ = stats.linregress(x_sim, y_sim)
    y_pred = slope * x_sim + intercept
    residuos = y_sim - y_pred
    
    # Plotagem
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_pred, y=residuos, mode='markers', name=r"Resíduos", marker=dict(color="#1E3A8A", opacity=0.7)))
    fig.add_hline(y=0, line_dash="dash", line_color="#991B1B")
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Dispersão de Resíduos vs Valores Ajustados</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valores Ajustados", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Resíduos", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    if hetero_toggle:
        st.info(r"Observação: Com a heterocedasticidade ativada, nota-se um padrão de dispersão variável (forma de funil). Isso viola a premissa de variância constante, tornando os erros-padrão dos coeficientes subestimados ou superestimados.")
    else:
        st.success(r"Observação: O padrão de ruído parece aleatório, o que é consistente com a premissa de homocedasticidade do modelo linear.")
    
    # --- Deduções Analíticas ---
    st.subheader(r"📐 Processo de Diagnóstico Estrutural")
    st.latex(r"\mathbf{e} = (\mathbf{I} - \mathbf{H})\mathbf{y}")
    st.write(r"Onde $\mathbf{H}$ é a matriz chapéu que projeta os valores observados no espaço de predição.")
    st.latex(r"\text{Var}(e_i) = \sigma^2(1 - h_{ii})")
    st.write(r"Esta relação ajusta a variância do resíduo com base na alavancagem ($h_{ii}$) de cada ponto.")
    
    # --- Casos de Aplicação Prática ---
    st.subheader(r"📈 Casos de Aplicação Prática: Custos Industriais")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Análise de Custos")
        st.markdown(r"Num estudo de custos industriais (n=15), obteve-se um valor ajustado de 5000 para a observação i, com um resíduo de 450 e alavancagem h=0,15. A variância do erro é estimada em 2500.")
        st.latex(r"e_i = 450, \quad h_{ii} = 0,15, \quad \sigma^2 = 2500")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo da variância ajustada: $\text{Var}(e_i) = 2500 \times (1 - 0,15)$")
        st.markdown(r"- Resultado final: $\text{Var}(e_i) = 2500 \times 0,85 = 2125$")
        st.success(r"Laudo: A variância teórica de 2125 confirma que o desvio observado de 450 está dentro de uma faixa esperada, permitindo prosseguir com a análise diagnóstica.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Avaliação de Normalidade e Bondade do Ajuste")
    
    # Prosa Teórica
    st.markdown(r"""
    A suposição de normalidade dos resíduos é um pilar fundamental na inferência estatística aplicada a modelos de regressão. Esta condição garante que os testes de hipóteses sobre os coeficientes do modelo (testes t e F) possuam a validade matemática necessária para a tomada de decisão.
    """)
    
    st.markdown(r"""
    Para diagnosticar possíveis desvios desta suposição, utilizamos um conjunto de ferramentas diagnósticas que combinam análise visual e testes formais:
    - **Gráfico de Quantis (Q-Q Plot):** Ferramenta gráfica que compara os quantis dos resíduos observados contra os quantis teóricos de uma distribuição normal.
    - **Teste de Shapiro-Wilk:** Teste formal que avalia a evidência estatística contra a hipótese de normalidade.
    """)
    
    # O Coração Matemático
    st.subheader(r"📐 O Coração Matemático: Formalismo do Teste de Shapiro-Wilk")
    
    st.markdown(r"A estatística de teste $W$ é calculada ponderando os resíduos ordenados, enquanto os quantis teóricos $q_i$ são definidos pela função inversa da normal acumulada:")
    
    st.latex(r"W = \frac{(\sum_{i=1}^{n} a_i e_{(i)})^2}{\sum_{i=1}^{n} e_i^2}")
    st.latex(r"q_i = \Phi^{-1}\left(\frac{i - 0.375}{n + 0.25}\right)")
    
    st.markdown(r"**Passo a passo analítico da verificação:**")
    
    st.latex(r"e_i = Y_i - \hat{Y}_i")
    st.markdown(r"Os resíduos são dispostos em ordem crescente para o cálculo dos pesos:")
    st.latex(r"e_{(1)} \le e_{(2)} \le \dots \le e_{(n)}")
    st.markdown(r"A estatística $W$ quantifica a correlação linear entre os resíduos observados e os quantis esperados sob normalidade. Se o valor-p resultante for superior ao nível de significância $\alpha$, a hipótese de normalidade é preservada:")
    st.latex(r"\text{Se } p\text{-valor} > \alpha, \text{ aceita-se a normalidade dos erros.}")
    
    # Casos de Aplicação
    st.subheader(r"📈 Casos de Aplicação Prática: Diagnóstico de Modelos")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Teste de Shapiro-Wilk em n=15")
        st.markdown(r"Em uma análise de regressão com 15 observações, obteve-se o valor de $W = 0,9067$ com um $p\text{-valor} = 0,1207$. Avalie a hipótese de normalidade ao nível de significância de 5%.")
        
        st.latex(r"p\text{-valor} = 0,1207, \quad \alpha = 0,05")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Hipótese Nula ($H_0$):** Os resíduos seguem uma distribuição normal.")
        st.markdown(r"- **Critério de Decisão:** Como $0,1207 > 0,05$, não há evidências suficientes para rejeitar $H_0$.")
        
        st.success(r"Conclusão e Laudo Comercial: O modelo é considerado robusto para a aplicação de inferências t e F. A suposição de normalidade está preservada sob as condições testadas, permitindo confiabilidade nos intervalos de confiança calculados.")
    
    # Nota de rodapé técnica
    st.info(r"Nota: A violação da normalidade em amostras pequenas pode comprometer a validade dos intervalos de confiança. Em tais casos, recomenda-se a aplicação de transformações de Box-Cox ou o uso de métodos não-paramétricos.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Identificação de Observações Não Usuais: Outliers e Pontos de Alavanca")
    
    # Introdução e Prosa Teórica
    st.markdown(r"""
    A análise de regressão linear, embora fundamentada no método dos mínimos quadrados ordinários, exige cautela quanto à heterogeneidade dos dados. A robustez do estimador $\hat{\boldsymbol{\beta}}$ é frequentemente ameaçada por observações que se desviam do comportamento central, seja por erros de medição ou fenômenos latentes.
    """)
    
    st.info(r"A distinção entre *outlier* e ponto de alavanca é o pilar para a validade das inferências: o primeiro distorce a variável resposta, enquanto o segundo exerce pressão estrutural na configuração dos preditores.")
    
    st.markdown(r"""
    Para garantir a precisão, devemos monitorar dois perfis de anomalia:
    - **Outlier:** Observação cuja resposta $Y_i$ é surpreendente frente à previsão do modelo $\hat{Y}_i$, identificada via resíduos.
    - **Ponto de Alavanca:** Observação na matriz de desenho $\mathbf{X}$ situada em regiões de baixa densidade, capaz de inclinar o hiperplano de regressão.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Métricas de Influência")
    
    st.markdown(r"A matriz chapéu, $\mathbf{H} = \mathbf{X}(\mathbf{X}^{\top} \mathbf{X})^{-1} \mathbf{X}^{\top}$, permite isolar o efeito mecânico de cada observação:")
    st.latex(r"h_{ii} = \mathbf{X}_i(\mathbf{X}^{\top}\mathbf{X})^{-1}\mathbf{X}_i^{\top} \quad \text{ (Medida de Alavancagem)}")
    
    st.markdown(r"Para neutralizar o mascaramento em pontos de alta alavancagem, utilizamos o resíduo estudentizado:")
    st.latex(r"t_i = \frac{e_i}{\hat{\sigma}\sqrt{1-h_{ii}}} \quad \text{ (Resíduo Estudentizado)}")
    
    st.markdown(r"Critérios de diagnóstico para detecção de pontos influentes:")
    st.latex(r"h_{ii} > \frac{2(p+1)}{n} \quad \text{e} \quad |t_i| > 2")
    
    # Simulador de Influência
    st.subheader(r"📊 Simulador de Influência: Visualização de Pontos")
    
    col1, col2 = st.columns(2)
    n_pontos = col1.slider(r"Número de observações", 10, 50, 20, key="n_pontos_subtopico_4")
    toggle_outlier = col2.toggle(r"Adicionar ponto de alavanca", key="toggle_outlier_subtopico_4")
    
    # Geração de dados simulados
    np.random.seed(42)
    x = np.linspace(0, 10, n_pontos)
    y = 2 * x + np.random.normal(0, 2, n_pontos)
    
    if toggle_outlier:
        x = np.append(x, 9.5)
        y = np.append(y, 2)  # Ponto influente forçando a reta para baixo
    
    # Cálculo linear
    slope, intercept, _, _, _ = stats.linregress(x, y)
    y_pred = slope * x + intercept
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers', name='Dados', marker=dict(color='#1E3A8A')))
    fig.add_trace(go.Scatter(x=x, y=y_pred, mode='lines', name='Regressão', line=dict(color='#991B1B', width=2)))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Efeito da Alavancagem no Ajuste</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="X", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Y", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")
    
    if toggle_outlier:
        st.warning(r"Com a inclusão do ponto de alavanca, observa-se uma inclinação artificial na reta, evidenciando o efeito de fulcro que observações periféricas exercem sobre o modelo de mínimos quadrados.")
    else:
        st.success(r"O modelo apresenta estabilidade, sem observações de alta alavancagem que comprometam a estimativa dos coeficientes.")
    
    # Exemplo Prático Resolvido
    st.subheader(r"📈 Caso de Aplicação: Experimento Industrial")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Análise de Diagnóstico")
        st.markdown(r"Em um experimento industrial com $n=20$ e $p=2$, a décima observação apresenta uma alavancagem $h_{10,10} = 0,45$ e um resíduo estudentizado $|t_{10}| = 3,236$.")
        
        st.latex(r"h_{10,10} = 0,45, \quad |t_{10}| = 3,236, \quad n=20, \quad p+1=3")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Limiar de alavancagem:** $\frac{2(3)}{20} = 0,3$.")
        st.markdown(r"- **Comparação:** Como $0,45 > 0,3$ e $|3,236| > 2$, o ponto é estatisticamente crítico.")
        
        st.success(r"O ponto é classificado simultaneamente como outlier e ponto de alavanca, indicando alta influência no modelo. Recomenda-se a reavaliação dos dados originais e verificação de erro experimental.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDcgLSBUw7NwaWNvIDcuMTogRGlhZ27Ds3N0aWNvIGUgYm9uZGFkZSBkbyBhanVzdGU6IEFuw6FsaXNlIGRlIHJlc8OtZHVvcyIsICJxdWVzdG9lc19tdWx0aXBsYV9lc2NvbGhhIjogW3siZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBkZSBvdGltaXphw6fDo28gZGUgcHJvY2Vzc29zIGluZHVzdHJpYWlzIHBhcmEgcmVkdXppciBhIHZhcmlhYmlsaWRhZGUgbmEgZXNwZXNzdXJhIGRlIHBsYWNhcyBtZXTDoWxpY2FzLCB1bSBlbmdlbmhlaXJvIGFqdXN0b3UgdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyLiBBIG1hdHJpeiBjaGFww6l1LCBkZW5vdGFkYSBwb3IgJFxcbWF0aGJme0h9ID0gXFxtYXRoYmZ7WH0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9XFxtYXRoYmZ7WH1ee1xcdG9wfSQsIGRlc2VtcGVuaGEgdW0gcGFwZWwgZnVuZGFtZW50YWwgbm8gZGlhZ27Ds3N0aWNvIGRvIGFqdXN0ZS4gQ29uc2lkZXJlIHF1ZSBvIG1vZGVsbyBmb2kgYWp1c3RhZG8gcGFyYSAkbj0yMCQgb2JzZXJ2YcOnw7VlcyBjb20gJHA9MyQgdmFyacOhdmVpcyBwcmVkaXRvcmFzIChhbMOpbSBkbyBpbnRlcmNlcHRvKS4gQ29tIGJhc2UgbmFzIHByb3ByaWVkYWRlcyBlc3RhdMOtc3RpY2FzIGRvcyByZXPDrWR1b3MgZSBkYSBtYXRyaXogJFxcbWF0aGJme0h9JCwgcXVhbCBkYXMgc2VndWludGVzIGFmaXJtYcOnw7VlcyDDqSBjb3JyZXRhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBzb21hIGRvcyBlbGVtZW50b3MgZGlhZ29uYWlzIGRhIG1hdHJpeiAkXFxtYXRoYmZ7SH0kIMOpIGlndWFsIGEgJG4kLiIsICJCIjogIkEgdmFyacOibmNpYSBkb3MgcmVzw61kdW9zIMOpIGNvbnN0YW50ZSBwYXJhIHRvZGFzIGFzIG9ic2VydmHDp8O1ZXMsIGluZGVwZW5kZW50ZW1lbnRlIGRvcyB2YWxvcmVzIGRlICRoX3tpaX0kLiIsICJDIjogIk8gdmV0b3IgZGUgcmVzw61kdW9zICRcXG1hdGhiZntlfSQgw6kgZGFkbyBwb3IgJChcXG1hdGhiZntJfSAtIFxcbWF0aGJme0h9KVxcbWF0aGJme3l9JCwgc2VuZG8gZXN0ZSBvcnRvZ29uYWwgw6BzIGNvbHVuYXMgZGUgJFxcbWF0aGJme1h9JC4iLCAiRCI6ICJPcyBlbGVtZW50b3MgJGhfe2lpfSQgZGEgbWF0cml6ICRcXG1hdGhiZntIfSQgcmVwcmVzZW50YW0gYSB2YXJpw6JuY2lhIGRlIGNhZGEgb2JzZXJ2YcOnw6NvICR5X2kkLiIsICJFIjogIkEgbWF0cml6ICRcXG1hdGhiZntIfSQgbsOjbyDDqSBpZGVtcG90ZW50ZSwgcG9pcyBkZXBlbmRlIGRhIGludmVyc8OjbyBkYSBtYXRyaXogJFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgcmVsYcOnw6NvIGdlb23DqXRyaWNhIGVudHJlIG8gdmV0b3IgZGUgb2JzZXJ2YcOnw7VlcywgbyBlc3Bhw6dvIGRvIG1vZGVsbyAocHJvamV0YWRvIHBvciAkXFxtYXRoYmZ7SH0kKSBlIG8gZXNwYcOnbyBvcnRvZ29uYWwgKHByb2pldGFkbyBwb3IgJFxcbWF0aGJme0l9LVxcbWF0aGJme0h9JCkuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGFsdGVybmF0aXZhIEMgw6kgYSBjb3JyZXRhLiBQb3IgZGVmaW5pw6fDo28sIG8gdmV0b3IgZGUgcmVzw61kdW9zIMOpICRcXG1hdGhiZntlfSA9IFxcbWF0aGJme3l9IC0gXFxoYXR7XFxtYXRoYmZ7eX19JC4gQ29tbyAkXFxoYXR7XFxtYXRoYmZ7eX19ID0gXFxtYXRoYmZ7SH1cXG1hdGhiZnt5fSQsIHRlbW9zICRcXG1hdGhiZntlfSA9IChcXG1hdGhiZntJfSAtIFxcbWF0aGJme0h9KVxcbWF0aGJme3l9JC4gVW1hIHByb3ByaWVkYWRlIGNlbnRyYWwgZGEgcHJvamXDp8OjbyBvcnRvZ29uYWwgbm8gZXNwYcOnbyBkbyBtb2RlbG8gw6kgcXVlICRcXG1hdGhiZntIfVxcbWF0aGJme1h9ID0gXFxtYXRoYmZ7WH0kLCBvIHF1ZSBpbXBsaWNhIHF1ZSAkKFxcbWF0aGJme0l9IC0gXFxtYXRoYmZ7SH0pXFxtYXRoYmZ7WH0gPSBcXG1hdGhiZnswfSQsIGRlbW9uc3RyYW5kbyBxdWUgb3MgcmVzw61kdW9zIHPDo28gb3J0b2dvbmFpcyDDoHMgY29sdW5hcyBkZSAkXFxtYXRoYmZ7WH0kLiBTb2JyZSBhcyBvdXRyYXM6IEEgKHRyKCRcXG1hdGhiZntIfSQpID0gJHArMSQpLCBCIChhIHZhcmnDom5jaWEgZGVwZW5kZSBkZSAkaF97aWl9JCksIEQgKCRoX3tpaX0kIG1lZGUgYWxhdmFuY2FnZW0vaW5mbHXDqm5jaWEpLCBFICgkXFxtYXRoYmZ7SH0kIMOpIGlkZW1wb3RlbnRlIHBvciBjb25zdHJ1w6fDo28pLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW0gYW5hbGlzdGEgZGUgZGFkb3MgZGUgSW9UIG1vbml0b3JhIGEgdGVtcGVyYXR1cmEgZGUgdW0gc2Vydmlkb3IuIEFvIHJlYWxpemFyIHVtYSByZWdyZXNzw6NvIGxpbmVhciBwYXJhIHByZXZlciBhIHRlbXBlcmF0dXJhIGVtIGZ1bsOnw6NvIGRvIHRlbXBvIGRlIGF0aXZpZGFkZSwgZWxlIGlkZW50aWZpY2EgdW1hIG9ic2VydmHDp8OjbyBjb20gdW0gdmFsb3IgZGUgYWxhdmFuY2FnZW0gKCRoX3tpaX0kKSBzaWduaWZpY2F0aXZhbWVudGUgYWx0by4gU29icmUgbyBpbXBhY3RvIGRlc3NhIG9ic2VydmHDp8OjbyBuYSBtYXRyaXogY2hhcMOpdSBlIG5vcyByZXPDrWR1b3MsIGFzc2luYWxlIGEgYWx0ZXJuYXRpdmEgY29ycmV0YToiLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIlVtIHZhbG9yIGRlICRoX3tpaX0kIG11aXRvIHByw7N4aW1vIGRlIDEgaW5kaWNhIHF1ZSBhIG9ic2VydmHDp8OjbyB0ZW0gYmFpeGEgaW5mbHXDqm5jaWEgbm8gYWp1c3RlIGRvIG1vZGVsby4iLCAiQiI6ICJBIHZhcmnDom5jaWEgZG8gcmVzw61kdW8gJGVfaSQgYXNzb2NpYWRvIGEgdW1hIG9ic2VydmHDp8OjbyBjb20gYWx0YSBhbGF2YW5jYWdlbSB0ZW5kZSBhIHNlciBtZW5vciBkbyBxdWUgYSB2YXJpw6JuY2lhIGRlIHJlc8OtZHVvcyBlbSBvYnNlcnZhw6fDtWVzIGNvbSBiYWl4YSBhbGF2YW5jYWdlbS4iLCAiQyI6ICJBIG1hdHJpeiAkXFxtYXRoYmZ7SH0kIHByb2pldGEgbyB2ZXRvciBkZSBkYWRvcyBvYnNlcnZhZG9zICRcXG1hdGhiZnt5fSQgZW0gdW0gc3ViZXNwYcOnbyBkZSBkaW1lbnPDo28gJG4kLiIsICJEIjogIkEgYWxhdmFuY2FnZW0gJGhfe2lpfSQgw6kgaW5kZXBlbmRlbnRlIGRvIG7Dum1lcm8gZGUgcHJlZGl0b3JlcyBubyBtb2RlbG8uIiwgIkUiOiAiQSBzb21hIGRlIHRvZG9zIG9zIGVsZW1lbnRvcyAkaF97aWl9JCBkZXZlIHNlciBpZ3VhbCBhIDAsIHBvaXMgYSBtYXRyaXogw6kgZGUgcHJvamXDp8Ojby4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkNvbnNpZGVyZSBhIHByb3ByaWVkYWRlICRWYXIoZV9pKSA9IFxcc2lnbWFeMigxLWhfe2lpfSkkLiBPIHF1ZSBhY29udGVjZSBjb20gYSB2YXJpw6JuY2lhIGRvIHJlc8OtZHVvIHF1YW5kbyAkaF97aWl9JCBzZSBhcHJveGltYSBkZSAxPyIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBhbHRlcm5hdGl2YSBCIMOpIGEgY29ycmV0YS4gU2FiZW1vcyBxdWUgJFZhcihlX2kpID0gXFxzaWdtYV4yKDEgLSBoX3tpaX0pJC4gU2UgdW1hIG9ic2VydmHDp8OjbyBwb3NzdWkgYWx0YSBhbGF2YW5jYWdlbSAoJGhfe2lpfSQgcHLDs3hpbW8gZGUgMSksIG8gdGVybW8gJCgxLWhfe2lpfSkkIHNlIHRvcm5hIHBlcXVlbm8sIHJlZHV6aW5kbyBhIHZhcmnDom5jaWEgZG8gcmVzw61kdW8gY29ycmVzcG9uZGVudGUuIElzc28gb2NvcnJlIHBvcnF1ZSBvIG1vZGVsbyDDqSBmb3LDp2FkbyBhIHBhc3NhciBtdWl0byBwcsOzeGltbyBkZXNzZSBwb250bywgdG9ybmFuZG8gbyByZXPDrWR1byBwZXF1ZW5vIGFydGlmaWNpYWxtZW50ZS4gQSDDqSBmYWxzYSAoYWx0YSBhbGF2YW5jYWdlbSBzaWduaWZpY2EgYWx0YSBpbmZsdcOqbmNpYSksIEMgw6kgZmFsc2EgKGRpbWVuc8OjbyAkcCsxJCksIEQgw6kgZmFsc2EgKGFsYXZhbmNhZ2VtIGRlcGVuZGUgZGUgJFxcbWF0aGJme1h9JCksIEUgw6kgZmFsc2EgKGEgc29tYSDDqSAkcCsxJCkuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVswLCAwLjIsIDAuNCwgMC42LCAwLjgsIDEuMF0sIHk9WzEsIDAuOCwgMC42LCAwLjQsIDAuMiwgMF0sIG1vZGU9J2xpbmVzK21hcmtlcnMnLCBuYW1lPXInVmFyKCRlX2kkKS8kXFxzaWdtYV4yJCcsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTMpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPXInPGI+UmVsYcOnw6NvIGVudHJlIEFsYXZhbmNhZ2VtICgkaF97aWl9JCkgZSBWYXJpw6JuY2lhIGRvIFJlc8OtZHVvPC9iPicsIHhheGlzX3RpdGxlPXInQWxhdmFuY2FnZW0gKCRoX3tpaX0kKScsIHlheGlzX3RpdGxlPXInVmFyacOibmNpYSBSZWxhdGl2YScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIk7DrXZlYSBCaXNwbywgQXVsYSAxMzogQW7DoWxpc2UgZGUgUmVzw61kdW9zIG5vIE1STFMsIHAuIDMifSwgeyJlbnVuY2lhZG8iOiAiVW0gZW5nZW5oZWlybyBkZSBjb250cm9sZSBkZSBxdWFsaWRhZGUgYWp1c3RvdSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgc2ltcGxlcyBwYXJhIHByZXZlciBvIHRlbXBvIGRlIGZhbGhhIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyBlbSBmdW7Dp8OjbyBkYSB0ZW1wZXJhdHVyYSBkZSBvcGVyYcOnw6NvLiBBcMOzcyBvIGFqdXN0ZSwgYW8gYW5hbGlzYXIgbyBncsOhZmljbyBkZSByZXPDrWR1b3MgJGVfaSQgdmVyc3VzIHZhbG9yZXMgYWp1c3RhZG9zICRcXGhhdHtZfV9pJCwgbyBlbmdlbmhlaXJvIG9ic2Vydm91IHF1ZSBvcyByZXPDrWR1b3Mgc2UgZXNwYWxoYW0gZW0gdW0gZm9ybWF0byBkZSBmdW5pbCwgb25kZSBhIGFtcGxpdHVkZSBkYSBkaXNwZXJzw6NvIGRvcyByZXPDrWR1b3MgYXVtZW50YSBjb25mb3JtZSBvcyB2YWxvcmVzIGRlICRcXGhhdHtZfV9pJCBjcmVzY2VtLiBDb20gYmFzZSBuZXNzYSBvYnNlcnZhw6fDo28gdmlzdWFsLCBxdWFsIGRhcyBwcmVtaXNzYXMgYsOhc2ljYXMgZG8gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIHNpbXBsZXMgw6kgbWFpcyBwcm92YXZlbG1lbnRlIHZpb2xhZGE/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIGxpbmVhcmlkYWRlIGRhIHJlbGHDp8OjbyBlbnRyZSBhIHZhcmnDoXZlbCByZXNwb3N0YSBlIGEgdmFyacOhdmVsIHByZWRpdG9yYS4iLCAiQiI6ICJBIGhvbW9jZWRhc3RpY2lkYWRlLCBvdSBjb25zdMOibmNpYSBkYSB2YXJpw6JuY2lhIGRvcyBlcnJvcy4iLCAiQyI6ICJBIGluZGVwZW5kw6puY2lhIGRvcyBlcnJvcywgdmlvbGFkYSBwZWxhIGF1dG9jb3JyZWxhw6fDo28gdGVtcG9yYWwuIiwgIkQiOiAiQSBub3JtYWxpZGFkZSBkb3MgZXJyb3MgcG9wdWxhY2lvbmFpcyAkXFx2YXJlcHNpbG9uX2kkLiIsICJFIjogIkEgZXNwZXJhbsOnYSBtYXRlbcOhdGljYSBkb3MgZXJyb3MgcG9wdWxhY2lvbmFpcyBzZXIgemVybywgb3Ugc2VqYSwgJFxcbWF0aGJie0V9KFxcdmFyZXBzaWxvbl9pKSBcXG5lcSAwJC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk8gZm9ybWF0byBkZSBmdW5pbCDDqSB1bSBpbmRpY2F0aXZvIGNsw6Fzc2ljbyBkZSBxdWUgYSB2YXJpYWJpbGlkYWRlIG7Do28gw6kgY29uc3RhbnRlIGFvIGxvbmdvIGRhIGZhaXhhIGRlIHZhbG9yZXMgZGEgdmFyacOhdmVsIGFqdXN0YWRhLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBob21vY2VkYXN0aWNpZGFkZSBleGlnZSBxdWUgYSB2YXJpw6JuY2lhIGRvcyBlcnJvcyBwb3B1bGFjaW9uYWlzICRcXHNpZ21hXjIkIHNlamEgY29uc3RhbnRlIHBhcmEgdG9kYXMgYXMgb2JzZXJ2YcOnw7Vlcy4gTyBncsOhZmljbyBkZSByZXPDrWR1b3MgdmVyc3VzIHZhbG9yZXMgYWp1c3RhZG9zIMOpIGEgZmVycmFtZW50YSB2aXN1YWwgcHJpbcOhcmlhIHBhcmEgZXNzYSB2ZXJpZmljYcOnw6NvLiBTZSBvcyByZXPDrWR1b3MgYXByZXNlbnRhbSB1bSBwYWRyw6NvIGRlICdmdW5pbCcgb3UgJ2xlcXVlJywgaXNzbyBzdWdlcmUgcXVlIGEgdmFyacOibmNpYSBkb3MgZXJyb3MgKCRWYXIoZV9pKSQpIGVzdMOhIGF1bWVudGFuZG8gb3UgZGltaW51aW5kbyBjb25mb3JtZSBvIHZhbG9yIGRlICRcXGhhdHtZfV9pJCwgY2FyYWN0ZXJpemFuZG8gYSBoZXRlcm9jZWRhc3RpY2lkYWRlLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoMTAsIDEwMCwgMTAwKVxueSA9IDAuNSAqIHggKyBucC5yYW5kb20ubm9ybWFsKDAsIDAuMSAqIHgsIDEwMClcbnJlcyA9IHkgLSAoMC41ICogeClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PTAuNSAqIHgsIHk9cmVzLCBtb2RlPSdtYXJrZXJzJywgbWFya2VyPWRpY3QoY29sb3I9JyMxRTNBOEEnKSwgbmFtZT0nUmVzw61kdW9zJykpXG5maWcuYWRkX2hsaW5lKHk9MCwgbGluZV9kYXNoPVwiZGFzaFwiLCBsaW5lX2NvbG9yPVwiIzk5MUIxQlwiKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9XCI8Yj5HcsOhZmljbyBkZSBSZXPDrWR1b3MgdnMgVmFsb3JlcyBBanVzdGFkb3MgKEV4ZW1wbG8gZGUgSGV0ZXJvY2VkYXN0aWNpZGFkZSk8L2I+XCIsIHhheGlzX3RpdGxlPVwiVmFsb3JlcyBBanVzdGFkb3MgKCRcXGhhdHtZfV9pJClcIiwgeWF4aXNfdGl0bGU9XCJSZXPDrWR1b3MgKCRlX2kkKVwiLCB0ZW1wbGF0ZT1cInBsb3RseV93aGl0ZVwiKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkZhcmF3YXksIExpbmVhciBNb2RlbHMgd2l0aCBSLCBDYXAgNywgcC4gODMifSwgeyJlbnVuY2lhZG8iOiAiQW8gdmVyaWZpY2FyIGEgdmFsaWRhZGUgZGUgdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIGFqdXN0YWRvIHBhcmEgZGFkb3MgZGUgY3VzdG9zIGRlIHByb2R1w6fDo28sIHVtIGFuYWxpc3RhIGNvbnN0cnVpdSB1bSBncsOhZmljbyBkZSBxdWFudGlzIG5vcm1haXMgKFEtUSBQbG90KSBkb3MgcmVzw61kdW9zLiBPIGFuYWxpc3RhIG5vdG91IHF1ZSBvcyBwb250b3Mgbm8gZ3LDoWZpY28gc2UgYWZhc3RhbSBzaXN0ZW1hdGljYW1lbnRlIGRhIGxpbmhhIGRpYWdvbmFsIHRlw7NyaWNhLCBlc3BlY2lhbG1lbnRlIG5hcyBleHRyZW1pZGFkZXMgKGNhdWRhcykgZG8gZ3LDoWZpY28uIE8gcXVlIGVzc2UgZGlhZ27Ds3N0aWNvIHZpc3VhbCBwZXJtaXRlIGNvbmNsdWlyIHNvYnJlIG8gbW9kZWxvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyBtb2RlbG8gYXByZXNlbnRhIHBlcmZlaXRhIG5vcm1hbGlkYWRlLCBwb2lzIHBlcXVlbm9zIGRlc3Zpb3MgbmFzIGNhdWRhcyBzw6NvIGVzcGVyYWRvcyBkZXZpZG8gYW8gcnXDrWRvIGFsZWF0w7NyaW8uIiwgIkIiOiAiSMOhIGZvcnRlcyBldmlkw6puY2lhcyBkZSBoZXRlcm9jZWRhc3RpY2lkYWRlLCBleGlnaW5kbyB1bWEgdHJhbnNmb3JtYcOnw6NvIGxvZ2Fyw610bWljYSBuYSB2YXJpw6F2ZWwgcmVzcG9zdGEuIiwgIkMiOiAiQSBzdXBvc2nDp8OjbyBkZSBub3JtYWxpZGFkZSBkb3MgZXJyb3MgcG9wdWxhY2lvbmFpcyAkXFx2YXJlcHNpbG9uX2kkIMOpIHF1ZXN0aW9uw6F2ZWwsIGluZGljYW5kbyBxdWUgYXMgY29uY2x1c8O1ZXMgaW5mZXJlbmNpYWlzICh0ZXN0ZXMgdCBlIGludGVydmFsb3MgZGUgY29uZmlhbsOnYSkgcG9kZW0gbsOjbyBzZXIgcm9idXN0YXMuIiwgIkQiOiAiTyBtb2RlbG8gbsOjbyDDqSBsaW5lYXIsIHBvcnRhbnRvIGEgY29ycmVsYcOnw6NvIGFtb3N0cmFsICRyX3tran0kIG7Do28gw6kgdW1hIG1lZGlkYSBhZGVxdWFkYSBkZSBib25kYWRlIGRlIGFqdXN0ZS4iLCAiRSI6ICJPcyByZXPDrWR1b3MgcG9zc3VlbSBhdXRvY29ycmVsYcOnw6NvLCBzZW5kbyBuZWNlc3PDoXJpbyB1dGlsaXphciB1bSBtb2RlbG8gZGUgc8OpcmllIHRlbXBvcmFsIHBhcmEgY29ycmlnaXIgYSBkZXBlbmTDqm5jaWEuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJPIGdyw6FmaWNvIFEtUSBwbG90IGNvbXBhcmEgYSBkaXN0cmlidWnDp8OjbyBlbXDDrXJpY2EgZG9zIHJlc8OtZHVvcyBjb20gYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgdGXDs3JpY2EuIE8gZGVzdmlvIHNpc3RlbcOhdGljbyBpbmRpY2EgcXVlIGEgZGlzdHJpYnVpw6fDo28gZG9zIGVycm9zIG7Do28gc2VndWUgdW1hIGN1cnZhIG5vcm1hbC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgc3Vwb3Npw6fDo28gZGUgbm9ybWFsaWRhZGUgZG9zIGVycm9zLCAkXFx2YXJlcHNpbG9uX2kgXFxzaW0gTigwLCBcXHNpZ21hXjIpJCwgw6kgZnVuZGFtZW50YWwgcGFyYSBhIHZhbGlkYWRlIGRvcyB0ZXN0ZXMgZGUgaGlww7N0ZXNlcyBzb2JyZSBvcyBjb2VmaWNpZW50ZXMgZGEgcmVncmVzc8OjbyAoY29tbyBvcyB0ZXN0ZXMgdCBwYXJhICRcXGJldGFfaiQpLiBPIFEtUSBwbG90IMOpIG8gZ3LDoWZpY28gdXRpbGl6YWRvIHBhcmEgdmVyaWZpY2FyIHNlIG9zIHJlc8OtZHVvcyBzZWd1ZW0gZXNzYSBkaXN0cmlidWnDp8Ojby4gU2Ugb3MgcG9udG9zIHNlIGRlc3ZpYW0gZGEgcmV0YSwgY29uY2x1aS1zZSBxdWUgYSBzdXBvc2nDp8OjbyBkZSBub3JtYWxpZGFkZSBmb2kgdmlvbGFkYSwgbyBxdWUgcG9kZSBjb21wcm9tZXRlciBhIHByZWNpc8OjbyBkb3MgcC12YWxvcmVzIGUgZG9zIGludGVydmFsb3MgZGUgY29uZmlhbsOnYS4iLCAiY29kaWdvX3Bsb3RseSI6ICJpbXBvcnQgc2NpcHkuc3RhdHMgYXMgc3RhdHNcbnJlcyA9IG5wLnJhbmRvbS5leHBvbmVudGlhbChzaXplPTEwMCkgLSAxXG5xcSA9IHN0YXRzLnByb2JwbG90KHJlcywgZGlzdD1cIm5vcm1cIilcbmZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1xcVswXVswXSwgeT1xcVswXVsxXSwgbW9kZT0nbWFya2VycycsIG1hcmtlcj1kaWN0KGNvbG9yPScjMUUzQThBJyksIG5hbWU9J1Jlc8OtZHVvcycpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9cXFbMF1bMF0sIHk9cXFbMV1bMF0qcXFbMF1bMF0gKyBxcVsxXVsxXSwgbW9kZT0nbGluZXMnLCBsaW5lPWRpY3QoY29sb3I9JyM5OTFCMUInKSwgbmFtZT0nUmV0YSBUZcOzcmljYScpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9XCI8Yj5HcsOhZmljbyBkZSBRdWFudGlzIE5vcm1haXMgKFEtUSBQbG90KTwvYj5cIiwgeGF4aXNfdGl0bGU9XCJRdWFudGlzIFRlw7NyaWNvc1wiLCB5YXhpc190aXRsZT1cIlJlc8OtZHVvcyBPcmRlbmFkb3NcIiwgdGVtcGxhdGU9XCJwbG90bHlfd2hpdGVcIikiLCAicmVmZXJlbmNpYV9saXZybyI6ICJGYXJhd2F5LCBMaW5lYXIgTW9kZWxzIHdpdGggUiwgQ2FwIDcsIHAuIDg4In0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBkZSBtb2RlbGFnZW0gZGUgZGVtYW5kYSBlbmVyZ8OpdGljYSBpbmR1c3RyaWFsLCB2b2PDqiBhanVzdG91IHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvIGxpbmVhciBwYXJhIHByZXZlciBvIGNvbnN1bW8gZGUgZWxldHJpY2lkYWRlICgkWSQpIGVtIGZ1bsOnw6NvIGRhIHByb2R1w6fDo28gKCRYJCkuIEFww7NzIG9idGVyIG9zIHJlc8OtZHVvcyBhbW9zdHJhaXMgJGVfaSA9IFlfaSAtIFxcaGF0e1l9X2kkLCB2b2PDqiBkZWNpZGl1IGF2YWxpYXIgYSBzdXBvc2nDp8OjbyBkZSBub3JtYWxpZGFkZSBkb3MgZXJyb3MgJFxcdmFyZXBzaWxvbl9pIFxcc2ltIE4oMCwgXFxzaWdtYV4yKSQgdXRpbGl6YW5kbyBvIGdyw6FmaWNvIGRlIHByb2JhYmlsaWRhZGUgbm9ybWFsIChRLVEgcGxvdCkuIEFvIG9ic2VydmFyIG8gZ3LDoWZpY28sIHZvY8OqIG5vdGEgcXVlIG9zIHBvbnRvcyBzZSBkZXN2aWFtIHNpc3RlbWF0aWNhbWVudGUgZGEgbGluaGEgZGlhZ29uYWwsIGZvcm1hbmRvIHVtIHBhZHLDo28gZGUgY3VydmEgYWNlbnR1YWRvIG5hcyBleHRyZW1pZGFkZXMuIFF1YWwgZGFzIHNlZ3VpbnRlcyBpbnRlcnByZXRhw6fDtWVzIMOpIGEgbWFpcyBhZGVxdWFkYSBwYXJhIGVzdGUgZGlhZ27Ds3N0aWNvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiT3MgcmVzw61kdW9zIGFwcmVzZW50YW0gdmFyacOibmNpYSBjb25zdGFudGUsIGUgbyBtb2RlbG8gw6kgcGVyZmVpdGFtZW50ZSBhZGVxdWFkbyBwYXJhIGluZmVyw6puY2lhIGVzdGF0w61zdGljYSwgZGFkbyBxdWUgbyBkZXN2aW8gw6kgYXBlbmFzIHVtYSBjYXJhY3RlcsOtc3RpY2EgYWxlYXTDs3JpYSBkYSBhbW9zdHJhLiIsICJCIjogIk8gcGFkcsOjbyBvYnNlcnZhZG8gaW5kaWNhIHF1ZSBhIGRpc3RyaWJ1acOnw6NvIGRvcyBlcnJvcyBwb3NzdWkgY2F1ZGFzIG1haXMgcGVzYWRhcyBvdSDDqSBhc3NpbcOpdHJpY2EsIHN1Z2VyaW5kbyB1bWEgcG9zc8OtdmVsIHZpb2xhw6fDo28gZGEgc3Vwb3Npw6fDo28gZGUgbm9ybWFsaWRhZGUgcXVlIGNvbXByb21ldGUgYSB2YWxpZGFkZSBkb3MgaW50ZXJ2YWxvcyBkZSBjb25maWFuw6dhLiIsICJDIjogIk8gZ3LDoWZpY28gaW5kaWNhIHF1ZSBuw6NvIGjDoSBhdXRvY29ycmVsYcOnw6NvIG5vcyByZXPDrWR1b3MsIG1hcyBuw6NvIGZvcm5lY2UgaW5mb3JtYcOnw7VlcyBzdWZpY2llbnRlcyBwYXJhIGF2YWxpYXIgYSBub3JtYWxpZGFkZSwgc2VuZG8gbmVjZXNzw6FyaW8gcmVhbGl6YXIgb2JyaWdhdG9yaWFtZW50ZSB1bSB0ZXN0ZSBkZSBEdXJiaW4tV2F0c29uLiIsICJEIjogIk8gZGVzdmlvIGRvcyBwb250b3MgZW0gcmVsYcOnw6NvIMOgIGxpbmhhIGRpYWdvbmFsIG5vIFEtUSBwbG90IMOpIHVtIGluZGljYXRpdm8gY2zDoXNzaWNvIGRlIHF1ZSBhIHZhcmnDoXZlbCBleHBsaWNhdGl2YSAkWCQgbsOjbyDDqSBzaWduaWZpY2F0aXZhIG5vIG1vZGVsbyBwcm9wb3N0by4iLCAiRSI6ICJPIG1vZGVsbyBlc3TDoSBjb3JyZXRvLCBlIGEgY3VydmF0dXJhIG5vcyBleHRyZW1vcyBkbyBRLVEgcGxvdCDDqSBlc3BlcmFkYSBwYXJhIHF1YWxxdWVyIGNvbmp1bnRvIGRlIGRhZG9zIGNvbSAkbiA+IDMwJCBjb25mb3JtZSBvIFRlb3JlbWEgQ2VudHJhbCBkbyBMaW1pdGUuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlLCBlbSB1bSBRLVEgcGxvdCwgYSBhZGVyw6puY2lhIMOgIHJldGEgZGlhZ29uYWwgw6kgbyBjcml0w6lyaW8gdmlzdWFsIHBhcmEgYSBzdXBvc2nDp8OjbyBkZSBub3JtYWxpZGFkZS4gRGVzdmlvcyBzaXN0ZW3DoXRpY29zIG5hcyBjYXVkYXMgZG8gZ3LDoWZpY28gc2luYWxpemFtIHF1ZSBhIGRpc3RyaWJ1acOnw6NvIGRvcyByZXPDrWR1b3MgYW1vc3RyYWlzIGRpZmVyZSBkYSBkaXN0cmlidWnDp8OjbyB0ZcOzcmljYSBOb3JtYWwgZXNwZXJhZGEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJPIFEtUSBwbG90IGNvbXBhcmEgb3MgcXVhbnRpcyB0ZcOzcmljb3MgZGUgdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBwYWRyw6NvIGNvbSBvcyBxdWFudGlzIG9ic2VydmFkb3MgZG9zIHJlc8OtZHVvcy4gQSBzdXBvc2nDp8OjbyBkZSBub3JtYWxpZGFkZSBkb3MgZXJyb3MgJFxcdmFyZXBzaWxvbl9pIFxcc2ltIE4oMCwgXFxzaWdtYV4yKSQgw6kgZnVuZGFtZW50YWwgcGFyYSB0ZXN0ZXMgZGUgaGlww7N0ZXNlcyBlIGludGVydmFsb3MgZGUgY29uZmlhbsOnYSB2w6FsaWRvcy4gUXVhbmRvIG9zIHBvbnRvcyBzZSBkZXN2aWFtIGRhIHJldGEgZGlhZ29uYWwgZGUgZm9ybWEgc2lzdGVtw6F0aWNhIChjdXJ2YXR1cmEpLCBpc3NvIGluZGljYSBxdWUgb3MgcmVzw61kdW9zIG7Do28gc2VndWVtIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwuIENhdWRhcyBtYWlzIHBlc2FkYXMgb3UgYXNzaW1ldHJpYXMgZnJlcXVlbnRlbWVudGUgY2F1c2FtIGVzdGUgdGlwbyBkZSBhZmFzdGFtZW50by4gUG9ydGFudG8sIGEgYWx0ZXJuYXRpdmEgQiDDqSBhIGNvcnJldGEsIHBvaXMgcmVjb25oZWNlIGEgdmlvbGHDp8OjbyBkYSBwcmVtaXNzYSBuZWNlc3PDoXJpYSBwYXJhIGEgdmFsaWRhZGUgZXN0YXTDrXN0aWNhIGRhcyBpbmZlcsOqbmNpYXMuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVstMiwgMCwgMl0sIHk9Wy0yLjEsIDAsIDIuMV0sIG1vZGU9J2xpbmVzJywgbmFtZT0nTGluaGEgZGUgUmVmZXLDqm5jaWEnLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0yKSkpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bLTIsIC0xLCAwLCAxLCAyXSwgeT1bLTMsIC0wLjUsIDAuMSwgMC44LCA0LjVdLCBtb2RlPSdtYXJrZXJzJywgbmFtZT0nUmVzw61kdW9zIChRLVEpJywgbWFya2VyPWRpY3QoY29sb3I9JyM5OTFCMUInLCBzaXplPTgpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdFeGVtcGxvIGRlIFEtUSBQbG90IGNvbSBWaW9sYcOnw6NvJywgeGF4aXNfdGl0bGU9J1F1YW50aXMgVGXDs3JpY29zJywgeWF4aXNfdGl0bGU9J1F1YW50aXMgT2JzZXJ2YWRvcycsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkFvIHJlYWxpemFyIHVtYSBhbsOhbGlzZSBkZSByZXPDrWR1b3MgZW0gdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gcGFyYSBhdmFsaWFyIGEgYm9uZGFkZSBkbyBhanVzdGUsIHZvY8OqIGFwbGljYSBvIHRlc3RlIGRlIFNoYXBpcm8tV2lsayBzb2JyZSBvcyAkbiQgcmVzw61kdW9zIGFtb3N0cmFpcy4gTyByZXN1bHRhZG8gcmVwb3J0YWRvIHBlbG8gc29mdHdhcmUgZXN0YXTDrXN0aWNvIMOpICRXID0gMCw4NSQgY29tIHVtICRwXFx0ZXh0ey12YWxvcn0gPSAwLDAyNSQuIENvbnNpZGVyYW5kbyB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLDA1JCwgcXVhbCDDqSBhIGNvbmNsdXPDo28gZXN0YXTDrXN0aWNhIGNvcnJldGEgc29icmUgYSBub3JtYWxpZGFkZSBkb3MgZXJyb3M/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJDb21vIG8gJHBcXHRleHR7LXZhbG9yfSA+IFxcYWxwaGEkLCBuw6NvIGjDoSBldmlkw6puY2lhcyBwYXJhIHJlamVpdGFyIGEgaGlww7N0ZXNlIGRlIG5vcm1hbGlkYWRlLCB2YWxpZGFuZG8gYXMgc3Vwb3Npw6fDtWVzIGRvIG1vZGVsby4iLCAiQiI6ICJPIHZhbG9yIGRlICRXJCDDqSBtdWl0byBhbHRvLCBvIHF1ZSBpbXBsaWNhIHF1ZSBvcyBkYWRvcyBzw6NvIHBlcmZlaXRhbWVudGUgbm9ybWFpcyBlIG8gZXJybyB0aXBvIEkgw6kgbnVsby4iLCAiQyI6ICJDb21vIG8gJHBcXHRleHR7LXZhbG9yfSBcXGxlIFxcYWxwaGEkLCByZWplaXRhbW9zIGEgaGlww7N0ZXNlIG51bGEgZGUgcXVlIG9zIGVycm9zIHNlZ3VlbSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLCBpbmRpY2FuZG8gdW1hIHBvc3PDrXZlbCB2aW9sYcOnw6NvIGRhIHN1cG9zacOnw6NvIGRlIG5vcm1hbGlkYWRlLiIsICJEIjogIk8gdGVzdGUgZGUgU2hhcGlyby1XaWxrIG7Do28gw6kgYXByb3ByaWFkbyBwYXJhIGF2YWxpYXIgcmVzw61kdW9zIGRlIHJlZ3Jlc3PDo28sIGRldmVuZG8gc2VyIHN1YnN0aXR1w61kbyBleGNsdXNpdmFtZW50ZSBwb3IgaGlzdG9ncmFtYXMgc2ltcGxlcy4iLCAiRSI6ICJPIHRhbWFuaG8gYW1vc3RyYWwgJG4kIMOpIGlycmVsZXZhbnRlIHBhcmEgYSBpbnRlcnByZXRhw6fDo28gZG8gJHBcXHRleHR7LXZhbG9yfSQsIGxvZ28gYSBub3JtYWxpZGFkZSDDqSBjb25maXJtYWRhIHNlICRXJCBlc3RpdmVyIHByw7N4aW1vIGRlIDEuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJBIGhpcMOzdGVzZSBudWxhIGRvIHRlc3RlIGRlIFNoYXBpcm8tV2lsayDDqSBxdWUgb3MgZGFkb3Mgc2VndWVtIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwuIENvbXBhcmUgbyAkcFxcdGV4dHstdmFsb3J9JCBvYnRpZG8gY29tIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCBlc3RpcHVsYWRvLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyB0ZXN0ZSBkZSBTaGFwaXJvLVdpbGsgdGVzdGEgYSBoaXDDs3Rlc2UgbnVsYSAkSF8wJDogb3MgcmVzw61kdW9zIHNlZ3VlbSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLiBTZSBvICRwXFx0ZXh0ey12YWxvcn0kIHJlc3VsdGFudGUgZm9yIG1lbm9yIG91IGlndWFsIGFvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSA9IDAsMDUkLCB0ZW1vcyBldmlkw6puY2lhIGVzdGF0w61zdGljYSBzdWZpY2llbnRlIHBhcmEgcmVqZWl0YXIgJEhfMCQuIENvbSAkcFxcdGV4dHstdmFsb3J9ID0gMCwwMjUgXFxsZSAwLDA1JCwgYSBjb25jbHVzw6NvIMOpIHF1ZSBvcyBkYWRvcyBuw6NvIHNlZ3VlbSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLCBzdWdlcmluZG8gcXVlIGFzIHByZW1pc3NhcyBkZSBub3JtYWxpZGFkZSBwYXJhIGFzIGluZmVyw6puY2lhcyBiYXNlYWRhcyBubyBtb2RlbG8gbGluZWFyIG7Do28gc8OjbyBhdGVuZGlkYXMuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gc29icmUgbyBpbXBhY3RvIGRhIHRlbXBlcmF0dXJhICgkWF8xJCkgZSBkYSBwcmVzc8OjbyAoJFhfMiQpIG5hIHJlc2lzdMOqbmNpYSBkZSB1bSBub3ZvIHBvbMOtbWVybywgdW0gcGVzcXVpc2Fkb3IgYWp1c3RvdSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgbcO6bHRpcGxhIGNvbSAkbiA9IDQwJCBvYnNlcnZhw6fDtWVzLiBBbyBhbmFsaXNhciBhIG1hdHJpeiBjaGFww6l1ICRcXG1hdGhiZntIfSQsIG9ic2Vydm91LXNlIHF1ZSB1bWEgZGFzIG9ic2VydmHDp8O1ZXMgYXByZXNlbnRvdSB1bSB2YWxvciBkZSBhbGF2YW5jYWdlbSAkaF97aWl9ID0gMC4yOCQuIFV0aWxpemFuZG8gbyBjcml0w6lyaW8gZGUgZGlhZ27Ds3N0aWNvIHBhcmEgcG9udG9zIGRlIGFsYXZhbmNhLCBvbmRlIG8gbGltaXRlIGNyw610aWNvIMOpIGRlZmluaWRvIHBvciAkaF97aWl9ID4gXFxmcmFjezIocCsxKX17bn0kLCBxdWFsIMOpIGEgY29uY2x1c8OjbyBjb3JyZXRhIHNvYnJlIGVzdGEgb2JzZXJ2YcOnw6NvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBvYnNlcnZhw6fDo28gw6kgdW0gb3V0bGllciwgcG9pcyBzZXUgcmVzw61kdW8gZXN0dWRlbnRpemFkbyBkZXZlIHNlciBzdXBlcmlvciBhIDIuIiwgIkIiOiAiQSBvYnNlcnZhw6fDo28gw6kgdW0gcG9udG8gZGUgYWxhdmFuY2EsIHBvaXMgJDAuMjggPiBcXGZyYWN7MigyKzEpfXs0MH0gPSAwLjE1JC4iLCAiQyI6ICJBIG9ic2VydmHDp8OjbyBuw6NvIMOpIHVtIHBvbnRvIGRlIGFsYXZhbmNhLCBwb2lzICQwLjI4JCDDqSBpbmZlcmlvciBhbyB2YWxvciBjcsOtdGljbyBkZSAkMC4zMCQuIiwgIkQiOiAiQSBvYnNlcnZhw6fDo28gw6kgdW0gcG9udG8gZGUgYWxhdmFuY2EsIG1hcyBuw6NvIGV4ZXJjZSBpbmZsdcOqbmNpYSBzb2JyZSBvcyBjb2VmaWNpZW50ZXMgZXN0aW1hZG9zLiIsICJFIjogIk7Do28gw6kgcG9zc8OtdmVsIGNsYXNzaWZpY2FyIGEgb2JzZXJ2YcOnw6NvIHNlbSBvIGPDoWxjdWxvIHByw6l2aW8gZG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7eX0kLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiQ2FsY3VsZSBvIG7Dum1lcm8gZGUgcHJlZGl0b3JlcyAkcCQgZSBzdWJzdGl0dWEgb3MgdmFsb3JlcyBuYSBmw7NybXVsYSBkbyBsaW1pYXIgJGhfe2lpfSA+IFxcZnJhY3syKHArMSl9e259JC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBhcmEgZXN0ZSBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgbcO6bHRpcGxhIGNvbSBkb2lzIHByZWRpdG9yZXMsIHRlbW9zICRwID0gMiQuIE8gdGFtYW5obyBhbW9zdHJhbCDDqSAkbiA9IDQwJC4gTyBsaW1pYXIgcGFyYSBpZGVudGlmaWNhciBwb250b3MgZGUgYWxhdmFuY2Egw6kgZGFkbyBwb3IgJGhfe2lpfSA+IFxcZnJhY3syKDIrMSl9ezQwfSA9IFxcZnJhY3s2fXs0MH0gPSAwLjE1JC4gQ29tbyBhIGFsYXZhbmNhZ2VtIG9ic2VydmFkYSAkaF97aWl9ID0gMC4yOCQgw6kgbWFpb3IgcXVlICQwLjE1JCwgYSBvYnNlcnZhw6fDo28gw6kgY2xhc3NpZmljYWRhIGNvbW8gdW0gcG9udG8gZGUgYWxhdmFuY2EsIGluZGljYW5kbyBxdWUgZWxhIGVzdMOhIGRpc3RhbnRlIGRvIGNlbnRyb2lkZSBkb3MgZGFkb3Mgbm8gZXNwYcOnbyBkb3MgcHJlZGl0b3Jlcy4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9WzEsIDIsIDNdLCB5PVswLjA1LCAwLjI4LCAwLjEyXSwgbW9kZT0nbWFya2VycycsIG1hcmtlcj1kaWN0KHNpemU9MTIsIGNvbG9yPScjMUUzQThBJyksIG5hbWU9J0FsYXZhbmNhZ2VtJykpXG5maWcuYWRkX2hsaW5lKHk9MC4xNSwgbGluZV9kYXNoPSdkYXNoJywgbGluZV9jb2xvcj0nIzk5MUIxQicsIGFubm90YXRpb25fdGV4dD0nTGltaWFyICgwLjE1KScpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nQW7DoWxpc2UgZGUgQWxhdmFuY2FnZW0nLCB4YXhpc190aXRsZT0nSUQgZGEgT2JzZXJ2YcOnw6NvJywgeWF4aXNfdGl0bGU9J1ZhbG9yIGRlICRoX3tpaX0kJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvIHBhcmEgcHJldmVyIG8gZ2FzdG8gbWVuc2FsIGNvbSBlbmVyZ2lhIGVsw6l0cmljYSAoJFkkKSBjb20gYmFzZSBuYSDDoXJlYSBkYSByZXNpZMOqbmNpYSAoJFgkKS4gQXDDs3MgbyBhanVzdGUsIG8gYW5hbGlzdGEgdmVyaWZpY2EgYSBpbmZsdcOqbmNpYSBkYXMgb2JzZXJ2YcOnw7VlcyB1dGlsaXphbmRvIHJlc8OtZHVvcyBlc3R1ZGVudGl6YWRvcy4gUXVhbCBkYXMgYWZpcm1hw6fDtWVzIGFiYWl4byBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgbyBkaWFnbsOzc3RpY28gZXN0YXTDrXN0aWNvIHBhcmEgdW1hIG9ic2VydmHDp8OjbyBuw6NvIHVzdWFsPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiVW0gcG9udG8gZGUgYWxhdmFuY2EgcG9zc3VpIG9icmlnYXRvcmlhbWVudGUgdW0gdmFsb3IgZGUgcmVzw61kdW8gZXN0dWRlbnRpemFkbyAkfHRfaXwgPiAyJC4iLCAiQiI6ICJVbSBvdXRsaWVyIMOpIGNhcmFjdGVyaXphZG8gcG9yIHBvc3N1aXIgdW0gdmFsb3IgZXh0cmVtbyBuYSB2YXJpw6F2ZWwgcHJlZGl0b3JhICRYJCwgaW5kZXBlbmRlbnRlIGRvIHNldSByZXPDrWR1by4iLCAiQyI6ICJPIHJlc8OtZHVvIGVzdHVkZW50aXphZG8gJHx0X2l8ID4gMiQgw6kgdW0gaW5kaWNhZG9yIGRlIHF1ZSBhIG9ic2VydmHDp8OjbyDDqSB1bSBvdXRsaWVyLCBwb2lzIHNlIGRlc3ZpYSBzaWduaWZpY2F0aXZhbWVudGUgZG8gcGFkcsOjbyBkYSB2YXJpw6F2ZWwgcmVzcG9zdGEuIiwgIkQiOiAiQSBkaXN0w6JuY2lhIGRlIE1haGFsYW5vYmlzIMOpIHV0aWxpemFkYSBleGNsdXNpdmFtZW50ZSBwYXJhIGlkZW50aWZpY2FyIG91dGxpZXJzIG5hIHZhcmnDoXZlbCByZXNwb3N0YSAkWSQuIiwgIkUiOiAiUG9udG9zIGNvbSBhbHRhIGFsYXZhbmNhZ2VtIHNlbXByZSBwb3NzdWVtIHJlc8OtZHVvcyBtdWl0byBlbGV2YWRvcywgdG9ybmFuZG8gbyBtb2RlbG8gXFxpbsO6dGlsLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGRpc3RpbsOnw6NvIGNvbmNlaXR1YWw6IHBvbnRvcyBkZSBhbGF2YW5jYSBlc3TDo28gcmVsYWNpb25hZG9zIMOgcyB2YXJpw6F2ZWlzIHByZWRpdG9yYXMgKCRYJCksIGVucXVhbnRvIG91dGxpZXJzIChkZXRlY3RhZG9zIHBvciByZXPDrWR1b3MpIGVzdMOjbyByZWxhY2lvbmFkb3Mgw6AgdmFyacOhdmVsIHJlc3Bvc3RhICgkWSQpLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQ29uZm9ybWUgbyBmb3JtYWxpc21vLCAkfHRfaXwgPiAyJCBpbmRpY2EgdW1hIG9ic2VydmHDp8OjbyBvbmRlIG8gZXJybyDDqSBhdMOtcGljbyBlbSByZWxhw6fDo28gYW8gYWp1c3RlIGRvIG1vZGVsbywgY2xhc3NpZmljYW5kby1hIGNvbW8gdW0gb3V0bGllci4gUG9udG9zIGRlIGFsYXZhbmNhIGRlcGVuZGVtIGFwZW5hcyBkYXMgdmFyacOhdmVpcyBwcmVkaXRvcmFzIChlc3Bhw6dvIGRlICRYJCksIHNlbmRvIG1lZGlkb3MgcG9yICRoX3tpaX0kLiBBc3NpbSwgYSBhbHRlcm5hdGl2YSBDIMOpIGEgw7puaWNhIHF1ZSByZWZsZXRlIGNvcnJldGFtZW50ZSBvIHVzbyBkb3MgcmVzw61kdW9zIGVzdHVkZW50aXphZG9zIGNvbW8gZmVycmFtZW50YSBkZSBkaWFnbsOzc3RpY28gcGFyYSBvdXRsaWVycy4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH1dLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbeyJlbnVuY2lhZG8iOiAiU2VqYSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgbcO6bHRpcGxhICRcXG1hdGhiZnt5fSA9IFxcbWF0aGJme1h9XFxiZXRhICsgXFxlcHNpbG9uJCBjb20gJG4kIG9ic2VydmHDp8O1ZXMgZSAkcCQgcHJlZGl0b3Jlcy4gUHJvdmUgcXVlIGEgbWF0cml6IGNoYXDDqXUgJFxcbWF0aGJme0h9ID0gXFxtYXRoYmZ7WH0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9XFxtYXRoYmZ7WH1ee1xcdG9wfSQgw6kgaWRlbXBvdGVudGUsIG91IHNlamEsICRcXG1hdGhiZntIfV4yID0gXFxtYXRoYmZ7SH0kLCBlIGV4cGxpcXVlIGEgaW1wb3J0w6JuY2lhIGRlc3NhIHByb3ByaWVkYWRlIG5hIHByb2plw6fDo28gb3J0b2dvbmFsLiIsICJkaWNhIjogIk11bHRpcGxpcXVlICRcXG1hdGhiZntIfSQgcG9yIHNpIG1lc21hIGUgdXRpbGl6ZSBhIGRlZmluacOnw6NvIGRhIG1hdHJpeiBkZSBwcm9qZcOnw6NvICQoXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KShcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0pXnstMX0gPSBcXG1hdGhiZntJfSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkRlZmluaW1vcyAkXFxtYXRoYmZ7SH0gPSBcXG1hdGhiZntYfShcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0pXnstMX1cXG1hdGhiZntYfV57XFx0b3B9JC4iLCAiQ2FsY3VsYW1vcyAkXFxtYXRoYmZ7SH1eMiA9IFxcbWF0aGJme0h9XFxtYXRoYmZ7SH0gPSBbXFxtYXRoYmZ7WH0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9XFxtYXRoYmZ7WH1ee1xcdG9wfV1bXFxtYXRoYmZ7WH0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9XFxtYXRoYmZ7WH1ee1xcdG9wfV0kLiIsICJBZ3J1cGFtb3Mgb3MgdGVybW9zIGNlbnRyYWlzOiAkXFxtYXRoYmZ7SH1eMiA9IFxcbWF0aGJme1h9KFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfSBbXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9XSAoXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9XFxtYXRoYmZ7WH1ee1xcdG9wfSQuIiwgIkNvbW8gJFtcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH1dIChcXG1hdGhiZntYfV57XFx0b3B9XFxtYXRoYmZ7WH0pXnstMX0gPSBcXG1hdGhiZntJfSQsIHRlbW9zICRcXG1hdGhiZntIfV4yID0gXFxtYXRoYmZ7WH0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9IFxcbWF0aGJme0l9IFxcbWF0aGJme1h9XntcXHRvcH0kLiIsICJSZXN1bHRhbmRvIGVtICRcXG1hdGhiZntIfV4yID0gXFxtYXRoYmZ7WH0oXFxtYXRoYmZ7WH1ee1xcdG9wfVxcbWF0aGJme1h9KV57LTF9XFxtYXRoYmZ7WH1ee1xcdG9wfSA9IFxcbWF0aGJme0h9JC4iLCAiQSBpZGVtcG90w6puY2lhIGdhcmFudGUgcXVlIGFwbGljYcOnw7VlcyBzdWNlc3NpdmFzIGRhIHByb2plw6fDo28gbsOjbyBhbHRlcmFtIG8gcmVzdWx0YWRvLCBjb25zb2xpZGFuZG8gYSBwcm9qZcOnw6NvIGRlICRcXG1hdGhiZnt5fSQgbm8gZXNwYcOnbyBkZSBjb2x1bmFzIGRlICRcXG1hdGhiZntYfSQgY29tbyB1bSBwb250byBmaXhvIG5vIGVzcGHDp28gZG9zIHZhbG9yZXMgYWp1c3RhZG9zLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIk7DrXZlYSBCaXNwbywgQXVsYSAxMTogRXN0aW1hZG9yIGRlIE3DrW5pbW9zIFF1YWRyYWRvcywgcC4gNyIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyB2ZXRvciBkZSByZXPDrWR1b3MgZGVmaW5pZG8gcG9yICRcXG1hdGhiZntlfSA9IChcXG1hdGhiZntJfSAtIFxcbWF0aGJme0h9KVxcbWF0aGJme3l9JC4gRGVtb25zdHJlIG1hdGVtYXRpY2FtZW50ZSBxdWUgYSBlc3BlcmFuw6dhIGRvIHZldG9yIGRlIHJlc8OtZHVvcyDDqSBudWxhLCBhc3N1bWluZG8gcXVlICRcXG1hdGhiYntFfShcXG1hdGhiZnt5fSkgPSBcXG1hdGhiZntYfVxcYmV0YSQuIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIHByb3ByaWVkYWRlIGRhIGxpbmVhcmlkYWRlIGRhIGVzcGVyYW7Dp2EgZSBkYSByZWxhw6fDo28gJChcXG1hdGhiZntJfS1cXG1hdGhiZntIfSlcXG1hdGhiZntYfSA9IDAkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBIGVzcGVyYW7Dp2EgZG8gdmV0b3IgZGUgcmVzw61kdW9zIMOpICRcXG1hdGhiYntFfShcXG1hdGhiZntlfSkgPSBcXG1hdGhiYntFfSgoXFxtYXRoYmZ7SX0gLSBcXG1hdGhiZntIfSlcXG1hdGhiZnt5fSkkLiIsICJQZWxhIGxpbmVhcmlkYWRlIGRhIGVzcGVyYW7Dp2E6ICRcXG1hdGhiYntFfShcXG1hdGhiZntlfSkgPSAoXFxtYXRoYmZ7SX0gLSBcXG1hdGhiZntIfSlcXG1hdGhiYntFfShcXG1hdGhiZnt5fSkkLiIsICJTdWJzdGl0dWluZG8gYSBwcmVtaXNzYSBkZSBxdWUgJFxcbWF0aGJie0V9KFxcbWF0aGJme3l9KSA9IFxcbWF0aGJme1h9XFxiZXRhJCwgdGVtb3MgJFxcbWF0aGJie0V9KFxcbWF0aGJme2V9KSA9IChcXG1hdGhiZntJfSAtIFxcbWF0aGJme0h9KVxcbWF0aGJme1h9XFxiZXRhJC4iLCAiRGlzdHJpYnVpbmRvIG8gcHJvZHV0bzogJFxcbWF0aGJie0V9KFxcbWF0aGJme2V9KSA9IChcXG1hdGhiZntYfSAtIFxcbWF0aGJme0h9XFxtYXRoYmZ7WH0pXFxiZXRhJC4iLCAiQ29tbyAkXFxtYXRoYmZ7SH1cXG1hdGhiZntYfSA9IFxcbWF0aGJme1h9KFxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSleey0xfVxcbWF0aGJme1h9XntcXHRvcH1cXG1hdGhiZntYfSA9IFxcbWF0aGJme1h9KFxcbWF0aGJme0l9KSA9IFxcbWF0aGJme1h9JCwgdGVtb3MgJFxcbWF0aGJme0V9KFxcbWF0aGJme2V9KSA9IChcXG1hdGhiZntYfSAtIFxcbWF0aGJme1h9KVxcYmV0YSA9IFxcbWF0aGJmezB9XFxiZXRhID0gXFxtYXRoYmZ7MH0kLiIsICJDb25jbHXDrW1vcyBxdWUsIHNvYiBvIG1vZGVsbyBlc3BlY2lmaWNhZG8sIG9zIHJlc8OtZHVvcyBzw6NvIGNlbnRyYWRvcyBlbSB6ZXJvLCByZWZsZXRpbmRvIG8gYWp1c3RlIG7Do28gdmllc2Fkby4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJOw612ZWEgQmlzcG8sIEF1bGEgMTM6IEFuw6FsaXNlIGRlIFJlc8OtZHVvcyBubyBNUkxTLCBwLiAzIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGV4cGVyaW1lbnRvIGNvbSAkbj01JCBvYnNlcnZhw6fDtWVzLCBvYnRldmUtc2UgJFNRVG90YWwgPSAxMDAkIGUgJFNRUGFyID0gODAkLiBDYWxjdWxlIGEgU29tYSBkZSBRdWFkcmFkb3MgZG9zIFJlc8OtZHVvcyAoJFNRUmVzJCkgZSBvIHZhbG9yIGRhIGVzdGF0w61zdGljYSBkZSBhbGF2YW5jYWdlbSBtw6lkaWEgJFxcYmFye2h9JCBwYXJhIHVtIG1vZGVsbyBjb20gdW0gaW50ZXJjZXB0byBlIHVtIHByZWRpdG9yLiIsICJkaWNhIjogIlVzZSAkU1FUb3RhbCA9IFNRUGFyICsgU1FSZXMkIGUgYSBwcm9wcmllZGFkZSBkZSBxdWUgJFxcc3VtIGhfe2lpfSA9IHArMSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkRhZGEgYSBkZWNvbXBvc2nDp8OjbyBkYSBzb21hIGRlIHF1YWRyYWRvczogJFNRVG90ID0gU1FQYXIgKyBTUVJlcyQuIiwgIkxvZ28sICRTUVJlcyA9IFNRVG90IC0gU1FQYXIgPSAxMDAgLSA4MCA9IDIwJC4iLCAiU2FiZW1vcyBxdWUgYSBzb21hIGRvcyBlbGVtZW50b3MgZGlhZ29uYWlzIGRhIG1hdHJpeiBjaGFww6l1LCAkXFx0ZXh0e3RyfShcXG1hdGhiZntIfSkgPSBcXHN1bV97aT0xfV5uIGhfe2lpfSQsIMOpIGlndWFsIGFvIG7Dum1lcm8gZGUgcGFyw6JtZXRyb3MgZG8gbW9kZWxvLCBvdSBzZWphLCAkcCsxJC4iLCAiUGFyYSB1bSBtb2RlbG8gY29tIGludGVyY2VwdG8gZSB1bSBwcmVkaXRvciwgJHA9MSQsIGxvZ28gJHArMSA9IDIkLiIsICJBIGFsYXZhbmNhZ2VtIG3DqWRpYSDDqSAkXFxiYXJ7aH0gPSBcXGZyYWN7XFx0ZXh0e3RyfShcXG1hdGhiZntIfSl9e259ID0gXFxmcmFjezJ9ezV9ID0gMC40JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJOw612ZWEgQmlzcG8sIEF1bGEgMTE6IEVzdGltYWRvciBkZSBNw61uaW1vcyBRdWFkcmFkb3MsIHAuIDkiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjR9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gZGUgcmVncmVzc8Ojbywgdm9jw6ogb2J0ZXZlIHVtIHJlc8OtZHVvICRlX2kkIHBhcmEgdW1hIG9ic2VydmHDp8OjbyBlc3BlY8OtZmljYSwgb25kZSBvIHZhbG9yIG9ic2VydmFkbyDDqSAkWV9pID0gMTUwJCBlIG8gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIGVzdGltYWRvIHByb2R1eml1ICRcXGhhdHtZfV9pID0gMTQyJC4gRXhwbGlxdWUgY29uY2VpdHVhbG1lbnRlIG8gcXVlIG8gcmVzw61kdW8gcmVwcmVzZW50YSBubyBkaWFnbsOzc3RpY28gZG8gbW9kZWxvIGUgY2FsY3VsZSBvIHZhbG9yIGRlICRlX2kkIHBhcmEgZXN0YSBvYnNlcnZhw6fDo28uIEFsw6ltIGRpc3NvLCBkaXNjdXRhIGEgaW1wb3J0w6JuY2lhIGRhIG3DqWRpYSBkb3MgcmVzw61kdW9zIHNlciBwcsOzeGltYSBkZSB6ZXJvLiIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBkZWZpbmnDp8OjbyBkZSByZXPDrWR1bzogJGVfaSA9IFlfaSAtIFxcaGF0e1l9X2kkLiBBIG3DqWRpYSBkb3MgcmVzw61kdW9zICRcXGJhcntlfSA9IFxcZnJhY3sxfXtufSBcXHN1bSBlX2kkIMOpIG51bGEgcG9yIGNvbnN0cnXDp8OjbyBubyBtw6l0b2RvIGRvcyBNw61uaW1vcyBRdWFkcmFkb3MuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkRlZmluacOnw6NvIGRvIHJlc8OtZHVvOiBPIHJlc8OtZHVvICRlX2kkIHJlcHJlc2VudGEgYSBwYXJ0ZSBkYSB2YXJpYcOnw6NvIG5hIHZhcmnDoXZlbCByZXNwb3N0YSAkWV9pJCBxdWUgbsOjbyDDqSBleHBsaWNhZGEgcGVsbyBtb2RlbG8gbGluZWFyLCBzZXJ2aW5kbyBjb21vIHVtYSBlc3RpbWF0aXZhIGRvIGVycm8gYWxlYXTDs3JpbyAkXFx2YXJlcHNpbG9uX2kkLiIsICJDw6FsY3VsbzogRGFkbyAkWV9pID0gMTUwJCBlICRcXGhhdHtZfV9pID0gMTQyJCwgdGVtb3M6ICQkZV9pID0gMTUwIC0gMTQyID0gOCQkIiwgIkRpc2N1c3PDo286IEEgc29tYSBkb3MgcmVzw61kdW9zICRcXHN1bSBlX2kgPSAwJCwgbyBxdWUgaW1wbGljYSBxdWUgYSBtw6lkaWEgZG9zIHJlc8OtZHVvcyAkXFxiYXJ7ZX0gPSAwJC4gSXNzbyDDqSB1bWEgcHJvcHJpZWRhZGUgYWxnw6licmljYSBkbyBtw6l0b2RvIGRlIE3DrW5pbW9zIFF1YWRyYWRvcy4gU2UgYSBtw6lkaWEgc2UgZGVzdmlhc3NlIHNpZ25pZmljYXRpdmFtZW50ZSBkZSB6ZXJvIGVtIHVtYSBhbW9zdHJhLCBzZXJpYSB1bSBpbmTDrWNpbyBkZSBmYWxoYSBuYSBlc3BlY2lmaWNhw6fDo28gZG8gbW9kZWxvIChjb21vIGEgb21pc3PDo28gZGUgdW1hIGNvbnN0YW50ZSBvdSB2acOpcyBlc3RydXR1cmFsKS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDguMH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBvIG1vZGVsbyBkZSByZWdyZXNzw6NvIGxpbmVhciAkWV9pID0gXFxiZXRhXzAgKyBcXGJldGFfMSBYX2kgKyBcXHZhcmVwc2lsb25faSQuIEV4cGxpcXVlIGNvbW8gbyBncsOhZmljbyBkZSByZXPDrWR1b3MgdmVyc3VzIGEgdmFyacOhdmVsIHByZWRpdG9yYSAoJFhfaSQpIHBvZGUgZGlhZ25vc3RpY2FyIGEgbmVjZXNzaWRhZGUgZGUgaW5jbHVpciB1bSB0ZXJtbyBxdWFkcsOhdGljbyBubyBtb2RlbG8gKGV4OiAkXFxiZXRhXzIgWF9pXjIkKS4gQ29tbyBvIHBhZHLDo28gdmlzdWFsIG11ZGFyaWEgYXDDs3MgYSBjb3JyZcOnw6NvIGRvIG1vZGVsbz8iLCAiZGljYSI6ICJTZSBhIHJlbGHDp8OjbyBmb3IgY3VydmEgZSBuw6NvIGxpbmVhciwgb3MgcmVzw61kdW9zIGRvIG1vZGVsbyBsaW5lYXIgYXByZXNlbnRhcsOjbyB1bSBwYWRyw6NvIHNpc3RlbcOhdGljbyAobsOjbyBhbGVhdMOzcmlvKS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRGlhZ27Ds3N0aWNvIHZpc3VhbDogU2UgYSByZWxhw6fDo28gcmVhbCBlbnRyZSAkWCQgZSAkWSQgZm9yIHF1YWRyw6F0aWNhLCBtYXMgYWp1c3RhbW9zIHVtIG1vZGVsbyBsaW5lYXIsIG8gZ3LDoWZpY28gZGUgJGVfaSQgdmVyc3VzICRYX2kkIGV4aWJpcsOhIHVtIHBhZHLDo28gZW0gZm9ybWF0byBkZSAnVScgb3UgYXJjbyBpbnZlcnRpZG8uIiwgIkludGVycHJldGHDp8OjbzogRXN0ZSBwYWRyw6NvIGluZGljYSBxdWUgbyBlcnJvIG7Do28gZXN0w6EgZGlzdHJpYnXDrWRvIGFsZWF0b3JpYW1lbnRlIGVtIHRvcm5vIGRlIHplcm8sIG1hcyBcXHNpbSBxdWUgbyBtb2RlbG8gbGluZWFyIHN1YmVzdGltYSBvdSBzdXBlcmVzdGltYSBzaXN0ZW1hdGljYW1lbnRlIGEgdmFyacOhdmVsIHJlc3Bvc3RhIGVtIGNlcnRhcyBmYWl4YXMgZGUgJFgkLiIsICJDb3JyZcOnw6NvOiBBbyBpbmNsdWlyIG8gdGVybW8gJFxcYmV0YV8yIFhfaV4yJCwgYSBlc3RydXR1cmEgZGEgY3VydmF0dXJhIMOpIGNhcHR1cmFkYSBwZWxvIG1vZGVsby4gQ29uc2VxdWVudGVtZW50ZSwgbyBub3ZvIGdyw6FmaWNvIGRlIHJlc8OtZHVvcyB2ZXJzdXMgJFhfaSQgZGV2ZSBtb3N0cmFyIHBvbnRvcyBkaXN0cmlidcOtZG9zIGFsZWF0b3JpYW1lbnRlIGVtIHRvcm5vIGRlIHplcm8sIHNlbSBvIHBhZHLDo28gY3Vydmlsw61uZW8gYW50ZXJpb3IuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiRmFyYXdheSwgTGluZWFyIE1vZGVscyB3aXRoIFIsIENhcCA3LCBwLiA4MSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJBbmFsaXNlIGEgaW5kZXBlbmTDqm5jaWEgZG9zIGVycm9zLiBFbSB1bSBlc3R1ZG8gc29icmUgY29uc3VtbyBkZSBlbmVyZ2lhLCB2b2PDqiBkaXNww7VlIGRlIHJlc8OtZHVvcyBjb2xldGFkb3MgbWVuc2FsbWVudGUgYW8gbG9uZ28gZGUgNDggbWVzZXMuIE8gcXVlIGFjb250ZWNlIHNlLCBhbyBwbG90YXIgJGVfdCQgdmVyc3VzIG8gdGVtcG8gJHQkLCB2b2PDqiBvYnNlcnZhciB1bSBwYWRyw6NvIG9uZGUgcmVzw61kdW9zIHBvc2l0aXZvcyBzw6NvIHNlZ3VpZG9zIHBvciByZXPDrWR1b3MgcG9zaXRpdm9zIGUgcmVzw61kdW9zIG5lZ2F0aXZvcyBwb3IgbmVnYXRpdm9zPyBRdWUgc3Vwb3Npw6fDo28gZm9pIHZpb2xhZGEgZSBxdWFsIGEgaW1wbGljYcOnw6NvIGVzdGF0w61zdGljYT8iLCAiZGljYSI6ICJBIHN1cG9zacOnw6NvIGRlIGluZGVwZW5kw6puY2lhIGRvcyBlcnJvcyBzaWduaWZpY2EgcXVlICRDb3YoXFx2YXJlcHNpbG9uX2ksIFxcdmFyZXBzaWxvbl9qKSA9IDAkIHBhcmEgJGkgXFxuZXEgaiQuIEEgcGVyc2lzdMOqbmNpYSB2aXN1YWwgc3VnZXJlIGF1dG9jb3JyZWxhw6fDo28uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlN1cG9zacOnw6NvIHZpb2xhZGE6IEEgc3Vwb3Npw6fDo28gZGUgaW5kZXBlbmTDqm5jaWEgZG9zIGVycm9zICgkQ292KFxcdmFyZXBzaWxvbl9pLCBcXHZhcmVwc2lsb25faikgPSAwJCkgZm9pIHZpb2xhZGEuIE8gcGFkcsOjbyBvYnNlcnZhZG8gw6kgaW5kaWNhdGl2byBkZSBhdXRvY29ycmVsYcOnw6NvIHBvc2l0aXZhLiIsICJJbXBsaWNhw6fDo28gZXN0YXTDrXN0aWNhOiBRdWFuZG8gaMOhIGF1dG9jb3JyZWxhw6fDo28sIGFzIGVzdGltYXRpdmFzIGRhIHZhcmnDom5jaWEgZG9zIGNvZWZpY2llbnRlcyBjYWxjdWxhZGFzIHBlbG8gTVJMUyBwYWRyw6NvIG7Do28gc8OjbyBjb25macOhdmVpcy4gSXNzbyBwb2RlIGxldmFyIGEgZXJyb3MtcGFkcsOjbyBzdWJlc3RpbWFkb3MsIHJlc3VsdGFuZG8gZW0gZXN0YXTDrXN0aWNhcyAkdF8wJCBpbmZsYWRhcyBlLCBjb25zZXF1ZW50ZW1lbnRlLCBwLXZhbG9yZXMgZW5nYW5vc2FtZW50ZSBiYWl4b3MsIGluZGljYW5kbyB1bWEgc2lnbmlmaWPDom5jaWEgcXVlIHBvZGUgc2VyIGVzcMO6cmlhLiIsICJDb25jbHVzw6NvOiBPIGRpYWduw7NzdGljbyB2aXN1YWwgbW9zdHJhIHF1ZSBvcyByZXPDrWR1b3MgY2FycmVnYW0gaW5mb3JtYcOnw6NvIHRlbXBvcmFsIG7Do28gY2FwdHVyYWRhIHBlbG8gbW9kZWxvLCBzdWdlcmluZG8gYSBuZWNlc3NpZGFkZSBkZSBtb2RlbG9zIGRlIHPDqXJpZXMgdGVtcG9yYWlzLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSBtb2RlbG8gbGluZWFyIGFqdXN0YWRvIGNvbSAkbj0yMCQgb2JzZXJ2YcOnw7Vlcy4gT3MgcmVzw61kdW9zIGFtb3N0cmFpcyBmb3JhbSBjYWxjdWxhZG9zIGUgb3JkZW5hZG9zIGNvbW8gJGVfeygxKX0gXFxsZSBlX3soMil9IFxcbGUgXFxkb3RzIFxcbGUgZV97KDIwKX0kLiBFeHBsaXF1ZSwgdXRpbGl6YW5kbyBhIGRlZmluacOnw6NvIGRvIHRlc3RlIGRlIFNoYXBpcm8tV2lsaywgY29tbyBhIGVzdGF0w61zdGljYSAkVyQgw6kgY2FsY3VsYWRhIGUgcG9yIHF1ZSBlbGEgw6kgc2Vuc8OtdmVsIGEgZGVzdmlvcyBkZSBub3JtYWxpZGFkZS4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlICRXID0gXFxmcmFjeyhcXHN1bV97aT0xfV57bn0gYV9pIGVfeyhpKX0pXjJ9e1xcc3VtX3tpPTF9XntufSBlX2leMn0kLCBvbmRlICRhX2kkIHPDo28gY29lZmljaWVudGVzIGJhc2VhZG9zIG5vcyBlc3RhdMOtc3RpY29zIGRlIG9yZGVtIGRhIE5vcm1hbC4gUGVuc2UgbmEgcmVsYcOnw6NvIGVudHJlIGEgdmFyacOibmNpYSBkb3MgcmVzw61kdW9zIGUgYSBjb21iaW5hw6fDo28gbGluZWFyIGRvcyBtZXNtb3MuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgZXN0YXTDrXN0aWNhICRXJCDDqSBkZWZpbmlkYSBwb3IgJCRXID0gXFxmcmFjeyhcXHN1bV97aT0xfV57bn0gYV9pIGVfeyhpKX0pXjJ9e1xcc3VtX3tpPTF9XntufSBlX2leMn0kJCBvbmRlICRlX3soaSl9JCBzw6NvIG9zIHJlc8OtZHVvcyBvcmRlbmFkb3MgZSAkYV9pJCBzw6NvIGNvbnN0YW50ZXMgb2J0aWRhcyBkb3MgZXNwZXJhZG9zIGRvcyBlc3RhdMOtc3RpY29zIGRlIG9yZGVtIGRhIG5vcm1hbCBwYWRyw6NvLiIsICJPIGRlbm9taW5hZG9yICRcXHN1bSBlX2leMiQgcmVwcmVzZW50YSBhIHNvbWEgZGUgcXVhZHJhZG9zIHRvdGFsIGRvcyByZXPDrWR1b3MuIiwgIk8gbnVtZXJhZG9yIMOpIG8gcXVhZHJhZG8gZGUgdW1hIGNvbWJpbmHDp8OjbyBsaW5lYXIgcG9uZGVyYWRhIGRvcyByZXPDrWR1b3Mgb3JkZW5hZG9zLiIsICJTb2Igbm9ybWFsaWRhZGUsIG9zIHJlc8OtZHVvcyBvcmRlbmFkb3MgZGV2ZXJpYW0gYWxpbmhhci1zZSBkZSBmb3JtYSBjb25zaXN0ZW50ZSBjb20gb3MgcGVzb3MgJGFfaSQsIHJlc3VsdGFuZG8gZW0gdW0gdmFsb3IgZGUgJFckIHByw7N4aW1vIGRlIDEuIiwgIlNlIGEgZGlzdHJpYnVpw6fDo28gZG9zIGVycm9zIG7Do28gZm9yIG5vcm1hbCwgbyBhbGluaGFtZW50byBlc3BlcmFkbyBlbnRyZSBvcyByZXPDrWR1b3Mgb3JkZW5hZG9zIGUgb3MgY29lZmljaWVudGVzICRhX2kkIGRpbWludWksIHJlZHV6aW5kbyBvIHZhbG9yIGRlICRXJCBlIGxldmFuZG8gw6AgcmVqZWnDp8OjbyBkZSAkSF8wJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bWEgYW7DoWxpc2UgZGUgcmVzw61kdW9zIGRlIHVtIG1vZGVsbyBjb20gJG49MTAwJCBvYnNlcnZhw6fDtWVzLCBvIFEtUSBwbG90IG1vc3RyYSBxdWUsIG5hIHJlZ2nDo28gY2VudHJhbCwgb3MgcG9udG9zIGVzdMOjbyBzb2JyZSBhIHJldGEsIG1hcyBuYXMgY2F1ZGFzIChpbmZlcmlvciBlIHN1cGVyaW9yKSBlbGVzIHNlIGRpc3RhbmNpYW0sIHNpdHVhbmRvLXNlIGFiYWl4byBkYSByZXRhIG5hIGNhdWRhIGluZmVyaW9yIGUgYWNpbWEgbmEgc3VwZXJpb3IuIEludGVycHJldGUgZXN0ZSBmZW7DtG1lbm8gZW0gdGVybW9zIGRlIGN1cnRvc2UgZSBpbmRpcXVlIHNlIGEgaW5mZXLDqm5jaWEgZXN0YXTDrXN0aWNhIGJhc2VhZGEgbmEgbm9ybWFsaWRhZGUgZG9zIGVycm9zIHNlcmlhIHNldmVyYW1lbnRlIGFmZXRhZGEuIiwgImRpY2EiOiAiQ29uc2lkZXJlIGEgcmVsYcOnw6NvIGVudHJlIGEgZm9ybWEgZG9zIGRhZG9zIG5hcyBjYXVkYXMgZG8gUS1RIHBsb3QgZSBhIGN1cnRvc2UgZGEgZGlzdHJpYnVpw6fDo28gKGNhdWRhcyBwZXNhZGFzIHZlcnN1cyBjYXVkYXMgbGV2ZXMpLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJPIFEtUSBwbG90IGRlc2NyZXZlIG8gY29tcG9ydGFtZW50byBkb3MgcXVhbnRpcy4gU2Ugb3MgcG9udG9zIGVzdMOjbyBhYmFpeG8gZGEgcmV0YSBuYSBjYXVkYSBpbmZlcmlvciwgaXNzbyBzaWduaWZpY2EgcXVlIG9zIHF1YW50aXMgb2JzZXJ2YWRvcyBzw6NvIG1haW9yZXMgcXVlIG9zIHF1YW50aXMgdGXDs3JpY29zLiIsICJTZSBvcyBwb250b3MgZXN0w6NvIGFjaW1hIGRhIHJldGEgbmEgY2F1ZGEgc3VwZXJpb3IsIG9zIHF1YW50aXMgb2JzZXJ2YWRvcyBzw6NvIG1haW9yZXMgcXVlIG9zIHRlw7NyaWNvcy4iLCAiRXNzZSBjb21wb3J0YW1lbnRvIGluZGljYSBxdWUgYSBkaXN0cmlidWnDp8OjbyBwb3NzdWkgY2F1ZGFzIG1haXMgcGVzYWRhcyBkbyBxdWUgYSBkaXN0cmlidWnDp8OjbyBOb3JtYWwgKGN1cnRvc2UgZXhjZXNzaXZhIHBvc2l0aXZhIG91IGxlcHRvY8O6cnRpY2EpLiIsICJDb21vICRuPTEwMCQgw6kgdW0gdGFtYW5obyBhbW9zdHJhbCByYXpvYXZlbG1lbnRlIGdyYW5kZSwgbyBpbXBhY3RvIGRhIG7Do28tbm9ybWFsaWRhZGUgbmEgaW5mZXLDqm5jaWEgcG9kZSBzZXIgYXRlbnVhZG8gcGVsbyBUZW9yZW1hIENlbnRyYWwgZG8gTGltaXRlIGVtIGNlcnRvcyBjb250ZXh0b3MuIiwgIk5vIGVudGFudG8sIGVtIG1vZGVsb3MgZGUgcmVncmVzc8OjbywgY2F1ZGFzIG11aXRvIHBlc2FkYXMgcG9kZW0gaW52YWxpZGFyIHRlc3RlcyAkdCQgZSAkRiQsIHRvcm5hbmRvIG5lY2Vzc8OhcmlhIGEgYW7DoWxpc2UgY3VpZGFkb3NhIGRhIGluZmx1w6puY2lhIGRlIG91dGxpZXJzLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtYSBhbW9zdHJhIGRlICRuPTE1JCByZXPDrWR1b3MgZGUgdW0gbW9kZWxvIGxpbmVhciBkZSBjdXN0b3Mgb2J0ZXZlIHVtYSBlc3RhdMOtc3RpY2EgZGUgU2hhcGlyby1XaWxrICRXPTAsOTQkLiBTYWJlbmRvIHF1ZSBwYXJhICRuPTE1JCBvIHZhbG9yIGNyw610aWNvIGRlICRXJCBwYXJhICRcXGFscGhhPTAsMDUkIMOpIGFwcm94aW1hZGFtZW50ZSAkMCw4OCQsIGNhbGN1bGUgb3UgZGVzY3JldmEgYSBkZWNpc8OjbyBlc3RhdMOtc3RpY2EgZSBleHBsaXF1ZSBwb3IgcXVlIGEgbm9ybWFsaWRhZGUgw6kgaW1wb3J0YW50ZSBwYXJhIGEgdmFsaWRhZGUgZG9zIGVzdGltYWRvcmVzIGRlIE3DrW5pbW9zIFF1YWRyYWRvcy4iLCAiZGljYSI6ICJDb21wYXJlIG8gJFdfe1xcdGV4dHtjYWxjfX0kIGNvbSBvICRXX3tcXHRleHR7Y3JpdH19JC4gTGVtYnJlLXNlIHF1ZSBvIHRlc3RlIHJlamVpdGEgYSBub3JtYWxpZGFkZSBzZSAkV197XFx0ZXh0e2NhbGN9fSA8IFdfe1xcdGV4dHtjcml0fX0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJJZGVudGlmaWNhbW9zIG8gdmFsb3IgZGEgZXN0YXTDrXN0aWNhIGNhbGN1bGFkYTogJFdfe1xcdGV4dHtjYWxjfX0gPSAwLDk0JC4iLCAiSWRlbnRpZmljYW1vcyBvIHZhbG9yIGNyw610aWNvIGRvIHRlc3RlIHBhcmEgJFxcYWxwaGEgPSAwLDA1JCBlICRuPTE1JDogJFdfe1xcdGV4dHtjcml0fX0gPSAwLDg4JC4iLCAiQSByZWdyYSBkZSBkZWNpc8OjbyBwYXJhIG8gdGVzdGUgZGUgU2hhcGlyby1XaWxrIMOpOiByZWplaXRhLXNlIGEgbm9ybWFsaWRhZGUgc2UgJFdfe1xcdGV4dHtjYWxjfX0gPCBXX3tcXHRleHR7Y3JpdH19JC4iLCAiQ29tbyAkMCw5NCA+IDAsODgkLCBuw6NvIHJlamVpdGFtb3MgYSBoaXDDs3Rlc2UgbnVsYSBkZSBub3JtYWxpZGFkZS4iLCAiQSBub3JtYWxpZGFkZSBkb3MgZXJyb3MgJFxcdmFyZXBzaWxvbl9pIFxcc2ltIE4oMCwgXFxzaWdtYV4yKSQgw6kgaW1wb3J0YW50ZSBwb2lzIGdhcmFudGUgcXVlIG9zIGVzdGltYWRvcmVzIGRlIE3DrW5pbW9zIFF1YWRyYWRvcyBzZWphbSBuw6NvIGFwZW5hcyBCTFVFIChCZXN0IExpbmVhciBVbmJpYXNlZCBFc3RpbWF0b3JzKSwgbWFzIHRhbWLDqW0gb3MgZXN0aW1hZG9yZXMgZGUgbcOheGltYSB2ZXJvc3NpbWlsaGFuw6dhLCBwZXJtaXRpbmRvIGEgY29uc3RydcOnw6NvIGRlIGludGVydmFsb3MgZGUgY29uZmlhbsOnYSBlIHRlc3RlcyAkdCQgZXhhdG9zIHBhcmEgb3MgY29lZmljaWVudGVzICRcXGJldGEkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC45NH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIHByb2pldG8gZGUgSW9UIHBhcmEgbW9uaXRvcmFtZW50byBkZSBzZW5zb3JlcywgdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIHNpbXBsZXMgZm9pIGFqdXN0YWRvIGNvbSAkbiA9IDYwJCBvYnNlcnZhw6fDtWVzIHBhcmEgcHJldmVyIGEgdm9sdGFnZW0gZGUgc2HDrWRhLiBDYWxjdWxlIG8gdmFsb3IgY3LDrXRpY28gcGFyYSBhIGlkZW50aWZpY2HDp8OjbyBkZSBwb250b3MgZGUgYWxhdmFuY2EgdXRpbGl6YW5kbyBvIGNyaXTDqXJpbyBmb3JtYWwgJCRoX3tpaX0gPiBcXGZyYWN7MihwKzEpfXtufSQkLiIsICJkaWNhIjogIkVtIHVtYSByZWdyZXNzw6NvIGxpbmVhciBzaW1wbGVzLCBvIG7Dum1lcm8gZGUgcHJlZGl0b3JlcyAkcCQgw6kgaWd1YWwgYSAxLiBTdWJzdGl0dWEgb3MgdmFsb3JlcyBjb25oZWNpZG9zIG5hIGbDs3JtdWxhIGZvcm5lY2lkYS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiSWRlbnRpZmljYW1vcyBvcyBwYXLDom1ldHJvcyBkbyBtb2RlbG86ICRuID0gNjAkIGUgJHAgPSAxJCAocmVncmVzc8OjbyBsaW5lYXIgc2ltcGxlcykuIiwgIkEgZsOzcm11bGEgZG8gbGltaXRlIGRlIGFsYXZhbmNhZ2VtIMOpICRcXHRleHR7TGltaWFyfSA9IFxcZnJhY3syKHArMSl9e259JC4iLCAiU3Vic3RpdHXDrW1vcyBvcyB2YWxvcmVzOiAkXFx0ZXh0e0xpbWlhcn0gPSBcXGZyYWN7MigxKzEpfXs2MH0kLiIsICJSZWFsaXphbW9zIG8gY8OhbGN1bG86ICRcXGZyYWN7MigyKX17NjB9ID0gXFxmcmFjezR9ezYwfSQuIiwgIk8gcmVzdWx0YWRvIGZpbmFsIMOpIGFwcm94aW1hZGFtZW50ZSAkMC4wNjY3JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMDY2N30sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCBzb2IgYSDDs3RpY2EgZGEgZ2VvbWV0cmlhIGRhIHJlZ3Jlc3PDo28gcG9yIG3DrW5pbW9zIHF1YWRyYWRvcywgcG9yIHF1ZSB1bSBwb250byBkZSBhbGF2YW5jYSB0ZW0gbyBwb3RlbmNpYWwgZGUgJ3B1eGFyJyBhIHJldGEgZGUgcmVncmVzc8OjbyBlbSBzdWEgZGlyZcOnw6NvLCBtZXNtbyBxdWUgbyBzZXUgcmVzw61kdW8gJGVfaSQgc2VqYSBwZXF1ZW5vLiIsICJkaWNhIjogIkNvbnNpZGVyZSBxdWUgYSBtYXRyaXogY2hhcMOpdSAkXFxtYXRoYmZ7SH0kIHByb2pldGEgbyB2ZXRvciBkZSBvYnNlcnZhw6fDtWVzICRcXG1hdGhiZntZfSQgbm8gZXNwYcOnbyBkZWZpbmlkbyBwZWxvcyBwcmVkaXRvcmVzLiBDb21vIG8gcG9udG8gZXN0w6EgbG9uZ2UgZG8gY2VudHJvaWRlLCBhIG1pbmltaXphw6fDo28gZGEgc29tYSBkZSBxdWFkcmFkb3MgZG9zIGVycm9zIGZvcsOnYSBvIG1vZGVsbyBhIGFqdXN0YXItc2UgYSBlbGUuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgZXN0aW1hw6fDo28gcG9yIG3DrW5pbW9zIHF1YWRyYWRvcyBidXNjYSBtaW5pbWl6YXIgJFxcc3VtIGVfaV4yJCwgb3Ugc2VqYSwgbWluaW1pemFyIGEgZGlzdMOibmNpYSB2ZXJ0aWNhbCBlbnRyZSBvcyBkYWRvcyBlIGEgcmV0YS4iLCAiTyBlbGVtZW50byAkaF97aWl9JCBkYSBkaWFnb25hbCBkYSBtYXRyaXogJFxcbWF0aGJme0h9JCByZXByZXNlbnRhIGEgZGlzdMOibmNpYSBkZSBNYWhhbGFub2JpcyBkYSBvYnNlcnZhw6fDo28gJGkkIGF0w6kgbyBjZW50cm9pZGUgZGUgJFgkLiIsICJQb250b3MgY29tIGFsdG8gJGhfe2lpfSQgZXN0w6NvIHNpdHVhZG9zIG5hcyBleHRyZW1pZGFkZXMgZG8gZXNwYcOnbyBhbW9zdHJhbCBkb3MgcHJlZGl0b3Jlcy4iLCAiQ29tbyBhIHJldGEgZGUgcmVncmVzc8OjbyBkZXZlIHBhc3NhciBwcsOzeGltbyBhIGVzc2VzIHBvbnRvcyBleHRyZW1vcyBwYXJhIG1hbnRlciBvIGFqdXN0ZSBnbG9iYWwsIG1lc21vIHVtIHJlc8OtZHVvICRlX2kkIHBlcXVlbm8gbmVzc2UgcG9udG8gZXhlcmNlIHVtYSBwcmVzc8OjbyBhbmd1bGFyIHNpZ25pZmljYXRpdmEgc29icmUgb3MgY29lZmljaWVudGVzICRcXGhhdHtcXGJldGF9XzAkIGUgJFxcaGF0e1xcYmV0YX1fMSQgZGV2aWRvIMOgIHN1YSBhbGF2YW5jYWdlbSBlbGV2YWRhLiIsICJDb25jbHXDrW1vcyBxdWUgYSBpbmZsdcOqbmNpYSDDqSB1bSBwcm9kdXRvIGRhIGFsYXZhbmNhZ2VtIGUgZGEgbWFnbml0dWRlIGRvIHJlc8OtZHVvLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBweC5zY2F0dGVyKHg9WzEsIDIsIDgsIDksIDEwXSwgeT1bMSwgMiwgOCwgOSwgMl0sIGxhYmVscz17J3gnOiAnUHJlZGl0b3JlcycsICd5JzogJ1Jlc3Bvc3RhJ30pXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMSwgMTBdLCB5PVsxLCAyXSwgbW9kZT0nbGluZXMnLCBsaW5lPWRpY3QoY29sb3I9JyM5OTFCMUInKSwgbmFtZT0nUmV0YSBJbmZsdWVuY2lhZGEnKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdFZmVpdG8gZGUgQWxhdmFuY2EnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJTZWphIHVtIG1vZGVsbyBjb20gJG49MjUkIGUgJHA9NCQuIFNlIHVtYSBvYnNlcnZhw6fDo28gJGskIHBvc3N1aSB1bSByZXPDrWR1byBlc3R1ZGVudGl6YWRvICR8dF9rfCA9IDIuNSQgZSB1bSB2YWxvciBkZSBhbGF2YW5jYWdlbSAkaF97a2t9ID0gMC41JCwgY2xhc3NpZmlxdWUgZXN0YSBvYnNlcnZhw6fDo28gc2VndW5kbyBvIGNyaXTDqXJpbyBmb3JtYWwgZSBqdXN0aWZpcXVlIHN1YSBpbXBvcnTDom5jaWEgcGFyYSBvIGRpYWduw7NzdGljbyBkbyBtb2RlbG8uIiwgImRpY2EiOiAiQ29tcGFyZSBvcyB2YWxvcmVzIGZvcm5lY2lkb3MgY29tIG9zIGxpbWlhcmVzIGZvcm1haXMgcGFyYSAkfHRfaXwkIGUgJGhfe2lpfSQgYXByZXNlbnRhZG9zIG5vIHN1YnTDs3BpY28uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlByaW1laXJvLCBjYWxjdWxhbW9zIG8gbGltaWFyIGRlIGFsYXZhbmNhZ2VtOiAkXFxmcmFjezIocCsxKX17bn0gPSBcXGZyYWN7Mig0KzEpfXsyNX0gPSBcXGZyYWN7MTB9ezI1fSA9IDAuNCQuIiwgIkNvbXBhcmFuZG8gJGhfe2trfSA9IDAuNSQgY29tIG8gbGltaWFyIGRlICQwLjQkLCB0ZW1vcyAkMC41ID4gMC40JCwgbG9nbyDDqSB1bSBwb250byBkZSBhbGF2YW5jYS4iLCAiQ29tcGFyYW5kbyAkfHRfa3wgPSAyLjUkIGNvbSBvIGNyaXTDqXJpbyAkfHRfaXwgPiAyJCwgdGVtb3MgJDIuNSA+IDIkLCBsb2dvIMOpIGNsYXNzaWZpY2FkbyBjb21vIG91dGxpZXIuIiwgIkNvbmNsdXPDo286IEVzdGEgb2JzZXJ2YcOnw6NvIMOpIHRhbnRvIHVtIHBvbnRvIGRlIGFsYXZhbmNhIHF1YW50byB1bSBvdXRsaWVyLCBzZW5kbyB1bWEgb2JzZXJ2YcOnw6NvIGFsdGFtZW50ZSBpbmZsdWVudGUgcXVlIHBvZGUgZGlzdG9yY2VyIHNldmVyYW1lbnRlIG8gbW9kZWxvIGRlIHJlZ3Jlc3PDo28uIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfV19').decode('utf-8'))


    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    
    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do total de exercícios
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discs = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcqs) + len(discs)
    acertos = sum(1 for v in st.session_state.respostas_certas.values() if v)
    
    # Barra de progresso
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    
    st.divider()
    
    # --- Seção de Questões de Múltipla Escolha ---
    if mcqs:
        st.subheader("📝 Questões de Múltipla Escolha")
        for i, questao in enumerate(mcqs):
            with st.container():
                st.markdown(f"**Questão {i+1}:** {questao.get('enunciado')}")
                
                # Referência bibliográfica
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                # Plotly opcional
                codigo = questao.get("codigo_plotly")
                if codigo:
                    try:
                        local_vars = {"go": go, "np": np}
                        exec(codigo, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True)
                    except Exception as e:
                        st.error(f"Erro ao renderizar gráfico: {e}")
    
                # Alternativas
                alts = questao.get("alternativas", {})
                escolha = st.radio(
                    "Escolha uma opção:",
                    options=list(alts.keys()),
                    format_func=lambda x: f"{x}: {alts[x]}",
                    key=f"radio_mcq_{i}"
                )
                
                # Dica
                if st.button("💡 Dica", key=f"dica_mcq_{i}"):
                    st.info(questao.get("dica", "Dica indisponível."))
                
                # Verificação
                if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
                    if escolha == questao.get("alternativa_correta"):
                        st.success("Correto! Muito bem.")
                        st.session_state.respostas_certas[f"mcq_{i}"] = True
                        st.rerun()
                    else:
                        st.error("Resposta incorreta. Tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
                
                # Gabarito comentado
                with st.expander("✅ Ver Gabarito Comentado"):
                    st.write(questao.get("gabarito_comentado", "Gabarito indisponível."))
            
            st.divider()
    
    # --- Seção de Questões Discursivas ---
    if discs:
        st.subheader("✍️ Questões Discursivas e Práticas")
        for i, questao in enumerate(discs):
            with st.container():
                st.markdown(f"**Questão {i+1}:** {questao.get('enunciado')}")
                
                # Referência
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                # Plotly opcional
                codigo = questao.get("codigo_plotly")
                if codigo:
                    try:
                        local_vars = {"go": go, "np": np, "px": __import__("plotly.express")}
                        exec(codigo, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True)
                    except Exception as e:
                        st.error(f"Erro ao renderizar gráfico: {e}")
    
                st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
                
                # Lógica de validação numérica ou checkbox
                esperado = questao.get("resposta_numerica_esperada")
                if esperado is not None:
                    val_user = st.number_input("Digite o resultado numérico para validação:", format="%.4f", key=f"num_disc_{i}")
                    if st.button("Validar Cálculo", key=f"btn_val_{i}"):
                        if abs(val_user - esperado) <= max(0.01, 0.01 * abs(esperado)):
                            st.success("Resposta Numérica Correta! Excelente trabalho.")
                            st.session_state.respostas_certas[f"disc_{i}"] = True
                            st.rerun()
                        else:
                            st.error("O valor calculado difere do gabarito. Verifique suas fórmulas.")
                else:
                    if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                    else:
                        st.session_state.respostas_certas[f"disc_{i}"] = False
    
                # Dica
                if st.button("💡 Dica", key=f"dica_disc_{i}"):
                    st.info(questao.get("dica", "Dica indisponível."))
    
                # Resolução passo a passo
                with st.expander("✅ Ver Resolução Detalhada"):
                    for passo in questao.get("gabarito_passo_a_passo", []):
                        st.write(f"- {passo}")
            
            st.divider()
