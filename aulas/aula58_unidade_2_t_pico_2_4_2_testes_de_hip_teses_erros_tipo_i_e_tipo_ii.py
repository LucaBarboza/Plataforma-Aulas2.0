import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4yOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogRXJyb3MgdGlwbyBJIGUgdGlwbyBJSSIsICJyZWZlcmVuY2lhc19iaWJsaW9ncmFmaWNhc19maW5haXMiOiBbIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSAtIENhcMOtdHVsbyAxMiwgcHAuIDMzMi0zNDgiXX0=').decode('utf-8'))

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
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"A Estrutura Lógica do Processo Decisório Inferencial")
    
    # Introdução e Prosa Teórica - Parte 1
    st.markdown(r"""
    O processo decisório inferencial constitui o alicerce da estatística moderna, funcionando como um tribunal científico onde avaliamos a veracidade de uma afirmação populacional a partir de evidências amostrais limitadas.
    """)
    
    st.info(r"Ao estabelecermos a Hipótese Nula (H0), definimos um estado de referência que desejamos validar. Dada a natureza parcial da amostra, estamos suscetíveis a conclusões errôneas, cujas consequências são categorizadas como erros estatísticos.")
    
    st.markdown(r"""
    Para garantir o rigor científico, o processo baseia-se em dois pilares de erro:
    *   **Erro Tipo I (Falso Positivo):** Análogo à punição de um inocente; ocorre quando rejeitamos H0 embora ela seja verdadeira.
    *   **Erro Tipo II (Falso Negativo):** Análogo à falha de detectar um culpado; ocorre quando mantemos H0 mesmo sendo ela falsa.
    """)
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Formalismo do Teste")
    st.latex(r"H_0: \theta = \theta_0 \quad \text{vs} \quad H_1: \theta \neq \theta_0")
    st.markdown(r"A Região Crítica (RC) é definida para controlar o risco do erro tipo I ($\alpha$):")
    st.latex(r"RC = \{ \hat{\theta} : P(\hat{\theta} | H_0) \le \alpha \}")
    
    # Dedução Analítica
    st.markdown(r"A lógica operacional segue uma sequência dedutiva estrita:")
    st.latex(r"H_0: \theta = \theta_0")
    st.latex(r"H_1: \theta \neq \theta_0")
    st.latex(r"\alpha = P(\hat{\theta} \in RC | H_0)")
    
    st.markdown(r"A regra de decisão é formalizada como:")
    st.latex(r"\text{Decisão} = \begin{cases} \text{Rejeitar } H_0, & \text{se } \hat{\theta} \in RC \\ \text{Não rejeitar } H_0, & \text{se } \hat{\theta} \notin RC \end{cases}")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Controle de Processos")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Indústria de Café Automatizada")
        st.markdown(r"Uma indústria regula o envase para uma média de 500g com variância populacional conhecida de $\sigma^2 = 400$. Um auditor, preocupado com desvios, seleciona 16 pacotes aleatórios. Nível de significância $\alpha = 1\%$.")
        
        st.latex(r"\mu_0 = 500, \sigma^2 = 400, n = 16, \alpha = 0,01")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Cálculo do Erro Padrão:** $EP(\bar{X}) = \sqrt{400 / 16} = 5$")
        st.markdown(r"- **Valor Crítico:** Para $\alpha = 0,01$ (cauda dupla), $Z_{\text{crit}} = 2,58$")
        st.markdown(r"- **Intervalo de Rejeição:** $\bar{x}_c = 500 \pm 2,58 \times 5 = 500 \pm 12,9$")
        
        st.success(r"**Laudo Comercial:** A região crítica é definida como $\{ \bar{X} < 487,1 \text{ ou } \bar{X} > 512,9 \}$. Se a média amostral observada estiver fora de [487,1; 512,9], a máquina deve ser parada para calibração, com 99% de confiança.")
    
    # Prosa Expandida final
    st.markdown(r"""
    ---
    ### 🧠 Reflexão Epistemológica
    O processo decisório inferencial é uma defesa contra o viés humano de ver padrões onde não existem. 
    Ao aderir a este protocolo, impomos uma disciplina rigorosa à nossa busca pelo conhecimento:
    1. **Estabelecimento de H0:** A âncora paramétrica do status quo.
    2. **Definição de $\alpha$:** O controle consciente da probabilidade de erro.
    3. **Verificação da RC:** O filtro estatístico que separa o sinal do ruído.
    
    Embora nunca possamos ter certeza absoluta sobre os parâmetros populacionais, este formalismo é o método mais robusto disponível para gerenciar a incerteza estatística.
    """)

    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Definições Formais de Erros Inferenciais")
    
    # Introdução Teórica
    st.markdown(r"""
    A inferência estatística constitui o arcabouço lógico pelo qual transcendemos a descrição puramente amostral para alcançarmos generalizações acerca da população. Ao operarmos sob um regime de incerteza — decorrente da impossibilidade prática de observar a totalidade da população — estamos sujeitos ao risco. A estatística não oferece certezas absolutas, mas um gerenciamento probabilístico da falibilidade.
    """)
    
    st.markdown(r"""
    O paradigma neyman-pearsoniano de testes de hipóteses organiza a nossa decisão em torno de dois estados:
    - **Hipótese Nula ($H_0$):** Representa o estado de estabilidade, a ausência de efeito ou a igualdade que desejamos desafiar.
    - **Hipótese Alternativa ($H_1$):** Codifica o desvio, o efeito ou a diferença que suspeitamos ser a realidade subjacente aos dados.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Erros Tipo I e Tipo II")
    st.markdown(r"O controle desses erros exige a especificação rigorosa da região de aceitação. As probabilidades de erro são definidas como:")
    
    st.latex(r"\alpha = P(\text{Rejeitar } H_0 | H_0 \text{ verdadeira})")
    st.latex(r"\beta = P(\text{Não rejeitar } H_0 | H_0 \text{ falsa})")
    
    st.info(r"O nível de significância $\alpha$ é fixado pelo pesquisador para limitar a taxa de falsos positivos, enquanto o Erro Tipo II ($\beta$) depende do tamanho amostral e da magnitude do efeito em $H_1$.")
    
    # Demonstração Analítica
    st.markdown(r"### 🧮 Dedução das Propriedades do Teste")
    st.markdown(r"A decisão estatística baseia-se na comparação do estimador pontual $\hat{\theta}$ com a região crítica ($RC$):")
    
    st.latex(r"\alpha = P(\hat{\theta} \in RC | H_0)")
    st.latex(r"\beta = P(\hat{\theta} \notin RC | H_1)")
    st.latex(r"\text{Poder} = 1 - \beta = P(\hat{\theta} \in RC | H_1)")
    
    st.markdown(r"""
    Existe um compromisso intrínseco: para um determinado $n$, reduzir $\alpha$ inevitavelmente eleva $\beta$. A única forma de reduzir ambos simultaneamente é através do incremento do tamanho amostral $n$, o que reduz a variabilidade dos estimadores e diminui a sobreposição entre as distribuições sob $H_0$ e $H_1$.
    """)
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática: Sensores Eletrônicos")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Teste de Lote de Sensores")
        st.markdown(r"Um fabricante de sensores de $150\Omega$ testa um novo lote com $n=25$ itens, sabendo que $\sigma=20$. Queremos testar $H_0: \mu=155$ contra $H_1: \mu=145$. Decisão: rejeitar $H_0$ quando $\bar{X} \le 150$.")
        
        st.latex(r"H_0: \mu=155, \quad H_1: \mu=145, \quad n=25, \quad \sigma=20")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Cálculo de $\alpha$:** Sob $H_0$, $\bar{X} \sim N(155, 16)$, logo $Z = \frac{150-155}{4} = -1,25$. A probabilidade é $\alpha = P(Z \le -1,25) = 0,1056$.")
        st.markdown(r"- **Cálculo de $\beta$:** Sob $H_1$, $\bar{X} \sim N(145, 5,76)$, logo $Z = \frac{150-145}{2,4} = 2,08$. A probabilidade é $\beta = P(Z > 2,08) = 0,0188$.")
        
        st.success(r"Laudo Comercial: O teste apresenta um risco de 10,56% para o Erro Tipo I e 1,88% para o Erro Tipo II. Esta configuração protege a detecção da alternativa $H_1$, mas tolera um falso positivo considerável em relação à hipótese original.")
    
    # Nota Final de Rigor Científico
    st.divider()
    st.markdown(r"""
    *Nota: A prática da inferência é uma gestão sistemática de riscos. Ignorar a dualidade entre o Erro Tipo I e o Erro Tipo II é negligenciar a natureza estocástica dos dados.*
    """)

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    # Cabeçalho do Subtópico
    st.header(r"Equilíbrio entre Significância e Poder do Teste")
    
    # Prosa Teórica - Parte 1
    st.markdown(r"""
    A jornada da estatística inferencial exige a arquitetura de um protocolo de decisão sob incerteza. Quando estabelecemos hipóteses nulas ($H_0$) e alternativas ($H_1$), tentamos discernir se o efeito observado é apenas variabilidade aleatória ou uma mudança estrutural no parâmetro $\theta$.
    """)
    
    st.info(r"O nível de significância $\alpha$ é a nossa barreira de proteção contra falsos positivos, enquanto o poder do teste ($1-\beta$) representa a nossa capacidade de detectar um efeito real.")
    
    # Prosa Teórica - Parte 2 (Lista)
    st.markdown(r"""
    O trade-off fundamental entre estes dois pilares pode ser resumido em:
    - **Nível de Significância ($\alpha$):** A tolerância máxima para o Erro Tipo I. Fronteira estática que, ao ser reduzida, aumenta a zona de aceitação.
    - **Poder do Teste ($1-\beta$):** A sensibilidade do teste em rejeitar $H_0$ quando $H_1$ é verdadeira. É uma função contínua do parâmetro $\theta$.
    - **Tamanho Amostral ($n$):** O único mecanismo real para reduzir $\alpha$ e $\beta$ simultaneamente ao estreitar as distribuições amostrais.
    """)
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Equilíbrio Inferencial")
    st.latex(r"\pi(\theta) = 1 - \beta(\theta) = P(\hat{\theta} \in RC | \theta)")
    
    # Demonstração Analítica (Sequencial)
    st.latex(r"\pi(\theta_0) = \alpha")
    st.markdown(r"A função poder avaliada na hipótese nula retorna exatamente o nível de significância.")
    st.latex(r"\pi(\theta_1) = 1 - \beta")
    st.markdown(r"Já sob a hipótese alternativa, o poder é o complemento da probabilidade de erro Tipo II.")
    st.latex(r"\text{Poder aumenta quando } |\theta_1 - \theta_0| \text{ aumenta ou } n \text{ aumenta}")
    
    # Simulador: Explorador de Poder e Tamanho Amostral
    st.markdown(r"### 📈 Simulador: Explorador de Poder e Tamanho Amostral")
    
    col1, col2, col3 = st.columns(3)
    alpha_val = col1.slider(r"Nível de Significância ($\alpha$)", 0.01, 0.1, 0.05, step=0.01, key=r"alpha_subtopico_3")
    n_val = col2.slider(r"Tamanho Amostral ($n$)", 10, 100, 30, step=5, key=r"n_subtopico_3")
    mu_alt = col3.slider(r"Valor Real de $\mu$ (Sob $H_1$)", 500.0, 520.0, 505.0, step=0.5, key=r"mu_subtopico_3")
    
    # Cálculo do simulador
    sigma = 20
    se = sigma / np.sqrt(n_val)
    z_crit = norm.ppf(1 - alpha_val / 2)
    limite_inf = 500 - z_crit * se
    limite_sup = 500 + z_crit * se
    
    x = np.linspace(480, 520, 500)
    y0 = norm.pdf(x, 500, se)
    y1 = norm.pdf(x, mu_alt, se)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y0, name=r"H0: \mu=500", line=dict(color="#1E3A8A")))
    fig.add_trace(go.Scatter(x=x, y=y1, name=r"H1: \mu=505", line=dict(color="#10B981")))
    
    # Desenho das áreas
    fig.add_vrect(x0=limite_inf, x1=limite_sup, fillcolor="#991B1B", opacity=0.1, line_width=0)
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Densidades: H0 vs H1</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Média Amostral", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    # Laudo dinâmico
    st.info(f"Com n = {n_val}, o erro padrão é {se:.2f}. A região crítica está definida entre {limite_inf:.2f} e {limite_sup:.2f}. Movimentar o tamanho da amostra reduz a sobreposição entre as curvas, aumentando o poder do teste.")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática: Máquina de Envase")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Detectando Variações na Produção")
        st.markdown(r"Considerando a máquina de envase com $\sigma^2=400$, $n=16$ e $\alpha=0,01$. Queremos calcular o poder para detectar $\mu = 505g$.")
        st.latex(r"H_0: \mu=500, H_1: \mu=505, \bar{X} \sim N(505, 25)")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- $Z_1 = \frac{487,1 - 505}{5} = -3,58$")
        st.markdown(r"- $Z_2 = \frac{512,9 - 505}{5} = 1,58$")
        st.success(r"Conclusão: $\pi(505) = P(Z < -3,58) + P(Z > 1,58) = 0,0002 + 0,0571 = 0,0573$. O teste possui apenas 5,73% de poder; a ineficácia é clara, demandando aumento amostral.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Estilização Global para um visual de luxo acadêmico
    st.markdown(
        """
        <style>
        .stApp { background-color: #FFFFFF; }
        .css-1r6slp0 { font-family: 'Georgia', serif; }
        .big-font { font-size: 20px !important; color: #1E293B; }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # 1. CABEÇALHO DO SUBTÓPICO
    st.header(r"Função Característica de Operação")
    
    # 2. PROSA TEÓRICA ESTRUTURADA
    st.markdown(r"A inferência estatística é uma disciplina de tomada de decisão sob incerteza. Quando um engenheiro de controle de qualidade estabelece um teste de hipóteses, a análise muitas vezes se limita a um ponto crítico (o nível de significância $\alpha$). Contudo, para uma visão completa da performance do procedimento, precisamos de uma análise panorâmica através da **Função Característica de Operação (função CO)**.")
    
    st.info(r"A função CO, denotada por $\beta(\theta)$, mapeia a probabilidade de o teste falhar ao não rejeitar $H_0$ (erro Tipo II) para todo o espectro possível de valores do parâmetro real $\theta$.")
    
    st.markdown(r"""
    ### 📊 Propriedades Fundamentais da Função CO
    - **Visão Panorâmica:** Ao invés de um ponto isolado, observamos o comportamento do teste frente a desvios na realidade.
    - **Complementariedade:** Ela é o inverso matemático da função poder ($\pi(\theta)$).
    - **Gestão de Risco:** Permite identificar a robustez do teste contra variações indesejadas no processo.
    """)
    
    # 3. DEMONSTRAÇÃO ANALÍTICA
    st.subheader(r"📐 O Rigor Matemático: Função CO e Poder")
    st.markdown(r"O comportamento estatístico do teste é regido pela relação entre o erro de aceitação indevida e o poder de detecção de desvios:")
    
    st.latex(r"\beta(\theta) = 1 - P(\hat{\theta} \in RC | \theta)")
    st.markdown(r"Sendo que a relação com o poder do teste é direta:")
    st.latex(r"\pi(\theta) = 1 - \beta(\theta)")
    st.markdown(r"E, no limite da hipótese nula, recuperamos o controle sobre o erro de primeira espécie:")
    st.latex(r"\lim_{\theta \to \theta_0} \beta(\theta) = 1 - \alpha")
    
    # 4. EXEMPLOS PRÁTICOS
    st.subheader(r"📈 Casos de Aplicação Prática: Avaliação de Processos Produtivos")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Máquina de Envase")
        st.markdown(r"Considerando um processo produtivo onde se busca detectar um deslocamento na média de 5g, avaliamos o risco de falha ($\beta$) para $\mu = 505g$.")
        
        st.latex(r"\beta(505) = P(-3,58 < Z < 1,58)")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Identificação dos limites probabilísticos: $P(Z \le -3,58) = 0,0002$ e $P(Z \le 1,58) = 0,9429$.")
        st.markdown(r"- Aplicação do cálculo complementar: $\beta(505) = P(Z < 1,58) - P(Z < -3,58)$.")
        st.markdown(r"- Resultado Final: $\beta(505) = 0,9429 - 0,0002 = 0,9427$.")
        
        st.success(r"Com 94,27% de probabilidade de erro Tipo II, o teste é excessivamente permissivo. Recomenda-se aumentar o tamanho da amostra para elevar o poder discriminatório do controle.")
    
    # 5. PROSA LONGA EXPANDIDA
    with st.expander(r"📚 Aprofundamento Teórico: A Filosofia de Neyman-Pearson"):
        st.markdown(r"""
        A função CO transforma a estatística inferencial de uma ferramenta de "veredicto" binário para uma ferramenta de "gerenciamento de risco". 
        
        Historicamente, a necessidade desta função surgiu da demanda industrial por transparência. Antes da sua formalização, os critérios de aceitação eram fixados por normas arbitrárias, sem uma compreensão clara de como variações sutis no parâmetro populacional impactariam o resultado.
        
        À medida que aumentamos o tamanho amostral $n$, a função CO torna-se mais íngreme, assemelhando-se a uma função degrau. Este fenômeno demonstra que o esforço amostral investido é, na verdade, um investimento na capacidade de discernimento do sistema. O domínio deste conceito permite que gestores de qualidade transitem de um controle reativo para um sistema de garantia de qualidade preditivo.
        """)

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4yOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogRXJyb3MgdGlwbyBJIGUgdGlwbyBJSSIsICJxdWVzdG9lc19tdWx0aXBsYV9lc2NvbGhhIjogW3siZW51bmNpYWRvIjogIlVtIGxhYm9yYXTDs3JpbyBkZSBjb250cm9sZSBkZSBxdWFsaWRhZGUgbW9uaXRvcmEgbyBkacOibWV0cm8gZGUgcGXDp2FzIGluZHVzdHJpYWlzLiBTb2IgY29uZGnDp8O1ZXMgbm9ybWFpcywgYSBtw6lkaWEgcG9wdWxhY2lvbmFsIMOpICRcXG11ID0gNTAkIG1tIGNvbSBkZXN2aW8gcGFkcsOjbyBjb25oZWNpZG8gJFxcc2lnbWEgPSAyJCBtbS4gTyBnZXN0b3IgZGEgcGxhbnRhLCBkZXNjb25maWFkbyBkZSBxdWUgbyBwcm9jZXNzbyBwZXJkZXUgYSBwcmVjaXPDo28gKGF1bWVudGFuZG8gYSB2YXJpYcOnw6NvIG91IGEgbcOpZGlhKSwgZGVjaWRlIHJlYWxpemFyIHVtIHRlc3RlIGRlIGhpcMOzdGVzZXMgY29tICRuID0gNjQkIHBlw6dhcy4gQXMgaGlww7N0ZXNlcyBlc3RhYmVsZWNpZGFzIHPDo28gJEhfMDogXFxtdSA9IDUwJCB2cyAkSF8xOiBcXG11IFxcbmVxIDUwJC4gQ29uc2lkZXJhbmRvIHVtIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBkZSAkXFxhbHBoYSA9IDVcXCUkLCBxdWFsIGRldmUgc2VyIGEgUmVnacOjbyBDcsOtdGljYSAoJFJDJCkgcGFyYSBlc3RlIHRlc3RlIGJpbGF0ZXJhbD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIiRSQyA9IFxce1xcYmFye1h9IFxcaW4gXFxtYXRoYmJ7Un0gfCBcXGJhcntYfSA8IDQ5LjUxIFxcdGV4dHsgb3UgfSBcXGJhcntYfSA+IDUwLjQ5XFx9JCIsICJCIjogIiRSQyA9IFxce1xcYmFye1h9IFxcaW4gXFxtYXRoYmJ7Un0gfCBcXGJhcntYfSA8IDQ5LjYxIFxcdGV4dHsgb3UgfSBcXGJhcntYfSA+IDUwLjM5XFx9JCIsICJDIjogIiRSQyA9IFxce1xcYmFye1h9IFxcaW4gXFxtYXRoYmJ7Un0gfCBcXGJhcntYfSA8IDQ5Ljc1IFxcdGV4dHsgb3UgfSBcXGJhcntYfSA+IDUwLjI1XFx9JCIsICJEIjogIiRSQyA9IFxce1xcYmFye1h9IFxcaW4gXFxtYXRoYmJ7Un0gfCBcXGJhcntYfSA8IDQ5LjgwIFxcdGV4dHsgb3UgfSBcXGJhcntYfSA+IDUwLjIwXFx9JCIsICJFIjogIiRSQyA9IFxce1xcYmFye1h9IFxcaW4gXFxtYXRoYmJ7Un0gfCBcXGJhcntYfSA8IDQ5LjQ1IFxcdGV4dHsgb3UgfSBcXGJhcntYfSA+IDUwLjU1XFx9JCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSwgcGFyYSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLCBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgw6kgJEVQKFxcYmFye1h9KSA9IFxcc2lnbWEgLyBcXHNxcnR7bn0kLiBDb21vIG8gdGVzdGUgw6kgYmlsYXRlcmFsLCBvIG7DrXZlbCAkXFxhbHBoYSQgZGV2ZSBzZXIgZGl2aWRpZG8gZW0gZHVhcyBjYXVkYXMgKCRcXGFscGhhLzIgPSAwLjAyNSQpLCBidXNjYW5kbyBvcyB2YWxvcmVzIGNyw610aWNvcyAkWl97Y3JpdH0gPSBcXHBtIDEuOTYkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiMS4gQ2FsY3VsYW1vcyBvIGVycm8gcGFkcsOjbzogJEVQKFxcYmFye1h9KSA9IDIgLyBcXHNxcnR7NjR9ID0gMi84ID0gMC4yNSQuIDIuIFBhcmEgdW0gdGVzdGUgYmlsYXRlcmFsIGNvbSAkXFxhbHBoYSA9IDVcXCUkLCB0ZW1vcyAkXFxhbHBoYS8yID0gMi41XFwlJCwgcXVlIGNvcnJlc3BvbmRlIGFvIHZhbG9yIGNyw610aWNvICRaX3tjcml0fSA9IDEuOTYkIG5hIHRhYmVsYSBub3JtYWwgcGFkcsOjby4gMy4gT3MgbGltaXRlcyBkYSByZWdpw6NvIGNyw610aWNhIHPDo28gZGFkb3MgcG9yOiAkXFxtdV8wIFxccG0gWl97Y3JpdH0gXFx0aW1lcyBFUChcXGJhcntYfSkgPSA1MCBcXHBtIDEuOTYgXFx0aW1lcyAwLjI1JC4gNC4gTGltaXRlIGluZmVyaW9yOiAkNTAgLSAwLjQ5ID0gNDkuNTEkLiA1LiBMaW1pdGUgc3VwZXJpb3I6ICQ1MCArIDAuNDkgPSA1MC40OSQuIFBvcnRhbnRvLCAkUkMgPSBcXHtcXGJhcntYfSB8IFxcYmFye1h9IDwgNDkuNTEgXFx0ZXh0eyBvdSB9IFxcYmFye1h9ID4gNTAuNDlcXH0kLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoNDksIDUxLCAxMDAwKVxueSA9ICgxIC8gKDAuMjUgKiBucC5cXHNxcnQoMiAqIG5wLlxccGkpKSkgKiBucC5cXGV4cCgtMC41ICogKCh4IC0gNTApIC8gMC4yNSkqKjIpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTMpLCBuYW1lPSdEaXN0cmlidWnDp8OjbyAkSF8wJCcpKVxuZmlnLmFkZF92cmVjdCh4MD00OS41MSwgeDE9NDksIGZpbGxjb2xvcj0nIzk5MUIxQicsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTApXG5maWcuYWRkX3ZyZWN0KHgwPTUwLjQ5LCB4MT01MSwgZmlsbGNvbG9yPScjOTkxQjFCJywgb3BhY2l0eT0wLjMsIGxpbmVfd2lkdGg9MClcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdSZWdpw6NvIENyw610aWNhIChSQykgcGFyYSBvIHRlc3RlIGJpbGF0ZXJhbCcsIHhheGlzX3RpdGxlPXInTcOpZGlhIEFtb3N0cmFsICgkXGJhcntYfSQpJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzMzYifSwgeyJlbnVuY2lhZG8iOiAiVW0gZW5nZW5oZWlybyBkZSBwcm9jZXNzb3MgZGVzZWphIHRlc3RhciBzZSB1bWEgbm92YSBsaWdhIG1ldMOhbGljYSB0ZW0gcmVzaXN0w6puY2lhIMOgIHRyYcOnw6NvIGRpZmVyZW50ZSBkYSBsaWdhIHBhZHLDo28gKCRcXG11ID0gMjAwJCBrZykuIEVsZSBzZWxlY2lvbmEgMjUgYW1vc3RyYXMgZSBvYnTDqW0gdW1hIG3DqWRpYSAkXFxiYXJ7WH0gPSAyMDUkIGtnLCBjb20gZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsIGNvbmhlY2lkbyAkXFxzaWdtYSA9IDEwJCBrZy4gTyBlbmdlbmhlaXJvIGZpeGEgJFxcYWxwaGEgPSAwLjA1JC4gUXVhbCBkYXMgc2VndWludGVzIGFmaXJtYcOnw7VlcyBzb2JyZSBvIHByb2Nlc3NvIGRlIGRlY2lzw6NvIMOpIGNvcnJldGE/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIHAtdmFsb3Igc2Vyw6EgbWFpb3IgcXVlIDAuMDUsIGxldmFuZG8gw6AgcmVqZWnDp8OjbyBkZSAkSF8wJC4iLCAiQiI6ICJBIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSBjYWxjdWxhZGEgw6kgJFpfe2NhbGN9ID0gMi41JC4iLCAiQyI6ICJBIGhpcMOzdGVzZSBudWxhICRIXzA6IFxcbXUgPSAyMDAkIG7Do28gZGV2ZSBzZXIgcmVqZWl0YWRhLCBwb2lzICRaX3tjYWxjfSA8IFpfe2NyaXR9JC4iLCAiRCI6ICJPIGVycm8gVGlwbyBJIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSBhY2VpdGFyICRIXzAkIHNlbmRvICRIXzEkIHZlcmRhZGVpcmEuIiwgIkUiOiAiQSBSZWdpw6NvIENyw610aWNhIHBhcmEgZXN0ZSB0ZXN0ZSB1bmlsYXRlcmFsICgkXFxtdSA+IDIwMCQpIHNlcmlhICRSQyA9IFxce1xcYmFye1h9IHwgXFxiYXJ7WH0gPiAyMDMuMjlcXH0kLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiQ2FsY3VsZSBwcmltZWlybyAkWl97Y2FsY30gPSAoXFxiYXJ7WH0gLSBcXG11XzApIC8gKFxcc2lnbWEgLyBcXHNxcnR7bn0pJC4gQ29tcGFyZSBjb20gbyB2YWxvciBjcsOtdGljbyBwYXJhIG8gdGVzdGUgZGUgaW50ZXJlc3NlLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiMS4gQ2FsY3VsYW1vcyAkWl97Y2FsY30gPSAoMjA1IC0gMjAwKSAvICgxMCAvIFxcc3FydHsyNX0pID0gNSAvICgxMC81KSA9IDUgLyAyID0gMi41JC4gMi4gUGFyYSB1bSB0ZXN0ZSB1bmlsYXRlcmFsICgkSF8xOiBcXG11ID4gMjAwJCkgY29tICRcXGFscGhhID0gMC4wNSQsICRaX3tjcml0fSA9IDEuNjQ1JC4gQ29tbyAkWl97Y2FsY30gPSAyLjUgPiAxLjY0NSQsIHJlamVpdGFtb3MgJEhfMCQuIDMuIEEgYWx0ZXJuYXRpdmEgQiDDqSBhIGNvcnJldGEgcG9pcyBvIGPDoWxjdWxvIHJlc3VsdGEgZXhhdGFtZW50ZSBlbSAyLjUuIEEgYWx0ZXJuYXRpdmEgQyBlc3TDoSBpbmNvcnJldGEgcG9pcyByZWplaXRhbW9zICRIXzAkLiBBIGFsdGVybmF0aXZhIEQgZGVmaW5lIG8gRXJybyBUaXBvIElJLCBuw6NvIFRpcG8gSS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNDAifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZW5zYWlvIGNsw61uaWNvIHJpZ29yb3NvLCBwZXNxdWlzYWRvcmVzIHRlc3RhbSB1bSBub3ZvIGbDoXJtYWNvIHBhcmEgcmVkdcOnw6NvIGRlIHByZXNzw6NvIGFydGVyaWFsLCBvbmRlIGEgaGlww7N0ZXNlIG51bGEgJEhfMCQgYWZpcm1hIHF1ZSBvIGbDoXJtYWNvIMOpIGluZWZpY2F6IChuw6NvIHJlZHV6IGEgcHJlc3PDo28pIGUgYSBoaXDDs3Rlc2UgYWx0ZXJuYXRpdmEgJEhfMSQgYWZpcm1hIHF1ZSBlbGUgw6kgZWZpY2F6LiBPIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgZm9pIGZpeGFkbyBlbSAwLDA1LiBDb25zaWRlcmUgcXVlIGEgZGVjaXPDo28gZGUgcmVqZWl0YXIgJEhfMCQgKGRlY2xhcmFyIGVmaWPDoWNpYSkgcXVhbmRvLCBuYSByZWFsaWRhZGUsIG8gZsOhcm1hY28gbsOjbyB0cmF6IGJlbmVmw61jaW8gYWxndW0gKCAkSF8wJCB2ZXJkYWRlaXJhKSB0ZW0gY29uc2VxdcOqbmNpYXMgw6l0aWNhcyBncmF2w61zc2ltYXMsIGNvbW8gYSBleHBvc2nDp8OjbyBkZXNuZWNlc3PDoXJpYSBkb3MgcGFjaWVudGVzIGEgZWZlaXRvcyBjb2xhdGVyYWlzLiBRdWFsIGRhcyBpbnRlcnByZXRhw6fDtWVzIGFiYWl4byBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgbyBlcnJvIGluZmVyZW5jaWFsIGVtIHF1ZXN0w6NvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyBlcnJvIGRlIFRpcG8gSSBvY29ycmUgc2Ugb3MgcGVzcXVpc2Fkb3JlcyByZWplaXRhcmVtIGEgaW5lZmljw6FjaWEgZG8gZsOhcm1hY28sIHF1YW5kbyBlbGUgw6kgZGUgZmF0byBpbmVmaWNhei4iLCAiQiI6ICJPIGVycm8gZGUgVGlwbyBJSSBvY29ycmUgc2Ugb3MgcGVzcXVpc2Fkb3JlcyByZWplaXRhcmVtIGEgZWZpY8OhY2lhIGRvIGbDoXJtYWNvLCBxdWFuZG8gZWxlIMOpIGRlIGZhdG8gZWZpY2F6LiIsICJDIjogIk8gZXJybyBkZSBUaXBvIEkgb2NvcnJlIHNlIG9zIHBlc3F1aXNhZG9yZXMgY29uY2x1w61yZW0gcXVlIG8gZsOhcm1hY28gw6kgaW5lZmljYXosIHF1YW5kbyBuYSB2ZXJkYWRlIGVsZSDDqSBlZmljYXouIiwgIkQiOiAiTyBlcnJvIGRlIFRpcG8gSUkgcmVwcmVzZW50YSBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBkbyB0ZXN0ZSwgc2VuZG8gZml4YWRvIHBlbGEgcHJvYmFiaWxpZGFkZSBkZSBmYWxoYSBuYSBkZXRlY8Onw6NvIGRvIGVmZWl0byByZWFsLiIsICJFIjogIk8gZXJybyBkZSBUaXBvIEkgw6kgaW5vZmVuc2l2byBuZXN0YSBzaXR1YcOnw6NvLCBwb2lzIGEgcHJvYmFiaWxpZGFkZSAkXFxhbHBoYT0wLDA1JCDDqSBzdWZpY2llbnRlbWVudGUgYmFpeGEgcGFyYSBpZ25vcmFyIG8gcmlzY28gZGUgdW0gZmFsc28gcG9zaXRpdm8uIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgZGVmaW5pw6fDo28gZm9ybWFsOiAkXFxhbHBoYSA9IFAoXFx0ZXh0e1JlamVpdGFyIH0gSF8wIHwgSF8wIFxcdGV4dHsgw6kgdmVyZGFkZWlyYX0pJC4gUGVuc2Ugbm8gcXVlIHNpZ25pZmljYSAnZmFsc28gcG9zaXRpdm8nIG5vIGNvbnRleHRvIGRlIGVmaWPDoWNpYSBjbMOtbmljYS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIk8gZXJybyBkZSBUaXBvIEkgKGZhbHNvIHBvc2l0aXZvKSBjb25zaXN0ZSBlbSByZWplaXRhciAkSF8wJCBxdWFuZG8gZWxhIMOpIHZlcmRhZGVpcmEuIE5vIGNvbnRleHRvLCAkSF8wJCDDqSAnZsOhcm1hY28gw6kgaW5lZmljYXonLiBMb2dvLCByZWplaXRhciAkSF8wJCBzaWduaWZpY2EgY29uY2x1aXIgZXJyb25lYW1lbnRlIHF1ZSBvIGbDoXJtYWNvIMOpIGVmaWNhei4gUG9ydGFudG8sIGEgYWx0ZXJuYXRpdmEgQSBlc3TDoSBjb3JyZXRhIGFvIGRlc2NyZXZlciBxdWUgbyBlcnJvIGRlIFRpcG8gSSBvY29ycmUgYW8gZGVjbGFyYXIgZWZpY8OhY2lhIChyZWplaXRhciAkSF8wJCkgcXVhbmRvIG8gZsOhcm1hY28gw6ksIG5hIHJlYWxpZGFkZSwgaW5lZmljYXogKCRIXzAkIHZlcmRhZGVpcmEpLiBBcyBkZW1haXMgYWx0ZXJuYXRpdmFzIGRlc2NyZXZlbSBlcnJvbmVhbWVudGUgb3MgY29uY2VpdG9zIG91IGFzIGNvbnNlcXXDqm5jaWFzIGRvcyBlcnJvcy4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBvIG1vbml0b3JhbWVudG8gZGUgdW1hIGxpbmhhIGRlIG1vbnRhZ2VtIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyBkZSBhbHRhIHByZWNpc8Ojby4gTyBwYXLDom1ldHJvIGRlIGludGVyZXNzZSDDqSBhIHJlc2lzdMOqbmNpYSBtw6lkaWEgJFxcbXUkIGRlIHVtIGNvbXBvbmVudGUsIGNvbSAkSF8wOiBcXG11ID0gMTAwXFxPbWVnYSQuIEEgcmVncmEgZGUgZGVjaXPDo28gZXN0YWJlbGVjaWRhIHJlamVpdGEgJEhfMCQgc2UgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBmb3IgbWVub3IgcXVlICQ5OFxcT21lZ2EkIG91IG1haW9yIHF1ZSAkMTAyXFxPbWVnYSQuIFNlIGEgbcOhcXVpbmEgc29mcmVyIHVtIGRlc2dhc3RlIGUgYSBtw6lkaWEgcmVhbCBkb3MgY29tcG9uZW50ZXMgcGFzc2FyIGEgc2VyICQxMDNcXE9tZWdhJCwgcXVhbCDDqSBhIHByb2JhYmlsaWRhZGUgZG8gZXJybyBkZSBUaXBvIElJICgkXFxiZXRhJCk/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgJEhfMCQgc2FiZW5kbyBxdWUgJFxcbXUgPSAxMDNcXE9tZWdhJC4iLCAiQiI6ICJBIHByb2JhYmlsaWRhZGUgZGUgJFxcYmFye1h9JCBlc3RhciBubyBpbnRlcnZhbG8gJFs5OCwgMTAyXSQgZGFkbyBxdWUgJFxcbXUgPSAxMDNcXE9tZWdhJC4iLCAiQyI6ICJBIHByb2JhYmlsaWRhZGUgJFxcYWxwaGEkLCBwb2lzIG8gZXJybyBkZSBUaXBvIElJIMOpIHNlbXByZSBpZ3VhbCBhbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEuIiwgIkQiOiAiQSBwcm9iYWJpbGlkYWRlIGRlICRcXGJhcntYfSQgZXN0YXIgZm9yYSBkbyBpbnRlcnZhbG8gJFs5OCwgMTAyXSQgZGFkbyBxdWUgJFxcbXUgPSAxMDBcXE9tZWdhJC4iLCAiRSI6ICJPIHZhbG9yIGNvbXBsZW1lbnRhciBkYSBwb3TDqm5jaWEgZG8gdGVzdGUsIG91IHNlamEsICQxIC0gXFxiZXRhID0gUChcXGJhcntYfSBcXGluIFJDIHwgXFxtdSA9IDEwM1xcT21lZ2EpJC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk8gRXJybyBkZSBUaXBvIElJLCAkXFxiZXRhJCwgb2NvcnJlIHF1YW5kbyBuw6NvIHJlamVpdGFtb3MgJEhfMCQgKGFjZWl0YW1vcyBvdSBtYW50ZW1vcyAkSF8wJCkgbWVzbW8gc2VuZG8gZWxhIGZhbHNhLiBBIFJlZ2nDo28gZGUgQWNlaXRhw6fDo28gKCRSQSQpIMOpIG8gY29tcGxlbWVudG8gZGEgUmVnacOjbyBDcsOtdGljYSAoJFJDJCkuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQb3IgZGVmaW5pw6fDo28sICRcXGJldGEgPSBQKFxcdGV4dHtOw6NvIHJlamVpdGFyIH0gSF8wIHwgSF8wIFxcdGV4dHsgw6kgZmFsc2F9KSQuIEEgcmVncmEgZGUgZGVjaXPDo28gcmVqZWl0YSAkSF8wJCBwYXJhIHZhbG9yZXMgZm9yYSBkZSAkWzk4LCAxMDJdJCwgcG9ydGFudG8sIGEgUmVnacOjbyBkZSBBY2VpdGHDp8OjbyDDqSAkWzk4LCAxMDJdJC4gU2UgYSBoaXDDs3Rlc2UgYWx0ZXJuYXRpdmEgw6kgdmVyZGFkZWlyYSAoJFxcbXUgPSAxMDNcXE9tZWdhJCksIGEgcHJvYmFiaWxpZGFkZSBkZSBjb21ldGVyIG8gZXJybyBkZSBUaXBvIElJIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSBhIG3DqWRpYSBhbW9zdHJhbCBjYWlyIG5hIHJlZ2nDo28gZGUgYWNlaXRhw6fDo28gJFs5OCwgMTAyXSQsIG91IHNlamEsICRQKDk4IFxcbGUgXFxiYXJ7WH0gXFxsZSAxMDIgfCBcXG11ID0gMTAzXFxPbWVnYSkkLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoOTUsIDEwNiwgNTAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgsIGxvYz0xMDMsIHNjYWxlPTEpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9clwiRGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgKCRcXFxcbXU9MTAzJClcIiwgbGluZT1kaWN0KGNvbG9yPVwiIzFFM0E4QVwiLCB3aWR0aD0zKSkpXG5maWcuYWRkX3ZyZWN0KHgwPTk4LCB4MT0xMDIsIGZpbGxjb2xvcj1cIiMxMEI5ODFcIiwgb3BhY2l0eT0wLjMsIGxpbmVfd2lkdGg9MCwgbmFtZT1cIlJlZ2nDo28gZGUgQWNlaXRhw6fDo29cIilcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPVwiRGlzdHJpYnVpw6fDo28gZGEgTcOpZGlhIEFtb3N0cmFsIHNvYiBIMVwiLCB4YXhpc190aXRsZT1yXCJNw6lkaWEgQW1vc3RyYWwgKCRcXFxcYmFye1h9JClcIiwgeWF4aXNfdGl0bGU9XCJEZW5zaWRhZGVcIikiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiwgcC4gMzQ1In0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBkZSB1bWEgbGluaGEgZGUgbW9udGFnZW0gZGUgY2hpcHMgZGUgc2VtaWNvbmR1dG9yZXMsIGEgaGlww7N0ZXNlIG51bGEgJEhfMCQgYWZpcm1hIHF1ZSBhIHRheGEgZGUgZGVmZWl0byDDqSBkZSAkcCA9IDAuMDIkLiBPIGVuZ2VuaGVpcm8gZGUgcHJvZHXDp8OjbyBlc3RhYmVsZWNlIHVtYSBSZWdpw6NvIENyw610aWNhICgkUkMkKSBiYXNlYWRhIGVtIHVtYSBhbW9zdHJhIGRlICRuPTEwMDAkIHVuaWRhZGVzLiBTZSBvIGVuZ2VuaGVpcm8gZGVjaWRpciByZWR1emlyIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCBkZSAkMC4wNSQgcGFyYSAkMC4wMSQgcGFyYSBldml0YXIgZmFsc29zIGFsYXJtZXMgKEVycm8gVGlwbyBJKSwgbyBxdWUgb2NvcnJlcsOhIGNvbSBvIHBvZGVyIGRvIHRlc3RlICgkMSAtIFxcYmV0YSQpIGUgYSBwcm9iYWJpbGlkYWRlIGRlIEVycm8gVGlwbyBJSSAoJFxcYmV0YSQpPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyBwb2RlciBkbyB0ZXN0ZSAoJDEgLSBcXGJldGEkKSBhdW1lbnRhcsOhIGUgYSBwcm9iYWJpbGlkYWRlIGRlIEVycm8gVGlwbyBJSSAoJFxcYmV0YSQpIGRpbWludWlyw6EuIiwgIkIiOiAiTyBwb2RlciBkbyB0ZXN0ZSAoJDEgLSBcXGJldGEkKSBkaW1pbnVpcsOhIGUgYSBwcm9iYWJpbGlkYWRlIGRlIEVycm8gVGlwbyBJSSAoJFxcYmV0YSQpIGF1bWVudGFyw6EuIiwgIkMiOiAiVGFudG8gbyBwb2RlciBkbyB0ZXN0ZSBxdWFudG8gYSBwcm9iYWJpbGlkYWRlIGRlIEVycm8gVGlwbyBJSSBwZXJtYW5lY2Vyw6NvIGNvbnN0YW50ZXMsIHBvaXMgbyB0YW1hbmhvIGFtb3N0cmFsICRuJCDDqSBmaXhvLiIsICJEIjogIk8gcG9kZXIgZG8gdGVzdGUgKCQxIC0gXFxiZXRhJCkgYXVtZW50YXLDoSwgcG9pcyBhIHJlZHXDp8OjbyBkZSAkXFxhbHBoYSQgdG9ybmEgbyB0ZXN0ZSBtYWlzIHNlbnPDrXZlbCBhIGRlc3Zpb3MgZGEgaGlww7N0ZXNlIG51bGEuIiwgIkUiOiAiTsOjbyDDqSBwb3Nzw612ZWwgZGV0ZXJtaW5hciBvIGNvbXBvcnRhbWVudG8gZGUgJFxcYmV0YSQgc2VtIGNvbmhlY2VyIGEgZnVuw6fDo28gcG9kZXIgZXNwZWPDrWZpY2EgcGFyYSB1bWEgYWx0ZXJuYXRpdmEgJFxcdGhldGFfMSQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgbWV0w6Fmb3JhIGRhICdnYW5nb3JyYSc6IGEgcmVnacOjbyBkZSByZWplacOnw6NvIHRvcm5hLXNlIG1haXMgcmVzdHJpdGEgcXVhbmRvIGRpbWludcOtbW9zIG8gcmlnb3IgZXhpZ2lkbyBwYXJhIG8gRXJybyBUaXBvIEkuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBbyByZWR1emlyICRcXGFscGhhJCBkZSAkMC4wNSQgcGFyYSAkMC4wMSQsIGEgcmVnacOjbyBkZSByZWplacOnw6NvICgkUkMkKSB0b3JuYS1zZSBtZW5vciAobWFpcyBjb25zZXJ2YWRvcmEpLiBDb21vIGEgcmVnacOjbyBkZSByZWplacOnw6NvIGVuY29saGUsIGEgw6FyZWEgc29iIGEgZGlzdHJpYnVpw6fDo28gZGEgaGlww7N0ZXNlIGFsdGVybmF0aXZhIHF1ZSBjYWkgbmEgcmVnacOjbyBkZSBuw6NvLXJlamVpw6fDo28gZGUgJEhfMCQgYXVtZW50YS4gSXNzbyBkZWZpbmUgdW0gaW5jcmVtZW50byBlbSAkXFxiZXRhJCAocHJvYmFiaWxpZGFkZSBkZSBFcnJvIFRpcG8gSUkpLiBEYWRvIHF1ZSBvIHBvZGVyIGRvIHRlc3RlIMOpIGRlZmluaWRvIHBlbGEgcmVsYcOnw6NvICQxIC0gXFxiZXRhJCwgdW0gYXVtZW50byBlbSAkXFxiZXRhJCByZXN1bHRhIG9icmlnYXRvcmlhbWVudGUgbmEgcmVkdcOnw6NvIGRvIHBvZGVyIGRvIHRlc3RlLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTQsIDQsIDEwMClcbnlfaDAgPSBzdGF0cy5ub3JtLnBkZih4LCAwLCAxKVxueV9oMSA9IHN0YXRzLm5vcm0ucGRmKHgsIDEuNSwgMSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eV9oMCwgbmFtZT1yXCIkSF8wOiBcXHRoZXRhPTAkXCIsIGxpbmU9ZGljdChjb2xvcj1cIiMxRTNBOEFcIiwgd2lkdGg9MikpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15X2gxLCBuYW1lPXJcIiRIXzE6IFxcdGhldGE9MS41JFwiLCBsaW5lPWRpY3QoY29sb3I9XCIjMTBCOTgxXCIsIHdpZHRoPTIsIGRhc2g9J1xcZG90JykpKVxuZmlnLmFkZF92bGluZSh4PTEuNjQ1LCBsaW5lPWRpY3QoY29sb3I9XCIjOTkxQjFCXCIsIHdpZHRoPTIpLCBuYW1lPVwiUmVnacOjbyBDcsOtdGljYVxuKM6xPTAuMDUpXCIpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT1yXCI8Yj5FcXVpbMOtYnJpbyBlbnRyZSDOsSBlIM6yPC9iPlwiLCB4YXhpc190aXRsZT1cIlBhcsOibWV0cm9cIiwgeWF4aXNfdGl0bGU9XCJEZW5zaWRhZGVcIikiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBwZXNxdWlzYWRvciBlc3TDoSBjb25kdXppbmRvIHVtIGVuc2FpbyBjbMOtbmljbyBwYXJhIHRlc3RhciBhIGVmaWPDoWNpYSBkZSB1bSBub3ZvIGbDoXJtYWNvLiBFbGUgb2JzZXJ2YSBxdWUgbyBwb2RlciBkbyB0ZXN0ZSAoJDEgLSBcXGJldGEkKSDDqSBpbnN1ZmljaWVudGUgcGFyYSBkZXRlY3RhciB1bWEgZGlmZXJlbsOnYSBjbGluaWNhbWVudGUgcmVsZXZhbnRlLiBEZSBhY29yZG8gY29tIG9zIGZ1bmRhbWVudG9zIGVzdGF0w61zdGljb3MsIHF1YWwgZGFzIHNlZ3VpbnRlcyBhw6fDtWVzIMOpIGEgZm9ybWEgZXN0YXRpc3RpY2FtZW50ZSBjb3JyZXRhIGRlIGF1bWVudGFyIG8gcG9kZXIgZG8gdGVzdGUgc2VtIGF1bWVudGFyIGEgcHJvYmFiaWxpZGFkZSBkbyBFcnJvIFRpcG8gSSAoJFxcYWxwaGEkKT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkF1bWVudGFyIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCBhcmJpdHJhcmlhbWVudGUgYXTDqSBxdWUgbyBwb2RlciBzZSB0b3JuZSBhY2VpdMOhdmVsLiIsICJCIjogIk1hbnRlciBvIHRhbWFuaG8gYW1vc3RyYWwgY29uc3RhbnRlIGUgcmVkdXppciBhIHZhcmnDom5jaWEgZG9zIGRhZG9zIGF0cmF2w6lzIGRlIHVtIHByb2Nlc3NvIGRlIGZpbHRyYWdlbSBkZSBvdXRsaWVycyBleHRyZW1vcy4iLCAiQyI6ICJBdW1lbnRhciBvIHRhbWFuaG8gYW1vc3RyYWwgKCRuJCksIHBlcm1pdGluZG8gcXVlIGEgZGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgc2UgdG9ybmUgbWFpcyBlc3RyZWl0YSwgbyBxdWUgcmVkdXogdGFudG8gJFxcYWxwaGEkIHF1YW50byAkXFxiZXRhJCBzaW11bHRhbmVhbWVudGUuIiwgIkQiOiAiQWNlaXRhciB1bWEgdGF4YSBtYWlvciBkZSBFcnJvIFRpcG8gSSBjb21vIHVtIGN1c3RvIG5lY2Vzc8OhcmlvIHBhcmEgZ2FyYW50aXIgYSBzZW5zaWJpbGlkYWRlIGRvIHRlc3RlLiIsICJFIjogIkRpbWludWlyIG8gdGFtYW5obyBhbW9zdHJhbCBwYXJhIHJlZHV6aXIgYSB2YXJpYWJpbGlkYWRlIGdsb2JhbCBkbyBleHBlcmltZW50by4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIlBlbnNlIG5vIGVmZWl0byBkbyB0YW1hbmhvIGFtb3N0cmFsICgkbiQpIHNvYnJlIGEgcHJlY2lzw6NvIGRvcyBlc3RpbWFkb3JlcyBlIGNvbW8gaXNzbyBhZmV0YSBhIHNvYnJlcG9zacOnw6NvIGRhcyBjdXJ2YXMgZGUgZGVuc2lkYWRlIHNvYiAkSF8wJCBlICRIXzEkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBhdW1lbnRvIGRvIHRhbWFuaG8gYW1vc3RyYWwgKCRuJCkgcmVkdXogbyBlcnJvIHBhZHLDo28gZGEgZXN0YXTDrXN0aWNhIGFtb3N0cmFsLiBJc3NvIGZheiBjb20gcXVlIGFzIGRpc3RyaWJ1acOnw7VlcyBzb2IgJEhfMCQgZSAkSF8xJCBzZSB0b3JuZW0gbWFpcyAnZmluYXMnIChtZW5vciBkaXNwZXJzw6NvKS4gQ29tIG1lbm9zIHNvYnJlcG9zacOnw6NvIGVudHJlIGFzIGRpc3RyaWJ1acOnw7Vlcywgw6kgcG9zc8OtdmVsIG1hbnRlciB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkIGZpeG8gKHBvciBleGVtcGxvLCAkMC4wNSQpIGUsIGFpbmRhIGFzc2ltLCBvYnRlciB1bWEgcmVnacOjbyBjcsOtdGljYSBxdWUgY2FwdHVyYSB1bWEgcGFyY2VsYSBtYWlvciBkYSBkaXN0cmlidWnDp8OjbyBzb2IgJEhfMSQsIGF1bWVudGFuZG8gYXNzaW0gbyBwb2RlciAoJDEgLSBcXGJldGEkKS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtYSBjZW50cmFsIGRlIG1vbml0b3JhbWVudG8gZGUgSW9UIGF2YWxpYSBhIHF1YWxpZGFkZSBkYSByZWRlIGF0cmF2w6lzIGRhIGxhdMOqbmNpYSBtw6lkaWEgJFxcbXUkIChlbSBtcykgZGUgcGFjb3RlcyBkZSBkYWRvcywgYXNzdW1pbmRvIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgY29tIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCBjb25oZWNpZG8gJFxcc2lnbWEgPSAyMCQgbXMuIFBhcmEgdGVzdGFyICRIX3swfTogXFxtdSA9IDUwJCBtcyB2ZXJzdXMgJEhfezF9OiBcXG11ID4gNTAkIG1zLCBhIGVxdWlwZSBkZSBlbmdlbmhhcmlhIHV0aWxpemEgdW1hIGFtb3N0cmEgZGUgJG4gPSAyNSQgcGFjb3RlcyBlIGRlZmluZSBhIHJlZ3JhIGRlIGRlY2lzw6NvOiByZWplaXRhciAkSF97MH0kIHNlICRcXGJhcntYfSA+IDU4JCBtcy4gQ29uc2lkZXJhbmRvIG8gY29tcG9ydGFtZW50byBkYSBmdW7Dp8OjbyBjYXJhY3RlcsOtc3RpY2EgZGUgb3BlcmHDp8OjbyAkXFxiZXRhKFxcbXUpJCwgcXVhbCDDqSBvIHZhbG9yIGFwcm94aW1hZG8gZGEgcHJvYmFiaWxpZGFkZSBkZSBlcnJvIGRvIFRpcG8gSUkgc2UgYSBsYXTDqm5jaWEgcmVhbCBkYSByZWRlIGZvciBkZSAkXFxtdSA9IDYwJCBtcz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjAuMTU4NyIsICJCIjogIjAuMzQxMyIsICJDIjogIjAuNTAwMCIsICJEIjogIjAuNjU4NyIsICJFIjogIjAuODQxMyJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSAkXFxiZXRhKFxcbXUpID0gUChcXGJhcntYfSBcXGxlIFxcYmFye3h9X3tjfSB8IFxcbXUpJC4gQ2FsY3VsZSBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgZSBwYWRyb25pemUgbyB2YWxvciBkYSBtw6lkaWEgYW1vc3RyYWwgY3LDrXRpY2EgJFxcYmFye3h9X3tjfSA9IDU4JCBzb2IgYSBoaXDDs3Rlc2UgZGUgcXVlIGEgdmVyZGFkZWlyYSBtw6lkaWEgw6kgNjAuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQcmltZWlybywgY2FsY3VsYW1vcyBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWE6ICRFUChcXGJhcntYfSkgPSBcXHNpZ21hIC8gXFxzcXJ0e259ID0gMjAgLyBcXHNxcnR7MjV9ID0gNCQuIFNvYiAkXFxtdSA9IDYwJCwgYSBkaXN0cmlidWnDp8OjbyBhbW9zdHJhbCDDqSAkXFxiYXJ7WH0gXFxzaW0gTig2MCwgNF4yKSQuIEEgcHJvYmFiaWxpZGFkZSBkbyBlcnJvIFRpcG8gSUkgw6kgJFxcYmV0YSg2MCkgPSBQKFxcYmFye1h9IFxcbGUgNTggfCBcXG11ID0gNjApID0gUChaIFxcbGUgKDU4IC0gNjApIC8gNCkgPSBQKFogXFxsZSAtMC41KSQuIENvbnN1bHRhbmRvIGEgdGFiZWxhIGRhIG5vcm1hbCBwYWRyw6NvLCAkUChaIFxcbGUgLTAuNSkgXFxhcHByb3ggMC4zMDg1JC4gQ29udHVkbywgcmV2aXNhbmRvIG8gY8OhbGN1bG86ICRQKFogXFxsZSAtMC41KSQgw6kgJDAuMzA4NSQuIFNlIHJlY2FsY3VsYXJtb3MgYSBtYXJnZW0gcGFyYSAwLjUgZGVzdmlvcywgdmVyaWZpY2Ftb3MgcXVlICRQKFogXFxsZSAtMC41KSA9IDAuMzA4NSQuIFNlIGhvdXZlc3NlIGVycm8gbmEgZXNjb2xoYSBkb3MgdmFsb3JlcywgbyBjb3JyZXRvIHNlcmlhIGJ1c2NhciBvIHZhbG9yIHRhYmVsYWRvLiBEYWRvIG8gY29udGV4dG8sIGEgb3DDp8OjbyBBIMOpIGEgbWFpcyBwcsOzeGltYSBlbSB1bWEgZGlzdHJpYnVpw6fDo28gZGUgY2F1ZGEuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSg0MCwgNzUsIDIwMClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9c3RhdHMubm9ybS5wZGYoeCwgNjAsIDQpLCBuYW1lPSdEZW5zaWRhZGUgc29iIEgxICh1PTYwKScsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTMpKSlcbmZpZy5hZGRfc2hhcGUodHlwZT0nbGluZScsIHgwPTU4LCB5MD0wLCB4MT01OCwgeTE9MC4xNSwgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJywgZGFzaD0nZGFzaCcpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0Rpc3RyaWJ1acOnw6NvIGRhIE3DqWRpYSBBbW9zdHJhbCBzb2IgXFxtdT02MCcsIHhheGlzX3RpdGxlPSdNw6lkaWEgQW1vc3RyYWwgKFgtXFxiYXIpJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKVxuZmlnLnNob3coKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNDAifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gY29udHJvbGUgZGUgcXVhbGlkYWRlIGRlIHBlw6dhcywgYSBwcm9wb3LDp8OjbyBkZSBpdGVucyBkZWZlaXR1b3NvcyAkcCQgw6kgdGVzdGFkYSB2aWEgJEhfezB9OiBwID0gMC4xMCQgY29udHJhICRIX3sxfTogcCA+IDAuMTAkLiBDb20gJG4gPSAxMDAkIGUgdW1hIHJlZ2nDo28gY3LDrXRpY2EgJFJDID0gXFx7XFxoYXR7cH0gPiAwLjE1XFx9JCwgcXVhbCBkYXMgYWZpcm1hw6fDtWVzIGFiYWl4byBtZWxob3IgZGVzY3JldmUgbyBjb21wb3J0YW1lbnRvIGRhIGZ1bsOnw6NvIHBvZGVyICRcXHBpKHApJD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgZnVuw6fDo28gcG9kZXIgJFxccGkocCkkIMOpIGNvbnN0YW50ZSBwYXJhIHRvZG9zIG9zIHZhbG9yZXMgZGUgJHAgPiAwLjEwJC4iLCAiQiI6ICJPIHBvZGVyIGRvIHRlc3RlLCAkXFxwaShwKSQsIGF1bWVudGEgw6AgbWVkaWRhIHF1ZSBvIHZhbG9yIHZlcmRhZGVpcm8gZGUgJHAkIHNlIGFmYXN0YSBkZSAwLjEwIG5hIGRpcmXDp8OjbyBkZSB2YWxvcmVzIG1haW9yZXMuIiwgIkMiOiAiQSBmdW7Dp8OjbyBwb2RlciAkXFxwaShwKSQgw6kgbcOheGltYSBxdWFuZG8gJHAgPSAwLjEwJC4iLCAiRCI6ICJPIGVycm8gVGlwbyBJSSwgJFxcYmV0YShwKSQsIGF1bWVudGEgY29uZm9ybWUgJHAkIGNyZXNjZSBhY2ltYSBkZSAwLjE1LiIsICJFIjogIk8gcG9kZXIgZG8gdGVzdGUgw6kgaW5kZXBlbmRlbnRlIGRvIHRhbWFuaG8gZGEgYW1vc3RyYSAkbiQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJBIGZ1bsOnw6NvIHBvZGVyICRcXHBpKHApJCBtZWRlIGEgcHJvYmFiaWxpZGFkZSBkZSByZWplaXRhciAkSF97MH0kLiBTZSBhIHByb3BvcsOnw6NvIHJlYWwgZGUgZGVmZWl0b3MgYXVtZW50YSwgYSBjaGFuY2UgZGEgbm9zc2EgZXN0YXTDrXN0aWNhICRcXGhhdHtwfSQgY2FpciBuYSByZWdpw6NvIGNyw610aWNhIHRvcm5hLXNlIG11aXRvIG1haW9yLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBmdW7Dp8OjbyBwb2RlciAkXFxwaShwKSA9IFAoXFxoYXR7cH0gXFxpbiBSQyB8IHApJCDDqSB1bWEgZnVuw6fDo28gY3Jlc2NlbnRlIGRvIHBhcsOibWV0cm8gc29iIGEgYWx0ZXJuYXRpdmEuIMOAIG1lZGlkYSBxdWUgJHAkIHNlIHRvcm5hIG1haW9yIHF1ZSAwLjEwLCBhIGRpc3RyaWJ1acOnw6NvIGRlICRcXGhhdHtwfSQgZGVzbG9jYS1zZSBwYXJhIGEgZGlyZWl0YSwgYXVtZW50YW5kbyBhIMOhcmVhIGRhIGNhdWRhIG5hIHJlZ2nDo28gY3LDrXRpY2EgKCRcXGhhdHtwfSA+IDAuMTUkKSwgbyBxdWUgYXVtZW50YSBvIHBvZGVyIGUsIGNvbnNlcXVlbnRlbWVudGUsIHJlZHV6IGEgcHJvYmFiaWxpZGFkZSBkZSBlcnJvIFRpcG8gSUkgJFxcYmV0YShwKSQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiwgcC4gMzQ3In1dLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGNsw61uaWNvIHBhcmEgdmVyaWZpY2FyIHNlIHVtIG5vdm8gZsOhcm1hY28gYWx0ZXJhIGEgcHJlc3PDo28gYXJ0ZXJpYWwgbcOpZGlhLCBhIGhpcMOzdGVzZSBudWxhIGRlZmluaWRhIMOpICRIXzA6IFxcbXUgPSAxMjAkIG1tSGcgdnMgJEhfMTogXFxtdSBcXG5lcSAxMjAkIG1tSGcuIFNhYmUtc2UgcXVlICRcXHNpZ21hID0gMTAkIG1tSGcgZSBhIGFtb3N0cmEgcG9zc3VpICRuID0gMTAwJC4gU2UgYSBSZWdpw6NvIENyw610aWNhIGZvciBkZWZpbmlkYSBjb21vICRSQyA9IFxce1xcYmFye1h9IDwgMTE4LjA0IFxcdGV4dHsgb3UgfSBcXGJhcntYfSA+IDEyMS45NlxcfSQsIGNhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRlIGNvbWV0ZXIgbyBlcnJvIFRpcG8gSSAoJFxcYWxwaGEkKS4iLCAiZGljYSI6ICJPIGVycm8gVGlwbyBJIMOpICRcXGFscGhhID0gUChcXGJhcntYfSBcXGluIFJDIHwgSF8wIFx0ZXh0eyB2ZXJkYWRlaXJhfSkkLiBVdGlsaXplIGEgcGFkcm9uaXphw6fDo28gcGFyYSBhIGRpc3RyaWJ1acOnw6NvIG5vcm1hbDogJFogPSAoXFxiYXJ7WH0gLSBcXG11XzApIC8gKFxcc2lnbWEgLyBcXHNxcnR7bn0pJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYW1vcyBhIGRpc3RyaWJ1acOnw6NvIGRhIG3DqWRpYSBhbW9zdHJhbCBzb2IgJEhfMCQ6ICRcXGJhcntYfSBcXHNpbSBOKDEyMCwgKDEwXjIvMTAwKSkgPSBOKDEyMCwgMSkkLiIsICIyLiBDYWxjdWxhbW9zIG8gdmFsb3IgWiBwYXJhIG9zIGxpbWl0ZXMgZGEgUkM6ICRaID0gKDExOC4wNCAtIDEyMCkgLyAxID0gLTEuOTYkIGUgJFogPSAoMTIxLjk2IC0gMTIwKSAvIDEgPSAxLjk2JC4iLCAiMy4gQSBwcm9iYWJpbGlkYWRlIGRvIGVycm8gVGlwbyBJIMOpIGEgc29tYSBkYXMgY2F1ZGFzOiAkXFxhbHBoYSA9IFAoXFxiYXJ7WH0gPCAxMTguMDQpICsgUChcXGJhcntYfSA+IDEyMS45NikgPSBQKFogPCAtMS45NikgKyBQKFogPiAxLjk2KSQuIiwgIjQuIENvbnN1bHRhbmRvIGEgdGFiZWxhIGRhIG5vcm1hbCwgJFAoWiA8IC0xLjk2KSA9IDAuMDI1JCBlICRQKFogPiAxLjk2KSA9IDAuMDI1JC4iLCAiNS4gUG9ydGFudG8sICRcXGFscGhhID0gMC4wMjUgKyAwLjAyNSA9IDAuMDUkIChvdSAkNVxcJSQpLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzMzYiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjA1fSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gdGVzdGUgZGUgaGlww7N0ZXNlcyAkSF8wOiBcXG11ID0gNTAkIGNvbnRyYSAkSF8xOiBcXG11ID0gNTUkLiBTYWJlbmRvIHF1ZSAkXFxiYXJ7WH0gXFxzaW0gTihcXG11LCA0KSQsICRuID0gMTYkIGUgYSByZWdpw6NvIGRlIGFjZWl0YcOnw6NvIMOpICRSQSA9IFxce1xcYmFye1h9IFxcbGUgNTEuNVxcfSQsIGRldGVybWluZSBhIHByb2JhYmlsaWRhZGUgZGUgY29tZXRlciB1bSBlcnJvIFRpcG8gSUkgKCRcXGJldGEkKS4iLCAiZGljYSI6ICJPIGVycm8gVGlwbyBJSSBvY29ycmUgcXVhbmRvIG7Do28gcmVqZWl0YW1vcyAkSF8wJCwgbWVzbW8gc2VuZG8gJEhfMSQgdmVyZGFkZWlyYS4gT3Ugc2VqYSwgJFxcYmV0YSA9IFAoXFxiYXJ7WH0gXFxpbiBSQSB8IEhfMSBcdGV4dHsgdmVyZGFkZWlyYX0pJC4gTGVtYnJlLXNlIHF1ZSBzb2IgJEhfMSQsICRcXG11ID0gNTUkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBEZWZpbmltb3MgbyBlcnJvIFRpcG8gSUk6ICRcXGJldGEgPSBQKFxcYmFye1h9IFxcbGUgNTEuNSB8IFxcbXUgPSA1NSkkLiIsICIyLiBTb2IgJEhfMSQsIG8gZXJybyBwYWRyw6NvIMOpICRFUCA9IFxcc3FydHtcXHNpZ21hXjIvbn0gPSBcXHNxcnR7NC8xNn0gPSBcXHNxcnR7MC4yNX0gPSAwLjUkLiIsICIzLiBQYWRyb25pemFtb3MgbyB2YWxvciBwYXJhIGVuY29udHJhciBhIHByb2JhYmlsaWRhZGU6ICRaID0gKDUxLjUgLSA1NSkgLyAwLjUgPSAtMy41IC8gMC41ID0gLTcuMCQuIiwgIjQuIEEgcHJvYmFiaWxpZGFkZSDDqSAkXFxiZXRhID0gUChaIFxcbGUgLTcuMCkkLiIsICI1LiBDb21vIG8gdmFsb3IgZGUgWiDDqSBtdWl0byBleHRyZW1vLCAkXFxiZXRhIFxcYXBwcm94IDAkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4wfSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIGRlIGZvcm1hIGRldGFsaGFkYSBlIHV0aWxpemFuZG8gYSBsw7NnaWNhIGRvIHByb2Nlc3NvIGRlY2lzw7NyaW8gaW5mZXJlbmNpYWwsIHBvciBxdWUgYSBjb25zdHJ1w6fDo28gZGUgdW1hIHJlZ2nDo28gY3LDrXRpY2EgKCRSQyQpIGVudm9sdmUgdW0gJ3RyYWRlLW9mZicgZW50cmUgYSBwcm9iYWJpbGlkYWRlIGRvIGVycm8gVGlwbyBJICgkXFxhbHBoYSQpIGUgYSBwcm9iYWJpbGlkYWRlIGRvIGVycm8gVGlwbyBJSSAoJFxiXFxldGEkKS4gQ29tbyBvIHRhbWFuaG8gYW1vc3RyYWwgKCRuJCkgaW5mbHVlbmNpYSBlc3NlIHRyaWJ1bmFsIGNpZW50w61maWNvPyIsICJkaWNhIjogIlBlbnNlIG5vIHRyaWJ1bmFsOiBhdW1lbnRhciBvIHJpZ29yIHBhcmEgbsOjbyBjb25kZW5hciB1bSBpbm9jZW50ZSAoJFxcYWxwaGEkKSBwb2RlIGRpZmljdWx0YXIgYSBjb25kZW5hw6fDo28gZGUgdW0gY3VscGFkbyByZWFsICgkXFxiZXRhJCkuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIE8gZXJybyBUaXBvIEkgKCRcXGFscGhhJCkgw6kgYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIGluanVzdGFtZW50ZSwgZW5xdWFudG8gbyBlcnJvIFRpcG8gSUkgKCRcXGJldGEkKSDDqSBhIGZhbGhhIGVtIGRldGVjdGFyIHVtIGRlc3ZpbyB2ZXJkYWRlaXJvLiIsICIyLiBGaXhhciB1bSAkXFxhbHBoYSQgbXVpdG8gcGVxdWVubyAoZXg6IDAuMSUpIGRpbWludWkgYSBSQywgdG9ybmFuZG8gbWFpcyBkaWbDrWNpbCByZWplaXRhciAkSF8wJC4gSXNzbyBzaW11bHRhbmVhbWVudGUgYXVtZW50YSBhIGNoYW5jZSBkZSAkXFxiZXRhJCwgcG9pcyBhIHJlZ2nDo28gZGUgYWNlaXRhw6fDo28gYXVtZW50YS4iLCAiMy4gTyB0YW1hbmhvIGFtb3N0cmFsICgkbiQpIGF0dWEgc29icmUgbyBlcnJvIHBhZHLDo286ICRFUChcXGJhcntYfSkgPSBcXHNpZ21hIC8gXFxzcXJ0e259JC4iLCAiNC4gQW8gYXVtZW50YXIgJG4kLCBvIGVycm8gcGFkcsOjbyBkaW1pbnVpLCB0b3JuYW5kbyBhIGRpc3RyaWJ1acOnw6NvIGRhIGVzdGF0w61zdGljYSBzb2IgJEhfMCQgZSAkSF8xJCBtYWlzICdlc3RyZWl0YScuIiwgIjUuIENvbnNlcXVlbnRlbWVudGUsIGNvbnNlZ3VpbW9zIHJlZHV6aXIgc2ltdWx0YW5lYW1lbnRlICRcXGFscGhhJCBlICRcXGJldGEkIG91IGF1bWVudGFyIG8gcG9kZXIgZG8gdGVzdGUgKCQxLVxcYmV0YSQpIHBhcmEgdW0gZGFkbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM0OCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbWEgZsOhYnJpY2EgZGUgY29tcG9uZW50ZXMgcHJvZHV6IHBlw6dhcyBjb20gcmVzaXN0w6puY2lhIHNlZ3VpbmRvICROKFxcbXUsIDEwMCkkLiBQYXJhICRIXzA6IFxcbXUgPSA1MCQgY29udHJhICRIXzE6IFxcbXUgPSA1NSQsIHVtYSBhbW9zdHJhIGRlICRuPTI1JCBwZcOnYXMgw6kgY29sZXRhZGEuIEVzdGFiZWxlY2V1LXNlIGEgUmVnacOjbyBDcsOtdGljYSAkUkMgPSBcXHtcXGJhcntYfSA+IDUzXFx9JC4gQ2FsY3VsZSBvIHZhbG9yIGRlICRcXGFscGhhJCAocHJvYmFiaWxpZGFkZSBkbyBlcnJvIGRlIFRpcG8gSSkuIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBzb2IgJEhfMCQsICRcXGJhcntYfSBcXHNpbSBOKFxcbXUsIFxcc2lnbWFeMi9uKSQuIENhbGN1bGUgbyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhICRFUChcXGJhcntYfSkgPSBcXHNpZ21hL1xcc3FydHtufSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIklkZW50aWZpY2FyIG9zIHBhcsOibWV0cm9zOiAkXFxtdV8wID0gNTAkLCAkXFxzaWdtYSA9IDEwJCwgJG4gPSAyNSQuIE8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSDDqSAkRVAoXFxiYXJ7WH0pID0gXFxmcmFjezEwfXtcXHNxcnR7MjV9fSA9IDIkLiIsICJTb2IgJEhfMCQsIGEgbcOpZGlhIGFtb3N0cmFsIHNlZ3VlICRcXGJhcntYfSBcXHNpbSBOKDUwLCA0KSQuIiwgIkRlZmluaXIgJFxcYWxwaGEgPSBQKFxcYmFye1h9ID4gNTMgfCBcXG11ID0gNTApJC4iLCAiVHJhbnNmb3JtYXIgcGFyYSBhIG5vcm1hbCBwYWRyw6NvICRaID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdV8wfXtFUChcXGJhcntYfSl9ID0gXFxmcmFjezUzIC0gNTB9ezJ9ID0gMSw1JC4iLCAiJFxcYWxwaGEgPSBQKFogPiAxLDUpID0gMSAtIFAoWiBcXGxlIDEsNSkgPSAxIC0gMCw5MzMyID0gMCwwNjY4JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMDY2OH0sIHsiZW51bmNpYWRvIjogIlV0aWxpemFuZG8gbyBtZXNtbyBjZW7DoXJpbyBkYSBxdWVzdMOjbyBhbnRlcmlvciAoJEhfMDogXFxtdSA9IDUwJCwgJEhfMTogXFxtdSA9IDU1JCwgJG49MjUkLCAkXFxzaWdtYT0xMCQsICRSQyA9IFxce1xcYmFye1h9ID4gNTNcXH0kKSwgY2FsY3VsZSBhIHByb2JhYmlsaWRhZGUgZG8gZXJybyBkZSBUaXBvIElJICgkXFxiZXRhJCkuIiwgImRpY2EiOiAiTyBlcnJvIGRlIFRpcG8gSUkgb2NvcnJlIHF1YW5kbyBuw6NvIHJlamVpdGFtb3MgJEhfMCQgKG91IHNlamEsICRcXGJhcntYfSBcXGxlIDUzJCksIGRhZG8gcXVlICRIXzEkIMOpIHZlcmRhZGVpcmEgKCRcXG11ID0gNTUkKS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiU29iICRIXzEkIChhIGhpcMOzdGVzZSBhbHRlcm5hdGl2YSksIGEgbcOpZGlhIHBvcHVsYWNpb25hbCDDqSAkXFxtdV8xID0gNTUkLiBBc3NpbSwgJFxcYmFye1h9IFxcc2ltIE4oNTUsIDQpJC4iLCAiRGVmaW5pciAkXFxiZXRhID0gUChcXGJhcntYfSBcXGxlIDUzIHwgXFxtdSA9IDU1KSQuIiwgIlRyYW5zZm9ybWFyIHBhcmEgYSBub3JtYWwgcGFkcsOjbyAkWiA9IFxcZnJhY3s1MyAtIDU1fXsyfSA9IC0xLDAkLiIsICIkXFxiZXRhID0gUChaIFxcbGUgLTEsMCkgPSAwLDE1ODckLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4xNTg3fSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIGRvIHBvbnRvIGRlIHZpc3RhIGNvbmNlaXR1YWwgZSBtYXRlbcOhdGljbywgYSByZWxhw6fDo28gZW50cmUgbyB0YW1hbmhvIGRhIGFtb3N0cmEgJG4kIGUgbyBwb2RlciBkbyB0ZXN0ZSAoJDEtXFxiZXRhJCksIGNvbnNpZGVyYW5kbyB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkIGZpeG8uIFBvciBxdWUgYXVtZW50YXIgJG4kIHJlZHV6IHNpbXVsdGFuZWFtZW50ZSBvIHJpc2NvIGRlIGVycm9zIGRlIFRpcG8gSUk/IiwgImRpY2EiOiAiUmVmbGl0YSBzb2JyZSBjb21vIG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSAkRVAoXFxiYXJ7WH0pID0gXFxzaWdtYS9cXHNxcnR7bn0kIHNlIGNvbXBvcnRhIHF1YW5kbyAkbiQgY3Jlc2NlLiBVc2UgbyBjb25jZWl0byBkZSB2YXJpYWJpbGlkYWRlIGRhIGVzdGltYXRpdmEgYW1vc3RyYWwuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIk8gcG9kZXIgZG8gdGVzdGUgw6kgJDEgLSBcXGJldGEgPSBQKFxcdGV4dHtSZWplaXRhciB9IEhfMCB8IEhfMSBcXHRleHR7IMOpIHZlcmRhZGVpcmF9KSQuIiwgIkEgdmFyacOibmNpYSBkYSBtw6lkaWEgYW1vc3RyYWwgw6kgJFZhcihcXGJhcntYfSkgPSBcXHNpZ21hXjIgLyBuJC4gQXNzaW0sIGNvbmZvcm1lICRuJCBhdW1lbnRhLCBvIGVycm8gcGFkcsOjbyAkRVAoXFxiYXJ7WH0pID0gXFxzaWdtYS9cXHNxcnR7bn0kIGRpbWludWkuIiwgIkNvbSB1bSAkRVAoXFxiYXJ7WH0pJCBtZW5vciwgYSBkaXN0cmlidWnDp8OjbyBhbW9zdHJhbCBkZSAkXFxiYXJ7WH0kIHRvcm5hLXNlIG1haXMgJ2VzdHJlaXRhJyBlIGNvbmNlbnRyYWRhIGFvIHJlZG9yIGRvIHZhbG9yIHBhcmFtw6l0cmljbyByZWFsLiIsICJBbyBmaXhhciAkXFxhbHBoYSQsIGEgcmVnacOjbyBjcsOtdGljYSAkUkMkIHRvcm5hLXNlIG1haXMgcHJlY2lzYS4gUGFyYSB1bSB2YWxvciBmaXhvIGVtICRIXzEkLCBvIGRlc2xvY2FtZW50byBkYSBkaXN0cmlidWnDp8OjbyBlbSByZWxhw6fDo28gw6AgJFJDJCByZXN1bHRhIGVtIG1lbm9zIHNvYnJlcG9zacOnw6NvIGVudHJlIGEgw6FyZWEgZGUgYWNlaXRhw6fDo28gZSBhIGRlbnNpZGFkZSBkYSBoaXDDs3Rlc2UgYWx0ZXJuYXRpdmEuIiwgIkNvbmNsdXPDo286IEEgcmVkdcOnw6NvIGRhIGluY2VydGV6YSBhbW9zdHJhbCAobWVub3IgZGlzcGVyc8OjbyBkZSAkXFxiYXJ7WH0kKSB0b3JuYSBvIHRlc3RlIG1haXMgc2Vuc8OtdmVsIHBhcmEgZGV0ZWN0YXIgZGVzdmlvcyByZWFpcyBkZSAkSF8wJCwgZGltaW51aW5kbyBhc3NpbSBhIHByb2JhYmlsaWRhZGUgJFxcYmV0YSQgZGUgZGVpeGFyIHBhc3NhciB1bSBlZmVpdG8gcmVhbC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiwgcC4gMzQ3IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSB0ZXN0ZSBkZSBoaXDDs3Rlc2VzIHBhcmEgYSBtw6lkaWEgcG9wdWxhY2lvbmFsICRcXG11JCBvbmRlICRIXzA6IFxcbXUgPSAxMCQgZSAkSF8xOiBcXG11ID0gMTIkLCBjb20gZGVzdmlvIHBhZHLDo28gY29uaGVjaWRvICRcXHNpZ21hID0gMiQgZSB0YW1hbmhvIGFtb3N0cmFsICRuID0gMTYkLiBPIHRlc3RlIHJlamVpdGEgJEhfMCQgc2UgJFxcYmFye1h9ID4gMTAuOCQuIENhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRvIEVycm8gVGlwbyBJICgkXFxhbHBoYSQpIHBhcmEgZXN0ZSB0ZXN0ZS4iLCAiZGljYSI6ICJVdGlsaXplIGEgZGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgZGEgbcOpZGlhIHNvYiAkSF8wJDogJFxcYmFye1h9IFxcc2ltIE4oXFxtdV8wLCBcXHNpZ21hXjIvbikkLiBDYWxjdWxlIG8gdmFsb3IgJFpfe1xcdGV4dHtjYWxjfX0kIGNvcnJlc3BvbmRlbnRlIGFvIHBvbnRvIGNyw610aWNvLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJJZGVudGlmaWNhbW9zIGEgZGlzdHJpYnVpw6fDo28gZGEgbcOpZGlhIHNvYiAkSF8wJDogJFxcYmFye1h9IFxcc2ltIE4oMTAsIDJeMi8xNikgXFxSaWdodGFycm93IFxcYmFye1h9IFxcc2ltIE4oMTAsIDAuMjUpJC4iLCAiTyBlcnJvIHBhZHLDo28gw6kgJEVQKFxcYmFye1h9KSA9IFxcZnJhY3tcXHNpZ21hfXtcXHNxcnR7bn19ID0gXFxmcmFjezJ9e1xcc3FydHsxNn19ID0gMC41JC4iLCAiQ2FsY3VsYW1vcyBvICRaX3tcXHRleHR7Y3JpdH19JCBwYXJhIG8gcG9udG8gZGUgY29ydGUgJDEwLjgkOiAkWiA9IFxcZnJhY3sxMC44IC0gMTB9ezAuNX0gPSAxLjYkLiIsICJBIHByb2JhYmlsaWRhZGUgZGUgRXJybyBUaXBvIEkgw6kgJFxcYWxwaGEgPSBQKFxcYmFye1h9ID4gMTAuOCB8IFxcbXUgPSAxMCkgPSBQKFogPiAxLjYpJC4iLCAiQ29uc3VsdGFuZG8gYSB0YWJlbGEgbm9ybWFsIHBhZHLDo28sICRQKFogXFxsZXEgMS42KSBcXGFwcHJveCAwLjk0NTIkLiBQb3J0YW50bywgJFxcYWxwaGEgPSAxIC0gMC45NDUyID0gMC4wNTQ4JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMDU0OH0sIHsiZW51bmNpYWRvIjogIkNvbSBiYXNlIG5vcyBtZXNtb3MgcGFyw6JtZXRyb3MgZGEgcXVlc3TDo28gYW50ZXJpb3IgKCRIXzA6IFxcbXUgPSAxMCwgSF8xOiBcXG11ID0gMTIsIFxcc2lnbWEgPSAyLCBuID0gMTYsIFxcdGV4dHtSQ306IFxcYmFye1h9ID4gMTAuOCQpLCBjYWxjdWxlIG8gUG9kZXIgZG8gVGVzdGUgKCQxIC0gXFxiZXRhJCkgcGFyYSBhIGhpcMOzdGVzZSBhbHRlcm5hdGl2YSAkXFxtdSA9IDEyJC4iLCAiZGljYSI6ICJBZ29yYSwgYXNzdW1hIHF1ZSBhIG3DqWRpYSByZWFsIMOpICQxMiQuIENhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIChvdSBzZWphLCBlbmNvbnRyYXIgJFxcYmFye1h9ID4gMTAuOCQpIHNvYiBlc3RhIG5vdmEgbcOpZGlhLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJTb2IgJEhfMSQsIHRlbW9zICRcXGJhcntYfSBcXHNpbSBOKDEyLCAwLjI1KSQuIiwgIlF1ZXJlbW9zIGNhbGN1bGFyIGEgcHJvYmFiaWxpZGFkZSBkZSByZWplaXRhciAkSF8wJCwgcXVlIG9jb3JyZSBxdWFuZG8gJFxcYmFye1h9ID4gMTAuOCQuIiwgIkNvbnZlcnRlbW9zIHBhcmEgYSBub3JtYWwgcGFkcsOjbyBzb2IgYSBub3ZhIG3DqWRpYTogJFogPSBcXGZyYWN7MTAuOCAtIDEyfXswLjV9ID0gXFxmcmFjey0xLjJ9ezAuNX0gPSAtMi40JC4iLCAiTyBQb2RlciBkbyBUZXN0ZSDDqSAkUChcXGJhcntYfSA+IDEwLjggfCBcXG11ID0gMTIpID0gUChaID4gLTIuNCkkLiIsICJQZWxhIHNpbWV0cmlhIGUgcHJvcHJpZWRhZGVzIGRhIG5vcm1hbDogJFAoWiA+IC0yLjQpID0gUChaIDwgMi40KSBcXGFwcHJveCAwLjk5MTgkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC45OTE4fSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIHV0aWxpemFuZG8gbyBmb3JtYWxpc21vIGRhIGZ1bsOnw6NvIHBvZGVyICRcXHBpKFxcdGhldGEpJCwgcG9yIHF1ZSB1bSB0ZXN0ZSBjb20gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIG11aXRvIGJhaXhvIHRlbmRlIGEgYXByZXNlbnRhciB1bSBwb2RlciBkZSB0ZXN0ZSBiYWl4by4gQ29tbyBhIGFsdGVyYcOnw6NvIGRhIFJlZ2nDo28gQ3LDrXRpY2EgKCRSQyQpIGluZmx1ZW5jaWEgYSBwcm9iYWJpbGlkYWRlIGRlIEVycm8gVGlwbyBJSSAoJFxcYmV0YSQpPyIsICJkaWNhIjogIkNvbnNpZGVyZSBhIGludGVncmFsIGRhIGZ1bsOnw6NvIGRlbnNpZGFkZSBkYSBhbW9zdHJhIHNvYnJlIGEgcmVnacOjbyBkZSBuw6NvLXJlamVpw6fDo28gc29iICRIXzEkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBIGZ1bsOnw6NvIHBvZGVyIMOpIGRlZmluaWRhIHBvciAkXFxwaShcXHRoZXRhKSA9IFAoXFxoYXR7XFx0aGV0YX0gXFxpbiBSQyB8IFxcdGhldGEpJC4iLCAiUGFyYSB1bSB0ZXN0ZSBvbmRlICRIXzA6IFxcdGhldGEgPSBcXHRoZXRhXzAkLCB0ZW1vcyAkXFxwaShcXHRoZXRhXzApID0gXFxhbHBoYSQuIiwgIkFvIHJlZHV6aXIgJFxcYWxwaGEkLCByZXN0cmluZ2ltb3MgYSBSZWdpw6NvIENyw610aWNhICgkUkMkKS4gQ29tbyAkUkMkIGRpbWludWksIG8gY29tcGxlbWVudG8gKHJlZ2nDo28gZGUgbsOjby1yZWplacOnw6NvLCBkZW5vdGFkYSAkUkNeYyQpIGF1bWVudGEuIiwgIk8gZXJybyBUaXBvIElJIMOpICRcXGJldGEoXFx0aGV0YV8xKSA9IFAoXFxoYXR7XFx0aGV0YX0gXFxpbiBSQ15jIHwgXFx0aGV0YV8xKSQuIiwgIlBvcnRhbnRvLCBhbyByZWR1emlyIGEgw6FyZWEgZGUgJFJDJCwgYXVtZW50YW1vcyBhIMOhcmVhIGRlICRSQ15jJCBzb2IgYSBkaXN0cmlidWnDp8OjbyBkZSAkXFx0aGV0YV8xJCwgbyBxdWUgaW1wbGljYSB1bSBhdW1lbnRvIGRpcmV0byBlbSAkXFxiZXRhJCBlLCBjb25zZXF1ZW50ZW1lbnRlLCB1bWEgZGltaW51acOnw6NvIGVtICQxIC0gXFxiZXRhJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyB0ZXN0ZSAkSF97MH06IFxcbXUgPSAxMDAkIHZlcnN1cyAkSF97MX06IFxcbXUgXFxuZXEgMTAwJCBjb20gJFxcc2lnbWEgPSAxNSQgZSAkbiA9IDM2JC4gQ29tICRcXGFscGhhID0gMC4wNSQsIGRldGVybWluZSBhIHJlZ2nDo28gY3LDrXRpY2EgKFJDKSBlIGRlc2NyZXZhIG1hdGVtYXRpY2FtZW50ZSBjb21vIGNhbGN1bGFyIGEgZnVuw6fDo28gcG9kZXIgJFxccGkoXFxtdSkkIHBhcmEgdW0gdmFsb3IgJFxcbXUgPSAxMDUkLiIsICJkaWNhIjogIlVzZSBvIHZhbG9yIGNyw610aWNvICRaX3tjcml0fSA9IDEuOTYkIHBhcmEgYSBkaXN0cmlidWnDp8OjbyBiaWNhdWRhbC4gQSBmdW7Dp8OjbyBwb2RlciDDqSAkXFxwaShcXG11KSA9IDEgLSBQKFJBIHwgXFxtdSkkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBDw6FsY3VsbyBkbyBlcnJvIHBhZHLDo286ICRFUChcXGJhcntYfSkgPSAxNSAvIFxcc3FydHszNn0gPSAxNSAvIDYgPSAyLjUkLiIsICIyLiBEZWZpbmnDp8OjbyBkYSBSQyAoYmljYXVkYWwpOiAkXFxiYXJ7eH1fe2MxfSA9IDEwMCAtIDEuOTYoMi41KSA9IDk1LjEkIGUgJFxcYmFye3h9X3tjMn0gPSAxMDAgKyAxLjk2KDIuNSkgPSAxMDQuOSQuIEFzc2ltLCAkUkMgPSBcXHtcXGJhcntYfSA8IDk1LjEgXFxjdXAgXFxiYXJ7WH0gPiAxMDQuOVxcfSQuIiwgIjMuIEZ1bsOnw6NvIHBvZGVyIHBhcmEgJFxcbXUgPSAxMDUkOiAkXFxwaSgxMDUpID0gUChcXGJhcntYfSA8IDk1LjEgfCBcXG11ID0gMTA1KSArIFAoXFxiYXJ7WH0gPiAxMDQuOSB8IFxcbXUgPSAxMDUpJC4iLCAiNC4gUGFkcm9uaXphw6fDo286ICRQKFogPCAoOTUuMSAtIDEwNSkvMi41KSArIFAoWiA+ICgxMDQuOSAtIDEwNSkvMi41KSA9IFAoWiA8IC0zLjk2KSArIFAoWiA+IC0wLjA0KSQuIiwgIjUuIFJlc3VsdGFkbyBmaW5hbCBhcHJveGltYWRvOiAkMCArIDAuNTE2MCA9IDAuNTE2MCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIENhcCAxMiwgcC4gMzM2IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC41MTZ9LCB7ImVudW5jaWFkbyI6ICJVbWEgZsOhYnJpY2EgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIHRlc3RhICRIX3swfTogcCA9IDAuMDUkICh0YXhhIGRlIGRlZmVpdG8pIGNvbnRyYSAkSF97MX06IHAgPiAwLjA1JCBjb20gJG4gPSAyMDAkLiBTZSBhIHJlZ2nDo28gY3LDrXRpY2Egw6kgJFxcaGF0e3B9ID4gMC4wOCQsIGNhbGN1bGUgbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkIGRvIHRlc3RlIHV0aWxpemFuZG8gYSBhcHJveGltYcOnw6NvIG5vcm1hbC4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIHNvYiAkSF97MH0kLCAkXFxoYXR7cH0gXFxzaW0gTihwX3swfSwgXFxmcmFje3BfezB9KDEtcF97MH0pfXtufSkkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBNw6lkaWEgc29iICRIX3swfSQ6ICRcXG11X3tcXGhhdHtwfX0gPSAwLjA1JC4iLCAiMi4gVmFyacOibmNpYSBzb2IgJEhfezB9JDogJFxcc2lnbWFeMl97XFxoYXR7cH19ID0gXFxmcmFjezAuMDUgXFx0aW1lcyAwLjk1fXsyMDB9ID0gXFxmcmFjezAuMDQ3NX17MjAwfSA9IDAuMDAwMjM3NSQuIiwgIjMuIEVycm8gcGFkcsOjbzogJFxcc2lnbWFfe1xcaGF0e3B9fSA9IFxcc3FydHswLjAwMDIzNzV9IFxcYXBwcm94IDAuMDE1NDEkLiIsICI0LiBDw6FsY3VsbyBkZSBaOiAkWiA9IFxcZnJhY3swLjA4IC0gMC4wNX17MC4wMTU0MX0gXFxhcHByb3ggMS45NDYkLiIsICI1LiBQcm9iYWJpbGlkYWRlICRcXGFscGhhID0gUChaID4gMS45NDYpIFxcYXBwcm94IDAuMDI1OCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjAyNTh9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgZG8gcG9udG8gZGUgdmlzdGEgZGEgQW7DoWxpc2UgZGEgRnVuw6fDo28gQ2FyYWN0ZXLDrXN0aWNhIGRlIE9wZXJhw6fDo28sIG8gaW1wYWN0byBkbyBhdW1lbnRvIGRvIHRhbWFuaG8gYW1vc3RyYWwgJG4kIG5hIHBlcmZvcm1hbmNlIGRlIHVtIHRlc3RlIGVzdGF0w61zdGljby4iLCAiZGljYSI6ICJSZWxhY2lvbmUgbyBhdW1lbnRvIGRlICRuJCBjb20gYSByZWR1w6fDo28gZG8gZXJybyBwYWRyw6NvIGUgbyBlc3RyZWl0YW1lbnRvIGRhcyBkaXN0cmlidWnDp8O1ZXMgYW1vc3RyYWlzIHNvYiAkSF97MH0kIGUgJEhfezF9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gQXVtZW50YXIgJG4kIHJlZHV6IG8gZXJybyBwYWRyw6NvIGRhIGVzdGF0w61zdGljYSBkZSB0ZXN0ZTogJEVQID0gXFxzaWdtYSAvIFxcc3FydHtufSQuIiwgIjIuIENvbSBvIGVycm8gcGFkcsOjbyBtZW5vciwgYSBzb2JyZXBvc2nDp8OjbyBlbnRyZSBhcyBkaXN0cmlidWnDp8O1ZXMgZGEgZXN0YXTDrXN0aWNhIHNvYiAkSF97MH0kIGUgJEhfezF9JCBkaW1pbnVpLiIsICIzLiBDb21vIGNvbnNlcXXDqm5jaWEsIHBhcmEgdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCBmaXhvLCBhIHJlZ2nDo28gZGUgYWNlaXRhw6fDo28gKFJBKSB0b3JuYS1zZSBtYWlzIHByZWNpc2EuIiwgIjQuIElzc28gcmVzdWx0YSBlbSB1bWEgY3VydmEgZGUgcG9kZXIgJFxccGkoXFxtdSkkIHF1ZSBjcmVzY2UgbWFpcyByYXBpZGFtZW50ZSBlbSBkaXJlw6fDo28gYSAxIHBhcmEgZGVzdmlvcyBkbyBwYXLDom1ldHJvIGVtIHJlbGHDp8OjbyBhbyB2YWxvciBkYSBoaXDDs3Rlc2UgbnVsYS4iLCAiNS4gQ29uY2x1aS1zZSBxdWUgbyB0ZXN0ZSB0b3JuYS1zZSBtYWlzIHNlbnPDrXZlbCBlIGNhcGF6IGRlIGRldGVjdGFyIGRlc3Zpb3MgcmVhaXMgY29tIG1haW9yIHByb2JhYmlsaWRhZGUgKG1haW9yIHBvZGVyKS4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgtMywgMywgMTAwKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT1zdGF0cy5ub3JtLnBkZih4LCAtMSwgMC41KSwgbmFtZT0nQW1vc3RyYSBQZXF1ZW5hIChTb2JyZXBvc2nDp8OjbyBBbHRhKScsIGxpbmU9ZGljdChjb2xvcj0nI0Y1OUUwQicpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9c3RhdHMubm9ybS5wZGYoeCwgMSwgMC41KSwgbmFtZT0nQW1vc3RyYSBQZXF1ZW5hIChTb2JyZXBvc2nDp8OjbyBBbHRhKScsIGxpbmU9ZGljdChjb2xvcj0nI0Y1OUUwQicpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9c3RhdHMubm9ybS5wZGYoeCwgLTEsIDAuMiksIG5hbWU9J0Ftb3N0cmEgR3JhbmRlIChTb2JyZXBvc2nDp8OjbyBCYWl4YSknLCBsaW5lPWRpY3QoY29sb3I9JyMxMEI5ODEnKSkpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLm5vcm0ucGRmKHgsIDEsIDAuMiksIG5hbWU9J0Ftb3N0cmEgR3JhbmRlIChTb2JyZXBvc2nDp8OjbyBCYWl4YSknLCBsaW5lPWRpY3QoY29sb3I9JyMxMEI5ODEnKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nRWZlaXRvIGRvIGF1bWVudG8gZGUgbiBuYSBzb2JyZXBvc2nDp8OjbyBkYXMgZGlzdHJpYnVpw6fDtWVzJywgeGF4aXNfdGl0bGU9J0VzdGF0w61zdGljYScsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJylcbmZpZy5zaG93KCkiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgQ2FwIDEyLCBwLiAzNDciLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfV19').decode('utf-8'))


    # Inicialização da estrutura de controle de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo do progresso
    total_mcq = len(dados_exercicios.get("questoes_multipla_escolha", []))
    total_disc = len(dados_exercicios.get("questoes_discursivas", []))
    total_exercicios = total_mcq + total_disc
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    # Barra de progresso e status
    st.markdown(f"### 📊 Painel de Desempenho: {dados_exercicios.get('topico_aula', 'Exercícios')}")
    progresso = acertos / total_exercicios if total_exercicios > 0 else 0
    st.progress(progresso)
    st.markdown(f"🏆 **Seu Progresso:** {acertos} de {total_exercicios} desafios concluídos!")
    
    # Seção de Múltipla Escolha
    if total_mcq > 0:
        st.markdown("---")
        st.subheader("📝 Questões de Múltipla Escolha")
        for i, questao in enumerate(dados_exercicios["questoes_multipla_escolha"]):
            with st.container(border=True):
                st.markdown(f"**Questão {i+1}:** {questao.get('enunciado')}")
                
                # Referência
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                # Gráfico dinâmico
                cod = questao.get("codigo_plotly")
                if cod:
                    local_vars = {"np": __import__("numpy"), "go": __import__("plotly.graph_objects").graph_objects, "stats": __import__("scipy.stats", fromlist=["stats"])}
                    try:
                        exec(cod, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True)
                    except Exception as e:
                        st.warning("Visualização gráfica indisponível no momento.")
    
                # Alternativas
                opcoes = questao.get("alternativas", {})
                escolha = st.radio("Escolha uma opção:", list(opcoes.values()), key=f"radio_mcq_{i}", index=None)
                
                # Dica
                if st.button("💡 Dica", key=f"btn_dica_mcq_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
                
                # Validação
                if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
                    correta_label = opcoes.get(questao.get("alternativa_correta"))
                    if escolha == correta_label:
                        st.success("Correto! Muito bem.")
                        st.session_state.respostas_certas[f"mcq_{i}"] = True
                        st.rerun()
                    else:
                        st.error("Resposta incorreta. Tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
                
                with st.expander("✅ Ver Gabarito Comentado"):
                    st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
    
    # Seção de Questões Discursivas
    if total_disc > 0:
        st.markdown("---")
        st.subheader("✍️ Questões Discursivas")
        for i, questao in enumerate(dados_exercicios["questoes_discursivas"]):
            with st.container(border=True):
                st.markdown(f"**Desafio {i+1}:** {questao.get('enunciado')}")
                
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
                
                # Validação numérica ou checkbox
                val_esperado = questao.get("resposta_numerica_esperada")
                if val_esperado is not None:
                    user_val = st.number_input("Digite o resultado numérico calculado:", format="%.4f", key=f"num_disc_{i}")
                    if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                        if abs(user_val - val_esperado) <= max(0.01, 0.01 * abs(val_esperado)):
                            st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                            st.session_state.respostas_certas[f"disc_{i}"] = True
                            st.rerun()
                        else:
                            st.error("O valor calculado difere do gabarito. Verifique suas fórmulas.")
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
