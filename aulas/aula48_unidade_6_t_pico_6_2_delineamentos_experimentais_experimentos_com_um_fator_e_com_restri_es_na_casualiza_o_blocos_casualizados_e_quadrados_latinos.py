import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDYgLSBUw7NwaWNvIDYuMjogRGVsaW5lYW1lbnRvcyBleHBlcmltZW50YWlzOiBFeHBlcmltZW50b3MgY29tIHVtIGZhdG9yIGUgY29tIHJlc3RyacOnw7VlcyBuYSBjYXN1YWxpemHDp8OjbyAoYmxvY29zIGNhc3VhbGl6YWRvcyBlIHF1YWRyYWRvcyBsYXRpbm9zKSIsICJyZWZlcmVuY2lhc19iaWJsaW9ncmFmaWNhc19maW5haXMiOiBbIkJpc3BvLCBOLiwgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzIC0gQXVsYSAxNyBlIDE4LCBwcC4gNi0xNyIsICJMdW5hLCBKLiBHLiAmIEVzdGV2ZXMsIEUuIE0uLCBFc3RhdMOtc3RpY2EgRXhwZXJpbWVudGFsIC0gQ2Fww610dWxvIDQsIHBwLiA4My0xMTIiLCAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhIC0gQ2Fww610dWxvIDE0LCBwcC4gMzg1LTM5MiIsICJNb250Z29tZXJ5LCBEZXNpZ24gYW5kIEFuYWx5c2lzIG9mIEV4cGVyaW1lbnRzIC0gQ2Fww610dWxvIDQsIHBwLiAxMzUtMTQyIl19').decode('utf-8'))

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
            background: linear-gradient(135deg, #678ae8 0%, #3B82F6 100%);
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
            border-top: 3px solid #678ae8 !important;
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
            background: linear-gradient(90deg, #678ae8 0%, #ff8d00 100%) !important;
            border-radius: 10px !important;
        }
        
        /* Inputs e Sliders na aula */
        div.stSlider [data-testid="stSliderTickBar"] {
            background-color: #678ae8 !important;
        }
        
        /* Botões na aula */
        div.stButton > button {
            background: linear-gradient(135deg, #678ae8 0%, #3B82F6 100%) !important;
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
PRIMARY_BLUE = "#678ae8"
SECONDARY_GREEN = "#ff8d00"
WARNING_AMBER = "#F59E0B"
CRITICAL_RED = "#991B1B"

# Criação das Duas Grandes Abas Globais
tab_conteudo, tab_exercicios = st.tabs(["📚 Conteúdo Acadêmico Interativo", "📝 Caderno de Exercícios"])

with tab_conteudo:

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"A Arquitetura do Experimento: Repetição, Casualização e Controle Local")
    
    # Prosa Inicial
    st.markdown(r"""
    A arquitetura de um experimento científico não é um mero protocolo burocrático de coleta de dados; trata-se, fundamentalmente, de um exercício de inteligência logística e epistemológica. O desafio central do pesquisador é separar o **sinal** (o efeito real da intervenção) do **ruído** (as variações naturais e não controladas do ambiente).
    """)
    
    st.info(r"O planejamento experimental, fundamentado por Ronald Fisher, baseia-se em três pilares inegociáveis: a Repetição, a Casualização e o Controle Local. Juntos, estes mecanismos garantem a validade e a sensibilidade da inferência estatística.")
    
    st.markdown(r"""
    ### 🧬 Os Pilares da Robustez Experimental
    - **Repetição:** Essencial para a estimação da variância residual e quantificação da incerteza experimental. Sem ela, a diferença entre tratamentos torna-se indistinguível do erro aleatório.
    - **Casualização:** Atua como um escudo contra vieses sistemáticos, garantindo que variáveis ocultas sejam distribuídas de forma aleatória entre as unidades experimentais.
    - **Controle Local:** Estratégia refinada que utiliza a blocagem para isolar gradientes ambientais (como fertilidade do solo), reduzindo o erro residual e aumentando a sensibilidade do teste.
    """)
    
    # Formalismo Matemático
    st.markdown(r"### 📐 Formalismo do Modelo Linear")
    st.markdown(r"A estrutura física do experimento é traduzida pelo seguinte modelo linear:")
    st.latex(r"y_{ij} = \mu + \tau_i + \beta_j + e_{ij}")
    st.markdown(r"Onde $\tau_i$ representa o efeito do tratamento de interesse e $\beta_j$ o controle local exercido pelo bloco.")
    
    # Demonstração Analítica (Sequencial Estática)
    st.markdown(r"### 🧮 Partição da Variância e Teste de Hipóteses")
    st.markdown(r"Para verificar a significância dos efeitos, realizamos a partição da Soma de Quadrados:")
    
    st.latex(r"SQT = \sum_{i=1}^{k} \sum_{j=1}^{b} (y_{ij} - \bar{X}_{..})^2")
    st.markdown(r"A variação total é decomposta na contribuição dos tratamentos:")
    st.latex(r"SQTr = b \sum_{i=1}^{k} (\bar{X}_{i.} - \bar{X}_{..})^2")
    st.markdown(r"E na contribuição do controle local (blocos):")
    st.latex(r"SQB = k \sum_{j=1}^{b} (\bar{X}_{.j} - \bar{X}_{..})^2")
    st.markdown(r"Por fim, isolamos o erro experimental residual:")
    st.latex(r"SQE = SQT - SQTr - SQB")
    st.markdown(r"A inferência é realizada via estatística F:")
    st.latex(r"F_{\text{calc}} = \frac{QM_{Tr}}{QM_{Res}} = \frac{SQTr / (k-1)}{SQE / ((k-1)(b-1))}")
    
    # Exemplo Prático
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Teste de Cultivares de Soja")
        st.markdown(r"Um engenheiro agrônomo testa 4 cultivares de soja em 3 blocos. O objetivo é testar $H_0: \tau_1 = \tau_2 = \tau_3 = \tau_4$ frente a um gradiente de fertilidade Norte-Sul.")
        
        st.latex(r"n=12, gl_{\text{num}}=3, gl_{\text{den}}=6")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- **Passo 1:** Cálculo do fator de correção $C = y_{..}^2 / 12$.")
        st.markdown(r"- **Passo 2:** Determinação da SQT e SQTr a partir das médias marginais.")
        st.markdown(r"- **Passo 3:** Ajuste pelo efeito dos blocos (SQB) para purificar o resíduo.")
        
        st.success(r"**Conclusão:** Ao comparar $F_{\text{calc}}$ com $F_{\text{crit}}(3, 6)$, rejeita-se $H_0$ se a estatística exceder o valor crítico, confirmando diferenças significativas entre cultivares após a remoção do ruído ambiental.")
    
    # Painel de Controle (Simulador estático)
    st.markdown(r"### 📊 Simulador de Poder Experimental")
    col1, col2 = st.columns(2)
    n_blocos = col1.slider(r"Número de Blocos", 2, 10, 3, key=r"n_blocos_subtopico_1")
    alfa = col2.select_slider(r"Nível de Significância", options=[0.01, 0.05, 0.1], value=0.05, key=r"alfa_subtopico_1")
    
    # Gráfico
    x = np.linspace(0, 5, 100)
    y = stats.f.pdf(x, 3, (n_blocos-1)*3)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Distribuição F', line=dict(color='#678ae8', width=2)))
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição da Estatística F sob H0</b>", font=dict(size=14, color="#1E293B"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valor de F"), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade"), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    st.info(f"Com {n_blocos} blocos e um nível de significância de {alfa}, a arquitetura do experimento é otimizada para capturar variações espaciais, garantindo que o denominador do teste F (variância residual) seja minimizado.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Delineamento em Blocos Completos Casualizados (DBC): Controle de Heterogeneidade")
    
    # Introdução
    st.markdown(r"""
    O Delineamento em Blocos Completos Casualizados (DBC) representa a manifestação pragmática do **princípio do controle local**, sendo um dos pilares fundamentais da inferência científica em ciências agrárias. Diferente do ideal platônico de homogeneidade absoluta, o campo experimental frequentemente apresenta variações sistemáticas que, se ignoradas, obscurecem a resposta biológica dos tratamentos.
    
    A estratégia central do DBC envolve:
    *   **Particionamento da Variabilidade:** Identificação e isolamento de fontes de variação controláveis (blocos).
    *   **Controle de Tendências Espaciais:** Agrupamento de unidades experimentais em estratos homogêneos (declividade, umidade, fertilidade).
    *   **Balanceamento Ortogonal:** Garantia de que cada tratamento apareça exatamente uma vez em cada bloco, mantendo o equilíbrio estatístico.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Modelo Linear Aditivo")
    st.markdown(r"A resposta de uma unidade experimental $y_{ij}$ é modelada pela soma dos efeitos do tratamento, do bloco e do erro aleatório:")
    st.latex(r"y_{ij} = \mu + \tau_i + \beta_j + e_{ij} \text{ onde } e_{ij} \sim N(0, \sigma^2)")
    
    st.markdown(r"Neste modelo, ao isolarmos o efeito do bloco $\beta_j$, reduzimos a variância residual que inflaria o erro experimental, aumentando a sensibilidade estatística do teste F.")
    
    # Dedução Analítica
    st.subheader(r"🧮 Decomposição da Variância")
    st.markdown(r"A soma de quadrados total (SQT) é decomposta para isolar os efeitos de tratamento e blocos:")
    
    st.latex(r"SQT = \sum_{i=1}^{k} \sum_{j=1}^{b} (y_{ij} - \bar{X}_{..})^2")
    st.markdown(r"Soma de quadrados dos tratamentos (SQTr):")
    st.latex(r"SQTr = b \sum_{i=1}^{k} (\bar{X}_{i.} - \bar{X}_{..})^2")
    st.markdown(r"Soma de quadrados dos blocos (SQB):")
    st.latex(r"SQB = k \sum_{j=1}^{b} (\bar{X}_{.j} - \bar{X}_{..})^2")
    st.markdown(r"Soma de quadrados do erro (SQE):")
    st.latex(r"SQE = SQT - SQTr - SQB")
    st.markdown(r"Estatística de teste:")
    st.latex(r"F_{\text{calc}} = \frac{SQTr / (k-1)}{SQE / ((k-1)(b-1))}")
    
    # Simulador de Particionamento
    st.subheader(r"⚙️ Simulador de Particionamento de Variância em DBC")
    col1, col2 = st.columns(2)
    with col1:
        var_bloco = st.slider(r"Variabilidade dos Blocos", 0.0, 100.0, 50.0, key=r"slider_bloco_subtopico_2")
    with col2:
        efe_trat = st.slider(r"Efeito dos Tratamentos", 0.0, 50.0, 25.0, key=r"slider_trat_subtopico_2")
    
    # Lógica do Simulador (estática/determinística para demonstração didática)
    sqt_total = 200
    sq_bloco = var_bloco
    sq_trat = efe_trat
    sq_erro = sqt_total - sq_bloco - sq_trat
    f_calc = (sq_trat / 2) / (sq_erro / 8) if sq_erro > 0 else 0
    
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[r"Tratamento", r"Blocos", r"Erro"], y=[sq_trat, sq_bloco, sq_erro], marker_color=[r"#678ae8", r"#ff8d00", r"#991B1B"]))
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Decomposição da Variância</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Fontes de Variação", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Soma de Quadrados", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    st.info(f"Ao ajustar a variabilidade dos blocos para {var_bloco:.1f}, o erro residual é minimizado. O F_calc resultante de {f_calc:.2f} demonstra como o bloqueamento aumenta a sensibilidade estatística.")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Eficácia de Fontes de Nitrogênio")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Fontes de Nitrogênio no Milho")
        st.markdown(r"Pesquisadores avaliam a eficácia de 3 fontes de nitrogênio (N1, N2, N3) em 5 blocos, controlando fertilidade Leste-Oeste.")
        st.latex(r"k=3, b=5, n=15, gl_{\text{num}}=2, gl_{\text{den}}=8")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Passo 1: Cálculo da constante C = y_{..}^2 / 15")
        st.markdown(r"- Passo 2: Cálculo da SQTr através das médias dos tratamentos")
        st.markdown(r"- Passo 3: Cálculo da SQB através das médias dos blocos")
        st.markdown(r"- Passo 4: Obtenção do SQE por diferença residual")
        st.success(r"O sucesso deste delineamento permitiu que a variância ambiental fosse controlada, resultando em um F_calc robusto que confirma a superioridade de uma das fontes de nitrogênio.")

    # Importações necessárias (assumindo que o ambiente principal as possui)
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Delineamento em Quadrados Latinos (DQL): Duplo Bloqueamento e Rigor Experimental")
    
    # Introdução e Prosa densa
    st.markdown(r"""
    Quando a heterogeneidade ambiental ocorre em dois gradientes simultâneos — como fertilidade Norte-Sul e umidade Leste-Oeste — o Delineamento em Quadrados Latinos (DQL) torna-se a ferramenta de eleição. Este design impõe uma restrição de ortogonalidade onde cada tratamento surge uma única vez em cada linha e coluna. Esta estrutura permite remover duas fontes de variação sistemática, isolando o efeito do tratamento com extrema precisão. Embora altamente eficaz, a exigência de que o número de tratamentos, linhas e colunas sejam iguais impõe uma limitação prática em estudos com múltiplos fatores ou restrições de espaço.
    """)
    
    st.info(r"O delineamento experimental é, em sua essência, a arte de controlar o ruído. Para o agrônomo que se debruça sobre um talhão experimental, a maior ameaça à validade de suas conclusões não é o tratamento em si, mas a imperfeição inerente ao solo.")
    
    st.markdown(r"""
    ### 📐 O Coração Matemático: Modelo Linear do DQL
    Para compreender o rigor matemático que sustenta o DQL, observamos o modelo linear aditivo que descreve a resposta observada em cada parcela.
    """)
    
    st.latex(r"y_{ijk} = \mu + \tau_k + L_i + C_j + e_{ijk}")
    
    st.markdown(r"""
    Nesta formulação:
    - $y_{ijk}$: Valor observado na linha $i$, coluna $j$, com tratamento $k$.
    - $\mu$: Média geral do experimento.
    - $\tau_k$: Efeito específico do $k$-ésimo tratamento.
    - $L_i$ e $C_j$: Efeitos dos gradientes de linhas e colunas.
    - $e_{ijk}$: Componente de erro aleatório com média zero e variância constante.
    """)
    
    st.markdown(r"### 🧮 Dedução Analítica da Partição da Variância")
    
    st.markdown(r"A variação total é decomposta na soma das fontes de variação:")
    st.latex(r"SQT = \sum_{i=1}^{r} \sum_{j=1}^{r} (y_{ij} - \bar{X}_{...})^2")
    
    st.markdown(r"O efeito das linhas é isolado como:")
    st.latex(r"SQL = r \sum_{i=1}^{r} (\bar{X}_{i..} - \bar{X}_{...})^2")
    
    st.markdown(r"O efeito das colunas é isolado como:")
    st.latex(r"SQC = r \sum_{j=1}^{r} (\bar{X}_{.j.} - \bar{X}_{...})^2")
    
    st.markdown(r"O erro residual é obtido pela subtração da variação total menos os efeitos controlados:")
    st.latex(r"SQE = SQT - SQL - SQC - SQTr")
    
    st.markdown(r"O teste de hipóteses para a significância dos tratamentos segue a distribuição F:")
    st.latex(r"F_{\text{calc}} = \frac{SQTr / (r-1)}{SQE / ((r-1)(r-2))}")
    
    st.markdown(r"### 📈 Casos de Aplicação Prática: Experimento com Cultivares")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Teste de Cultivares de Milho")
        st.markdown(r"Um experimento testa 4 cultivares de milho sob dois gradientes de campo (inclinação e irrigação) usando um DQL 4x4.")
        
        st.latex(r"r=4, gl_{\text{Tr}}=3, gl_{\text{L}}=3, gl_{\text{C}}=3, gl_{\text{Res}}=6")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Passo 1: Cálculo da Soma de Quadrados dos Tratamentos: $SQTr = \frac{\sum T_k^2}{4} - C$")
        st.markdown(r"- Passo 2: Cálculo da Soma de Quadrados das Linhas: $SQL = \frac{\sum L_i^2}{4} - C$")
        st.markdown(r"- Passo 3: Cálculo da Soma de Quadrados das Colunas: $SQC = \frac{\sum C_j^2}{4} - C$")
        st.markdown(r"- Passo 4: Obtenção do erro por diferença: $SQE = SQT - SQTr - SQL - SQC$")
        st.markdown(r"- Passo 5: Determinação da estatística de teste: $F_{\text{calc}} = \frac{SQTr / 3}{SQE / 6}$")
        
        st.success(r"O DQL foi decisivo para isolar o ruído espacial das duas direções, validando a comparação entre cultivares com elevado rigor estatístico, dado que o erro residual foi minimizado significativamente pela estrutura de bloqueamento duplo.")
    
    st.markdown(r"""
    ---
    ### 💡 Considerações sobre o Rigor no Planejamento
    A restrição de que o número de tratamentos seja igual ao número de linhas e colunas é, ao mesmo tempo, a maior virtude e a principal limitação do DQL. Do ponto de vista pedagógico, é fundamental notar:
    - **Graus de Liberdade:** O erro é calculado como $(t-1)(t-2)$. Se $t$ for pequeno, o poder do teste cai significativamente.
    - **Aleatorização:** Deve-se sortear a ordem das linhas e colunas para garantir que o quadrado seja apenas um entre os muitos possíveis, protegendo contra vieses espaciais ocultos.
    """)

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDYgLSBUw7NwaWNvIDYuMjogRGVsaW5lYW1lbnRvcyBleHBlcmltZW50YWlzOiBFeHBlcmltZW50b3MgY29tIHVtIGZhdG9yIGUgY29tIHJlc3RyacOnw7VlcyBuYSBjYXN1YWxpemHDp8OjbyAoYmxvY29zIGNhc3VhbGl6YWRvcyBlIHF1YWRyYWRvcyBsYXRpbm9zKSIsICJxdWVzdG9lc19tdWx0aXBsYV9lc2NvbGhhIjogW3siZW51bmNpYWRvIjogIlVtIGVuZ2VuaGVpcm8gYWdyw7Rub21vIHBsYW5lamEgdW0gZXhwZXJpbWVudG8gcGFyYSBjb21wYXJhciBhIGVmaWNpw6puY2lhIGRlIDQgbm92b3MgYmlvZmVydGlsaXphbnRlcyBlbSB1bWEgY3VsdHVyYSBkZSBtaWxoby4gTyBjYW1wbyBleHBlcmltZW50YWwgYXByZXNlbnRhIHVtIGRlY2xpdmUgYWNlbnR1YWRvLCBvIHF1ZSBzdWdlcmUgdW1hIHZhcmlhw6fDo28gbmEgZmVydGlsaWRhZGUgZG8gc29sbyBhbyBsb25nbyBkYSBlbmNvc3RhLiBQYXJhIGdhcmFudGlyIGEgdmFsaWRhZGUgZXN0YXTDrXN0aWNhIGRhcyBjb25jbHVzw7VlcyBzb2JyZSBvIGVmZWl0byBkb3MgdHJhdGFtZW50b3MgKCRcdGF1X2kkKSwgbyBwZXNxdWlzYWRvciBkZWNpZGUgaW1wbGVtZW50YXIgbyBwcmluY8OtcGlvIGRhIGNhc3VhbGl6YcOnw6NvLiBDb25zaWRlcmFuZG8gbyBtb2RlbG8gbGluZWFyIGFkaXRpdm8gJHlfe2lqfSA9IFxiXFxldGFfMCArIFx0YXVfaSArIGVfe2lqfSQsIHF1YWwgw6kgbyBvYmpldGl2byBmdW5kYW1lbnRhbCBkYSBjYXN1YWxpemHDp8OjbyBuZXN0ZSBjb250ZXh0bz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkVsaW1pbmFyIGNvbXBsZXRhbWVudGUgYSB2YXJpYWJpbGlkYWRlIG5hdHVyYWwgKCRcXHNpZ21hXjIkKSBwcmVzZW50ZSBuYXMgdW5pZGFkZXMgZXhwZXJpbWVudGFpcywgdG9ybmFuZG8gb3MgZGFkb3MgcGVyZmVpdGFtZW50ZSBob21vZ8OqbmVvcy4iLCAiQiI6ICJHYXJhbnRpciBxdWUgYXMgdW5pZGFkZXMgZXhwZXJpbWVudGFpcyByZWNlYmFtIHRyYXRhbWVudG9zIGRlIGZvcm1hIGEgYmFsYW5jZWFyIGVmZWl0b3Mgc2lzdGVtw6F0aWNvcyBkZXNjb25oZWNpZG9zLCBldml0YW5kbyB2aWVzZXMgbmEgZXN0aW1hdGl2YSBkbyBlZmVpdG8gZG8gdHJhdGFtZW50by4iLCAiQyI6ICJQZXJtaXRpciBxdWUgYSBtw6lkaWEgZ2xvYmFsICgkXFxtdSQpIHNlamEgY2FsY3VsYWRhIGNvbSB1bSBuw612ZWwgZGUgY29uZmlhbsOnYSBzdXBlcmlvciBhIDk1JSwgaW5kZXBlbmRlbnRlbWVudGUgZG8gdGFtYW5obyBhbW9zdHJhbCAoJG4kKS4iLCAiRCI6ICJBdW1lbnRhciBhIHZhcmnDom5jaWEgcmVzaWR1YWwgKCRTXjIkKSBwYXJhIHF1ZSBvIHRlc3RlIGRlIGhpcMOzdGVzZSBzZWphIG1haXMgY29uc2VydmFkb3IgYW8gcmVqZWl0YXIgYSBoaXDDs3Rlc2UgbnVsYSAoJEhfMCQpLiIsICJFIjogIkdhcmFudGlyIHF1ZSB0b2RvcyBvcyB0cmF0YW1lbnRvcyBhcHJlc2VudGVtLCBuZWNlc3NhcmlhbWVudGUsIGEgbWVzbWEgcmVzcG9zdGEgbcOpZGlhICgkXFxiYXJ7WH1faSQpLCBjb25maXJtYW5kbyBhIGVmaWPDoWNpYSBkbyBleHBlcmltZW50by4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIlBlbnNlIG5vIG9iamV0aXZvIGRlIEZpc2hlcjogYSBjYXN1YWxpemHDp8OjbyBwcm90ZWdlIGNvbnRyYSBmYXRvcmVzIGV4dGVybm9zIHF1ZSBvIHBlc3F1aXNhZG9yIG7Do28gY29uc2VndWUgY29udHJvbGFyIHRvdGFsbWVudGUsIGltcGVkaW5kbyBxdWUgZXNzYXMgdmFyaWHDp8O1ZXMgc2VqYW0gY29uZnVuZGlkYXMgY29tIG8gZWZlaXRvIGRvcyB0cmF0YW1lbnRvcy4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgY2FzdWFsaXphw6fDo28gw6kgbyBwcmluY8OtcGlvIHF1ZSBwcm90ZWdlIG8gZXhwZXJpbWVudG8gY29udHJhIHZpZXNlcyBzaXN0ZW3DoXRpY29zLiBBbyBhdHJpYnVpciBvcyB0cmF0YW1lbnRvcyAoJFxcdGF1X2kkKSBhbGVhdG9yaWFtZW50ZSDDoHMgdW5pZGFkZXMgZXhwZXJpbWVudGFpcywgZ2FyYW50aW1vcyBxdWUgcXVhaXNxdWVyIGZhdG9yZXMgbsOjbyBjb250cm9sYWRvcyAoY29tbyBncmFkaWVudGVzIGRlIGZlcnRpbGlkYWRlIG91IGluY2lkw6puY2lhIHNvbGFyKSBzZWphbSBkaXN0cmlidcOtZG9zIGRlIGZvcm1hIGFsZWF0w7NyaWEgZW50cmUgb3MgZ3J1cG9zLCBlIG7Do28gY29uY2VudHJhZG9zIGVtIHVtIMO6bmljbyB0cmF0YW1lbnRvLiBJc3NvIGV2aXRhIHF1ZSBvIGVmZWl0byBkbyB0cmF0YW1lbnRvIHNlamEgc3VwZXJlc3RpbWFkbyBvdSBzdWJlc3RpbWFkbyBwb3IgZmF0b3JlcyBlc3BhY2lhaXMsIGFzc2VndXJhbmRvIGEgdmFsaWRhZGUgaW50ZXJuYSBkYSBhbsOhbGlzZSBlc3RhdMOtc3RpY2EuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgdW0gZW5zYWlvIGRlIHJlc2lzdMOqbmNpYSBkZSBtYXRlcmlhaXMgZW0gMyBsb3RlcyBkZSBwcm9kdcOnw6NvIGRpc3RpbnRvcywgb25kZSBzZSBzdXNwZWl0YSBkZSB1bWEgdmFyaWHDp8OjbyBuYSBxdWFsaWRhZGUgZG8gbWF0ZXJpYWwgZW50cmUgb3MgbG90ZXMuIFVtIGVuZ2VuaGVpcm8gZGVjaWRlIHV0aWxpemFyIG8gZGVsaW5lYW1lbnRvIGVtIGJsb2NvcyBjYXN1YWxpemFkb3MgKERCQykuIFNlIG8gbW9kZWxvIGRvIGV4cGVyaW1lbnRvIMOpICR5X3tpan0gPSBcYmFye1h9ICsgXHRhdV9pICsgXGJcXGV0YV9qICsgZV97aWp9JCwgY29tbyBvIGNvbnRyb2xlIGxvY2FsIGF0cmF2w6lzIGRvIHRlcm1vICRcYlxcZXRhX2okIGFmZXRhIGEgYW7DoWxpc2UgZXN0YXTDrXN0aWNhIGVtIGNvbXBhcmHDp8OjbyBhIHVtIGRlbGluZWFtZW50byBpbnRlaXJhbWVudGUgYW8gYWNhc28gKERJQyk/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIGNvbnRyb2xlIGxvY2FsIGF1bWVudGEgbyB2YWxvciBkbyBwLXZhbG9yLCB0b3JuYW5kbyBtYWlzIGRpZsOtY2lsIGEgcmVqZWnDp8OjbyBkYSBoaXDDs3Rlc2UgbnVsYSAoJEhfMCQpIHNvYnJlIG9zIHRyYXRhbWVudG9zLiIsICJCIjogIk8gdGVybW8gJFxcYmV0YV9qJCByZWR1eiBhIG3DqWRpYSBnbG9iYWwgKCRcXG11JCksIHBlcm1pdGluZG8gdW0gY8OhbGN1bG8gbWFpcyBwcmVjaXNvIGRvIGRlc3ZpbyBwYWRyw6NvIGFtb3N0cmFsICgkUyQpLiIsICJDIjogIk8gYmxvcXVlYW1lbnRvIGlzb2xhIGEgaGV0ZXJvZ2VuZWlkYWRlIGFtYmllbnRhbCwgcmVkdXppbmRvIG8gZXJybyBleHBlcmltZW50YWwgKCRlX3tpan0kKSBlLCBjb25zZXF1ZW50ZW1lbnRlLCBhdW1lbnRhbmRvIG8gcG9kZXIgZG8gdGVzdGUgcGFyYSBkZXRlY3RhciBkaWZlcmVuw6dhcyBlbnRyZSBvcyB0cmF0YW1lbnRvcyAoJFxcdGF1X2kkKS4iLCAiRCI6ICJPIGNvbnRyb2xlIGxvY2FsIMOpIG9icmlnYXTDs3JpbyBhcGVuYXMgcXVhbmRvIG8gbsO6bWVybyBkZSByZXBldGnDp8O1ZXMgKCRuJCkgcG9yIHRyYXRhbWVudG8gw6kgaW5mZXJpb3IgYSAzLCBuw6NvIGluZmx1ZW5jaWFuZG8gYSBwcmVjaXPDo28gc2UgJG4kIGZvciBncmFuZGUuIiwgIkUiOiAiTyB0ZXJtbyAkXFxiZXRhX2okIHN1YnN0aXR1aSBhIG5lY2Vzc2lkYWRlIGRlIHJlcGV0acOnw6NvLCBwZXJtaXRpbmRvIHF1ZSBjYWRhIHRyYXRhbWVudG8gc2VqYSBhcGxpY2FkbyB1bWEgw7puaWNhIHZleiBlbSBjYWRhIGxvdGUuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJPIGNvbnRyb2xlIGxvY2FsIChibG9jb3MpIHNlcnZlIHBhcmEgcmVtb3ZlciBhIHZhcmlhw6fDo28gaW5kZXNlamFkYSBkbyByZXPDrWR1bywgZmF6ZW5kbyBjb20gcXVlIGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlIHNlamEgbWFpcyBzZW5zw612ZWwuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJObyBtb2RlbG8gJHlfe2lqfSA9IFxiYXJ7WH0gKyBcdGF1X2kgKyBcYlxcZXRhX2ogKyBlX3tpan0kLCBhIHZhcmlhYmlsaWRhZGUgdG90YWwgb2JzZXJ2YWRhIMOpIGRlY29tcG9zdGEuIEFvIHV0aWxpemFyIGJsb2NvcyAoJFxcYmV0YV9qJCksIHJlbW92ZW1vcyBhIHZhcmlhw6fDo28gYXRyaWJ1w612ZWwgw6AgaGV0ZXJvZ2VuZWlkYWRlIGRvcyBsb3RlcyBkbyBlcnJvIGV4cGVyaW1lbnRhbCAoJGVfe2lqfSQpLiBBbyByZWR1emlyIGEgdmFyacOibmNpYSBkbyBlcnJvLCBhdW1lbnRhbW9zIG8gdmFsb3IgZGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlICgkRl97XFx0ZXh0e2NhbGN9fSQpLCBwb2lzIGEgdmFyacOibmNpYSByZXNpZHVhbCBubyBkZW5vbWluYWRvciBkbyB0ZXN0ZSAkRiQgc2Vyw6EgbWVub3IsIGNvbmZlcmluZG8gbWFpb3IgcHJlY2lzw6NvIGUgcG9kZXIgZXN0YXTDrXN0aWNvIHBhcmEgYXZhbGlhciBvcyBlZmVpdG9zIGZpeG9zIGRvcyB0cmF0YW1lbnRvcyAoJFxcdGF1X2kkKS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtIGFncsO0bm9tbyBwbGFuZWphIHRlc3RhciBxdWF0cm8gZGlmZXJlbnRlcyB2YXJpZWRhZGVzIGRlIG1pbGhvIChUcmF0YW1lbnRvczogJEEsIEIsIEMsIEQkKSBlbSB1bWEgcHJvcHJpZWRhZGUgcXVlIGFwcmVzZW50YSB1bSBncmFkaWVudGUgY2xhcm8gZGUgdW1pZGFkZSBubyBzb2xvLiBQYXJhIGNvbnRyb2xhciBlc3NhIGhldGVyb2dlbmVpZGFkZSwgZWxlIHV0aWxpemEgbyBEZWxpbmVhbWVudG8gZW0gQmxvY29zIENvbXBsZXRvcyBDYXN1YWxpemFkb3MgKERCQyksIG9yZ2FuaXphbmRvIGEgw6FyZWEgZW0gNSBibG9jb3MsIG9uZGUgY2FkYSBibG9jbyByZWNlYmUgYXMgNCB2YXJpZWRhZGVzLiBBbyBmaW5hbGl6YXIgbyBleHBlcmltZW50byBlIHJlYWxpemFyIGEgQU5PVkEsIGVsZSBvYnRldmUgdW1hIGVzdGF0w61zdGljYSAkRl97MFR9ID0gNC44MCQgcGFyYSB0cmF0YW1lbnRvcyBlICRGX3swQn0gPSAwLjk1JCBwYXJhIGJsb2NvcywgY29tIHZhbG9yIGNyw610aWNvICRGX3tcdGV4dHtjcml0fX0oMywgMTIpID0gMy40OSQgcGFyYSB0cmF0YW1lbnRvcyBlICRGX3tcdGV4dHtjcml0fX0oNCwgMTIpID0gMy4yNiQgcGFyYSBibG9jb3MgKCRcXGFscGhhID0gNVxcJSQpLiBBc3N1bWluZG8gcXVlIGFzIHByZW1pc3NhcyBkbyBtb2RlbG8gJHlfe2lqfSA9IFxcbXUgKyBcXHRhdV9pICsgXFxiZXRhX2ogKyBlX3tpan0kIGZvcmFtIHNhdGlzZmVpdGFzLCBxdWFsIMOpIGEgY29uY2x1c8OjbyBlc3RhdGlzdGljYW1lbnRlIGNvcnJldGE/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJFeGlzdGUgZGlmZXJlbsOnYSBzaWduaWZpY2F0aXZhIGVudHJlIGFzIHZhcmllZGFkZXMsIG1hcyBvIGJsb3F1ZWFtZW50byBuw6NvIGZvaSBlZmljYXogZW0gY29udHJvbGFyIGEgaGV0ZXJvZ2VuZWlkYWRlIGFtYmllbnRhbC4iLCAiQiI6ICJOw6NvIGV4aXN0ZSBkaWZlcmVuw6dhIGVudHJlIGFzIHZhcmllZGFkZXMgZSBvIGJsb3F1ZWFtZW50byBmb2kgZXNzZW5jaWFsIHBhcmEgbyBzdWNlc3NvIGRvIGV4cGVyaW1lbnRvLiIsICJDIjogIkV4aXN0ZSBkaWZlcmVuw6dhIGVudHJlIGFzIHZhcmllZGFkZXMgZSBvIGJsb3F1ZWFtZW50byBmb2kgZGVzbmVjZXNzw6FyaW8sIHBvaXMgJEZfezBCfSA8IEZfe1x0ZXh0e2NyaXR9fSQuIiwgIkQiOiAiTyBtb2RlbG8gbsOjbyDDqSB2w6FsaWRvLCBwb2lzIGEgc29tYSBkb3MgZWZlaXRvcyBkb3MgYmxvY29zICRcXHN1bSBcXGJldGFfaiQgZGV2ZSBzZXIgaWd1YWwgYSAxLCBlIG7Do28gMC4iLCAiRSI6ICJPIGJsb3F1ZWFtZW50byBmb2kgZWZpY2F6IGUgbsOjbyBleGlzdGUgZXZpZMOqbmNpYSBkZSBkaWZlcmVuw6dhIGVudHJlIGFzIHZhcmllZGFkZXMgZGUgbWlsaG8uIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJDb21wYXJlIGNhZGEgZXN0YXTDrXN0aWNhIGNhbGN1bGFkYSAoJEZfezBUfSQgZSAkRl97MEJ9JCkgY29tIHNldSByZXNwZWN0aXZvIHZhbG9yIGNyw610aWNvLiBMZW1icmUtc2UgcXVlIG8gZWZlaXRvIGRlIGJsb2NvcyBzZXJ2ZSBhcGVuYXMgcGFyYSBjb250cm9sZSBsb2NhbCBlIHJlZHXDp8OjbyBkYSB2YXJpw6JuY2lhIHJlc2lkdWFsLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUGFyYSBvcyB0cmF0YW1lbnRvczogJEZfezBUfSA9IDQuODAgPiBGX3tcXHRleHR7Y3JpdH19ID0gMy40OSQsIGxvZ28gcmVqZWl0YW1vcyAkSF8wJCAoZXhpc3RlIGRpZmVyZW7Dp2EgZW50cmUgYXMgdmFyaWVkYWRlcykuIFBhcmEgb3MgYmxvY29zOiAkRl97MEJ9ID0gMC45NSA8IEZfe1xcdGV4dHtjcml0fX0gPSAzLjI2JCwgbG9nbyBuw6NvIGjDoSBldmlkw6puY2lhIGRlIHF1ZSBvcyBibG9jb3MgZGlmZXJpcmFtIHNpZ25pZmljYXRpdmFtZW50ZSBlbnRyZSBzaS4gUG9ydGFudG8sIGVtYm9yYSBvIGNvbnRyb2xlIGxvY2FsIHRlbmhhIHNpZG8gYXBsaWNhZG8sIG9zIGRhZG9zIG7Do28gaW5kaWNhbSBxdWUgYSBoZXRlcm9nZW5laWRhZGUgZGEgdW1pZGFkZSBlcmEgdMOjbyBhY2VudHVhZGEgYSBwb250byBkZSB0b3JuYXIgb3MgYmxvY29zIHNpZ25pZmljYXRpdmFtZW50ZSBkaXN0aW50b3MsIGNvbmZpcm1hbmRvIGEgYWx0ZXJuYXRpdmEgQS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIk7DrXZlYSBCaXNwbywgQXVsYSAxODogSW50cm9kdcOnw6NvIMOgIEFOT1ZBIG5vcyBkZWxpbmVhbWVudG9zIGFtb3N0cmFpcywgcC4gNCJ9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgdW0gZXhwZXJpbWVudG8gZW0gREJDIGNvbSAkaz0zJCB0cmF0YW1lbnRvcyBlICRiPTQkIGJsb2Nvcy4gQSBzb21hIGRlIHF1YWRyYWRvcyBkbyBlcnJvIGZvaSBjYWxjdWxhZGEgY29tbyAkU1FFID0gMTMuMyQgZSBvIG7Dum1lcm8gZGUgZ3JhdXMgZGUgbGliZXJkYWRlIGRvIHJlc8OtZHVvIMOpICRnbF97cmVzfSA9IChrLTEpKGItMSkkLiBRdWFsIG8gdmFsb3IgZG8gUXVhZHJhZG8gTcOpZGlvIGRvIFJlc8OtZHVvICgkUU1SZXMkKSB1dGlsaXphZG8gbm8gY8OhbGN1bG8gZGEgZXN0YXTDrXN0aWNhICRGJCBlIG5vIHRlc3RlIGRlIGNvbXBhcmHDp8O1ZXMgbcO6bHRpcGxhcyBkZSBUdWtleT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjMuMzI1IiwgIkIiOiAiMi4yMTciLCAiQyI6ICIxLjEwOCIsICJEIjogIjYuNjUwIiwgIkUiOiAiMTMuMzAwIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJPICRRTVJlcyQgw6kgb2J0aWRvIHBlbGEgZGl2aXPDo28gZGEgc29tYSBkZSBxdWFkcmFkb3MgZG8gcmVzw61kdW8gKCRTUUUkKSBwZWxvcyBzZXVzIGdyYXVzIGRlIGxpYmVyZGFkZSAoJGdsX3tyZXN9JCkuIE5vIERCQywgJGdsX3tyZXN9ID0gKGstMSkoYi0xKSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJEYWRvczogJGs9MyQsICRiPTQkLCAkU1FFID0gMTMuMyQuIEPDoWxjdWxvIGRvcyBncmF1cyBkZSBsaWJlcmRhZGU6ICRnbF97cmVzfSA9ICgzLTEpIFxcdGltZXMgKDQtMSkgPSAyIFxcdGltZXMgMyA9IDYkLiBDw6FsY3VsbyBkbyAkUU1SZXMgPSBcXGZyYWN7U1FFfXtnbF97cmVzfX0gPSBcXGZyYWN7MTMuM317Nn0gXFxhcHByb3ggMi4yMTY2JC4gQXJyZWRvbmRhbmRvLCBvYnRlbW9zIDIuMjE3LiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTsOtdmVhIEJpc3BvLCBBdWxhIDE3OiBJbnRyb2R1w6fDo28gw6AgQU5PVkEgbm9zIGRlbGluZWFtZW50b3MgYW1vc3RyYWlzLCBwLiAxOCJ9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlbnNhaW8gYWdyb27DtG1pY28gcGFyYSBhdmFsaWFyIGEgcHJvZHV0aXZpZGFkZSBkZSBkaWZlcmVudGVzIGN1bHRpdmFyZXMgZGUgc29qYSwgdW0gcGVzcXVpc2Fkb3IgdXRpbGl6b3UgdW0gRGVsaW5lYW1lbnRvIGVtIEJsb2NvcyBDb21wbGV0b3MgQ2FzdWFsaXphZG9zIChEQkMpIGNvbSA0IGJsb2NvcyBlIDUgY3VsdGl2YXJlcywgdmlzYW5kbyBjb250cm9sYXIgYSB2YXJpYcOnw6NvIG5hIGZlcnRpbGlkYWRlIGRvIHNvbG8gZW0gdW0gZGVjbGl2ZS4gQXDDs3MgYSBhbsOhbGlzZSBkYSB2YXJpw6JuY2lhLCBvYnRldmUtc2UgdW0gUXVhZHJhZG8gTcOpZGlvIGRvIFJlc8OtZHVvICgkUU1fe1JlcyhEQkMpfSQpIGRlIDEyLDUgJGtnXjIvaGFeMiQuIFNlIG8gZXhwZXJpbWVudG8gdGl2ZXNzZSBzaWRvIGNvbmR1emlkbyBlbSB1bSBEZWxpbmVhbWVudG8gSW50ZWlyYW1lbnRlIENhc3VhbGl6YWRvIChESUMpLCBvIFF1YWRyYWRvIE3DqWRpbyBkbyBFcnJvICgkUU1fe1JlcyhESUMpfSQpIGVzdGltYWRvLCBjb21iaW5hbmRvIGEgdmFyaWHDp8OjbyBkb3MgYmxvY29zIGNvbSBvIHJlc8OtZHVvLCByZXN1bHRvdSBlbSAyNSwwICRrZ14yL2hhXjIkLiBDb25zaWRlcmFuZG8gcXVlIG9zIGdyYXVzIGRlIGxpYmVyZGFkZSBkbyByZXPDrWR1byBubyBEQkMgc8OjbyAkZ2xfe0V9ID0gMTIkIGUgb3MgZ3JhdXMgZGUgbGliZXJkYWRlIHRvdGFpcyBubyBESUMgaGlwb3TDqXRpY28gc8OjbyAkZ2xfe1RyfSArIGdsX3tFfSA9IDE5JCwgcXVhbCBhIGVmaWNpw6puY2lhIHJlbGF0aXZhICgkRVIkKSBkbyBEQkMgZW0gcmVsYcOnw6NvIGFvIERJQz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjEsODUiLCAiQiI6ICIyLDE0IiwgIkMiOiAiMSw5OCIsICJEIjogIjIsMDUiLCAiRSI6ICIxLDUwIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgZGUgYXBsaWNhciBhIGbDs3JtdWxhIGRlIGNvcnJlw6fDo28gcGFyYSBhIGVmaWNpw6puY2lhIHJlbGF0aXZhIHV0aWxpemFuZG8gb3MgZ3JhdXMgZGUgbGliZXJkYWRlIGRvIHJlc8OtZHVvIChkZW5vbWluYWRvcik6ICRFUiA9IFxcZnJhY3soZ2xfe1xcdGV4dHtkZW4oRElDKX19ICsgMSkoZ2xfe1xcdGV4dHtkZW4oREJDKX19ICsgMyl9eyhnbF97XFx0ZXh0e2RlbihEQkMpfX0gKyAxKShnbF97XFx0ZXh0e2RlbihESUMpfX0gKyAzKX0gXFxjZG90IFxcZnJhY3tRTV97UmVzKERJQyl9fXtRTV97UmVzKERCQyl9fSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIGNhbGN1bGFyIGEgZWZpY2nDqm5jaWEgcmVsYXRpdmEsIHRlbW9zOiAkZ2xfe1xcdGV4dHtkZW4oREJDKX19ID0gMTIkIGUgJGdsX3tcXHRleHR7ZGVuKERJQyl9fSA9IDE5JC4gU3Vic3RpdHVpbmRvIG5hIGbDs3JtdWxhOiAkRVIgPSBcXGZyYWN7KDE5KzEpKDEyKzMpfXsoMTIrMSkoMTkrMyl9IFxcY2RvdCBcXGZyYWN7MjUsMH17MTIsNX0gPSBcXGZyYWN7MjAgXFxjZG90IDE1fXsxMyBcXGNkb3QgMjJ9IFxcY2RvdCAyID0gXFxmcmFjezMwMH17Mjg2fSBcXGNkb3QgMiBcXGFwcHJveCAxLDA0ODkgXFxjZG90IDIgXFxhcHByb3ggMiwwOTc4JC4gQXJyZWRvbmRhbmRvIHBhcmEgZHVhcyBjYXNhcyBkZWNpbWFpcywgbyB2YWxvciBtYWlzIHByw7N4aW1vIMOpIDIsMTQgKGRldmlkbyBhb3MgYWp1c3RlcyBkZSBwcmVjaXPDo28gY29tdW0gZW0gdGFiZWxhcyBkZSBncmF1cyBkZSBsaWJlcmRhZGUpLiBOb3RhOiBvIHZhbG9yIGRlIDIsMTQgcmVmbGV0ZSBhIHByZWNpc8OjbyBlc3RhdMOtc3RpY2EgZ2FuaGEgY29tIG8gY29udHJvbGUgbG9jYWwgZG9zIGJsb2Nvcy4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtIGFncsO0bm9tbyBhbmFsaXNhIG8gQ29lZmljaWVudGUgZGUgVmFyaWHDp8OjbyAoJENWJCkgZGUgdW0gZXhwZXJpbWVudG8gZGUgbWlsaG8gY29uZHV6aWRvIGVtIERCQy4gTyBkZXN2aW8gcGFkcsOjbyByZXNpZHVhbCBjYWxjdWxhZG8gYSBwYXJ0aXIgZG8gJFFNX3tSZXMoREJDKX0kIGZvaSBkZSA4LDAgdC9oYSwgZW5xdWFudG8gYSBtw6lkaWEgZ2VyYWwgZGFzIG9ic2VydmHDp8O1ZXMgZm9pIGRlIDQwLDAgdC9oYS4gQ29tbyBvIHBlc3F1aXNhZG9yIGRldmUgY2xhc3NpZmljYXIgYSBwcmVjaXPDo28gZXhwZXJpbWVudGFsIGRlc3RlIGVzdHVkbyBzZWd1bmRvIG9zIGNyaXTDqXJpb3MgdXN1YWlzIGRhIMOhcmVhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiw5N0aW1hIHByZWNpc8OjbyBleHBlcmltZW50YWwsIHBvaXMgbyBDViDDqSAxMCUuIiwgIkIiOiAiQm9hIHByZWNpc8OjbyBleHBlcmltZW50YWwsIHBvaXMgbyBDViBlc3TDoSBlbnRyZSAxMCUgZSAyMCUuIiwgIkMiOiAiUMOpc3NpbWEgcHJlY2lzw6NvIGV4cGVyaW1lbnRhbCwgcG9pcyBvIENWIMOpIHN1cGVyaW9yIGEgMjAlLiIsICJEIjogIsOTdGltYSBwcmVjaXPDo28gZXhwZXJpbWVudGFsLCBwb2lzIG8gQ1Ygw6kgMjAlLiIsICJFIjogIkJvYSBwcmVjaXPDo28gZXhwZXJpbWVudGFsLCBwb2lzIG8gQ1Ygw6kgNSUuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJDYWxjdWxlIHByaW1laXJvIG8gY29lZmljaWVudGUgZGUgdmFyaWHDp8OjbyB1dGlsaXphbmRvIGEgZsOzcm11bGEgJENWID0gKFMgLyBcXGJhcntYfV97Li59KSBcXHRpbWVzIDEwMCQsIG9uZGUgJFMgPSBcXHNxcnR7UU1fe1JlcyhEQkMpfX0kLCBlIGNvbXBhcmUgY29tIG9zIGludGVydmFsb3MgZGUgY2xhc3NpZmljYcOnw6NvOiAkMC0xMFxcJSQsICQxMC0yMFxcJSQsIGUgJD4yMFxcJSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJPIGRlc3ZpbyBwYWRyw6NvIHJlc2lkdWFsIMOpICRTID0gOCwwJC4gQSBtw6lkaWEgw6kgJFxcYmFye1h9X3suLn0gPSA0MCwwJC4gTyAkQ1YgPSAoOCwwIC8gNDAsMCkgXFx0aW1lcyAxMDAgPSAwLDIgXFx0aW1lcyAxMDAgPSAyMFxcJSQuIERlIGFjb3JkbyBjb20gb3MgY3JpdMOpcmlvcyBkZSBwcmVjaXPDo28gZXhwZXJpbWVudGFsICgwLTEwJSDDs3RpbWEsIDEwLTIwJSBib2EsID4yMCUgcMOpc3NpbWEpLCBvIHZhbG9yIGRlIDIwJSBzaXR1YS1zZSBubyBsaW1pdGUgc3VwZXJpb3IgZGEgY2xhc3NpZmljYcOnw6NvIGRlICdib2EgcHJlY2lzw6NvJy4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoZGF0YT1bZ28uQmFyKHg9WydDViBFeHBlcmltZW50YWwnXSwgeT1bMjBdLCBtYXJrZXJfY29sb3I9JyNmZjhkMDAnKV0pXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nQ29lZmljaWVudGUgZGUgVmFyaWHDp8OjbyBFeHBlcmltZW50YWwnLCB5YXhpcz1kaWN0KHRpdGxlPSdDViAoJSknLCByYW5nZT1bMCwgMzBdKSwgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTsOtdmVhIEJpc3BvLCBBdWxhIDE4OiBJbnRyb2R1w6fDo28gw6AgQU5PVkEgbm9zIGRlbGluZWFtZW50b3MgYW1vc3RyYWlzLCBERVNULVVGQkEgMjAyNS4xIn0sIHsiZW51bmNpYWRvIjogIlVtIGFncsO0bm9tbyBwbGFuZWphIHVtIGV4cGVyaW1lbnRvIHBhcmEgY29tcGFyYXIgYSBwcm9kdXRpdmlkYWRlIGRlICRyPTQkIGN1bHRpdmFyZXMgZGUgbWlsaG8gZW0gdW1hIMOhcmVhIGV4cGVyaW1lbnRhbCBxdWUgYXByZXNlbnRhIGRvaXMgZ3JhZGllbnRlcyBkZSBmZXJ0aWxpZGFkZSBkaXN0aW50b3M6IHVtIGdyYWRpZW50ZSBkZSBkZWNsaXZlIG5vIHNlbnRpZG8gTm9ydGUtU3VsIGUgdW0gZ3JhZGllbnRlIGRlIGRyZW5hZ2VtIG5vIHNlbnRpZG8gTGVzdGUtT2VzdGUuIENvbnNpZGVyYW5kbyBxdWUgbyBkZWxpbmVhbWVudG8gZXNjb2xoaWRvIGZvaSBvIFF1YWRyYWRvIExhdGlubyAoJDQgXFx0aW1lcyA0JCksIHF1YWwgZGFzIGFsdGVybmF0aXZhcyBhYmFpeG8gZGVzY3JldmUgY29ycmV0YW1lbnRlIGEgbMOzZ2ljYSBkZSBjb250cm9sZSBkZXNzZSBhcnJhbmpvIGV4cGVyaW1lbnRhbD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gRFFMIHBlcm1pdGUgYXBlbmFzIG8gY29udHJvbGUgZGUgdW0gw7puaWNvIGdyYWRpZW50ZSBkZSBmZXJ0aWxpZGFkZSwgc2VuZG8gaW5mZXJpb3IgYW8gRGVsaW5lYW1lbnRvIGVtIEJsb2NvcyBDb21wbGV0b3MgQ2FzdWFsaXphZG9zIHBhcmEgYSBzaXR1YcOnw6NvIGRlc2NyaXRhLiIsICJCIjogIk8gRFFMIGlzb2xhIG8gZWZlaXRvIGRlIGNhZGEgY3VsdGl2YXIsIG1hcyBuw6NvIGNvbnNlZ3VlIHNlcGFyYXIgb3MgZWZlaXRvcyBzaXN0ZW3DoXRpY29zIGRvcyBncmFkaWVudGVzIGRlIHNvbG8sIG1hbnRlbmRvLW9zIGluY29ycG9yYWRvcyBubyBlcnJvIGV4cGVyaW1lbnRhbC4iLCAiQyI6ICJPIERRTCB1dGlsaXphIGEgb3J0b2dvbmFsaWRhZGUgcGFyYSBnYXJhbnRpciBxdWUgY2FkYSBjdWx0aXZhciBhcGFyZcOnYSBleGF0YW1lbnRlIHVtYSB2ZXogZW0gY2FkYSBsaW5oYSBlIGNhZGEgY29sdW5hLCBwZXJtaXRpbmRvIGEgZWxpbWluYcOnw6NvIGRhIHZhcmlhYmlsaWRhZGUgYXNzb2NpYWRhIGFvcyBkb2lzIGdyYWRpZW50ZXMgZGUgZm9ybWEgaW5kZXBlbmRlbnRlLiIsICJEIjogIk8gbsO6bWVybyBkZSBncmF1cyBkZSBsaWJlcmRhZGUgZG8gZXJybyBleHBlcmltZW50YWwgbm8gRFFMICQ0IFxcdGltZXMgNCQgw6kgc3VwZXJpb3IgYW8gZGUgdW0gRGVsaW5lYW1lbnRvIEludGVpcmFtZW50ZSBDYXN1YWxpemFkbyAoRElDKSBjb20gbyBtZXNtbyBuw7ptZXJvIHRvdGFsIGRlIHVuaWRhZGVzIGV4cGVyaW1lbnRhaXMuIiwgIkUiOiAiQSByZXN0cmnDp8OjbyBkbyBEUUwgZXhpZ2UgcXVlIGFzIHBhcmNlbGFzIHNlamFtIGRpc3Bvc3RhcyBhbGVhdG9yaWFtZW50ZSBzZW0gY29uc2lkZXJhciBhcyBsaW5oYXMgZSBjb2x1bmFzLCB0cmF0YW5kby1hcyBhcGVuYXMgY29tbyByZXBldGnDp8O1ZXMgc2ltcGxlcy4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgYSBlc3PDqm5jaWEgZG8gUXVhZHJhZG8gTGF0aW5vIMOpIGEgY2FwYWNpZGFkZSBkZSByZWFsaXphciB1bSBkdXBsbyBibG9xdWVhbWVudG8gYXRyYXbDqXMgZG8gY29udHJvbGUgZGUgbGluaGFzIGUgY29sdW5hcyBzaW11bHRhbmVhbWVudGUuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGFsdGVybmF0aXZhIGNvcnJldGEgw6kgYSBDLiBPIERRTCDDqSBlc3RyYXRlZ2ljYW1lbnRlIHN1cGVyaW9yIHBhcmEgY29udHJvbGFyIGRvaXMgZ3JhZGllbnRlcyBhbWJpZW50YWlzIChsaW5oYXMgZSBjb2x1bmFzKS4gQW8gaW1wb3IgYSByZXN0cmnDp8OjbyBkZSBxdWUgY2FkYSB0cmF0YW1lbnRvIG9jb3JyYSB1bWEgdmV6IHBvciBsaW5oYSBlIHVtYSB2ZXogcG9yIGNvbHVuYSwgbyBtb2RlbG8gbGluZWFyICR5X3tpamt9ID0gXFxtdSArIFxcdGF1X2sgKyBMX2kgKyBDX2ogKyBlX3tpamt9JCBwZXJtaXRlIHBhcnRpY2lvbmFyIGEgc29tYSBkZSBxdWFkcmFkb3MgdG90YWwgZW0gY29tcG9uZW50ZXMgYXRyaWJ1w612ZWlzIGEgdHJhdGFtZW50b3MsIGxpbmhhcywgY29sdW5hcyBlIGVycm8uIElzc28gYXVtZW50YSBhIHByZWNpc8OjbyBhbyByZWR1emlyIG8gZXJybyBleHBlcmltZW50YWwgcmVzaWR1YWwgKCRTUUUkKSwgcGVybWl0aW5kbyBtYWlvciBwb2RlciBubyB0ZXN0ZSBkZSBoaXDDs3Rlc2VzIHNvYnJlIG9zIHRyYXRhbWVudG9zLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZShkYXRhPVtnby5IZWF0bWFwKHo9W1sxLCAyLCAzLCA0XSwgWzIsIDMsIDQsIDFdLCBbMywgNCwgMSwgMl0sIFs0LCAxLCAyLCAzXV0sIGNvbG9yc2NhbGU9W1swLCAnIzY3OGFlOCddLCBbMSwgJyNmZjhkMDAnXV0pXSk7IGZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5MYXlvdXQgZGUgdW0gUXVhZHJhZG8gTGF0aW5vICg0eDQpPC9iPicsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnLCB4YXhpcz1kaWN0KHRpdGxlPSdDb2x1bmEnLCBmaXhlZHJhbmdlPVRydWUpLCB5YXhpcz1kaWN0KHRpdGxlPSdMaW5oYScsIGZpeGVkcmFuZ2U9VHJ1ZSkpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXhwZXJpbWVudG8gZGUgRFFMIGNvbSAkcj01JCB0cmF0YW1lbnRvcyAoZG9zZXMgZGUgYWR1Ym8pLCBkZXNlamEtc2UgcmVhbGl6YXIgYSBhbsOhbGlzZSBkZSB2YXJpw6JuY2lhIChBTk9WQSkgcGFyYSB2ZXJpZmljYXIgc2UgZXhpc3RlbSBkaWZlcmVuw6dhcyBzaWduaWZpY2F0aXZhcyBuYSBwcm9kdcOnw6NvLiBRdWFsIMOpIG8gbsO6bWVybyBkZSBncmF1cyBkZSBsaWJlcmRhZGUgKCRnbCQpIGFzc29jaWFkbyBhbyByZXPDrWR1byAoZXJybyBleHBlcmltZW50YWwpIG5lc3NlIGRlbGluZWFtZW50bz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjQiLCAiQiI6ICIxMiIsICJDIjogIjE2IiwgIkQiOiAiMjAiLCAiRSI6ICIyNCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiQSBmw7NybXVsYSBkb3MgZ3JhdXMgZGUgbGliZXJkYWRlIGRvIGVycm8gZW0gdW0gRFFMIMOpICQoci0xKShyLTIpJCwgb25kZSAkciQgw6kgbyBuw7ptZXJvIGRlIHRyYXRhbWVudG9zLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBhbHRlcm5hdGl2YSBjb3JyZXRhIMOpIGEgQi4gUGFyYSB1bSBEUUwgZGUgb3JkZW0gJHIgXFx0aW1lcyByJCwgdGVtb3M6ICRnbF97XFx0ZXh0e3RyYXRhbWVudG99fSA9IHItMSQsICRnbF97XFx0ZXh0e2xpbmhhc319ID0gci0xJCwgJGdsX3tcXHRleHR7Y29sdW5hc319ID0gci0xJC4gTyBuw7ptZXJvIHRvdGFsIGRlIG9ic2VydmHDp8O1ZXMgw6kgJG4gPSByXjIkLCBlbnTDo28gJGdsX3tcXHRleHR7dG90YWx9fSA9IHJeMiAtIDEkLiBDb21vICRnbF97XFx0ZXh0e2Vycm99fSA9IGdsX3tcXHRleHR7dG90YWx9fSAtIChnbF97XFx0ZXh0e3RyYXRhbWVudG99fSArIGdsX3tcXHRleHR7bGluaGFzfX0gKyBnbF97XFx0ZXh0e2NvbHVuYXN9fSkkLCB0ZW1vcyAkZ2xfe1xcdGV4dHtlcnJvfX0gPSAocl4yIC0gMSkgLSAzKHItMSkgPSAoci0xKShyKzEpIC0gMyhyLTEpID0gKHItMSkocisxLTMpID0gKHItMSkoci0yKSQuIFBhcmEgJHI9NSQ6ICQoNS0xKSg1LTIpID0gNCBcXHRpbWVzIDMgPSAxMiQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBlbmdlbmhlaXJvIGFncsO0bm9tbyBwbGFuZWphIHVtIGV4cGVyaW1lbnRvIHBhcmEgYXZhbGlhciBhIGVmaWPDoWNpYSBkZSBxdWF0cm8gZG9zZXMgZGUgdW0gbm92byBmZXJ0aWxpemFudGUgKCRyPTQkKSBzb2JyZSBhIHByb2R1dGl2aWRhZGUgZGUgbWlsaG8uIEVsZSBvcHRhIHBvciB1bSBEZWxpbmVhbWVudG8gZW0gUXVhZHJhZG8gTGF0aW5vIChEUUwpIHBhcmEgY29udHJvbGFyIG8gZWZlaXRvIGRhIGZlcnRpbGlkYWRlIGRvIHNvbG8gZW0gZHVhcyBkaXJlw6fDtWVzIHBlcnBlbmRpY3VsYXJlcyAoZGVjbGl2aWRhZGUgZSB0ZXh0dXJhKS4gU2FiZW5kbyBxdWUgbyBEUUwgw6kgdW0gZGVsaW5lYW1lbnRvIGV4dHJlbWFtZW50ZSByw61naWRvLCBxdWFsIMOpIG8gbsO6bWVybyBkZSBncmF1cyBkZSBsaWJlcmRhZGUgZG8gcmVzw61kdW8gKCRnbF97UmVzfSQpIGRpc3BvbsOtdmVsIHBhcmEgYSBlc3RpbWF0aXZhIGRhIHZhcmnDom5jaWEgZXhwZXJpbWVudGFsIG5lc3RhIGNvbmZpZ3VyYcOnw6NvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiNiIsICJCIjogIjkiLCAiQyI6ICIxMiIsICJEIjogIjE1IiwgIkUiOiAiMyJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGbDs3JtdWxhIGRlIGdyYXVzIGRlIGxpYmVyZGFkZSBkbyByZXPDrWR1byBwYXJhIG8gRFFMOiAkZ2xfe1Jlc30gPSAoci0xKShyLTIpJCwgb25kZSAkciQgw6kgbyBuw7ptZXJvIGRlIHRyYXRhbWVudG9zLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTm8gRFFMLCBvIG7Dum1lcm8gZGUgZ3JhdXMgZGUgbGliZXJkYWRlIHBhcmEgbyByZXPDrWR1byDDqSBkZXRlcm1pbmFkbyBwZWxhIGbDs3JtdWxhICQoci0xKShyLTIpJC4gUGFyYSB1bSBleHBlcmltZW50byBjb20gJHI9NCQgdHJhdGFtZW50b3MsIHRlbW9zOiAkZ2xfe1Jlc30gPSAoNC0xKSg0LTIpID0gMyBcdGltZXMgMiA9IDYkLiBBIHJpZ2lkZXogZG8gRFFMIGRlY29ycmUganVzdGFtZW50ZSBkZXNzYSBwZXJkYSBkZSBncmF1cyBkZSBsaWJlcmRhZGUgZGV2aWRvIGFvIGNvbnRyb2xlIGVtIGR1YXMgZGlyZcOnw7VlcyAobGluaGFzIGUgY29sdW5hcyksIG8gcXVlIHBvZGUgcmVkdXppciBvIHBvZGVyIGRvIHRlc3RlIEYgc2UgbyBuw7ptZXJvIGRlIHRyYXRhbWVudG9zIGZvciBtdWl0byBiYWl4by4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSBleHBlcmltZW50byBlbSBEUUwgY29tICRyPTUkIHRyYXRhbWVudG9zLiBBcMOzcyBhIGNvbGV0YSBkb3MgZGFkb3MsIGEgYW7DoWxpc2UgZGUgdmFyacOibmNpYSAoQU5PVkEpIGZvaSByZWFsaXphZGEuIFF1YWwgZGFzIGFsdGVybmF0aXZhcyBhYmFpeG8gZGVzY3JldmUgY29ycmV0YW1lbnRlIHVtYSBsaW1pdGHDp8OjbyBjb25jZWl0dWFsIGltcG9ydGFudGUgZGVzdGUgZGVsaW5lYW1lbnRvIGFvIHZlcmlmaWNhciBhcyBwcmVtaXNzYXMgZG8gbW9kZWxvIGxpbmVhciBhZGl0aXZvICR5X3tpamt9ID0gXFxtdSArIFxcdGF1X2sgKyBMX2kgKyBDX2ogKyBlX3tpamt9JD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gRFFMIHNlbXByZSBnYXJhbnRlIHF1ZSBhIHZhcmnDom5jaWEgZG8gZXJybyBzZWphIGNvbnN0YW50ZSwgaW5kZXBlbmRlbnRlbWVudGUgZGEgcHJlc2Vuw6dhIGRlIG91dGxpZXJzIG5hcyBsaW5oYXMgb3UgY29sdW5hcy4iLCAiQiI6ICJBIHJlc3RyacOnw6NvIGRlIG9ydG9nb25hbGlkYWRlIGV4aWdlIHF1ZSBvcyBlZmVpdG9zIGRlIGxpbmhhIGUgY29sdW5hIHNlamFtIG9icmlnYXRvcmlhbWVudGUgYWxlYXTDs3Jpb3MuIiwgIkMiOiAiVmlvbGHDp8O1ZXMgZGEgc3Vwb3Npw6fDo28gZGUgYWRpdGl2aWRhZGUgKGludGVyYcOnw6NvIGVudHJlIHRyYXRhbWVudG9zIGUgYmxvY29zKSBwb2RlbSBpbmZsYXIgYSBzb21hIGRlIHF1YWRyYWRvcyBkbyByZXPDrWR1bywgbWFzY2FyYW5kbyBlZmVpdG9zIHJlYWlzIGRvcyB0cmF0YW1lbnRvcy4iLCAiRCI6ICJPIG7Dum1lcm8gZGUgZ3JhdXMgZGUgbGliZXJkYWRlIGRvIGVycm8gYXVtZW50YSBwcm9wb3JjaW9uYWxtZW50ZSBjb20gbyBuw7ptZXJvIGRlIHRyYXRhbWVudG9zLCBlbGltaW5hbmRvIHJpc2NvcyBkZSBiYWl4byBwb2RlciBlc3RhdMOtc3RpY28uIiwgIkUiOiAiTyBtb2RlbG8gcHJlc3N1cMO1ZSBxdWUgbyBlZmVpdG8gZGFzIGNvbHVuYXMgbsOjbyBwb3NzdWkgbcOpZGlhIHplcm8sIGV4aWdpbmRvIHVtYSBjb3JyZcOnw6NvIGNvbXBsZXhhIG5vIGPDoWxjdWxvIGRhIHNvbWEgZGUgcXVhZHJhZG9zIHRvdGFsLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiTyBtb2RlbG8gRFFMIMOpIGFkaXRpdm8uIFNlIGhvdXZlciBpbnRlcmHDp8OjbyAobyB0cmF0YW1lbnRvIHJlc3BvbmRlIGRlIGZvcm1hIGRpZmVyZW50ZSBkZXBlbmRlbmRvIGRhIGxpbmhhIG91IGNvbHVuYSksIG8gbW9kZWxvIGxpbmVhciBzaW1wbGVzIGZhbGhhLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBtb2RlbG8gZXN0YXTDrXN0aWNvIGRvIERRTCDDqSBlc3RyaXRhbWVudGUgYWRpdGl2by4gU2UgaG91dmVyIGludGVyYcOnw6NvIGVudHJlIG8gdHJhdGFtZW50byBlIGFzIGZvbnRlcyBkZSBjb250cm9sZSAobGluaGFzIG91IGNvbHVuYXMpLCBhIHN1cG9zacOnw6NvIGRlIGFkaXRpdmlkYWRlIMOpIHZpb2xhZGEuIElzc28gZmF6IGNvbSBxdWUgZXNzYSB2YXJpYcOnw6NvIGRhIGludGVyYcOnw6NvIHNlamEgY2FwdGFkYSBwZWxvIHRlcm1vIGRlIGVycm8gKCRlX3tpamt9JCksIGF1bWVudGFuZG8gYSBlc3RpbWF0aXZhIGRhIHZhcmnDom5jaWEgcmVzaWR1YWwgKCRRTVJlcyQpLCBvIHF1ZSByZWR1eiBvIHZhbG9yIGRhIGVzdGF0w61zdGljYSAkRl97Y2FsY30kIGUsIGNvbnNlcXVlbnRlbWVudGUsIGRpbWludWkgbyBwb2RlciBlc3RhdMOtc3RpY28gZG8gdGVzdGUsIHBvZGVuZG8gbGV2YXIgYSBlcnJvcyBkbyBUaXBvIElJIChuw6NvIHJlamVpdGFyICRIXzAkIHF1YW5kbyBlbGEgw6kgZmFsc2EpLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfV0sICJxdWVzdG9lc19kaXNjdXJzaXZhcyI6IFt7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgZGUgZm9ybWEgdMOpY25pY2EgZSB1dGlsaXphbmRvIGEgbm90YcOnw6NvIGRvIG1vZGVsbyBsaW5lYXIgYWRpdGl2byAkeV97aWp9ID0gXGJhcntYfSArIFx0YXVfaSArIFxiXFxldGFfaiArIGVfe2lqfSQsIHF1YWwgYSBpbXBvcnTDom5jaWEgZGUgY2FkYSBjb21wb25lbnRlIGRvIG1vZGVsbyBwYXJhIGEgYXJxdWl0ZXR1cmEgZGUgdW0gZXhwZXJpbWVudG8gZW0gYmxvY29zIGNhc3VhbGl6YWRvcy4gQ29tbyBhIHByZW1pc3NhICRlX3tpan0gXGJhY2tzaW0gTigwLCBcYmFye1xcc2lnbWF9XjIpJCBzdXN0ZW50YSBhIGFuw6FsaXNlIGVzdGF0w61zdGljYT8iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIGNhZGEgY29tcG9uZW50ZSByZXByZXNlbnRhIHVtYSBmb250ZSBkZSB2YXJpYcOnw6NvIG91IHVtIGVmZWl0byBlc3RydXR1cmFsLiBPIHRlcm1vICRlX3tpan0kIMOpIGEgYmFzZSBwYXJhIG8gZXJybyBleHBlcmltZW50YWwsIGUgc3VhIG5vcm1hbGlkYWRlIMOpIGNydWNpYWwgcGFyYSBhIGluZmVyw6puY2lhLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJPIG1vZGVsbyAkeV97aWp9ID0gXGJhcntYfSArIFx0YXVfaSArIFxiXFxldGFfaiArIGVfe2lqfSQgZGVzY3JldmUgYSByZXNwb3N0YSBvYnNlcnZhZGEgZGVjb21wb3N0YSBlbSBlZmVpdG9zIGFkaXRpdm9zLiIsICIkXFxiYXJ7WH0kIChtw6lkaWEgZ2xvYmFsKTogUmVwcmVzZW50YSBhIHJlc3Bvc3RhIG3DqWRpYSBlc3BlcmFkYSBkZSB0b2RhcyBhcyB1bmlkYWRlcyBleHBlcmltZW50YWlzIGRvIGV4cGVyaW1lbnRvLiIsICIkXFx0YXVfaSQ6IEVmZWl0byBmaXhvIGRvICRpJC3DqXNpbW8gdHJhdGFtZW50bywgcXVlIHJlZmxldGUgbyBkZXN2aW8gZGEgbcOpZGlhIGNhdXNhZG8gZXNwZWNpZmljYW1lbnRlIHBlbGEgaW50ZXJ2ZW7Dp8OjbyAoZXg6IGZlcnRpbGl6YW50ZSkuIiwgIiRcXGJldGFfaiQ6IEVmZWl0byBkbyAkaiQtw6lzaW1vIGJsb2NvLCBxdWUgaXNvbGEgYSBoZXRlcm9nZW5laWRhZGUgY29uaGVjaWRhIChleDogZGVjbGl2ZSBkbyB0ZXJyZW5vKSwgcmVtb3ZlbmRvLWEgZGEgdmFyaWHDp8OjbyBxdWUgc2VyaWEgY29udGFkYSBubyBlcnJvLiIsICIkZV97aWp9JDogRXJybyBhbGVhdMOzcmlvLCBxdWUgY2FwdHVyYSB0b2RhIGEgdmFyaWFiaWxpZGFkZSBuw6NvIGV4cGxpY2FkYS4gQSBwcmVtaXNzYSAkZV97aWp9IFxiYWNrc2ltIE4oMCwgXFxzaWdtYV4yKSQgw6kgZnVuZGFtZW50YWwgcG9pcyBnYXJhbnRlIHF1ZSBhIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSBzZWd1aXLDoSB1bWEgZGlzdHJpYnVpw6fDo28gJEYkIHNvYiBhIGhpcMOzdGVzZSBudWxhICRIXzAkLCBwZXJtaXRpbmRvIGEgcmVhbGl6YcOnw6NvIGRlIHRlc3RlcyBkZSBzaWduaWZpY8OibmNpYSB2w6FsaWRvcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBleHBlcmltZW50byBjb20gNCB0cmF0YW1lbnRvcyBlIDUgcmVwZXRpw6fDtWVzIGZvaSBjb25kdXppZG8gZW0gdW0gRElDIChpbnRlaXJhbWVudGUgYW8gYWNhc28pLiBPIHBlc3F1aXNhZG9yIGRlc2NvYnJpdSBhcMOzcyBvIGV4cGVyaW1lbnRvIHF1ZSBvIHNvbG8gdGluaGEgdW1hIGluY2xpbmHDp8OjbyBhY2VudHVhZGEuIFNlIGVsZSB0aXZlc3NlIHV0aWxpemFkbyB1bSBEQkMgKGJsb2NvcyBjYXN1YWxpemFkb3MpIGNvbSA1IGJsb2NvcywgY29tbyBhIHNvbWEgZGUgcXVhZHJhZG9zIGRvIGVycm8gKCRTUUUkKSBzZXJpYSBhZmV0YWRhIGUgcXVhbCBvIGltcGFjdG8gbm8gcC12YWxvciBkbyB0ZXN0ZSBGIHBhcmEgbyBlZmVpdG8gZG9zIHRyYXRhbWVudG9zPyIsICJkaWNhIjogIkNvbnNpZGVyZSBxdWUgYSBzb21hIGRlIHF1YWRyYWRvcyB0b3RhbCAoJFNRVCQpIMOpIGZpeGEuIFNlIGEgdmFyaWHDp8OjbyBkZSBibG9jb3MgKCRTUUIkKSBmb3IgZXh0cmHDrWRhIGRlICRTUUUkLCBvIHF1ZSBhY29udGVjZSBjb20gYSB2YXJpw6JuY2lhIHJlc2lkdWFsICgkUU1SZXMkKT8iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRW0gdW0gRElDLCAkU1FUID0gU1FSICsgU1FFJC4gVG9kbyBvIGVycm8gYW1iaWVudGFsIGVzdMOhIGNvbnRpZG8gZW0gJFNRRSQuIiwgIkVtIHVtIERCQywgJFNRVCA9IFNRUiArIFNRQiArIFNRRSQuIE8gdGVybW8gJFNRQiQgY2FwdHVyYSBwYXJ0ZSBkYSB2YXJpYcOnw6NvIGFtYmllbnRhbCBxdWUgZXN0YXZhIGVtICRTUUUkLiIsICJDb21vICRTUUVfe0RCQ30gPCBTUUVfe0RJQ30kLCB0ZW1vcyBxdWUgbyBRdWFkcmFkbyBNw6lkaW8gZG8gUmVzw61kdW8gKCRRTVJlcyA9IFNRRSAvIGdsX3tyZXN9JCkgZGltaW51aS4iLCAiQSBlc3RhdMOtc3RpY2EgJEYgPSBRTVQgLyBRTVJlcyQgYXVtZW50YSwgcG9pcyBvIGRlbm9taW5hZG9yIGRpbWludWl1LiIsICJDb21vICRGX3tcXHRleHR7Y2FsY319JCBhdW1lbnRhLCBhIHByb2JhYmlsaWRhZGUgZGUgb2JzZXJ2YXIgdW0gdmFsb3Igc3VwZXJpb3Igc29iICRIXzAkIGRpbWludWksIHJlc3VsdGFuZG8gZW0gdW0gJHBcdGV4dHstdmFsb3J9JCBtZW5vciwgYXVtZW50YW5kbyBhIHNlbnNpYmlsaWRhZGUgcGFyYSByZWplaXRhciAkSF8wJC4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uQmFyKHg9WydESUMnLCAnREJDJ10sIHk9WzE1MCwgNDVdLCBuYW1lPSdFcnJvIEV4cGVyaW1lbnRhbCcsIG1hcmtlcl9jb2xvcj0nIzk5MUIxQicpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J1JlZHXDp8OjbyBkbyBFcnJvIEV4cGVyaW1lbnRhbCBwb3IgQmxvcXVlYW1lbnRvJywgeGF4aXNfdGl0bGU9J0RlbGluZWFtZW50bycsIHlheGlzX3RpdGxlPSdWYXJpw6JuY2lhIFJlc2lkdWFsJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpXG5zdC5wbG90bHlfY2hhcnQoZmlnLCB1c2VfY29udGFpbmVyX3dpZHRoPVRydWUpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGVmaW5hIG8gcHJpbmPDrXBpbyBkYSByZXBldGnDp8OjbyBubyBwbGFuZWphbWVudG8gZXhwZXJpbWVudGFsIGUgZGVtb25zdHJlLCBhdHJhdsOpcyBkYSBmw7NybXVsYSBkYSB2YXJpw6JuY2lhIGRhIG3DqWRpYSBhbW9zdHJhbCAkRVAoXFxiYXJ7WH0pID0gXFxzcXJ0e1xcc2lnbWFeMi9ufSQsIHBvciBxdWUgYXVtZW50YXIgbyBuw7ptZXJvIGRlIHJlcGV0acOnw7VlcyAoJG4kKSBwb3IgdHJhdGFtZW50byDDqSBtYXRlbWF0aWNhbWVudGUgZXNzZW5jaWFsIHBhcmEgYSBwcmVjaXPDo28gZGFzIGVzdGltYXRpdmFzIGRlIGVmZWl0b3MgZGUgdHJhdGFtZW50by4iLCAiZGljYSI6ICJBbmFsaXNlIG8gY29tcG9ydGFtZW50byBkYSBmdW7Dp8OjbyBkZSBlcnJvIHBhZHLDo28gcXVhbmRvICRuJCBjcmVzY2UuIE8gcXVlIGFjb250ZWNlIGNvbSBhIGluY2VydGV6YSBkYSBlc3RpbWF0aXZhIGRhIG3DqWRpYT8iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSByZXBldGnDp8OjbyBjb25zaXN0ZSBuYSBhcGxpY2HDp8OjbyBkZSB1bSB0cmF0YW1lbnRvIGVtIG3Dumx0aXBsYXMgdW5pZGFkZXMgZXhwZXJpbWVudGFpcyBpbmRlcGVuZGVudGVzLCBwZXJtaXRpbmRvIGEgZXN0aW1hdGl2YSBkYSB2YXJpw6JuY2lhICRcXHNpZ21hXjIkLiIsICJPIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgZGUgdW0gdHJhdGFtZW50byDDqSBkYWRvIHBvciAkRVAoXFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0kLiIsICLDgCBtZWRpZGEgcXVlIGF1bWVudGFtb3MgbyBuw7ptZXJvIGRlIHJlcGV0acOnw7VlcyAkbiQsIG8gZGVub21pbmFkb3IgJFxcc3FydHtufSQgY3Jlc2NlLiIsICJNYXRlbWF0aWNhbWVudGUsICRcXGxpbV97biBcXHRvIFxcaW5mdHl9IFxcZnJhY3tcXHNpZ21hfXtcXHNxcnR7bn19ID0gMCQuIiwgIlBvcnRhbnRvLCBxdWFudG8gbWFpb3IgbyAkbiQsIG1lbm9yIGEgdmFyaWFiaWxpZGFkZSBkYSBlc3RpbWF0aXZhICRcXGJhcntYfV9pJCBlbSB0b3JubyBkYSB2ZXJkYWRlaXJhIG3DqWRpYSAkXFxtdV9pJCwgdG9ybmFuZG8gYSBlc3RpbWF0aXZhIG1haXMgcHJlY2lzYSBlIHJlZHV6aW5kbyBhIGFtcGxpdHVkZSBkbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBwYXJhIGEgY29tcGFyYcOnw6NvIGVudHJlIGRvaXMgdHJhdGFtZW50b3MuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIGNhbXBvLCB1bSBwZXNxdWlzYWRvciBjb21wYXJvdSAzIHRpcG9zIGRlIGZlcnRpbGl6YW50ZXMgKCRUXzEsIFRfMiwgVF8zJCkgZW0gNCBibG9jb3MgZGlzdGludG9zLiBBIHNvbWEgZGUgcXVhZHJhZG9zIGRvcyB0cmF0YW1lbnRvcyBmb2kgJFNRVHJhdCA9IDEwNjAuNyQgZSBhIHNvbWEgZGUgcXVhZHJhZG9zIGRvIGVycm8gZm9pICRTUUUgPSAxMy4zJC4gQ2FsY3VsZSBhIGVzdGF0w61zdGljYSAkRl97Y2FsY30kIHBhcmEgdGVzdGFyIGEgaGlww7N0ZXNlIG51bGEgZGUgaWd1YWxkYWRlIGRhcyBtw6lkaWFzIGRvcyB0cmF0YW1lbnRvcy4gTW9zdHJlIG9zIHBhc3NvcyBkZSBjw6FsY3VsbyBkb3MgZ3JhdXMgZGUgbGliZXJkYWRlIGUgZG9zIHF1YWRyYWRvcyBtw6lkaW9zLiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgJFFNVHJhdCA9IFxcZnJhY3tTUVRyYXR9e2stMX0kIGUgJFFNUmVzID0gXFxmcmFje1NRRX17KGstMSkoYi0xKX0kLiBBIGVzdGF0w61zdGljYSAkRiQgw6kgYSByYXrDo28gJFFNVHJhdCAvIFFNUmVzJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogSWRlbnRpZmljYXIgb3MgcGFyw6JtZXRyb3MuICRrID0gMyQgKHRyYXRhbWVudG9zKSBlICRiID0gNCQgKGJsb2NvcykuIiwgIlBhc3NvIDI6IENhbGN1bGFyIG9zIGdyYXVzIGRlIGxpYmVyZGFkZS4gJGdsX3t0cmF0fSA9IGsgLSAxID0gMyAtIDEgPSAyJC4gJGdsX3tyZXN9ID0gKGstMSkoYi0xKSA9IDIgXFx0aW1lcyAzID0gNiQuIiwgIlBhc3NvIDM6IENhbGN1bGFyIG9zIHF1YWRyYWRvcyBtw6lkaW9zLiAkUU1UcmF0ID0gXFxmcmFjezEwNjAuN317Mn0gPSA1MzAuMzUkLiAkUU1SZXMgPSBcXGZyYWN7MTMuM317Nn0gXFxhcHByb3ggMi4yMTY3JC4iLCAiUGFzc28gNDogQ2FsY3VsYXIgYSBlc3RhdMOtc3RpY2EgJEZfe2NhbGN9ID0gXFxmcmFjezUzMC4zNX17Mi4yMTY3fSBcXGFwcHJveCAyMzkuMjUkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIk7DrXZlYSBCaXNwbywgQXVsYSAxNzogSW50cm9kdcOnw6NvIMOgIEFOT1ZBIG5vcyBkZWxpbmVhbWVudG9zIGFtb3N0cmFpcywgcC4gMTgiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAyMzkuMjV9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgw7N0aWNhIGRvIGNvbnRyb2xlIGxvY2FsLCBwb3IgcXVlIG5vIERlbGluZWFtZW50byBlbSBCbG9jb3MgQ29tcGxldG9zIENhc3VhbGl6YWRvcyAoREJDKSwgbyB0ZXJtbyBkZSBlcnJvIGV4cGVyaW1lbnRhbCAoJFNRRSQpIHRlbmRlIGEgc2VyIG1lbm9yIGRvIHF1ZSBubyBEZWxpbmVhbWVudG8gSW50ZWlyYW1lbnRlIGFvIEFjYXNvIChESUMpIHF1YW5kbyBow6EgdW1hIHZhcmlhw6fDo28gYW1iaWVudGFsIHNpc3RlbcOhdGljYSAoY29tbyB1bSBkZWNsaXZlIG5vIHRlcnJlbm8pLiIsICJkaWNhIjogIlBlbnNlIG5hIGRlY29tcG9zacOnw6NvIGRhIHZhcmnDom5jaWEgdG90YWwuIE5vIERJQywgdG9kYSBhIHZhcmlhw6fDo28gbsOjbyBhdHJpYnXDrWRhIGFvcyB0cmF0YW1lbnRvcyDDqSBpbmNvcnBvcmFkYSBhbyByZXPDrWR1by4gTm8gREJDLCBwYXJ0ZSBkZXNzYSB2YXJpYcOnw6NvIMOpIGNhcHR1cmFkYSBwZWxvIGVmZWl0byBkb3MgYmxvY29zICgkXFxiZXRhX2okKS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gTm8gRElDLCBhIHZhcmnDom5jaWEgdG90YWwgw6kgZGVjb21wb3N0YSBjb21vICRTUVQgPSBTUVRyYXQgKyBTUUVfe0RJQ30kLiIsICIyLiBObyBEQkMsIGEgdmFyacOibmNpYSB0b3RhbCDDqSBkZWNvbXBvc3RhIGNvbW8gJFNRVCA9IFNRVHJhdCArIFNRQmwgKyBTUUVfe0RCQ30kLiIsICIzLiBDb21vIG8gYmxvcXVlYW1lbnRvIG9yZ2FuaXphIGFzIHVuaWRhZGVzIGVtIGdydXBvcyBob21vZ8OqbmVvcywgZWxlIGlzb2xhIGEgdmFyaWFiaWxpZGFkZSBjYXVzYWRhIHBlbG8gYW1iaWVudGUgKGNvbW8gdW0gZGVjbGl2ZSkgbmEgZm9udGUgZGUgdmFyaWHDp8OjbyAnQmxvY29zJy4iLCAiNC4gQ29uc2VxdWVudGVtZW50ZSwgbyBlcnJvIGV4cGVyaW1lbnRhbCAkU1FFX3tEQkN9JCBzZXLDoSAkU1FFX3tESUN9IC0gU1FCbCQsIHJlZHV6aW5kbyBvIGVycm8gZSBhdW1lbnRhbmRvIGEgc2Vuc2liaWxpZGFkZSBkbyB0ZXN0ZSBlc3RhdMOtc3RpY28gKG8gZGVub21pbmFkb3IgZGEgZXN0YXTDrXN0aWNhICRGJCBkaW1pbnVpKS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJOw612ZWEgQmlzcG8sIEF1bGEgMTc6IEludHJvZHXDp8OjbyDDoCBBTk9WQSBub3MgZGVsaW5lYW1lbnRvcyBhbW9zdHJhaXMsIHAuIDE0IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyYW5kbyBvIGV4ZW1wbG8gZG8gZmVydGlsaXphbnRlIGVtIHNvamEgY29tICRRTVJlcyA9IDIuMiQgZSAkYj00JCBibG9jb3MsIGNhbGN1bGUgYSBkaWZlcmVuw6dhIG3DrW5pbWEgc2lnbmlmaWNhdGl2YSAoJFxcRGVsdGEkKSBwYXJhIG8gdGVzdGUgZGUgVHVrZXkgYW8gbsOtdmVsIGRlIDUlLCBzYWJlbmRvIHF1ZSBvIHZhbG9yIHRhYmVsYWRvIGRlICRxX3tcXGFscGhhfSQgcGFyYSAkaz0zJCBlICRnbF97cmVzfT02JCDDqSBhcHJveGltYWRhbWVudGUgNC4zNC4gQ29tbyBlc3NhIGRpZmVyZW7Dp2EgJFxcRGVsdGEkIGRldmUgc2VyIGludGVycHJldGFkYSBhbyBjb21wYXJhciBhcyBtw6lkaWFzIGRlIGRvaXMgdHJhdGFtZW50b3M/IiwgImRpY2EiOiAiQSBmw7NybXVsYSBmb3JuZWNpZGEgcGVsbyBwcm9mZXNzb3IgcGFyYSBvIHRlc3RlIGRlIFR1a2V5IG5vIERCQyDDqSAkXFxEZWx0YSA9IHFfe1xcYWxwaGF9IFxcc3FydHtcXGZyYWN7UU1SZXN9e2J9fSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIElkZW50aWZpY2FyIG9zIHZhbG9yZXM6ICRxX3tcXGFscGhhfSA9IDQuMzQkLCAkUU1SZXMgPSAyLjIkLCAkYiA9IDQkLiIsICIyLiBTdWJzdGl0dWlyIG5hIGbDs3JtdWxhOiAkXFxEZWx0YSA9IDQuMzQgXFx0aW1lcyBcXHNxcnR7XFxmcmFjezIuMn17NH19JC4iLCAiMy4gQ2FsY3VsYXIgbyB0ZXJtbyBpbnRlcm5vOiAkXFxzcXJ0ezAuNTV9IFxcYXBwcm94IDAuNzQxNiQuIiwgIjQuIENhbGN1bGFyIG8gcHJvZHV0bzogJFxcRGVsdGEgPSA0LjM0IFxcdGltZXMgMC43NDE2IFxcYXBwcm94IDMuMjE4JC4iLCAiNS4gSW50ZXJwcmV0YcOnw6NvOiBTZSBhIGRpZmVyZW7Dp2EgYWJzb2x1dGEgZW50cmUgYXMgbcOpZGlhcyBkZSBkb2lzIHRyYXRhbWVudG9zICR8XGJhcntUX2l9IC0gXGJhcntUX2p9fCQgZm9yIHN1cGVyaW9yIGEgMy4yMTgsIGVsZXMgc8OjbyBjb25zaWRlcmFkb3MgZXN0YXRpc3RpY2FtZW50ZSBkaWZlcmVudGVzIGFvIG7DrXZlbCBkZSA1JS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJOw612ZWEgQmlzcG8sIEF1bGEgMTg6IEludHJvZHXDp8OjbyDDoCBBTk9WQSBub3MgZGVsaW5lYW1lbnRvcyBhbW9zdHJhaXMsIHAuIDIiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAzLjIxOH0sIHsiZW51bmNpYWRvIjogIlVtIGV4cGVyaW1lbnRvIGVtIERCQyBjb20gMyBibG9jb3MgZSA0IHRyYXRhbWVudG9zIGFwcmVzZW50b3UgdW0gJFFNX3tSZXMoREJDKX0gPSAxMCwwJC4gTyBwZXNxdWlzYWRvciBkZXNlamEgY2FsY3VsYXIgYSBlZmljacOqbmNpYSByZWxhdGl2YSBjb21wYXJhbmRvIGVzdGUgZGVzZW5obyBjb20gdW0gZGVsaW5lYW1lbnRvIGludGVpcmFtZW50ZSBjYXN1YWxpemFkbyAoRElDKS4gU2FiZW5kbyBxdWUgYSBzb21hIGRvcyBxdWFkcmFkb3MgZG8gZXJybyBubyBEQkMgw6kgNjAsMCBlIHF1ZSBvICRRTV97UmVzKERJQyl9JCDDqSBjYWxjdWxhZG8gY29tbyBhIHNvbWEgZGFzIHNvbWFzIGRlIHF1YWRyYWRvcyBkb3MgYmxvY29zIGUgZG8gcmVzw61kdW8sIGRpdmlkaWRhIHBlbG8gdG90YWwgZGUgZ3JhdXMgZGUgbGliZXJkYWRlLCBhc3N1bWluZG8gcXVlIGEgc29tYSBkb3MgcXVhZHJhZG9zIGRvcyBibG9jb3MgZm9pIDMwLDAsIGNhbGN1bGUgYSAkRVIkLiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgJFFNX3tSZXMoRElDKX0gPSAoU1Ffe0Jsb2NvfSArIFNRX3tSZXN9KSAvIChnbF97VHJhdH0gKyBnbF97UmVzfSkkLiBDYWxjdWxlICRTUV97UmVzfSQgdXNhbmRvICRRTV97UmVzfSBcXGNkb3QgZ2xfe1Jlc30kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiBJZGVudGlmaWNhciBncmF1cyBkZSBsaWJlcmRhZGU6ICRnbF97VHJhdH0gPSA0LTEgPSAzJCwgJGdsX3tCbG9jb30gPSAzLTEgPSAyJCwgJGdsX3tSZXN9ID0gKDQtMSkoMy0xKSA9IDYkLiIsICJQYXNzbyAyOiBDYWxjdWxhciAkU1Ffe1Jlc30gPSBRTV97UmVzKERCQyl9IFxcY2RvdCBnbF97UmVzfSA9IDEwLDAgXFxjZG90IDYgPSA2MCwwJC4iLCAiUGFzc28gMzogQ2FsY3VsYXIgJFFNX3tSZXMoRElDKX0gPSAoU1Ffe0Jsb2NvfSArIFNRX3tSZXN9KSAvIChnbF97VHJhdH0gKyBnbF97UmVzfSkgPSAoMzAsMCArIDYwLDApIC8gKDMgKyA2KSA9IDkwIC8gOSA9IDEwLDAkLiIsICJQYXNzbyA0OiBBcGxpY2FyIGbDs3JtdWxhICRFUiA9IFxcZnJhY3soNisxKSg5KzMpfXsoOSsxKSg2KzMpfSBcXGNkb3QgXFxmcmFjezEwLDB9ezEwLDB9ID0gXFxmcmFjezcgXFxjZG90IDEyfXsxMCBcXGNkb3QgOX0gPSA4NCAvIDkwID0gMCw5MzMkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC45MzN9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSBvIGltcGFjdG8gZG8gYmxvcXVlYW1lbnRvIG5hIHZhcmlhYmlsaWRhZGUgcmVzaWR1YWwgZGUgdW0gZXhwZXJpbWVudG8uIFNlIHVtIGV4cGVyaW1lbnRvIGVtIERCQyBhcHJlc2VudGEgdW0gJEZfe2NhbGN9JCBwYXJhIG8gZWZlaXRvIGRlIGJsb2NvIHNpZ25pZmljYXRpdmFtZW50ZSBtYWlvciBxdWUgbyAkRl97Y3JpdH0kLCBvIHF1ZSBpc3NvIG5vcyBkaXogc29icmUgYSBwcmVjaXPDo28gZXhwZXJpbWVudGFsIGFsY2Fuw6dhZGE/IiwgImRpY2EiOiAiQ29uc2lkZXJlIHF1ZSBhIGRlY29tcG9zacOnw6NvIGRhIHZhcmnDom5jaWEgbm8gREJDIGlzb2xhIG8gZWZlaXRvIGRvcyBibG9jb3MsIHJlbW92ZW5kby1vIGRvIGVycm8gcmVzaWR1YWwuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgYmxvY2FnZW0gw6kgdW1hIHTDqWNuaWNhIGRlIGNvbnRyb2xlIGxvY2FsIHBhcmEgcmVkdXppciBvIGVycm8gZXhwZXJpbWVudGFsLiIsICJBbyBzZXBhcmFyIGEgdmFyaWHDp8OjbyBkb3MgYmxvY29zICgkU1Ffe0Jsb2NvfSQpLCBlbGEgbsOjbyBjb21ww7VlIG1haXMgbyBlcnJvIHJlc2lkdWFsICgkU1Ffe1Jlc30kKSwgcmVzdWx0YW5kbyBlbSB1bSAkUU1fe1Jlc30kIG1lbm9yLiIsICJTZSAkRl97Y2FsY30gPiBGX3tjcml0fSQgcGFyYSBibG9jb3MsIGluZGljYSBxdWUgYSBoZXRlcm9nZW5laWRhZGUgZG8gc29sbyBmb2kgc2lnbmlmaWNhdGl2YSBlIHF1ZSBvIGJsb3F1ZWFtZW50byBjb25zZWd1aXUgaXNvbGFyIGVzc2EgdmFyaWHDp8OjbyBjb20gc3VjZXNzby4iLCAiQ29tbyBjb25zZXF1w6puY2lhLCBhIHByZWNpc8OjbyBkbyBleHBlcmltZW50byDDqSBhdW1lbnRhZGEsIHBlcm1pdGluZG8gcXVlIG8gdGVzdGUgRiBwYXJhIHRyYXRhbWVudG9zIHNlamEgbWFpcyBzZW5zw612ZWwuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTsOtdmVhIEJpc3BvLCBBdWxhIDE3LzE4LCBERVNULVVGQkEgMjAyNS4xIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkRhZGEgdW1hIG3DqWRpYSBnZXJhbCBkZSA1MCwwIGUgdW0gJFFNX3tSZXMoREJDKX0gPSAyNSwwJCwgY2FsY3VsZSBvIGNvZWZpY2llbnRlIGRlIHZhcmlhw6fDo28gKCRDViQpIGUgaW50ZXJwcmV0ZSBvIG7DrXZlbCBkZSBwcmVjaXPDo28gb2J0aWRvIHNlZ3VuZG8gYSBtZXRvZG9sb2dpYSBhY2Fkw6ptaWNhIGFwcmVzZW50YWRhLiIsICJkaWNhIjogIlVzZSBhIGbDs3JtdWxhICRDViA9IChcXHNxcnR7UU1fe1Jlc319IC8gXFxiYXJ7WH1fey4ufSkgXFx0aW1lcyAxMDAkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiBDYWxjdWxhciBvIGRlc3ZpbyBwYWRyw6NvICRTID0gXFxzcXJ0ezI1LDB9ID0gNSwwJC4iLCAiUGFzc28gMjogQ2FsY3VsYXIgbyAkQ1YgPSAoNSwwIC8gNTAsMCkgXFx0aW1lcyAxMDAkLiIsICJQYXNzbyAzOiBSZWFsaXphciBvIGPDoWxjdWxvOiAkQ1YgPSAwLDEgXFxjZG90IDEwMCA9IDEwXFwlJC4iLCAiUGFzc28gNDogSW50ZXJwcmV0YcOnw6NvOiBDb21vICRDViA9IDEwXFwlJCwgbyBleHBlcmltZW50byBhcHJlc2VudGEgw7N0aW1hIHByZWNpc8OjbyBleHBlcmltZW50YWwuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAxMC4wfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtIGV4cGVyaW1lbnRvIGRlIERRTCBwYXJhIGF2YWxpYXIgNCBsaW5oYWdlbnMgZGUgc29qYSBlbSB1bSBzb2xvIGNvbSBncmFkaWVudGUgTm9ydGUtU3VsIGUgTGVzdGUtT2VzdGUuIEEgdGFiZWxhIEFOT1ZBIHJlc3VsdGFudGUgYXByZXNlbnRvdSBhcyBzZWd1aW50ZXMgc29tYXMgZGUgcXVhZHJhZG9zOiAkU1FUID0gMjQwJCwgJFNRX3tsaW5oYXN9ID0gNDAkLCAkU1Ffe2NvbHVuYXN9ID0gNjAkLCAkU1Ffe3RyYXRhbWVudG9zfSA9IDgwJC4gQ2FsY3VsZSBhIGVzdGF0w61zdGljYSAkRl97XFx0ZXh0e2NhbGN9fSQgcGFyYSBvIHRlc3RlIGRlIHNpZ25pZmljw6JuY2lhIGRvcyB0cmF0YW1lbnRvcy4iLCAiZGljYSI6ICJDYWxjdWxlIHByaW1laXJvIGEgJFNRRSQgKFNvbWEgZGUgUXVhZHJhZG9zIGRvIEVycm8pIHN1YnRyYWluZG8gYXMgb3V0cmFzIGZvbnRlcyBkYSAkU1FUJC4gRW0gc2VndWlkYSwgb2J0ZW5oYSBvcyBxdWFkcmFkb3MgbcOpZGlvcyBkaXZpZGluZG8gcGVsYXMgcmVzcGVjdGl2YXMgJGdsJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYXIgb3MgZ3JhdXMgZGUgbGliZXJkYWRlOiAkcj00JC4gJGdsX3t0cmF0fSA9IDMkLCAkZ2xfe2xpbmhhc30gPSAzJCwgJGdsX3tjb2x9ID0gMyQuICRnbF97ZXJyb30gPSAoci0xKShyLTIpID0gMyBcXHRpbWVzIDIgPSA2JC4iLCAiMi4gQ2FsY3VsYXIgYSAkU1FFJDogJFNRRSA9IFNRVCAtIChTUV97bGluaGFzfSArIFNRX3tjb2x1bmFzfSArIFNRX3t0cmF0YW1lbnRvc30pID0gMjQwIC0gKDQwICsgNjAgKyA4MCkgPSAyNDAgLSAxODAgPSA2MCQuIiwgIjMuIENhbGN1bGFyIG9zIFF1YWRyYWRvcyBNw6lkaW9zOiAkUU1fe3RyYXR9ID0gU1Ffe3RyYXR9IC8gZ2xfe3RyYXR9ID0gODAgLyAzIFxcYXBwcm94IDI2LjY3JC4gJFFNX3tlcnJvfSA9IFNRRSAvIGdsX3tlcnJvfSA9IDYwIC8gNiA9IDEwJC4iLCAiNC4gQ2FsY3VsYXIgJEZfe1xcdGV4dHtjYWxjfX0gPSBRTV97dHJhdH0gLyBRTV97ZXJyb30gPSAyNi42NyAvIDEwID0gMi42NjckLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMi42Njd9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgw7N0aWNhIGRvIHJpZ29yIGV4cGVyaW1lbnRhbCwgcG9yIHF1ZSBvIGFjcsOpc2NpbW8gZGUgdHJhdGFtZW50b3MgZW0gdW0gRFFMIGNhdXNhIHVtYSByZXN0cmnDp8OjbyBwcsOhdGljYSBubyBkZXNlbmhvIGRvIGV4cGVyaW1lbnRvLCBlc3BlY2lhbG1lbnRlIHF1YW5kbyBjb21wYXJhZG8gYSB1bSBESUMgKERlbGluZWFtZW50byBJbnRlaXJhbWVudGUgQ2FzdWFsaXphZG8pLiIsICJkaWNhIjogIlJlZmxpdGEgc29icmUgYSByZWxhw6fDo28gZW50cmUgbyBuw7ptZXJvIGRlIHRyYXRhbWVudG9zIGUgbyBuw7ptZXJvIGRlIHBhcmNlbGFzIGV4cGVyaW1lbnRhaXMgbmVjZXNzw6FyaWFzIGVtIHVtIGFycmFuam8gJHIgXFx0aW1lcyByJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiTm8gRFFMLCBhIGVzdHJ1dHVyYSDDqSB1bWEgbWF0cml6IHF1YWRyYWRhIGRlIG9yZGVtICRyIFxcdGltZXMgciQuIiwgIk8gbsO6bWVybyB0b3RhbCBkZSB1bmlkYWRlcyBleHBlcmltZW50YWlzIG5lY2Vzc8OhcmlhcyDDqSAkbiA9IHJeMiQuIiwgIkVucXVhbnRvIG5vIERJQyBvIG7Dum1lcm8gZGUgcmVwZXRpw6fDtWVzIHBvZGUgc2VyIGZsZXhpYmlsaXphZG8gcGFyYSBxdWFscXVlciB2YWxvciAkbiQgY29uZm9ybWUgYSBkaXNwb25pYmlsaWRhZGUgZGUgcmVjdXJzb3MsIG5vIERRTCwgc2UgbyBuw7ptZXJvIGRlIHRyYXRhbWVudG9zICRyJCBhdW1lbnRhLCBvIG7Dum1lcm8gZGUgdW5pZGFkZXMgY3Jlc2NlIHF1YWRyYXRpY2FtZW50ZS4iLCAiUG9yIGV4ZW1wbG8sIHBhcmEgJHI9MyQgc8OjbyA5IHBhcmNlbGFzLCBwYXJhICRyPTUkIHPDo28gMjUsIGUgcGFyYSAkcj0xMCQgc2VyaWFtIDEwMCBwYXJjZWxhcywgdG9ybmFuZG8gbyBkZWxpbmVhbWVudG8gbXVpdG8gb25lcm9zbyBlIGRpZsOtY2lsIGRlIGNvbmR1emlyIGVtIGNhbXBvLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkRhZG8gbyBtb2RlbG8gbGluZWFyICR5X3tpamt9ID0gXFxtdSArIFxcdGF1X2sgKyBMX2kgKyBDX2ogKyBlX3tpamt9JCwgZGVzY3JldmEgbyBwYXBlbCBkbyB0ZXJtbyAkZV97aWprfSQgZSBjb21vIGEgdMOpY25pY2EgZGUgZHVwbG8gYmxvcXVlYW1lbnRvIGRvIERRTCBhdHVhIHNvYnJlIGEgdmFyacOibmNpYSBkZXNzZSB0ZXJtby4iLCAiZGljYSI6ICJQZW5zZSBubyBwYXJ0aWNpb25hbWVudG8gZGEgdmFyaWHDp8OjbyB0b3RhbCBlIGNvbW8gbyBjb250cm9sZSBsb2NhbCByZWR1eiBhIGluY2VydGV6YSBleHBlcmltZW50YWwuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIk8gdGVybW8gJGVfe2lqa30kIHJlcHJlc2VudGEgYSB2YXJpYWJpbGlkYWRlIGFsZWF0w7NyaWEgbsOjbyBleHBsaWNhZGEgcGVsb3MgdHJhdGFtZW50b3MsIGxpbmhhcyBvdSBjb2x1bmFzLiIsICJObyBEUUwsIG8gY29udHJvbGUgbG9jYWwgZGUgbGluaGFzICgkTF9pJCkgZSBjb2x1bmFzICgkQ19qJCkgcmV0aXJhIGRhIHNvbWEgZGUgcXVhZHJhZG9zIHRvdGFsIGFzIHZhcmlhw6fDtWVzIGNhdXNhZGFzIHBvciBncmFkaWVudGVzIHNpc3RlbcOhdGljb3MgKGNvbW8gZmVydGlsaWRhZGUgZSBkcmVuYWdlbSkuIiwgIkNvbnNlcXVlbnRlbWVudGUsIGEgdmFyacOibmNpYSByZXNpZHVhbCBkbyBlcnJvIGV4cGVyaW1lbnRhbCAkZV97aWprfSQgw6kgcmVkdXppZGEsIHBvaXMgZmF0b3JlcyBhbnRlcyBjb25mdW5kaWRvcyBjb20gbyBlcnJvIHPDo28gYWdvcmEgZXhwbGljYWRvcyBwZWxhcyBsaW5oYXMgZSBjb2x1bmFzLiIsICJJc3NvIHJlc3VsdGEgZW0gdW0gdGVzdGUgZGUgaGlww7N0ZXNlcyBtYWlzIHNlbnPDrXZlbCAobWFpb3IgcG9kZXIpIHBhcmEgZGV0ZWN0YXIgZGlmZXJlbsOnYXMgZW50cmUgb3MgdHJhdGFtZW50b3MgJFxcdGF1X2skLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKTsgZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9WzEsIDIsIDMsIDRdLCB5PVsxMCwgMTIsIDExLCAxNV0sIG1vZGU9J2xpbmVzK21hcmtlcnMnLCBsaW5lPWRpY3QoY29sb3I9JyM2NzhhZTgnLCB3aWR0aD0zKSkpOyBmaWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+UmVkdcOnw6NvIGRhIFZhcmlhYmlsaWRhZGUgUmVzaWR1YWw8L2I+JywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScsIHhheGlzPWRpY3QodGl0bGU9J1RyYXRhbWVudG8nLCBmaXhlZHJhbmdlPVRydWUpLCB5YXhpcz1kaWN0KHRpdGxlPSdSZXNwb3N0YSAoJHlfe2lqa30kKScsIGZpeGVkcmFuZ2U9VHJ1ZSkpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW0gcGVzcXVpc2Fkb3IgbW9udG91IHVtIERRTCAkNSBcXHRpbWVzIDUkIHBhcmEgY29tcGFyYXIgY2luY28gdGlwb3MgZGUgZGVmZW5zaXZvcyBhZ3LDrWNvbGFzLiBBIHNvbWEgZGUgcXVhZHJhZG9zIHRvdGFsIGZvaSAkU1FUID0gNDUwJC4gQXMgc29tYXMgZGUgcXVhZHJhZG9zIGRhcyBmb250ZXMgZm9yYW06ICRTUUwgPSA4MCQsICRTUUMgPSA2MCQgZSAkU1FUcmF0ID0gMjEwJC4gQ2FsY3VsZSBhIHZhcmnDom5jaWEgcmVzaWR1YWwgKCRTXjIgPSBRTVJlcyQpIGUgbyBjb2VmaWNpZW50ZSBkZSB2YXJpYcOnw6NvICgkQ1ZcXCUkKSwgc2FiZW5kbyBxdWUgYSBtw6lkaWEgZ2xvYmFsIGRhIHByb2R1dGl2aWRhZGUgZm9pICRcXGJhcnt5fSA9IDE1MCBcXCwga2cvaGEkLiIsICJkaWNhIjogIkNhbGN1bGUgcHJpbWVpcm8gYSAkU1FSZXMgPSBTUVQgLSBTUUwgLSBTUUMgLSBTUVRyYXQkIGUgZW5jb250cmUgb3MgZ3JhdXMgZGUgbGliZXJkYWRlIGRvIHJlc8OtZHVvIHBhcmEgb2J0ZXIgbyAkUU1SZXMkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBDw6FsY3VsbyBkYSBzb21hIGRlIHF1YWRyYWRvcyBkbyByZXPDrWR1bzogJCRTUVJlcyA9IFNRVCAtIFNRTCAtIFNRQyAtIFNRVHJhdCA9IDQ1MCAtIDgwIC0gNjAgLSAyMTAgPSAxMDAkJC4iLCAiMi4gRGV0ZXJtaW5hw6fDo28gZG9zIGdyYXVzIGRlIGxpYmVyZGFkZSBkbyByZXPDrWR1byBwYXJhICRyPTUkOiAkJGdsX3tSZXN9ID0gKHItMSkoci0yKSA9ICg1LTEpKDUtMikgPSA0IFxcdGltZXMgMyA9IDEyJCQuIiwgIjMuIEPDoWxjdWxvIGRvIHF1YWRyYWRvIG3DqWRpbyBkbyByZXPDrWR1byAodmFyacOibmNpYSByZXNpZHVhbCk6ICQkUU1SZXMgPSBcXGZyYWN7U1FSZXN9e2dsX3tSZXN9fSA9IFxcZnJhY3sxMDB9ezEyfSBcXGFwcHJveCA4LDMzJCQuIiwgIjQuIEPDoWxjdWxvIGRvIGRlc3ZpbyBwYWRyw6NvIGV4cGVyaW1lbnRhbDogJCRTID0gXFxzcXJ0e1FNUmVzfSA9IFxcc3FydHs4LDMzfSBcXGFwcHJveCAyLDg5JCQuIiwgIjUuIEPDoWxjdWxvIGRvIGNvZWZpY2llbnRlIGRlIHZhcmlhw6fDo286ICQkQ1ZcXCUgPSBcXGxlZnQoIFxcZnJhY3tTfXtcXGJhcnt5fX0gXFxyaWdodCkgXFx0aW1lcyAxMDAgPSBcXGxlZnQoIFxcZnJhY3syLDg5fXsxNTB9IFxccmlnaHQpIFxcdGltZXMgMTAwIFxcYXBwcm94IDEsOTNcXCUkJC4gSW50ZXJwcmV0YW5kbyBvIHZhbG9yLCBvIGV4cGVyaW1lbnRvIGFwcmVzZW50b3UgZXhjZWxlbnRlIHByZWNpc8Ojby4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDEuOTN9LCB7ImVudW5jaWFkbyI6ICJQcm92ZSBhbGdlYnJpY2FtZW50ZSwgYSBwYXJ0aXIgZGFzIHJlc3RyacOnw7VlcyAkXFxzdW1fe2s9MX1ee3J9IFxcdGF1X2sgPSAwJCwgJFxcc3VtX3tpPTF9XntyfSBMX2kgPSAwJCBlICRcXHN1bV97aj0xfV57cn0gQ19qID0gMCQsIHF1ZSBvIGVzdGltYWRvciBkZSBtw61uaW1vcyBxdWFkcmFkb3MgcGFyYSBhIG3DqWRpYSBnbG9iYWwgZW0gdW0gRFFMIGJhbGFuY2VhZG8gw6ksIGRlIGZhdG8sIGEgbcOpZGlhIGFyaXRtw6l0aWNhIHNpbXBsZXMgZGFzIG9ic2VydmHDp8O1ZXMgKCRcXGJhcnt5fV97Li4ufSQpLiIsICJkaWNhIjogIlV0aWxpemUgYSBtaW5pbWl6YcOnw6NvIGRhIHNvbWEgZGUgcXVhZHJhZG9zIGRvcyByZXPDrWR1b3MgJFNRRSA9IFxcc3VtX3tpfSBcXHN1bV97an0gKHlfe2lqfSAtIFxcbXUgLSBcXHRhdV9rIC0gTF9pIC0gQ19qKV4yJCBlIGNvbnNpZGVyZSBhIG5hdHVyZXphIGJhbGFuY2VhZGEgZG8gZGVzaWduIG9uZGUgY2FkYSB0cmF0YW1lbnRvIGFwYXJlY2UgdW1hIHZleiBwb3IgbGluaGEgZSBjb2x1bmEuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIERlZmluYSBhIGZ1bsOnw6NvIGEgc2VyIG1pbmltaXphZGE6ICQkZihcXG11LCBcXHRhdSwgTCwgQykgPSBcXHN1bSBcXHN1bSAoeV97aWp9IC0gXFxtdSAtIFxcdGF1X2sgLSBMX2kgLSBDX2opXjIkJC4iLCAiMi4gRGVyaXZlIGVtIHJlbGHDp8OjbyBhICRcXG11JDogJCRcXGZyYWN7XFxwYXJ0aWFsIGZ9e1xccGFydGlhbCBcXG11fSA9IC0yIFxcc3VtIFxcc3VtICh5X3tpan0gLSBcXG11IC0gXFx0YXVfayAtIExfaSAtIENfaikgPSAwJCQuIiwgIjMuIEV4cGFuZGEgbyBzb21hdMOzcmlvOiAkJFxcc3VtIFxcc3VtIHlfe2lqfSAtIHJeMiBcXG11IC0gciBcXHN1bSBcXHRhdV9rIC0gciBcXHN1bSBMX2kgLSByIFxcc3VtIENfaiA9IDAkJC4iLCAiNC4gQXBsaXF1ZSBhcyByZXN0cmnDp8O1ZXMgZGUgc29tYSBudWxhOiAkXFxzdW0gXFx0YXVfayA9IDAkLCAkXFxzdW0gTF9pID0gMCQsICRcXHN1bSBDX2ogPSAwJC4iLCAiNS4gQSBlcXVhw6fDo28gcmVkdXotc2UgYTogJCRcXHN1bSBcXHN1bSB5X3tpan0gLSByXjIgXFxtdSA9IDAkJCwgbG9nbyAkJFxcbXUgPSBcXGZyYWN7XFxzdW0gXFxzdW0geV97aWp9fXtyXjJ9ID0gXFxiYXJ7eX1fey4uLn0kJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBEUUwgJDQgXFx0aW1lcyA0JCwgbyBwZXNxdWlzYWRvciBkZXNlamEgdGVzdGFyIHNlIG8gdHJhdGFtZW50byBBIChDb250cm9sZSkgZGlmZXJlIGRvcyBkZW1haXMgdHJhdGFtZW50b3MgKEIsIEMsIEQpLiBTZSAkU1FUcmF0ID0gMTIwJCBjb20gMyBncmF1cyBkZSBsaWJlcmRhZGUsIGNvbnN0cnVhIG8gdGVzdGUgcGFyYSBvIGNvbnRyYXN0ZSBkZSBEdW5uZXR0IG91IHVtIGNvbnRyYXN0ZSBvcnRvZ29uYWwgZXF1aXZhbGVudGUsIGFzc3VtaW5kbyBxdWUgYSBzb21hIGRlIHF1YWRyYWRvcyBkbyByZXPDrWR1byDDqSAkU1FSZXMgPSAyNCQgY29tICRnbF97UmVzfSA9IDYkLiBRdWFsIMOpIG8gdmFsb3IgZGEgZXN0YXTDrXN0aWNhICRGJCBwYXJhIGVzdGUgdGVzdGUgZGUgY29udHJhc3RlPyIsICJkaWNhIjogIlBhcmEgdW0gY29udHJhc3RlIGRlIGNvbXBhcmHDp8OjbyBzaW1wbGVzLCBhIHNvbWEgZGUgcXVhZHJhZG9zIGRvIGNvbnRyYXN0ZSDDqSBkYWRhIHBvciAkU1Ffe0NvbnRyYXN0ZX0gPSBcXGZyYWN7KFxcc3VtIGNfaSBcXGJhcnt5fV9pKV4yfXtcXHN1bSBjX2leMiAvIHJfaX0kLiBMZW1icmUtc2UgcXVlICRRTVJlcyQgw6kgbyBkZW5vbWluYWRvciBkbyB0ZXN0ZSBGLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBDYWxjdWxlIGEgdmFyacOibmNpYSByZXNpZHVhbDogJCRRTVJlcyA9IFxcZnJhY3tTUVJlc317Z2xfe1Jlc319ID0gXFxmcmFjezI0fXs2fSA9IDQkJC4iLCAiMi4gSWRlbnRpZmlxdWUgcXVlIHVtIGNvbnRyYXN0ZSBkZSBjb21wYXJhw6fDo28gZW50cmUgdW0gY29udHJvbGUgZSBvcyBkZW1haXMgcG9zc3VpICQxJCBncmF1IGRlIGxpYmVyZGFkZS4iLCAiMy4gU3Vwb25oYSBxdWUsIGEgcGFydGlyIGRvcyBkYWRvcywgbyBjb250cmFzdGUgJEMkIHJlc3VsdG91IGVtICRTUV97Q29udHJhc3RlfSA9IDE2JC4iLCAiNC4gQ2FsY3VsZSBvICRRTV97Q29udHJhc3RlfSA9IFxcZnJhY3tTUV97Q29udHJhc3RlfX17MX0gPSAxNiQuIiwgIjUuIENhbGN1bGUgYSBlc3RhdMOtc3RpY2EgJEYkOiAkJEZfe2NhbGN9ID0gXFxmcmFje1FNX3tDb250cmFzdGV9fXtRTVJlc30gPSBcXGZyYWN7MTZ9ezR9ID0gNCQkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogNC4wfV19').decode('utf-8'))


    import streamlit as st
    import plotly.graph_objects as go
    
    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do total de exercícios
    mcq_list = dados_exercicios.get("questoes_multipla_escolha", [])
    disc_list = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcq_list) + len(disc_list)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    # Interface de progresso
    st.markdown("### 🎯 Progresso do Estudo")
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso:** {acertos} de {total_exercicios} desafios concluídos!")
    else:
        st.info("Nenhum exercício carregado.")
    
    st.divider()
    
    # Seção de Questões de Múltipla Escolha
    if mcq_list:
        st.header("📝 Questões de Múltipla Escolha")
        for i, questao in enumerate(mcq_list):
            with st.container(border=True):
                st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
                
                # Referência Bibliográfica
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
    
                # Renderização de Gráfico Plotly
                codigo = questao.get("codigo_plotly")
                if codigo:
                    local_vars = {"go": go}
                    try:
                        exec(codigo, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_chart_mcq_{i}")
                    except Exception as e:
                        st.warning("Não foi possível renderizar o gráfico.")
    
                # Alternativas
                opcoes = questao.get("alternativas", {})
                escolha = st.radio(
                    "Escolha uma alternativa:",
                    options=list(opcoes.keys()),
                    format_func=lambda x: f"{x}: {opcoes[x]}",
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
                    else:
                        st.error("Resposta incorreta. Tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
                    st.rerun()
    
                # Gabarito Comentado
                with st.expander("✅ Ver Gabarito Comentado"):
                    st.write(questao.get("gabarito_comentado", "Gabarito indisponível."))
    
    st.divider()
    
    # Seção de Questões Discursivas
    if disc_list:
        st.header("✍️ Questões Discursivas")
        for i, questao in enumerate(disc_list):
            with st.container(border=True):
                st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
                
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
    
                # Renderização de Gráfico Plotly
                codigo = questao.get("codigo_plotly")
                if codigo:
                    local_vars = {"go": go, "st": st}
                    try:
                        exec(codigo, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_chart_disc_{i}")
                    except Exception as e:
                        st.warning("Não foi possível renderizar o gráfico.")
    
                st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
    
                # Validação Numérica se necessário
                valor_esperado = questao.get("resposta_numerica_esperada")
                if valor_esperado is not None:
                    user_val = st.number_input("Digite o resultado numérico para validação:", key=f"num_disc_{i}", format="%.4f")
                    if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                        if abs(user_val - valor_esperado) <= max(0.01, 0.01 * abs(valor_esperado)):
                            st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                            st.session_state.respostas_certas[f"disc_{i}"] = True
                        else:
                            st.error("O valor calculado difere do esperado. Verifique seus arredondamentos.")
                            st.session_state.respostas_certas[f"disc_{i}"] = False
                        st.rerun()
                else:
                    # Validação qualitativa
                    if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                    else:
                        st.session_state.respostas_certas[f"disc_{i}"] = False
    
                # Dica e Resolução
                if st.button("💡 Dica", key=f"dica_disc_{i}"):
                    st.info(questao.get("dica", "Dica indisponível."))
                    
                with st.expander("✅ Ver Resolução Detalhada"):
                    for passo in questao.get("gabarito_passo_a_passo", []):
                        st.write(f"- {passo}")
