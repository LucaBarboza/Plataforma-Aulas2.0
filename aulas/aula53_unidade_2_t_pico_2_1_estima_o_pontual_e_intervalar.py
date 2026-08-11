import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuMTogRXN0aW1hw6fDo28gcG9udHVhbCBlIGludGVydmFsYXIiLCAicmVmZXJlbmNpYXNfYmlibGlvZ3JhZmljYXNfZmluYWlzIjogWyJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDExLCBwcC4gMjk4LTMwMyIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDExLCBwcC4gMzAxLTMwMyIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDEyLCBwcC4gMzIwLTMyNSIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDExLCBwcC4gMzEyLTMxMyIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDEyLCBwcC4gMzM5LTM0MCIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDEyLCBwcC4gMzU1LTM1NiIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDcsIHBwLiAxOTIiLCAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhIC0gQ2FwLiAxMSwgcHAuIDMxNCIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDExLCBwcC4gMzE0LTMxNiIsICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDEwLCBwcC4gMjgwLTI4MiJdfQ==').decode('utf-8'))

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
    import pandas as pd
    import numpy as np
    
    # Cabeçalho Principal
    st.header(r"A Natureza da Estimação: Parâmetros, Estatísticas e o Viés de Estimadores")
    
    # Introdução Teórica
    st.markdown(r"""
    A inferência estatística é a arte e a ciência de tirar conclusões sobre uma população inteira a partir de uma amostra. Os valores que descrevem a população, como a média populacional, são chamados de **parâmetros**.
    """)
    
    st.info(r"Como muitas vezes desconhecemos esses parâmetros, precisamos estimá-los. Para isso, utilizamos **estatísticas**, que são funções dos dados observados na amostra.")
    
    st.markdown(r"""
    A estimação pontual fornece um valor único como a melhor aposta para o parâmetro. Contudo, essa aposta está sujeita a erros, e o viés é a medida de erro sistemático: um estimador é não viesado se, em média, ele acerta o valor do parâmetro.
    """)
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Decomposição do EQM")
    st.markdown(r"A qualidade global de um estimador é mensurada pelo Erro Quadrático Médio (EQM), que combina o erro sistemático (viés) e a variabilidade (precisão):")
    st.latex(r"EQM(T; \theta) = E[(T - \theta)^2] = Var(T) + [B(T)]^2")
    
    # Dedução Analítica (Estática e Sequencial)
    st.markdown(r"**Dedução da Decomposição do EQM:**")
    st.latex(r"EQM(T; \theta) = E[(T - \theta)^2]")
    st.markdown(r"Expandindo o termo central, inserimos e subtraímos a esperança do estimador $E(T)$:")
    st.latex(r"EQM(T; \theta) = E[(T - E(T) + E(T) - \theta)^2]")
    st.markdown(r"Ao desenvolver o quadrado do trinômio, observamos a variância e o viés:")
    st.latex(r"EQM(T; \theta) = E[(T - E(T))^2] + 2E[(T - E(T))(E(T) - \theta)] + E[(E(T) - \theta)^2]")
    st.markdown(r"Como o termo cruzado anula-se, obtemos a forma final:")
    st.latex(r"EQM(T; \theta) = Var(T) + 0 + [B(T)]^2")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática: Estimadores de Variância")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Estimação da Variância Populacional")
        st.markdown(r"Um engenheiro de controle de qualidade deseja estimar a variância populacional de peças produzidas. Ele coleta uma amostra aleatória de n=10 peças e compara dois estimadores distintos.")
        
        # Tabela descritiva dos estimadores
        dados_estimadores = pd.DataFrame({
            "Estimador": [r"Variância Amostral (n)", r"Variância Amostral (n-1)"],
            "Fórmula": [r"\frac{1}{n} \sum (X_i - \bar{X})^2", r"\frac{1}{n-1} \sum (X_i - \bar{X})^2"],
            "Notação": [r"\hat{\sigma}^2", r"S^2"]
        })
        st.table(dados_estimadores)
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.latex(r"E(\hat{\sigma}^2) = \frac{n-1}{n} \sigma^2")
        st.latex(r"B(\hat{\sigma}^2) = E(\hat{\sigma}^2) - \sigma^2 = -\frac{\sigma^2}{n}")
        st.latex(r"E(S^2) = \sigma^2")
        
        st.success(r"O estimador $\hat{\sigma}^2$ apresenta viés negativo de $-\frac{\sigma^2}{n}$, subestimando a variabilidade. A variância amostral $S^2$ é preferível por ser não viesada, garantindo uma estimativa correta da variância populacional para o controle de qualidade.")
    
    # Prosa Expandida
    st.markdown(r"---")
    st.markdown(r"### 🧠 Reflexão Profunda: O Trade-off Viés-Variância")
    st.markdown(r"""
    A inferência estatística não é apenas uma coleção de fórmulas; é a ponte intelectual que nos permite saltar do particular para o universal. O problema central da ciência experimental reside no fato de que, frequentemente, não temos acesso a toda a população de interesse. 
    
    O conceito de **viés** surge como a métrica de honestidade do estimador. Se a mira está desalinhada, teremos um erro persistente. Contudo, a lição pedagógica aqui é contraintuitiva: às vezes, pesquisadores preferem um estimador ligeiramente viesado se isso reduzir drasticamente a variância. 
    
    Ao aumentarmos o tamanho da amostra $n$, esperamos que a variância diminua — uma propriedade conhecida como **consistência**. A nossa missão como estudiosos é dominar estas métricas para extrair verdades com o rigor científico exigido pela gestão consciente do erro.
    """)

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Propriedades Estatísticas Desejáveis: Consistência e Eficiência")
    
    # Introdução e Prosa Expandida
    st.markdown(r"""
    A tarefa fundamental da estatística inferencial reside na capacidade de transpor o conhecimento contido em um conjunto limitado de observações — a amostra — para a compreensão dos mecanismos subjacentes que regem a população. Contudo, a simples construção de um estimador não garante uma ferramenta confiável.
    """)
    
    st.markdown(r"""
    Para avaliar se um estimador é robusto, observamos dois pilares essenciais:
    *   **Consistência:** Garante a convergência do estimador ao valor real conforme a amostra cresce.
    *   **Eficiência:** Garante a minimização do ruído amostral, selecionando o estimador com a menor variância possível.
    """)
    
    # Seção de Formalismo e Dedução Analítica
    st.markdown(r"### 📐 O Coração Matemático: Consistência e Eficiência")
    
    st.markdown(r"Abaixo, detalhamos o rigor analítico que fundamenta estas propriedades:")
    
    st.latex(r"Var(T) = E[(T - E(T))^2]")
    st.latex(r"EQM(T_n; \theta) = Var(T_n) + [B(T_n)]^2")
    
    st.info(r"A consistência implica que, no limite, o estimador se torna o próprio parâmetro. Matematicamente:")
    st.latex(r"\lim_{n \to \infty} E(T_n) = \theta \quad \text{e} \quad \lim_{n \to \infty} Var(T_n) = 0 \implies T_n \text{ é consistente.}")
    
    st.latex(r"\text{eff}(T_1, T_2) = \frac{Var(T_2)}{Var(T_1)} > 1 \iff Var(T_1) < Var(T_2)")
    
    # Simulador: Convergência da Média Amostral
    st.markdown(r"### 🧪 Simulador Interativo: Convergência da Média Amostral")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        n_samples = st.slider(r"Tamanho da Amostra (n)", 1, 500, 50, key=r"n_samples_subtopico_2")
    with col2:
        n_simulations = 1000
        means = [np.mean(np.random.normal(0, 1, n_samples)) for _ in range(n_simulations)]
    
    # Plotagem Plotly
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=means, nbinsx=40, marker_color="#1E3A8A", name=r"Distribuição das Médias"))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        title=dict(text="<b>Convergência da Média Amostral ao Valor Real (0)</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valores da Média Amostral", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Frequência", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    st.info(f"Ao aumentar o tamanho da amostra para n = {n_samples}, observamos que a dispersão das médias amostrais diminui, concentrando-se cada vez mais em torno da média populacional (0). Este comportamento ilustra a consistência do estimador.")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Comparação de Estimadores")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Média vs Mediana em População Normal")
        st.markdown(r"Para estimar a média $\mu$ de uma população normal, avaliamos a média amostral $\bar{X}$ e a mediana amostral $md$.")
        
        st.latex(r"Var(\bar{X}) = \frac{\sigma^2}{n}, \quad Var(md) = \frac{\pi\sigma^2}{2n}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Definimos a eficiência relativa como a razão entre as variâncias: $\text{eff}(\bar{X}, md) = \frac{Var(md)}{Var(\bar{X})}$.")
        st.markdown(r"- Substituindo os valores: $\text{eff}(\bar{X}, md) = \frac{\pi\sigma^2 / 2n}{\sigma^2 / n} = \frac{\pi}{2}$.")
        st.markdown(r"- Calculando o valor final: $\text{eff}(\bar{X}, md) \approx 1,57$.")
        
        st.success(r"Como 1,57 > 1, a média amostral $\bar{X}$ é cerca de 57% mais eficiente que a mediana amostral, sendo o estimador preferencial para a média de populações normais.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Construção de Intervalos de Confiança e Margem de Erro")
    
    # Discussão Teórica
    st.markdown(r"""
    A estimação intervalar busca suprir a falha da estimação pontual em comunicar a incerteza. Em vez de um valor único, propomos uma faixa, o **Intervalo de Confiança**, com uma probabilidade associada. 
    A **Margem de Erro** é a semi-amplitude que define nossa tolerância à imprecisão, ajustável conforme o nível de confiança desejado.
    """)
    
    st.info(r"O objetivo central aqui é transformar um palpite estatístico pontual em um território de plausibilidade, onde o verdadeiro parâmetro populacional tem alta probabilidade de residir.")
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Formalismo do Intervalo")
    st.latex(r"IC = [\bar{X} - E, \bar{X} + E] \quad \text{, onde } E = Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}")
    
    # Dedução Analítica
    st.markdown(r"A dedução do intervalo baseia-se na normalização da média amostral:")
    st.latex(r"P\left( -Z_{\alpha/2} \leq \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \leq Z_{\alpha/2} \right) = 1 - \alpha")
    st.latex(r"P\left( -Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} \leq \bar{X} - \mu \leq Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} \right) = 1 - \alpha")
    st.latex(r"P\left( \bar{X} - Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} \leq \mu \leq \bar{X} + Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} \right) = 1 - \alpha")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Vida Útil de Capacitores")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Fabricação de Componentes")
        st.markdown(r"Um fabricante testa capacitores com desvio padrão populacional conhecido $\sigma = 50$ horas. Com uma amostra de n=100 e média $\bar{X} = 1200$, calcula-se o intervalo de confiança de 95% para a vida útil média.")
        st.latex(r"n=100, \bar{X}=1200, \sigma=50, Z_{0,025}=1,96")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Erro Padrão:** $EP(\bar{X}) = \frac{50}{\sqrt{100}} = 5$")
        st.markdown(r"- **Margem de Erro:** $E = 1,96 \cdot 5 = 9,8$")
        st.markdown(r"- **Intervalo:** $IC = [1200 - 9,8; 1200 + 9,8] = [1190,2; 1209,8]$")
        
        st.success(r"Com 95% de confiança, a vida útil média dos capacitores está entre 1190,2 e 1209,8 horas. Este intervalo permite ao gestor planejar a garantia do produto com base na precisão da estimativa.")
    
    # Prosa Longa Expandida
    st.markdown(r"### 🧠 Reflexões sobre a Inferência Frequentista")
    st.markdown(r"""
    A prática da estatística inferencial, em sua essência, não consiste apenas em fornecer um valor único para um parâmetro populacional desconhecido, mas em quantificar, com rigor matemático, a incerteza inerente ao processo de amostragem. 
    
    * **O Dilema da Precisão:** Ao escolhermos um nível de confiança $1-\alpha$, estamos definindo o quão "seguros" queremos estar. Aumentar o nível de confiança expande o intervalo, reduzindo a precisão, mas aumentando a robustez do método.
    * **Consistência dos Estimadores:** À medida que o tamanho da amostra $n$ cresce, o erro padrão diminui, estreitando o intervalo de confiança, o que ilustra a consistência dos estimadores estatísticos.
    """)
    
    st.warning(r"**Nota sobre Interpretação:** Não dizemos que existe 95% de probabilidade de o parâmetro estar no intervalo. O parâmetro é fixo. A probabilidade reside no procedimento de amostragem: em 95% das vezes, o método produz intervalos que contêm o parâmetro.")
    
    st.markdown(r"""
    Por fim, é crucial notar que, na ausência do desvio padrão populacional $\sigma$, utilizamos o desvio padrão amostral $S$, o que nos conduz à distribuição $t$ de Student. Esta distribuição apresenta caudas mais pesadas, compensando a incerteza adicional. Dominar essa transição entre a normalidade idealizada e a realidade amostral é o diferencial na construção de inferências profissionais.
    """)

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    st.header(r"Inferência sobre a Média com Variância Populacional Desconhecida (t de Student)")
    
    st.markdown(r"""
    A inferência estatística sobre a média populacional é, indiscutivelmente, um dos pilares mais fundamentais da ciência moderna. Contudo, na prática laboratorial, industrial ou social, o pesquisador raramente desfruta do privilégio de conhecer o parâmetro de variabilidade populacional $\sigma^2$. 
    
    Neste contexto, destacamos os desafios fundamentais:
    - **A Aproximação da Normal:** Em um cenário idealizado onde $\sigma$ é conhecido, utilizamos a estatística $Z$.
    - **A Realidade Amostral:** O uso do desvio padrão amostral $S$ introduz uma camada adicional de incerteza e variabilidade.
    - **A Solução de Student:** A distribuição $t$ de Student compensa essa flutuação ao apresentar caudas mais pesadas do que a distribuição normal.
    """)
    
    st.info(r"A distribuição t de Student atua como um ajuste de conservadorismo: à medida que a amostra aumenta, a incerteza de $S$ diminui, convergindo para a distribuição normal padrão.")
    
    st.markdown(r"### 📐 O Coração Matemático: Formalismo e Derivação")
    
    st.markdown(r"Para realizar inferências, construímos a estatística $T$ que relaciona a média amostral, a média populacional e o erro padrão estimado.")
    
    st.latex(r"T = \frac{\bar{X} - \mu}{S / \sqrt{n}} \sim t(n-1)")
    
    st.markdown(r"O intervalo de confiança, que nos permite estimar $\mu$ com um nível de precisão definido, é estruturado da seguinte forma:")
    
    st.latex(r"IC = \bar{X} \pm t_{\text{crit}} \cdot \frac{S}{\sqrt{n}}")
    
    st.markdown(r"A fundamentação analítica desta estatística deriva da relação entre a distribuição normal e a distribuição qui-quadrado:")
    
    st.latex(r"\frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)")
    
    st.markdown(r"Considerando a distribuição da variância amostral:")
    
    st.latex(r"\frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)")
    
    st.markdown(r"Ao realizar a razão entre a variável normal e a raiz quadrada da variável qui-quadrado normalizada pelos graus de liberdade, obtemos a definição da estatística $T$:")
    
    st.latex(r"T = \frac{\frac{\bar{X} - \mu}{\sigma / \sqrt{n}}}{\sqrt{\frac{(n-1)S^2}{\sigma^2} / (n-1)}} = \frac{\bar{X} - \mu}{S / \sqrt{n}}")
    
    st.markdown(r"### 📈 Casos de Aplicação Prática: Estimativa de Resposta")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Tempo de resposta de um novo sensor")
        st.markdown(r"Avaliação da precisão de um componente eletrônico com amostra de $n=16$, média $\bar{X} = 45$ ms e $S = 4$ ms, buscando um IC de 95%.")
        
        st.latex(r"n=16, \quad gl=15, \quad \bar{X}=45, \quad S=4, \quad t_{0,025}(15)=2,131")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo do erro amostral: $E = 2,131 \cdot \frac{4}{\sqrt{16}} = 2,131$")
        st.markdown(r"- Construção do intervalo: $IC = [45 - 2,131; 45 + 2,131] = [42,869; 47,131]$")
        
        st.success(r"O tempo médio de resposta está entre 42,87 e 47,13 ms com 95% de confiança. A utilização da distribuição t compensa a variabilidade desconhecida da população com pequena amostra.")
    
    st.markdown(r"""
    A história por trás desta distribuição é um exemplo fascinante de como a necessidade prática molda o rigor matemático. William Sealy Gosset, trabalhando na cervejaria Guinness, percebeu que pequenas amostras exigiam um tratamento estatístico distinto. 
    
    Ao adotar o pseudônimo 'Student', ele legou à posteridade um método que nos permite:
    1. Trabalhar com amostras reduzidas sem comprometer a integridade científica.
    2. Reconhecer a incerteza intrínseca ao estimador $S$.
    3. Aplicar intervalos de confiança que se alargam automaticamente diante da escassez de dados, mantendo a honestidade estatística sobre as conclusões extraídas.
    """)

    # Cabecalho do Subtopico
    st.header(r"Estimação de Proporções em Grandes Amostras")
    
    # Prosa Inicial e Contextualizacao
    st.markdown(r"""
    A inferência sobre proporções constitui um dos pilares fundamentais da estatística inferencial aplicada, desempenhando um papel crucial em áreas que variam da biometria e economia à teoria de pesquisas de opinião pública. Quando nos deparamos com uma variável aleatória dicotômica — isto é, uma variável que assume apenas dois valores possíveis, convencionalmente codificados como "sucesso" (1) ou "fracasso" (0) — estamos lidando com um processo de Bernoulli.
    """)
    
    st.info(r"O parâmetro de interesse é a probabilidade $p$ de ocorrência de um sucesso, sendo a proporção amostral $\hat{p}$ o estimador não-viciado para este parâmetro populacional.")
    
    st.markdown(r"""
    Historicamente, o desenvolvimento das técnicas para lidar com proporções em grandes amostras deve muito à intuição de pioneiros como De Moivre e Laplace. Eles perceberam que a acumulação de ensaios de Bernoulli independentes converge para uma forma de sino simétrica, permitindo que a proporção amostral seja tratada com as propriedades da distribuição normal.
    """)
    
    # O Coracao Matematico
    st.subheader(r"📐 O Coração Matemático: Estimação e Variabilidade")
    
    st.markdown(r"A proporção amostral é definida como $\hat{p} = X/n$. Para amostras suficientemente grandes, utilizamos a distribuição normal para realizar inferências. Abaixo, acompanhamos a lógica dedutiva:")
    
    st.latex(r"\hat{p} = \frac{X}{n}, \quad Var(\hat{p}) = \frac{p(1-p)}{n}")
    
    st.markdown(r"Através do Teorema do Limite Central, padronizamos a variável para obter a estatística $Z$:")
    
    st.latex(r"\frac{\hat{p} - p}{\sqrt{p(1-p)/n}} \approx N(0, 1)")
    
    st.markdown(r"Ao isolar o parâmetro $p$, estabelecemos os limites do intervalo com o nível de confiança $\gamma$:")
    
    st.latex(r"\hat{p} - z(\gamma)\sqrt{\frac{\hat{p}\hat{q}}{n}} \le p \le \hat{p} + z(\gamma)\sqrt{\frac{\hat{p}\hat{q}}{n}}")
    
    # Consideracoes Estruturais
    st.markdown(r"""
    ##### Condições de Aplicabilidade
    Para que a aproximação normal seja válida e os intervalos de confiança sejam robustos, devemos observar alguns critérios:
    * **Independência:** As observações amostrais devem ser independentes.
    * **Tamanho Amostral:** Recomenda-se que $np \ge 10$ e $nq \ge 10$ para garantir a simetria da aproximação gaussiana.
    * **Consistência:** O erro padrão diminui com o aumento de $n$, garantindo a convergência para o valor populacional.
    """)
    
    # Casos de Aplicacao
    st.subheader(r"📈 Casos de Aplicação Prática: Estimativa de Market-Share")
    
    # Exemplo 1
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Preferência de Marca")
        st.markdown(r"Em uma amostra de 400 clientes, observou-se que 60% preferem a marca A. O objetivo é determinar o intervalo de confiança de 95% para a proporção populacional.")
        
        st.latex(r"n=400, \quad \hat{p}=0,6, \quad \hat{q}=0,4, \quad z(0,95)=1,96")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- **Passo 1:** Cálculo do Erro Padrão: $EP(\hat{p}) = \sqrt{\frac{0,6 \cdot 0,4}{400}} = 0,0245$")
        st.markdown(r"- **Passo 2:** Cálculo da Margem de Erro: $E = 1,96 \cdot 0,0245 = 0,048$")
        st.markdown(r"- **Passo 3:** Construção do IC: $IC = [0,6 - 0,048; 0,6 + 0,048]$")
        
        st.success(r"Conclusão: A proporção de consumidores que preferem a marca A situa-se entre 55,2% e 64,8% com 95% de confiança, oferecendo uma base sólida para análise de market-share.")
    
    # Consideracoes Finais
    st.warning(r"Em casos onde a proporção estimada é próxima de 0 ou 1, a aproximação normal pode ser imprecisa. Nestas situações, métodos como o de Wilson ou Clopper-Pearson devem ser considerados em substituição ao método de Wald aqui apresentado.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuMTogRXN0aW1hw6fDo28gcG9udHVhbCBlIGludGVydmFsYXIiLCAicXVlc3RvZXNfbXVsdGlwbGFfZXNjb2xoYSI6IFt7ImVudW5jaWFkbyI6ICJVbSBlbmdlbmhlaXJvIGRlIHF1YWxpZGFkZSBlbSB1bWEgcGxhbnRhIGRlIG1hbnVmYXR1cmEgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIGRlc2VqYSBlc3RpbWFyIGEgcHJvcG9yw6fDo28gZGUgcGXDp2FzIGRlZmVpdHVvc2FzICgkcCQpIGVtIHVtIGxvdGUgZGUgZ3JhbmRlcyBwcm9wb3LDp8O1ZXMuIEVsZSBkZWNpZGUgY29sZXRhciB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIHNpbXBsZXMgZGUgJG49MTAwJCBjb21wb25lbnRlcy4gRWxlIGNvbnNpZGVyYSBkb2lzIGVzdGltYWRvcmVzIHBhcmEgJHAkOiBvIHByaW1laXJvLCAkXFxoYXR7cH1fMSA9IFxcZnJhY3tYfXtufSQsIG9uZGUgJFgkIMOpIG8gbsO6bWVybyBkZSBzdWNlc3NvcyAoZGVmZWl0b3MpIG9ic2VydmFkbywgZSBvIHNlZ3VuZG8sICRcXGhhdHtwfV8yID0gXFxmcmFje1grMX17bisyfSQuIFNvYnJlIGFzIHByb3ByaWVkYWRlcyBkZSB2acOpcyBkZXNzZXMgZXN0aW1hZG9yZXMsIGNvbnNpZGVyYW5kbyBxdWUgJFggXFxzaW0gQmluKG4sIHApJCwgcXVhbCBkYXMgYWZpcm1hw6fDtWVzIGFiYWl4byBlc3TDoSBjb3JyZXRhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQW1ib3Mgb3MgZXN0aW1hZG9yZXMgc8OjbyBuw6NvLXZpZXNhZG9zLCBwb2lzIGEgZXNwZXJhbsOnYSBkZSBxdWFscXVlciBlc3RpbWFkb3IgbGluZWFyIGRlIHVtYSBwcm9wb3LDp8OjbyDDqSBvIHByw7NwcmlvIHBhcsOibWV0cm8uIiwgIkIiOiAiQXBlbmFzICRcXGhhdHtwfV8yJCDDqSB1bSBlc3RpbWFkb3IgbsOjby12aWVzYWRvLCBpbmRlcGVuZGVudGVtZW50ZSBkbyB2YWxvciBkZSAkbiQuIiwgIkMiOiAiTyBlc3RpbWFkb3IgJFxcaGF0e3B9XzEkIMOpIG7Do28tdmllc2FkbywgZW5xdWFudG8gJFxcaGF0e3B9XzIkIHBvc3N1aSB1bSB2acOpcyBxdWUgZGVwZW5kZSBkZSAkcCQgZSAkbiQuIiwgIkQiOiAiQW1ib3Mgb3MgZXN0aW1hZG9yZXMgc8OjbyB2aWVzYWRvcyBwYXJhIHF1YWxxdWVyICRuJCBmaW5pdG8sIG1hcyB0ZW5kZW0gYSBzZXIgbsOjby12aWVzYWRvcyBjb25mb3JtZSAkbiQgY3Jlc2NlLiIsICJFIjogIk8gZXN0aW1hZG9yICRcXGhhdHtwfV8yJCDDqSBvIGVzdGltYWRvciBkZSBtw6F4aW1hIHZlcm9zc2ltaWxoYW7Dp2EgZSwgcG9ydGFudG8sIMOpIHNlbXByZSBuw6NvLXZpZXNhZG8uIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIHBhcmEgdW1hIHZhcmnDoXZlbCBiaW5vbWlhbCAkWCQsICRFKFgpID0gbnAkLiBDYWxjdWxlICRFKFxcaGF0e3B9XzEpJCBlICRFKFxcaGF0e3B9XzIpJCBlIHZlcmlmaXF1ZSBzZSBhcyBlc3BlcmFuw6dhcyByZXN1bHRhbSBlbSAkcCQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIG8gcHJpbWVpcm8gZXN0aW1hZG9yOiAkRShcXGhhdHtwfV8xKSA9IEUoWC9uKSA9IEUoWCkvbiA9IChucCkvbiA9IHAkLiBQb3J0YW50bywgJFxcaGF0e3B9XzEkIMOpIG7Do28tdmllc2Fkby4gUGFyYSBvIHNlZ3VuZG8gZXN0aW1hZG9yOiAkRShcXGhhdHtwfV8yKSA9IEUoKFgrMSkvKG4rMikpID0gKG5wKzEpLyhuKzIpJC4gQ29tbyAkKG5wKzEpLyhuKzIpIFxcbmVxIHAkIHBhcmEgJHAkIGdlbsOpcmljbyBlICRuJCBmaW5pdG8sIG8gZXN0aW1hZG9yICRcXGhhdHtwfV8yJCDDqSB2aWVzYWRvLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gZXN0aW1hZG9yICRUJCBkZSB1bSBwYXLDom1ldHJvICRcXHRoZXRhJCB0YWwgcXVlICRFKFQpID0gXFx0aGV0YSArIDAuNSQgZSAkVmFyKFQpID0gMC43NSQuIFF1YWwgw6kgbyBFcnJvIFF1YWRyw6F0aWNvIE3DqWRpbyAoRVFNKSBkZXN0ZSBlc3RpbWFkb3I/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIwLjc1IiwgIkIiOiAiMS4wMCIsICJDIjogIjAuMjUiLCAiRCI6ICIxLjI1IiwgIkUiOiAiMC41MCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTyBFUU0gw6kgZGVmaW5pZG8gY29tbyAkRVFNKFQ7IFxcdGhldGEpID0gVmFyKFQpICsgW1YoVCldXjIkLCBvbmRlICRWKFQpJCDDqSBvIHZpw6lzIGRvIGVzdGltYWRvci4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIk8gdmnDqXMgZGUgJFQkIMOpICRWKFQpID0gRShUKSAtIFxcdGhldGEgPSAoXFx0aGV0YSArIDAuNSkgLSBcXHRoZXRhID0gMC41JC4gQXNzaW0sICRbVihUKV1eMiA9ICgwLjUpXjIgPSAwLjI1JC4gTyBFUU0gc2Vyw6EgJFZhcihUKSArIFtWKFQpXV4yID0gMC43NSArIDAuMjUgPSAxLjAwJC4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5CYXIoeD1bJ1ZhcmnDom5jaWEnLCAnUXVhZHJhZG8gZG8gVmnDqXMnXSwgeT1bMC43NSwgMC4yNV0sIG1hcmtlcl9jb2xvcj1bJyMxRTNBOEEnLCAnIzk5MUIxQiddKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdDb21wb3Npw6fDo28gZG8gRVFNJywgeGF4aXM9ZGljdCh0aXRsZT0nQ29tcG9uZW50ZXMnKSwgeWF4aXM9ZGljdCh0aXRsZT0nVmFsb3InKSkiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMSwgcC4gMzAyIn0sIHsiZW51bmNpYWRvIjogIlVtYSBpbmTDunN0cmlhIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyB1dGlsaXphIHVtYSBtw6FxdWluYSBkZSBwcmVjaXPDo28gcGFyYSBwcm9kdXppciByZXNpc3RvcmVzLCBjdWpvIHZhbG9yIGRhIHJlc2lzdMOqbmNpYSBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIGNvbSBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgJFxcc2lnbWEgPSAyLDAkIG9obXMuIFBhcmEgYXZhbGlhciBhIGNhbGlicmHDp8OjbyBkYSBtw6FxdWluYSwgZm9pIGNvbGV0YWRhIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgc2ltcGxlcyBkZSAkbiA9IDY0JCByZXNpc3RvcmVzLCBxdWUgYXByZXNlbnRvdSB1bWEgcmVzaXN0w6puY2lhIG3DqWRpYSBkZSAkXFxiYXJ7WH0gPSAxMDAsNSQgb2htcy4gQ29uc2lkZXJhbmRvIHVtIG7DrXZlbCBkZSBjb25maWFuw6dhIGRlICQ5NVxcJSQsIHF1YWwgw6kgYSBNYXJnZW0gZGUgRXJybyAoJEUkKSBlIG8gcmVzcGVjdGl2byBJbnRlcnZhbG8gZGUgQ29uZmlhbsOnYSAoJElDJCkgcGFyYSBhIHJlc2lzdMOqbmNpYSBtw6lkaWEgcG9wdWxhY2lvbmFsPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJEUgPSAwLDQ5JCBvaG1zOyAkSUMgPSBbMTAwLDAxOyAxMDAsOTldJCBvaG1zIiwgIkIiOiAiJEUgPSAwLDk4JCBvaG1zOyAkSUMgPSBbOTksNTI7IDEwMSw0OF0kIG9obXMiLCAiQyI6ICIkRSA9IDAsMjUkIG9obXM7ICRJQyA9IFsxMDAsMjU7IDEwMCw3NV0kIG9obXMiLCAiRCI6ICIkRSA9IDEsOTYkIG9obXM7ICRJQyA9IFs5OCw1NDsgMTAyLDQ2XSQgb2htcyIsICJFIjogIiRFID0gMCw0MCQgb2htczsgJElDID0gWzEwMCwxMDsgMTAwLDkwXSQgb2htcyJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBvIHZhbG9yIGNyw610aWNvICRaX3tcXGFscGhhLzJ9JCBwYXJhIHVtIG7DrXZlbCBkZSBjb25maWFuw6dhIGRlICQ5NVxcJSQgw6kgJDEsOTYkLiBBIE1hcmdlbSBkZSBFcnJvIMOpIGNhbGN1bGFkYSBjb21vICRFID0gWl97XFxhbHBoYS8yfSBcXGNkb3QgXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0kLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUHJpbWVpcm8sIGNhbGN1bGFtb3MgbyBFcnJvIFBhZHLDo28gZGEgTcOpZGlhOiAkRVAoXFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0gPSBcXGZyYWN7MiwwfXtcXHNxcnR7NjR9fSA9IFxcZnJhY3syLDB9ezh9ID0gMCwyNSQuIEEgTWFyZ2VtIGRlIEVycm8gw6kgJEUgPSAxLDk2IFxcY2RvdCAwLDI1ID0gMCw0OSQuIE8gJElDJCDDqSBjb25zdHJ1w61kbyBjb21vICRbXFxiYXJ7WH0gLSBFLCBcXGJhcntYfSArIEVdID0gWzEwMCw1IC0gMCw0OSwgMTAwLDUgKyAwLDQ5XSA9IFsxMDAsMDEsIDEwMCw5OV0kLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMTAwLjAxLCAxMDAuOTldLCB5PVsxLCAxXSwgbW9kZT0nbGluZXMrbWFya2VycycsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTMpLCBuYW1lPSdJQyAoOTUlKScpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9WzEwMC41XSwgeT1bMV0sIG1vZGU9J21hcmtlcnMnLCBtYXJrZXI9ZGljdChjb2xvcj0nIzEwQjk4MScsIHNpemU9MTApLCBuYW1lPSdNw6lkaWEgQW1vc3RyYWwgKCRcXGJhcntYfSQpJykpXG5maWcudXBkYXRlX2xheW91dCh0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJywgdGl0bGU9JzxiPkludGVydmFsbyBkZSBDb25maWFuw6dhIHBhcmEgYSBSZXNpc3TDqm5jaWE8L2I+JywgeGF4aXM9ZGljdCh0aXRsZT0nUmVzaXN0w6puY2lhIChvaG1zKScsIGZpeGVkcmFuZ2U9VHJ1ZSksIHlheGlzPWRpY3Qoc2hvd3RpY2tsYWJlbHM9RmFsc2UsIGZpeGVkcmFuZ2U9VHJ1ZSkpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTEsIHAuIDMxMiJ9LCB7ImVudW5jaWFkbyI6ICJVbSBhbmFsaXN0YSBkZSBtZXJjYWRvIGRlc2VqYSBlc3RpbWFyIGEgbcOpZGlhIGRlIGdhc3RvcyBtZW5zYWlzIGNvbSB0ZWxlZm9uaWEgZGUgdW1hIHBvcHVsYcOnw6NvLiBFbGUgc2FiZSBxdWUgYSB2YXJpw6JuY2lhIHBvcHVsYWNpb25hbCDDqSAkXFxzaWdtYV4yID0gNDAwJC4gUXVhbCBkZXZlIHNlciBvIHRhbWFuaG8gZGEgYW1vc3RyYSAoJG4kKSBuZWNlc3PDoXJpbyBwYXJhIHF1ZSBhIG1hcmdlbSBkZSBlcnJvICgkRSQpIG7Do28gZXhjZWRhIDIsMCByZWFpcyBjb20gdW0gbsOtdmVsIGRlIGNvbmZpYW7Dp2EgZGUgJDk1XFwlJCAoJFpfe1xcYWxwaGEvMn0gPSAxLDk2JCk/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIkbiA9IDEwMCQiLCAiQiI6ICIkbiA9IDE5NiQiLCAiQyI6ICIkbiA9IDM4NCQiLCAiRCI6ICIkbiA9IDQwMCQiLCAiRSI6ICIkbiA9IDUwMCQifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSBkYSBNYXJnZW0gZGUgRXJybyBpc29sYW5kbyBvICRuJDogJEUgPSBaX3tcXGFscGhhLzJ9IFxcY2RvdCBcXGZyYWN7XFxzaWdtYX17XFxzcXJ0e259fSBcXGltcGxpZXMgbiA9IFxcbGVmdCggXFxmcmFje1pfe1xcYWxwaGEvMn0gXFxjZG90IFxcc2lnbWF9e0V9IFxccmlnaHQpXjIkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiRGFkbyBxdWUgJFxcc2lnbWFeMiA9IDQwMCQsIHRlbW9zICRcXHNpZ21hID0gXFxzcXJ0ezQwMH0gPSAyMCQuIEEgZsOzcm11bGEgcGFyYSBvIHRhbWFuaG8gZGEgYW1vc3RyYSDDqSAkbiA9IFxcZnJhY3taX3tcXGFscGhhLzJ9XjIgXFxjZG90IFxcc2lnbWFeMn17RV4yfSQuIFN1YnN0aXR1aW5kbyBvcyB2YWxvcmVzOiAkbiA9IFxcZnJhY3sxLDk2XjIgXFxjZG90IDQwMH17MiwwXjJ9ID0gXFxmcmFjezMsODQxNiBcXGNkb3QgNDAwfXs0fSA9IDMsODQxNiBcXGNkb3QgMTAwID0gMzg0LDE2JC4gQ29tbyBvIHRhbWFuaG8gZGEgYW1vc3RyYSBkZXZlIHNlciBpbnRlaXJvLCBhcnJlZG9uZGFtb3MgcGFyYSBvIHByw7N4aW1vIGludGVpcm8sIHJlc3VsdGFuZG8gZW0gJDM4NCQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMSwgcC4gMjg5IChFeGVtcGxvIDEwLjEzIGFkYXB0YWRvKSJ9LCB7ImVudW5jaWFkbyI6ICJVbWEgZsOhYnJpY2EgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIHV0aWxpemEgdW1hIG3DoXF1aW5hIGNhbGlicmFkYSBwYXJhIHByb2R1emlyIHJlc2lzdG9yZXMgY29tIHJlc2lzdMOqbmNpYSBtw6lkaWEgZGUgJFxcbXUgPSAyMDAgXFx0ZXh0eyB9zqkkIGUgZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsIGNvbmhlY2lkbyBkZSAkXFxzaWdtYSA9IDEwIFxcdGV4dHsgfc6pJC4gUGFyYSB2ZXJpZmljYXIgc2UgbyBwcm9jZXNzbyBkZSBwcm9kdcOnw6NvIGNvbnRpbnVhIHNvYiBjb250cm9sZSwgZm9pIGNvbGV0YWRhIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgZGUgJG4gPSAzNiQgcmVzaXN0b3JlcywgcmVzdWx0YW5kbyBlbSB1bWEgcmVzaXN0w6puY2lhIG3DqWRpYSBhbW9zdHJhbCBkZSAkXFxiYXJ7WH0gPSAyMDQgXFx0ZXh0eyB9zqkkLiBDb25zaWRlcmFuZG8gdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGRlICRcXGFscGhhID0gMCwwNSQgcGFyYSB1bSB0ZXN0ZSBkZSBoaXDDs3Rlc2UgYmlsYXRlcmFsICgkSF8wOiBcXG11ID0gMjAwJCBjb250cmEgJEhfMTogXFxtdSBcXG5lcSAyMDAkKSwgcXVhbCDDqSBhIGRlY2lzw6NvIGVzdGF0w61zdGljYSBjb3JyZXRhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiUmVqZWl0YXIgJEhfMCQsIHBvaXMgJFpfe1xcdGV4dHtjYWxjfX0gPSAyLDQkIMOpIG1haW9yIHF1ZSAkWl97XFx0ZXh0e2NyaXR9fSA9IDEsOTYkLiIsICJCIjogIk7Do28gcmVqZWl0YXIgJEhfMCQsIHBvaXMgJFpfe1xcdGV4dHtjYWxjfX0gPSAxLDQ0JCDDqSBtZW5vciBxdWUgJFpfe1xcdGV4dHtjcml0fX0gPSAxLDk2JC4iLCAiQyI6ICJSZWplaXRhciAkSF8wJCwgcG9pcyAkWl97XFx0ZXh0e2NhbGN9fSA9IDEsNDQkIGVzdMOhIGZvcmEgZGEgcmVnacOjbyBkZSBhY2VpdGHDp8Ojby4iLCAiRCI6ICJOw6NvIHJlamVpdGFyICRIXzAkLCBwb2lzICRaX3tcXHRleHR7Y2FsY319ID0gMiw0JCBlc3TDoSBkZW50cm8gZGEgcmVnacOjbyBkZSBhY2VpdGHDp8Ojby4iLCAiRSI6ICJSZWplaXRhciAkSF8wJCwgcG9pcyAkWl97XFx0ZXh0e2NhbGN9fSA9IDAsNCQgw6kgbWVub3IgcXVlICRaX3tcXHRleHR7Y3JpdH19ID0gMSw5NiQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJDYWxjdWxlIGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlIHBhZHJvbml6YWRhICRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdX17XFxzaWdtYSAvIFxcc3FydHtufX0kIGUgY29tcGFyZSBjb20gbyB2YWxvciBjcsOtdGljbyBkYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgcGFkcsOjbyBwYXJhICRcXGFscGhhLzIgPSAwLDAyNSQgZW0gY2FkYSBjYXVkYS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBhc3NvIDE6IERlZmluaXIgaGlww7N0ZXNlczogJEhfMDogXFxtdSA9IDIwMCQgZSAkSF8xOiBcXG11IFxcbmVxIDIwMCQuIFBhc3NvIDI6IENhbGN1bGFyIG8gZXJybyBwYWRyw6NvOiAkRVAoXFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0gPSBcXGZyYWN7MTB9e1xcc3FydHszNn19ID0gXFxmcmFjezEwfXs2fSBcXGFwcHJveCAxLDY2NyQuIFBhc3NvIDM6IENhbGN1bGFyICRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFjezIwNCAtIDIwMH17MSw2Njd9ID0gMiw0JC4gUGFzc28gNDogUGFyYSAkXFxhbHBoYSA9IDAsMDUkIChiaWxhdGVyYWwpLCAkWl97XFx0ZXh0e2NyaXR9fSA9IDEsOTYkLiBDb21vICR8Miw0fCA+IDEsOTYkLCByZWplaXRhbW9zICRIXzAkIGFvIG7DrXZlbCBkZSA1JS4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAyMDApXG55ID0gc3RhdHMubm9ybS5wZGYoeClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbmFtZT0nTigwLDEpJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJykpKVxuZmlnLmFkZF92cmVjdCh4MD0xLjk2LCB4MT00LCBmaWxsY29sb3I9JyM5OTFCMUInLCBvcGFjaXR5PTAuMywgbGluZV93aWR0aD0wLCBuYW1lPSdSQycpXG5maWcuYWRkX3ZyZWN0KHgwPS00LCB4MT0tMS45NiwgZmlsbGNvbG9yPScjOTkxQjFCJywgb3BhY2l0eT0wLjMsIGxpbmVfd2lkdGg9MClcbmZpZy5hZGRfdmxpbmUoeD0yLjQsIGxpbmVfZGFzaD0nZGFzaCcsIGxpbmVfY29sb3I9JyNGNTlFMEInLCBhbm5vdGF0aW9uX3RleHQ9J1pfY2FsYycpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nRGlzdHJpYnVpw6fDo28gTm9ybWFsIGUgUmVnacOjbyBDcsOtdGljYScsIHhheGlzX3RpdGxlPSdaJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIHNvYnJlIG8gY29uc3VtbyBkZSBjb21idXN0w612ZWwgZGUgdW1hIG5vdmEgZnJvdGEgZGUgdmXDrWN1bG9zLCBzYWJlLXNlIHF1ZSBvIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCDDqSAkXFxzaWdtYSA9IDAsOCQga20vTC4gRGVzZWphLXNlIGVzdGltYXIgYSBtw6lkaWEgcG9wdWxhY2lvbmFsICRcXG11JCBjb20gdW0gbsOtdmVsIGRlIGNvbmZpYW7Dp2EgZGUgOTUlICgkWl97XFx0ZXh0e2NyaXR9fSA9IDEsOTYkKS4gU2UgbyBwZXNxdWlzYWRvciBkZWNpZGlyIGF1bWVudGFyIG8gdGFtYW5obyBkYSBhbW9zdHJhIG9yaWdpbmFsIGRlICRuID0gMTYkIHBhcmEgJG4gPSA2NCQsIHF1YWwgc2Vyw6EgbyBlZmVpdG8gc29icmUgYSBtYXJnZW0gZGUgZXJybyAkRSQgZG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2E/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIG1hcmdlbSBkZSBlcnJvIHNlcsOhIHJlZHV6aWRhIMOgIG1ldGFkZSBkbyB2YWxvciBvcmlnaW5hbC4iLCAiQiI6ICJBIG1hcmdlbSBkZSBlcnJvIHBlcm1hbmVjZXLDoSBpbmFsdGVyYWRhLCBwb2lzIGRlcGVuZGUgYXBlbmFzIGRlICRcXHNpZ21hJC4iLCAiQyI6ICJBIG1hcmdlbSBkZSBlcnJvIGRvYnJhcsOhLCBwb2lzIG8gdGFtYW5obyBkYSBhbW9zdHJhIGF1bWVudG91LiIsICJEIjogIkEgbWFyZ2VtIGRlIGVycm8gc2Vyw6EgcmVkdXppZGEgYSB1bSBxdWFydG8gZG8gdmFsb3Igb3JpZ2luYWwuIiwgIkUiOiAiQSBtYXJnZW0gZGUgZXJybyBhdW1lbnRhcsOhLCBwb2lzIGEgdmFyaWFiaWxpZGFkZSBhdW1lbnRhIGNvbSBvIHRhbWFuaG8gZGEgYW1vc3RyYS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIkFuYWxpc2UgYSBmw7NybXVsYSBkYSBtYXJnZW0gZGUgZXJybyAkRSA9IFpfe1xcdGV4dHtjcml0fX0gXFxjZG90IFxcZnJhY3tcXHNpZ21hfXtcXHNxcnR7bn19JC4gTm90ZSBxdWUgJG4kIGVzdMOhIG5vIGRlbm9taW5hZG9yIHNvYiBhIHJhaXouIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIG1hcmdlbSBkZSBlcnJvIMOpIGRhZGEgcG9yICRFID0gWl97XFx0ZXh0e2NyaXR9fSBcXGNkb3QgXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0kLiBRdWFuZG8gJG4kIGF1bWVudGEgZGUgMTYgcGFyYSA2NCAodW0gZmF0b3IgZGUgNCksIGEgcmFpeiBxdWFkcmFkYSAkXFxzcXJ0e259JCBhdW1lbnRhIHBvciB1bSBmYXRvciBkZSAkXFxzcXJ0ezR9ID0gMiQuIENvbW8gbyB0ZXJtbyAkXFxzcXJ0e259JCBlc3TDoSBubyBkZW5vbWluYWRvciwgZGl2aWRpciBwb3IgMiByZWR1eiBhIG1hcmdlbSBkZSBlcnJvIHRvdGFsIHBlbGEgbWV0YWRlICgkRV97bm92b30gPSBcXGZyYWN7MX17Mn0gRV97YW50aWdvfSQpLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIGVuZ2VuaGFyaWEgZGUgbWF0ZXJpYWlzLCBkZXNlamEtc2UgZXN0aW1hciBhIHJlc2lzdMOqbmNpYSBtw6lkaWEgw6AgdHJhw6fDo28gKCRcXG11JCkgZGUgdW1hIG5vdmEgbGlnYSBtZXTDoWxpY2EuIERldmlkbyBhbyBhbHRvIGN1c3RvIGRlIGNhZGEgZW5zYWlvLCBvYnRldmUtc2UgYXBlbmFzIHVtYSBhbW9zdHJhIGRlIHRhbWFuaG8gJG4gPSA5JC4gU2FiZS1zZSBxdWUgYSBwb3B1bGHDp8OjbyBkYSByZXNpc3TDqm5jaWEgw6kgbm9ybWFsbWVudGUgZGlzdHJpYnXDrWRhLCBtYXMgbyBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgJFxcc2lnbWEkIMOpIGRlc2NvbmhlY2lkby4gUXVhbCBkYXMgYWx0ZXJuYXRpdmFzIGFiYWl4byBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgYSBhYm9yZGFnZW0gZXN0YXTDrXN0aWNhIGlkZWFsIHBhcmEgYSBjb25zdHJ1w6fDo28gZG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgcGFyYSAkXFxtdSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJVdGlsaXphciBhIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBwYWRyw6NvICROKDAsIDEpJCBjb20gbyB2YWxvciBjcsOtdGljbyAkWl97XFx0ZXh0e2NyaXR9fSQgcGFyYSBvIG7DrXZlbCBkZSBjb25maWFuw6dhLCBwb2lzIG8gVGVvcmVtYSBMaW1pdGUgQ2VudHJhbCBnYXJhbnRlIGEgbm9ybWFsaWRhZGUgZGEgbcOpZGlhIGFtb3N0cmFsLiIsICJCIjogIlV0aWxpemFyIGEgZGlzdHJpYnVpw6fDo28gdCBkZSBTdHVkZW50IGNvbSAkZ2wgPSA4JCBncmF1cyBkZSBsaWJlcmRhZGUsIGRhZGEgYSBpbmNlcnRlemEgaW50cm9kdXppZGEgcGVsYSBzdWJzdGl0dWnDp8OjbyBkZSAkXFxzaWdtYSQgcGVsbyBlc3RpbWFkb3IgJFMkLiIsICJDIjogIlV0aWxpemFyIGEgZGlzdHJpYnVpw6fDo28gdCBkZSBTdHVkZW50IGNvbSAkZ2wgPSA5JCBncmF1cyBkZSBsaWJlcmRhZGUsIHVtYSB2ZXogcXVlIG8gdGFtYW5obyBkYSBhbW9zdHJhIGRldmUgc2VyIHNvbWFkbyDDoCB2YXJpYWJpbGlkYWRlIGFtb3N0cmFsLiIsICJEIjogIk7Do28gw6kgcG9zc8OtdmVsIHJlYWxpemFyIGEgZXN0aW1hw6fDo28sIHBvaXMgbyBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgJFxcc2lnbWEkIMOpIGRlc2NvbmhlY2lkbyBlIG8gdGFtYW5obyBkYSBhbW9zdHJhIMOpIG1lbm9yIHF1ZSAzMC4iLCAiRSI6ICJVdGlsaXphciBhIGRpc3RyaWJ1acOnw6NvIFF1aS1xdWFkcmFkbyBjb20gJGdsID0gOCQgZ3JhdXMgZGUgbGliZXJkYWRlIHBhcmEgZW5jb250cmFyIG8gdmFsb3IgY3LDrXRpY28gZSBkZWZpbmlyIG9zIGxpbWl0ZXMgZG8gaW50ZXJ2YWxvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBhIGRpc3RyaWJ1acOnw6NvIHQgZGUgU3R1ZGVudCBmb2kgZGVzZW5oYWRhIGV4YXRhbWVudGUgcGFyYSBjb3JyaWdpciBhIGluY2VydGV6YSBhZGljaW9uYWwgZ2VyYWRhIHF1YW5kbyBlc3RpbWFtb3MgYSB2YXJpw6JuY2lhIHBvcHVsYWNpb25hbCAkXFxzaWdtYV4yJCB1c2FuZG8gYSB2YXJpw6JuY2lhIGFtb3N0cmFsICRTXjIkIGVtIGFtb3N0cmFzIHBlcXVlbmFzLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBlc3RhdMOtc3RpY2EgZGUgdGVzdGUgdXRpbGl6YWRhIMOpICRUID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdX17UyAvIFxcc3FydHtufX0kLCBhIHF1YWwgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIHQgZGUgU3R1ZGVudCBjb20gJGdsID0gbiAtIDEkLiBDb21vICRuID0gOSQsIHRlbW9zICRnbCA9IDkgLSAxID0gOCQuIEEgdXRpbGl6YcOnw6NvIGRhIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCAkTigwLDEpJCBzZXJpYSBpbmFkZXF1YWRhIGRldmlkbyBhbyB0YW1hbmhvIHJlZHV6aWRvIGRhIGFtb3N0cmEgZSBhbyBmYXRvIGRlIHF1ZSAkXFxzaWdtYSQgw6kgZGVzY29uaGVjaWRvLCBvIHF1ZSB0b3JuYSBhIHZhcmlhYmlsaWRhZGUgZGEgZXN0YXTDrXN0aWNhICRUJCBtYWlvciBxdWUgYSBkYSBlc3RhdMOtc3RpY2EgJFokLiBQb3J0YW50bywgYSBhbHRlcm5hdGl2YSBCIMOpIGEgY29ycmV0YS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDcsIHAuIDE5MSJ9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSAkSUMoXFxtdTsgMSAtIFxcYWxwaGEpID0gXFxiYXJ7WH0gXFxwbSB0X3tcXHRleHR7Y3JpdH19IFxcY2RvdCBcXGZyYWN7U317XFxzcXJ0e259fSQgcGFyYSBhIG3DqWRpYSBwb3B1bGFjaW9uYWwgZGUgdW1hIHZhcmnDoXZlbCBub3JtYWxtZW50ZSBkaXN0cmlidcOtZGEuIFNvYnJlIGEgbGFyZ3VyYSBkZXNzZSBpbnRlcnZhbG8gZW0gZnVuw6fDo28gZG8gdGFtYW5obyBhbW9zdHJhbCAkbiQsIMOpIGNvcnJldG8gYWZpcm1hciBxdWU6IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIGxhcmd1cmEgZG8gaW50ZXJ2YWxvIMOpIGludmVyc2FtZW50ZSBwcm9wb3JjaW9uYWwgYSAkbiQsIHBvcnRhbnRvLCBhdW1lbnRhciAkbiQgcmVkdXogYSBsYXJndXJhIGRlIGZvcm1hIGxpbmVhci4iLCAiQiI6ICJBIGxhcmd1cmEgZG8gaW50ZXJ2YWxvIGRlcGVuZGUgYXBlbmFzIGRlICRTJCBlIGRlICRcXGFscGhhJCwgc2VuZG8gbyB0YW1hbmhvIGRhIGFtb3N0cmEgJG4kIHVtIGZhdG9yIGlycmVsZXZhbnRlIHBhcmEgYSBwcmVjaXPDo28gZGEgZXN0aW1hdGl2YS4iLCAiQyI6ICJPIGF1bWVudG8gZGUgJG4kIGRpbWludWkgYSBsYXJndXJhIGRvIGludGVydmFsbywgbsOjbyBhcGVuYXMgcGVsYSBwcmVzZW7Dp2EgZGUgJFxcc3FydHtufSQgbm8gZGVub21pbmFkb3IsIG1hcyB0YW1iw6ltIHBlbGEgcmVkdcOnw6NvIGRvIHZhbG9yIGNyw610aWNvICR0X3tcXHRleHR7Y3JpdH19JCBhc3NvY2lhZG8gYW9zIGdyYXVzIGRlIGxpYmVyZGFkZSAkZ2wgPSBuLTEkLiIsICJEIjogIkEgbGFyZ3VyYSBkbyBpbnRlcnZhbG8gYXVtZW50YSDDoCBtZWRpZGEgcXVlICRuJCBhdW1lbnRhLCBwb2lzIGEgZGlzdHJpYnVpw6fDo28gdCBkZSBTdHVkZW50IHRvcm5hLXNlIG1haXMgZXNwYWxoYWRhIHBhcmEgdmFsb3JlcyBtYWlvcmVzIGRlICRuJC4iLCAiRSI6ICJPIG7DrXZlbCBkZSBjb25maWFuw6dhICQxIC0gXFxhbHBoYSQgbsOjbyBhZmV0YSBhIGxhcmd1cmEgZG8gaW50ZXJ2YWxvLCBwb2lzICR0X3tcXHRleHR7Y3JpdH19JCDDqSBmaXhvIHBhcmEgcXVhbHF1ZXIgdmFsb3IgZGUgJFxcYWxwaGEkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiQW5hbGlzZSBvIGltcGFjdG8gZGUgJG4kIHRhbnRvIG5vIGVycm8gcGFkcsOjbyAkUy9cXHNxcnR7bn0kIHF1YW50byBubyB2YWxvciBjcsOtdGljbyAkdF97XFx0ZXh0e2NyaXR9fSQgb2J0aWRvIG5hIHRhYmVsYSBkYSBkaXN0cmlidWnDp8OjbyB0LiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBsYXJndXJhIGRvIGludGVydmFsbyDDqSBkYWRhIHBvciAkMiBcXGNkb3QgdF97XFx0ZXh0e2NyaXR9fSBcXGNkb3QgXFxmcmFje1N9e1xcc3FydHtufX0kLiDDgCBtZWRpZGEgcXVlICRuJCBhdW1lbnRhLCBhIHJhaXogcXVhZHJhZGEgJFxcc3FydHtufSQgbm8gZGVub21pbmFkb3IgcmVkdXogZGlyZXRhbWVudGUgYSBtYXJnZW0gZGUgZXJyby4gU2ltdWx0YW5lYW1lbnRlLCBjb21vICRnbCA9IG4gLSAxJCwgw6AgbWVkaWRhIHF1ZSAkbiBcXHJpZ2h0YXJyb3cgXFxpbmZ0eSQsICR0X3tcXHRleHR7Y3JpdH19JCBhcHJveGltYS1zZSBkZSAkWl97XFx0ZXh0e2NyaXR9fSQsIHF1ZSDDqSB1bSB2YWxvciBtZW5vciBkbyBxdWUgbyAkdF97XFx0ZXh0e2NyaXR9fSQgcGFyYSBwZXF1ZW5hcyBhbW9zdHJhcy4gQW1ib3Mgb3MgZWZlaXRvcyBjb250cmlidWVtIHBhcmEgYSByZWR1w6fDo28gZGEgbGFyZ3VyYSBkbyBpbnRlcnZhbG8sIHRvcm5hbmRvIGEgZXN0aW1hdGl2YSBtYWlzIHByZWNpc2EuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSg1LCA1MCwgMTAwKVxudF9jcml0ID0gc3RhdHMudC5wcGYoMC45NzUsIHgtMSlcbmxhcmd1cmEgPSAyICogdF9jcml0ICogKDEgLyBucC5cXHNxcnQoeCkpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PWxhcmd1cmEsIG1vZGU9J2xpbmVzJywgbmFtZT0nTGFyZ3VyYSBkbyBJQycsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTMpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5FZmVpdG8gZG8gdGFtYW5obyBhbW9zdHJhbCBuYSBsYXJndXJhIGRvIElDPC9iPicsIHhheGlzX3RpdGxlPSdUYW1hbmhvIGFtb3N0cmFsICgkbiQpJywgeWF4aXNfdGl0bGU9J0xhcmd1cmEgUmVsYXRpdmEgKFM9MSknKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtYSBlbXByZXNhIGRlIHRlY25vbG9naWEgZGVzZWphIGVzdGltYXIgYSBwcm9wb3LDp8OjbyAkcCQgZGUgdXN1w6FyaW9zIHF1ZSB1dGlsaXphbSB1bWEgbm92YSBmdW5jaW9uYWxpZGFkZSBkZSBpbnRlbGlnw6puY2lhIGFydGlmaWNpYWwgZW0gc2V1IGFwbGljYXRpdm8uIEZvaSByZWFsaXphZGEgdW1hIHBlc3F1aXNhIGFsZWF0w7NyaWEgc2ltcGxlcyBjb20gJG4gPSA0MDAkIHVzdcOhcmlvcywgb25kZSAkMTIwJCBkZWNsYXJhcmFtIHV0aWxpemFyIGEgZnVuY2lvbmFsaWRhZGUgcmVndWxhcm1lbnRlLiBDb25zdHJ1YSB1bSBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBkZSAkOTVcXCUkIHBhcmEgYSBwcm9wb3LDp8OjbyBwb3B1bGFjaW9uYWwgJHAkIGUgaWRlbnRpZmlxdWUgYSBhbHRlcm5hdGl2YSBxdWUgYXByZXNlbnRhIG9zIGxpbWl0ZXMgY2FsY3VsYWRvcy4iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjAsMjUzIGUgMCwzNDciLCAiQiI6ICIwLDI2NSBlIDAsMzM1IiwgIkMiOiAiMCwyNzAgZSAwLDMzMCIsICJEIjogIjAsMjQwIGUgMCwzNjAiLCAiRSI6ICIwLDI1MCBlIDAsMzUwIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlICRcXGhhdHtwfSA9IGsvbiQuIE8gaW50ZXJ2YWxvIMOpIGRhZG8gcG9yICRcXGhhdHtwfSBcXHBtIHooXFxnYW1tYSkgXFxzcXJ0e1xcZnJhY3tcXGhhdHtwfVxcaGF0e3F9fXtufX0kLiBQYXJhICQ5NVxcJSQsIHV0aWxpemUgJHooMCw5NSkgPSAxLDk2JC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlByaW1laXJvLCBjYWxjdWxhbW9zIGEgcHJvcG9yw6fDo28gYW1vc3RyYWw6ICRcXGhhdHtwfSA9IDEyMC80MDAgPSAwLDMkLiBDb25zZXF1ZW50ZW1lbnRlLCAkXFxoYXR7cX0gPSAxIC0gMCwzID0gMCw3JC4gTyBlcnJvIHBhZHLDo28gZXN0aW1hZG8gw6kgJFxcc3FydHsoMCwzIFxcdGltZXMgMCw3KSAvIDQwMH0gPSBcXHNxcnR7MCwyMSAvIDQwMH0gPSBcXHNxcnR7MCwwMDA1MjV9IFxcYXBwcm94IDAsMDIyOSQuIEEgbWFyZ2VtIGRlIGVycm8gcGFyYSAkXFxnYW1tYSA9IDAsOTUkIMOpICRFID0gMSw5NiBcXHRpbWVzIDAsMDIyOSBcXGFwcHJveCAwLDA0NDkkLiBBc3NpbSwgb3MgbGltaXRlcyBkbyAkSUMkIHPDo28gJDAsMyBcXHBtIDAsMDQ0OSQsIHJlc3VsdGFuZG8gZW0gJFswLDI1NTE7IDAsMzQ0OV0kLCBhcnJlZG9uZGFuZG8gcGFyYSBhcyBvcMOnw7VlcywgYSBhbHRlcm5hdGl2YSBBIMOpIGEgbWFpcyBwcmVjaXNhLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMC4yNTUsIDAuMzQ1XSwgeT1bMSwgMV0sIG1vZGU9J2xpbmVzK21hcmtlcnMnLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0zKSwgbmFtZT0nSUMgOTUlJykpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nSW50ZXJ2YWxvIGRlIENvbmZpYW7Dp2EgcGFyYSBhIFByb3BvcsOnw6NvJywgeGF4aXNfdGl0bGU9J1Byb3BvcsOnw6NvIChwKScsIHlheGlzPWRpY3QodmlzaWJsZT1GYWxzZSksIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDExLCBwLiAzMTQifSwgeyJlbnVuY2lhZG8iOiAiVW0gYW5hbGlzdGEgZGUgbWVyY2FkbyBwcmVjaXNhIGVzdGltYXIgYSBwcm9wb3LDp8OjbyBkZSBkb21pY8OtbGlvcyBxdWUgcG9zc3VlbSBhY2Vzc28gw6AgZmlicmEgw7N0aWNhLiBFbGUgdXRpbGl6YSBhIGFib3JkYWdlbSBjb25zZXJ2YWRvcmEgKGFzc3VtaW5kbyAkcD0wLDUkIHBhcmEgbWF4aW1pemFyIG8gZXJybyBwYWRyw6NvKSBwYXJhIGdhcmFudGlyIHF1ZSBvIGVycm8gZGEgZXN0aW1hdGl2YSBuw6NvIGV4Y2VkYSAkMCwwMyQgY29tICQ5NVxcJSQgZGUgY29uZmlhbsOnYS4gUXVhbCBvIHRhbWFuaG8gYW1vc3RyYWwgJG4kIG5lY2Vzc8OhcmlvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiODAwIiwgIkIiOiAiMTA2NyIsICJDIjogIjEyNTAiLCAiRCI6ICIxNTAwIiwgIkUiOiAiMjAwMCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTyBlcnJvIG3DoXhpbW8gJEUkIMOpIGRhZG8gcG9yICR6IFxcc3FydHtwKDEtcCkvbn0kLiBDb21vIHF1ZXJlbW9zIGEgZXN0aW1hdGl2YSBjb25zZXJ2YWRvcmEsIHVzZSAkcD0wLDUkIGUgcmVzb2x2YSBwYXJhICRuID0gel4yIFxcZnJhY3twKDEtcCl9e0VeMn0kLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUGFyYSB1bWEgY29uZmlhbsOnYSBkZSAkOTVcXCUkLCAkeiA9IDEsOTYkLiBBIGbDs3JtdWxhIGRvIHRhbWFuaG8gYW1vc3RyYWwgY29uc2VydmFkb3Igw6kgJG4gPSB6XjIgXFxmcmFjezAsMjV9e0VeMn0kLiBTdWJzdGl0dWluZG86ICRuID0gKDEsOTYpXjIgXFx0aW1lcyBcXGZyYWN7MCwyNX17KDAsMDMpXjJ9ID0gMyw4NDE2IFxcdGltZXMgXFxmcmFjezAsMjV9ezAsMDAwOX0gPSAzLDg0MTYgXFx0aW1lcyAyNzcsNzcgXFxhcHByb3ggMTA2NywxMSQuIFBvcnRhbnRvLCBzw6NvIG5lY2Vzc8OhcmlvcyAxMDY3IGRvbWljw61saW9zLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTEsIHAuIDMxNC0zMTUifV0sICJxdWVzdG9lc19kaXNjdXJzaXZhcyI6IFt7ImVudW5jaWFkbyI6ICJTZWphICRYXzEsIFxcZG90cywgWF9uJCB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIHNpbXBsZXMgZGUgdW1hIHBvcHVsYcOnw6NvIGNvbSBtw6lkaWEgJFxcbXUkIGUgdmFyacOibmNpYSAkXFxzaWdtYV4yJC4gQ29uc2lkZXJlIGRvaXMgZXN0aW1hZG9yZXMgcGFyYSAkXFxtdSQ6ICRcXGJhcntYfSQgKG3DqWRpYSBhbW9zdHJhbCkgZSAkVCA9IFxcZnJhY3tYXzEgKyBYX259ezJ9JC4gKGEpIE1vc3RyZSBxdWUgYW1ib3Mgc8OjbyBuw6NvLXZpZXNhZG9zLiAoYikgQ29tcGFyZSBhcyB2YXJpw6JuY2lhcyBkZSAkXFxiYXJ7WH0kIGUgJFQkIGUgZGV0ZXJtaW5lIHF1YWwgZXN0aW1hZG9yIMOpIG1haXMgZWZpY2llbnRlLiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgJEUoXFxiYXJ7WH0pID0gXFxtdSQsICRWYXIoXFxiYXJ7WH0pID0gXFxzaWdtYV4yL24kLCAkRShUKSA9IFxcbXUkLCBlICRWYXIoVCkgPSBWYXIoKFhfMStYX24pLzIpID0gXFxmcmFjezF9ezR9KFZhcihYXzEpICsgVmFyKFhfbikpJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFyYSAkXFxiYXJ7WH0kOiAkRShcXGJhcntYfSkgPSBFKFxcZnJhY3sxfXtufVxcc3VtIFhfaSkgPSBcXGZyYWN7MX17bn0gXFxzdW0gRShYX2kpID0gXFxmcmFjezF9e259IChuXFxtdSkgPSBcXG11JC4gUG9ydGFudG8sIMOpIG7Do28tdmllc2Fkby4iLCAiUGFyYSAkVCQ6ICRFKFQpID0gRShcXGZyYWN7WF8xICsgWF9ufXsyfSkgPSBcXGZyYWN7MX17Mn0oRShYXzEpICsgRShYX24pKSA9IFxcZnJhY3sxfXsyfShcXG11ICsgXFxtdSkgPSBcXG11JC4gUG9ydGFudG8sIMOpIG7Do28tdmllc2Fkby4iLCAiVmFyacOibmNpYSBkZSAkXFxiYXJ7WH0kOiAkVmFyKFxcYmFye1h9KSA9IFxcZnJhY3tcXHNpZ21hXjJ9e259JC4iLCAiVmFyacOibmNpYSBkZSAkVCQ6ICRWYXIoVCkgPSBWYXIoXFxmcmFje1hfMSArIFhfbn17Mn0pID0gXFxmcmFjezF9ezR9KFZhcihYXzEpICsgVmFyKFhfbikpID0gXFxmcmFjezF9ezR9KFxcc2lnbWFeMiArIFxcc2lnbWFeMikgPSBcXGZyYWN7Mlxcc2lnbWFeMn17NH0gPSBcXGZyYWN7XFxzaWdtYV4yfXsyfSQuIiwgIkNvbXBhcmHDp8OjbzogUGFyYSAkbiA+IDIkLCB0ZW1vcyAkXFxmcmFje1xcc2lnbWFeMn17bn0gPCBcXGZyYWN7XFxzaWdtYV4yfXsyfSQsIGxvZ28gJFxcYmFye1h9JCBwb3NzdWkgbWVub3IgdmFyacOibmNpYSBlIMOpIG1haXMgZWZpY2llbnRlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBvIGVzdGltYWRvciAkVCA9IFxcZnJhY3tufXtuKzF9TSQsIG9uZGUgJE0kIMOpIG8gbcOheGltbyBkZSB1bWEgYW1vc3RyYSBkZSB0YW1hbmhvICRuJCBkZSB1bWEgZGlzdHJpYnVpw6fDo28gdW5pZm9ybWUgbm8gaW50ZXJ2YWxvICQoMCwgXFx0aGV0YSkkLiBEYWRvIHF1ZSAkRShNKSA9IFxcZnJhY3tufXtuKzF9XFx0aGV0YSQgZSAkVmFyKE0pID0gXFxmcmFje25cXHRoZXRhXjJ9eyhuKzEpXjIobisyKX0kLCBjYWxjdWxlIG8gdmnDqXMgZGUgJFQkIGUgZGVtb25zdHJlIHF1ZSAkVCQgw6kgdW0gZXN0aW1hZG9yIG7Do28tdmllc2Fkby4iLCAiZGljYSI6ICJDYWxjdWxlIGEgZXNwZXJhbsOnYSBkZSAkVCQgdXNhbmRvIGEgcHJvcHJpZWRhZGUgZGEgbGluZWFyaWRhZGU6ICRFKFQpID0gRShcXGZyYWN7bn17bisxfU0pID0gXFxmcmFje259e24rMX1FKE0pJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiTyB2acOpcyBkZSB1bSBlc3RpbWFkb3IgJFQkIMOpICRWKFQpID0gRShUKSAtIFxcdGhldGEkLiIsICJDYWxjdWxhbmRvIGEgZXNwZXJhbsOnYSBkZSAkVCQ6ICRFKFQpID0gRShcXGZyYWN7bn17bisxfU0pID0gXFxmcmFje259e24rMX1FKE0pJC4iLCAiU3Vic3RpdHVpbmRvICRFKE0pID0gXFxmcmFje259e24rMX1cXHRoZXRhJDogJEUoVCkgPSBcXGZyYWN7bn17bisxfSBcXGNkb3QgXFxmcmFje24rMX17bn1cXHRoZXRhID0gXFx0aGV0YSQuIiwgIlBvcnRhbnRvLCAkVihUKSA9IFxcdGhldGEgLSBcXHRoZXRhID0gMCQuIiwgIkNvbW8gYSBlc3BlcmFuw6dhIGRlICRUJCDDqSBpZ3VhbCBhbyBwYXLDom1ldHJvICRcXHRoZXRhJCwgY29uY2x1w61tb3MgcXVlICRUJCDDqSB1bSBlc3RpbWFkb3IgbsOjby12aWVzYWRvLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDExLCBQcm9ibGVtYSAzOCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMH0sIHsiZW51bmNpYWRvIjogIlVtYSBwb3B1bGHDp8OjbyB0ZW0gdmFyacOibmNpYSAkXFxzaWdtYV4yJC4gRG9pcyBlc3RpbWFkb3JlcyBwYXJhIGEgdmFyacOibmNpYSBzw6NvIHByb3Bvc3RvczogJFxcaGF0e1xcc2lnbWF9XjIgPSBcXGZyYWN7MX17bn0gXFxzdW0gKFhfaSAtIFxcYmFye1h9KV4yJCBlICRTXjIgPSBcXGZyYWN7MX17bi0xfSBcXHN1bSAoWF9pIC0gXFxiYXJ7WH0pXjIkLiBTYWJlbmRvIHF1ZSAkRShcXGhhdHtcXHNpZ21hfV4yKSA9IFxcZnJhY3tuLTF9e259XFxzaWdtYV4yJCwgY2FsY3VsZSBvIHZpw6lzIGRlIGNhZGEgZXN0aW1hZG9yLiIsICJkaWNhIjogIk8gdmnDqXMgw6kgJFYoVCkgPSBFKFQpIC0gXFxzaWdtYV4yJC4gVXNlIG8gZmF0byBkZSBxdWUgJEUoU14yKSA9IFxcc2lnbWFeMiQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlZpw6lzIGRlICRcXGhhdHtcXHNpZ21hfV4yJDogJFYoXFxoYXR7XFxzaWdtYX1eMikgPSBFKFxcaGF0e1xcc2lnbWF9XjIpIC0gXFxzaWdtYV4yID0gXFxmcmFje24tMX17bn1cXHNpZ21hXjIgLSBcXHNpZ21hXjIgPSAoXFxmcmFje24tMX17bn0gLSAxKVxcc2lnbWFeMiA9IC1cXGZyYWN7MX17bn1cXHNpZ21hXjIkLiIsICJWacOpcyBkZSAkU14yJDogJFYoU14yKSA9IEUoU14yKSAtIFxcc2lnbWFeMiQuIiwgIkNvbW8gJFNeMiQgw6kgdW0gZXN0aW1hZG9yIG7Do28tdmllc2FkbywgJEUoU14yKSA9IFxcc2lnbWFeMiQuIiwgIlBvcnRhbnRvLCAkVihTXjIpID0gXFxzaWdtYV4yIC0gXFxzaWdtYV4yID0gMCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTEsIHAuIDMwMCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbWEgZW1wcmVzYSBkZSBcXGxvZ8Otc3RpY2EgbW9uaXRvcmEgbyB0ZW1wbyBkZSBlbnRyZWdhIGRlIG1lcmNhZG9yaWFzLiBIaXN0b3JpY2FtZW50ZSwgbyBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgw6kgJFxcc2lnbWEgPSAxNSQgbWludXRvcy4gRW0gdW1hIGFtb3N0cmEgZGUgJG4gPSAxMDAkIGVudHJlZ2FzLCBvYnNlcnZvdS1zZSB1bWEgbcOpZGlhIGFtb3N0cmFsIGRlICRcXGJhcntYfSA9IDQ1JCBtaW51dG9zLiBDb25zdHJ1YSB1bSBJbnRlcnZhbG8gZGUgQ29uZmlhbsOnYSBwYXJhIGEgbcOpZGlhIHBvcHVsYWNpb25hbCAoJFxcbXUkKSBjb20gdW0gY29lZmljaWVudGUgZGUgY29uZmlhbsOnYSAkXFxnYW1tYSA9IDk5XFwlJC4gVXRpbGl6ZSAkWl97MCwwMDV9ID0gMiw1NzYkLiBFeHBsaXF1ZSBvIHNpZ25pZmljYWRvIGVzdGF0w61zdGljbyBkZXN0ZSBpbnRlcnZhbG8uIiwgImRpY2EiOiAiTyBpbnRlcnZhbG8gw6kgZGFkbyBwb3IgJFxcYmFye1h9IFxccG0gWl97XFxhbHBoYS8yfSBcXGNkb3QgXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0kLiBMZW1icmUtc2UgcXVlICQxLVxcYWxwaGEgPSAwLDk5JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYXIgb3MgcGFyw6JtZXRyb3M6ICRcXGJhcntYfSA9IDQ1JCwgJFxcc2lnbWEgPSAxNSQsICRuID0gMTAwJCwgJFpfe1xcYWxwaGEvMn0gPSAyLDU3NiQuIiwgIjIuIENhbGN1bGFyIG8gRXJybyBQYWRyw6NvIGRhIE3DqWRpYTogJEVQKFxcYmFye1h9KSA9IFxcZnJhY3sxNX17XFxzcXJ0ezEwMH19ID0gXFxmcmFjezE1fXsxMH0gPSAxLDUkLiIsICIzLiBDYWxjdWxhciBhIE1hcmdlbSBkZSBFcnJvOiAkRSA9IDIsNTc2IFxcY2RvdCAxLDUgPSAzLDg2NCQuIiwgIjQuIERlZmluaXIgb3MgbGltaXRlcyBkbyAkSUMkOiAkSUMgPSBbNDUgLSAzLDg2NDsgNDUgKyAzLDg2NF0gPSBbNDEsMTM2OyA0OCw4NjRdJC4iLCAiNS4gSW50ZXJwcmV0YcOnw6NvOiBUZW1vcyA5OSUgZGUgY29uZmlhbsOnYSBkZSBxdWUgbyB2ZXJkYWRlaXJvIHRlbXBvIG3DqWRpbyBwb3B1bGFjaW9uYWwgZGUgZW50cmVnYSBlc3TDoSBjb250aWRvIG5vIGludGVydmFsbyBkZSA0MSwxMzYgYSA0OCw4NjQgbWludXRvcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDQ4Ljg2NH0sIHsiZW51bmNpYWRvIjogIlN1cG9uaGEgcXVlIHVtYSBwb3B1bGHDp8OjbyBkZSBwYXJhZnVzb3MgdGVuaGEgdW1hIHJlc2lzdMOqbmNpYSDDoCB0cmHDp8OjbyBjb20gZGVzdmlvIHBhZHLDo28gY29uaGVjaWRvICRcXHNpZ21hID0gMTAkIGtnZi4gRGVzZWphLXNlIGVzdGltYXIgYSByZXNpc3TDqm5jaWEgbcOpZGlhIHBvcHVsYWNpb25hbCBjb20gdW1hIG1hcmdlbSBkZSBlcnJvIGRlICQxLDAkIGtnZi4gUXVhbCBvIHRhbWFuaG8gbcOtbmltbyBkYSBhbW9zdHJhIHBhcmEgcXVlIG8gbsOtdmVsIGRlIGNvbmZpYW7Dp2Egc2VqYSBkZSAkOTBcXCUkICgkWl97MCwwNX0gPSAxLDY0NSQpPyIsICJkaWNhIjogIlVzZSBhIGbDs3JtdWxhIGRhIG1hcmdlbSBkZSBlcnJvICRFID0gWl97XFxhbHBoYS8yfSBcXGNkb3QgXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0kIGUgaXNvbGUgJG4kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBGw7NybXVsYTogJEUgPSBaX3tcXGFscGhhLzJ9IFxcY2RvdCBcXGZyYWN7XFxzaWdtYX17XFxzcXJ0e259fSQuIiwgIjIuIElzb2xhbmRvICRuJDogJFxcc3FydHtufSA9IFxcZnJhY3taX3tcXGFscGhhLzJ9IFxcY2RvdCBcXHNpZ21hfXtFfSBcXGltcGxpZXMgbiA9IFxcbGVmdCggXFxmcmFje1pfe1xcYWxwaGEvMn0gXFxjZG90IFxcc2lnbWF9e0V9IFxccmlnaHQpXjIkLiIsICIzLiBTdWJzdGl0dWluZG86ICRuID0gXFxsZWZ0KCBcXGZyYWN7MSw2NDUgXFxjZG90IDEwfXsxLDB9IFxccmlnaHQpXjIgPSAoMTYsNDUpXjIkLiIsICI0LiBDw6FsY3VsbyBmaW5hbDogJG4gPSAyNzAsNjAyNSQuIiwgIjUuIEFycmVkb25kYW1lbnRvOiBDb21vICRuJCBkZXZlIHNlciBpbnRlaXJvLCBhcnJlZG9uZGEtc2UgcGFyYSBjaW1hIHBhcmEgZ2FyYW50aXIgYSBwcmVjaXPDo28gZXhpZ2lkYTogJG4gPSAyNzEkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMjcxLjB9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgZG8gcG9udG8gZGUgdmlzdGEgY29uY2VpdHVhbCwgcG9yIHF1ZSBhbyBhdW1lbnRhciBvIG7DrXZlbCBkZSBjb25maWFuw6dhIChleDogZGUgJDk1XFwlJCBwYXJhICQ5OVxcJSQpIHBhcmEgdW0gbWVzbW8gdGFtYW5obyBkZSBhbW9zdHJhIGUgdmFyacOibmNpYSBjb25oZWNpZGEsIGEgYW1wbGl0dWRlIGRvIEludGVydmFsbyBkZSBDb25maWFuw6dhIGF1bWVudGEuIiwgImRpY2EiOiAiQ29uc2lkZXJlIG8gY29tcG9ydGFtZW50byBkbyB2YWxvciBjcsOtdGljbyAkWl97XFxhbHBoYS8yfSQgbmEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIHBhZHLDo28gcXVhbmRvICRcXGFscGhhJCBkaW1pbnVpLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBBIGFtcGxpdHVkZSBkbyBpbnRlcnZhbG8gw6kgZGFkYSBwb3IgJDJFID0gMiBcXGNkb3QgWl97XFxhbHBoYS8yfSBcXGNkb3QgXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0kLiIsICIyLiBBbyBhdW1lbnRhciBvIG7DrXZlbCBkZSBjb25maWFuw6dhIChleDogZGUgMCw5NSBwYXJhIDAsOTkpLCBvIHZhbG9yIGRlICRcXGFscGhhJCAobsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhKSBkaW1pbnVpIChkZSAwLDA1IHBhcmEgMCwwMSkuIiwgIjMuIE8gdmFsb3IgY3LDrXRpY28gJFpfe1xcYWxwaGEvMn0kIGNvcnJlc3BvbmRlIGFvIHF1YW50aWwgZGEgbm9ybWFsIHBhZHLDo28gcXVlIGRlaXhhIHVtYSDDoXJlYSBkZSAkXFxhbHBoYS8yJCBuYXMgY2F1ZGFzLiBQb3J0YW50bywgcXVhbnRvIG1lbm9yIG8gJFxcYWxwaGEkLCBtYWlvciBvIHZhbG9yIGFic29sdXRvIGRlICRaX3tcXGFscGhhLzJ9JCAoZXg6IDEsOTYgcGFyYSA5NSUgZSAyLDU3NiBwYXJhIDk5JSkuIiwgIjQuIENvbW8gJFpfe1xcYWxwaGEvMn0kIMOpIHVtIG11bHRpcGxpY2Fkb3IgZGlyZXRvIG5hIGbDs3JtdWxhIGRhIE1hcmdlbSBkZSBFcnJvLCB1bSB2YWxvciBtYWlvciBkZSAkWl97XFxhbHBoYS8yfSQgcmVzdWx0YSBlbSB1bWEgTWFyZ2VtIGRlIEVycm8gbWFpb3IuIiwgIjUuIENvbmNsdXPDo286IFBhcmEgZ2FyYW50aXIgbWFpb3IgY29uZmlhbsOnYSBkZSBxdWUgbyBwYXLDom1ldHJvIGVzdMOhIGNvbnRpZG8gbm8gaW50ZXJ2YWxvLCBzb21vcyBvYnJpZ2Fkb3MgYSBleHBhbmRpciBhIGxhcmd1cmEgZGEgbm9zc2EgJ3JlZGUgZGUgY2FwdHVyYScsIG8gcXVlIGluZXZpdGF2ZWxtZW50ZSBhdW1lbnRhIGEgYW1wbGl0dWRlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtYSBlbXByZXNhIGRlIFxcbG9nw61zdGljYSBtb25pdG9yYSBvIHRlbXBvIGRlIGVudHJlZ2EgZGUgZW5jb21lbmRhcywgcXVlIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgY29tIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCAkXFxzaWdtYSA9IDUkIG1pbnV0b3MuIEVtIHVtYSBhbW9zdHJhIGRlICRuID0gMjUkIGVudHJlZ2FzLCBvYnRldmUtc2UgdW0gdGVtcG8gbcOpZGlvICRcXGJhcntYfSA9IDQyJCBtaW51dG9zLiBUZXN0ZSBhIGhpcMOzdGVzZSBkZSBxdWUgbyB0ZW1wbyBtw6lkaW8gZGUgZW50cmVnYSDDqSBzdXBlcmlvciBhIDQwIG1pbnV0b3MgYW8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGRlICRcXGFscGhhID0gMCwwNSQuIEFwcmVzZW50ZSBvIGPDoWxjdWxvIGRlICRaX3tcXHRleHR7Y2FsY319JCBlIGEgY29uY2x1c8Ojby4iLCAiZGljYSI6ICJPIHRlc3RlIMOpIHVuaWxhdGVyYWwgw6AgZGlyZWl0YS4gVXNlICRIXzA6IFxcbXUgPSA0MCQgZSAkSF8xOiBcXG11ID4gNDAkLiBDYWxjdWxlICRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdV8wfXtcXHNpZ21hIC8gXFxzcXJ0e259fSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIiQkSF8wOiBcXG11ID0gNDAsIFxcdGV4dHsgfSBIXzE6IFxcbXUgPiA0MCQkIiwgIiQkXFx0ZXh0e0Vycm8gUGFkcsOjbzogfSBFUChcXGJhcntYfSkgPSBcXGZyYWN7XFxzaWdtYX17XFxzcXJ0e259fSA9IFxcZnJhY3s1fXtcXHNxcnR7MjV9fSA9IFxcZnJhY3s1fXs1fSA9IDEkJCIsICIkJFxcdGV4dHtFc3RhdMOtc3RpY2EgZGUgdGVzdGU6IH0gWl97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3s0MiAtIDQwfXsxfSA9IDIsMCQkIiwgIiQkXFx0ZXh0e1ZhbG9yIGNyw610aWNvOiBQYXJhIH0gXFxhbHBoYSA9IDAsMDUgXFx0ZXh0eyAodW5pbGF0ZXJhbCksIH0gWl97XFx0ZXh0e2NyaXR9fSA9IDEsNjQ1JCQiLCAiJCRcXHRleHR7Q29uY2x1c8OjbzogQ29tbyB9IFpfe1xcdGV4dHtjYWxjfX0gKDIsMCkgPiBaX3tcXHRleHR7Y3JpdH19ICgxLDY0NSksIFxcdGV4dHsgcmVqZWl0YW1vcyB9IEhfMC4gXFx0ZXh0eyBIw6EgZXZpZMOqbmNpYSBlc3RhdMOtc3RpY2EgZGUgcXVlIG8gdGVtcG8gbcOpZGlvIMOpIHN1cGVyaW9yIGEgNDAgbWludXRvcy59JCQiXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDIuMH0sIHsiZW51bmNpYWRvIjogIkNhbGN1bGUgbyB0YW1hbmhvIGFtb3N0cmFsICRuJCBuZWNlc3PDoXJpbyBwYXJhIGVzdGltYXIgYSByZXNpc3TDqm5jaWEgbcOpZGlhIGRlIHVtIG1hdGVyaWFsLCBzYWJlbmRvIHF1ZSBvIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCDDqSAkXFxzaWdtYSA9IDEyJCB1bmlkYWRlcyBlIGRlc2VqYS1zZSBxdWUgYSBtYXJnZW0gZGUgZXJybyAkRSQgbsOjbyBleGNlZGEgMiB1bmlkYWRlcyBjb20gdW0gbsOtdmVsIGRlIGNvbmZpYW7Dp2EgZGUgOTklICh1c2UgJFpfe1xcdGV4dHtjcml0fX0gPSAyLDU3NiQpLiIsICJkaWNhIjogIlV0aWxpemUgYSBmw7NybXVsYSBkYSBtYXJnZW0gZGUgZXJybyAkRSA9IFpfe1xcdGV4dHtjcml0fX0gXFxjZG90IFxcZnJhY3tcXHNpZ21hfXtcXHNxcnR7bn19JCBlIGlzb2xlICRuJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiJCRFID0gWl97XFx0ZXh0e2NyaXR9fSBcXGNkb3QgXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0gXFxpbXBsaWVzIFxcc3FydHtufSA9IFxcZnJhY3taX3tcXHRleHR7Y3JpdH19IFxcY2RvdCBcXHNpZ21hfXtFfSQkIiwgIiQkbiA9IFxcbGVmdCggXFxmcmFje1pfe1xcdGV4dHtjcml0fX0gXFxjZG90IFxcc2lnbWF9e0V9IFxccmlnaHQpXjIkJCIsICIkJG4gPSBcXGxlZnQoIFxcZnJhY3syLDU3NiBcXGNkb3QgMTJ9ezJ9IFxccmlnaHQpXjIkJCIsICIkJG4gPSAoMiw1NzYgXFxjZG90IDYpXjIgPSAoMTUsNDU2KV4yIFxcYXBwcm94IDIzOCw4OSQkIiwgIiQkXFx0ZXh0e0NvbW8gbyB0YW1hbmhvIGFtb3N0cmFsIGRldmUgc2VyIGludGVpcm8sIGFycmVkb25kYW1vcyBwYXJhIGNpbWE6IH0gbiA9IDIzOS4kJCJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMjM5LjB9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBwcm9jZXNzbyBpbmR1c3RyaWFsIGRlIGZhYnJpY2HDp8OjbyBkZSBwYXJhZnVzb3MsIGEgbcOpZGlhIGRlIGRpw6JtZXRybyDDqSAkXFxtdSA9IDEwJCBtbSBjb20gJFxcc2lnbWEgPSAwLDUkIG1tLiBVbWEgYW1vc3RyYSBkZSAkbiA9IDEwMCQgcGFyYWZ1c29zIHJldmVsb3UgdW1hIG3DqWRpYSAkXFxiYXJ7WH0gPSAxMCwxNSQgbW0uIENhbGN1bGUgbyBwLXZhbG9yIHBhcmEgZXN0ZSB0ZXN0ZSwgYXNzdW1pbmRvICRIXzE6IFxcbXUgPiAxMCQuIiwgImRpY2EiOiAiTyBwLXZhbG9yIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSBvYnNlcnZhciB1bSB2YWxvciBwZWxvIG1lbm9zIHTDo28gZXh0cmVtbyBxdWFudG8gbyBjYWxjdWxhZG8sIG91IHNlamEsICRQKFogPiBaX3tcXHRleHR7Y2FsY319KSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIiQkWl97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXV9e1xcc2lnbWEgLyBcXHNxcnR7bn19ID0gXFxmcmFjezEwLDE1IC0gMTB9ezAsNSAvIFxcc3FydHsxMDB9fSA9IFxcZnJhY3swLDE1fXswLDA1fSA9IDMsMCQkIiwgIiQkXFx0ZXh0e3AtdmFsb3J9ID0gUChaID4gMywwKSA9IDEgLSBQKFogXFxsZSAzLDApJCQiLCAiJCRcXHRleHR7Q29uc3VsdGFuZG8gYSB0YWJlbGEgbm9ybWFsIHBhZHLDo286IH0gUChaIFxcbGUgMywwKSBcXGFwcHJveCAwLDk5ODckJCIsICIkJFxcdGV4dHtwLXZhbG9yfSA9IDEgLSAwLDk5ODcgPSAwLDAwMTMkJCJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueiA9IG5wLmxpbnNwYWNlKC00LCA0LCAyMDApXG5kZW5zID0gc3RhdHMubm9ybS5wZGYoeilcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXosIHk9ZGVucywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJykpKVxuZmlnLmFkZF92cmVjdCh4MD0zLCB4MT00LCBmaWxsY29sb3I9JyM5OTFCMUInLCBvcGFjaXR5PTAuNSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdDw6FsY3VsbyBkZSBwLXZhbG9yJywgeGF4aXNfdGl0bGU9J1onLCB5YXhpc190aXRsZT0nRGVuc2lkYWRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMDAxM30sIHsiZW51bmNpYWRvIjogIlVtIGxhYm9yYXTDs3JpbyBkZSBjb250cm9sZSBkZSBxdWFsaWRhZGUgbWVkZSBhIGNvbmNlbnRyYcOnw6NvIGRlIHVtIHBvbHVlbnRlIGVtIGVmbHVlbnRlcyBpbmR1c3RyaWFpcy4gVW1hIGFtb3N0cmEgZGUgMTYgbWVkacOnw7VlcyBhcHJlc2VudG91IG3DqWRpYSAkXFxiYXJ7WH0gPSA0NSQgbWcvTCBlIGRlc3ZpbyBwYWRyw6NvIGFtb3N0cmFsICRTID0gOCQgbWcvTC4gQ29uc2lkZXJhbmRvIGEgcG9wdWxhw6fDo28gbm9ybWFsLCBjYWxjdWxlIG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgZGUgOTUlIHBhcmEgYSBtw6lkaWEgcG9wdWxhY2lvbmFsICRcXG11JC4iLCAiZGljYSI6ICJJZGVudGlmaXF1ZSBvcyBncmF1cyBkZSBsaWJlcmRhZGUgJGdsID0gbiAtIDEkIGUgY29uc3VsdGUgbyB2YWxvciBjcsOtdGljbyAkdF97XFx0ZXh0e2NyaXR9fSQgcGFyYSAkMSAtIFxcYWxwaGEgPSAwLDk1JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYXIgb3MgcGFyw6JtZXRyb3M6ICRcXGJhcntYfSA9IDQ1JCwgJFMgPSA4JCwgJG4gPSAxNiQsICRcXGFscGhhID0gMCwwNSQuIiwgIjIuIENhbGN1bGFyIG9zIGdyYXVzIGRlIGxpYmVyZGFkZTogJGdsID0gMTYgLSAxID0gMTUkLiIsICIzLiBEZXRlcm1pbmFyIG8gdmFsb3IgY3LDrXRpY28gJHRfe1xcdGV4dHtjcml0fX0kIHRhbCBxdWUgJFAoLXRfe1xcdGV4dHtjcml0fX0gPCB0KDE1KSA8IHRfe1xcdGV4dHtjcml0fX0pID0gMCw5NSQuIFBlbGEgdGFiZWxhLCAkdF97XFx0ZXh0e2NyaXR9fSBcXGFwcHJveCAyLDEzMSQuIiwgIjQuIENhbGN1bGFyIG8gZXJybyBwYWRyw6NvOiAkRVAoXFxiYXJ7WH0pID0gXFxmcmFje1N9e1xcc3FydHtufX0gPSBcXGZyYWN7OH17XFxzcXJ0ezE2fX0gPSBcXGZyYWN7OH17NH0gPSAyJC4iLCAiNS4gQ2FsY3VsYXIgbyBpbnRlcnZhbG86ICRJQyhcXG11OyAwLDk1KSA9IDQ1IFxccG0gKDIsMTMxIFxcY2RvdCAyKSA9IDQ1IFxccG0gNCwyNjIkLiIsICI2LiBDb25jbHVzw6NvOiBPIGludGVydmFsbyBkZSBjb25maWFuw6dhIMOpICRbNDAsNzM4OyA0OSwyNjJdJCBtZy9MLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNTYiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiA0MC43Mzh9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgZG8gcG9udG8gZGUgdmlzdGEgY29uY2VpdHVhbCBlIG1hdGVtw6F0aWNvLCBwb3IgcXVlIGEgZGlzdHJpYnVpw6fDo28gdCBkZSBTdHVkZW50IGFwcmVzZW50YSBjYXVkYXMgbWFpcyAncGVzYWRhcycgZG8gcXVlIGEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIHBhZHLDo28gZSBjb21vIGlzc28gYWZldGEgYSBlc3RpbWHDp8OjbyBkZSAkXFxtdSQuIiwgImRpY2EiOiAiUGVuc2UgbmEgZGlmZXJlbsOnYSBlbnRyZSBvIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCAkXFxzaWdtYSQgZSBvIGVzdGltYWRvciBhbW9zdHJhbCAkUyQgZSBjb21vIGEgaW5jZXJ0ZXphIHNvYnJlICRTJCBpbmZsdWVuY2lhIGEgZGlzcGVyc8OjbyBkYSBlc3RhdMOtc3RpY2EgJFQkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBBIGVzdGF0w61zdGljYSAkWiA9IChcXGJhcntYfSAtIFxcbXUpIC8gKFxcc2lnbWEvXFxzcXJ0e259KSQgdXRpbGl6YSB1bSBwYXLDom1ldHJvIGZpeG8gJFxcc2lnbWEkLCBlbnF1YW50byAkVCA9IChcXGJhcntYfSAtIFxcbXUpIC8gKFMvXFxzcXJ0e259KSQgdXRpbGl6YSB1bWEgdmFyacOhdmVsIGFsZWF0w7NyaWEgJFMkLiIsICIyLiBDb21vICRTJCDDqSB1bWEgZXN0aW1hdGl2YSwgZWxlIHBvZGUgYXNzdW1pciB2YWxvcmVzIG1lbm9yZXMgcXVlIG8gdmVyZGFkZWlybyAkXFxzaWdtYSQgZGV2aWRvIMOgIHZhcmlhYmlsaWRhZGUgYW1vc3RyYWwuIiwgIjMuIFF1YW5kbyAkUyQgw6kgc3ViZXN0aW1hZG8sIG8gdmFsb3IgZGUgJFQkIHRlbmRlIGEgdmFsb3JlcyBtYWlzIGV4dHJlbW9zIChtYWlvcmVzIGVtIG3Ds2R1bG8pLCBvIHF1ZSByZXN1bHRhIGVtIHVtYSBkaXN0cmlidWnDp8OjbyBjb20gbWFpb3IgY29uY2VudHJhw6fDo28gbmFzIGNhdWRhcy4iLCAiNC4gTWF0ZW1hdGljYW1lbnRlLCBhIHZhcmnDom5jaWEgZGEgZGlzdHJpYnVpw6fDo28gdCDDqSAkVmFyKFQpID0gZ2wgLyAoZ2wgLSAyKSQgcGFyYSAkZ2wgPiAyJCwgbyBxdWUgw6kgc2VtcHJlIG1haW9yIHF1ZSAxIChhIHZhcmnDom5jaWEgZGEgbm9ybWFsIHBhZHLDo28pLiIsICI1LiBJc3NvIGFmZXRhIGEgZXN0aW1hw6fDo28gZXhpZ2luZG8gdmFsb3JlcyBjcsOtdGljb3MgKCR0X3tcXHRleHR7Y3JpdH19JCkgbWFpb3JlcyBkbyBxdWUgb3MgZGEgbm9ybWFsICgkWl97XFx0ZXh0e2NyaXR9fSQpIHBhcmEgbyBtZXNtbyBuw612ZWwgZGUgY29uZmlhbsOnYSwgdG9ybmFuZG8gbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBtYWlzIGNvbnNlcnZhZG9yIChtYWlzIGxhcmdvKS4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgtNCwgNCwgMjAwKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT1zdGF0cy5ub3JtLnBkZih4KSwgbmFtZT0nTm9ybWFsICROKDAsMSkkJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJykpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT1zdGF0cy50LnBkZih4LCAzKSwgbmFtZT0ndCBkZSBTdHVkZW50ICgkZ2w9MyQpJywgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJykpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkNvbXBhcmHDp8OjbzogTm9ybWFsIHZzLiB0IGRlIFN0dWRlbnQ8L2I+JywgeGF4aXNfdGl0bGU9J3gnLCB5YXhpc190aXRsZT0nRGVuc2lkYWRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJTdXBvbmhhIHF1ZSB1bSBub3ZvIHByb2Nlc3NvIGRlIG1vbnRhZ2VtIHJlZHV6aXUgbyB0ZW1wbyBtw6lkaW8gZGUgdGFyZWZhIHBhcmEgODUgbWludXRvcywgY29tIHVtIGRlc3ZpbyBwYWRyw6NvIGRlIDEyIG1pbnV0b3MsIGJhc2VhZG8gZW0gdW1hIGFtb3N0cmEgZGUgMTYgb3BlcsOhcmlvcy4gQ29uc3RydWEgbyBsaW1pdGUgc3VwZXJpb3IgZGUgdW0gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgZGUgOTklIHBhcmEgYSB2ZXJkYWRlaXJhIG3DqWRpYSBwb3B1bGFjaW9uYWwgJFxcbXUkLiIsICJkaWNhIjogIkNvbnNpZGVyZSAkbj0xNiQgZSAkXFxhbHBoYT0wLDAxJC4gTyB2YWxvciBjcsOtdGljbyAkdF97XFx0ZXh0e2NyaXR9fSQgcGFyYSAkZ2w9MTUkIGNvbSA5OSUgZGUgY29uZmlhbsOnYSDDqSBhcHJveGltYWRhbWVudGUgMiw5NDcuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIERhZG9zOiAkXFxiYXJ7WH0gPSA4NSQsICRTID0gMTIkLCAkbiA9IDE2JC4iLCAiMi4gR3JhdXMgZGUgbGliZXJkYWRlOiAkZ2wgPSAxNiAtIDEgPSAxNSQuIiwgIjMuIE7DrXZlbCBkZSBjb25maWFuw6dhIDk5JSAoJDEtXFxhbHBoYSA9IDAsOTkkKSwgbG9nbyAkdF97XFx0ZXh0e2NyaXR9fSA9IDIsOTQ3JC4iLCAiNC4gRXJybyBwYWRyw6NvOiAkRVAgPSBTIC8gXFxzcXJ0e259ID0gMTIgLyA0ID0gMyQuIiwgIjUuIE1hcmdlbSBkZSBlcnJvOiAkRSA9IHRfe1xcdGV4dHtjcml0fX0gXFxjZG90IEVQID0gMiw5NDcgXFxjZG90IDMgPSA4LDg0MSQuIiwgIjYuIExpbWl0ZSBzdXBlcmlvcjogJExTID0gXFxiYXJ7WH0gKyBFID0gODUgKyA4LDg0MSA9IDkzLDg0MSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM1OCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDkzLjg0MX0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBkZSBjb250cm9sZSBkZSBxdWFsaWRhZGUsIHVtYSBhbW9zdHJhIGRlICRuID0gOTAwJCBjb21wb25lbnRlcyBmb2kgdGVzdGFkYSwgcmV2ZWxhbmRvIHF1ZSAkNDUkIGVyYW0gZGVmZWl0dW9zb3MuIENvbnN0cnVhIG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgZGUgJDk5XFwlJCBwYXJhIGEgcHJvcG9yw6fDo28gcG9wdWxhY2lvbmFsICRwJCBkZSBjb21wb25lbnRlcyBkZWZlaXR1b3NvcyBlIGludGVycHJldGUgbyByZXN1bHRhZG8uIiwgImRpY2EiOiAiVXNlICR6ID0gMiw1NzYkIHBhcmEgJDk5XFwlJCBkZSBjb25maWFuw6dhLiBDYWxjdWxlICRcXGhhdHtwfSA9IDQ1LzkwMCQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIiRcXGhhdHtwfSA9IDQ1IC8gOTAwID0gMCwwNSQuIiwgIiRcXGhhdHtxfSA9IDEgLSAwLDA1ID0gMCw5NSQuIiwgIk8gZXJybyBwYWRyw6NvIGVzdGltYWRvIMOpICRFUCA9IFxcc3FydHsoMCwwNSBcXHRpbWVzIDAsOTUpIC8gOTAwfSA9IFxcc3FydHswLDA0NzUgLyA5MDB9IFxcYXBwcm94IDAsMDA3MjYkLiIsICJBIG1hcmdlbSBkZSBlcnJvIHBhcmEgJFxcZ2FtbWEgPSAwLDk5JCDDqSAkRSA9IDIsNTc2IFxcdGltZXMgMCwwMDcyNiBcXGFwcHJveCAwLDAxODckLiIsICJPICRJQyhwOyAwLDk5KSA9IDAsMDUgXFxwbSAwLDAxODckLCByZXN1bHRhbmRvIGVtICRbMCwwMzEzOyAwLDA2ODddJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMDV9LCB7ImVudW5jaWFkbyI6ICJTdXBvbmhhIHF1ZSB1bSBwZXNxdWlzYWRvciBkZXNlamUgcmVkdXppciBhIGFtcGxpdHVkZSBkbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBjYWxjdWxhZG8gbmEgcXVlc3TDo28gYW50ZXJpb3IgcGVsYSBtZXRhZGUsIG1hbnRlbmRvIG8gbsOtdmVsIGRlIGNvbmZpYW7Dp2EuIENvbW8gbyB0YW1hbmhvIGRhIGFtb3N0cmEgZGV2ZSBzZXIgYWx0ZXJhZG8/IiwgImRpY2EiOiAiQSBhbXBsaXR1ZGUgZG8gaW50ZXJ2YWxvIMOpICRBID0gMiBcXHRpbWVzIHogXFx0aW1lcyBcXHNxcnR7XFxoYXR7cH1cXGhhdHtxfS9ufSQuIEFuYWxpc2UgYSByZWxhw6fDo28gZW50cmUgJEEkIGUgJFxcc3FydHtufSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgYW1wbGl0dWRlIGRvIGludGVydmFsbyDDqSBkYWRhIHBvciAkQSA9IDIgeiBcXHNxcnR7XFxmcmFje1xcaGF0e3B9XFxoYXR7cX19e259fSQuIiwgIlBhcmEgcmVkdXppciBhIGFtcGxpdHVkZSBwZWxhIG1ldGFkZSAoJEFfe25vdm99ID0gQS8yJCksIGRldmUtc2UgdGVyICRcXGZyYWN7MX17XFxzcXJ0e25fe25vdm99fX0gPSBcXGZyYWN7MX17Mlxcc3FydHtuX3tvcmlnaW5hbH19fSQuIiwgIklzc28gaW1wbGljYSAkXFxzcXJ0e25fe25vdm99fSA9IDJcXHNxcnR7bl97b3JpZ2luYWx9fSQsIG91ICRuX3tub3ZvfSA9IDQgbl97b3JpZ2luYWx9JC4iLCAiUG9ydGFudG8sIG8gdGFtYW5obyBkYSBhbW9zdHJhIGRldmUgc2VyIHF1YWRydXBsaWNhZG8gcGFyYSByZWR1emlyIGEgbWFyZ2VtIGRlIGVycm8gKGUgY29uc2VxdWVudGVtZW50ZSBhIGFtcGxpdHVkZSkgcGVsYSBtZXRhZGUuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIGR1YXMgY2lkYWRlcywgQSBlIEIuIE5hIGNpZGFkZSBBLCB1bWEgYW1vc3RyYSBkZSAkNDAwJCBwZXNzb2FzIHJldmVsb3UgcXVlICQxODAkIGFwcm92YW0gdW0gcHJvamV0byBww7pibGljby4gTmEgY2lkYWRlIEIsIHVtYSBhbW9zdHJhIGRlICQ2MDAkIHBlc3NvYXMgcmV2ZWxvdSBxdWUgJDM1MCQgYXByb3ZhbSBvIG1lc21vIHByb2pldG8uIENhbGN1bGUgYSBkaWZlcmVuw6dhIGVudHJlIGFzIHByb3BvcsOnw7VlcyBhbW9zdHJhaXMgJFxcaGF0e3B9X0EgLSBcXGhhdHtwfV9CJCBlIG8gZXJybyBwYWRyw6NvIGRlc3NhIGRpZmVyZW7Dp2EuIiwgImRpY2EiOiAiVXNlICRFUF97ZGlmfSA9IFxcc3FydHtcXGZyYWN7XFxoYXR7cH1fQVxcaGF0e3F9X0F9e25fQX0gKyBcXGZyYWN7XFxoYXR7cH1fQlxcaGF0e3F9X0J9e25fQn19JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiJFxcaGF0e3B9X0EgPSAxODAgLyA0MDAgPSAwLDQ1JCBlICRcXGhhdHtwfV9CID0gMzUwIC8gNjAwIFxcYXBwcm94IDAsNTgzMyQuIiwgIkEgZGlmZXJlbsOnYSDDqSAkXFxoYXR7cH1fQSAtIFxcaGF0e3B9X0IgPSAwLDQ1IC0gMCw1ODMzID0gLTAsMTMzMyQuIiwgIiRcXGhhdHtxfV9BID0gMCw1NSQgZSAkXFxoYXR7cX1fQiA9IDEgLSAwLDU4MzMgPSAwLDQxNjckLiIsICJWYXJpw6JuY2lhIEE6ICQwLDQ1IFxcdGltZXMgMCw1NSAvIDQwMCA9IDAsMjQ3NSAvIDQwMCA9IDAsMDAwNjE4NzUkLiIsICJWYXJpw6JuY2lhIEI6ICQwLDU4MzMgXFx0aW1lcyAwLDQxNjcgLyA2MDAgXFxhcHByb3ggMCwyNDMxIC8gNjAwID0gMCwwMDA0MDUyJC4iLCAiRXJybyBwYWRyw6NvIGRhIGRpZmVyZW7Dp2E6ICRcXHNxcnR7MCwwMDA2MTg3NSArIDAsMDAwNDA1Mn0gPSBcXHNxcnR7MCwwMDEwMjM5NX0gXFxhcHByb3ggMCwwMzE5OTgkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEzLCBwLiAzODgiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAtMC4xMzMzfV19').decode('utf-8'))


    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    from scipy import stats
    
    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do total de exercícios
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discs = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcqs) + len(discs)
    
    # Placar de progresso
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    
    st.divider()
    
    # --- Renderização de Questões de Múltipla Escolha ---
    if mcqs:
        st.subheader("📝 Questões de Múltipla Escolha")
        for i, questao in enumerate(mcqs):
            with st.container(border=True):
                st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
                
                # Referência bibliográfica
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
    
                # Renderização de gráfico plotly, se houver
                codigo = questao.get("codigo_plotly")
                if codigo:
                    local_vars = {"go": go, "np": np, "stats": stats}
                    try:
                        exec(codigo, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
                    except Exception as e:
                        st.warning(f"Erro ao renderizar gráfico: {e}")
    
                # Dica
                if st.button("💡 Dica", key=f"btn_dica_mcq_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
    
                # Alternativas
                alts = questao.get("alternativas", {})
                opcoes = [f"{k}: {v}" for k, v in alts.items()]
                escolha = st.radio("Escolha uma alternativa:", opcoes, key=f"radio_mcq_{i}", index=None)
    
                # Verificação
                if st.button("✅ Verificar Resposta", key=f"btn_check_mcq_{i}"):
                    if escolha:
                        letra_escolhida = escolha.split(":")[0]
                        if letra_escolhida == questao.get("alternativa_correta"):
                            st.success("Correto! Muito bem.")
                            st.session_state.respostas_certas[f"mcq_{i}"] = True
                        else:
                            st.error("Resposta incorreta. Tente novamente!")
                            st.session_state.respostas_certas[f"mcq_{i}"] = False
                    else:
                        st.warning("Selecione uma alternativa antes de verificar.")
    
                # Gabarito Comentado
                with st.expander("✅ Ver Gabarito Comentado"):
                    st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
    
    st.divider()
    
    # --- Renderização de Questões Discursivas ---
    if discs:
        st.subheader("✍️ Questões Discursivas")
        for i, questao in enumerate(discs):
            with st.container(border=True):
                st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
                
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                codigo = questao.get("codigo_plotly")
                if codigo:
                    local_vars = {"go": go, "np": np, "stats": stats}
                    try:
                        exec(codigo, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
                    except Exception as e:
                        st.warning(f"Erro ao renderizar gráfico: {e}")
                
                st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
                
                # Validação numérica ou checkbox de conclusão
                esperada = questao.get("resposta_numerica_esperada")
                if esperada is not None:
                    user_val = st.number_input("Digite o resultado numérico calculado:", key=f"num_disc_{i}", format="%.4f")
                    if st.button("Validar Cálculo", key=f"val_disc_{i}"):
                        if abs(user_val - esperada) <= max(0.01, 0.01 * abs(esperada)):
                            st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                            st.session_state.respostas_certas[f"disc_{i}"] = True
                        else:
                            st.error("O valor calculado difere do gabarito oficial. Tente novamente.")
                            st.session_state.respostas_certas[f"disc_{i}"] = False
                else:
                    concluido = st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}")
                    st.session_state.respostas_certas[f"disc_{i}"] = concluido
    
                if st.button("💡 Dica", key=f"btn_dica_disc_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
    
                with st.expander("✅ Ver Resolução Detalhada"):
                    for passo in questao.get("gabarito_passo_a_passo", []):
                        st.markdown(f"- {passo}")
