import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuMi4yOiBJbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBwYXJhIGEgbcOpZGlhIGRlIHBvcHVsYcOnw7VlcyBOb3JtYWlzIChWYXJpw6JuY2lhIGRlc2NvbmhlY2lkYTogdXNvIGRhIGRpc3RyaWJ1acOnw6NvIHQgZGUgU3R1ZGVudCkiLCAicmVmZXJlbmNpYXNfYmlibGlvZ3JhZmljYXNfZmluYWlzIjogWyJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcMOtdHVsbyA3IC0gVmFyacOhdmVpcyBBbGVhdMOzcmlhcyBDb250w61udWFzIC0gcHAuIDE5MS0xOTIiLCAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXDDrXR1bG8gMTEgLSBJbmZlcsOqbmNpYSBFc3RhdMOtc3RpY2EgLSBwcC4gMjk3LTMwMCIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcMOtdHVsbyAxMiAtIFRlc3RlcyBkZSBIaXDDs3Rlc2VzIC0gcHAuIDM1NS0zNTYiLCAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXDDrXR1bG8gMTEgLSBFc3RpbWHDp8OjbyAtIHBwLiAzMTItMzE0IiwgIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2Fww610dWxvIDEyIC0gVGVzdGVzIGRlIEhpcMOzdGVzZXMgLSBwcC4gMzU1LTM1NyIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcMOtdHVsbyAxNSAtIEluZmVyw6puY2lhIHBhcmEgdsOhcmlhcyBwb3B1bGHDp8O1ZXMgLSBwcC4gNDMxLTQzMiIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcMOtdHVsbyAxMiAtIFRlc3RlcyBkZSBIaXDDs3Rlc2VzIC0gcHAuIDM1Ni0zNTciXX0=').decode('utf-8'))

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
    from scipy.stats import t, norm
    
    # Cabeçalho do Subtópico
    st.header(r"A Limitação da Variância Populacional Conhecida e a Necessidade da Estimação")
    
    # Introdução em prosa com quebra de ritmo
    st.markdown(r"""
    Em um cenário ideal de inferência estatística, teríamos acesso irrestrito aos parâmetros fundamentais de uma população, como a média real ($\mu$) e a variabilidade dos dados ($\sigma^2$). Sob essa perspectiva platônica, o Teorema Central do Limite nos permitiria utilizar a distribuição normal para calcular probabilidades com precisão absoluta.
    """)
    
    st.info(r"Na prática científica, contudo, a variabilidade populacional é um parâmetro latente, quase sempre desconhecido. Assumir que conhecemos $\sigma$ quando, na verdade, estamos apenas estimando-o via dados amostrais, constitui um erro de modelagem que subestima a incerteza real do processo.")
    
    st.markdown(r"""
    Ao trabalharmos com amostras reais, enfrentamos uma **dualidade da incerteza**:
    *   A incerteza intrínseca da média amostral em relação à populacional.
    *   A incerteza da variabilidade amostral ($S$) em relação ao parâmetro desconhecido ($\sigma$).
    
    Para resolver este dilema, William Sealy Gosset desenvolveu a **distribuição t de Student**, que ajusta as caudas da distribuição para compensar a imprecisão introduzida pelo uso de $S$. Esta correção é vital para garantir o rigor estatístico em amostras reduzidas.
    """)
    
    # O Coração Matemático
    st.markdown(r"### 📐 O Coração Matemático: A Derivação da Estatística t")
    
    st.markdown(r"A dedução analítica da estatística $T$ demonstra como a substituição da variância populacional pela amostral altera a natureza da distribuição da nossa estatística de teste:")
    
    st.latex(r"Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)")
    st.markdown(r"Definição da estatística $Z$ utilizando a variância populacional conhecida.")
    
    st.latex(r"Y = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)")
    st.markdown(r"A distribuição da variância amostral normalizada, seguindo uma distribuição qui-quadrado.")
    
    st.latex(r"T = \frac{Z}{\sqrt{Y/(n-1)}}")
    st.markdown(r"Definição da variável $t$ de Student como a razão entre uma normal padrão e a raiz quadrada de uma qui-quadrado normalizada pelos graus de liberdade.")
    
    st.latex(r"T = \frac{(\bar{X} - \mu) / (\sigma / \sqrt{n})}{\sqrt{[(n-1)S^2 / \sigma^2] / (n-1)}}")
    st.markdown(r"Substituição algébrica completa dos componentes da normal e da qui-quadrado.")
    
    st.latex(r"T = \frac{\bar{X} - \mu}{S/\sqrt{n}}")
    st.markdown(r"Simplificação final: a estatística $T$ depende apenas de valores amostrais, cancelando os termos populacionais desconhecidos.")
    
    # Simulador Educativo (Visualização da t-Student vs Normal)
    st.markdown(r"---")
    st.markdown(r"### 📊 Simulador: A Influência dos Graus de Liberdade")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        gl = st.slider(r"Graus de Liberdade (n-1)", min_value=1, max_value=30, value=5, key="gl_subtopico_1")
        mostrar_normal = st.toggle(r"Comparar com Normal (Z)", value=True, key="toggle_normal_subtopico_1")
    
    x = np.linspace(-4, 4, 200)
    y_t = t.pdf(x, gl)
    y_n = norm.pdf(x)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y_t, mode='lines', name=f't-Student (gl={gl})', line=dict(color="#1E3A8A", width=2)))
    if mostrar_normal:
        fig.add_trace(go.Scatter(x=x, y=y_n, mode='lines', name='Normal Padrão', line=dict(color="#991B1B", width=2, dash='dash')))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição t de Student vs Normal</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valor", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    st.plotly_chart(fig, use_container_width=True, key="chart_dist_subtopico_1")
    
    st.info(fr"Com {gl} graus de liberdade, observa-se que as caudas da distribuição t são mais pesadas que a da normal. À medida que o tamanho da amostra aumenta, o efeito da incerteza diminui e a distribuição t converge para a Normal Padrão.")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática: Controle de Qualidade")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Tempo de Reação Química")
        st.markdown(r"Um laboratório de controle de qualidade mede o tempo de reação de um novo composto. Em uma amostra de $n=16$ testes, obteve-se $\bar{X} = 120$ ms e um desvio padrão amostral $S = 12$ ms. Construa um intervalo de confiança de 95%.")
        
        st.latex(r"n=16, \bar{X}=120, S=12, 1-\alpha=0.95, gl=15")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Identificação dos parâmetros: amostra pequena exige t de Student.")
        st.markdown(r"- Valor crítico $t_{0.025, 15} = 2.131$.")
        st.markdown(r"- Erro padrão calculado como $12 / \sqrt{16} = 3$.")
        st.markdown(r"- Margem de erro: $2.131 \times 3 = 6.393$.")
        
        st.success(r"O intervalo de confiança resultante é [113,607 ms; 126,393 ms]. Com 95% de confiança, a média populacional encontra-se neste intervalo, corrigindo a incerteza pela estimativa amostral.")

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    
    # Cabeçalho do Subtópico
    st.header(r"A Engenharia da Distribuição t de Student: Fundamentos e Dedução")
    
    # Introdução
    st.info(r"A distribuição t de Student surgiu como uma resposta genial a um problema prático que atormentava os estatísticos do início do século XX: como realizar inferências precisas sobre médias populacionais quando não conhecemos a variabilidade real da população? Em situações reais, especialmente com amostras pequenas, o desvio padrão populacional é desconhecido e precisamos estimá-lo a partir dos próprios dados amostrais.")
    
    st.markdown(r"""
    ### 💡 A Filosofia da Incerteza Amostral
    Ao utilizarmos o desvio padrão da amostra em substituição ao populacional, introduzimos uma nova fonte de incerteza. A distribuição t de Student atua como um mecanismo de correção através de:
    - **Caudas Pesadas:** Atribui maior probabilidade a valores extremos, compensando a fragilidade da estimação da variância.
    - **Conservadorismo Estatístico:** Confere regiões de rejeição mais amplas e, portanto, mais confiáveis para pequenas amostras.
    - **Convergência:** À medida que o tamanho da amostra aumenta, a distribuição aproxima-se da normal padrão, validando sua robustez.
    """)
    
    # Desenvolvimento teórico
    st.markdown(r"### 🧠 Fundamentos Históricos e Epistemológicos")
    st.markdown(r"O desenvolvimento desta ferramenta, liderado por William Sealy Gosset, resolveu o dilema da substituição de $\sigma$ por $S$. Enquanto $\bar{X}$ flutua em torno de $\mu$ de forma previsível, o desvio padrão amostral $S$ também oscila, introduzindo uma variabilidade estocástica que a distribuição normal simples não consegue capturar.")
    
    st.markdown(r"Abaixo, destacamos o ponto crucial da modelagem do erro de estimação:")
    st.warning(r"A aplicação da t de Student exige uma vigilância epistemológica: a verificação de que os dados amostrais não violam pressupostos de normalidade é um passo inegociável para a validade do teste.")
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Formalismo da Estatística T")
    st.latex(r"T = \frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(gl), \quad \text{onde } gl = n-1")
    st.markdown(r"Esta estatística representa a razão entre um desvio normalizado da média amostral e a estimativa do erro padrão. O parâmetro $gl$ (graus de liberdade) define a forma específica da distribuição, sendo a manifestação direta da informação disponível para a estimação da variância.")
    
    # Dedução Analítica
    st.subheader(r"📝 Dedução Analítica da Estrutura T")
    st.markdown(r"A derivação da estatística $T$ fundamenta-se na relação entre variáveis aleatórias independentes:")
    
    st.latex(r"Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1)")
    st.markdown(r"Definição da normal padrão para a média amostral quando o parâmetro populacional $\sigma$ é conhecido.")
    
    st.latex(r"Y = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)")
    st.markdown(r"Definição da distribuição da variância amostral normalizada, resultando em uma qui-quadrado com $n-1$ graus de liberdade.")
    
    st.latex(r"T = \frac{Z}{\sqrt{Y/(n-1)}}")
    st.markdown(r"Definição da variável t de Student como a razão entre uma normal padrão e a raiz quadrada de uma qui-quadrado normalizada.")
    
    st.latex(r"T = \frac{\bar{X} - \mu}{S/\sqrt{n}}")
    st.markdown(r"Simplificação final onde o parâmetro de dispersão populacional desconhecido $\sigma$ é cancelado, permitindo a inferência baseada apenas em estimadores amostrais.")
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática: Inferência com Pequenas Amostras")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Processo de Tratamento Térmico")
        st.markdown(r"Um novo processo de tratamento térmico de componentes de precisão é testado. O tempo de resistência ao calor, em minutos, de 10 componentes amostrados, revelou uma média de $\bar{X} = 145$ min e uma variância amostral $S^2 = 144$ min². Estime o intervalo de confiança de 95% para a média populacional.")
        
        st.latex(r"n = 10, \quad \bar{X} = 145, \quad S = \sqrt{144} = 12")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Identificação dos graus de liberdade: $gl = 10 - 1 = 9$.")
        st.markdown(r"- Definição do valor crítico para 95% de confiança: $t_{crit} = 2,262$.")
        st.markdown(r"- Cálculo do intervalo: $IC = 145 \pm 2,262 \cdot \frac{12}{\sqrt{10}}$.")
        
        st.success(r"O intervalo de confiança de 95% para o tempo médio de resistência térmica é de [136,42 min; 153,58 min]. Esta estimativa oferece a segurança necessária para o controle de qualidade, incorporando a incerteza da variância amostral de forma rigorosa.")

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Propriedades e Comportamento Assintótico da Estatística t")
    
    # Introdução Teórica com Ritmo Dinâmico
    st.markdown(r"""
    Ao utilizarmos a estatística t de Student em inferências sobre a média populacional, operamos sob uma condição de incerteza acrescida: não conhecemos a variabilidade real (variância populacional) e recorremos ao seu estimador amostral. Esta substituição altera fundamentalmente a forma da distribuição do erro amostral.
    """)
    
    st.info(r"""
    **A essência da distribuição t:** Enquanto a distribuição normal padrão assume precisão total sobre a dispersão, a distribuição t de Student admite que o estimador de variabilidade possui incerteza própria. Isso resulta em uma curva com **caudas mais pesadas**, concentrando mais probabilidade nas extremidades.
    """)
    
    st.markdown(r"""
    Na prática, esse comportamento atua como um sistema de segurança: ao realizar um intervalo de confiança, a distribuição t nos obriga a incluir uma margem de erro mais ampla, compensando o risco de subestimarmos a variabilidade com amostras pequenas.
    """)
    
    # Comportamento Assintótico
    st.subheader(r"📐 O Caminho para a Normalidade: Comportamento Assintótico")
    
    st.markdown(r"""
    A influência da incerteza extra diminui conforme o tamanho da amostra cresce. À medida que o tamanho da amostra ($n$) aumenta, o estimador amostral ($S^2$) torna-se mais preciso, convergindo para o parâmetro populacional ($\sigma^2$).
    """)
    
    # Formalismo Matemático
    st.latex(r"T = \frac{\bar{X} - \mu}{S/\sqrt{n}} \sim t(gl)")
    st.latex(r"\lim_{n \to \infty} t(n-1) = N(0,1)")
    
    st.markdown(r"""
    Este limite estabelece que, no horizonte de amostras vastas, a distribuição t de Student converge para a distribuição normal padrão, garantindo a robustez do método estatístico.
    """)
    
    # Dedução Analítica (Sequencial conforme solicitado)
    st.markdown(r"---")
    st.markdown(r"#### 🧩 Demonstração da Estrutura da Estatística t")
    
    st.latex(r"Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0,1)")
    st.markdown(r"Definição da estatística Z centrada e reduzida, sob pressuposto de variância conhecida.")
    
    st.latex(r"Y = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)")
    st.markdown(r"Definição da distribuição do estimador de variância normalizado.")
    
    st.latex(r"T = \frac{Z}{\sqrt{Y/(n-1)}} = \frac{(\bar{X} - \mu)/(\sigma/\sqrt{n})}{\sqrt{S^2/\sigma^2}}")
    st.markdown(r"Expressão de T como o quociente entre a Normal e a raiz da Qui-Quadrado normalizada.")
    
    st.latex(r"T = \frac{\bar{X} - \mu}{S/\sqrt{n}}")
    st.markdown(r"Cancelamento dos termos populacionais, revelando a estatística operacional.")
    
    st.latex(r"\lim_{n \to \infty} \frac{S}{\sigma} = 1 \implies T \xrightarrow{d} N(0,1)")
    st.markdown(r"Argumento de convergência baseado na consistência do estimador S.")
    
    # Exemplo Prático Rígido
    st.markdown(r"---")
    st.subheader(r"📈 Casos de Aplicação Prática: Precisão de Sensores IoT")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Estimação com Amostra Reduzida")
        st.markdown(r"Em um estudo de precisão de sensores IoT, uma amostra de $n=10$ leituras de temperatura apresentou um desvio padrão amostral de $S=0,5$ °C. Comparamos a distribuição t com a Normal padrão para 95% de confiança.")
        
        st.latex(r"1-\alpha = 0,95 \quad \text{com} \quad gl=9")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Valor crítico Z (95%): $1,96$")
        st.markdown(r"- Valor crítico t (95%, gl=9): $2,262$")
        st.markdown(r"- Margem de erro Z: $1,96 \cdot \frac{0,5}{\sqrt{10}} \approx 0,309$")
        st.markdown(r"- Margem de erro t: $2,262 \cdot \frac{0,5}{\sqrt{10}} \approx 0,358$")
        
        st.success(r"**Laudo:** A margem de erro via distribuição t (0,358) é 15% superior à da normal (0,309), demonstrando o caráter conservador e rigoroso necessário em amostras pequenas.")
    
    # Espaço de nota final
    st.markdown(r"---")
    st.warning(r"**Nota de Integridade:** Aplicar o valor crítico da normal em cenários de variância desconhecida e amostras modestas constitui uma subestimativa da incerteza, elevando o erro do Tipo I.")

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Construção Rigorosa de Intervalos de Confiança para a Média")
    
    # Discussão Teórica
    st.markdown(r"""
    A transição da estimação pontual para a estimação por intervalos representa um salto fundamental na maturidade estatística de um pesquisador. Enquanto a média amostral nos fornece um único valor que serve como o melhor palpite para a média populacional, ela carece de uma medida explícita de precisão.
    """)
    
    st.info(r"A construção rigorosa de um intervalo de confiança busca capturar a incerteza inerente ao processo amostral, garantindo que, em uma proporção definida de longo prazo, o intervalo resultante conterá o verdadeiro valor da média populacional.")
    
    st.markdown(r"""
    Quando não conhecemos a variância populacional, somos obrigados a utilizar o desvio padrão amostral como um substituto. Este procedimento adiciona uma camada de incerteza que a distribuição *t* de Student endereça com elegância. O método da variável pivô, detalhado abaixo, permite isolar o parâmetro de interesse dentro de uma desigualdade probabilística.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Formalismo Matemático: Método da Variável Pivô")
    st.markdown(r"A expressão fundamental que delimita o espaço de busca do parâmetro populacional $\mu$ é:")
    st.latex(r"IC(\mu; 1-\alpha) = \left( \bar{X} - t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}}, \bar{X} + t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \right)")
    
    st.markdown(r"""
    Nesta formulação:
    - **$\bar{X}$**: É a média amostral observada.
    - **$t_{\alpha/2, gl}$**: Representa o valor crítico da distribuição *t* de Student.
    - **$S/\sqrt{n}$**: Constitui o erro padrão da média, que pondera a dispersão amostral.
    """)
    
    # Dedução Analítica
    st.subheader(r"🧮 Demonstração da Derivação")
    st.markdown(r"A derivação do intervalo segue um rigor lógico baseado na manipulação de desigualdades probabilísticas:")
    
    st.latex(r"P\left( -t_{\alpha/2, gl} \le \frac{\bar{X} - \mu}{S/\sqrt{n}} \le t_{\alpha/2, gl} \right) = 1 - \alpha")
    st.markdown(r"Inicia-se com a definição probabilística da variável *t*, onde a estatística cai entre os valores críticos.")
    
    st.latex(r"P\left( -t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \le \bar{X} - \mu \le t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \right) = 1 - \alpha")
    st.markdown(r"Multiplicam-se todos os termos da desigualdade pelo erro padrão $S/\sqrt{n}$.")
    
    st.latex(r"P\left( -\bar{X} - t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \le -\mu \le -\bar{X} + t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \right) = 1 - \alpha")
    st.markdown(r"Subtrai-se a média amostral $\bar{X}$ de todos os membros da desigualdade.")
    
    st.latex(r"P\left( \bar{X} - t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \le \mu \le \bar{X} + t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \right) = 1 - \alpha")
    st.markdown(r"Ao multiplicar por $-1$, invertemos os sinais, isolando o parâmetro $\mu$ no centro do intervalo.")
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática: Indústria Farmacêutica")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Teste de Dosagem")
        st.markdown(r"Uma indústria farmacêutica está testando a dosagem de um novo fármaco. Com $n=9$, $\bar{X}=45$ mg e $S=6$ mg, construa o intervalo de 99% de confiança.")
        
        st.latex(r"\text{Dados: } n=9, \bar{X}=45, S=6, 1-\alpha=0.99, gl=8")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Valor crítico: $t_{0.005, 8} = 3,355$")
        st.markdown(r"- Margem de erro: $E = 3,355 \cdot (6/3) = 6,71$")
        st.markdown(r"- Intervalo: $45 \pm 6,71 = [38,29; 51,71]$")
        
        st.success(r"O intervalo de confiança de 99% para a dosagem média é [38,29 mg; 51,71 mg]. Temos 99% de confiança de que a verdadeira média populacional reside neste espectro.")
    
    # Simulador Interativo
    st.subheader(r"⚙️ Simulador de Incerteza e Precisão")
    col1, col2 = st.columns(2)
    n_val = col1.slider(r"Tamanho da Amostra (n)", 5, 100, 30, key=r"n_subtopico_4")
    conf_val = col2.select_slider(r"Nível de Confiança", [0.90, 0.95, 0.99], key=r"conf_subtopico_4")
    
    # Cálculos do simulador
    t_val = stats.t.ppf((1 + conf_val) / 2, df=n_val - 1)
    erro_padrao = 1.0 / np.sqrt(n_val) # Assumindo desvio unitário para simulação
    margem = t_val * erro_padrao
    
    # Gráfico
    x = np.linspace(-3, 3, 200)
    y = stats.t.pdf(x, df=n_val - 1)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Distribuição t', line=dict(color='#1E3A8A')))
    fig.add_vrect(x0=-margem, x1=margem, fillcolor="#10B981", opacity=0.3, line_width=0)
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição de Amostragem e Área de Confiança</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Estatística", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")
    
    st.info(f"Com uma amostra de tamanho n = {n_val} e {conf_val*100:.0f}% de confiança, a margem de erro normalizada é {margem:.4f}. O aumento de n reduz a dispersão, estreitando o intervalo e aumentando a precisão da estimativa.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Aplicações Práticas e Interpretação de Resultados Inferenciais")
    
    # Prosa Teórica - Fragmentação em partes elegantes
    st.markdown(r"""
    A construção de um intervalo de confiança para a média populacional não é apenas um exercício algébrico de manipulação de dados, mas uma ferramenta de diagnóstico fundamental na prática estatística. Quando calculamos um intervalo de confiança, estamos essencialmente quantificando nossa incerteza.
    """)
    
    st.warning(r"**Nota Importante sobre a Interpretação:** Ao contrário do que a intuição comum sugere, o intervalo de confiança não nos fornece a probabilidade de que a média populacional específica esteja contida entre dois valores fixos. O parâmetro $\mu$ é um valor constante da natureza, e não uma variável aleatória.")
    
    st.markdown(r"""
    Na visão frequêntista, se pudéssemos repetir o experimento de coleta de dados e construção de intervalos milhares de vezes, uma proporção definida pelo nível de confiança (ex: 95%) dos intervalos gerados conteria o verdadeiro valor do parâmetro populacional. A amplitude desse intervalo é um indicador direto da precisão da nossa estimativa:
    - **Variabilidade dos dados:** Quanto maior a dispersão ($S$), maior a incerteza e, portanto, maior a amplitude.
    - **Tamanho da amostra ($n$):** A raiz quadrada do tamanho da amostra no denominador reduz o erro padrão, estreitando o intervalo.
    - **Nível de Confiança ($1-\alpha$):** Níveis mais rigorosos exigem valores críticos maiores, resultando em intervalos mais conservadores (mais largos).
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Formalismo do Intervalo de Confiança")
    st.latex(r"IC(\mu; 1-\alpha) = \left[ \bar{X} - t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}}, \bar{X} + t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \right]")
    
    st.markdown(r"""
    - $\bar{X}$: Média amostral, estimador pontual.
    - $S$: Desvio padrão amostral com $n-1$ graus de liberdade.
    - $t_{\alpha/2, gl}$: Valor crítico da distribuição t de Student.
    - $\frac{S}{\sqrt{n}}$: Erro padrão da média, mensurando a dispersão do estimador.
    """)
    
    # Dedução Analítica
    st.markdown(r"### 🧪 Derivação da Estrutura Inferencial")
    st.latex(r"P\left( -t_{\alpha/2, gl} \le \frac{\bar{X} - \mu}{S/\sqrt{n}} \le t_{\alpha/2, gl} \right) = 1 - \alpha")
    st.markdown(r"Definição probabilística inicial baseada na distribuição t.")
    
    st.latex(r"P\left( -t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \le \bar{X} - \mu \le t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \right) = 1 - \alpha")
    st.markdown(r"Isolamento do erro de estimação.")
    
    st.latex(r"P\left( -\bar{X} - t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \le -\mu \le -\bar{X} + t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \right) = 1 - \alpha")
    st.markdown(r"Subtração da média amostral $\bar{X}$ de todos os membros.")
    
    st.latex(r"P\left( \bar{X} - t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \le \mu \le \bar{X} + t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}} \right) = 1 - \alpha")
    st.markdown(r"Resultado final após inversão dos sinais.")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Vida Útil de Semicondutores")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Estimativa de Vida Útil")
        st.markdown(r"Um fabricante deseja estimar a vida útil média de um novo semicondutor. Amostra de 12 unidades apresentou $\bar{X} = 1200$ e $S = 60$. Determine o IC de 95%.")
        st.latex(r"n=12, \bar{X}=1200, S=60, gl=11, t_{0.025, 11}=2.201")
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Margem de Erro: $E = 2.201 \cdot (60 / \sqrt{12}) \approx 38.12$")
        st.markdown(r"- Limites: $1200 \pm 38.12$")
        st.success(r"O intervalo de confiança de 95% é [1161.88, 1238.12]. Com 95% de confiança, a média real da população está contida aqui.")
    
    # Simulador Interativo
    st.subheader(r"🎛️ Simulador: Dinâmica do Intervalo")
    col1, col2 = st.columns(2)
    n_sim = col1.slider(r"Tamanho da Amostra (n)", 5, 100, 30, key=r"n_sim_subtopico_5")
    conf_sim = col2.select_slider(r"Nível de Confiança", [0.90, 0.95, 0.99], value=0.95, key=r"conf_sim_subtopico_5")
    
    media_sim = 1200
    s_sim = 60
    alpha = 1 - conf_sim
    t_crit = stats.t.ppf(1 - alpha/2, df=n_sim-1)
    erro_padrao = s_sim / np.sqrt(n_sim)
    margem = t_crit * erro_padrao
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[media_sim - margem, media_sim + margem], y=[1, 1], mode="lines+markers", line=dict(color="#1E3A8A", width=4), name=r"IC"))
    fig.add_trace(go.Scatter(x=[media_sim], y=[1], mode="markers", marker=dict(size=12, color="#991B1B"), name=r"Média"))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Dinâmica do Intervalo de Confiança</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Horas", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(showticklabels=False, fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"))
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_5")
    
    st.info(f"Ao ajustar o tamanho da amostra para {n_sim}, o erro padrão torna-se {erro_padrao:.2f}. Com {conf_sim*100}% de confiança, a margem de erro calculada é de {margem:.2f}, definindo um intervalo de [{media_sim-margem:.2f}, {media_sim+margem:.2f}].")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuMi4yOiBJbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBwYXJhIGEgbcOpZGlhIGRlIHBvcHVsYcOnw7VlcyBOb3JtYWlzIChWYXJpw6JuY2lhIGRlc2NvbmhlY2lkYTogdXNvIGRhIGRpc3RyaWJ1acOnw6NvIHQgZGUgU3R1ZGVudCkiLCAicXVlc3RvZXNfbXVsdGlwbGFfZXNjb2xoYSI6IFt7ImVudW5jaWFkbyI6ICJVbSBlbmdlbmhlaXJvIGRlIHF1YWxpZGFkZSBlbSB1bWEgcGxhbnRhIGRlIG1hbnVmYXR1cmEgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIGRlc2VqYSBhdmFsaWFyIGEgbcOpZGlhIGRlIHRlbXBvIGRlIHZpZGEgZGUgdW0gbm92byBsb3RlIGRlIHNlbnNvcmVzLiBFbGUgY29sZXRhIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgc2ltcGxlcyBkZSAkbj0xMiQgc2Vuc29yZXMgZSBlbmNvbnRyYSB1bWEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSA9IDE1MDAkIGhvcmFzIGUgdW0gZGVzdmlvIHBhZHLDo28gYW1vc3RyYWwgJFMgPSAxMjAkIGhvcmFzLiBBc3N1bWluZG8gcXVlIG8gdGVtcG8gZGUgdmlkYSBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLCBtYXMgZGVzY29uaGVjZW5kbyBhIHZhcmnDom5jaWEgcG9wdWxhY2lvbmFsICRcXHNpZ21hXjIkLCBxdWFsIGRhcyBzZWd1aW50ZXMgYWZpcm1hw6fDtWVzIG1lbGhvciBkZXNjcmV2ZSBhIGp1c3RpZmljYXRpdmEgZXN0YXTDrXN0aWNhIHBhcmEgbyB1c28gZGEgZGlzdHJpYnVpw6fDo28gJHQkIGRlIFN0dWRlbnQgZW0gdmV6IGRhIG5vcm1hbCBwYWRyw6NvICROKDAsIDEpJCBwYXJhIGEgaW5mZXLDqm5jaWEgZGEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIGRpc3RyaWJ1acOnw6NvICR0JCBkZSBTdHVkZW50IGRldmUgc2VyIHVzYWRhIHBvcnF1ZSBvIHRhbWFuaG8gZGEgYW1vc3RyYSDDqSBzdXBlcmlvciBhIDMwLCBvIHF1ZSBnYXJhbnRlIGEgdmFsaWRhZGUgZG8gVGVvcmVtYSBMaW1pdGUgQ2VudHJhbCBwYXJhIHF1YWxxdWVyIHZhcmnDom5jaWEuIiwgIkIiOiAiQSB1dGlsaXphw6fDo28gZGUgJFMkIG5vIGx1Z2FyIGRlICRcXHNpZ21hJCBpbnRyb2R1eiB1bWEgdmFyaWFiaWxpZGFkZSBhZGljaW9uYWwgbmEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlLCByZXN1bHRhbmRvIGVtIGNhdWRhcyBtYWlzIHBlc2FkYXMgbmEgZGlzdHJpYnVpw6fDo28sIGFzIHF1YWlzIHPDo28gYWRlcXVhZGFtZW50ZSBjb21wZW5zYWRhcyBwZWxhIGRpc3RyaWJ1acOnw6NvICR0KGdsKSQgY29tICRnbCA9IDExJC4iLCAiQyI6ICJBIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBwYWRyw6NvICROKDAsIDEpJCBzZW1wcmUgc3ViZXN0aW1hIG8gZXJybyBwYWRyw6NvLCB0b3JuYW5kbyBhIGRpc3RyaWJ1acOnw6NvICR0JCBkZSBTdHVkZW50IGRlc25lY2Vzc8OhcmlhIHNlIG8gZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsIGZvciBlc3RpbWFkbyBjb3JyZXRhbWVudGUuIiwgIkQiOiAiTyB1c28gZGUgJG4tMSQgZ3JhdXMgZGUgbGliZXJkYWRlIG5hIGRpc3RyaWJ1acOnw6NvICR0JCDDqSB1bWEgY29udmVuw6fDo28gaGlzdMOzcmljYSwgbWFzIG1hdGVtYXRpY2FtZW50ZSBhIGRpc3RyaWJ1acOnw6NvICROKDAsIDEpJCBzZXJpYSBlcXVpdmFsZW50ZSwgdW1hIHZleiBxdWUgYSBhbW9zdHJhIMOpIGFsZWF0w7NyaWEuIiwgIkUiOiAiQSBkaXN0cmlidWnDp8OjbyAkdCQgw6kgdXRpbGl6YWRhIGFwZW5hcyBwYXJhIHBvcHVsYcOnw7VlcyBxdWUgbsOjbyBzZWd1ZW0gdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCwgcGVybWl0aW5kbyBxdWUgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBjb252aXJqYSBwYXJhICRcXG11JCBtZXNtbyBjb20gJFMkIGRlc2NvbmhlY2lkby4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIlJlZmxpdGEgc29icmUgY29tbyBvIGRlbm9taW5hZG9yIGRhIGVzdGF0w61zdGljYSAkVCA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXV9e1MvXFxzcXJ0e259fSQgZGlmZXJlIGRvIGRlICRaID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdX17XFxzaWdtYS9cXHNxcnR7bn19JCBlIHF1YWwgbyBpbXBhY3RvIGRlc3NhIGluY2VydGV6YSBhZGljaW9uYWwgc29icmUgbyBmb3JtYXRvIGRhIGRlbnNpZGFkZSBkZSBwcm9iYWJpbGlkYWRlLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQW8gZGVzY29uaGVjZXJtb3MgYSB2YXJpw6JuY2lhIHBvcHVsYWNpb25hbCAkXFxzaWdtYV4yJCwgdXRpbGl6YW1vcyBvIGVzdGltYWRvciBuw6NvLXZpY2lhZG8gJFNeMiQuIEEgZXN0YXTDrXN0aWNhICRUID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdX17Uy9cXHNxcnR7bn19JCDDqSBvIHF1b2NpZW50ZSBkZSB1bWEgbm9ybWFsIHBhZHLDo28gcG9yIHVtYSByYWl6IHF1YWRyYWRhIGRlIHVtYSBxdWktcXVhZHJhZG8gaW5kZXBlbmRlbnRlLCBvIHF1ZSByZXN1bHRhIG5hIGRpc3RyaWJ1acOnw6NvICR0JCBkZSBTdHVkZW50IGNvbSAkZ2wgPSBuLTEgPSAxMSQuIENvbW8gJFMkIMOpIHVtYSB2YXJpw6F2ZWwgYWxlYXTDs3JpYSBxdWUgb3NjaWxhIGVudHJlIGFtb3N0cmFzLCBhIGRpc3RyaWJ1acOnw6NvICR0JCBhcHJlc2VudGEgbWFpb3IgZGlzcGVyc8OjbyAoY2F1ZGFzIG1haXMgcGVzYWRhcykgcXVlIGEgbm9ybWFsLCBjb3JyaWdpbmRvIGEgc3ViZXN0aW1hdGl2YSBkbyByaXNjbyBkZSBlcnJvIHF1ZSBvY29ycmVyaWEgc2UgdXPDoXNzZW1vcyAkWiQuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgtNCwgNCwgMjAwKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT1zdGF0cy5ub3JtLnBkZih4LCAwLCAxKSwgbmFtZT1yJ05vcm1hbCAkTigwLDEpJCcsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTIpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9c3RhdHMudC5wZGYoeCwgMTEpLCBuYW1lPXIndC1TdHVkZW50ICR0KDExKSQnLCBsaW5lPWRpY3QoY29sb3I9JyM5OTFCMUInLCB3aWR0aD0yKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+Q29tcGFyYcOnw6NvIGVudHJlIERpc3RyaWJ1acOnw7VlczwvYj4nLCB4YXhpc190aXRsZT0nRXN0YXTDrXN0aWNhJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnLCBsZWdlbmQ9ZGljdChvcmllbnRhdGlvbj0naCcpKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNTUifSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHF1ZSB1bSBnZXN0b3IgZGUgXFxsb2fDrXN0aWNhIGVzdHVkYSBhIHZhcmlhYmlsaWRhZGUgZGUgZW50cmVnYXMuIEVsZSBzYWJlIHF1ZSBhIHZhcmnDom5jaWEgcG9wdWxhY2lvbmFsICRcXHNpZ21hXjIkIMOpIHVtIHBhcsOibWV0cm8gY3LDrXRpY28gZSwgZW0gdW0gZXN0dWRvIGNvbSBhbW9zdHJhIGRlICRuPTE2JCwgY2FsY3Vsb3UgJFNeMiA9IDI1NiQgKGhvcmFzwrIpLiBTZSBvIG9iamV0aXZvIGZvciBjb25zdHJ1aXIgdW0gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgcGFyYSBhIG3DqWRpYSBwb3B1bGFjaW9uYWwgJFxcbXUkIHV0aWxpemFuZG8gYSBlc3RhdMOtc3RpY2EgJFQgPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11fXtTL1xcc3FydHtufX0kLCBxdWFsIGRhcyBzZWd1aW50ZXMgY29uY2x1c8O1ZXMgc29icmUgYSByb2J1c3RleiBkbyBtw6l0b2RvIMOpIGNvcnJldGEgYW8gYXNzdW1pciBxdWUgYSBwb3B1bGHDp8OjbyBvcmlnaW5hbCDDqSBub3JtYWw/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJDb21vICRcXHNpZ21hXjIkIMOpIGRlc2NvbmhlY2lkbywgbyB1c28gZGUgJFNeMiQgZ2FyYW50ZSBxdWUgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBzZWphIHVtIGVzdGltYWRvciB2aWNpYWRvLCBleGlnaW5kbyB1bWEgY29ycmXDp8OjbyBwb3IgJG4vKG4tMSkkLiIsICJCIjogIk8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSAkRVAoXFxiYXJ7WH0pID0gUy9cXHNxcnR7bn0kIMOpIHVtYSBjb25zdGFudGUgYWJzb2x1dGEgY2FsY3VsYWRhIGEgcGFydGlyIGRhIGFtb3N0cmEgZSBuw6NvIGRlcGVuZGUgZGEgZGlzdHJpYnVpw6fDo28gcG9wdWxhY2lvbmFsIHBhcmEgc2VyIG7Do28tdmljaWFkby4iLCAiQyI6ICJPIHVzbyBkYSBkaXN0cmlidWnDp8OjbyAkdCQgY29tICRnbCA9IDE1JCDDqSBhIGFib3JkYWdlbSBjb3JyZXRhIHBhcmEgbWl0aWdhciBvIGltcGFjdG8gZGEgaW5jZXJ0ZXphIHNvYnJlICRcXHNpZ21hXjIkLCBnYXJhbnRpbmRvIHF1ZSBvIG7DrXZlbCBkZSBjb25maWFuw6dhICQxLVxcYWxwaGEkIHNlamEgcmVzcGVpdGFkbywgc29iIGEgc3Vwb3Npw6fDo28gZGUgbm9ybWFsaWRhZGUgcG9wdWxhY2lvbmFsLiIsICJEIjogIlBhcmEgYW1vc3RyYXMgZGUgdGFtYW5obyAkbj0xNiQsIGEgZGlzdHJpYnVpw6fDo28gbm9ybWFsICROKDAsIDEpJCDDqSB1bWEgYXByb3hpbWHDp8OjbyBpZGVhbCBwYXJhICRUJCwgdmlzdG8gcXVlICRuJCDDqSBncmFuZGUgbyBzdWZpY2llbnRlIHBhcmEgaWdub3JhciBhIGluY2VydGV6YSBkZSAkU14yJC4iLCAiRSI6ICJBIGVzdGF0w61zdGljYSAkVCQgbsOjbyBwb3NzdWkgdmFyacOibmNpYSBkZWZpbmlkYSwgdG9ybmFuZG8gaW1wb3Nzw612ZWwgYSBjb25zdHJ1w6fDo28gZGUgaW50ZXJ2YWxvcyBkZSBjb25maWFuw6dhIGJhc2VhZG9zIGFwZW5hcyBuYSBhbW9zdHJhIHNlbSBjb25oZWNlciAkXFxzaWdtYV4yJCBwcmV2aWFtZW50ZS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIlBlbnNlIG5vIGRpbGVtYSBkYSAnaW5jZXJ0ZXphIGR1cGxhJyBtZW5jaW9uYWRvOiBhIGluY2VydGV6YSBuYSBtw6lkaWEgKCRcXGJhcntYfSQpIGUgYSBpbmNlcnRlemEgYWRpY2lvbmFsIGludHJvZHV6aWRhIHBlbGEgZXN0aW1hdGl2YSBkYSB2YXJpYWJpbGlkYWRlICgkUyQpIGEgcGFydGlyIGRlIHBvdWNvcyBkYWRvcy4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgZXN0YXTDrXN0aWNhICR0JCBkZSBTdHVkZW50IGZvaSBkZXNlbnZvbHZpZGEgcHJlY2lzYW1lbnRlIHBhcmEgbGlkYXIgY29tIGEgaW5jZXJ0ZXphIGdlcmFkYSBwZWxhIHN1YnN0aXR1acOnw6NvIGRlICRcXHNpZ21hJCBwb3IgJFMkLiBBbyBzdXBvciBhIG5vcm1hbGlkYWRlLCBhIGRpc3RyaWJ1acOnw6NvIGRlICRUJCDDqSBleGF0YW1lbnRlICR0KGdsKSQgY29tICRnbCA9IG4tMSQuIEEgb3DDp8OjbyBDIGRlc2NyZXZlIGNvcnJldGFtZW50ZSBxdWUgZXNzZSBhanVzdGUgY29tcGVuc2EgYSBpbmNlcnRlemEgZGEgdmFyacOibmNpYSBhbW9zdHJhbCwgZ2FyYW50aW5kbyBhIHZhbGlkYWRlIHByb2JhYmlsw61zdGljYSBkbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSwgbyBxdWUgbsOjbyBvY29ycmVyaWEgY29tIGEgbm9ybWFsIHBhZHLDo28gcGFyYSBhbW9zdHJhcyBwZXF1ZW5hcyAoJG49MTYkKS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNTUifSwgeyJlbnVuY2lhZG8iOiAiVW0gbGFib3JhdMOzcmlvIGRlIGVuZ2VuaGFyaWEgZGUgbWF0ZXJpYWlzIGVzdMOhIHRlc3RhbmRvIGEgcmVzaXN0w6puY2lhIMOgIHRyYcOnw6NvIGRlIHVtYSBub3ZhIGxpZ2EgbWV0w6FsaWNhLiBFbSB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIGRlICRuID0gMTAkIHBlw6dhcywgb2JzZXJ2b3Utc2UgdW1hIHJlc2lzdMOqbmNpYSBtw6lkaWEgJFxcYmFye1h9ID0gNDUwJCBNUGEgZSB1bWEgdmFyacOibmNpYSBhbW9zdHJhbCAkU14yID0gMTAwJCBNUGEkXjIkLiBBc3N1bWluZG8gcXVlIGEgcmVzaXN0w6puY2lhIGRlc3RhIGxpZ2Egc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCwgcXVhbCDDqSBhIGVzdGF0w61zdGljYSAkVCQgbmVjZXNzw6FyaWEgcGFyYSByZWFsaXphciB1bWEgaW5mZXLDqm5jaWEgc29icmUgYSBtw6lkaWEgcG9wdWxhY2lvbmFsICRcXG11JCBlIHF1YWwgw6kgbyBuw7ptZXJvIGRlIGdyYXVzIGRlIGxpYmVyZGFkZSAoJGdsJCkgZGEgZGlzdHJpYnVpw6fDo28gJHQkIGRlIFN0dWRlbnQgY29ycmVzcG9uZGVudGU/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIkVCA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXV9ezEwL1xcc3FydHsxMH19JCBjb20gJGdsID0gMTAkLiIsICJCIjogIiRUID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdX17MTAvXFxzcXJ0ezl9fSQgY29tICRnbCA9IDkkLiIsICJDIjogIiRUID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdX17MTAwL1xcc3FydHsxMH19JCBjb20gJGdsID0gMTAkLiIsICJEIjogIiRUID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdX17Uy9cXHNxcnR7MTB9fSQgY29tICRnbCA9IDEwJC4iLCAiRSI6ICIkVCA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXV9e1NeMi9cXHNxcnR7MTB9fSQgY29tICRnbCA9IDkkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGRlZmluacOnw6NvIGRhIGVzdGF0w61zdGljYSAkVCA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXV9e1MvXFxzcXJ0e259fSQgZSBxdWUgbyBkZXN2aW8gcGFkcsOjbyBhbW9zdHJhbCAkUyQgw6kgYSByYWl6IHF1YWRyYWRhIGRhIHZhcmnDom5jaWEgYW1vc3RyYWwgJFNeMiQuIE8gcGFyw6JtZXRybyAkZ2wkIMOpIGRlZmluaWRvIHBlbG8gbsO6bWVybyBkZSBvYnNlcnZhw6fDtWVzIG1lbm9zIHVtLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBlc3RhdMOtc3RpY2EgJFQkIHV0aWxpemFkYSBwYXJhIGluZmVyw6puY2lhIHNvYnJlIGEgbcOpZGlhIHBvcHVsYWNpb25hbCBxdWFuZG8gYSB2YXJpw6JuY2lhIHBvcHVsYWNpb25hbCAkXFxzaWdtYV4yJCDDqSBkZXNjb25oZWNpZGEgw6kgJFQgPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11fXtTL1xcc3FydHtufX0kLiBEYWRvcyBvIGVudW5jaWFkbzogJG4gPSAxMCQsICRcXGJhcntYfSA9IDQ1MCQgZSAkU14yID0gMTAwJCwgdGVtb3MgcXVlIG8gZGVzdmlvIHBhZHLDo28gYW1vc3RyYWwgw6kgJFMgPSBcXHNxcnR7U14yfSA9IFxcc3FydHsxMDB9ID0gMTAkLiBQb3J0YW50bywgJFQgPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11fXsxMC9cXHNxcnR7MTB9fSQuIENvbW8gbyBkZW5vbWluYWRvciDDqSAkUy9cXHNxcnR7bn0kLCB0ZW1vcyAkUy9cXHNxcnR7bn0gPSAxMC9cXHNxcnR7MTB9JCwgcXVlIMOpIGVxdWl2YWxlbnRlIGEgJDEwL1xcc3FydHsxMH0kIG91ICQxMC9cXHNxcnR7MTB9JCAobyBxdWUgc2ltcGxpZmljYSBwYXJhICRcXHNxcnR7MTB9JCkuIE9ic2VydmFuZG8gYSBhbHRlcm5hdGl2YSBCLCB0ZW1vcyAkUyA9IDEwJCBlICRuPTEwJCwgcmVzdWx0YW5kbyBlbSAkZ2wgPSBuIC0gMSA9IDkkLiBBIGV4cHJlc3PDo28gJDEwL1xcc3FydHs5fSQgZW0gQiByZWZsZXRlIGEgZm9ybWEgb3BlcmFjaW9uYWwgZG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNTUifSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHF1ZSB1bSBlbmdlbmhlaXJvIGRlIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBkZXNlamEgdmVyaWZpY2FyIHNlIGEgcHJlc3PDo28gZGUgdW0gbm92byBsb3RlIGRlIGNvbXByZXNzb3JlcyBkZSBhciBhdGVuZGUgw6AgZXNwZWNpZmljYcOnw6NvIHTDqWNuaWNhIGRlICRcXG11ID0gMTAwJCBQU0kuIEVsZSBjb2xldGEgdW1hIGFtb3N0cmEgZGUgJG4gPSAyNSQgdW5pZGFkZXMsIG9idGVuZG8gJFxcYmFye1h9ID0gMTAyJCBQU0kgZSAkUyA9IDUkIFBTSS4gQ29uc2lkZXJhbmRvIHVtIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSA9IDAsMDUkIHBhcmEgdW0gdGVzdGUgYmlsYXRlcmFsLCBvIGVuZ2VuaGVpcm8gYnVzY2EgYSByZWdpw6NvIGNyw610aWNhLiBRdWFsIMOpIGEgY2FyYWN0ZXLDrXN0aWNhIGZ1bmRhbWVudGFsIGRhIGRpc3RyaWJ1acOnw6NvICR0JCBkZSBTdHVkZW50IHF1ZSBhIHRvcm5hIG1haXMgYWRlcXVhZGEgcXVlIGEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIHBhZHLDo28gcGFyYSBlc3RlIHRlc3RlPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBkaXN0cmlidWnDp8OjbyAkdCQgZGUgU3R1ZGVudCBwb3NzdWkgY2F1ZGFzIG1haXMgbGV2ZXMgcXVlIGEgbm9ybWFsIHBhZHLDo28sIHBlcm1pdGluZG8gcmVqZWl0YXIgJEhfMCQgbWFpcyBmYWNpbG1lbnRlLiIsICJCIjogIkEgZGlzdHJpYnVpw6fDo28gJHQkIGRlIFN0dWRlbnQgdGVtIG1lbm9yIHZhcmnDom5jaWEgZG8gcXVlIGEgbm9ybWFsIHBhZHLDo28gcGFyYSBwZXF1ZW5vcyBncmF1cyBkZSBsaWJlcmRhZGUuIiwgIkMiOiAiQSBkaXN0cmlidWnDp8OjbyAkdCQgZGUgU3R1ZGVudCBwb3NzdWkgY2F1ZGFzIG1haXMgcGVzYWRhcywgbyBxdWUgY29tcGVuc2EgYSBpbmNlcnRlemEgYWRpY2lvbmFsIGludHJvZHV6aWRhIHBlbGEgZXN0aW1hw6fDo28gZGEgdmFyacOibmNpYSBwb3B1bGFjaW9uYWwgJFxcc2lnbWFeMiQgcGVsbyBkZXN2aW8gcGFkcsOjbyBhbW9zdHJhbCAkUyQuIiwgIkQiOiAiQSBkaXN0cmlidWnDp8OjbyAkdCQgZGUgU3R1ZGVudCBuw6NvIGRlcGVuZGUgZG8gdGFtYW5obyBhbW9zdHJhbCAkbiQsIHNlbmRvIHNlbXByZSBpZMOqbnRpY2Egw6AgZGlzdHJpYnVpw6fDo28gbm9ybWFsLiIsICJFIjogIkEgZGlzdHJpYnVpw6fDo28gJHQkIGRlIFN0dWRlbnQgw6kgbGltaXRhZGEgYW8gaW50ZXJ2YWxvIFswLCAxXSwgbyBxdWUgZmFjaWxpdGEgbyBjw6FsY3VsbyBkZSBwcm9iYWJpbGlkYWRlcy4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIlBlbnNlIHNvYnJlIG8gcXVlIGFjb250ZWNlIHF1YW5kbyBzdWJzdGl0dcOtbW9zIG8gcGFyw6JtZXRybyBwb3B1bGFjaW9uYWwgJFxcc2lnbWEkIHBlbG8gZXN0aW1hZG9yIGFtb3N0cmFsICRTJC4gQSBpbmNlcnRlemEgYXVtZW50YT8iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkFvIHV0aWxpemFyICRTJCBjb21vIGVzdGltYWRvciBkZSAkXFxzaWdtYSQsIGludHJvZHV6aW1vcyB1bWEgZm9udGUgYWRpY2lvbmFsIGRlIHZhcmlhYmlsaWRhZGUgbm9zIGRhZG9zLCBwb2lzICRTJCB2YXJpYSBlbnRyZSBkaWZlcmVudGVzIGFtb3N0cmFzLiBBIGRpc3RyaWJ1acOnw6NvICR0JCBkZSBTdHVkZW50IMOpIGNvbnN0cnXDrWRhIG1hdGVtYXRpY2FtZW50ZSBwYXJhIHNlciBtYWlzIGRpc3BlcnNhIChjYXVkYXMgbWFpcyBwZXNhZGFzKSBxdWUgYSBub3JtYWwgcGFkcsOjbyAkTigwLDEpJCwganVzdGFtZW50ZSBwYXJhIGluY29ycG9yYXIgZXNzYSBpbmNlcnRlemEgZXh0cmEuIElzc28gdG9ybmEgbyB0ZXN0ZSBtYWlzIGNvbnNlcnZhZG9yIChpbnRlcnZhbG9zIGRlIGNvbmZpYW7Dp2EgbWFpcyBhbXBsb3MsIHJlZ2nDtWVzIGRlIHJlamVpw6fDo28gbWFpcyBkaXN0YW50ZXMgZGEgbcOpZGlhKSBkbyBxdWUgc2UgdXPDoXNzZW1vcyBhIG5vcm1hbCBxdWFuZG8gJFxcc2lnbWEkIMOpIGRlc2NvbmhlY2lkby4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAyMDApXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLm5vcm0ucGRmKHgpLCBuYW1lPSdOKDAsMSknLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0yKSkpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLnQucGRmKHgsIGRmPTUpLCBuYW1lPSd0KGdsPTUpJywgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJywgd2lkdGg9MikpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkNvbXBhcmHDp8OjbzogTm9ybWFsIFBhZHLDo28gdnMuIHQgZGUgU3R1ZGVudDwvYj4nLCB4YXhpc190aXRsZT0nRXN0YXTDrXN0aWNhIGRlIFRlc3RlJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnLCBsZWdlbmQ9ZGljdChvcmllbnRhdGlvbj0naCcsIHlhbmNob3I9J2JvdHRvbScsIHk9MS4wMiwgeGFuY2hvcj0ncmlnaHQnLCB4PTEuMCkpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgNywgcC4gMTkxIn0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBkZSBjb250cm9sZSBkZSBxdWFsaWRhZGUgbmEgZW5nZW5oYXJpYSBkZSBwcm9kdcOnw6NvIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcywgdW0gZW5nZW5oZWlybyBhbmFsaXNhIGEgcmVzaXN0w6puY2lhIMOgIHRyYcOnw6NvIGRlIHVtYSBsaWdhIG1ldMOhbGljYSByZWPDqW0tZGVzZW52b2x2aWRhLiBDb21vIG8gZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsICRcXHNpZ21hJCDDqSBkZXNjb25oZWNpZG8sIGVsZSB1dGlsaXphIG8gZGVzdmlvIHBhZHLDo28gYW1vc3RyYWwgJFMkIHBhcmEgY29uc3RydWlyIGEgZXN0YXTDrXN0aWNhICRUID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdX17Uy9cXHNxcnR7bn19JC4gQW8gY29tcGFyYXIgYSBjdXJ2YSBkYSBkaXN0cmlidWnDp8OjbyAkdChuLTEpJCBjb20gYSBkYSBub3JtYWwgcGFkcsOjbyAkTigwLCAxKSQsIG9ic2VydmEtc2UgcXVlLCBwYXJhIHVtYSBhbW9zdHJhIHBlcXVlbmEsIGEgY3VydmEgJHQkIGFwcmVzZW50YSBjYXVkYXMgbWFpcyBwZXNhZGFzLiBRdWFsIGRhcyBhbHRlcm5hdGl2YXMgYWJhaXhvIG1lbGhvciBkZXNjcmV2ZSBhIGltcGxpY2HDp8OjbyBlc3RhdMOtc3RpY2EgZGVzc2EgY2FyYWN0ZXLDrXN0aWNhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQXMgY2F1ZGFzIHBlc2FkYXMgaW5kaWNhbSBxdWUgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCDDqSB1bSBlc3RpbWFkb3IgZW52aWVzYWRvIGRlICRcXG11JCBlbSBhbW9zdHJhcyBwZXF1ZW5hcy4iLCAiQiI6ICJBIGRpc3BlcnPDo28gZXh0cmEgaW50cm9kdXppZGEgcGVsYSBzdWJzdGl0dWnDp8OjbyBkZSAkXFxzaWdtYSQgcG9yICRTJCBleGlnZSB2YWxvcmVzIGNyw610aWNvcyBtYWlvcmVzIHBhcmEgdW0gbWVzbW8gbsOtdmVsIGRlIGNvbmZpYW7Dp2EsIGF1bWVudGFuZG8gYSBtYXJnZW0gZGUgZXJybyAkRSQuIiwgIkMiOiAiQSBlc3RhdMOtc3RpY2EgJFQkIGNvbnZlcmdlIHBhcmEgJE4oMCwxKSQgaW5zdGFudGFuZWFtZW50ZSwgaW5kZXBlbmRlbnRlbWVudGUgZG8gdmFsb3IgZGUgJG4kLCB0b3JuYW5kbyBhIGRpc3RpbsOnw6NvIGlycmVsZXZhbnRlIHBhcmEgYSBpbmZlcsOqbmNpYS4iLCAiRCI6ICJBIHZhcmnDom5jaWEgZGEgZXN0YXTDrXN0aWNhICRUJCDDqSBzZW1wcmUgbWVub3IgcXVlIDEsIG8gcXVlIHJlZHV6IGEgcHJvYmFiaWxpZGFkZSBkZSBlcnJvcyB0aXBvIEkgZW0gdGVzdGVzIGRlIGhpcMOzdGVzZXMuIiwgIkUiOiAiTyBjb21wb3J0YW1lbnRvIGRlIGNhdWRhcyBwZXNhZGFzIMOpIHVtIGFydGVmYXRvIG51bcOpcmljbyBxdWUgZGVzYXBhcmVjZSBhbyBhdW1lbnRhciBhIHByZWNpc8OjbyBkZSAkUyQsIG1hcyBuw6NvIGFmZXRhIGEgZm9ybWEgZGEgZGlzdHJpYnVpw6fDo28uIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJSZWZsaXRhIHNvYnJlIGNvbW8gYSBpbmNlcnRlemEgYWRpY2lvbmFsIGRhIGVzdGltYXRpdmEgZGUgdmFyaWFiaWxpZGFkZSAoJFMkKSBhZmV0YSBhIGRpc3RyaWJ1acOnw6NvIGRlIHByb2JhYmlsaWRhZGVzIG5hcyBleHRyZW1pZGFkZXMgKGNhdWRhcykgZGEgY3VydmEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIHN1YnN0aXR1acOnw6NvIGRlICRcXHNpZ21hJCBwb3IgJFMkIGFkaWNpb25hIHVtYSBmb250ZSBkZSB2YXJpYcOnw6NvIGVzdG9jw6FzdGljYSwgcG9pcyAkUyQgw6kgdW1hIHZhcmnDoXZlbCBhbGVhdMOzcmlhLiBJc3NvIGZheiBjb20gcXVlIGEgZXN0YXTDrXN0aWNhICRUJCB0ZW5oYSB1bWEgdmFyacOibmNpYSBzdXBlcmlvciDDoCBkYSBub3JtYWwgcGFkcsOjby4gQ29uc2VxdWVudGVtZW50ZSwgcGFyYSB1bSBkYWRvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQsIG9zIHBvbnRvcyBjcsOtdGljb3MgJHRfe1xcdGV4dHtjcml0fX0kIHPDo28gbWFpcyBhZmFzdGFkb3MgZGUgemVybyBkbyBxdWUgb3MgcG9udG9zIGNyw610aWNvcyAkWl97XFx0ZXh0e2NyaXR9fSQuIElzc28gcmVmbGV0ZSBuYSBuZWNlc3NpZGFkZSBkZSB1bWEgbWFyZ2VtIGRlIGVycm8gJEUkIG1haW9yIHBhcmEgY29icmlyIGEgaW5jZXJ0ZXphIGFkaWNpb25hbCBlbSBhbW9zdHJhcyBwZXF1ZW5hcywgcHJvdGVnZW5kbyBvIHBlc3F1aXNhZG9yIGNvbnRyYSBzdWJlc3RpbWFyIG8gZXJybyBhbW9zdHJhbC4iLCAiY29kaWdvX3Bsb3RseSI6ICJ4ID0gbnAubGluc3BhY2UoLTQsIDQsIDIwMClcbmZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLm5vcm0ucGRmKHgpLCBuYW1lPSdOKDAsMSknLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0yKSkpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLnQucGRmKHgsIGRmPTMpLCBuYW1lPSd0KGdsPTMpJywgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJywgd2lkdGg9MiwgZGFzaD0nXFxkb3QnKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nQ29tcGFyYcOnw6NvOiBOb3JtYWwgUGFkcsOjbyB2cyB0IGRlIFN0dWRlbnQgKGdsPTMpJywgeGF4aXNfdGl0bGU9J0VzdGF0w61zdGljYScsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCA3In0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBvIGNvbXBvcnRhbWVudG8gYXNzaW50w7N0aWNvIGRhIGVzdGF0w61zdGljYSAkVCA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXV9e1MvXFxzcXJ0e259fSQgY29tICRnbCA9IG4tMSQgZ3JhdXMgZGUgbGliZXJkYWRlLiBFbSB1bSBlbnNhaW8gY2zDrW5pY28sIG8gdGFtYW5obyBkYSBhbW9zdHJhICRuJCBhdW1lbnRhIHByb2dyZXNzaXZhbWVudGUgZGUgMTAgcGFyYSAxMDAwLiBPIHF1ZSBvY29ycmUgY29tIGEgZGlzdHJpYnVpw6fDo28gZGEgZXN0YXTDrXN0aWNhICRUJCBuZXNzZSBwcm9jZXNzbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgZGlzdHJpYnVpw6fDo28gdG9ybmEtc2UgcHJvZ3Jlc3NpdmFtZW50ZSBtYWlzIGFzc2ltw6l0cmljYSwgaW52YWxpZGFuZG8gbyB1c28gZGUgbcOpdG9kb3MgcGFyYW3DqXRyaWNvcy4iLCAiQiI6ICJBIHZhcmnDom5jaWEgZGEgZXN0YXTDrXN0aWNhICRUJCB0ZW5kZSBhIGluZmluaXRvLCBmYXplbmRvIGNvbSBxdWUgYSBtw6lkaWEgYW1vc3RyYWwgcGVyY2Egc3VhIGNvbnNpc3TDqm5jaWEuIiwgIkMiOiAiQSBkaXN0cmlidWnDp8OjbyAkdChuLTEpJCBjb252ZXJnZSBlbSBkaXN0cmlidWnDp8OjbyBwYXJhICROKDAsMSkkLCB2aXN0byBxdWUgJFNeMiQgY29udmVyZ2UgZW0gcHJvYmFiaWxpZGFkZSBwYXJhICRcXHNpZ21hXjIkIChjb25zaXN0w6puY2lhIGRvIGVzdGltYWRvciBkZSB2YXJpw6JuY2lhKS4iLCAiRCI6ICJBIGVzdGF0w61zdGljYSAkVCQgdHJhbnNmb3JtYS1zZSBlbSB1bWEgZGlzdHJpYnVpw6fDo28gUXVpLVF1YWRyYWRvIGRldmlkbyBhbyBhY8O6bXVsbyBkZSBncmF1cyBkZSBsaWJlcmRhZGUuIiwgIkUiOiAiTyBwLXZhbG9yIGNhbGN1bGFkbyBwZWxhIGRpc3RyaWJ1acOnw6NvICR0JCB0b3JuYS1zZSBjYWRhIHZleiBtZW5vciwgaW5kZXBlbmRlbnRlbWVudGUgZGEgdmVyYWNpZGFkZSBkYSBoaXDDs3Rlc2UgbnVsYSAkSF8wJC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIkNvbnNpZGVyZSBhIExlaSBkb3MgR3JhbmRlcyBOw7ptZXJvcyBhcGxpY2FkYSDDoCB2YXJpw6JuY2lhIGFtb3N0cmFsICRTXjIkIGNvbmZvcm1lIG8gdGFtYW5obyBkYSBhbW9zdHJhICRuJCBjcmVzY2UuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICLDgCBtZWRpZGEgcXVlICRuIFxcdG8gXFxpbmZ0eSQsIG8gZXN0aW1hZG9yICRTXjIkIGNvbnZlcmdlIGVtIHByb2JhYmlsaWRhZGUgcGFyYSBvIHBhcsOibWV0cm8gcG9wdWxhY2lvbmFsICRcXHNpZ21hXjIkLiBBc3NpbSwgYSByYXrDo28gJFMvXFxzaWdtYSQgdGVuZGUgYSAxLiBBIGVzdGF0w61zdGljYSAkVCA9IFxcZnJhY3tcXGJhcntYfS1cXG11fXtTL1xcc3FydHtufX0gPSBcXGxlZnQoIFxcZnJhY3tcXGJhcntYfS1cXG11fXtcXHNpZ21hL1xcc3FydHtufX0gXFxyaWdodCkgXFxjZG90IFxcbGVmdCggXFxmcmFje1xcc2lnbWF9e1N9IFxccmlnaHQpJC4gQ29tbyBvIHByaW1laXJvIHRlcm1vIGNvbnZlcmdlIHBhcmEgJE4oMCwxKSQgKFRlb3JlbWEgQ2VudHJhbCBkbyBMaW1pdGUpIGUgbyBzZWd1bmRvIHRlcm1vIGNvbnZlcmdlIHBhcmEgMSwgcG9yIFNsdXRza3ksICRUJCBjb252ZXJnZSBwYXJhICROKDAsMSkkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW0gZW5nZW5oZWlybyBkZSBxdWFsaWRhZGUgZW0gdW1hIHBsYW50YSBkZSBtYW51ZmF0dXJhIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyBkZXNlamEgZXN0aW1hciBhIHZpZGEgw7p0aWwgbcOpZGlhICgkXFxtdSQpIGRlIHVtIG5vdm8gbG90ZSBkZSBjYXBhY2l0b3Jlcy4gRWxlIHNlbGVjaW9uYSB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIGRlICRuID0gMTYkIHVuaWRhZGVzIGUgb2J0w6ltIHVtYSBtw6lkaWEgYW1vc3RyYWwgZGUgJFxcYmFye1h9ID0gMTUwMCQgaG9yYXMsIGNvbSB1bSBkZXN2aW8gcGFkcsOjbyBhbW9zdHJhbCBkZSAkUyA9IDIwMCQgaG9yYXMuIEFzc3VtaW5kbyBxdWUgYSB2aWRhIMO6dGlsIGRlc3NlcyBjYXBhY2l0b3JlcyBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLCBxdWFsIMOpIG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgZGUgOTUlIHBhcmEgYSBtw6lkaWEgcG9wdWxhY2lvbmFsPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiMTUwMCDCsSA0Miw0MiIsICJCIjogIjE1MDAgwrEgMTA2LDcyIiwgIkMiOiAiMTUwMCDCsSA1MCwwMCIsICJEIjogIjE1MDAgwrEgOTgsMDAiLCAiRSI6ICIxNTAwIMKxIDIxMyw0NCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRlIHF1ZSwgcXVhbmRvIGEgdmFyacOibmNpYSBwb3B1bGFjaW9uYWwgw6kgZGVzY29uaGVjaWRhIGUgbyB0YW1hbmhvIGRhIGFtb3N0cmEgw6kgcGVxdWVubywgdXRpbGl6YW1vcyBhIGRpc3RyaWJ1acOnw6NvIHQgZGUgU3R1ZGVudC4gVmVyaWZpcXVlIG8gdmFsb3IgY3LDrXRpY28gJHRfe1xcYWxwaGEvMiwgZ2x9JCBwYXJhICRnbCA9IG4tMSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIGNvbnN0cnVpciBvIGludGVydmFsbyBkZSBjb25maWFuw6dhIGNvbSB2YXJpw6JuY2lhIGRlc2NvbmhlY2lkYSwgdXRpbGl6YW1vcyBhIGbDs3JtdWxhICRJQyhcXG11OyAxLVxcYWxwaGEpID0gXFxiYXJ7WH0gXFxwbSB0X3tcXGFscGhhLzIsIGdsfSBcXGNkb3QgXFxmcmFje1N9e1xcc3FydHtufX0kLiBUZW1vcyAkbj0xNiQsIGxvZ28gJGdsID0gMTUkLiBQYXJhIHVtIG7DrXZlbCBkZSBjb25maWFuw6dhIGRlIDk1JSwgJFxcYWxwaGEgPSAwLDA1JCBlICRcXGFscGhhLzIgPSAwLDAyNSQuIE8gdmFsb3IgY3LDrXRpY28gJHRfezAsMDI1LCAxNX0gXFxhcHByb3ggMiwxMzEkLiBPIGVycm8gcGFkcsOjbyDDqSAkRVAoXFxiYXJ7WH0pID0gUy9cXHNxcnR7bn0gPSAyMDAvNCA9IDUwJC4gQSBtYXJnZW0gZGUgZXJybyDDqSAkRSA9IDIsMTMxIFxcY2RvdCA1MCA9IDEwNiw1NSQuIEFqdXN0YW5kbyBwZWxhIHByZWNpc8OjbyBkYSB0YWJlbGEgdCwgZW5jb250cmFtb3MgJDEwNiw3MiQuIFBvcnRhbnRvLCBvIGludGVydmFsbyDDqSAkMTUwMCBcXHBtIDEwNiw3MiQuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVsxMzkzLjI4LCAxNjA2LjcyXSwgeT1bMSwgMV0sIG1vZGU9J2xpbmVzK21hcmtlcnMnLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0zKSwgbmFtZT0nSW50ZXJ2YWxvIGRlIENvbmZpYW7Dp2EnKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVsxNTAwXSwgeT1bMV0sIG1vZGU9J21hcmtlcnMnLCBtYXJrZXI9ZGljdChjb2xvcj0nIzk5MUIxQicsIHNpemU9MTIpLCBuYW1lPSdNw6lkaWEgQW1vc3RyYWwgKCRcXGJhcntYfSQpJykpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+SW50ZXJ2YWxvIGRlIENvbmZpYW7Dp2EgOTUlIGRhIFZpZGEgw5p0aWw8L2I+JywgeGF4aXM9ZGljdCh0aXRsZT0nSG9yYXMnKSwgeWF4aXM9ZGljdChzaG93dGlja2xhYmVscz1GYWxzZSwgcmFuZ2U9KSwgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTEsIHAuIDMxMyJ9LCB7ImVudW5jaWFkbyI6ICJEdXJhbnRlIHVtIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBkZSB1bSBsb3RlLCB1bSBwZXNxdWlzYWRvciBjb2xldG91IHVtYSBhbW9zdHJhIGRlIDI1IHBlw6dhcyBlIGNhbGN1bG91IHVtYSBtw6lkaWEgZGUgcmVzaXN0w6puY2lhIGRlIDEyMCBrZ2YgY29tIHVtIGRlc3ZpbyBwYWRyw6NvIGFtb3N0cmFsIGRlIDEwIGtnZi4gU2UgZWxlIGRlY2lkaXIgY2FsY3VsYXIgdW0gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgcGFyYSBhIG3DqWRpYSBjb20gbsOtdmVsIGRlIDk5JSBkZSBjb25maWFuw6dhIGVtIHZleiBkZSA5NSUsIG8gcXVlIG9jb3JyZXLDoSBjb20gYSBhbXBsaXR1ZGUgZG8gaW50ZXJ2YWxvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBhbXBsaXR1ZGUgZGltaW51aXLDoSwgcG9pcyBvIG7DrXZlbCBkZSBjb25maWFuw6dhIG1haW9yIGV4aWdlIHVtIHZhbG9yIGNyw610aWNvIG1lbm9yLiIsICJCIjogIkEgYW1wbGl0dWRlIHBlcm1hbmVjZXLDoSBpbmFsdGVyYWRhLCBwb2lzIGRlcGVuZGUgYXBlbmFzIGRvcyBkYWRvcyBkYSBhbW9zdHJhLiIsICJDIjogIkEgYW1wbGl0dWRlIGF1bWVudGFyw6EsIHBvaXMgbyB2YWxvciBjcsOtdGljbyAkdF97XFxhbHBoYS8yLCBnbH0kIGF1bWVudGEgY29tIG8gbsOtdmVsIGRlIGNvbmZpYW7Dp2EuIiwgIkQiOiAiQSBhbXBsaXR1ZGUgc2UgdG9ybmFyw6EgZXhhdGFtZW50ZSBvIGRvYnJvIGRhIGFudGVyaW9yLiIsICJFIjogIkEgYW1wbGl0dWRlIGRlcGVuZGVyw6EgZG8gdmFsb3IgZGUgJFxcYmFye1h9JCwgcXVlIG7Do28gZm9pIGFsdGVyYWRvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiQW5hbGlzZSBjb21vIG8gdGVybW8gJHRfe1xcYWxwaGEvMiwgZ2x9JCBzZSBjb21wb3J0YSBxdWFuZG8gJFxcYWxwaGEkIGRpbWludWkgcGFyYSBhdW1lbnRhciBvIG7DrXZlbCBkZSBjb25maWFuw6dhICgkMS1cXGFscGhhJCkuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGFtcGxpdHVkZSBkZSB1bSBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSDDqSBkYWRhIHBvciAkMiBcXGNkb3QgdF97XFxhbHBoYS8yLCBnbH0gXFxjZG90IFxcZnJhY3tTfXtcXHNxcnR7bn19JC4gQW8gZWxldmFyIG8gbsOtdmVsIGRlIGNvbmZpYW7Dp2EgZGUgOTUlIHBhcmEgOTklLCByZWR1emltb3MgJFxcYWxwaGEkIGRlIDAsMDUgcGFyYSAwLDAxLCBvIHF1ZSBmYXogY29tIHF1ZSBhIMOhcmVhIG5hcyBjYXVkYXMgZGltaW51YSBlLCBjb25zZXF1ZW50ZW1lbnRlLCBvIHZhbG9yIGNyw610aWNvICR0X3tcXGFscGhhLzIsIGdsfSQgYXVtZW50ZS4gQ29tbyBvcyBkZW1haXMgdGVybW9zICgkUyQgZSAkbiQpIHBlcm1hbmVjZW0gY29uc3RhbnRlcywgbyBhdW1lbnRvIGRvIHZhbG9yIGNyw610aWNvIGltcGxpY2EgbmVjZXNzYXJpYW1lbnRlIHVtIGF1bWVudG8gbmEgYW1wbGl0dWRlIGRvIGludGVydmFsby4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtYSBsaW5oYSBkZSBtb250YWdlbSBhdXRvbWF0aXphZGEgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zLCBvIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBtZWRlIGEgcmVzaXN0w6puY2lhICgkXFxPbWVnYSQpIGRlIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgZGUgJG49MzYkIHVuaWRhZGVzLCBvYnRlbmRvIHVtYSBtw6lkaWEgJFxcYmFye1h9ID0gMTIwXFxPbWVnYSQgZSB1bSBkZXN2aW8gcGFkcsOjbyBhbW9zdHJhbCAkUyA9IDEyXFxPbWVnYSQuIENvbnNpZGVyYW5kbyB1bSBuw612ZWwgZGUgY29uZmlhbsOnYSBkZSA5NSUgKCQxLVxcYWxwaGE9MCw5NSQpLCBxdWFsIGRhcyBpbnRlcnByZXRhw6fDtWVzIGFiYWl4byByZWZsZXRlIGNvcnJldGFtZW50ZSBvIHNpZ25pZmljYWRvIGVzdGF0w61zdGljbyBkbyAkSUMkIGNvbnN0cnXDrWRvIHBhcmEgYSByZXNpc3TDqm5jaWEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJFeGlzdGUgOTUlIGRlIHByb2JhYmlsaWRhZGUgZGUgcXVlIGEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQgZXN0ZWphIGNvbnRpZGEgZXhhdGFtZW50ZSBubyBpbnRlcnZhbG8gY2FsY3VsYWRvLiIsICJCIjogIlNlIHJlcGV0aXJtb3MgbyBwcm9jZWRpbWVudG8gZGUgY29sZXRhIGUgY29uc3RydcOnw6NvIGRvIGludGVydmFsbyBkZXplbmFzIGRlIHZlemVzLCBhcHJveGltYWRhbWVudGUgOTUlIGRlc3NlcyBpbnRlcnZhbG9zIGNvbnRlcsOjbyBvIHZlcmRhZGVpcm8gcGFyw6JtZXRybyBwb3B1bGFjaW9uYWwgJFxcbXUkLiIsICJDIjogIk8gcGFyw6JtZXRybyAkXFxtdSQgdGVtIDk1JSBkZSBjaGFuY2UgZGUgdmFyaWFyIGRlbnRybyBkb3MgbGltaXRlcyBlc3RhYmVsZWNpZG9zIHBlbGEgYW1vc3RyYS4iLCAiRCI6ICJBIGFtcGxpdHVkZSBkbyBpbnRlcnZhbG8gZGltaW51aXLDoSBzZSBhdW1lbnRhcm1vcyBvIGRlc3ZpbyBwYWRyw6NvIGFtb3N0cmFsICRTJCwgbWFudGVuZG8gbyB0YW1hbmhvIGRhIGFtb3N0cmEgJG4kIGNvbnN0YW50ZS4iLCAiRSI6ICJPIG7DrXZlbCBkZSBjb25maWFuw6dhIGRlIDk1JSBnYXJhbnRlIHF1ZSBhIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0kIMOpIGlndWFsIMOgIG3DqWRpYSBwb3B1bGFjaW9uYWwgJFxcbXUkIGVtIDk1JSBkb3MgY2Fzb3Mgb2JzZXJ2YWRvcy4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBuYXR1cmV6YSBmcmVxdWVudGlzdGEgZGEgaW5mZXLDqm5jaWEgZXN0YXTDrXN0aWNhOiBvIHBhcsOibWV0cm8gcG9wdWxhY2lvbmFsIMOpIGZpeG8sIG7Do28gdW1hIHZhcmnDoXZlbCBhbGVhdMOzcmlhLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBpbnRlcnByZXRhw6fDo28gZnJlcXVlbnRpc3RhIGRvIGludGVydmFsbyBkZSBjb25maWFuw6dhIChJQykgYmFzZWlhLXNlIG5hIHJvYnVzdGV6IGRvIHByb2NlZGltZW50byBkZSBhbW9zdHJhZ2VtLiBPIHBhcsOibWV0cm8gJFxcbXUkIG7Do28gw6kgdW1hIHZhcmnDoXZlbCBhbGVhdMOzcmlhLCBwb3J0YW50bywgbsOjbyBmYXogc2VudGlkbyBhdHJpYnVpciBwcm9iYWJpbGlkYWRlIGEgZWxlIGVzdGFyIGNvbnRpZG8gZW0gdW0gaW50ZXJ2YWxvIGVzcGVjw61maWNvLiBPIGNvcnJldG8gw6kgYWZpcm1hciBxdWUsIGVtIHVtYSBzZXF1w6puY2lhIGRlIHJlcGV0acOnw7VlcyBkbyBleHBlcmltZW50bywgYSBwcm9wb3LDp8OjbyBkZSBpbnRlcnZhbG9zIHF1ZSBjb2JyZW0gbyB2ZXJkYWRlaXJvICRcXG11JCBjb252ZXJnaXLDoSBwYXJhIG8gbsOtdmVsIGRlIGNvbmZpYW7Dp2EgKDEtJFxcYWxwaGEkKS4gQWx0ZXJuYXRpdmFzIHF1ZSBtZW5jaW9uYW0gJ3Byb2JhYmlsaWRhZGUgZG8gcGFyw6JtZXRybyBlc3RhciBkZW50cm8nIGNvbWV0ZW0gdW0gZXJybyBjb25jZWl0dWFsIGNsw6Fzc2ljbyBlbSBpbmZlcsOqbmNpYS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDExLCBwLiAzMTIifSwgeyJlbnVuY2lhZG8iOiAiVW0gZW5nZW5oZWlybyBkZSBwcm9jZXNzb3MgZGVzZWphIHJlZHV6aXIgYSBhbXBsaXR1ZGUgZGUgdW0gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgcGFyYSBhIHZhesOjbyBtw6lkaWEgKCRcXG11JCkgZGUgdW0gZmx1aWRvIGVtIHVtYSB0dWJ1bGHDp8Ojby4gQXR1YWxtZW50ZSwgZWxlIHV0aWxpemEgJG49NjQkIG9ic2VydmHDp8O1ZXMuIFNhYmVuZG8gcXVlIG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSDDqSBkYWRvIHBvciAkRVAoXFxiYXJ7WH0pID0gUyAvIFxcc3FydHtufSQsIHF1YWwgYcOnw6NvIMOpIG1hdGVtYXRpY2FtZW50ZSBlZmljYXogcGFyYSByZWR1emlyIGEgYW1wbGl0dWRlIGRvICRJQyQgcGVsYSBtZXRhZGUsIG1hbnRlbmRvIG8gZGVzdmlvIHBhZHLDo28gJFMkIGUgbyB2YWxvciBjcsOtdGljbyAkdF97XFxhbHBoYS8yLCBnbH0kIGNvbnN0YW50ZXM/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJSZWR1emlyIG8gdGFtYW5obyBkYSBhbW9zdHJhIHBhcmEgJG49MTYkLiIsICJCIjogIkF1bWVudGFyIG8gdGFtYW5obyBkYSBhbW9zdHJhIHBhcmEgJG49MTI4JC4iLCAiQyI6ICJBdW1lbnRhciBvIHRhbWFuaG8gZGEgYW1vc3RyYSBwYXJhICRuPTI1NiQuIiwgIkQiOiAiTWFudGVyIG8gdGFtYW5obyBkYSBhbW9zdHJhIGUgYXVtZW50YXIgbyBuw612ZWwgZGUgY29uZmlhbsOnYSBwYXJhIDk5JS4iLCAiRSI6ICJEb2JyYXIgbyB2YWxvciBkbyBkZXN2aW8gcGFkcsOjbyBhbW9zdHJhbCAkUyQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJBbmFsaXNlIGEgZsOzcm11bGEgZGEgYW1wbGl0dWRlIGRvIGludGVydmFsbyAkTCA9IDIgXFxjZG90IHRfe1xcYWxwaGEvMiwgZ2x9IFxcY2RvdCAoUyAvIFxcc3FydHtufSkkIGUgb2JzZXJ2ZSBhIHJlbGHDp8OjbyBlbnRyZSAkTCQgZSAkXFxzcXJ0e259JC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgYW1wbGl0dWRlIGRvICRJQyQgw6kgcHJvcG9yY2lvbmFsIGEgJDEvXFxzcXJ0e259JC4gUGFyYSByZWR1emlyIGEgYW1wbGl0dWRlIHBlbGEgbWV0YWRlICgkTF97bm92b30gPSBMLzIkKSwgcHJlY2lzYW1vcyBxdWUgbyB0ZXJtbyAkMS9cXHNxcnR7bn0kIHNlamEgcmVkdXppZG8gcGVsYSBtZXRhZGUsIG91IHNlamEsICRcXHNxcnR7bl97bm92b319ID0gMiBcXGNkb3QgXFxzcXJ0e25fe2F0dWFsfX0kLiBFbGV2YW5kbyBhbWJvcyBvcyBsYWRvcyBhbyBxdWFkcmFkbywgdGVtb3MgJG5fe25vdm99ID0gNCBcXGNkb3Qgbl97YXR1YWx9JC4gQ29tICRuX3thdHVhbH09NjQkLCBvIG5vdm8gdGFtYW5obyBkZXZlIHNlciAkNjQgXFx0aW1lcyA0ID0gMjU2JC4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKTsgZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9WzE2LCA2NCwgMTQ0LCAyNTZdLCB5PVswLjUsIDAuMjUsIDAuMTYsIDAuMTI1XSwgbW9kZT0nbGluZXMrbWFya2VycycsIG5hbWU9J0FtcGxpdHVkZSBSZWxhdGl2YScsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScpKSk7IGZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdFZmVpdG8gZG8gVGFtYW5obyBBbW9zdHJhbCBuYSBQcmVjaXPDo28nLCB4YXhpc190aXRsZT0nVGFtYW5obyBkYSBhbW9zdHJhIChuKScsIHlheGlzX3RpdGxlPSdGYXRvciBkZSBhbXBsaXR1ZGUgKDEvXFxzcXJ0KG4pKScpOyIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH1dLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGNsw61uaWNvLCBvIG7DrXZlbCBkZSBjb3J0aXNvbCBkZSAkbj0xMCQgcGFjaWVudGVzIGZvaSBtZWRpZG8uIEEgbcOpZGlhIGFtb3N0cmFsIGZvaSBkZSAkXFxiYXJ7WH0gPSAxNS4wJCAkXFxtdSBnL2RMJCBlIG8gZGVzdmlvIHBhZHLDo28gYW1vc3RyYWwgZm9pICRTID0gMy4wJCAkXFxtdSBnL2RMJC4gU2FiZW5kbyBxdWUgbyBuw612ZWwgcG9wdWxhY2lvbmFsIG3DqWRpbyAkXFxtdSQgw6kgYWx2byBkZSBpbnZlc3RpZ2HDp8OjbywgY2FsY3VsZSBvIHZhbG9yIGRhIGVzdGF0w61zdGljYSAkdF97XFx0ZXh0e2NhbGN9fSQgcGFyYSB0ZXN0YXIgYSBoaXDDs3Rlc2UgJEhfMDogXFxtdSA9IDEyLjAkLiIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSBkYSBlc3RhdMOtc3RpY2EgdDogJFQgPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11fXtTL1xcc3FydHtufX0kIGNvbSAkbj0xMCQgZ3JhdXMgZGUgbGliZXJkYWRlIGFqdXN0YWRvcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiSWRlbnRpZmljYW1vcyBvcyBkYWRvcyBmb3JuZWNpZG9zOiAkXFxiYXJ7WH0gPSAxNS4wJCwgJFxcbXVfMCA9IDEyLjAkLCAkUyA9IDMuMCQgZSAkbiA9IDEwJC4iLCAiQ2FsY3VsYW1vcyBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWE6ICRFUChcXGJhcntYfSkgPSBcXGZyYWN7U317XFxzcXJ0e259fSA9IFxcZnJhY3szLjB9e1xcc3FydHsxMH19IFxcYXBwcm94IFxcZnJhY3szLjB9ezMuMTYyfSBcXGFwcHJveCAwLjk0ODckLiIsICJBcGxpY2Ftb3MgYSBmw7NybXVsYSBkYSBlc3RhdMOtc3RpY2EgJHQkOiAkJHRfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11XzB9e0VQKFxcYmFye1h9KX0gPSBcXGZyYWN7MTUuMCAtIDEyLjB9ezAuOTQ4N30gPSBcXGZyYWN7My4wfXswLjk0ODd9IFxcYXBwcm94IDMuMTYyJCQiLCAiQ29uY2x1c8OjbzogTyB2YWxvciBvYnNlcnZhZG8gJHRfe1xcdGV4dHtjYWxjfX0gXFxhcHByb3ggMy4xNjIkIGNvbSAkZ2wgPSAxMCAtIDEgPSA5JCBncmF1cyBkZSBsaWJlcmRhZGUuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAzLjE2Mn0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCBkbyBwb250byBkZSB2aXN0YSBkYSBpbmNlcnRlemEgZXN0YXTDrXN0aWNhLCBwb3IgcXVlIGEgdmFyacOibmNpYSBhbW9zdHJhbCAkU14yJCB1dGlsaXphICRuLTEkIGdyYXVzIGRlIGxpYmVyZGFkZSBubyBkZW5vbWluYWRvciBlbSB2ZXogZGUgJG4kLiBDb21vIGlzc28gc2UgY29uZWN0YSBjb20gYSBuZWNlc3NpZGFkZSBkYSBkaXN0cmlidWnDp8OjbyAkdCQgZGUgU3R1ZGVudCBhbyBlc3RpbWFyICRcXG11JD8iLCAiZGljYSI6ICJDb25zaWRlcmUgcXVlICRcXGJhcntYfSQgw6kgY2FsY3VsYWRvIGEgcGFydGlyIGRvcyBtZXNtb3MgZGFkb3MgJFhfaSQgcXVlIHVzYW1vcyBwYXJhIGNhbGN1bGFyICRTXjIkLCBvIHF1ZSBpbXDDtWUgdW1hIHJlc3RyacOnw6NvIGxpbmVhci4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSB2YXJpw6JuY2lhIGFtb3N0cmFsIMOpIGRhZGEgcG9yICRTXjIgPSBcXGZyYWN7MX17bi0xfSBcXHN1bV97aT0xfV5uIChYX2kgLSBcXGJhcntYfSleMiQuIiwgIkFvIHV0aWxpemFybW9zIGEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSQgcGFyYSBjYWxjdWxhciBvcyBkZXN2aW9zLCBwZXJkZW1vcyB1bSBncmF1IGRlIGxpYmVyZGFkZSwgcG9pcyAkXFxzdW0gKFhfaSAtIFxcYmFye1h9KSA9IDAkLiBBc3NpbSwgYXBlbmFzICRuLTEkIG9ic2VydmHDp8O1ZXMgc8OjbyBsaW5lYXJtZW50ZSBpbmRlcGVuZGVudGVzLiIsICJEaXZpZGlyIHBvciAkbi0xJCBnYXJhbnRlIHF1ZSAkRShTXjIpID0gXFxzaWdtYV4yJCwgdG9ybmFuZG8gJFNeMiQgdW0gZXN0aW1hZG9yIG7Do28tdmljaWFkby4iLCAiQSBuZWNlc3NpZGFkZSBkYSBkaXN0cmlidWnDp8OjbyAkdCQgc3VyZ2UgcG9ycXVlICRTJCDDqSB1bWEgdmFyacOhdmVsIGFsZWF0w7NyaWEgZGVwZW5kZW50ZSBkZSAkXFxiYXJ7WH0kIGUgdGVtIHZhcmlhYmlsaWRhZGUgcHLDs3ByaWEuIEFvIHN1YnN0aXR1aXIgJFxcc2lnbWEkIHBvciAkUyQsIGEgaW5jZXJ0ZXphIGRvIGVzdGltYWRvciAkU14yJCBzZSBwcm9wYWdhIHBhcmEgYSBlc3RhdMOtc3RpY2EgJFQkLCBleGlnaW5kbyBvIGFqdXN0ZSBkYXMgY2F1ZGFzIHBlc2FkYXMgZGEgZGlzdHJpYnVpw6fDo28gJHQkIHBhcmEgbWFudGVyIG8gcmlnb3IgaW5mZXJlbmNpYWwuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTEsIHAuIDMwMiIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJTdXBvbmhhIHF1ZSwgcGFyYSB1bWEgdmFyacOhdmVsIGFsZWF0w7NyaWEgJFggXFxzaW0gTihcXG11LCBcXHNpZ21hXjIpJCwgdGVtb3MgdW1hIGFtb3N0cmEgZGUgdGFtYW5obyAkbj0yNSQuIFNlIG8gZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsIGZvc3NlIGNvbmhlY2lkbyBjb21vICRcXHNpZ21hPTEwJCwgbyB2YWxvciBjcsOtdGljbyBkZSAkWiQgcGFyYSB1bSBuw612ZWwgZGUgY29uZmlhbsOnYSBkZSA5NSUgc2VyaWEgJDEuOTYkLiBDb21vIGFsdGVyYXJpYSBvIHZhbG9yIGNyw610aWNvIHNlIHNvdWLDqXNzZW1vcyBhcGVuYXMgbyBkZXN2aW8gcGFkcsOjbyBhbW9zdHJhbCAkUz0xMCQ/IEp1c3RpZmlxdWUgYmFzZWFuZG8tc2Ugbm8gY29tcG9ydGFtZW50byBkYXMgY2F1ZGFzLiIsICJkaWNhIjogIkNvbXBhcmUgbyB2YWxvciBkZSAkWl97XFx0ZXh0e2NyaXR9fSA9IDEuOTYkIGNvbSAkdF97XFx0ZXh0e2NyaXR9fSQgcGFyYSAkZ2w9MjQkLiBMZW1icmUtc2UgcXVlICR0JCBzZW1wcmUgcG9zc3VpIGNhdWRhcyBtYWlzIHBlc2FkYXMuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlNlICRcXHNpZ21hJCBmb3NzZSBjb25oZWNpZG8sIHV0aWxpemFyw61hbW9zICRaIFxcc2ltIE4oMCwgMSkkIGUgbyB2YWxvciBjcsOtdGljbyBwYXJhICQ5NVxcJSQgc2VyaWEgJFpfe1xcdGV4dHtjcml0fX0gPSAxLjk2JC4iLCAiQ29tbyAkXFxzaWdtYSQgw6kgZGVzY29uaGVjaWRvIGUgdXNhbW9zICRTJCwgZGV2ZW1vcyB1c2FyICRUIFxcc2ltIHQobi0xKSA9IHQoMjQpJC4iLCAiQ29uc3VsdGFuZG8gYSBkaXN0cmlidWnDp8OjbyAkdCQgcGFyYSAkZ2w9MjQkIGUgJDk1XFwlJCBkZSBjb25maWFuw6dhLCBvYnRlbW9zICR0X3tcXHRleHR7Y3JpdH19IFxcYXBwcm94IDIuMDY0JC4iLCAiQ29tcGFyYcOnw6NvOiAkMi4wNjQgPiAxLjk2JC4iLCAiSnVzdGlmaWNhdGl2YTogQSBkaXN0cmlidWnDp8OjbyAkdCQgcG9zc3VpIGNhdWRhcyBtYWlzIHBlc2FkYXMgcGFyYSBjb21wZW5zYXIgYSBpbmNlcnRlemEgYWRpY2lvbmFsIGludHJvZHV6aWRhIHBvciAkUyQuIElzc28gcmVzdWx0YSBlbSB1bSBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBtYWlzIGxhcmdvLCByZWZsZXRpbmRvIG1haW9yIGltcHJlY2lzw6NvIG5hIGVzdGltYcOnw6NvIGRhIG3DqWRpYSBxdWFuZG8gbyBwYXLDom1ldHJvIGRlIGRpc3BlcnPDo28gcG9wdWxhY2lvbmFsIMOpIGRlc2NvbmhlY2lkby4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgtMywgMywgMjAwKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT1zdGF0cy5ub3JtLnBkZih4KSwgbmFtZT0nTigwLDEpJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJykpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT1zdGF0cy50LnBkZih4LCAyNCksIG5hbWU9J3QoMjQpJywgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJykpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkNvbXBhcmHDp8OjbyBkZSBWYWxvcmVzIENyw610aWNvczwvYj4nLCB4YXhpc190aXRsZT0nRXN0YXTDrXN0aWNhJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNTUiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAyLjA2NH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVuc2FpbyBjbMOtbmljbywgbyB0ZW1wbyBtw6lkaW8gZGUgcmVhw6fDo28gZGUgJG49MTYkIHBhY2llbnRlcyBhIHVtIG5vdm8gZsOhcm1hY28gZm9pIGRlICRcXGJhcntYfT0zNTAkIG1zLCBjb20gdW0gZGVzdmlvIHBhZHLDo28gYW1vc3RyYWwgJFM9NDAkIG1zLiBTdXBvbmRvIHF1ZSBhIHBvcHVsYcOnw6NvIGRlIHRlbXBvcyBkZSByZWHDp8OjbyBzZWphIG5vcm1hbCwgY29uc3RydWEgdW0gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgZGUgOTUlICgkMS1cXGFscGhhPTAsOTUkKSBwYXJhIGEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQuIERldGFsaGUgY2FkYSBldGFwYSwgaW5jbHVpbmRvIGEgaWRlbnRpZmljYcOnw6NvIGRvIHZhbG9yIGNyw610aWNvICR0X3tcXHRleHR7Y3JpdH19JC4iLCAiZGljYSI6ICJPIGludGVydmFsbyDDqSBkZWZpbmlkbyBwb3IgJFxcYmFye1h9IFxccG0gdF97XFxnYW1tYX0gXFxmcmFje1N9e1xcc3FydHtufX0kLiBPbmRlICR0X3tcXGdhbW1hfSQgw6kgbyB2YWxvciBjcsOtdGljbyB0YWwgcXVlICRQKC10X3tcXGdhbW1hfSA8IHQgPCB0X3tcXGdhbW1hfSkgPSAwLDk1JCBjb20gJGdsID0gMTUkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBEZWZpbmlyIG9zIGRhZG9zOiAkbj0xNiwgXFxiYXJ7WH09MzUwLCBTPTQwLCBnbCA9IG4tMSA9IDE1JC4iLCAiMi4gTsOtdmVsIGRlIGNvbmZpYW7Dp2EgJDEtXFxhbHBoYSA9IDAsOTUkLCBsb2dvICRcXGFscGhhID0gMCwwNSQgZSAkXFxhbHBoYS8yID0gMCwwMjUkLiIsICIzLiBFbmNvbnRyYXIgJHRfe1xcdGV4dHtjcml0fX0kIHBhcmEgJGdsPTE1JCBlICRQKFQgPiB0X3tcXHRleHR7Y3JpdH19KSA9IDAsMDI1JC4gRGEgdGFiZWxhIHQsICR0X3tcXHRleHR7Y3JpdH19ID0gMiwxMzEkLiIsICI0LiBDYWxjdWxhciBvIGVycm8gcGFkcsOjbzogJEVQID0gUyAvIFxcc3FydHtufSA9IDQwIC8gXFxzcXJ0ezE2fSA9IDQwIC8gNCA9IDEwJC4iLCAiNS4gQ2FsY3VsYXIgYSBtYXJnZW0gZGUgZXJybzogJEUgPSB0X3tcXHRleHR7Y3JpdH19IFxcdGltZXMgRVAgPSAyLDEzMSBcXHRpbWVzIDEwID0gMjEsMzEkLiIsICI2LiBDb25zdHJ1aXIgbyAkSUMkOiAkMzUwIFxccG0gMjEsMzEgXFxSaWdodGFycm93IFszMjgsNjk7IDM3MSwzMV0kLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNTYiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAzMjguNjl9LCB7ImVudW5jaWFkbyI6ICJBIGVzdGF0w61zdGljYSAkVCA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXV9e1MvXFxzcXJ0e259fSQgw6kgZGl0YSB0ZXIgZGlzdHJpYnVpw6fDo28gJHQkIGRlIFN0dWRlbnQgY29tICRnbCA9IG4tMSQuIEV4cGxpcXVlIGEgZnVuZGFtZW50YcOnw6NvIHRlw7NyaWNhIGRlIHBvciBxdWUgYSB2YXJpw6JuY2lhIGFtb3N0cmFsICRTXjIkIGFwYXJlY2Ugbm8gZGVub21pbmFkb3IsIGNyaWFuZG8gbyBmb3JtYXRvIGRlICdjYXVkYXMgcGVzYWRhcycgZGEgZGlzdHJpYnVpw6fDo28uIENvbW8gZXNzYSByZWxhw6fDo28gc2UgYWx0ZXJhIG1hdGVtYXRpY2FtZW50ZSDDoCBtZWRpZGEgcXVlICRuIFxcdG8gXFxpbmZ0eSQ/IiwgImRpY2EiOiAiUmVmbGl0YSBzb2JyZSBhIHJlbGHDp8OjbyBlbnRyZSBhIGRpc3RyaWJ1acOnw6NvIE5vcm1hbCwgYSBkaXN0cmlidWnDp8OjbyBRdWktUXVhZHJhZG8gZSBvIHRlb3JlbWEgZGUgaW5kZXBlbmTDqm5jaWEgZW50cmUgJFxcYmFye1h9JCBlICRTXjIkIHBhcmEgcG9wdWxhw6fDtWVzIG5vcm1haXMuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIEEgZXN0YXTDrXN0aWNhICRUJCDDqSBkZWZpbmlkYSBjb21vIG8gcXVvY2llbnRlIGVudHJlIHVtYSB2YXJpw6F2ZWwgJFogXFxzaW0gTigwLDEpJCBlIGEgcmFpeiBxdWFkcmFkYSBkZSB1bWEgdmFyacOhdmVsIFF1aS1RdWFkcmFkbyBkaXZpZGlkYSBwZWxvcyBzZXVzIGdyYXVzIGRlIGxpYmVyZGFkZS4iLCAiMi4gTyBudW1lcmFkb3Igw6kgJFogPSBcXGZyYWN7KFxcYmFye1h9LVxcbXUpfXtcXHNpZ21hL1xcc3FydHtufX0kLCBxdWUgw6kgJE4oMCwxKSQuIiwgIjMuIE8gZGVub21pbmFkb3IgZGEgZXN0YXTDrXN0aWNhICR0JCBlbnZvbHZlICRcXHNxcnR7XFxmcmFjeyhuLTEpU14yfXtcXHNpZ21hXjJ9IC8gKG4tMSl9ID0gXFxzcXJ0e1xcZnJhY3tTXjJ9e1xcc2lnbWFeMn19JC4iLCAiNC4gQSByYXrDo28gJFxcZnJhY3sobi0xKVNeMn17XFxzaWdtYV4yfSBcXHNpbSBcXGNoaV4yKG4tMSkkLiIsICI1LiBBbyBkaXZpZGlyICRaJCBwb3IgJFxcc3FydHtcXGNoaV4yKG4tMSkvKG4tMSl9JCwgYSBpbmNlcnRlemEgZGUgJFNeMiQgZW0gcmVsYcOnw6NvIGEgJFxcc2lnbWFeMiQgY2F1c2EgYSBkaXNwZXJzw6NvIGV4dHJhIChjYXVkYXMgcGVzYWRhcykuIiwgIjYuIMOAIG1lZGlkYSBxdWUgJG4gXFx0byBcXGluZnR5JCwgYSBkaXN0cmlidWnDp8OjbyAkXFxjaGleMihuLTEpLyhuLTEpJCBjb252ZXJnZSBwYXJhIDEsIGZhemVuZG8gY29tIHF1ZSAkVCQgY29udmlyamEgcGFyYSAkWiBcXHNpbSBOKDAsMSkkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDcsIHAuIDE5MiIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBwcm9jZXNzbyBpbmR1c3RyaWFsIHByb2R1eiBwZcOnYXMgY29tIHVtYSBtYXNzYSBtw6lkaWEgYWx2byBkZSAkMTAwJCBnLiBFbSB1bWEgYW1vc3RyYSBkZSAkbj0xMCQgcGXDp2FzLCBhIG3DqWRpYSBjYWxjdWxhZGEgZm9pIGRlICQxMDQkIGcgZSBvIGRlc3ZpbyBwYWRyw6NvIGRlICRTPTUkIGcuIFRlc3RlIGEgaGlww7N0ZXNlICRIXzA6IFxcbXUgPSAxMDAkIGNvbnRyYSAkSF8xOiBcXG11ID4gMTAwJCBhbyBuw612ZWwgZGUgJFxcYWxwaGEgPSAwLDA1JC4gQXByZXNlbnRlIG8gY8OhbGN1bG8gZGEgZXN0YXTDrXN0aWNhICR0X3tcXHRleHR7Y2FsY319JCBlIGEgY29uY2x1c8OjbyBkbyB0ZXN0ZS4iLCAiZGljYSI6ICJDYWxjdWxlICR0X3tcXHRleHR7Y2FsY319ID0gXFxmcmFjeyhcXGJhcntYfSAtIFxcbXVfMCl9e1MvXFxzcXJ0e259fSQgZSBjb21wYXJlIGNvbSBvIHZhbG9yIGNyw610aWNvICR0X3tcXHRleHR7Y3JpdH19JCBwYXJhICRnbCA9IDkkIGUgJFxcYWxwaGEgPSAwLDA1JCAodW5pbGF0ZXJhbCkuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIEhpcMOzdGVzZXM6ICRIXzA6IFxcbXUgPSAxMDAkLCAkSF8xOiBcXG11ID4gMTAwJC4iLCAiMi4gRXN0YXTDrXN0aWNhOiAkdF97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3soMTA0IC0gMTAwKX17NSAvIFxcc3FydHsxMH19ID0gXFxmcmFjezR9ezUgLyAzLDE2Mn0gPSBcXGZyYWN7NH17MSw1ODF9ID0gMiw1MyQuIiwgIjMuIFZhbG9yIENyw610aWNvOiBQYXJhICRnbD05JCBlICRcXGFscGhhPTAsMDUkICh1bmlsYXRlcmFsKSwgJHRfe1xcdGV4dHtjcml0fX0gPSAxLDgzMyQuIiwgIjQuIENvbXBhcmHDp8OjbzogJDIsNTMgPiAxLDgzMyQuIiwgIjUuIENvbmNsdXPDo286IENvbW8gJHRfe1xcdGV4dHtjYWxjfX0kIGNhaSBuYSByZWdpw6NvIGRlIHJlamVpw6fDo28sIHJlamVpdGFtb3MgJEhfMCQuIEjDoSBldmlkw6puY2lhcyBkZSBxdWUgYSBtw6lkaWEgw6kgc3VwZXJpb3IgYSAxMDAgZy4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgtNCwgNCwgMTAwKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT1zdGF0cy50LnBkZih4LCBkZj05KSwgbmFtZT0ndChnbD05KScsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTIpKSlcbmZpZy5hZGRfdnJlY3QoeDA9MS44MzMsIHgxPTQsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTAsIG5hbWU9J1JlZ2nDo28gZGUgUmVqZWnDp8OjbycpXG5maWcuYWRkX3ZsaW5lKHg9Mi41MywgbGluZV9kYXNoPSdkYXNoJywgbGluZV9jb2xvcj0nIzFFMjkzQicsIGFubm90YXRpb25fdGV4dD0ndF9jYWxjPTIuNTMnKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPlRlc3RlIFVuaWxhdGVyYWw6IFJlZ2nDo28gZGUgUmVqZWnDp8OjbzwvYj4nLCB4YXhpc190aXRsZT0nRXN0YXTDrXN0aWNhIHQnLCB5YXhpc190aXRsZT0nRGVuc2lkYWRlJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM1NyIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDIuNTN9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBleHBlcmltZW50byBpbmR1c3RyaWFsLCBmb3JhbSBjb2xldGFkYXMgMTYgbWVkaWRhcyBkZSBlc3Blc3N1cmEgZGUgcGxhY2FzIGRlIGHDp28gKCRuPTE2JCkuIEEgbcOpZGlhIGNhbGN1bGFkYSBmb2kgJFxcYmFye1h9ID0gMTAuNSQgbW0gZSBvIGRlc3ZpbyBwYWRyw6NvIGFtb3N0cmFsIGZvaSAkUyA9IDAuOCQgbW0uIEFzc3VtaW5kbyBxdWUgYSBwb3B1bGHDp8OjbyBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLCBjYWxjdWxlIG8gdmFsb3IgZGEgZXN0YXTDrXN0aWNhICRUJCBwYXJhIHRlc3RhciBhIGhpcMOzdGVzZSBudWxhICRIXzA6IFxcbXUgPSAxMC4wJCBtbSBjb250cmEgJEhfMTogXFxtdSBcXG5lcSAxMC4wJCBtbS4iLCAiZGljYSI6ICJVdGlsaXplIGEgZsOzcm11bGEgJFQgPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11fXtTL1xcc3FydHtufX0kIGNvbSAkbi0xJCBncmF1cyBkZSBsaWJlcmRhZGUuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIklkZW50aWZpY2FyIG9zIHBhcsOibWV0cm9zOiAkXFxiYXJ7WH0gPSAxMC41JCwgJFxcbXUgPSAxMC4wJCwgJFMgPSAwLjgkLCAkbiA9IDE2JC4iLCAiQ2FsY3VsYXIgbyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhOiAkRVAoXFxiYXJ7WH0pID0gUyAvIFxcc3FydHtufSA9IDAuOCAvIFxcc3FydHsxNn0gPSAwLjggLyA0ID0gMC4yJC4iLCAiQ2FsY3VsYXIgYSBlc3RhdMOtc3RpY2EgdDogJFQgPSAoMTAuNSAtIDEwLjApIC8gMC4yID0gMC41IC8gMC4yID0gMi41JC4iLCAiQ29uY2x1c8OjbzogTyB2YWxvciBkYSBlc3RhdMOtc3RpY2EgJFQkIGNhbGN1bGFkYSDDqSAkMi41JCBjb20gJGdsID0gMTUkIGdyYXVzIGRlIGxpYmVyZGFkZS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDIuNX0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCBzb2IgYSDDs3RpY2EgZGEgdGVvcmlhIGRhIGluZmVyw6puY2lhLCBwb3IgcXVlIG8gdXNvIGRhIGVzdGF0w61zdGljYSAkVCQgKGRpc3RyaWJ1acOnw6NvICR0JCBkZSBTdHVkZW50KSDDqSBvYnJpZ2F0w7NyaW8gZW0gc3Vic3RpdHVpw6fDo28gw6AgZXN0YXTDrXN0aWNhICRaJCAoZGlzdHJpYnVpw6fDo28gbm9ybWFsKSBxdWFuZG8gbyBwYXLDom1ldHJvICRcXHNpZ21hJCDDqSBkZXNjb25oZWNpZG8gZSBhIGFtb3N0cmEgw6kgcGVxdWVuYS4iLCAiZGljYSI6ICJDb25zaWRlcmUgYSBkaWZlcmVuw6dhIGVudHJlIHRyYXRhciBhIHZhcmlhYmlsaWRhZGUgY29tbyB1bSB2YWxvciBmaXhvIGNvbmhlY2lkbyBlIHRyYXTDoS1sYSBjb21vIHVtYSB2YXJpw6F2ZWwgYWxlYXTDs3JpYSBlc3RpbWFkYS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSBlc3RhdMOtc3RpY2EgJFogPSBcXGZyYWN7XFxiYXJ7WH0tXFxtdX17XFxzaWdtYS9cXHNxcnR7bn19JCBwcmVzc3Vww7VlICRcXHNpZ21hJCBmaXhvLCByZXN1bHRhbmRvIGVtIHVtYSBkaXN0cmlidWnDp8OjbyBwZXJmZWl0YW1lbnRlIG5vcm1hbC4iLCAiUXVhbmRvIHN1YnN0aXR1w61tb3MgJFxcc2lnbWEkIHBvciAkUyQsIGludHJvZHV6aW1vcyB1bWEgdmFyacOhdmVsIGFsZWF0w7NyaWEgbm8gZGVub21pbmFkb3IuIEEgcmF6w6NvIGRlIGR1YXMgdmFyacOhdmVpcyBhbGVhdMOzcmlhcyAodW1hIG5vcm1hbCBlIG91dHJhIHJlbGFjaW9uYWRhIGEgdW1hIFF1aS1RdWFkcmFkbykgcmVzdWx0YSBuYSBkaXN0cmlidWnDp8OjbyAkdCQuIiwgIkVzc2EgZXN0aW1hdGl2YSBhZGljaW9uYWwgZGUgdmFyaWFiaWxpZGFkZSAoJFMkKSBuw6NvIMOpIHBlcmZlaXRhOyBlbSBhbW9zdHJhcyBwZXF1ZW5hcywgJFNeMiQgcG9kZSBlc3RhciBtdWl0byBkaXN0YW50ZSBkZSAkXFxzaWdtYV4yJC4iLCAiQSBkaXN0cmlidWnDp8OjbyAkdCQgaW5jb3Jwb3JhIGVzc2EgaW5jZXJ0ZXphIGV4dHJhIGF0cmF2w6lzIGRlIGNhdWRhcyBtYWlzIHBlc2FkYXMsIGdhcmFudGluZG8gcXVlIG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2Egc2VqYSBjb25zZXJ2YWRvciAobWFpcyBsYXJnbykgZSBhIHRheGEgZGUgZXJybyB0aXBvIEkgc2VqYSBtYW50aWRhIHNvYiBjb250cm9sZS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJTZWphIHVtIHByb2Nlc3NvIHF1ZSBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIGNvbSBtw6lkaWEgJFxcbXU9NTAkLiBDb25zaWRlcmUgdW1hIGFtb3N0cmEgZGUgdGFtYW5obyAkbj0yNSQgY29tIHZhcmnDom5jaWEgYW1vc3RyYWwgJFNeMj0xNiQuIERldGVybWluZSBvIHZhbG9yIGRhIGVzdGF0w61zdGljYSAkVCQgc2UgYSBtw6lkaWEgYW1vc3RyYWwgZm9yICRcXGJhcntYfT01MiQuIEVtIHNlZ3VpZGEsIGNvbXBhcmUgcXVhbGl0YXRpdmFtZW50ZSBvIHF1ZSBhY29udGVjZXJpYSBjb20gbyB2YWxvciBhYnNvbHV0byBkZSAkfFR8JCBzZSBhIGFtb3N0cmEgZm9zc2UgZGUgJG49MTAwJCBtYW50ZW5kbyAkXFxiYXJ7WH0kLCAkXFxtdSQgZSAkUyQgY29uc3RhbnRlcy4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlICRUJCBkZXBlbmRlIGludmVyc2FtZW50ZSBkbyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhICRTL1xcc3FydHtufSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhcmEgJG49MjUkOiAkUyA9IFxcc3FydHsxNn0gPSA0JC4iLCAiRXJybyBwYWRyw6NvOiAkRVAgPSA0IC8gXFxzcXJ0ezI1fSA9IDQgLyA1ID0gMC44JC4iLCAiRXN0YXTDrXN0aWNhICRUJDogJFQgPSAoNTIgLSA1MCkgLyAwLjggPSAyIC8gMC44ID0gMi41JC4iLCAiUGFyYSAkbj0xMDAkOiAkRVAgPSA0IC8gXFxzcXJ0ezEwMH0gPSA0IC8gMTAgPSAwLjQkLiIsICJFc3RhdMOtc3RpY2EgJFQkIHBhcmEgJG49MTAwJDogJFQgPSAoNTIgLSA1MCkgLyAwLjQgPSAyIC8gMC40ID0gNS4wJC4iLCAiQW7DoWxpc2U6IENvbSBvIGF1bWVudG8gZGEgYW1vc3RyYSwgbyBlcnJvIHBhZHLDo28gZGltaW51aSwgbyBxdWUgYXVtZW50YSBvIHZhbG9yIGFic29sdXRvIGRhIGVzdGF0w61zdGljYSAkVCQgcGFyYSBhIG1lc21hIGRpZmVyZW7Dp2EgZW50cmUgbcOpZGlhIGFtb3N0cmFsIGUgcG9wdWxhY2lvbmFsLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJ4ID0gbnAubGluc3BhY2UoLTYsIDYsIDIwMClcbmZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMi41LCAyLjVdLCB5PVswLCAwLjRdLCBuYW1lPSd0IHBhcmEgbj0yNScsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTMpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVs1LjAsIDUuMF0sIHk9WzAsIDAuNF0sIG5hbWU9J3QgcGFyYSBuPTEwMCcsIGxpbmU9ZGljdChjb2xvcj0nIzk5MUIxQicsIHdpZHRoPTMpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdFZmVpdG8gZG8gdGFtYW5obyBhbW9zdHJhbCBuYSBlc3RhdMOtc3RpY2EgVCcsIHhheGlzX3RpdGxlPSdUJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZSBFc3RpbWFkYScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMi41fSwgeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgcXXDrW1pY2EgZXN0w6EgdGVzdGFuZG8gYSBwdXJlemEgZGUgdW0gbm92byBjb21wb3N0by4gVW1hIGFtb3N0cmEgZGUgOSBsb3RlcyBhcHJlc2VudG91IG9zIHNlZ3VpbnRlcyDDrW5kaWNlcyBkZSBwdXJlemE6IDkyLCA5NSwgOTEsIDkzLCA5NCwgOTAsIDkyLCA5MywgOTEuIENvbnN0cnVhIG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgZGUgOTUlIHBhcmEgYSBwdXJlemEgbcOpZGlhIHBvcHVsYWNpb25hbCwgYWRtaXRpbmRvIHF1ZSBvIMOtbmRpY2UgZGUgcHVyZXphIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwuIiwgImRpY2EiOiAiQ2FsY3VsZSBwcmltZWlybyBhIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0kIGUgYSB2YXJpw6JuY2lhIGFtb3N0cmFsICRTXjIkLiBVdGlsaXplICRnbCA9IG4tMSA9IDgkIGdyYXVzIGRlIGxpYmVyZGFkZSBwYXJhIGVuY29udHJhciBvIHZhbG9yIGNyw610aWNvICR0X3swLDAyNSwgOH0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBDYWxjdWxhciBhIG3DqWRpYSBhbW9zdHJhbDogJFxcYmFye1h9ID0gXFxmcmFjezkyKzk1KzkxKzkzKzk0KzkwKzkyKzkzKzkxfXs5fSA9IDkyLDMzJC4iLCAiMi4gQ2FsY3VsYXIgYSB2YXJpw6JuY2lhIGFtb3N0cmFsICRTXjIgPSBcXGZyYWN7XFxzdW0oWF9pIC0gXFxiYXJ7WH0pXjJ9e24tMX0gPSBcXGZyYWN7KDkyLTkyLDMzKV4yICsgLi4uICsgKDkxLTkyLDMzKV4yfXs4fSBcXGFwcHJveCAyLDI1JCwgbG9nbyAkUyBcXGFwcHJveCAxLDUkLiIsICIzLiBEZWZpbmlyIG8gdmFsb3IgY3LDrXRpY286IFBhcmEgJG49OSQsICRnbD04JCBlICRcXGFscGhhPTAsMDUkLCB0ZW1vcyAkdF97MCwwMjUsIDh9IFxcYXBwcm94IDIsMzA2JC4iLCAiNC4gQ2FsY3VsYXIgbyBlcnJvIHBhZHLDo286ICRFUChcXGJhcntYfSkgPSBcXGZyYWN7MSw1fXtcXHNxcnR7OX19ID0gMCw1JC4iLCAiNS4gTW9udGFyIG8gaW50ZXJ2YWxvOiAkSUMoXFxtdTsgMCw5NSkgPSA5MiwzMyBcXHBtIDIsMzA2IFxcY2RvdCAwLDUgPSA5MiwzMyBcXHBtIDEsMTUzJC4iLCAiNi4gUmVzdWx0YWRvIGZpbmFsOiAkSUMoXFxtdTsgMCw5NSkgPSBbOTEsMTc3OyA5Myw0ODNdJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMSwgcC4gMzEzIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogOTIuMzN9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgw7N0aWNhIGRhIHZhcmnDoXZlbCBwaXbDtCwgcG9yIHF1ZSBhIHV0aWxpemHDp8OjbyBkYSBkaXN0cmlidWnDp8OjbyB0IGRlIFN0dWRlbnQgw6kgc3VwZXJpb3Igw6AgZGlzdHJpYnVpw6fDo28gbm9ybWFsIHBhcmEgYW1vc3RyYXMgcGVxdWVuYXMgb25kZSAkXFxzaWdtYSQgw6kgZGVzY29uaGVjaWRvLiBDb21vIGlzc28gYWZldGEgYSBjb25zdHJ1w6fDo28gZG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2E/IiwgImRpY2EiOiAiQ29uc2lkZXJlIHF1ZSBhIGVzdGF0w61zdGljYSAkWiA9IFxcZnJhY3tcXGJhcntYfS1cXG11fXtcXHNpZ21hL1xcc3FydHtufX0kIGV4aWdlIG8gcGFyw6JtZXRybyAkXFxzaWdtYSQuIFF1YW5kbyB1c2Ftb3MgJFMkLCBhIGVzdGF0w61zdGljYSByZXN1bHRhbnRlICRUID0gXFxmcmFje1xcYmFye1h9LVxcbXV9e1MvXFxzcXJ0e259fSQgYXByZXNlbnRhIG1haW9yIHZhcmlhYmlsaWRhZGUuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIEEgdmFyacOhdmVsIHBpdsO0IG9yaWdpbmFsIGJhc2VhZGEgbmEgbm9ybWFsIHBhZHLDo28gw6kgJFogPSBcXGZyYWN7XFxiYXJ7WH0tXFxtdX17XFxzaWdtYS9cXHNxcnR7bn19IFxcc2ltIE4oMCwxKSQuIiwgIjIuIFF1YW5kbyAkXFxzaWdtYSQgw6kgZGVzY29uaGVjaWRvLCBzdWJzdGl0dcOtbW9zIHBlbG8gZXN0aW1hZG9yICRTJCwgcmVzdWx0YW5kbyBlbSAkVCA9IFxcZnJhY3tcXGJhcntYfS1cXG11fXtTL1xcc3FydHtufX0kLiIsICIzLiBBIGVzdGF0w61zdGljYSAkVCQgbsOjbyBwb3NzdWkgZGlzdHJpYnVpw6fDo28gbm9ybWFsLCBtYXMgXFxzaW0gZGlzdHJpYnVpw6fDo28gdCBkZSBTdHVkZW50IGNvbSAkbi0xJCBncmF1cyBkZSBsaWJlcmRhZGUgZGV2aWRvIMOgIGluY2VydGV6YSBhZGljaW9uYWwgaW50cm9kdXppZGEgcG9yICRTJC4iLCAiNC4gQSBkaXN0cmlidWnDp8OjbyB0IHBvc3N1aSBjYXVkYXMgbWFpcyBwZXNhZGFzIGRvIHF1ZSBhIG5vcm1hbCwgbyBxdWUgcmVzdWx0YSBlbSB2YWxvcmVzIGNyw610aWNvcyBtYWlvcmVzLiIsICI1LiBDb25zZXF1ZW50ZW1lbnRlLCBpbnRlcnZhbG9zIGRlIGNvbmZpYW7Dp2EgY29uc3RydcOtZG9zIGNvbSBhIGRpc3RyaWJ1acOnw6NvIHQgc8OjbyBtYWlzIGFtcGxvcyBkbyBxdWUgYXF1ZWxlcyBxdWUgYXNzdW1pcmlhbSBlcnJvbmVhbWVudGUgdW1hIG5vcm1hbGlkYWRlLCBnYXJhbnRpbmRvIG8gbsOtdmVsIGRlIGNvbmZpYW7Dp2EgJDEtXFxhbHBoYSQgZGVzZWphZG8uIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW1hIGNvbnN1bHRvcmlhIGRlIFRJIGRlc2VqYSBlc3RpbWFyIG8gdGVtcG8gbcOpZGlvIChlbSBtaW51dG9zKSBkZSBlc3BlcmEgZG9zIHVzdcOhcmlvcyBwYXJhIHN1cG9ydGUgcmVtb3RvLiBVbWEgYW1vc3RyYSBkZSAyNSBjaGFtYWRvcyBpbmRpY291IHVtIHRlbXBvIG3DqWRpbyBkZSAxMiBtaW51dG9zIGUgdW0gZGVzdmlvIHBhZHLDo28gYW1vc3RyYWwgZGUgNCBtaW51dG9zLiBDYWxjdWxlIGEgbWFyZ2VtIGRlIGVycm8gKCRFJCkgcGFyYSB1bSBuw612ZWwgZGUgY29uZmlhbsOnYSBkZSA5MCUuIiwgImRpY2EiOiAiVXNlICRFID0gdF97XFxhbHBoYS8yLCAyNH0gXFxjZG90IFxcZnJhY3tTfXtcXHNxcnR7bn19JC4gTGVtYnJlLXNlIGRlIGNvbnZlcnRlciBvIG7DrXZlbCBkZSBjb25maWFuw6dhIHBhcmEgYSDDoXJlYSBuYXMgY2F1ZGFzLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBJZGVudGlmaWNhciBwYXLDom1ldHJvczogJFxcYmFye1h9PTEyLCBTPTQsIG49MjUsIDEtXFxhbHBoYT0wLDkwIFxcUmlnaHRhcnJvdyBcXGFscGhhPTAsMTAgXFxSaWdodGFycm93IFxcYWxwaGEvMj0wLDA1JC4iLCAiMi4gR3JhdXMgZGUgbGliZXJkYWRlOiAkZ2wgPSAyNS0xID0gMjQkLiIsICIzLiBWYWxvciBjcsOtdGljbzogJHRfezAsMDUsIDI0fSBcXGFwcHJveCAxLDcxMSQuIiwgIjQuIEVycm8gcGFkcsOjbzogJEVQKFxcYmFye1h9KSA9IFxcZnJhY3s0fXtcXHNxcnR7MjV9fSA9IFxcZnJhY3s0fXs1fSA9IDAsOCQuIiwgIjUuIE1hcmdlbSBkZSBlcnJvOiAkRSA9IDEsNzExIFxcY2RvdCAwLDggPSAxLDM2ODgkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMS4zNjg4fSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGNsw61uaWNvIHBhcmEgYXZhbGlhciBvIHRlbXBvIGRlIHJlYcOnw6NvICgkXFxtdSQpIGEgdW0gbm92byBmw6FybWFjbywgdW1hIGFtb3N0cmEgZGUgJG49MjUkIGluZGl2w61kdW9zIGFwcmVzZW50b3UgbcOpZGlhICRcXGJhcntYfSA9IDQ1MG1zJCBlIGRlc3ZpbyBwYWRyw6NvICRTID0gNTBtcyQuIENhbGN1bGUgbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBwYXJhIGEgbcOpZGlhIHBvcHVsYWNpb25hbCBjb20gJDk1XFwlJCBkZSBjb25maWFuw6dhLCBhc3N1bWluZG8gYSBkaXN0cmlidWnDp8OjbyB0IGRlIFN0dWRlbnQuIENvbnNpZGVyZSAkdF97MCwwMjU7IDI0fSBcXGFwcHJveCAyLDA2NCQuIiwgImRpY2EiOiAiVXRpbGl6ZSBhIGbDs3JtdWxhICRJQyhcXG11OyAwLDk1KSA9IFtcXGJhcntYfSAtIHRfe1xcYWxwaGEvMiwgZ2x9IFxcY2RvdCAoUyAvIFxcc3FydHtufSksIFxcYmFye1h9ICsgdF97XFxhbHBoYS8yLCBnbH0gXFxjZG90IChTIC8gXFxzcXJ0e259KV0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQcmltZWlybywgY2FsY3VsYW1vcyBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWE6ICRFUChcXGJhcntYfSkgPSBTIC8gXFxzcXJ0e259ID0gNTAgLyBcXHNxcnR7MjV9ID0gNTAgLyA1ID0gMTBtcyQuIiwgIklkZW50aWZpY2Ftb3MgbyB2YWxvciBjcsOtdGljbyAkdCQgcGFyYSAkZ2wgPSAyNS0xID0gMjQkIGdyYXVzIGRlIGxpYmVyZGFkZSBlICRcXGFscGhhLzIgPSAwLDAyNSQ6ICR0X3tjcml0fSA9IDIsMDY0JC4iLCAiQ2FsY3VsYW1vcyBhIG1hcmdlbSBkZSBlcnJvICRFID0gdF97Y3JpdH0gXFxjZG90IEVQKFxcYmFye1h9KSA9IDIsMDY0IFxcY2RvdCAxMCA9IDIwLDY0bXMkLiIsICJDb25zdHJ1w61tb3Mgb3MgbGltaXRlczogJExfe1xcaW5mfSA9IDQ1MCAtIDIwLDY0ID0gNDI5LDM2JCBlICRMX3tcXHN1cH0gPSA0NTAgKyAyMCw2NCA9IDQ3MCw2NCQuIiwgIkNvbmNsdXPDo286IE8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgcGFyYSBvIHRlbXBvIG3DqWRpbyBkZSByZWHDp8OjbyDDqSAkSUMoXFxtdTsgMCw5NSkgPSBbNDI5LDM2OyA0NzAsNjRdbXMkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogNDI5LjM2fSwgeyJlbnVuY2lhZG8iOiAiRGlzY3V0YSBvIHBhcGVsIGRvIGRlc3ZpbyBwYWRyw6NvIGFtb3N0cmFsICgkUyQpIG5hIHByZWNpc8OjbyBkYSBlc3RpbWF0aXZhIGRlIHVtIGludGVydmFsbyBkZSBjb25maWFuw6dhLiBTZSBlbSB1bWEgc2VndW5kYSBjb2xldGEgZGUgZGFkb3MgbyBtZXNtbyBmZW7DtG1lbm8gYXByZXNlbnRvdSB1bWEgZGlzcGVyc8OjbyBtdWl0byBtYWlvciAoJFMkIHNpZ25pZmljYXRpdmFtZW50ZSBtYWlzIGFsdG8pLCBjb21vIGlzc28gYWx0ZXJhIGEgYW1wbGl0dWRlIGRvICRJQyQgZSBvIHF1ZSBpc3NvIGltcGxpY2EgcGFyYSBhIGNvbmZpYW7Dp2EgbmEgZXN0aW1hdGl2YSBkbyBwYXLDom1ldHJvICRcXG11JD8iLCAiZGljYSI6ICJQZW5zZSBuYSByZWxhw6fDo28gZGlyZXRhIGVudHJlIHZhcmlhYmlsaWRhZGUgZSBpbmNlcnRlemEgKGVycm8gcGFkcsOjbykuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgYW1wbGl0dWRlIGRvICRJQyQgw6kgZGFkYSBwb3IgJEwgPSAyIFxcY2RvdCB0X3tcXGFscGhhLzIsIGdsfSBcXGNkb3QgKFMgLyBcXHNxcnR7bn0pJC4iLCAiT2JzZXJ2YS1zZSBxdWUgJEwkIMOpIGRpcmV0YW1lbnRlIHByb3BvcmNpb25hbCBhbyBkZXN2aW8gcGFkcsOjbyBhbW9zdHJhbCAkUyQuIiwgIlVtIGF1bWVudG8gZW0gJFMkIGltcGxpY2EgdW0gYXVtZW50byBkaXJldG8gbm8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSwgJEVQKFxcYmFye1h9KSA9IFMgLyBcXHNxcnR7bn0kLiIsICJDb25zZXF1ZW50ZW1lbnRlLCBhIGFtcGxpdHVkZSBkbyBpbnRlcnZhbG8gJEwkIHNlIHRvcm5hIG1haXMgbGFyZ2EsIG8gcXVlIGluZGljYSB1bWEgbWVub3IgcHJlY2lzw6NvIG5hIGVzdGltYXRpdmEgcG9udHVhbCBkYSBtw6lkaWEuIiwgIkVtYm9yYSBvIG7DrXZlbCBkZSBjb25maWFuw6dhICQxLVxcYWxwaGEkIHBlcm1hbmXDp2EgbyBtZXNtbyAoZXg6IDk1JSksIGEgdXRpbGlkYWRlIHByw6F0aWNhIGRhIGVzdGltYXRpdmEgZGltaW51aSBkZXZpZG8gw6AgbWFpb3IgaW5jZXJ0ZXphIChpbnRlcnZhbG8gbWFpcyBhbXBsbykuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW1hIGVtcHJlc2EgZGUgbWFudWZhdHVyYSBkZSBzZW5zb3JlcyBJb1QgZGVzZWphIGVzdGltYXIgYSBwcm9wb3LDp8OjbyBkZSBzZW5zb3JlcyBkZWZlaXR1b3NvcyAoJHAkKS4gRW0gdW0gbG90ZSBkZSAkbj00MDAkIHVuaWRhZGVzLCBlbmNvbnRyb3Utc2UgdW1hIHByb3BvcsOnw6NvIGFtb3N0cmFsICRcXGhhdHtwfSA9IDAsMDUkLiBDb25zdHJ1YSBvIGxpbWl0ZSBzdXBlcmlvciBkZSB1bSBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBkZSA5NSUgcGFyYSBhIHByb3BvcsOnw6NvIHBvcHVsYWNpb25hbCB1dGlsaXphbmRvIGEgYXByb3hpbWHDp8OjbyBub3JtYWwgKGNvbnNpZGVyZSAkWl97MCwwMjV9ID0gMSw5NiQpLiIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSAkSUMocDsgMCw5NSkgPSBcXGhhdHtwfSBcXHBtIFpfe1xcYWxwaGEvMn0gXFxjZG90IFxcc3FydHtcXGhhdHtwfSgxLVxcaGF0e3B9KS9ufSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIklkZW50aWZpY2Ftb3Mgb3MgcGFyw6JtZXRyb3M6ICRcXGhhdHtwfSA9IDAsMDUkLCAkbiA9IDQwMCQsICRcXGhhdHtxfSA9IDEgLSAwLDA1ID0gMCw5NSQuIiwgIkNhbGN1bGFtb3MgbyBlcnJvIHBhZHLDo28gZGEgcHJvcG9yw6fDo286ICRcXHNxcnR7XFxoYXR7cH1cXGhhdHtxfS9ufSA9IFxcc3FydHsoMCwwNSBcXGNkb3QgMCw5NSkgLyA0MDB9ID0gXFxzcXJ0ezAsMDQ3NSAvIDQwMH0gPSBcXHNxcnR7MCwwMDAxMTg3NX0gXFxhcHByb3ggMCwwMTA5JC4iLCAiQ2FsY3VsYW1vcyBhIG1hcmdlbSBkZSBlcnJvOiAkRSA9IDEsOTYgXFxjZG90IDAsMDEwOSBcXGFwcHJveCAwLDAyMTQkLiIsICJDYWxjdWxhbW9zIG8gbGltaXRlIHN1cGVyaW9yOiAkTF97XFxzdXB9ID0gXFxoYXR7cH0gKyBFID0gMCwwNSArIDAsMDIxNCA9IDAsMDcxNCQuIiwgIkNvbmNsdXPDo286IE8gbGltaXRlIHN1cGVyaW9yIHBhcmEgYSBwcm9wb3LDp8OjbyBwb3B1bGFjaW9uYWwgw6kgMCwwNzE0IG91IDcsMTQlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDExLCBwLiAzMTYiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjA3MTR9XX0=').decode('utf-8'))


    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    from scipy import stats
    
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discursivas = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcqs) + len(discursivas)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    st.subheader(f"Caderno de Exercícios: {dados_exercicios.get('topico_aula', 'Exercícios')}")
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    
    st.divider()
    
    # Questões de Múltipla Escolha
    st.markdown("### 🎯 Questões de Múltipla Escolha")
    for i, questao in enumerate(mcqs):
        with st.container(border=True):
            st.markdown(f"**Questão {i+1}:** {questao.get('enunciado')}")
            
            # Referência
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
    
            # Plotly
            cod_plot = questao.get("codigo_plotly")
            if cod_plot:
                local_vars = {"go": go, "np": np, "stats": stats}
                try:
                    exec(cod_plot, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
                except Exception as e:
                    st.warning("Gráfico indisponível no momento.")
    
            # Alternativas
            opcoes = questao.get("alternativas", {})
            escolha = st.radio(
                "Selecione uma alternativa:",
                options=list(opcoes.keys()),
                format_func=lambda x: f"{x}) {opcoes[x]}",
                key=f"radio_mcq_{i}"
            )
    
            # Dica e Verificação
            if st.button("💡 Dica", key=f"dica_mcq_{i}"):
                st.info(questao.get("dica", "Dica indisponível"))
    
            if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
                if escolha == questao.get("alternativa_correta"):
                    st.success("Correto! Muito bem.")
                    st.session_state.respostas_certas[f"mcq_{i}"] = True
                    st.rerun()
                else:
                    st.error("Resposta incorreta. Tente novamente!")
                    st.session_state.respostas_certas[f"mcq_{i}"] = False
                    st.rerun()
    
            with st.expander("✅ Ver Gabarito Comentado"):
                st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
    
    st.divider()
    
    # Questões Discursivas
    st.markdown("### ✍️ Questões Discursivas")
    for i, questao in enumerate(discursivas):
        with st.container(border=True):
            st.markdown(f"**Questão Discursiva {i+1}:** {questao.get('enunciado')}")
            
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
    
            # Plotly
            cod_plot = questao.get("codigo_plotly")
            if cod_plot:
                local_vars = {"go": go, "np": np, "stats": stats}
                try:
                    exec(cod_plot, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
                except:
                    pass
    
            st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
    
            if st.button("💡 Dica", key=f"dica_disc_{i}"):
                st.info(questao.get("dica", "Dica indisponível"))
    
            # Validação numérica ou checkbox manual
            esperada = questao.get("resposta_numerica_esperada")
            if esperada is not None:
                val_usuario = st.number_input("Digite o resultado numérico:", format="%.4f", key=f"num_disc_{i}")
                if st.button("Validar Cálculo", key=f"btn_val_{i}"):
                    if abs(val_usuario - esperada) <= max(0.01, 0.05 * abs(esperada)):
                        st.success("Resposta Numérica Correta!")
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                        st.rerun()
                    else:
                        st.error("Valor incorreto. Revise suas fórmulas.")
                        st.session_state.respostas_certas[f"disc_{i}"] = False
                        st.rerun()
            else:
                if st.checkbox("Marque aqui após responder esta questão", key=f"check_disc_{i}"):
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.session_state.respostas_certas[f"disc_{i}"] = False
    
            with st.expander("✅ Ver Resolução Detalhada"):
                for passo in questao.get("gabarito_passo_a_passo", []):
                    st.write(f"- {passo}")
