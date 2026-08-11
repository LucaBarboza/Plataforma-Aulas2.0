import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDEgLSBUw7NwaWNvIDEuMjogRGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgZGEgbcOpZGlhIGUgZGEgcHJvcG9yw6fDo28iLCAicmVmZXJlbmNpYXNfYmlibGlvZ3JhZmljYXNfZmluYWlzIjogWyJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDEwLCBwcC4gMjczLTI4NiIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDExLCBwcC4gMzAwLCAzMTIiXX0=').decode('utf-8'))

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

    # Cabeçalho do subtópico
    st.header(r"O Conceito de Distribuição Amostral e Variabilidade Inferencial")
    
    # Introdução teórica
    st.markdown(r"""
    A inferência estatística fundamenta-se na transição estratégica do desconhecido para o estimado. Em cenários onde o acesso à totalidade da população é inviável, extraímos amostras aleatórias para inferir parâmetros populacionais. 
    
    Contudo, a média amostral é uma variável aleatória que flutua conforme o plano amostral. Esta estrutura teórica é o alicerce que permite quantificar a precisão e a incerteza de nossas conclusões.
    """)
    
    st.info(r"A distribuição amostral descreve precisamente o comportamento probabilístico dos estimadores, transformando estimativas pontuais em processos rigorosos controlados pela probabilidade.")
    
    # Prosa expandida em tópicos
    st.markdown(r"""
    ### 🔍 A Natureza da Incerteza Amostral
    A estatística inferencial permite transitar do microcosmo dos dados observados para o macrocosmo das verdades universais. Para compreender este processo, devemos observar dois pilares:
    
    * **Variabilidade Inherente:** A média amostral não é um número fixo, mas uma variável aleatória que herda sua natureza da população. Se repetíssemos a amostragem infinitas vezes, cada estimativa $\bar{X}$ oscilaria em torno do parâmetro $\mu$.
    * **O Papel do Erro Padrão:** O erro padrão, denotado por $\frac{\sigma}{\sqrt{n}}$, quantifica o quanto nossas estimativas dispersam-se do valor real, permitindo a construção de intervalos de confiança rigorosos.
    """)
    
    st.warning(r"A média amostral é um estimador não-viciado. Isso significa que, em média, nossas estimativas coincidem com o valor populacional real, conferindo validade científica à inferência.")
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Propriedades da Média Amostral")
    st.markdown(r"As propriedades fundamentais que regem o comportamento da média amostral são definidas pelo seu valor esperado e sua variância:")
    st.latex(r"E(\bar{X}) = \mu \quad \text{e} \quad Var(\bar{X}) = \frac{\sigma^2}{n}")
    
    # Dedução Analítica
    st.markdown(r"**Dedução da Propriedade de Não-Viés:**")
    st.latex(r"E(\bar{X}) = E\left(\frac{1}{n} \sum_{i=1}^{n} X_i\right) = \frac{1}{n} \sum_{i=1}^{n} E(X_i) = \frac{n\mu}{n} = \mu")
    
    st.markdown(r"**Dedução da Variância da Média Amostral:**")
    st.latex(r"Var(\bar{X}) = Var\left(\frac{1}{n} \sum_{i=1}^{n} X_i\right) = \frac{1}{n^2} \sum_{i=1}^{n} Var(X_i) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Distribuição Amostral de n=2")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Simulação com População {1, 3, 5, 5, 7}")
        st.markdown(r"Consideramos uma população pequena com os valores {1, 3, 5, 5, 7}. Vamos analisar o comportamento da média amostral com amostras de tamanho n=2 selecionadas com reposição.")
        
        st.latex(r"\mu = 4,2 \quad \sigma^2 = 4,16 \quad n = 2")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo do Valor Esperado: E(\bar{X}) = \mu = 4,2")
        st.markdown(r"- Cálculo da Variância da Média Amostral: Var(\bar{X}) = \frac{4,16}{2} = 2,08")
        
        st.success(r"O valor esperado de 4,2 comprova a propriedade de não-viés do estimador. A variância de 2,08 quantifica a incerteza residual, demonstrando que, mesmo em pequenas amostras, o conjunto das médias possíveis preserva o centro de gravidade populacional.")
    
    # Conclusão final do tópico
    st.markdown(r"""
    ---
    ### 🎓 Síntese Didática
    A convergência da média amostral para a normalidade, sustentada pelo Teorema Central do Limite, é a resiliência matemática que torna a estatística inferencial uma ferramenta universal. Compreender que a variância decresce com o aumento de $n$ é entender o equilíbrio entre custo computacional/coleta e precisão estatística.
    """)

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    st.header(r"O Teorema Limite Central e a Convergência para a Normalidade")
    
    st.markdown(r"""
    A importância do Teorema Limite Central (TLC) para a estatística é monumental, atuando como o elo que confere ordem à aleatoriedade complexa. Ele postula que, sob condições de independência e variância finita, a média amostral de um grande volume de observações converge para uma distribuição normal, independentemente da forma original dos dados.
    """)
    
    st.markdown(r"""
    Este resultado viabiliza a inferência prática, fornecendo o rigor necessário para a construção de intervalos de confiança e testes de hipóteses quando o formato da população é desconhecido ou assimétrico.
    """)
    
    st.info(r"A maior parte dos fenômenos do mundo real não é normalmente distribuída. O TLC, contudo, atua como um operador de suavização que filtra as singularidades dos dados através da agregação amostral.")
    
    st.markdown(r"""
    ### 📐 O Coração Matemático: Convergência Assintótica
    Ao considerarmos uma sequência de variáveis aleatórias independentes e identicamente distribuídas (IID) com média finita $\mu$ e variância finita $\sigma^2$, a estatística padronizada converge para uma distribuição normal padrão.
    """)
    
    st.latex(r"Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{n \to \infty} N(0, 1)")
    
    st.markdown(r"A dedução analítica desta relação fundamental segue os passos abaixo:")
    
    st.latex(r"Z = \frac{\bar{X} - E(\bar{X})}{\sqrt{Var(\bar{X})}}")
    st.latex(r"E(\bar{X}) = \mu")
    st.latex(r"Var(\bar{X}) = \frac{\sigma^2}{n}")
    st.latex(r"Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}")
    st.latex(r"\lim_{n \to \infty} P(Z \le z) = \Phi(z)")
    
    st.markdown(r"""
    ### 📈 Casos de Aplicação Prática: Controle de Qualidade
    """)
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Tempo de vida de transistores")
        st.markdown(r"Uma fábrica de componentes monitora o tempo de vida de transistores. Históricos indicam média $\mu = 500$ horas e variância $\sigma^2 = 100$ horas². Para uma amostra de $n=100$, busca-se a probabilidade da média $\bar{X}$ estar entre 498 e 502 horas.")
        st.latex(r"\mu = 500, \sigma^2 = 100, n = 100")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Erro Padrão: $EP(\bar{X}) = \sqrt{100 / 100} = 1$")
        st.markdown(r"- Escores Z: $Z_1 = (498-500)/1 = -2$ e $Z_2 = (502-500)/1 = 2$")
        st.markdown(r"- Probabilidade: $P(-2 < Z < 2) \approx 0,9544$")
        st.success(r"Com 95,44% de probabilidade, a média amostral encontra-se no intervalo de 498 a 502 horas, validando a robustez do processo.")
    
    st.markdown(r"### 🚀 Simulador: Visualizador de Convergência do TLC")
    col1, col2 = st.columns(2)
    with col1:
        n_amostras = st.slider(r"Tamanho da amostra (n)", 5, 500, 30, key=r"n_sim_subtopico_2")
    with col2:
        dist_tipo = st.selectbox(r"Distribuição Populacional", [r"Uniforme", r"Exponencial"], key=r"dist_sim_subtopico_2")
    
    if dist_tipo == r"Uniforme":
        dados = np.random.uniform(0, 100, (n_amostras, 1000)).mean(axis=0)
    else:
        dados = np.random.exponential(50, (n_amostras, 1000)).mean(axis=0)
    
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=dados, histnorm=r"probability density", name=r"Distribuição das Médias", marker_color=r"#1E3A8A"))
    fig.update_layout(
        template=r"plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Distribuição das Médias Amostrais</b>", font=dict(size=14, color=r"#1E293B", family=r"Arial, sans-serif"), x=0.0, y=0.95),
        legend=dict(orientation=r"h", yanchor=r"bottom", y=1.02, xanchor=r"right", x=1.0, font=dict(size=9, color=r"#64748B"), bgcolor=r"rgba(255, 255, 255, 0.8)", bordercolor=r"#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor=r"#FFFFFF", font_size=12, font_color=r"#1E293B")
    )
    fig.update_xaxes(title=dict(text=r"Valor da Média Amostral", font=dict(size=11, color=r"#1E293B")), tickfont=dict(size=9, color=r"#64748B"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True)
    fig.update_yaxes(title=dict(text=r"Densidade", font=dict(size=11, color=r"#1E293B")), tickfont=dict(size=9, color=r"#64748B"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True)
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    st.info(f"Ao fixar n = {n_amostras}, observamos a convergência das médias amostrais para um formato gaussiano. Quanto maior o tamanho da amostra, menor a dispersão, conforme demonstrado pelo erro padrão decrescente.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy.stats import binom, norm
    
    # Cabeçalho do Subtópico
    st.header(r"Distribuição Amostral da Proporção e Modelagem Binomial")
    
    # Prosa Teórica
    st.markdown(r"""
    Ao iniciarmos o estudo da inferência estatística, frequentemente nos concentramos em variáveis quantitativas que permitem o cálculo da média aritmética tradicional. Contudo, em uma parcela significativa das aplicações científicas e sociais, encontramo-nos diante de variáveis qualitativas dicotômicas, onde os dados não se manifestam por grandezas numéricas contínuas, mas pela ocorrência ou não de um evento específico.
    """)
    
    st.info(r"Para tratar tais fenômenos, devemos transitar do domínio da média amostral para o domínio da proporção amostral, fundamentando-nos na distribuição de Bernoulli como o bloco construtor de processos de sucesso ou fracasso.")
    
    st.markdown(r"""
    A proporção amostral $\hat{p}$ não é apenas uma métrica, mas um estimador pontual da proporção populacional $p$. Suas propriedades fundamentais incluem:
    *   **Não-viesagem:** O valor esperado do estimador coincide com o parâmetro populacional.
    *   **Variabilidade:** A dispersão depende diretamente da proporção e do tamanho da amostra, atingindo incerteza máxima quando $p = 0,5$.
    *   **Convergência:** Com o aumento de $n$, a distribuição se concentra em torno de $p$ via Teorema Central do Limite.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Distribuição Amostral")
    st.latex(r"\text{E}(\hat{p}) = p \quad \text{e} \quad \text{Var}(\hat{p}) = \frac{p(1-p)}{n}")
    
    # Dedução Analítica
    st.latex(r"\text{E}(\hat{p}) = \frac{1}{n} \text{E}(X) = \frac{np}{n} = p")
    st.markdown(r"A esperança matemática confirma que o estimador é não-viesado.")
    st.latex(r"\text{Var}(\hat{p}) = \frac{1}{n^2} \text{Var}(X) = \frac{np(1-p)}{n^2} = \frac{p(1-p)}{n}")
    st.markdown(r"A variância diminui conforme o tamanho da amostra aumenta.")
    st.latex(r"\text{EP}(\hat{p}) = \sqrt{\frac{p(1-p)}{n}}")
    
    # Simulador Interativo
    st.subheader(r"📊 Simulador: Binomial vs. Normal")
    col1, col2 = st.columns(2)
    with col1:
        n_sim = st.slider(r"Tamanho da Amostra (n)", 10, 200, 100, key=r"n_sim_subtopico_3")
    with col2:
        p_sim = st.slider(r"Probabilidade (p)", 0.05, 0.95, 0.5, key=r"p_sim_subtopico_3")
    
    # Lógica do Simulador
    x = np.arange(0, n_sim + 1)
    y_binom = binom.pmf(x, n_sim, p_sim)
    x_norm = np.linspace(0, n_sim, 500)
    y_norm = norm.pdf(x_norm, n_sim * p_sim, np.sqrt(n_sim * p_sim * (1 - p_sim)))
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y_binom, name=r"Distribuição Binomial", marker_color="#1E3A8A", opacity=0.6))
    fig.add_trace(go.Scatter(x=x_norm, y=y_norm, name=r"Aproximação Normal", line=dict(color="#10B981", width=3)))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Convergência da Distribuição Binomial</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        xaxis=dict(title=dict(text="Número de Sucessos", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Probabilidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    # Laudo Dinâmico
    ep_val = np.sqrt(p_sim * (1 - p_sim) / n_sim)
    st.info(f"Com n = {n_sim} e p = {p_sim:.2f}, o erro padrão é de {ep_val:.4f}. Note como o aumento de n reduz o erro padrão, tornando a estimativa mais precisa e a curva mais estreita.")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Ensaio Clínico")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Eficácia de Tratamento")
        st.markdown(r"Em um ensaio clínico, a taxa de sucesso populacional é de $p = 0,70$. Para uma amostra de $n=100$ pacientes, deseja-se encontrar o valor esperado e o erro padrão.")
        st.latex(r"p = 0,70, \quad n = 100")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- E($\hat{p}$) = 0,70")
        st.markdown(r"- Var($\hat{p}$) = (0,70 * 0,30) / 100 = 0,0021")
        st.markdown(r"- EP($\hat{p}$) = $\sqrt{0,0021} \approx 0,0458$")
        st.success(r"O erro padrão de 0,0458 indica uma dispersão controlada da estimativa de sucesso. Como as condições np > 5 e n(1-p) > 5 são atendidas, o uso da normal é plenamente justificado para a inferência clínica.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDEgLSBUw7NwaWNvIDEuMjogRGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgZGEgbcOpZGlhIGUgZGEgcHJvcG9yw6fDo28iLCAicXVlc3RvZXNfbXVsdGlwbGFfZXNjb2xoYSI6IFt7ImVudW5jaWFkbyI6ICJVbWEgZW1wcmVzYSBkZSB0ZWNub2xvZ2lhIG1vbml0b3JhIG8gdGVtcG8gZGUgcHJvY2Vzc2FtZW50byBkZSBzZXJ2aWRvcmVzIGVtIG51dmVtLCBzZWd1aW5kbyB1bWEgZGlzdHJpYnVpw6fDo28gZGUgcHJvYmFiaWxpZGFkZSBjb20gbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSA9IDEyMCQgbXMgZSB2YXJpw6JuY2lhICRcXHNpZ21hXjIgPSA2NCQgbXMkXjIkLiBVbSBlbmdlbmhlaXJvIGRlIERldk9wcyBzZWxlY2lvbmEgYWxlYXRvcmlhbWVudGUgdW1hIGFtb3N0cmEgYWxlYXTDs3JpYSBzaW1wbGVzIChBQVMpIGRlICRuID0gMTYkIHNlcnZpZG9yZXMgcGFyYSByZWFsaXphciB1bSB0ZXN0ZSBkZSBjYXJnYS4gQ29uc2lkZXJhbmRvIHF1ZSBhIGVzdGF0w61zdGljYSBkZSBpbnRlcmVzc2Ugw6kgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCwgcXVhbCDDqSBvIGNvbXBvcnRhbWVudG8gZXNwZXJhZG8gcGFyYSBhIHZhcmnDom5jaWEgZGEgZGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgZGEgbcOpZGlhLCAkVmFyKFxcYmFye1h9KSQsIGUgY29tbyBpc3NvIHJlZmxldGUgYSB2YXJpYWJpbGlkYWRlIGluZmVyZW5jaWFsPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSB2YXJpw6JuY2lhIGRhIG3DqWRpYSBhbW9zdHJhbCDDqSAkNCQgbXMkXjIkLCBpbmRpY2FuZG8gcXVlIG8gZXJybyBhbW9zdHJhbCDDqSBtaW5pbWl6YWRvIGNvbmZvcm1lIGF1bWVudGFtb3MgbyB0YW1hbmhvIGRhIGFtb3N0cmEuIiwgIkIiOiAiQSB2YXJpw6JuY2lhIGRhIG3DqWRpYSBhbW9zdHJhbCDDqSAkMTYkIG1zJF4yJCwgbW9zdHJhbmRvIHF1ZSBhIG3DqWRpYSBkYXMgYW1vc3RyYXMgZGlzcGVyc2Etc2UgbWFpcyBxdWUgb3MgdmFsb3JlcyBpbmRpdmlkdWFpcyBkYSBwb3B1bGHDp8Ojby4iLCAiQyI6ICJBIHZhcmnDom5jaWEgZGEgbcOpZGlhIGFtb3N0cmFsIMOpICQ2NCQgbXMkXjIkLCBtYW50ZW5kby1zZSBjb25zdGFudGUgaW5kZXBlbmRlbnRlbWVudGUgZG8gdGFtYW5obyBkYSBhbW9zdHJhLiIsICJEIjogIkEgdmFyacOibmNpYSBkYSBtw6lkaWEgYW1vc3RyYWwgw6kgJDAuMjUkIG1zJF4yJCwgc3VnZXJpbmRvIHVtYSBtYWlvciBkaXNwZXJzw6NvIGRhIG3DqWRpYSBhbW9zdHJhbCBjb21wYXJhZGEgw6AgcG9wdWxhw6fDo28uIiwgIkUiOiAiQSB2YXJpw6JuY2lhIGRhIG3DqWRpYSBhbW9zdHJhbCDDqSBpbXBvc3PDrXZlbCBkZSBkZXRlcm1pbmFyIHNlbSBjb25oZWNlciBhIGZvcm1hIGV4YXRhIGRhIGRpc3RyaWJ1acOnw6NvIG9yaWdpbmFsIGRhIHBvcHVsYcOnw6NvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIHByb3ByaWVkYWRlIGRhIHZhcmnDom5jaWEgZGEgbcOpZGlhIGFtb3N0cmFsOiAkVmFyKFxcYmFye1h9KSA9IFxcZnJhY3tcXHNpZ21hXjJ9e259JC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBhcmEgdW1hIEFBUyBkZSB0YW1hbmhvICRuPTE2JCByZXRpcmFkYSBkZSB1bWEgcG9wdWxhw6fDo28gY29tIHZhcmnDom5jaWEgJFxcc2lnbWFeMiA9IDY0JCwgYSB2YXJpw6JuY2lhIGRhIGRpc3RyaWJ1acOnw6NvIGFtb3N0cmFsIGRhIG3DqWRpYSDDqSBkYWRhIHBvciAkVmFyKFxcYmFye1h9KSA9IFxcZnJhY3tcXHNpZ21hXjJ9e259ID0gXFxmcmFjezY0fXsxNn0gPSA0JC4gRXN0ZSByZXN1bHRhZG8gw6kgZnVuZGFtZW50YWwgbmEgaW5mZXLDqm5jaWEsIHBvaXMgZGVtb25zdHJhIHF1ZSwgYW8gYXVtZW50YXIgbyB0YW1hbmhvIGRhIGFtb3N0cmEsIGEgdmFyaWFiaWxpZGFkZSBkbyBlc3RpbWFkb3IgJFxcYmFye1h9JCBkaW1pbnVpLCB0b3JuYW5kbyBhIGVzdGltYXRpdmEgbWFpcyBwcmVjaXNhIGUgZXN0w6F2ZWwgYW8gcmVkb3IgZGEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnBvcCA9IG5wLnJhbmRvbS5ub3JtYWwoMTIwLCA4LCAxMDAwMClcbm1lZGlhX2Ftb3N0cmFsX2Rpc3QgPSBucC5yYW5kb20ubm9ybWFsKDEyMCwgOC9ucC5cXHNxcnQoMTYpLCAxMDAwMClcbmZpZy5hZGRfdHJhY2UoZ28uSGlzdG9ncmFtKHg9cG9wLCBuYW1lPSdEaXN0cmlidWnDp8OjbyBQb3B1bGFjaW9uYWwnLCBtYXJrZXJfY29sb3I9JyMxRTNBOEEnLCBvcGFjaXR5PTAuNikpXG5maWcuYWRkX3RyYWNlKGdvLkhpc3RvZ3JhbSh4PW1lZGlhX2Ftb3N0cmFsX2Rpc3QsIG5hbWU9J0Rpc3RyaWJ1acOnw6NvIEFtb3N0cmFsIGRlICRcXGJhcntYfSQgKCRuPTE2JCknLCBtYXJrZXJfY29sb3I9JyMxMEI5ODEnLCBvcGFjaXR5PTAuOCkpXG5maWcudXBkYXRlX2xheW91dChiYXJtb2RlPSdvdmVybGF5JywgdGl0bGU9JzxiPkNvbXBhcmHDp8OjbzogUG9wdWxhw6fDo28gdnMgRGlzdHJpYnVpw6fDo28gQW1vc3RyYWw8L2I+JywgeGF4aXNfdGl0bGU9J1RlbXBvIChtcyknLCB5YXhpc190aXRsZT0nRnJlcXXDqm5jaWEnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMCwgcC4gMjc4In0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBzb2JyZSBvIGNvbnN1bW8gZGUgZW5lcmdpYSBlbMOpdHJpY2EgZGUgYXBhcmVsaG9zIElvVCwgc2FiZS1zZSBxdWUgYSB2YXJpw6F2ZWwgWCAoY29uc3VtbyBkacOhcmlvKSB0ZW0gbcOpZGlhICRcXG11JCBlIHZhcmnDom5jaWEgJFxcc2lnbWFeMiQuIFVtIHBlc3F1aXNhZG9yIGNvbGV0YSB2w6FyaWFzIGFtb3N0cmFzIGRlIHRhbWFuaG8gJG4kIGUgY2FsY3VsYSBwYXJhIGNhZGEgdW1hIG8gdmFsb3IgZGUgJFNeMiQgKHZhcmnDom5jaWEgYW1vc3RyYWwpLiBBbyBhbmFsaXNhciBhIGRpc3RyaWJ1acOnw6NvIGRlICRTXjIkIGVtIHJlbGHDp8OjbyBhbyBwYXLDom1ldHJvICRcXHNpZ21hXjIkLCBvIHBlc3F1aXNhZG9yIG9ic2VydmEgcXVlICRFKFNeMikgPSBcXHNpZ21hXjIkLiBPIHF1ZSBlc3NhIHByb3ByaWVkYWRlIGVzdGF0w61zdGljYSBub3MgaW5mb3JtYSBzb2JyZSBvIGVzdGltYWRvciAkU14yJD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIlF1ZSAkU14yJCDDqSB1bSBlc3RpbWFkb3IgdmljaWFkbywgcG9pcyBzdWJlc3RpbWEgYSB2YXJpw6JuY2lhIHBvcHVsYWNpb25hbC4iLCAiQiI6ICJRdWUgJFNeMiQgw6kgdW0gZXN0aW1hZG9yIG7Do28tdmllc2FkbywgcGVybWl0aW5kbyBxdWUsIGVtIG3DqWRpYSwgYSBlc3RhdMOtc3RpY2EgYW1vc3RyYWwgYWNlcnRlIG8gdmFsb3IgZG8gcGFyw6JtZXRybyBwb3B1bGFjaW9uYWwuIiwgIkMiOiAiUXVlICRTXjIkIGRlcGVuZGUgZXN0cml0YW1lbnRlIGRvIHRhbWFuaG8gYW1vc3RyYWwsIHNlbmRvIGlycmVsZXZhbnRlIHBhcmEgZ3JhbmRlcyBwb3B1bGHDp8O1ZXMuIiwgIkQiOiAiUXVlIGEgZGlzdHJpYnVpw6fDo28gZGUgJFNeMiQgw6kgc2VtcHJlIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwsIGluZGVwZW5kZW50ZW1lbnRlIGRhIGRpc3RyaWJ1acOnw6NvIGRhIHBvcHVsYcOnw6NvIG9yaWdpbmFsLiIsICJFIjogIlF1ZSBhIHZhcmnDom5jaWEgYW1vc3RyYWwgc2VtcHJlIGNvaW5jaWRpcsOhIGV4YXRhbWVudGUgY29tIGEgdmFyacOibmNpYSBwb3B1bGFjaW9uYWwgZW0gcXVhbHF1ZXIgYW1vc3RyYSBjb2xldGFkYS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk8gdmFsb3IgZXNwZXJhZG8gZG8gZXN0aW1hZG9yIHNlciBpZ3VhbCBhbyBwYXLDom1ldHJvIMOpIGEgZGVmaW5pw6fDo28gdGXDs3JpY2EgZGUgdW0gZXN0aW1hZG9yIG7Do28tdmllc2Fkby4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgcHJvcHJpZWRhZGUgJEUoU14yKSA9IFxcc2lnbWFeMiQgY2FyYWN0ZXJpemEgJFNeMiQgY29tbyB1bSBlc3RpbWFkb3IgbsOjby12aWVzYWRvIHBhcmEgYSB2YXJpw6JuY2lhIHBvcHVsYWNpb25hbCAkXFxzaWdtYV4yJC4gRW0gaW5mZXLDqm5jaWEgZXN0YXTDrXN0aWNhLCB1bSBlc3RpbWFkb3IgbsOjby12aWVzYWRvIMOpIGFsdGFtZW50ZSBkZXNlasOhdmVsLCBwb2lzIGdhcmFudGUgcXVlLCBzZSByZXBldMOtc3NlbW9zIG8gcHJvY2Vzc28gZGUgYW1vc3RyYWdlbSBpbmRlZmluaWRhbWVudGUsIGEgbcOpZGlhIGRvcyB2YWxvcmVzIGNhbGN1bGFkb3MgZGUgJFNeMiQgc2VyaWEgZXhhdGFtZW50ZSBvIHBhcsOibWV0cm8gcG9wdWxhY2lvbmFsICRcXHNpZ21hXjIkLiBJc3NvIHJlZHV6IG8gZXJybyBzaXN0ZW3DoXRpY28gbmFzIG5vc3NhcyBlc3RpbWF0aXZhcy4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEwLCBwLiAyODYifSwgeyJlbnVuY2lhZG8iOiAiVW1hIGVtcHJlc2EgZGUgbWFudWZhdHVyYSBkZSBkaXNwb3NpdGl2b3MgZWxldHLDtG5pY29zIHV0aWxpemEgdW0gc2Vuc29yIGRlIGFsdGEgcHJlY2lzw6NvIHBhcmEgbW9uaXRvcmFyIG8gcGVzbyBkZSBjb21wb25lbnRlcyBlbSB1bWEgbGluaGEgZGUgcHJvZHXDp8Ojby4gU2FiZS1zZSwgcG9yIGhpc3TDs3JpY28gZGUgbG9uZ28gcHJhem8sIHF1ZSBhIHZhcmnDom5jaWEgZG8gcGVzbyBkb3MgY29tcG9uZW50ZXMgZmFicmljYWRvcyDDqSBkZSAkXFxzaWdtYV4yID0gNCwwIFxcdGV4dHsgZ3JhbWFzfV4yJC4gTyBlbmdlbmhlaXJvIHJlc3BvbnPDoXZlbCBkZXNlamEgZXN0aW1hciBhIG3DqWRpYSBwb3B1bGFjaW9uYWwgJFxcbXUkIGRvIHBlc28gZGVzc2VzIGNvbXBvbmVudGVzIHV0aWxpemFuZG8gYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBkZSB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIHNpbXBsZXMgZGUgJG4gPSAxNiQgdW5pZGFkZXMuIFF1YWwgw6kgYSB2YXJpw6JuY2lhIGRvIGVzdGltYWRvciBtw6lkaWEgYW1vc3RyYWwgJFZhcihcXGJhcntYfSkkIGUgcXVhbCBhIHByb3ByaWVkYWRlIHF1ZSBnYXJhbnRlIHF1ZSAkXFxiYXJ7WH0kIMOpIHVtIGVzdGltYWRvciBjZW50cmFkbyBlbSAkXFxtdSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJWYXJpw6JuY2lhID0gMCwyNSBlIG8gZXN0aW1hZG9yIMOpIG7Do28tdmllc2FkbywgcG9pcyAkRShcXGJhcntYfSkgPSBcXG11JC4iLCAiQiI6ICJWYXJpw6JuY2lhID0gMCw1MCBlIG8gZXN0aW1hZG9yIMOpIG7Do28tdmllc2FkbywgcG9pcyAkRShcXGJhcntYfSkgPSBcXHNpZ21hXjIvbiQuIiwgIkMiOiAiVmFyacOibmNpYSA9IDAsMjUgZSBvIGVzdGltYWRvciDDqSB2aWVzYWRvLCBwb2lzICRWYXIoXFxiYXJ7WH0pID0gXFxzaWdtYV4yL24kLiIsICJEIjogIlZhcmnDom5jaWEgPSA0LDAwIGUgbyBlc3RpbWFkb3Igw6kgbsOjby12aWVzYWRvLCBwb2lzICRFKFxcYmFye1h9KSA9IFxcbXUkLiIsICJFIjogIlZhcmnDom5jaWEgPSAwLDA2MjUgZSBvIGVzdGltYWRvciDDqSBuw6NvLXZpZXNhZG8sIHBvaXMgJEUoXFxiYXJ7WH0pID0gXFxtdS9uJC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgJFZhcihcXGJhcntYfSkgPSBcXHNpZ21hXjIvbiQgZSBxdWUgYSBhdXPDqm5jaWEgZGUgdmnDqXMgw6kgZGVmaW5pZGEgcGVsYSBpZ3VhbGRhZGUgZW50cmUgbyB2YWxvciBlc3BlcmFkbyBkbyBlc3RpbWFkb3IgZSBvIHBhcsOibWV0cm8gcG9wdWxhY2lvbmFsLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUGFyYSByZXNvbHZlciBlc3RhIHF1ZXN0w6NvLCBhcGxpY2Ftb3MgYXMgcHJvcHJpZWRhZGVzIHRlw7NyaWNhcyBkYSBtw6lkaWEgYW1vc3RyYWwuIEEgdmFyacOibmNpYSBkbyBlc3RpbWFkb3Igw6kgZGFkYSBwb3IgJFZhcihcXGJhcntYfSkgPSBcXHNpZ21hXjIvbiQuIFN1YnN0aXR1aW5kbyBvcyB2YWxvcmVzLCB0ZW1vcyAkVmFyKFxcYmFye1h9KSA9IDQsMCAvIDE2ID0gMCwyNSBcXHRleHR7IGd9XjIkLiBTb2JyZSBhIHByb3ByaWVkYWRlIGRlIG7Do28tdmllc2FtZW50bywgcG9yIGRlZmluacOnw6NvLCB1bSBlc3RpbWFkb3IgJFQkIMOpIG7Do28tdmllc2FkbyBwYXJhIHVtIHBhcsOibWV0cm8gJFxcdGhldGEkIHNlICRFKFQpID0gXFx0aGV0YSQuIENvbW8gJEUoXFxiYXJ7WH0pID0gXFxtdSQsIGEgbcOpZGlhIGFtb3N0cmFsIMOpIHVtIGVzdGltYWRvciBuw6NvLXZpZXNhZG8gZGEgbcOpZGlhIHBvcHVsYWNpb25hbC4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5CYXIoeD1bJ1ZhcmnDom5jaWEnXSwgeT1bMC4yNV0sIG1hcmtlcl9jb2xvcj0nIzFFM0E4QScsIG5hbWU9J1ZhcihYX2JhcnJhKScpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J1ZhcmnDom5jaWEgZGEgTcOpZGlhIEFtb3N0cmFsIChuPTE2KScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnLCB4YXhpcz1kaWN0KGZpeGVkcmFuZ2U9VHJ1ZSksIHlheGlzPWRpY3QoZml4ZWRyYW5nZT1UcnVlKSkiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMCwgcC4gMjc4In0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBjbMOtbmljbyBwYXJhIGF2YWxpYXIgbyB0ZW1wbyBkZSByZWHDp8OjbyBkZSBwYWNpZW50ZXMgc29iIGVmZWl0byBkZSB1bSBub3ZvIG1lZGljYW1lbnRvLCB1bSBwZXNxdWlzYWRvciBjb2xldGEgYW1vc3RyYXMgYWxlYXTDs3JpYXMgZGUgdGFtYW5ob3MgZGlmZXJlbnRlcy4gRWxlIG9ic2VydmEgcXVlLCBhbyBhdW1lbnRhciBvIHRhbWFuaG8gZGEgYW1vc3RyYSAkbiQgZGUgMjUgcGFyYSAxMDAsIGEgdmFyacOibmNpYSBkbyBlc3RpbWFkb3IgbcOpZGlhIGFtb3N0cmFsICRWYXIoXFxiYXJ7WH0pJCBzb2ZyZSB1bWEgcmVkdcOnw6NvIHNpZ25pZmljYXRpdmEuIEFzc3VtaW5kbyBxdWUgYSB2YXJpw6JuY2lhIHBvcHVsYWNpb25hbCAkXFxzaWdtYV4yJCBwZXJtYW5lY2UgY29uc3RhbnRlLCBxdWFsIMOpIGEgcmF6w6NvIGVudHJlIGEgdmFyacOibmNpYSBkbyBlc3RpbWFkb3IgY29tICRuPTI1JCBlIGEgdmFyacOibmNpYSBjb20gJG49MTAwJD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjIiLCAiQiI6ICI0IiwgIkMiOiAiMCwyNSIsICJEIjogIjEwIiwgIkUiOiAiMCw1In0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJDb25zaWRlcmUgcXVlICRWYXIoXFxiYXJ7WH1fbikgPSBcXHNpZ21hXjIvbiQuIEEgcmF6w6NvIGVudHJlIGFzIHZhcmnDom5jaWFzIMOpICRcXGZyYWN7XFxzaWdtYV4yLzI1fXtcXHNpZ21hXjIvMTAwfSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJDYWxjdWxhbW9zIGEgdmFyacOibmNpYSBwYXJhIGNhZGEgdGFtYW5obyBkZSBhbW9zdHJhOiAkVmFyKFxcYmFye1h9X3syNX0pID0gXFxzaWdtYV4yLzI1JCBlICRWYXIoXFxiYXJ7WH1fezEwMH0pID0gXFxzaWdtYV4yLzEwMCQuIEEgcmF6w6NvIGVudHJlIGVsYXMgw6kgZGFkYSBwb3IgJFxcZnJhY3tcXHNpZ21hXjIvMjV9e1xcc2lnbWFeMi8xMDB9ID0gXFxmcmFjezEwMH17MjV9ID0gNCQuIFBvcnRhbnRvLCBhdW1lbnRhciBhIGFtb3N0cmEgZW0gNCB2ZXplcyByZWR1eiBhIHZhcmnDom5jaWEgZG8gZXN0aW1hZG9yIHBhcmEgMS80IGRvIHZhbG9yIG9yaWdpbmFsLCBkZW1vbnN0cmFuZG8gbyBlZmVpdG8gZGEgcmVkdcOnw6NvIGRhIGluY2VydGV6YSBjb20gbyBhdW1lbnRvIGRlICRuJC4iLCAiY29kaWdvX3Bsb3RseSI6ICJuID0gWzI1LCAxMDBdXG52YXJfdmFscyA9IFsxLzI1LCAxLzEwMF1cbmZpZyA9IGdvLkZpZ3VyZShkYXRhPWdvLlNjYXR0ZXIoeD1uLCB5PXZhcl92YWxzLCBtb2RlPSdsaW5lcyttYXJrZXJzJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJyksIG1hcmtlcj1kaWN0KHNpemU9MTApKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdSZWR1w6fDo28gZGEgVmFyacOibmNpYSBjb20gbyBUYW1hbmhvIEFtb3N0cmFsJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScsIHhheGlzPWRpY3QodGl0bGU9J1RhbWFuaG8gZGEgQW1vc3RyYSAobiknLCBmaXhlZHJhbmdlPVRydWUpLCB5YXhpcz1kaWN0KHRpdGxlPXInVmFyacOibmNpYSBSZWxhdGl2YSAoJFxcc2lnbWFeMi9uJCknLCBmaXhlZHJhbmdlPVRydWUpKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEwLCBwLiAyNzkifSwgeyJlbnVuY2lhZG8iOiAiVW1hIGVtcHJlc2EgZGUgbWFudWZhdHVyYSBkZSBjb21wb25lbnRlcyBlbGV0csO0bmljb3MgcHJvZHV6IHNlbnNvcmVzIGN1am8gdGVtcG8gZGUgdmlkYSDDunRpbCBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gYXNzaW3DqXRyaWNhLCBjb20gbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSA9IDE1MDAkIGhvcmFzIGUgZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsICRcXHNpZ21hID0gNDAwJCBob3Jhcy4gTyBjb250cm9sZSBkZSBxdWFsaWRhZGUgZGVjaWRlIGF1ZGl0YXIgbG90ZXMsIHNvcnRlYW5kbyBhbW9zdHJhcyBkZSAkbiA9IDY0JCBzZW5zb3JlcyBlIGNhbGN1bGFuZG8gYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBkbyB0ZW1wbyBkZSB2aWRhLiBEZSBhY29yZG8gY29tIG8gVGVvcmVtYSBMaW1pdGUgQ2VudHJhbCwgcXVhbCDDqSBhIGRpc3RyaWJ1acOnw6NvIGFwcm94aW1hZGEgZGEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSQgZSBhIHByb2JhYmlsaWRhZGUgZGUgcXVlIGEgbcOpZGlhIGRlIHVtYSBhbW9zdHJhIHNlamEgaW5mZXJpb3IgYSAxNDAwIGhvcmFzPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJFxcYmFye1h9IFxcc2ltIE4oMTUwMCwgNDAwKSQ7ICRQKFxcYmFye1h9IDwgMTQwMCkgXFxhcHByb3ggMC4wMjI4JC4iLCAiQiI6ICIkXFxiYXJ7WH0gXFxzaW0gTigxNTAwLCA1MF4yKSQ7ICRQKFxcYmFye1h9IDwgMTQwMCkgXFxhcHByb3ggMC4wMjI4JC4iLCAiQyI6ICIkXFxiYXJ7WH0gXFxzaW0gTigxNTAwLCA0MDBeMikkOyAkUChcXGJhcntYfSA8IDE0MDApIFxcYXBwcm94IDAuNDAxMyQuIiwgIkQiOiAiJFxcYmFye1h9IFxcc2ltIE4oMTUwMCwgMjVeMikkOyAkUChcXGJhcntYfSA8IDE0MDApIFxcYXBwcm94IDAuMDAwMCQuIiwgIkUiOiAiJFxcYmFye1h9IFxcc2ltIE4oMTUwMCwgNTApJDsgJFAoXFxiYXJ7WH0gPCAxNDAwKSBcXGFwcHJveCAwLjA0NTYkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgw6kgZGFkbyBwb3IgJFxcc2lnbWFfe1xcYmFye1h9fSA9IFxcc2lnbWEgLyBcXHNxcnR7bn0kLiBPIFRMQyBnYXJhbnRlIHF1ZSBhIGRpc3RyaWJ1acOnw6NvIGFtb3N0cmFsIHRlbmRlIGEgdW1hIE5vcm1hbCBjb20gbcOpZGlhICRcXG11JCBlIHZhcmnDom5jaWEgJFxcc2lnbWFeMiAvIG4kLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUGVsbyBUZW9yZW1hIExpbWl0ZSBDZW50cmFsLCAkXFxiYXJ7WH0gXFxzaW0gTihcXG11LCBcXHNpZ21hXjIgLyBuKSQuIFRlbW9zICRcXG11ID0gMTUwMCQsICRcXHNpZ21hID0gNDAwJCBlICRuID0gNjQkLiBPIGRlc3ZpbyBwYWRyw6NvIGRhIG3DqWRpYSDDqSAkRVAoXFxiYXJ7WH0pID0gNDAwIC8gXFxzcXJ0ezY0fSA9IDQwMCAvIDggPSA1MCQuIFBvcnRhbnRvLCBhIHZhcmnDom5jaWEgw6kgJDUwXjIgPSAyNTAwJC4gUGFkcm9uaXphbmRvIHBhcmEgJFokOiAkWiA9ICgxNDAwIC0gMTUwMCkgLyA1MCA9IC0xMDAgLyA1MCA9IC0yJC4gQ29uc3VsdGFuZG8gYSB0YWJlbGEgZGEgbm9ybWFsLCAkUChaIDwgLTIpIFxcYXBwcm94IDAuMDIyOCQuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgxMzAwLCAxNzAwLCAyMDApXG55ID0gKDEgLyAoNTAgKiBucC5cXHNxcnQoMiAqIG5wLlxccGkpKSkgKiBucC5cXGV4cCgtMC41ICogKCh4IC0gMTUwMCkgLyA1MCkgKiogMilcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJywgd2lkdGg9MyksIG5hbWU9J0Rpc3RyaWJ1acOnw6NvICRcXGJhcntYfSQnKSlcbmZpZy5hZGRfdnJlY3QoeDA9MTMwMCwgeDE9MTQwMCwgZmlsbGNvbG9yPScjOTkxQjFCJywgb3BhY2l0eT0wLjMsIGxpbmVfd2lkdGg9MCwgbmFtZT0nw4FyZWEgZGUgUmVqZWnDp8OjbycpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nRGlzdHJpYnVpw6fDo28gQW1vc3RyYWwgZGEgTcOpZGlhICRcXGJhcntYfSQnLCB4YXhpc190aXRsZT0nTcOpZGlhIEFtb3N0cmFsICgkXFxiYXJ7WH0kKScsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEwLCBwLiAyODAifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gc2lzdGVtYSBkZSB0ZWxlY29tdW5pY2HDp8O1ZXMsIG8gcnXDrWRvIHBvciBzaW5hbCByZWNlYmlkbyDDqSB1bWEgdmFyacOhdmVsIGFsZWF0w7NyaWEgY29tIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCBjb25oZWNpZG8gZGUgJFxcc2lnbWEgPSAxMiQgZEIuIFNlIGNvbGV0YXJtb3MgMTQ0IG9ic2VydmHDp8O1ZXMgaW5kZXBlbmRlbnRlcyBwYXJhIGVzdGltYXIgbyBydcOtZG8gbcOpZGlvLCBxdWFsIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSBxdWUgbyBlcnJvIGFtb3N0cmFsLCBkZWZpbmlkbyBjb21vICR8XFxiYXJ7WH0gLSBcXG11fCQsIHNlamEgc3VwZXJpb3IgYSAyIGRCPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQXByb3hpbWFkYW1lbnRlIDAuMDQ1NiIsICJCIjogIkFwcm94aW1hZGFtZW50ZSAwLjAyMjgiLCAiQyI6ICJBcHJveGltYWRhbWVudGUgMC4wOTEyIiwgIkQiOiAiQXByb3hpbWFkYW1lbnRlIDAuOTU0NCIsICJFIjogIkFwcm94aW1hZGFtZW50ZSAwLjAwMjYifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIk8gZXJybyBwYWRyw6NvIMOpICRcXHNpZ21hIC8gXFxzcXJ0e259JC4gTyBlcnJvIGFtb3N0cmFsIG5vcm1hbGl6YWRvIMOpICRaID0gKFxcYmFye1h9IC0gXFxtdSkgLyBFUChcXGJhcntYfSkkLiBPIHByb2JsZW1hIHBlZGUgJFAofFp8ID4gMiAvIEVQKFxcYmFye1h9KSkkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBlcnJvIHBhZHLDo28gw6kgJEVQKFxcYmFye1h9KSA9IDEyIC8gXFxzcXJ0ezE0NH0gPSAxMiAvIDEyID0gMSQuIFF1ZXJlbW9zICRQKHxcXGJhcntYfSAtIFxcbXV8ID4gMikgPSBQKHxafCA+IDIgLyAxKSA9IFAofFp8ID4gMikkLiBQZWxhIHNpbWV0cmlhIGRhIG5vcm1hbCBwYWRyw6NvLCAkUChaID4gMikgKyBQKFogPCAtMikgPSAwLjAyMjggKyAwLjAyMjggPSAwLjA0NTYkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTAsIHAuIDI4MSJ9LCB7ImVudW5jaWFkbyI6ICJVbSBhbmFsaXN0YSBkZSBjb250cm9sZSBkZSBxdWFsaWRhZGUgZW0gdW1hIHBsYW50YSBkZSBzZW1pY29uZHV0b3JlcyBtb25pdG9yYSBhIHRheGEgZGUgZmFsaGFzICgkcCQpIGVtIHVtYSBsaW5oYSBkZSBwcm9kdcOnw6NvLCBxdWUgw6kgYXR1YWxtZW50ZSBkZSAwLjA0LiBQYXJhIGVzdGltYXIgYSBwcm9wb3LDp8OjbyBkZSBpdGVucyBkZWZlaXR1b3NvcywgbyBhbmFsaXN0YSBjb2xldGEgdW1hIGFtb3N0cmEgYWxlYXTDs3JpYSBkZSB0YW1hbmhvICRuPTEwMCQgZSBjYWxjdWxhIGEgcHJvcG9yw6fDo28gYW1vc3RyYWwgJFxcaGF0e3B9JC4gU2UgbyBhbmFsaXN0YSBkZWNpZGlyIHF1YWRydXBsaWNhciBvIHRhbWFuaG8gZGEgYW1vc3RyYSBwYXJhICRuPTQwMCQsIG8gcXVlIG9jb3JyZXLDoSBjb20gbyBlcnJvIHBhZHLDo28gZGEgcHJvcG9yw6fDo28gJEVQKFxcaGF0e3B9KSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIGVycm8gcGFkcsOjbyBzZXLDoSByZWR1emlkbyDDoCBtZXRhZGUgZG8gdmFsb3Igb3JpZ2luYWwuIiwgIkIiOiAiTyBlcnJvIHBhZHLDo28gcGVybWFuZWNlcsOhIGluYWx0ZXJhZG8sIHBvaXMgYSBwcm9wb3LDp8OjbyBwb3B1bGFjaW9uYWwgJHAkIMOpIGNvbnN0YW50ZS4iLCAiQyI6ICJPIGVycm8gcGFkcsOjbyBzZXLDoSByZWR1emlkbyBhIHVtIHF1YXJ0byBkbyB2YWxvciBvcmlnaW5hbC4iLCAiRCI6ICJPIGVycm8gcGFkcsOjbyBhdW1lbnRhcsOhLCBwb2lzIGEgdmFyaWFiaWxpZGFkZSBhdW1lbnRhIGNvbSBhbW9zdHJhcyBtYWlvcmVzLiIsICJFIjogIk8gZXJybyBwYWRyw6NvIHNlcsOhIHJlZHV6aWRvIHBhcmEgdW0gdmFsb3IgbWVub3IgcXVlIGEgbWV0YWRlLCBkZXBlbmRlbmRvIGFwZW5hcyBkYSB2YXJpw6JuY2lhLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGbDs3JtdWxhIGRvIGVycm8gcGFkcsOjbyBkYSBwcm9wb3LDp8OjbzogJEVQKFxcaGF0e3B9KSA9IFxcc3FydHtcXGZyYWN7cCgxLXApfXtufX0kLiBPYnNlcnZlIGNvbW8gbyB0ZXJtbyAkbiQgYXBhcmVjZSBkZW50cm8gZGEgcmFpeiBxdWFkcmFkYS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIk8gZXJybyBwYWRyw6NvIMOpIGRhZG8gcG9yICRFUChcXGhhdHtwfSkgPSBcXHNxcnR7XFxmcmFje3AoMS1wKX17bn19JC4gUXVhbmRvICRuJCBhdW1lbnRhIGRlIDEwMCBwYXJhIDQwMCwgdGVtb3M6ICRFUF97bm92b30gPSBcXHNxcnR7XFxmcmFje3AoMS1wKX17NDAwfX0gPSBcXHNxcnR7XFxmcmFjezF9ezR9IFxcY2RvdCBcXGZyYWN7cCgxLXApfXsxMDB9fSA9IFxcZnJhY3sxfXsyfSBcXHNxcnR7XFxmcmFje3AoMS1wKX17MTAwfX0gPSBcXGZyYWN7MX17Mn0gRVBfe29yaWdpbmFsfSQuIFBvcnRhbnRvLCBvIGVycm8gcGFkcsOjbyDDqSByZWR1emlkbyDDoCBtZXRhZGUuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKCk7IG5fdmFscyA9IG5wLmFycmF5KFsxMDAsIDQwMF0pOyBwID0gMC4wNDsgZXAgPSBucC5cXHNxcnQocCooMS1wKS9uX3ZhbHMpOyBmaWcuYWRkX3RyYWNlKGdvLkJhcih4PVsnbj0xMDAnLCAnbj00MDAnXSwgeT1lcCwgbWFya2VyX2NvbG9yPScjMUUzQThBJykpOyBmaWcudXBkYXRlX2xheW91dCh0aXRsZT0nRWZlaXRvIGRvIFRhbWFuaG8gQW1vc3RyYWwgbm8gRXJybyBQYWRyw6NvJywgeGF4aXNfdGl0bGU9J1RhbWFuaG8gQW1vc3RyYWwgKCRuJCknLCB5YXhpc190aXRsZT0nRXJybyBQYWRyw6NvICgkRVAoXFxoYXR7cH0pJCknKTsiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgcXVlIHVtYSBlbXByZXNhIGRlIHRlY25vbG9naWEgZGVzZWphIGVzdGltYXIgYSBwcm9wb3LDp8OjbyAkcCQgZGUgdXN1w6FyaW9zIHF1ZSBwcmVmZXJlbSB1bSBub3ZvIGRlc2lnbiBkZSBpbnRlcmZhY2UuIEEgYW1vc3RyYSBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gYmlub21pYWwgJFggXFxzaW0gQmluKG4sIHApJCwgb25kZSAkWCQgw6kgbyBuw7ptZXJvIGRlIHN1Y2Vzc29zLiBTb2JyZSBhIHByb3ByaWVkYWRlIGRvIGVzdGltYWRvciAkXFxoYXR7cH0gPSBYL24kLCBhc3NpbmFsZSBhIGFsdGVybmF0aXZhIGNvcnJldGEuIiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIHZhbG9yIGVzcGVyYWRvIGRvIGVzdGltYWRvciDDqSAkRShcXGhhdHtwfSkgPSBwL24kLiIsICJCIjogIk8gZXN0aW1hZG9yICRcXGhhdHtwfSQgw6kgdmllc2FkbywgcG9pcyBzZXUgdmFsb3IgZXNwZXJhZG8gZGVwZW5kZSBkYSB2YXJpw6JuY2lhIGFtb3N0cmFsLiIsICJDIjogIk8gZXN0aW1hZG9yIMOpIG7Do28tdmllc2FkbywgcG9pcyAkRShcXGhhdHtwfSkgPSBwJC4iLCAiRCI6ICJPIHZhbG9yIGVzcGVyYWRvIGRlICRcXGhhdHtwfSQgYXVtZW50YSBjb25mb3JtZSBvIHRhbWFuaG8gYW1vc3RyYWwgJG4kIGF1bWVudGEuIiwgIkUiOiAiQSB2YXJpw6JuY2lhIGRvIGVzdGltYWRvciAkXFxoYXR7cH0kIGluZGVwZW5kZSBkYSBwcm9wb3LDp8OjbyBwb3B1bGFjaW9uYWwgJHAkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiTyB2YWxvciBlc3BlcmFkbyBkZSB1bWEgdmFyacOhdmVsIGJpbm9taWFsICRYJCDDqSAkRShYKSA9IG4gXFxjZG90IHAkLiBVc2UgYSBwcm9wcmllZGFkZSBkYSBsaW5lYXJpZGFkZSBkYSBlc3BlcmFuw6dhOiAkRShYL24pID0gXFxmcmFjezF9e259IEUoWCkkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiU2FiZW5kbyBxdWUgJFggXFxzaW0gQmluKG4sIHApJCwgdGVtb3MgcXVlICRFKFgpID0gbiBcXGNkb3QgcCQuIFBhcmEgbyBlc3RpbWFkb3IgZGEgcHJvcG9yw6fDo28gJFxcaGF0e3B9ID0gWC9uJCwgY2FsY3VsYW1vcyBvIHZhbG9yIGVzcGVyYWRvIGNvbW8gJEUoXFxoYXR7cH0pID0gRShYL24pID0gXFxmcmFjezF9e259IEUoWCkgPSBcXGZyYWN7MX17bn0gKG4gXFxjZG90IHApID0gcCQuIENvbW8gJEUoXFxoYXR7cH0pID0gcCQsIGRpemVtb3MgcXVlIG8gZXN0aW1hZG9yIMOpIG7Do28tdmllc2Fkby4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIHByb2Nlc3NvIGRlIGF1ZGl0b3JpYSBpbnRlcm5hLCB1bWEgZW1wcmVzYSBkZXNlamEgZXN0aW1hciBhIG3DqWRpYSBkZSBnYXN0b3MgZGnDoXJpb3MgZGUgc2V1cyAkTiA9IDIwMDAkIGRlcGFydGFtZW50b3MuIE8gZ2VzdG9yIGRlY2lkZSBjb2xldGFyIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgc2ltcGxlcyBzZW0gcmVwb3Npw6fDo28uIENvbnNpZGVyYW5kbyBvIEZhdG9yIGRlIENvcnJlw6fDo28gcGFyYSBQb3B1bGHDp8O1ZXMgRmluaXRhcyAoRkNQRiksIGFuYWxpc2UgbyBjb21wb3J0YW1lbnRvIGRhIHZhcmnDom5jaWEgZGEgbcOpZGlhIGFtb3N0cmFsICRWYXIoXGJhcntYfSkkIMOgIG1lZGlkYSBxdWUgbyB0YW1hbmhvIGRhIGFtb3N0cmEgJG4kIGF1bWVudGEgZW0gZGlyZcOnw6NvIGEgJE4kLiBRdWFsIGRhcyBhbHRlcm5hdGl2YXMgZGVzY3JldmUgY29ycmV0YW1lbnRlIG8gZmVuw7RtZW5vIGVzdGF0w61zdGljbyBvYnNlcnZhZG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIHZhcmnDom5jaWEgZGEgbcOpZGlhIGFtb3N0cmFsICRWYXIoXGJhcntYfSkkIGF1bWVudGEgY29uZm9ybWUgJG4kIHNlIGFwcm94aW1hIGRlICROJCwgcG9pcyBhIGluY2VydGV6YSBzb2JyZSBhIHBvcHVsYcOnw6NvIHRvdGFsIGNyZXNjZS4iLCAiQiI6ICJPIGZhdG9yIGRlIGNvcnJlw6fDo28gJChOLW4pLyhOLTEpJCBhcHJveGltYS1zZSBkZSB6ZXJvIHF1YW5kbyAkbiBcdG8gTiQsIGluZGljYW5kbyBxdWUgYSB2YXJpw6JuY2lhIGRvIGVzdGltYWRvciAkXGJhcntYfSQgcmVkdXotc2Ugc2lnbmlmaWNhdGl2YW1lbnRlLCBhdGluZ2luZG8gdmFsb3IgemVybyBxdWFuZG8gJG49TiQuIiwgIkMiOiAiTyBGQ1BGIHBlcm1hbmVjZSBjb25zdGFudGUgZSBpZ3VhbCBhIDEsIGluZGVwZW5kZW50ZW1lbnRlIGRvIHRhbWFuaG8gZGEgYW1vc3RyYSAkbiQsIG7Do28gYWx0ZXJhbmRvIGEgcHJlY2lzw6NvIGRvIGVzdGltYWRvci4iLCAiRCI6ICJBIHZhcmnDom5jaWEgZGEgbcOpZGlhIGFtb3N0cmFsIMOpIGNvbnN0YW50ZSwgaW5kZXBlbmRlbnRlbWVudGUgZG8gdmFsb3IgZGUgJG4kLCB1bWEgdmV6IHF1ZSBhIHZhcmnDom5jaWEgcG9wdWxhY2lvbmFsICRcXHNpZ21hXjIkIMOpIGZpeGEuIiwgIkUiOiAiTyBmYXRvciBkZSBjb3JyZcOnw6NvIG7Do28gw6kgYXBsaWPDoXZlbCBlbSBwb3B1bGHDp8O1ZXMgZmluaXRhcyBxdWFuZG8gJG4kIMOpIG1lbm9yIHF1ZSA1JSBkZSAkTiQsIHNlbmRvIHN1YSBhcGxpY2HDp8OjbyByZXN0cml0YSBhcGVuYXMgYSBhbW9zdHJhZ2VucyBjZW5zaXTDoXJpYXMuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJBbmFsaXNlIG8gY29tcG9ydGFtZW50byBkbyB0ZXJtbyAkXFxmcmFje04tbn17Ti0xfSQgbm9zIGxpbWl0ZXMgcXVhbmRvICRuJCDDqSBwZXF1ZW5vIGUgcXVhbmRvICRuJCBzZSB0b3JuYSBpZ3VhbCBhICROJC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgZsOzcm11bGEgZGEgdmFyacOibmNpYSBkYSBtw6lkaWEgYW1vc3RyYWwgcGFyYSBwb3B1bGHDp8O1ZXMgZmluaXRhcyDDqSBkYWRhIHBvciAkVmFyKFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWFeMn17bn0gXFxsZWZ0KCBcXGZyYWN7TiAtIG59e04gLSAxfSBcXHJpZ2h0KSQuIMOAIG1lZGlkYSBxdWUgbyB0YW1hbmhvIGRhIGFtb3N0cmEgJG4kIGF1bWVudGEsIG8gbnVtZXJhZG9yIGRvIEZDUEYgJChOLW4pJCBkaW1pbnVpLiBRdWFuZG8gJG49TiQsIG8gZmF0b3IgJChOLU4pLyhOLTEpID0gMCQsIG8gcXVlIGltcGxpY2EgJFZhcihcYmFye1h9KSA9IDAkLiBJc3NvIGZheiBzZW50aWRvIGludHVpdGl2bzogc2UgYW1vc3RyYW1vcyB0b2RvcyBvcyBlbGVtZW50b3MgZGEgcG9wdWxhw6fDo28gKCRuPU4kKSwgbsOjbyBow6EgaW5jZXJ0ZXphIHNvYnJlIGEgbcOpZGlhLCBwb2lzIGEgbcOpZGlhIGFtb3N0cmFsIHRvcm5hLXNlIGEgbcOpZGlhIHBvcHVsYWNpb25hbCBleGF0YS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEwLCBwLiAyNzgifSwgeyJlbnVuY2lhZG8iOiAiVW0gaG9zcGl0YWwgcmVnaXN0cmEgbyB0ZW1wbyBkZSBlc3BlcmEgZGUgJE49NTAwJCBwYWNpZW50ZXMgZW0gdW1hIGFsYSBlc3BlY8OtZmljYS4gQSB2YXJpw6JuY2lhIHBvcHVsYWNpb25hbCBvYnNlcnZhZGEgw6kgJFxcc2lnbWFeMiA9IDI1JCBtaW51dG9zJF4yJC4gU2UgdW0gcGVzcXVpc2Fkb3IgZXh0cmFpIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgc2ltcGxlcyBzZW0gcmVwb3Npw6fDo28gZGUgJG49MTAwJCBwYWNpZW50ZXMsIHF1YWwgw6kgbyB2YWxvciBhcHJveGltYWRvIGRhIHZhcmnDom5jaWEgZGEgbcOpZGlhIGFtb3N0cmFsICRWYXIoXFxiYXJ7WH0pJD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjAsMjUwMCIsICJCIjogIjAsMjAwNCIsICJDIjogIjAsMDUwMCIsICJEIjogIjAsMjUwNSIsICJFIjogIjAsMTUwMCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRlIGFwbGljYXIgbyBGYXRvciBkZSBDb3JyZcOnw6NvIHBhcmEgUG9wdWxhw6fDtWVzIEZpbml0YXM6ICRWYXIoXFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWFeMn17bn0gXFxsZWZ0KCBcXGZyYWN7TiAtIG59e04gLSAxfSBcXHJpZ2h0KSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBcGxpY2FuZG8gb3MgdmFsb3JlcyBmb3JuZWNpZG9zIG5hIGbDs3JtdWxhOiAkVmFyKFxcYmFye1h9KSA9IFxcZnJhY3syNX17MTAwfSBcXGNkb3QgXFxmcmFjezUwMCAtIDEwMH17NTAwIC0gMX0gPSAwLDI1IFxcY2RvdCBcXGZyYWN7NDAwfXs0OTl9JC4gQ2FsY3VsYW5kbyBhIGZyYcOnw6NvLCB0ZW1vcyAkNDAwLzQ5OSBcXGFwcHJveCAwLDgwMTYkLiBNdWx0aXBsaWNhbmRvIHBvciAwLDI1LCBvYnRlbW9zICQwLDI1IFxcY2RvdCAwLDgwMTYgPSAwLDIwMDQkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTAsIHAuIDI3OCJ9XSwgInF1ZXN0b2VzX2Rpc2N1cnNpdmFzIjogW3siZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bWEgcG9wdWxhw6fDo28gcGVxdWVuYSAkUCA9IFxcezIsIDQsIDYsIDhcXH0kLiBEZXRlcm1pbmUgYSBtw6lkaWEgcG9wdWxhY2lvbmFsICRcXG11JCBlIGEgdmFyacOibmNpYSBwb3B1bGFjaW9uYWwgJFxcc2lnbWFeMiQuIEVtIHNlZ3VpZGEsIHN1cG9uaGEgcXVlIHNlbGVjaW9uYW1vcyB0b2RhcyBhcyBhbW9zdHJhcyBwb3Nzw612ZWlzIGRlIHRhbWFuaG8gJG4gPSAyJCBjb20gcmVwb3Npw6fDo28uIENvbnN0cnVhIGEgZGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgZGEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSQgZSBjYWxjdWxlICRFKFxcYmFye1h9KSQgZSAkVmFyKFxcYmFye1h9KSQuIFZlcmlmaXF1ZSBzZSAkRShcXGJhcntYfSkgPSBcXG11JCBlIHNlICRWYXIoXFxiYXJ7WH0pID0gXFxzaWdtYV4yIC8gbiQuIiwgImRpY2EiOiAiQ2FsY3VsZSBhIG3DqWRpYSBhcml0bcOpdGljYSBwYXJhIGNhZGEgdW1hIGRhcyAxNiBwb3Nzw612ZWlzIGFtb3N0cmFzICg0eDQpIGUgdXNlIGFzIGbDs3JtdWxhcyAkRShcXGJhcntYfSkgPSBcXHN1bSBcXGJhcnt4fV9pIFAoXFxiYXJ7WH0gPSBcXGJhcnt4fV9pKSQgZSAkVmFyKFxcYmFye1h9KSA9IFxcc3VtIChcXGJhcnt4fV9pIC0gXFxtdSleMiBQKFxcYmFye1h9ID0gXFxiYXJ7eH1faSkkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiAkXFxtdSA9ICgyKzQrNis4KS80ID0gNSQgZSAkXFxzaWdtYV4yID0gWygyLTUpXjIgKyAoNC01KV4yICsgKDYtNSleMiArICg4LTUpXjJdLzQgPSAoOSsxKzErOSkvNCA9IDUkLiIsICJQYXNzbyAyOiBBcyBtw6lkaWFzIGRhcyAxNiBhbW9zdHJhcyBwb3Nzw612ZWlzICQoWF8xLCBYXzIpJCBzw6NvOiAyLCAzLCA0LCA1LCAzLCA0LCA1LCA2LCA0LCA1LCA2LCA3LCA1LCA2LCA3LCA4LiIsICJQYXNzbyAzOiBBIGRpc3RyaWJ1acOnw6NvIGRlICRcXGJhcntYfSQgw6k6ICRQKDIpPTEvMTYsIFAoMyk9Mi8xNiwgUCg0KT0zLzE2LCBQKDUpPTQvMTYsIFAoNik9My8xNiwgUCg3KT0yLzE2LCBQKDgpPTEvMTYkLiIsICJQYXNzbyA0OiAkRShcXGJhcntYfSkgPSAoMlxcY2RvdCAxICsgM1xcY2RvdCAyICsgNFxcY2RvdCAzICsgNVxcY2RvdCA0ICsgNlxcY2RvdCAzICsgN1xcY2RvdCAyICsgOFxcY2RvdCAxKS8xNiA9IDgwLzE2ID0gNSQuIiwgIlBhc3NvIDU6ICRWYXIoXFxiYXJ7WH0pID0gXFxzdW0gKFxcYmFye3h9X2kgLSA1KV4yIFAoXFxiYXJ7WH0gPSBcXGJhcnt4fV9pKSA9IFsoLTMpXjJcXGNkb3QgMSArICgtMileMlxcY2RvdCAyICsgKC0xKV4yXFxjZG90IDMgKyAwXFxjZG90IDQgKyAxXjJcXGNkb3QgMyArIDJeMlxcY2RvdCAyICsgM14yXFxjZG90IDFdLzE2ID0gKDkrOCszKzArMys4KzkpLzE2ID0gNDAvMTYgPSAyLjUkLiIsICJQYXNzbyA2OiBDb25jbHVzw6NvOiAkRShcXGJhcntYfSkgPSA1ID0gXFxtdSQgZSAkVmFyKFxcYmFye1h9KSA9IDIuNSA9IDUvMiA9IFxcc2lnbWFeMi9uJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMCwgcC4gMjc4IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMi41fSwgeyJlbnVuY2lhZG8iOiAiVW0gcHJvY2Vzc28gZGUgbWFudWZhdHVyYSBkZSBjb21wb25lbnRlcyBlbGV0csO0bmljb3MgcHJvZHV6IGl0ZW5zIGNvbSB1bWEgcmVzaXN0w6puY2lhIHF1ZSBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIGNvbSBtw6lkaWEgJFxcbXUgPSA1MDAkIE9obXMgZSBkZXN2aW8gcGFkcsOjbyAkXFxzaWdtYSA9IDIwJCBPaG1zLiBTZSByZXRpcmFybW9zIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgc2ltcGxlcyBkZSAkbiA9IDI1JCBjb21wb25lbnRlcywgcXVhbCDDqSBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEsICRFUChcXGJhcntYfSkkLCBlIHF1YWwgYSBwcm9iYWJpbGlkYWRlIGRlIGEgbcOpZGlhIGFtb3N0cmFsIHNlciBpbmZlcmlvciBhIDQ5NiBPaG1zPyIsICJkaWNhIjogIk8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSDDqSAkRVAoXFxiYXJ7WH0pID0gXFxzaWdtYSAvIFxcc3FydHtufSQuIFV0aWxpemUgYSBwYWRyb25pemHDp8OjbyAkWiA9IChcXGJhcntYfSAtIFxcbXUpIC8gRVAoXFxiYXJ7WH0pJCBwYXJhIGNhbGN1bGFyIGEgcHJvYmFiaWxpZGFkZS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogQ2FsY3VsYXIgbyBlcnJvIHBhZHLDo286ICRFUChcXGJhcntYfSkgPSAyMCAvIFxcc3FydHsyNX0gPSAyMCAvIDUgPSA0JC4iLCAiUGFzc28gMjogUGFkcm9uaXphciBvIHZhbG9yIGRhIG3DqWRpYSBhbW9zdHJhbDogJFogPSAoNDk2IC0gNTAwKSAvIDQgPSAtNCAvIDQgPSAtMSQuIiwgIlBhc3NvIDM6IEEgcHJvYmFiaWxpZGFkZSAkUChcXGJhcntYfSA8IDQ5NikkIMOpIGVxdWl2YWxlbnRlIGEgJFAoWiA8IC0xKSQuIiwgIlBhc3NvIDQ6IENvbnN1bHRhbmRvIGEgdGFiZWxhIG5vcm1hbCBwYWRyw6NvLCAkUChaIDwgLTEpIFxcYXBwcm94IDAuMTU4NyQuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTQsIDQsIDEwMClcbnkgPSAoMS9ucC5cXHNxcnQoMipucC5cXHBpKSkgKiBucC5cXGV4cCgtMC41ICogeCoqMilcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJywgd2lkdGg9MikpKVxuZmlnLmFkZF92cmVjdCh4MD0tNCwgeDE9LTEsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTApXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+RGlzdHJpYnVpw6fDo28gTm9ybWFsIGRlICRaJCBlIFJlZ2nDo28gZGUgUHJvYmFiaWxpZGFkZTwvYj4nLCB4YXhpc190aXRsZT0nRXN0YXTDrXN0aWNhICRaJCcsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4xNTg3fSwgeyJlbnVuY2lhZG8iOiAiU3Vwb25oYSBxdWUgdW1hIHBvcHVsYcOnw6NvIGRlIGZ1bmNpb27DoXJpb3MgZGUgdW1hIGVtcHJlc2EgYXByZXNlbnRlIHNhbMOhcmlvcyBjb20gbcOpZGlhICRcXG11ID0gMzAwMCQgZSBkZXN2aW8gcGFkcsOjbyAkXFxzaWdtYSA9IDEwMDAkLiBPIGRlcGFydGFtZW50byBkZSBSSCBwbGFuZWphIGNvbGV0YXIgdW1hIGFtb3N0cmEgZGUgdGFtYW5obyAkbiQgcGFyYSBlc3RpbWFyIGEgbcOpZGlhIHNhbGFyaWFsLiBTZSBvIG9iamV0aXZvIMOpIHF1ZSBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgc2VqYSwgbm8gbcOheGltbywgNTAsIHF1YWwgZGV2ZSBzZXIgbyB0YW1hbmhvIGRhIGFtb3N0cmEgJG4kIG5lY2Vzc8OhcmlvPyIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSBkbyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhOiAkRVAoXFxiYXJ7WH0pID0gXFxzaWdtYSAvIFxcc3FydHtufSQgZSByZXNvbHZhIHBhcmEgJG4kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiBFc3RhYmVsZWNlciBhIGRlc2lndWFsZGFkZTogJFxcc2lnbWEgLyBcXHNxcnR7bn0gXFxsZSA1MCQuIiwgIlBhc3NvIDI6IFN1YnN0aXR1aXIgb3MgdmFsb3JlcyBjb25oZWNpZG9zOiAkMTAwMCAvIFxcc3FydHtufSBcXGxlIDUwJC4iLCAiUGFzc28gMzogSXNvbGFyICRcXHNxcnR7bn0kOiAkXFxzcXJ0e259IFxcZ2UgMTAwMCAvIDUwJC4iLCAiUGFzc28gNDogQ2FsY3VsYXIgbyB2YWxvcjogJFxcc3FydHtufSBcXGdlIDIwJC4iLCAiUGFzc28gNTogRWxldmFyIGFvIHF1YWRyYWRvIHBhcmEgb2J0ZXIgJG4kOiAkbiBcXGdlIDQwMCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiA0MDAuMH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bWEgcG9wdWxhw6fDo28gY29tIG3DqWRpYSAkXFxtdSQgZSB2YXJpw6JuY2lhICRcXHNpZ21hXjIkLiBTZWphICRcXGJhcntYfSA9IFxcZnJhY3sxfXtufSBcXHN1bV97aT0xfV57bn0gWF9pJCBhIG3DqWRpYSBkZSB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIHNpbXBsZXMuIERlbW9uc3RyZSwgdXRpbGl6YW5kbyBhcyBwcm9wcmllZGFkZXMgZGEgZXNwZXJhbsOnYSwgcXVlICRcXGJhcntYfSQgw6kgdW0gZXN0aW1hZG9yIG7Do28tdmllc2FkbyBkZSAkXFxtdSQsIG91IHNlamEsICRFKFxcYmFye1h9KSA9IFxcbXUkLiIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBsaW5lYXJpZGFkZSBkYSBlc3BlcmFuw6dhOiAkRShhWCArIGJZKSA9IGFFKFgpICsgYkUoWSkkLCBlIHF1ZSBlbSB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIHNpbXBsZXMsIHRvZG9zIG9zICRYX2kkIHTDqm0gYSBtZXNtYSBlc3BlcmFuw6dhICRcXG11JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRGVmaW5pbW9zIG8gdmFsb3IgZXNwZXJhZG8gZGEgbcOpZGlhIGFtb3N0cmFsOiAkRShcXGJhcntYfSkgPSBFXFxsZWZ0KCBcXGZyYWN7MX17bn0gXFxzdW1fe2k9MX1ee259IFhfaSBcXHJpZ2h0KSQuIiwgIlBlbGEgcHJvcHJpZWRhZGUgZGEgbGluZWFyaWRhZGUgZG8gdmFsb3IgZXNwZXJhZG8sIHJldGlyYW1vcyBhIGNvbnN0YW50ZSAkMS9uJDogJEUoXFxiYXJ7WH0pID0gXFxmcmFjezF9e259IEVcXGxlZnQoIFxcc3VtX3tpPTF9XntufSBYX2kgXFxyaWdodCkkLiIsICJBcGxpY2Ftb3MgYSBwcm9wcmllZGFkZSBkYSBzb21hdMOzcmlhOiAkRShcXGJhcntYfSkgPSBcXGZyYWN7MX17bn0gXFxzdW1fe2k9MX1ee259IEUoWF9pKSQuIiwgIkNvbW8gY2FkYSAkWF9pJCBwcm92w6ltIGRhIG1lc21hIHBvcHVsYcOnw6NvLCAkRShYX2kpID0gXFxtdSQgcGFyYSB0b2RvICRpJDogJEUoXFxiYXJ7WH0pID0gXFxmcmFjezF9e259IFxcc3VtX3tpPTF9XntufSBcXG11JC4iLCAiTyBzb21hdMOzcmlvIGRlIHVtYSBjb25zdGFudGUgJFxcbXUkIHBvciAkbiQgdmV6ZXMgw6kgJG5cXG11JDogJEUoXFxiYXJ7WH0pID0gXFxmcmFjezF9e259IChuXFxtdSkgPSBcXG11JC4iLCAiQ29uY2x1w61tb3MsIHBvcnRhbnRvLCBxdWUgJEUoXFxiYXJ7WH0pID0gXFxtdSQsIG8gcXVlIGNhcmFjdGVyaXphIG8gZXN0aW1hZG9yIGNvbW8gbsOjby12aWVzYWRvLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEwLCBwLiAyNzgiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQWluZGEgY29uc2lkZXJhbmRvIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgc2ltcGxlcyBkZSB0YW1hbmhvICRuJCByZXRpcmFkYSBkZSB1bWEgcG9wdWxhw6fDo28gY29tIHZhcmnDom5jaWEgJFxcc2lnbWFeMiQsIGRlbW9uc3RyZSBxdWUgYSB2YXJpw6JuY2lhIGRhIG3DqWRpYSBhbW9zdHJhbCDDqSAkVmFyKFxcYmFye1h9KSA9IFxcZnJhY3tcXHNpZ21hXjJ9e259JC4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlICRWYXIoYVgpID0gYV4yIFZhcihYKSQgZSBxdWUsIHBhcmEgdmFyacOhdmVpcyBhbGVhdMOzcmlhcyBpbmRlcGVuZGVudGVzLCAkVmFyKFxcc3VtIFhfaSkgPSBcXHN1bSBWYXIoWF9pKSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkRlZmluaW1vcyBhIHZhcmnDom5jaWEgZGEgbcOpZGlhIGFtb3N0cmFsOiAkVmFyKFxcYmFye1h9KSA9IFZhclxcbGVmdCggXFxmcmFjezF9e259IFxcc3VtX3tpPTF9XntufSBYX2kgXFxyaWdodCkkLiIsICJVdGlsaXphbW9zIGEgcHJvcHJpZWRhZGUgZGUgcXVlICRWYXIoYVgpID0gYV4yIFZhcihYKSQ6ICRWYXIoXFxiYXJ7WH0pID0gXFxmcmFjezF9e25eMn0gVmFyXFxsZWZ0KCBcXHN1bV97aT0xfV57bn0gWF9pIFxccmlnaHQpJC4iLCAiQ29tbyBvcyBlbGVtZW50b3MgZGEgYW1vc3RyYSBhbGVhdMOzcmlhIHNpbXBsZXMgc8OjbyBpbmRlcGVuZGVudGVzLCBhIHZhcmnDom5jaWEgZGEgc29tYSDDqSBhIHNvbWEgZGFzIHZhcmnDom5jaWFzOiAkVmFyKFxcYmFye1h9KSA9IFxcZnJhY3sxfXtuXjJ9IFxcc3VtX3tpPTF9XntufSBWYXIoWF9pKSQuIiwgIlNhYmVtb3MgcXVlICRWYXIoWF9pKSA9IFxcc2lnbWFeMiQgcGFyYSB0b2RvICRpJDogJFZhcihcXGJhcntYfSkgPSBcXGZyYWN7MX17bl4yfSBcXHN1bV97aT0xfV57bn0gXFxzaWdtYV4yJC4iLCAiTyBzb21hdMOzcmlvIGRlICRcXHNpZ21hXjIkIHBvciAkbiQgdmV6ZXMgcmVzdWx0YSBlbSAkblxcc2lnbWFeMiQ6ICRWYXIoXFxiYXJ7WH0pID0gXFxmcmFjezF9e25eMn0gKG5cXHNpZ21hXjIpJC4iLCAiU2ltcGxpZmljYW5kbyBvcyB0ZXJtb3M6ICRWYXIoXFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWFeMn17bn0kLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEwLCBwLiAyNzgiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gcHJvY2Vzc28gaW5kdXN0cmlhbCwgbyBkacOibWV0cm8gZGUgcGXDp2FzIG1ldMOhbGljYXMgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIGNvbSBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgJFxcc2lnbWEgPSAwLDIgXFx0ZXh0eyBtbX0kLiBEZXNlamEtc2UgZXN0aW1hciBhIG3DqWRpYSBwb3B1bGFjaW9uYWwgZG9zIGRpw6JtZXRyb3MuIFNlIGEgdmFyacOibmNpYSBkbyBlc3RpbWFkb3IgJFxcYmFye1h9JCBkZXZlIHNlciBubyBtw6F4aW1vICQwLDAwMSBcXHRleHR7IG1tfV4yJCwgcXVhbCDDqSBvIHRhbWFuaG8gbcOtbmltbyBkZSBhbW9zdHJhICRuJCBuZWNlc3PDoXJpbyBwYXJhIGdhcmFudGlyIGVzc2EgcHJlY2lzw6NvPyIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSBkYSB2YXJpw6JuY2lhIGRhIG3DqWRpYSBhbW9zdHJhbDogJFZhcihcXGJhcntYfSkgPSBcXGZyYWN7XFxzaWdtYV4yfXtufSQgZSBpc29sZSAkbiQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgZsOzcm11bGEgcGFyYSBhIHZhcmnDom5jaWEgZG8gZXN0aW1hZG9yIMOpICRWYXIoXFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWFeMn17bn0kLiIsICJUZW1vcyBvcyB2YWxvcmVzOiAkXFxzaWdtYSA9IDAsMiQsIHBvcnRhbnRvICRcXHNpZ21hXjIgPSAwLDA0JC4gTyBsaW1pdGUgZGVzZWphZG8gw6kgJFZhcihcXGJhcntYfSkgXFxsZSAwLDAwMSQuIiwgIlN1YnN0aXR1w61tb3MgbmEgZsOzcm11bGE6ICQwLDAwMSA9IFxcZnJhY3swLDA0fXtufSQuIiwgIklzb2xhbW9zICRuJDogJG4gPSBcXGZyYWN7MCwwNH17MCwwMDF9JC4iLCAiQ2FsY3VsYW1vcyBvIHZhbG9yIGZpbmFsOiAkbiA9IDQwJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDQwLjB9LCB7ImVudW5jaWFkbyI6ICJVbWEgZW1wcmVzYSBkZSBcXGxvZ8Otc3RpY2EgbW9uaXRvcmEgbyBwZXNvIGRlIHBhY290ZXMgZW52aWFkb3MuIFNhYmUtc2UgcXVlIG8gcGVzbyBkZSB1bSBwYWNvdGUgaW5kaXZpZHVhbCB0ZW0gZGlzdHJpYnVpw6fDo28gZGVzY29uaGVjaWRhIGNvbSBtw6lkaWEgJFxcbXUgPSA1MCQga2cgZSB2YXJpw6JuY2lhICRcXHNpZ21hXjIgPSAxMDAkIGtnwrIuIFNlIHVtYSBhbW9zdHJhIGRlIDEwMCBwYWNvdGVzIMOpIHNlbGVjaW9uYWRhIGFsZWF0b3JpYW1lbnRlLCBxdWFsIGEgcHJvYmFiaWxpZGFkZSBkZSBxdWUgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBlc3RlamEgZW50cmUgNDgsNSBrZyBlIDUxLDUga2c/IiwgImRpY2EiOiAiVXNlIG8gVExDIHBhcmEganVzdGlmaWNhciBxdWUgJFxcYmFye1h9IFxcYXBwcm94IE4oNTAsIDEwMC8xMDApJC4gQ2FsY3VsZSBvIGVycm8gcGFkcsOjbyBlIHBhZHJvbml6ZSBvcyBsaW1pdGVzLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJJZGVudGlmaWNhbW9zIG9zIHBhcsOibWV0cm9zOiAkXFxtdSA9IDUwJCwgJFxcc2lnbWFeMiA9IDEwMCQsIGxvZ28gJFxcc2lnbWEgPSAxMCQsIGUgJG4gPSAxMDAkLiIsICJDYWxjdWxhbW9zIG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYTogJEVQKFxcYmFye1h9KSA9IFxcZnJhY3tcXHNpZ21hfXtcXHNxcnR7bn19ID0gXFxmcmFjezEwfXtcXHNxcnR7MTAwfX0gPSBcXGZyYWN7MTB9ezEwfSA9IDEkLiIsICJBcGxpY2Ftb3MgbyBUTEM6ICRcXGJhcntYfSBcXGFwcHJveCBOKDUwLCAxXjIpJC4iLCAiUGFkcm9uaXphbW9zIG9zIGxpbWl0ZXM6ICRaXzEgPSBcXGZyYWN7NDguNSAtIDUwfXsxfSA9IC0xLjUkIGUgJFpfMiA9IFxcZnJhY3s1MS41IC0gNTB9ezF9ID0gMS41JC4iLCAiQ2FsY3VsYW1vcyBhIHByb2JhYmlsaWRhZGU6ICRQKC0xLjUgPCBaIDwgMS41KSA9IFxcUGhpKDEuNSkgLSBcXFBoaSgtMS41KSA9IDAuOTMzMiAtIDAuMDY2OCA9IDAuODY2NCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjg2NjR9LCB7ImVudW5jaWFkbyI6ICJVbSBmYWJyaWNhbnRlIGRlIGNpbGluZHJvcyBpbmR1c3RyaWFpcyBhZmlybWEgcXVlIG8gZGnDom1ldHJvIG3DqWRpbyBkZSBzdWEgcHJvZHXDp8OjbyDDqSBkZSA1MCBtbSwgY29tIHVtIGRlc3ZpbyBwYWRyw6NvIGRlIDIsNSBtbS4gUGFyYSB2ZXJpZmljYXIgbyBwcm9jZXNzbywgcmV0aXJhLXNlIHVtYSBhbW9zdHJhIGRlICRuID0gMjUkIGNpbGluZHJvcyBhIGNhZGEgaG9yYS4gU2UgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBmb3IgbWVub3IgcXVlIDQ5IG1tIG91IG1haW9yIHF1ZSA1MSBtbSwgbyBwcm9jZXNzbyDDqSBjb25zaWRlcmFkbyBkZXNyZWd1bGFkby4gUXVhbCBhIHByb2JhYmlsaWRhZGUgZGUgdW0gZmFsc28gYWxhcm1lIChwYXJhciBvIHByb2Nlc3NvIHF1YW5kbyBlbGUgZXN0w6EsIG5hIHZlcmRhZGUsIHJlZ3VsYWRvKT8iLCAiZGljYSI6ICJPIGVycm8gcGFkcsOjbyDDqSAkXFxzaWdtYS9cXHNxcnR7bn0kLiBPIGZhbHNvIGFsYXJtZSBvY29ycmUgcXVhbmRvIGEgbcOpZGlhIGRhIGFtb3N0cmEgY2FpIGZvcmEgZG8gaW50ZXJ2YWxvIGNyw610aWNvIHNvYiBhIGhpcMOzdGVzZSBkZSBxdWUgbyBwcm9jZXNzbyBlc3TDoSBzb2IgY29udHJvbGUgKCRcXG11PTUwJCkuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhcsOibWV0cm9zOiAkXFxtdSA9IDUwJCwgJFxcc2lnbWEgPSAyLjUkLCAkbiA9IDI1JC4iLCAiRXJybyBwYWRyw6NvOiAkRVAoXFxiYXJ7WH0pID0gXFxmcmFjezIuNX17XFxzcXJ0ezI1fX0gPSBcXGZyYWN7Mi41fXs1fSA9IDAuNSQuIiwgIlJlZ3JhIGRlIGRlY2lzw6NvOiBQYXJhciBzZSAkXFxiYXJ7WH0gPCA0OSQgb3UgJFxcYmFye1h9ID4gNTEkLiIsICJQYWRyb25pemFuZG86ICRaX3tcXGluZn0gPSBcXGZyYWN7NDkgLSA1MH17MC41fSA9IC0yJCBlICRaX3tcXHN1cH0gPSBcXGZyYWN7NTEgLSA1MH17MC41fSA9IDIkLiIsICJQcm9iYWJpbGlkYWRlIGRlIGVycm86ICRQKFxcYmFye1h9IDwgNDkpICsgUChcXGJhcntYfSA+IDUxKSA9IFAoWiA8IC0yKSArIFAoWiA+IDIpID0gMC4wMjI4ICsgMC4wMjI4ID0gMC4wNDU2JC4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSg0OCwgNTIsIDIwMClcbnkgPSAoMSAvICgwLjUgKiBucC5cXHNxcnQoMiAqIG5wLlxccGkpKSkgKiBucC5cXGV4cCgtMC41ICogKCh4IC0gNTApIC8gMC41KSAqKiAyKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0zKSkpXG5maWcuYWRkX3ZyZWN0KHgwPTQ4LCB4MT00OSwgZmlsbGNvbG9yPScjOTkxQjFCJywgb3BhY2l0eT0wLjQpXG5maWcuYWRkX3ZyZWN0KHgwPTUxLCB4MT01MiwgZmlsbGNvbG9yPScjOTkxQjFCJywgb3BhY2l0eT0wLjQpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nUHJvYmFiaWxpZGFkZSBkZSBGYWxzbyBBbGFybWUnLCB4YXhpc190aXRsZT0nTcOpZGlhIEFtb3N0cmFsICgkXFxiYXJ7WH0kKScsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEwLCBwLiAyOTEiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjA0NTZ9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gc29icmUgbyBjb25zdW1vIGRlIGVuZXJnaWEgZW0gdW1hIHBsYW50YSBpbmR1c3RyaWFsLCBzYWJlLXNlIHF1ZSBvIGNvbnN1bW8gbWVuc2FsIHBvciBtw6FxdWluYSB0ZW0gdW1hIGRpc3RyaWJ1acOnw6NvIGNvbSBtw6lkaWEgJFxcbXUgPSAyMDAkIGtXaCBlIGRlc3ZpbyBwYWRyw6NvICRcXHNpZ21hID0gNDAkIGtXaC4gU2UgYSBwbGFudGEgb3BlcmEgNjQgbcOhcXVpbmFzLCBxdWFsIGRldmUgc2VyIGEgbWFyZ2VtIGRlIGVycm8gJEUkIHRhbCBxdWUgbyBjb25zdW1vIG3DqWRpbyB0b3RhbCB0ZW5oYSA5NSUgZGUgcHJvYmFiaWxpZGFkZSBkZSBlc3RhciBjb250aWRvIGVtICRcXG11IFxccG0gRSQ/IiwgImRpY2EiOiAiTyBuw612ZWwgZGUgY29uZmlhbsOnYSBkZSA5NSUgbmEgbm9ybWFsIHBhZHLDo28gY29ycmVzcG9uZGUgYSAkWl97Y3JpdH0gXFxhcHByb3ggMS45NiQuIEEgbWFyZ2VtIGRlIGVycm8gw6kgJEUgPSBaX3tjcml0fSBcXHRpbWVzIEVQKFxcYmFye1h9KSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhcsOibWV0cm9zOiAkXFxtdSA9IDIwMCQsICRcXHNpZ21hID0gNDAkLCAkbiA9IDY0JC4iLCAiRXJybyBwYWRyw6NvOiAkRVAoXFxiYXJ7WH0pID0gXFxmcmFjezQwfXtcXHNxcnR7NjR9fSA9IFxcZnJhY3s0MH17OH0gPSA1JC4iLCAiWiBjcsOtdGljbyBwYXJhIDk1JTogJFAoLVogPCBaIDwgWikgPSAwLjk1IFxcaW1wbGllcyBaIFxcYXBwcm94IDEuOTYkLiIsICJNYXJnZW0gZGUgZXJybzogJEUgPSBaIFxcdGltZXMgRVAoXFxiYXJ7WH0pID0gMS45NiBcXHRpbWVzIDUkLiIsICJDw6FsY3VsbzogJEUgPSA5LjgkIGtXaC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDkuOH0sIHsiZW51bmNpYWRvIjogIlVtIGdlc3RvciBkZSBtYXJrZXRpbmcgZGVzZWphIGVzdGltYXIgYSB0YXhhIGRlIGNvbnZlcnPDo28gKCRwJCkgZGUgdW1hIGNhbXBhbmhhIGRpZ2l0YWwuIEVsZSBhc3N1bWUgcXVlICRwID0gMC4xMCQgZSBkZWNpZGUgYW5hbGlzYXIgdW1hIGFtb3N0cmEgYWxlYXTDs3JpYSBkZSAkbj01MDAkIGludGVyYcOnw7Vlcy4gQ2FsY3VsZSBvIHZhbG9yIGVzcGVyYWRvIGUgbyBlcnJvIHBhZHLDo28gZGEgcHJvcG9yw6fDo28gYW1vc3RyYWwgJFxcaGF0e3B9JCBuZXN0YSBjb25maWd1cmHDp8Ojby4iLCAiZGljYSI6ICJVdGlsaXplIGFzIGbDs3JtdWxhcyAkRShcXGhhdHtwfSkgPSBwJCBlICRFUChcXGhhdHtwfSkgPSBcXHNxcnR7XFxmcmFje3AoMS1wKX17bn19JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogSWRlbnRpZmljYXIgb3MgcGFyw6JtZXRyb3MgJG4gPSA1MDAkIGUgJHAgPSAwLjEwJC4iLCAiUGFzc28gMjogQ2FsY3VsYXIgbyB2YWxvciBlc3BlcmFkbzogJEUoXFxoYXR7cH0pID0gcCA9IDAuMTAkLiIsICJQYXNzbyAzOiBDYWxjdWxhciBhIHZhcmnDom5jaWE6ICRWYXIoXFxoYXR7cH0pID0gXFxmcmFje3AoMS1wKX17bn0gPSBcXGZyYWN7MC4xMCBcXGNkb3QgKDEgLSAwLjEwKX17NTAwfSA9IFxcZnJhY3swLjA5fXs1MDB9ID0gMC4wMDAxOCQuIiwgIlBhc3NvIDQ6IENhbGN1bGFyIG8gZXJybyBwYWRyw6NvOiAkRVAoXFxoYXR7cH0pID0gXFxzcXJ0ezAuMDAwMTh9IFxcYXBwcm94IDAuMDEzNCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjAxMzR9LCB7ImVudW5jaWFkbyI6ICJDb21wYXJlIGEgdmFyaWFiaWxpZGFkZSBkYSBwcm9wb3LDp8OjbyBhbW9zdHJhbCBlbnRyZSBkb2lzIHByb2Nlc3NvcyBpbmR1c3RyaWFpczogbyBQcm9jZXNzbyBBIHRlbSB0YXhhIGRlIGRlZmVpdG9zICRwX0EgPSAwLjA1JCBlIG8gUHJvY2Vzc28gQiB0ZW0gdGF4YSBkZSBkZWZlaXRvcyAkcF9CID0gMC4yNSQuIEFtYm9zIHPDo28gbW9uaXRvcmFkb3MgY29tIGFtb3N0cmFzIGRlIHRhbWFuaG8gJG49MjAwJC4gQ2FsY3VsZSAkVmFyKFxcaGF0e3B9X0EpJCBlICRWYXIoXFxoYXR7cH1fQikkIGUgaW50ZXJwcmV0ZSBxdWFsIHByb2Nlc3NvIGFwcmVzZW50YSBtYWlvciBpbmNlcnRlemEgbmEgZXN0aW1hdGl2YSBkYSBwcm9wb3LDp8Ojby4iLCAiZGljYSI6ICJBIHZhcmlhYmlsaWRhZGUgZGEgcHJvcG9yw6fDo28gw6kgZGFkYSBwb3IgJFZhcihcXGhhdHtwfSkgPSBcXGZyYWN7cCgxLXApfXtufSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IENhbGN1bGFyICRWYXIoXFxoYXR7cH1fQSkgPSBcXGZyYWN7MC4wNSBcXGNkb3QgKDEtMC4wNSl9ezIwMH0gPSBcXGZyYWN7MC4wNSBcXGNkb3QgMC45NX17MjAwfSA9IFxcZnJhY3swLjA0NzV9ezIwMH0gPSAwLjAwMDIzNzUkLiIsICJQYXNzbyAyOiBDYWxjdWxhciAkVmFyKFxcaGF0e3B9X0IpID0gXFxmcmFjezAuMjUgXFxjZG90ICgxLTAuMjUpfXsyMDB9ID0gXFxmcmFjezAuMjUgXFxjZG90IDAuNzV9ezIwMH0gPSBcXGZyYWN7MC4xODc1fXsyMDB9ID0gMC4wMDA5Mzc1JC4iLCAiUGFzc28gMzogQ29tcGFyYXIgb3MgcmVzdWx0YWRvczogJFZhcihcXGhhdHtwfV9CKSA+IFZhcihcXGhhdHtwfV9BKSQuIiwgIlBhc3NvIDQ6IEludGVycHJldGHDp8OjbzogTyBQcm9jZXNzbyBCIGFwcmVzZW50YSBtYWlvciB2YXJpYWJpbGlkYWRlLCBwb2lzIGEgdmFyacOibmNpYSBkYSBkaXN0cmlidWnDp8OjbyBkZSBCZXJub3VsbGkgw6kgbcOheGltYSBxdWFuZG8gJHA9MC41JCBlIGRpbWludWkgY29uZm9ybWUgJHAkIHNlIGFmYXN0YSBkZSAwLjUgZW0gZGlyZcOnw6NvIGFvcyBleHRyZW1vcy4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKCk7IHBfdmFscyA9IG5wLmxpbnNwYWNlKDAsIDEsIDEwMCk7IHZhcl92YWxzID0gcF92YWxzICogKDEgLSBwX3ZhbHMpIC8gMjAwOyBmaWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1wX3ZhbHMsIHk9dmFyX3ZhbHMsIG5hbWU9J1ZhcmnDom5jaWEnLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0zKSkpOyBmaWcudXBkYXRlX2xheW91dCh0aXRsZT0nVmFyacOibmNpYSBkYSBQcm9wb3LDp8OjbyB2cy4gUHJvYmFiaWxpZGFkZSAkcCQnLCB4YXhpc190aXRsZT0nUHJvcG9yw6fDo28gUG9wdWxhY2lvbmFsICgkcCQpJywgeWF4aXNfdGl0bGU9J1ZhcmnDom5jaWEgJFZhcihcXGhhdHtwfSkkJyk7IiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjAwMDkzNzV9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgw7N0aWNhIGRhIHZhcmnDoXZlbCBkZSBCZXJub3VsbGksIHBvciBxdWUgYSBzb21hIGRlICRuJCBvYnNlcnZhw6fDtWVzIGluZGVwZW5kZW50ZXMgcmVzdWx0YSBlbSB1bWEgdmFyacOhdmVsIGFsZWF0w7NyaWEgQmlub21pYWwgZSBjb21vIGEgcHJvcG9yw6fDo28gYW1vc3RyYWwgw6kgZGVyaXZhZGEgZGVzc2UgcHJvY2Vzc28uIiwgImRpY2EiOiAiQ29uc2lkZXJlIHF1ZSBjYWRhIG9ic2VydmHDp8OjbyAkWF9pIFxcc2ltIEJlcm5vdWxsaShwKSQgZSBxdWUgJFggPSBcXHN1bSBYX2kkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiBEZWZpbmlyIGEgdmFyacOhdmVsIGRlIEJlcm5vdWxsaSAkWF9pIFxcaW4gXFx7MCwgMVxcfSQgY29tICRQKFhfaT0xKSA9IHAkLiIsICJQYXNzbyAyOiBFeHBsaWNhciBxdWUgYSBzb21hICRYID0gXFxzdW1fe2k9MX1ebiBYX2kkIGNvbnRhIG8gbsO6bWVybyB0b3RhbCBkZSBzdWNlc3NvcyBlbSAkbiQgZW5zYWlvcyBpbmRlcGVuZGVudGVzLCBvIHF1ZSBkZWZpbmUgYSBkaXN0cmlidWnDp8OjbyBCaW5vbWlhbCAkWCBcXHNpbSBCaW4obiwgcCkkLiIsICJQYXNzbyAzOiBBIHByb3BvcsOnw6NvIGFtb3N0cmFsIMOpIGRlZmluaWRhIGNvbW8gJFxcaGF0e3B9ID0gXFxmcmFje1h9e259JC4iLCAiUGFzc28gNDogQ29uY2x1aXIgcXVlICRcXGhhdHtwfSQgw6kgYSBtw6lkaWEgYXJpdG3DqXRpY2EgZGFzIHZhcmnDoXZlaXMgZGUgQmVybm91bGxpLCByZXByZXNlbnRhbmRvIGEgZnJhw6fDo28gb2JzZXJ2YWRhIGRlIHN1Y2Vzc29zIG5hIGFtb3N0cmEuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtYSBwb3B1bGHDp8OjbyBmaW5pdGEgZGUgJE49MTAwMCQgcGXDp2FzIHByb2R1emlkYXMgcG9yIHVtYSBtw6FxdWluYSwgY29tIHZhcmnDom5jaWEgcG9wdWxhY2lvbmFsICRcXHNpZ21hXjIgPSA0MDAkLiBDYWxjdWxlIGEgdmFyacOibmNpYSBkYSBtw6lkaWEgYW1vc3RyYWwgJFZhcihcXGJhcntYfSkkIHBhcmEgdW1hIGFtb3N0cmEgZGUgdGFtYW5obyAkbj01MCQgZXh0cmHDrWRhIHNlbSByZXBvc2nDp8Ojby4gQ29tcGFyZSBlc3RlIHJlc3VsdGFkbyBjb20gYSB2YXJpw6JuY2lhIGRhIG3DqWRpYSBhbW9zdHJhbCBxdWUgc2VyaWEgb2J0aWRhIHNlIGEgYW1vc3RyYSBmb3NzZSBleHRyYcOtZGEgY29tIHJlcG9zacOnw6NvLiIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSAkVmFyKFxcYmFye1h9KSA9IFxcZnJhY3tcXHNpZ21hXjJ9e259IFxcbGVmdCggXFxmcmFje04gLSBufXtOIC0gMX0gXFxyaWdodCkkIHBhcmEgbyBjYXNvIHNlbSByZXBvc2nDp8OjbyBlICRWYXIoXFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWFeMn17bn0kIHBhcmEgbyBjYXNvIGNvbSByZXBvc2nDp8Ojby4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gUGFyYSBvIGNhc28gY29tIHJlcG9zacOnw6NvOiAkVmFyKFxcYmFye1h9KV97XFx0ZXh0e3JlcH19ID0gXFxmcmFje1xcc2lnbWFeMn17bn0gPSBcXGZyYWN7NDAwfXs1MH0gPSA4JC4iLCAiMi4gUGFyYSBvIGNhc28gc2VtIHJlcG9zacOnw6NvLCBhcGxpY2Ftb3MgbyBGQ1BGOiAkVmFyKFxcYmFye1h9KV97XFx0ZXh0e3NlbSByZXB9fSA9IFxcZnJhY3s0MDB9ezUwfSBcXGNkb3QgXFxmcmFjezEwMDAgLSA1MH17MTAwMCAtIDF9JC4iLCAiMy4gUmVhbGl6YW5kbyBvIGPDoWxjdWxvIGRvIGZhdG9yOiAkOCBcXGNkb3QgXFxmcmFjezk1MH17OTk5fSBcXGFwcHJveCA4IFxcY2RvdCAwLDk1MDk1ID0gNyw2MDc2JC4iLCAiNC4gQ29uY2x1c8OjbzogQSB2YXJpw6JuY2lhIGRhIG3DqWRpYSBhbW9zdHJhbCBzZW0gcmVwb3Npw6fDo28gKDcsNjA3Nikgw6kgbWVub3IgcXVlIGEgdmFyacOibmNpYSBjb20gcmVwb3Npw6fDo28gKDgpLCBkZW1vbnN0cmFuZG8gYSBtYWlvciBwcmVjaXPDo28gb2J0aWRhIHBlbGEgYW1vc3RyYWdlbSBzZW0gcmVwb3Npw6fDo28gZW0gcG9wdWxhw6fDtWVzIGZpbml0YXMuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiA3LjYwNzZ9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgw7N0aWNhIGVzdGF0w61zdGljYSwgcG9yIHF1ZSBhIHZhcmnDom5jaWEgZGEgbcOpZGlhIGFtb3N0cmFsIGRpbWludWkgcXVhbmRvIHJlYWxpemFtb3MgdW1hIGFtb3N0cmFnZW0gc2VtIHJlcG9zacOnw6NvIGVtIHBvcHVsYcOnw7VlcyBmaW5pdGFzLCBlbSBjb21wYXJhw6fDo28gw6AgYW1vc3RyYWdlbSBjb20gcmVwb3Npw6fDo28uIFF1YWwgw6kgbyBwYXBlbCBkbyB0ZXJtbyAkKE4tbikvKE4tMSkkIG5lc3RlIHByb2Nlc3NvPyIsICJkaWNhIjogIlJlZmxpdGEgc29icmUgYSBpbmRlcGVuZMOqbmNpYSBkYXMgb2JzZXJ2YcOnw7VlcyBlIGEgcmVkdcOnw6NvIGRhIGluY2VydGV6YSBhbyBleHBsb3JhciB1bWEgZnJhw6fDo28gZGEgcG9wdWxhw6fDo28uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIE5hIGFtb3N0cmFnZW0gY29tIHJlcG9zacOnw6NvLCBjYWRhIG9ic2VydmHDp8OjbyAkWF9pJCDDqSBpbmRlcGVuZGVudGUgZSB0ZW0gYSBtZXNtYSBkaXN0cmlidWnDp8OjbywgcmVzdWx0YW5kbyBlbSAkVmFyKFxcYmFye1h9KSA9IFxcc2lnbWFeMi9uJC4iLCAiMi4gTmEgYW1vc3RyYWdlbSBzZW0gcmVwb3Npw6fDo28sIGEgc2VsZcOnw6NvIGRlIHVtIGVsZW1lbnRvIGFsdGVyYSBhIGNvbXBvc2nDp8OjbyBkYSBwb3B1bGHDp8OjbyByZXN0YW50ZSwgaW50cm9kdXppbmRvIGRlcGVuZMOqbmNpYSBlbnRyZSBhcyBlc2NvbGhhcy4iLCAiMy4gTyBmYXRvciAkKE4tbikvKE4tMSkkIGF0dWEgY29tbyB1bSBjb3JyZXRvciBxdWUgYWp1c3RhIGEgdmFyacOibmNpYSBwYXJhIHJlZmxldGlyIHF1ZSwgYW8gcmV0aXJhcm1vcyBtYWlzIGVsZW1lbnRvcyBkYSBwb3B1bGHDp8OjbywgdGVtb3MgbWFpb3IgY29uaGVjaW1lbnRvIGRhIG1lc21hLCBkaW1pbnVpbmRvIGEgaW5jZXJ0ZXphIHRlw7NyaWNhICh2YXJpw6JuY2lhKSBkbyBlc3RpbWFkb3IuIiwgIjQuIFF1YW5kbyAkbiQgw6kgdW1hIGZyYcOnw6NvIHBlcXVlbmEgZGUgJE4kLCBvIGZhdG9yIHRlbmRlIGEgMTsgcXVhbmRvICRuJCBzZSBhcHJveGltYSBkZSAkTiQsIG8gZmF0b3IgdGVuZGUgYSAwLCByZWR1emluZG8gYSB2YXJpw6JuY2lhIGEgemVybyBubyBjZW5zby4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMCwgcC4gMjc4IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBwb3B1bGFjaW9uYWwgY29tICROPTUwMCQsIGEgdmFyacOibmNpYSBkYSBwb3B1bGHDp8OjbyDDqSAkXFxzaWdtYV4yPTEwMCQuIENvbXBhcmUgYSB2YXJpw6JuY2lhIGRhIG3DqWRpYSBhbW9zdHJhbCAkVmFyKFxcYmFye1h9KSQgcGFyYSBvcyBzZWd1aW50ZXMgdGFtYW5ob3MgZGUgYW1vc3RyYSBzZW0gcmVwb3Npw6fDo286ICRuXzE9NTAkIGUgJG5fMj0yNTAkLiBDYWxjdWxlIGFtYmFzIGUgZGlzY3V0YSBhIG1hZ25pdHVkZSBkYSByZWR1w6fDo28gZGEgdmFyacOibmNpYSBhbyBhdW1lbnRhciBhIGFtb3N0cmEuIiwgImRpY2EiOiAiQ2FsY3VsZSAkVmFyKFxcYmFye1h9KSQgdXNhbmRvIGEgZsOzcm11bGEgJFZhcihcXGJhcntYfSkgPSBcXGZyYWN7XFxzaWdtYV4yfXtufSBcXGxlZnQoIFxcZnJhY3tOIC0gbn17TiAtIDF9IFxccmlnaHQpJCBwYXJhIGFtYm9zIG9zIGNhc29zLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBQYXJhICRuXzE9NTAkOiAkVmFyKFxcYmFye1h9KV8xID0gXFxmcmFjezEwMH17NTB9IFxcY2RvdCBcXGZyYWN7NTAwIC0gNTB9ezUwMCAtIDF9ID0gMiBcXGNkb3QgXFxmcmFjezQ1MH17NDk5fSBcXGFwcHJveCAyIFxcY2RvdCAwLDkwMTggPSAxLDgwMzYkLiIsICIyLiBQYXJhICRuXzI9MjUwJDogJFZhcihcXGJhcntYfSlfMiA9IFxcZnJhY3sxMDB9ezI1MH0gXFxjZG90IFxcZnJhY3s1MDAgLSAyNTB9ezUwMCAtIDF9ID0gMCw0IFxcY2RvdCBcXGZyYWN7MjUwfXs0OTl9IFxcYXBwcm94IDAsNCBcXGNkb3QgMCw1MDEwID0gMCwyMDA0JC4iLCAiMy4gT2JzZXJ2YcOnw6NvOiBBIHZhcmnDom5jaWEgcmVkdXppdSBzaWduaWZpY2F0aXZhbWVudGUgKGRlIGFwcm94aW1hZGFtZW50ZSAxLDgwIHBhcmEgMCwyMCksIG7Do28gYXBlbmFzIHBlbG8gYXVtZW50byBkZSAkbiQsIG1hcyB0YW1iw6ltIHBlbGEgYcOnw6NvIGRvIEZDUEYsIHF1ZSB0b3Jub3Utc2UgbXVpdG8gbWVub3Igbm8gc2VndW5kbyBjYXNvLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5CYXIoeD1bJ249NTAnLCAnbj0yNTAnXSwgeT1bMS44MDM2LCAwLjIwMDRdLCBtYXJrZXJfY29sb3I9JyMxRTNBOEEnKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdWYXJpw6JuY2lhIGRhIE3DqWRpYSBBbW9zdHJhbCBwb3IgVGFtYW5obyBkZSBBbW9zdHJhJywgeGF4aXNfdGl0bGU9J1RhbWFuaG8gZGEgQW1vc3RyYSAobiknLCB5YXhpc190aXRsZT0nVmFyKFhfXFxiYXIpJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMjAwNH1dfQ==').decode('utf-8'))


    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    
    # Inicialização do estado da sessão para controle de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do total de exercícios
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discursivas = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcqs) + len(discursivas)
    
    # Barra de progresso e estatísticas
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    if total_exercicios > 0:
        progresso = acertos / total_exercicios
        st.progress(progresso)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    
    st.divider()
    
    # Processamento das Questões de Múltipla Escolha
    if mcqs:
        st.header("📝 Questões de Múltipla Escolha")
        for i, questao in enumerate(mcqs):
            with st.container(border=True):
                st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
                
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                # Gráfico dinâmico (se existir)
                codigo = questao.get("codigo_plotly")
                if codigo:
                    local_vars = {"go": go, "np": np}
                    try:
                        exec(codigo, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True)
                    except Exception as e:
                        st.error(f"Erro ao carregar visualização: {e}")
    
                alternativas = questao.get("alternativas", {})
                escolha = st.radio(
                    "Escolha uma alternativa:",
                    options=list(alternativas.keys()),
                    format_func=lambda x: f"{x}: {alternativas[x]}",
                    key=f"radio_mcq_{i}"
                )
                
                if st.button("💡 Dica", key=f"btn_dica_mcq_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
                
                if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
                    if escolha == questao.get("alternativa_correta"):
                        st.success("Correto! Muito bem.")
                        st.session_state.respostas_certas[f"mcq_{i}"] = True
                        st.rerun()
                    else:
                        st.error("Resposta incorreta. Tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
                
                with st.expander("✅ Ver Gabarito Comentado"):
                    st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
    
    # Processamento das Questões Discursivas
    if discursivas:
        st.header("✍️ Questões Discursivas")
        for i, questao in enumerate(discursivas):
            with st.container(border=True):
                st.markdown(f"**Desafio {i+1}:** {questao.get('enunciado', '')}")
                
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                codigo = questao.get("codigo_plotly")
                if codigo:
                    local_vars = {"go": go, "np": np}
                    try:
                        exec(codigo, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True)
                    except Exception as e:
                        st.error(f"Erro ao carregar visualização: {e}")
                
                st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
                
                # Lógica para questões numéricas vs qualitativas
                esperada = questao.get("resposta_numerica_esperada")
                if esperada is not None:
                    user_val = st.number_input("Digite o resultado numérico calculado para validação:", key=f"num_disc_{i}", format="%f")
                    if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                        if abs(user_val - esperada) <= max(0.01, 0.01 * abs(esperada)):
                            st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                            st.session_state.respostas_certas[f"disc_{i}"] = True
                            st.rerun()
                        else:
                            st.error("O valor calculado difere do gabarito oficial. Verifique seus arredondamentos e fórmulas e tente novamente.")
                            st.session_state.respostas_certas[f"disc_{i}"] = False
                else:
                    if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                    else:
                        st.session_state.respostas_certas[f"disc_{i}"] = False
                
                if st.button("💡 Dica", key=f"btn_dica_disc_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
                
                with st.expander("✅ Ver Resolução Detalhada"):
                    for passo in questao.get("gabarito_passo_a_passo", []):
                        st.write(f"- {passo}")
