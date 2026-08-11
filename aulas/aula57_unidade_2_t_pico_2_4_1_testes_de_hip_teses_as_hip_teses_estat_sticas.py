import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4xOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogQXMgaGlww7N0ZXNlcyBlc3RhdMOtc3RpY2FzIiwgInJlZmVyZW5jaWFzX2JpYmxpb2dyYWZpY2FzX2ZpbmFpcyI6IFsiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhIC0gQ2FwLiAxMiwgcHAuIDMzMS0zNDEiXX0=').decode('utf-8'))

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

    # A Lógica da Inferência: A Natureza das Hipóteses Estatísticas
    
    st.header(r"A Lógica da Inferência: A Natureza das Hipóteses Estatísticas")
    
    st.markdown(r"""
    A inferência estatística fundamenta-se na capacidade de realizar generalizações sobre parâmetros populacionais a partir de evidências contidas em amostras representativas. Em cenários práticos, como o controle de qualidade industrial, a medição exaustiva de uma população é, frequentemente, impossível devido a restrições de custo, tempo ou natureza destrutiva do teste.
    """)
    
    st.info(r"O teste de hipóteses emerge como um rigoroso filtro lógico, estruturado para confrontar uma suposição inicial acerca da população, a hipótese nula, com os dados observados.")
    
    st.markdown(r"""
    A lógica subjacente é a da redução ao absurdo: assumimos a validade da hipótese nula e avaliamos se os dados amostrais apresentam evidências suficientemente fortes para refutar essa premissa. Caso a estatística amostral calculada situe-se em uma região de baixa probabilidade sob a égide da hipótese nula, somos compelidos a rejeitá-la, concluindo que o efeito observado é estatisticamente significante.
    """)
    
    st.markdown(r"### 📐 O Coração Matemático: Estruturação de Hipóteses")
    
    st.markdown(r"""
    Para compreender a lógica da inferência estatística, devemos primeiro reconhecer que a estatística amostral é, em si, uma variável aleatória que traz consigo uma margem de incerteza inerente. O teste de hipóteses organiza essa incerteza em um embate entre duas proposições antagônicas:
    """)
    
    st.latex(r"H_0: \theta = \theta_0 \quad \text{vs.} \quad H_1: \theta \neq \theta_0 \text{ (ou } \theta < \theta_0, \theta > \theta_0 \text{)}")
    
    st.markdown(r"""
    Esta formulação deve ser interpretada como um compromisso metodológico de "presunção de inocência" da hipótese nula, onde o parâmetro é considerado em seu estado de estabilidade até que provas robustas indiquem o contrário.
    """)
    
    st.markdown(r"### 🔍 Dedução Analítica: Probabilidades e Decisão")
    
    st.markdown(r"O processo de decisão inferencial é regido pelas seguintes definições formais que quantificam o risco de erro:")
    
    st.latex(r"P(\text{Erro Tipo I}) = P(\text{rejeitar } H_0 | H_0 \text{ é verdadeira}) = \alpha")
    
    st.markdown(r"A Região Crítica (RC) é o conjunto de valores da estatística de teste que leva à rejeição da hipótese nula:")
    
    st.latex(r"\text{RC} = \{ \hat{\theta} \in \mathbb{R} | P(\hat{\theta} \in \text{RC} | H_0 \text{ verdadeira}) = \alpha \}")
    
    st.markdown(r"Complementarmente, a probabilidade de falhar em detectar um efeito real é definida como o Erro Tipo II:")
    
    st.latex(r"\beta = P(\text{não rejeitar } H_0 | H_0 \text{ é falsa}) = P(\text{aceitar } H_0 | H_1 \text{ é verdadeira})")
    
    st.markdown(r"### 📈 Casos de Aplicação Prática: Controle de Qualidade Laticínios")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Verificação de Conformidade de Gordura")
        st.markdown(r"""
        Uma indústria de laticínios deseja verificar se a média de gordura em um novo lote de leite em pó é de 20g por porção, conforme especificado no rótulo. Sabe-se que o teor de gordura segue uma distribuição normal com desvio padrão populacional $\sigma = 2g$.
        
        Coleta-se uma amostra aleatória de $n = 25$ porções, resultando em uma média amostral $\bar{X} = 21g$. Adota-se um nível de significância de $\alpha = 0,05$.
        """)
        
        st.latex(r"\mu_0 = 20, \quad \sigma = 2, \quad n = 25, \quad \bar{X} = 21, \quad \alpha = 0,05")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Cálculo do Erro Padrão:** $EP(\bar{X}) = \frac{\sigma}{\sqrt{n}} = \frac{2}{5} = 0,4$")
        st.markdown(r"- **Cálculo da Estatística Z:** $Z_{\text{calc}} = \frac{\bar{X} - \mu_0}{EP(\bar{X})} = \frac{21 - 20}{0,4} = 2,5$")
        st.markdown(r"- **Comparação:** $|2,5| > 1,96$ (onde 1,96 é o valor crítico para $\alpha=0,05$ bilateral)")
        
        st.success(r"**Conclusão:** Com $|Z_{\text{calc}}| = 2,5 > 1,96$, rejeita-se a hipótese nula. O teor de gordura apresenta uma diferença estatisticamente significante, recomendando-se a interrupção do lote para inspeção técnica.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título Principal do Subtópico
    st.header(r"Arquitetura do Teste: Formulações Unilaterais e Bilaterais")
    
    # Introdução e Contextualização
    st.markdown(r"""
    A estruturação de um teste de hipóteses transcende a mera manipulação algébrica de valores críticos e estatísticas de teste; ela representa, fundamentalmente, a formalização estatística da intenção do investigador frente a um fenômeno de interesse. 
    """)
    
    st.info(r"A decisão de adotar uma estrutura bilateral ou unilateral não é um detalhe técnico trivial, mas uma escolha de cunho epistemológico que molda a capacidade do pesquisador de detectar desvios em relação a um estado de estabilidade, denominado hipótese nula.")
    
    st.markdown(r"""
    A escolha entre essas duas arquiteturas deve ser estritamente fundamentada no conhecimento teórico prévio. Devemos equilibrar o rigor exigido pelo nível de significância $\alpha$ e a sensibilidade do procedimento, ou seja, o poder do teste, definido por $1 - \beta$.
    """)
    
    # Seção: A Neutralidade vs Precisão
    st.subheader(r"⚖️ Neutralidade Científica vs. Precisão Estratégica")
    
    st.markdown(r"""
    - **Teste Bilateral (Neutralidade):** Atua como a sentinela da neutralidade científica. Quando formulamos $H_1: \theta \neq \theta_0$, declaramos não possuir justificativas empíricas para antecipar a direção do efeito. A massa de significância $\alpha$ é dividida, protegendo o pesquisador contra desvios inesperados.
    - **Teste Unilateral (Precisão):** Surge como uma ferramenta de alta precisão quando o arcabouço teórico postula uma direção específica. Ao concentrar toda a massa de $\alpha$ em uma única cauda, o teste torna-se inerentemente mais potente para detectar efeitos na direção desejada.
    """)
    
    st.warning(r"Aviso Crítico: A escolha da direção do teste baseada apenas na observação dos resultados (o 'ajuste de cauda') constitui uma violação severa da integridade científica e um erro crasso de metodologia.")
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Arquiteturas de Decisão")
    st.latex(r"H_1: \theta \neq \theta_0 \text{ (Bilateral) } \quad \text{vs.} \quad H_1: \theta > \theta_0 \text{ ou } H_1: \theta < \theta_0 \text{ (Unilaterais)}")
    
    st.markdown(r"A geometria da região de rejeição ($RC$) altera o comportamento do teste. Abaixo, observamos a definição dos valores críticos sob a distribuição normal padrão:")
    
    st.latex(r"P(|Z_{\text{calc}}| > Z_{\text{crit}}) = \alpha \Rightarrow Z_{\text{crit}} = 1,96 \text{ (Bilateral)}")
    st.markdown(r"Para testes unilaterais, o rigor é redirecionado:")
    st.latex(r"P(Z_{\text{calc}} > Z_{\text{crit}}) = \alpha \Rightarrow Z_{\text{crit}} = 1,645 \text{ (Unilateral à direita)}")
    st.latex(r"P(Z_{\text{calc}} < Z_{\text{crit}}) = \alpha \Rightarrow Z_{\text{crit}} = -1,645 \text{ (Unilateral à esquerda)}")
    
    # Seção de Casos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática: Auditoria de Performance")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Eficiência de Telecomunicações")
        st.markdown(r"Um órgão de defesa do consumidor investiga uma empresa de telecomunicações que promete uma velocidade média de download de 100 Mbps. O auditor coletou uma amostra de 36 testes, com média $\bar{X} = 96$ e desvio padrão populacional $\sigma = 12$, ao nível de significância de 5%.")
        
        # Dados sumarizados via DataFrame
        df_dados = pd.DataFrame({
            "Parâmetro": [r"Média Nula (\mu_0)", r"Desvio Padrão (\sigma)", r"Tamanho Amostra (n)", r"Média Amostral (\bar{X})", r"Nível Significância (\alpha)"],
            "Valor": ["100 Mbps", "12 Mbps", "36", "96 Mbps", "0,05"]
        })
        st.table(df_dados)
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Erro Padrão: $EP(\bar{X}) = \frac{12}{\sqrt{36}} = 2,0$")
        st.markdown(r"- Estatística de Teste: $Z_{\text{calc}} = \frac{96 - 100}{2,0} = -2,0$")
        
        st.success(r"Conclusão: Como $Z_{\text{calc}} = -2,0 < -1,645$, rejeitamos $H_0$. Com 95% de confiança, a velocidade média é estatisticamente inferior a 100 Mbps, fundamentando a notificação à empresa.")
    
    # Conclusão Final
    st.markdown(r"""
    ---
    **Nota do Arquiteto de Dados:** A eficácia de qualquer teste de hipóteses não reside na sofisticação da fórmula, mas na clareza do pensamento que a precede. A decisão entre a simetria bilateral e o direcionamento unilateral é o primeiro passo para a integridade científica.
    """)

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    # Cabeçalho do Subtópico
    st.header(r"Erros de Decisão e o Controle de Significância")
    
    # Prosa Teórica - Parte 1
    st.markdown(r"""
    A inferência estatística, na sua essência, não é o exercício de buscar a verdade absoluta, mas a arte de gerenciar a incerteza inerente ao processo de tomada de decisão a partir de evidências parciais. 
    Ao realizarmos um teste de hipóteses, confrontamos dois estados da natureza: a hipótese nula ($H_0$) e a hipótese alternativa ($H_1$).
    """)
    
    st.info(r"A decisão de rejeitar ou não $H_0$ não é um juízo determinístico, mas uma conclusão probabilística fundamentada no paradigma de Neyman-Pearson.")
    
    # Prosa Teórica - Parte 2: Erros
    st.markdown(r"""
    Dentro desse framework, operamos sob a constante ameaça de dois tipos de equívocos fundamentais:
    - **Erro Tipo I ($\alpha$):** A 'falsa descoberta'. Ocorre quando rejeitamos $H_0$ sendo ela verdadeira. Representa nosso nível de tolerância ao falso positivo.
    - **Erro Tipo II ($\beta$):** O 'erro de negligência'. Ocorre quando falhamos em rejeitar $H_0$ quando $H_1$ é o cenário real. Reflete a falta de sensibilidade do teste.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Gestão da Incerteza")
    st.latex(r"P(\text{Erro Tipo I}) = \alpha, \quad P(\text{Erro Tipo II}) = \beta, \quad \text{Poder} = 1 - \beta")
    
    st.markdown(r"Abaixo, detalhamos o formalismo analítico que rege a decisão estatística:")
    st.latex(r"\alpha = P(\bar{X} \in RC | H_0 \text{ verdadeira})")
    st.latex(r"\beta = P(\bar{X} \notin RC | \mu = \mu_1)")
    st.latex(r"\text{Poder} = P(\bar{X} \in RC | \mu = \mu_1)")
    
    # Simulador: Visualizador de Erros e Poder
    st.subheader(r"🎛️ Simulador: Visualizador de Erros e Poder")
    col1, col2 = st.columns(2)
    with col1:
        n = st.slider(r"Tamanho da Amostra ($n$)", 5, 100, 16, key=r"n_subtopico_3")
        alfa = st.slider(r"Nível de Significância ($\alpha$)", 0.01, 0.20, 0.05, key=r"alfa_subtopico_3")
    with col2:
        mu1 = st.slider(r"Média sob $H_1$ ($\mu_1$)", 5.5, 8.0, 6.0, key=r"mu1_subtopico_3")
    
    # Cálculos do Simulador
    mu0 = 5.0
    sigma = 2.0
    ep = sigma / np.sqrt(n)
    z_alfa = norm.ppf(1 - alfa)
    rc = mu0 + z_alfa * ep
    beta = norm.cdf(rc, loc=mu1, scale=ep)
    poder = 1 - beta
    
    # Plotagem
    x = np.linspace(2, 9, 200)
    y0 = norm.pdf(x, mu0, ep)
    y1 = norm.pdf(x, mu1, ep)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y0, name=r"H0 (Nula)", line=dict(color="#1E3A8A")))
    fig.add_trace(go.Scatter(x=x, y=y1, name=r"H1 (Alternativa)", line=dict(color="#991B1B")))
    fig.add_vline(x=rc, line_dash="dash", line_color="#F59E0B", annotation_text=r"Região Crítica")
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuições e Área de Erro</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif")),
        xaxis=dict(title=dict(text="Parâmetro", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"))
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    # Laudo Dinâmico
    st.info(f"Com n={n} e alpha={alfa}, o poder do teste é de {poder:.2%}. A região crítica começa em {rc:.3f}. Ao aumentar o tamanho amostral, o Erro Padrão diminui, tornando as curvas mais estreitas e aumentando o poder estatístico.")
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Eficácia de Fármaco")
        st.markdown(r"Avaliação de novo fármaco para redução de pressão. $H_0: \mu=5, H_1: \mu>5, n=16, \sigma=2, \alpha=0.05$.")
        st.latex(r"\mu_0 = 5, \quad \mu_1 = 6, \quad \sigma = 2, \quad n = 16, \quad \alpha = 0.05")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Erro Padrão: $EP(\bar{X}) = 2 / \sqrt{16} = 0.5$")
        st.markdown(r"- Região Crítica: $RC: \bar{X} > 5 + (1.645 \cdot 0.5) = 5.8225$")
        st.markdown(r"- $\beta = P(\bar{X} \leq 5.8225 | \mu = 6) \approx 0.3613$")
        st.success(r"O erro tipo II de 36,13% indica um poder estatístico de 63,87%. O teste possui sensibilidade moderada, mas a expansão amostral é recomendada para maior robustez.")

    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"O Procedimento Sistemático: Etapas para a Construção de Testes")
    
    # Discussão Teórica
    st.markdown(r"""
    A inferência estatística é, fundamentalmente, uma disciplina de controle de erro sob incerteza. Para que possamos transpor a barreira que separa uma simples observação amostral de uma conclusão científica generalizável, é imperativo seguir um protocolo sistemático que minimize a subjetividade.
    """)
    
    st.info(r"Sem um método formal, o pesquisador corre o risco de cair na falácia da confirmação, ajustando a interpretação dos dados para atender a desejos prévios em vez de permitir que a estrutura probabilística da amostra dite a viabilidade de uma hipótese.")
    
    st.markdown(r"""
    ### 📐 O Coração Matemático: Protocolo de Testes de Hipóteses
    Para que a inferência seja válida e replicável, a aplicação de testes deve seguir estritamente as etapas abaixo:
    """)
    
    st.latex(r"1. \text{ Formulação: } H_0: \theta = \theta_0 \text{ vs. } H_1: \theta \neq \theta_0")
    st.latex(r"2. \text{ Estatística de Teste: } \hat{\theta} \sim f(\theta_0, \sigma^2/n)")
    st.latex(r"3. \text{ Nível de Significância: } RC \text{ tal que } P(\hat{\theta} \in RC) = \alpha")
    st.latex(r"4. \text{ Cálculo Empírico: } \hat{\theta}_{\text{calc}} = g(X_1, ..., X_n)")
    st.latex(r"5. \text{ Tomada de Decisão: } \text{Rejeitar } H_0 \text{ se } \hat{\theta}_{\text{calc}} \in RC")
    
    # Simulador de Região Crítica
    st.subheader(r"📈 Simulador Interativo: Região Crítica")
    
    col1, col2 = st.columns(2)
    with col1:
        alfa = st.select_slider(r"Nível de Significância (α)", options=[0.01, 0.05, 0.10], value=0.05, key=r"alfa_simulador_subtopico_4")
        tipo_teste = st.selectbox(r"Tipo de Teste", [r"Bilateral", r"Unilateral Direita", r"Unilateral Esquerda"], key=r"tipo_teste_simulador_subtopico_4")
    with col2:
        z_calc = st.number_input(r"Valor da Estatística Z_calc", value=0.0, step=0.1, key=r"z_calc_simulador_subtopico_4")
        exibir_regiao = st.toggle(r"Sombrear Região Crítica", value=True, key=r"toggle_simulador_subtopico_4")
    
    # Lógica do Simulador
    x = np.linspace(-4, 4, 200)
    y = stats.norm.pdf(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=r"Distribuição Normal", line=dict(color="#1E3A8A", width=2)))
    
    if exibir_regiao:
        if tipo_teste == r"Bilateral":
            crit = stats.norm.ppf(1 - alfa/2)
            fig.add_vrect(x0=crit, x1=4, fillcolor="#991B1B", opacity=0.3, line_width=0)
            fig.add_vrect(x0=-4, x1=-crit, fillcolor="#991B1B", opacity=0.3, line_width=0)
            rejeicao = abs(z_calc) > crit
        elif tipo_teste == r"Unilateral Direita":
            crit = stats.norm.ppf(1 - alfa)
            fig.add_vrect(x0=crit, x1=4, fillcolor="#991B1B", opacity=0.3, line_width=0)
            rejeicao = z_calc > crit
        else:
            crit = stats.norm.ppf(alfa)
            fig.add_vrect(x0=-4, x1=crit, fillcolor="#991B1B", opacity=0.3, line_width=0)
            rejeicao = z_calc < crit
    
    fig.add_trace(go.Scatter(x=[z_calc], y=[stats.norm.pdf(z_calc)], mode='markers', name=r"Estatística Calculada", marker=dict(color="#10B981", size=12)))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Simulador de Região Crítica</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valor Z", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")
    
    # Feedback Dinâmico
    decisao_texto = "Rejeitar H0" if rejeicao else "Não rejeitar H0"
    st.info(f"Com nível de significância de {alfa} e teste {tipo_teste}, o valor Z calculado de {z_calc} resulta na decisão: **{decisao_texto}**.")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática: Auditoria de Envase")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Indústria de Bebidas")
        st.markdown(r"Uma indústria de bebidas deseja auditar o volume de enchimento de suas garrafas de 500ml. Com desvio padrão populacional de 10ml, uma amostra de 25 garrafas resultou em uma média de 495ml.")
        st.latex(r"\mu_0 = 500, \quad \sigma = 10, \quad n = 25, \quad \bar{X} = 495, \quad \alpha = 0,05")
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Formulação: $H_0: \mu = 500$ vs $H_1: \mu \neq 500$")
        st.markdown(r"- Estatística Z: $Z = \frac{495 - 500}{10 / \sqrt{25}} = -2,5$")
        st.markdown(r"- Critério: Rejeitar se $|Z| > 1,96$")
        st.success(r"Conclusão: Como $|-2,5| > 1,96$, rejeitamos a hipótese nula. O volume de enchimento sofreu alteração significativa e exige manutenção imediata.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4xOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogQXMgaGlww7N0ZXNlcyBlc3RhdMOtc3RpY2FzIiwgInF1ZXN0b2VzX211bHRpcGxhX2VzY29saGEiOiBbeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgYWxpbWVudMOtY2lhIHV0aWxpemEgdW1hIG3DoXF1aW5hIHBhcmEgZW52YXNhciBwYWNvdGVzIGNvbSBwZXNvIG5vbWluYWwgZGUgJFxcbXUgPSA1MDAkIGcgZSB2YXJpw6JuY2lhIHBvcHVsYWNpb25hbCAkXFxzaWdtYV4yID0gNDAwJCBnJF4yJC4gTyBzZXRvciBkZSBxdWFsaWRhZGUgZGVzZWphIHZlcmlmaWNhciBzZSBhIG3DoXF1aW5hIGVzdMOhIGRlc3JlZ3VsYWRhLCBzZWphIHBhcmEgbWFpcyBvdSBwYXJhIG1lbm9zLCB1dGlsaXphbmRvIHVtYSBhbW9zdHJhIGRlICRuID0gMTYkIHBhY290ZXMuIENvbnNpZGVyYW5kbyBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSA9IDFcXCUkLCBxdWFsIMOpIGEgaW50ZXJwcmV0YcOnw6NvIGNvcnJldGEgZGEgUmVnacOjbyBDcsOtdGljYSAoJFJDJCkgZSBkYSBoaXDDs3Rlc2UgbnVsYSAoJEhfMCQpIG5lc3RlIGNlbsOhcmlvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBoaXDDs3Rlc2UgbnVsYSDDqSAkSF8wOiBcXG11IFxcbmVxIDUwMCQgZSBhICRSQyQgw6kgdW5pbGF0ZXJhbCDDoCBkaXJlaXRhLCByZWplaXRhbmRvICRIXzAkIHNlICRcXGJhcntYfSA+IDUxMiw5JC4iLCAiQiI6ICJBIGhpcMOzdGVzZSBudWxhIMOpICRIXzA6IFxcbXUgPSA1MDAkIGUgYSAkUkMkIMOpIGJpbGF0ZXJhbCwgZGVmaW5pZGEgY29tbyAkUkMgPSBcXHsgXFxiYXJ7WH0gXFxpbiBcXG1hdGhiYntSfSB8IFxcYmFye1h9IFxcbGUgNDg3LDEgXFx0ZXh0eyBvdSB9IFxcYmFye1h9IFxcZ2UgNTEyLDkgXFx9JC4iLCAiQyI6ICJBIGhpcMOzdGVzZSBudWxhIMOpICRIXzA6IFxcbXUgPSA1MDAkIGUgYSAkUkMkIMOpIHVuaWxhdGVyYWwgw6AgZXNxdWVyZGEsIHJlamVpdGFuZG8gJEhfMCQgc2UgJFxcYmFye1h9IDwgNDg3LDEkLiIsICJEIjogIkEgaGlww7N0ZXNlIG51bGEgw6kgJEhfMDogXFxtdSBcXGdlIDUwMCQgZSBvIGVycm8gZG8gdGlwbyBJIMOpIGRlZmluaWRvIHBlbGEgcHJvYmFiaWxpZGFkZSBkZSBhY2VpdGFyICRIXzAkIHF1YW5kbyAkXFxtdSA9IDUwMCQuIiwgIkUiOiAiQSBoaXDDs3Rlc2UgYWx0ZXJuYXRpdmEgJEhfMSQgw6kgJFxcbXUgPSA1MDAkLCBvIHF1ZSBpbXBsaWNhIHVtIHRlc3RlIGRlIHNpZ25pZmljw6JuY2lhIHBhcmEgdmVyaWZpY2FyIHNlIGEgbcOpZGlhIMOpIGV4YXRhbWVudGUgaWd1YWwgYW8gdmFsb3Igbm9taW5hbC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgdW0gdGVzdGUgYmlsYXRlcmFsIHBhcmEgYSBtw6lkaWEgcG9wdWxhY2lvbmFsIHV0aWxpemEgYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgcGFkcsOjbyBwYXJhIGVuY29udHJhciBvcyB2YWxvcmVzIGNyw610aWNvcyBhc3NvY2lhZG9zIGEgJFxcYWxwaGEvMiQgZW0gY2FkYSBjYXVkYSBkYSBkaXN0cmlidWnDp8Ojby4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBhcmEgJEhfMDogXFxtdSA9IDUwMCQgdnMgJEhfMTogXFxtdSBcXG5lcSA1MDAkLCBjb20gJFxcc2lnbWEgPSAyMCQgZSAkbiA9IDE2JCwgdGVtb3MgbyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhICRFUChcXGJhcntYfSkgPSBcXHNpZ21hIC8gXFxzcXJ0e259ID0gMjAgLyA0ID0gNSQuIEFvIG7DrXZlbCBkZSAkXFxhbHBoYSA9IDFcXCUkLCBidXNjYW1vcyB2YWxvcmVzIGNyw610aWNvcyAkWl97Y3JpdH0kIHRhbCBxdWUgYSDDoXJlYSBuYXMgY2F1ZGFzIHRvdGFsaXplIDAsMDEuIFBlbGEgdGFiZWxhICROKDAsMSkkLCAkWl97Y3JpdH0gPSBcXHBtIDIsNTgkLiBPcyB2YWxvcmVzIGNyw610aWNvcyBkYSBtw6lkaWEgYW1vc3RyYWwgc8OjbyAkXFxiYXJ7eH1fYyA9IFxcbXVfMCBcXHBtIFpfe2NyaXR9IFxcY2RvdCBFUChcXGJhcntYfSkgPSA1MDAgXFxwbSAyLDU4IFxcY2RvdCA1JC4gTG9nbywgJFxcYmFye3h9X3tjMX0gPSA0ODcsMSQgZSAkXFxiYXJ7eH1fe2MyfSA9IDUxMiw5JC4gQSByZWdpw6NvIGNyw610aWNhIMOpIG8gY29uanVudG8gZGUgdmFsb3JlcyBleHRyZW1vcyBxdWUgbGV2YW0gw6AgcmVqZWnDp8OjbyBkZSAkSF8wJC4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDQ4MCwgNTIwLCAxMDApXG55ID0gc3RhdHMubm9ybS5wZGYoeCwgNTAwLCA1KVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBuYW1lPSdEaXN0cmlidWnDp8OjbyBkYSBNw6lkaWEnLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0zKSkpXG5maWcuYWRkX3ZyZWN0KHgwPTQ4MCwgeDE9NDg3LjEsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTAsIG5hbWU9J1JDJylcbmZpZy5hZGRfdnJlY3QoeDA9NTEyLjksIHgxPTUyMCwgZmlsbGNvbG9yPScjOTkxQjFCJywgb3BhY2l0eT0wLjMsIGxpbmVfd2lkdGg9MCwgbmFtZT0nUkMnKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkRpc3RyaWJ1acOnw6NvIGRhIE3DqWRpYSBBbW9zdHJhbCBlIFJlZ2nDo28gQ3LDrXRpY2E8L2I+JywgeGF4aXNfdGl0bGU9cidNw6lkaWEgQW1vc3RyYWwgKCRcXGJhcntYfSQpJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM0MCJ9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSB0ZXN0ZSBkZSBoaXDDs3Rlc2VzIHNvYnJlIG8gcGFyw6JtZXRybyBwb3B1bGFjaW9uYWwgJFxcdGhldGEkLCBvIHBlc3F1aXNhZG9yIGRlc2VqYSBtYW50ZXIgbyBjb250cm9sZSBzb2JyZSBhIHByb2JhYmlsaWRhZGUgZGUgZXJybyBkZSB0aXBvIEkgKCRcXGFscGhhJCkgZSBvIHBvZGVyIGRvIHRlc3RlICgkMS1cXGJldGEkKS4gU29icmUgYSBuYXR1cmV6YSBkZXNzZXMgY29uY2VpdG9zLCBhc3NpbmFsZSBhIGFsdGVybmF0aXZhIGNvcnJldGE6IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIHBvZGVyIGRvIHRlc3RlICgkMS1cXGJldGEkKSDDqSBhIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgYSBoaXDDs3Rlc2UgbnVsYSAkSF8wJCBxdWFuZG8gZWxhIMOpLCBkZSBmYXRvLCB2ZXJkYWRlaXJhLiIsICJCIjogIk8gZXJybyBkZSB0aXBvIEkgb2NvcnJlIHF1YW5kbyBmYWxoYW1vcyBlbSBkZXRlY3RhciB1bSBkZXN2aW8gcmVhbCBkbyBwYXLDom1ldHJvLCBtYW50ZW5kbyAkSF8wJCBpbmNvcnJldGFtZW50ZS4iLCAiQyI6ICJPIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgcmVwcmVzZW50YSBhIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgYSBoaXDDs3Rlc2UgbnVsYSBxdWFuZG8gZWxhIMOpIHZlcmRhZGVpcmEuIiwgIkQiOiAiUGFyYSB1bSB0YW1hbmhvIGFtb3N0cmFsIGZpeG8gJG4kLCBhIHJlZHXDp8OjbyBkYSBwcm9iYWJpbGlkYWRlIGRvIGVycm8gZGUgdGlwbyBJICgkXFxhbHBoYSQpIHNlbXByZSByZXN1bHRhIGVtIHVtIGF1bWVudG8gZG8gcG9kZXIgZG8gdGVzdGUgKCQxLVxcYmV0YSQpLiIsICJFIjogIk8gZXJybyBkZSB0aXBvIElJIMOpIGRlZmluaWRvIGNvbW8gJFxcYWxwaGEgPSBQKFxcdGV4dHtyZWplaXRhciB9IEhfMCB8IEhfMCBcXHRleHR7IMOpIGZhbHNhfSkkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiUmV2aXNlIGFzIGRlZmluacOnw7VlcyBmdW5kYW1lbnRhaXMgZGUgZXJybyBkZSBwcmltZWlyYSBlIHNlZ3VuZGEgZXNww6ljaWU6IGVycm8gdGlwbyBJIMOpIGEgJ2ZhbHNhIGFsYXJtZScsIGVucXVhbnRvIG8gZXJybyB0aXBvIElJIMOpIGEgJ2ZhbGhhIGVtIGRldGVjdGFyJy4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgYWx0ZXJuYXRpdmEgQyBkZWZpbmUgY29ycmV0YW1lbnRlIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICgkXFxhbHBoYSQpLCBxdWUgw6kgbyByaXNjbyBtw6F4aW1vIGFjZWl0w6F2ZWwgZGUgY29tZXRlciBvIGVycm8gdGlwbyBJIChyZWplaXRhciAkSF8wJCBlcnJvbmVhbWVudGUpLiBBIGFsdGVybmF0aXZhIEEgY29uZnVuZGUgcG9kZXIgY29tIGVycm8gdGlwbyBJLiBBIEIgZGVzY3JldmUgbyBlcnJvIHRpcG8gSUkuIEEgRCDDqSBpbmNvcnJldGEgcG9pcyBleGlzdGUgdW0gdHJhZGUtb2ZmOiByZWR1emlyICRcXGFscGhhJCBzZW0gYXVtZW50YXIgJG4kIGdlcmFsbWVudGUgcmVkdXogbyBwb2Rlci4gQSBFIGludmVydGUgYSBkZWZpbmnDp8OjbyBkZSAkXFxhbHBoYSQgZSAkXFxiZXRhJC4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzMzgifSwgeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIHV0aWxpemEgdW1hIG3DoXF1aW5hIGNhbGlicmFkYSBwYXJhIHByb2R1emlyIG1pY3JvY2hpcHMgY29tIHVtYSByZXNpc3TDqm5jaWEgw6AgdHJhw6fDo28gbcOpZGlhIGRlICRcXG11ID0gNTAwJCBOLiBDb21vIHBhcnRlIGRvIHByb3RvY29sbyBkZSBjb250cm9sZSBkZSBxdWFsaWRhZGUsIHVtYSBlcXVpcGUgZGUgZW5nZW5oYXJpYSBzdXNwZWl0YSBxdWUgYSBtw6FxdWluYSBlc3RlamEgb3BlcmFuZG8gZm9yYSBkb3MgcGFkcsO1ZXMgZGV2aWRvIGEgdW0gZGVzZ2FzdGUgbm9zIGNvbXBvbmVudGVzIGludGVybm9zLCBwb2RlbmRvIHJlc3VsdGFyIGVtIHVtYSByZXNpc3TDqm5jaWEgbcOpZGlhIG1lbm9yIG91IG1haW9yIHF1ZSBvIHZhbG9yIGRlIHJlZmVyw6puY2lhLiBBbyBjb2xldGFyIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgZGUgJG4gPSAyNSQgY2hpcHMsIGEgZXF1aXBlIGRlY2lkZSByZWFsaXphciB1bSB0ZXN0ZSBkZSBoaXDDs3Rlc2VzIHBhcmEgdmVyaWZpY2FyIGEgY2FsaWJyYcOnw6NvIGRhIG3DoXF1aW5hLiBDb25zaWRlcmFuZG8gbyByaWdvciBtZXRvZG9sw7NnaWNvLCBxdWFsIMOpIGEgZm9ybXVsYcOnw6NvIGFkZXF1YWRhIGRhcyBoaXDDs3Rlc2VzIGUgYSBjYXJhY3RlcsOtc3RpY2EgZGEgcmVnacOjbyBjcsOtdGljYSBwYXJhIGVzdGUgY2Vuw6FyaW8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIkSF8wOiBcXG11ID0gNTAwJCBjb250cmEgJEhfMTogXFxtdSA8IDUwMCQsIGNvbSByZWdpw6NvIGNyw610aWNhIHNpdHVhZGEgbmEgY2F1ZGEgaW5mZXJpb3IgZGEgZGlzdHJpYnVpw6fDo28uIiwgIkIiOiAiJEhfMDogXFxtdSA9IDUwMCQgY29udHJhICRIXzE6IFxcbXUgPiA1MDAkLCBjb20gcmVnacOjbyBjcsOtdGljYSBzaXR1YWRhIG5hIGNhdWRhIHN1cGVyaW9yIGRhIGRpc3RyaWJ1acOnw6NvLiIsICJDIjogIiRIXzA6IFxcbXUgPSA1MDAkIGNvbnRyYSAkSF8xOiBcXG11IFxcbmVxIDUwMCQsIGNvbmZpZ3VyYW5kbyB1bSB0ZXN0ZSBiaWxhdGVyYWwgY29tIGEgcmVnacOjbyBjcsOtdGljYSBkaXN0cmlidcOtZGEgaWd1YWxtZW50ZSBuYXMgZHVhcyBjYXVkYXMuIiwgIkQiOiAiJEhfMDogXFxtdSBcXG5lcSA1MDAkIGNvbnRyYSAkSF8xOiBcXG11ID0gNTAwJCwgY29tIGEgcmVnacOjbyBjcsOtdGljYSBjZW50cmFsaXphZGEgbm8gdmFsb3IgZGEgbcOpZGlhIGFtb3N0cmFsLiIsICJFIjogIiRIXzA6IFxcbXUgPSA1MDAkIGNvbnRyYSAkSF8xOiBcXG11IFxcbmVxIDUwMCQsIGNvbmZpZ3VyYW5kbyB1bSB0ZXN0ZSB1bmlsYXRlcmFsIGRldmlkbyDDoCBpbmNlcnRlemEgc29icmUgbyBkZXNnYXN0ZSBkbyBlcXVpcGFtZW50by4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIlJlZmxpdGEgc2UgYSBzdXNwZWl0YSBkYSBlcXVpcGUgZGUgZW5nZW5oYXJpYSBhcG9udGEgcGFyYSB1bWEgZGlyZcOnw6NvIGVzcGVjw61maWNhIGRvIGRlc3ZpbyBvdSBzZSBxdWFscXVlciBkZXN2aW8gZW0gcmVsYcOnw6NvIGFvIHZhbG9yIG5vbWluYWwgZGUgNTAwIE4gw6kgY29uc2lkZXJhZG8gdW1hIGZhbGhhIG5vIGNvbnRyb2xlIGRlIHF1YWxpZGFkZS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIk5vIGNvbnRleHRvIGFwcmVzZW50YWRvLCBvIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBwcmVjaXNhIGRldGVjdGFyIGRlc3Zpb3MgZGEgZXNwZWNpZmljYcOnw6NvIG5vbWluYWwgKDUwMCBOKSB0YW50byBwYXJhIG1haXMgcXVhbnRvIHBhcmEgbWVub3MuIFF1YW5kbyBvIGludGVyZXNzZSBjaWVudMOtZmljbyBvdSBwcsOhdGljbyBuw6NvIMOpIGRpcmVjaW9uYWwsIGEgYXJxdWl0ZXR1cmEgZG8gdGVzdGUgZXhpZ2UgYSBmb3JtdWxhw6fDo28gZGUgdW1hIGhpcMOzdGVzZSBhbHRlcm5hdGl2YSBiaWxhdGVyYWwgJEhfMTogXFxtdSBcXG5lcSA1MDAkLiBQb3IgY29uc2VxdcOqbmNpYSwgYSByZWdpw6NvIGNyw610aWNhICgkUkMkKSBkZXZlIHNlciBkaXZpZGlkYSBlbnRyZSBhcyBkdWFzIGNhdWRhcyBkYSBkaXN0cmlidWnDp8OjbyBwYXJhIG1hbnRlciBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgZXF1aWxpYnJhZG8sIGdhcmFudGluZG8gdW1hIHBvc3R1cmEgbmV1dHJhIGZyZW50ZSBhIHZhcmlhw6fDtWVzIGVtIGFtYmFzIGFzIGRpcmXDp8O1ZXMuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgtNCwgNCwgMjAwKVxueSA9ICgxIC8gbnAuXFxzcXJ0KDIgKiBucC5cXHBpKSkgKiBucC5cXGV4cCgtMC41ICogeCoqMilcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJywgd2lkdGg9MiksIG5hbWU9J0Rpc3RyaWJ1acOnw6NvICRIXzAkJykpXG4jIFJlZ2nDtWVzIENyw610aWNhcyAoQWxwaGEgPSAwLjA1LCBaY3JpdCA9IDEuOTYpXG5maWcuYWRkX3ZyZWN0KHgwPTEuOTYsIHgxPTQsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTAsIG5hbWU9J1JDIChEaXJlaXRhKScpXG5maWcuYWRkX3ZyZWN0KHgwPS00LCB4MT0tMS45NiwgZmlsbGNvbG9yPScjOTkxQjFCJywgb3BhY2l0eT0wLjMsIGxpbmVfd2lkdGg9MCwgbmFtZT0nUkMgKEVzcXVlcmRhKScpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+QXJxdWl0ZXR1cmEgZGUgVGVzdGUgQmlsYXRlcmFsPC9iPicsIHhheGlzX3RpdGxlPXInRXN0YXTDrXN0aWNhIGRlIFRlc3RlICgkWl97XHRleHR7Y2FsY319JCknLCB5YXhpc190aXRsZT0nRGVuc2lkYWRlJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM0MCJ9LCB7ImVudW5jaWFkbyI6ICJVbSBmYXJtYWPDqnV0aWNvIGRlc2VqYSBhdmFsaWFyIHNlIHVtIG5vdm8gc3VwbGVtZW50byBudXRyaWNpb25hbCBhdW1lbnRhIGEgY29uY2VudHJhw6fDo28gZGUgdml0YW1pbmEgRCBlbSBwYWNpZW50ZXMgcXVlIGFwcmVzZW50YW0gbsOtdmVpcyBiYWl4b3MuIEEgbcOpZGlhIHBvcHVsYWNpb25hbCBlc3BlcmFkYSBhcMOzcyBvIHRyYXRhbWVudG8gZGUgY29udHJvbGUgw6kgZGUgJDMwJCBuZy9tTC4gTyBvYmpldGl2byBkbyBlc3R1ZG8gw6kgdmVyaWZpY2FyLCBjb20gdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhID0gMCwwNSQsIHNlIG8gbm92byBzdXBsZW1lbnRvIHByb3BvcmNpb25hIHVtIGdhbmhvIGRlIHBlcmZvcm1hbmNlIG5hIGNvbmNlbnRyYcOnw6NvIGRhIHZpdGFtaW5hLCBzdXBlcmFuZG8gYSBtw6lkaWEgZGUgY29udHJvbGUuIFF1YWwgZGV2ZSBzZXIgYSBhcnF1aXRldHVyYSBkbyB0ZXN0ZSBhIHNlciBhZG90YWRhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiVGVzdGUgYmlsYXRlcmFsIGNvbSAkSF8xOiBcXG11IFxcbmVxIDMwJCwgcG9pcyDDqSBvIHRlc3RlIG1haXMgY29uc2VydmFkb3IuIiwgIkIiOiAiVGVzdGUgdW5pbGF0ZXJhbCDDoCBkaXJlaXRhIGNvbSAkSF8xOiBcXG11ID4gMzAkLCBkYWRvIHF1ZSBvIGludGVyZXNzZSBkbyBwZXNxdWlzYWRvciDDqSB2ZXJpZmljYXIgZXNwZWNpZmljYW1lbnRlIHVtYSBtZWxob3JhIG5vIGdhbmhvIGRlIGNvbmNlbnRyYcOnw6NvLiIsICJDIjogIlRlc3RlIHVuaWxhdGVyYWwgw6AgZXNxdWVyZGEgY29tICRIXzE6IFxcbXUgPCAzMCQsIHZpc2FuZG8gdGVzdGFyIHNlIG8gc3VwbGVtZW50byDDqSBpbmVmaWNhei4iLCAiRCI6ICJOw6NvIHNlIHBvZGUgcmVhbGl6YXIgdW0gdGVzdGUgZXN0YXTDrXN0aWNvLCBwb2lzIG7Do28gY29uaGVjZW1vcyBvIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbC4iLCAiRSI6ICJUZXN0ZSBiaWxhdGVyYWwgY29tICRIXzE6IFxcbXUgPiAzMCQsIHBvaXMgbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkIHByZWNpc2Egc2VyIGRpc3RyaWJ1w61kbyBwYXJhIGdhcmFudGlyIG1haW9yIHBvZGVyLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTyBlbnVuY2lhZG8gZXNwZWNpZmljYSBxdWUgbyBpbnRlcmVzc2Ugw6kgdmVyaWZpY2FyIHVtICdnYW5obycgb3UgJ3BlcmZvcm1hbmNlIHN1cGVyaW9yJy4gQ29tbyBvIG9iamV0aXZvIMOpIGNsYXJhbWVudGUgZGlyZWNpb25hbCwgYSBiYXJyZWlyYSBkZSBzaWduaWZpY8OibmNpYSBwb2RlIHNlciBhbG9jYWRhIGludGVpcmFtZW50ZSBlbSB1bWEgw7puaWNhIGNhdWRhLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBlc2NvbGhhIGRhIGFycXVpdGV0dXJhIGRvIHRlc3RlIGRldmUgcmVmbGV0aXIgYSBoaXDDs3Rlc2UgZGUgcGVzcXVpc2EuIFF1YW5kbyBvIHBlc3F1aXNhZG9yIHBvc3N1aSB1bSBtb3Rpdm8gZnVuZGFtZW50YWRvIHBhcmEgZXNwZXJhciB1bSBlZmVpdG8gZW0gdW1hIMO6bmljYSBkaXJlw6fDo28gKG5lc3RlIGNhc28sIGF1bWVudG8gb3UgZ2FuaG8pLCBvIHRlc3RlIHVuaWxhdGVyYWwgw6kgYSBmZXJyYW1lbnRhIGRlIHByZWNpc8OjbyBhZGVxdWFkYS4gQW8gZm9ybXVsYXJtb3MgJEhfMTogXFxtdSA+IDMwJCwgY29uY2VudHJhbW9zIHRvZG8gbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLDA1JCBuYSBjYXVkYSBzdXBlcmlvciwgbyBxdWUgYXVtZW50YSBhIHNlbnNpYmlsaWRhZGUgKHBvZGVyKSBkbyB0ZXN0ZSBwYXJhIGRldGVjdGFyIG8gZWZlaXRvIGRlIGF1bWVudG8sIGNhc28gZWxlIGRlIGZhdG8gb2NvcnJhLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM0MiJ9LCB7ImVudW5jaWFkbyI6ICJVbSBsYWJvcmF0w7NyaW8gZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlIG1vbml0b3JhIG8gZGnDom1ldHJvIGRlIGNvbXBvbmVudGVzIGRlIHByZWNpc8Ojby4gTyBwcm9jZXNzbyBhdHVhbCwgcXVhbmRvIHNvYiBjb250cm9sZSwgcHJvZHV6IGNvbXBvbmVudGVzIGNvbSBkacOibWV0cm8gbcOpZGlvICRcXG11ID0gMjAsMCQgbW0gZSBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgY29uaGVjaWRvICRcXHNpZ21hID0gMCw1JCBtbS4gVW1hIGFtb3N0cmEgYWxlYXTDs3JpYSBkZSAkbiA9IDI1JCBjb21wb25lbnRlcyDDqSBjb2xldGFkYS4gQSByZWdyYSBkZSBkZWNpc8OjbyBlc3RhYmVsZWNpZGEgcmVqZWl0YSBhIGhpcMOzdGVzZSBudWxhICRIXzA6IFxcbXUgPSAyMCwwJCBlbSBmYXZvciBkYSBhbHRlcm5hdGl2YSAkSF8xOiBcXG11ID4gMjAsMCQgc2UgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBmb3Igc3VwZXJpb3IgYSAkMjAsMiQgbW0uIFF1YWwgw6kgYSBwcm9iYWJpbGlkYWRlIGRlIGNvbWV0ZXIgbyBFcnJvIFRpcG8gSSAoJFxcYWxwaGEkKSBuZXN0ZSB0ZXN0ZT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjAsMDExNCIsICJCIjogIjAsMDIyOCIsICJDIjogIjAsMDQ1NiIsICJEIjogIjAsMDUwMCIsICJFIjogIjAsMDY2OCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBzb2IgJEhfMCQsIGEgZGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgZGEgbcOpZGlhIMOpICRcXGJhcntYfSBcXHNpbSBOKFxcbXUsIFxcc2lnbWFeMi9uKSQuIENhbGN1bGUgbyBlc2NvcmUgJFokIHBhcmEgbyB2YWxvciBjcsOtdGljbyAkXFxiYXJ7eH1fYyA9IDIwLDIkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUGFyYSBlbmNvbnRyYXIgJFxcYWxwaGEkLCBjYWxjdWxhbW9zIGEgcHJvYmFiaWxpZGFkZSBkZSByZWplaXRhciAkSF8wJCBkYWRvIHF1ZSBlbGEgw6kgdmVyZGFkZWlyYTogJFAoXFxiYXJ7WH0gPiAyMCwyIHwgXG5cXG11ID0gMjAsMCkkLiBPIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgw6kgJEVQKFxcYmFye1h9KSA9IFxcc2lnbWEgLyBcXHNxcnR7bn0gPSAwLDUgLyBcXHNxcnR7MjV9ID0gMCw1IC8gNSA9IDAsMSQuIE8gdmFsb3IgJFpfe2NhbGN9JCDDqTogJCRaX3tjYWxjfSA9IFxcZnJhY3tcXGJhcnt4fV9jIC0gXFxtdX17RVAoXFxiYXJ7WH0pfSA9IFxcZnJhY3syMCwyIC0gMjAsMH17MCwxfSA9IFxcZnJhY3swLDJ9ezAsMX0gPSAyLDAkJC4gQSBwcm9iYWJpbGlkYWRlIGNvcnJlc3BvbmRlbnRlIGEgJFogPiAyLDAkIG5hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBwYWRyw6NvIMOpICQxIC0gUChaIFxcbGUgMiwwKSA9IDEgLSAwLDk3NzIgPSAwLDAyMjgkLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoMTkuNywgMjAuNSwgMTAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgsIDIwLCAwLjEpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9XCJEaXN0cmlidWnDp8OjbyBzb2IgSDBcIiwgbGluZT1kaWN0KGNvbG9yPVwiIzFFM0E4QVwiLCB3aWR0aD0zKSkpXG54X2ZpbGwgPSBucC5saW5zcGFjZSgyMC4yLCAyMC41LCAxMDApXG55X2ZpbGwgPSBzdGF0cy5ub3JtLnBkZih4X2ZpbGwsIDIwLCAwLjEpXG5maWcuYWRkX3RyYWNlKGdvLkZpbGwoeD1ucC5jb25jYXRlbmF0ZShbeF9maWxsLCBbMjAuNSwgMjAuMl1dKSwgeT1ucC5jb25jYXRlbmF0ZShbeV9maWxsLCBbMCwgMF1dKSwgZmlsbD1cInRvc2VsZlwiLCBmaWxsY29sb3I9XCIjOTkxQjFCXCIsIG5hbWU9XCJFcnJvIFRpcG8gSSAozrEpXCIpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9XCI8Yj5EaXN0cmlidWnDp8OjbyBBbW9zdHJhbCBzb2IgSDAgZSBSZWdpw6NvIENyw610aWNhPC9iPlwiLCB4YXhpcz1kaWN0KHRpdGxlPXJcIk3DqWRpYSBBbW9zdHJhbCAoJFxcYmFye1h9JClcIiksIHlheGlzPWRpY3QodGl0bGU9clwiRGVuc2lkYWRlXCIpLCB0ZW1wbGF0ZT1cInBsb3RseV93aGl0ZVwiKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzMzMifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGNsw61uaWNvIHBhcmEgdmVyaWZpY2FyIGEgZWZpY8OhY2lhIGRlIHVtIG5vdm8gZsOhcm1hY28sIGVzdGFiZWxlY2V1LXNlICRIXzA6IFxcbXUgPSA1MCQgKHNlbSBlZmVpdG8pIGNvbnRyYSAkSF8xOiBcXG11IFxcbmVxIDUwJCAoY29tIGVmZWl0bykuIE8gcGVzcXVpc2Fkb3IgZml4b3UgbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgZW0gJFxcYWxwaGEgPSAwLDA1JC4gU2UgbyB0ZXN0ZSBlc3RhdMOtc3RpY28gYXByZXNlbnRhciB1bSBwLXZhbG9yIGRlICQwLDAzJCwgcXVhbCDDqSBhIGNvbmNsdXPDo28gY29ycmV0YSBlIG8gcmlzY28gYXNzb2NpYWRvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiUmVqZWl0YS1zZSAkSF8wJCwgY29tIHJpc2NvIGRlIGNvbWV0ZXIgRXJybyBUaXBvIElJIGlndWFsIGEgMyUuIiwgIkIiOiAiTsOjbyBzZSByZWplaXRhICRIXzAkLCBjb20gcmlzY28gZGUgY29tZXRlciBFcnJvIFRpcG8gSSBpZ3VhbCBhIDMlLiIsICJDIjogIlJlamVpdGEtc2UgJEhfMCQsIHBvaXMgbyBwLXZhbG9yIMOpIG1lbm9yIHF1ZSBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSwgaW5jb3JyZW5kbyBubyByaXNjbyBkZSBFcnJvIFRpcG8gSSBkZWZpbmlkbyBwb3IgJFxcYWxwaGEkLiIsICJEIjogIk7Do28gc2UgcmVqZWl0YSAkSF8wJCwgcG9pcyBvIGVycm8gdGlwbyBJSSBmb2kgY29udHJvbGFkbyBlbSAwLDAzLiIsICJFIjogIk8gcmVzdWx0YWRvIMOpIGluY29uY2x1c2l2bywgcG9pcyBvIHAtdmFsb3IgZGV2ZXJpYSBzZXIgZXhhdGFtZW50ZSAwLDA1LiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiTyBwLXZhbG9yIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSBvYnNlcnZhciB1bSByZXN1bHRhZG8gdMOjbyBleHRyZW1vIHF1YW50byBvIG9idGlkbywgYXNzdW1pbmRvIHF1ZSAkSF8wJCBzZWphIHZlcmRhZGVpcmEuIFNlICRwXFx0ZXh0ey12YWxvcn0gPCBcXGFscGhhJCwgcmVqZWl0YW1vcyBhIGhpcMOzdGVzZSBudWxhLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBwLXZhbG9yIGRlIDAsMDMgw6kgbWVub3IgcXVlIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhID0gMCwwNSQuIElzc28gc2lnbmlmaWNhIHF1ZSBhIGV2aWTDqm5jaWEgYW1vc3RyYWwgw6kgZm9ydGUgbyBzdWZpY2llbnRlIHBhcmEgcmVqZWl0YXIgYSBoaXDDs3Rlc2UgbnVsYS4gQW8gcmVqZWl0YXIgJEhfMCQgcXVhbmRvIGVsYSDDqSB2ZXJkYWRlaXJhLCBjb21ldGVtb3MgbyBFcnJvIFRpcG8gSSwgY3VqYSBwcm9iYWJpbGlkYWRlIG3DoXhpbWEgYWNlaXTDoXZlbCBmb2kgZml4YWRhIGVtICRcXGFscGhhPTAsMDUkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW1hIGbDoWJyaWNhIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyB1dGlsaXphIHVtIHNlbnNvciBkZSBwcmVjaXPDo28gcXVlIGRldmUgb3BlcmFyIGNvbSB1bWEgbcOpZGlhIGRlIGVtaXNzw6NvIGRlIHNpbmFsIGRlICRcXG11XzAgPSA1MDAkIHVuaWRhZGVzLiBQYXJhIGdhcmFudGlyIGEgY2FsaWJyYcOnw6NvLCBvIGVuZ2VuaGVpcm8gZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlIGNvbGV0YSB1bWEgYW1vc3RyYSBkZSAkbiA9IDEwMCQgY29tcG9uZW50ZXMgZSBkZXNlamEgdGVzdGFyIHNlIG8gcHJvY2Vzc28gZXN0w6Egc29iIGNvbnRyb2xlIG91IHNlIGhvdXZlIHVtIGRlc3ZpbyBzaWduaWZpY2F0aXZvIChzZWphIHBhcmEgbWFpcyBvdSBwYXJhIG1lbm9zKS4gTyBwcm9jZWRpbWVudG8gc2lzdGVtw6F0aWNvIHNlZ3VlIGFzIDUgZXRhcGFzIHByb3RvY29sYXJlcy4gQW8gZml4YXIgbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLDA1JCBlIGRlZmluaXIgYSBlc3RhdMOtc3RpY2EgZGUgdGVzdGUgY29tbyBvIHZhbG9yICRaJCBwYWRyb25pemFkbywgcXVhbCBkYXMgYWx0ZXJuYXRpdmFzIGFiYWl4byBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgYSBsw7NnaWNhIGRhIGV0YXBhIDMgKEZpeGHDp8OjbyBkYSBSZWdpw6NvIENyw610aWNhKSBwYXJhIGVzdGUgdGVzdGUgYmlsYXRlcmFsPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBSZWdpw6NvIENyw610aWNhICgkUkMkKSDDqSBkZWZpbmlkYSBjb21vIHRvZG9zIG9zIHZhbG9yZXMgZGUgJFpfe1xcdGV4dHtjYWxjfX0kIG9uZGUgbyBwLXZhbG9yIMOpIHN1cGVyaW9yIGEgJDAsMDUkLiIsICJCIjogIkEgUmVnacOjbyBDcsOtdGljYSAoJFJDJCkgw6kgY29tcG9zdGEgcGVsb3MgdmFsb3JlcyBkZSAkWl97XFx0ZXh0e2NhbGN9fSQgdGFpcyBxdWUgJHxaX3tcXHRleHR7Y2FsY319fCA+IDEsOTYkLCBvbmRlICQxLDk2JCDDqSBvIHZhbG9yIGNyw610aWNvIHBhcmEgJFxcYWxwaGEgPSAwLDA1JCBlbSB1bSB0ZXN0ZSBiaWxhdGVyYWwuIiwgIkMiOiAiQSBSZWdpw6NvIENyw610aWNhICgkUkMkKSDDqSBmaXhhZGEgYXBlbmFzIG5hIGNhdWRhIGRpcmVpdGEgZGEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLCBwb2lzIGEgdmFyacOibmNpYSDDqSBjb25oZWNpZGEuIiwgIkQiOiAiTyB2YWxvciBjcsOtdGljbyDDqSBkZWZpbmlkbyBwZWxhIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0kLCBkZSBtb2RvIHF1ZSAkUkMgPSBcXHsgXFxiYXJ7WH0gOiBcXGJhcntYfSA8IDUwMCBcXH0kLiIsICJFIjogIkEgUmVnacOjbyBDcsOtdGljYSAoJFJDJCkgw6kgZGVmaW5pZGEgZGUgbW9kbyBxdWUgYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIHF1YW5kbyBlbGEgw6kgZmFsc2Egc2VqYSBleGF0YW1lbnRlICQwLDA1JC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgZW0gdW0gdGVzdGUgYmlsYXRlcmFsLCBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgw6kgZGlzdHJpYnXDrWRvIGlndWFsbWVudGUgZW50cmUgYXMgZHVhcyBjYXVkYXMgZGEgZGlzdHJpYnVpw6fDo28gZGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBhbHRlcm5hdGl2YSBCIMOpIGEgY29ycmV0YSBwb2lzIHNlZ3VlIGVzdHJpdGFtZW50ZSBhIGV0YXBhIDMgZG8gcHJvY2VkaW1lbnRvIHNpc3RlbcOhdGljby4gRW0gdW0gdGVzdGUgYmlsYXRlcmFsIGNvbSAkXFxhbHBoYSA9IDAsMDUkLCBkaXZpZGltb3MgYSBwcm9iYWJpbGlkYWRlIGRlIGVycm8gdGlwbyBJIHBlbGFzIGR1YXMgZXh0cmVtaWRhZGVzIGRhIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCBwYWRyw6NvICROKDAsMSkkLCByZXN1bHRhbmRvIGVtICQwLDAyNSQgZW0gY2FkYSBjYXVkYS4gTyB2YWxvciBjcsOtdGljbyAkWl97XFx0ZXh0e2NyaXR9fSQgcXVlIGRlaXhhICQwLDAyNSQgbmEgY2F1ZGEgc3VwZXJpb3Igw6kgJDEsOTYkLiBQb3J0YW50bywgYSByZWdpw6NvIGRlIHJlamVpw6fDo28gKCRSQyQpIMOpIGRlZmluaWRhIHBlbG8gY29uanVudG8gZGUgdmFsb3JlcyBvbmRlIGEgZXZpZMOqbmNpYSBhbW9zdHJhbCDDqSB0w6NvIGV4dHJlbWEgcXVlICR8Wl97XFx0ZXh0e2NhbGN9fXwgPiAxLDk2JC4gQXMgb3V0cmFzIGFsdGVybmF0aXZhcyBmYWxoYW0gbmEgZGVmaW5pw6fDo28gdMOpY25pY2EgZGUgcmVnacOjbyBjcsOtdGljYSBvdSBubyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgYXBsaWNhZG8uIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgtNCwgNCwgMTAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgsIDAsIDEpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTIpLCBuYW1lPSdEZW5zaWRhZGUgTigwLDEpJykpXG5yY194ID0gbnAubGluc3BhY2UoMS45NiwgNCwgNTApXG5maWcuYWRkX3RyYWNlKGdvLkZpbGwoeD1ucC5jb25jYXRlbmF0ZShbcmNfeCwgcmNfeFs6Oi0xXV0pLCB5PW5wLmNvbmNhdGVuYXRlKFtzdGF0cy5ub3JtLnBkZihyY194LCAwLCAxKSwgbnAuemVyb3NfbGlrZShyY194KV0pLCBmaWxsY29sb3I9JyM5OTFCMUInLCBuYW1lPSdSQyAoRGlyZWl0YSknLCBvcGFjaXR5PTAuNSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+UmVnacOjbyBDcsOtdGljYSBwYXJhIFotdGVzdGUgKEJpbGF0ZXJhbCk8L2I+JywgeGF4aXM9ZGljdCh0aXRsZT1yJyRaX3tcXHRleHR7Y2FsY319JCcpLCB5YXhpcz1kaWN0KHRpdGxlPSdEZW5zaWRhZGUnKSwgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiTm8gY29udGV4dG8gZGEgY29uc3RydcOnw6NvIGRlIHRlc3RlcyBkZSBoaXDDs3Rlc2VzLCBvIHByb2NlZGltZW50byBzaXN0ZW3DoXRpY28gZXhpZ2UgcXVlLCBhbyBjb25jbHVpciBhIEV0YXBhIDUgKFJlZ3JhIGRlIERlY2lzw6NvKSwgbyBwZXNxdWlzYWRvciBjb21wYXJlIGEgZXN0YXTDrXN0aWNhIGNhbGN1bGFkYSBjb20gb3MgdmFsb3JlcyBjcsOtdGljb3MuIFN1cG9uaGEgcXVlLCBwYXJhIHVtIHRlc3RlIGRlIGhpcMOzdGVzZSB1bmlsYXRlcmFsIGNvbSAkSF8xOiBcXHRoZXRhID4gXFx0aGV0YV8wJCwgbyBwZXNxdWlzYWRvciB0ZW5oYSBjYWxjdWxhZG8gdW1hIGVzdGF0w61zdGljYSAkWl97XFx0ZXh0e2NhbGN9fSA9IDEsNjgkIGUgbyB2YWxvciBjcsOtdGljbyBwYXJhICRcXGFscGhhID0gMCwwNSQgc2VqYSAkWl97XFx0ZXh0e2NyaXR9fSA9IDEsNjQ1JC4gUXVhbCBkZXZlIHNlciBhIGNvbmR1dGEgY29ycmV0YSBkbyBwZXNxdWlzYWRvciBzZWd1aW5kbyBvIHByb3RvY29sbyBlc3RhdMOtc3RpY28/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJOw6NvIHJlamVpdGFyICRIXzAkLCBwb2lzIG8gdmFsb3IgY2FsY3VsYWRvIMOpIG11aXRvIHByw7N4aW1vIGRvIGNyw610aWNvLCBpbmRpY2FuZG8gaW5jZXJ0ZXphLiIsICJCIjogIlJlamVpdGFyICRIXzAkLCBwb2lzICRaX3tcXHRleHR7Y2FsY319IFxcaW4gUkMkLCBvIHF1ZSBzaWduaWZpY2EgcXVlIGEgZXZpZMOqbmNpYSBhbW9zdHJhbCDDqSBlc3RhdGlzdGljYW1lbnRlIGluY29tcGF0w612ZWwgY29tICRIXzAkIGFvIG7DrXZlbCBkZSAkNVxcJSQuIiwgIkMiOiAiUmVmYXplciBhIGNvbGV0YSBkZSBkYWRvcywgcG9pcyBvIHRlc3RlIG7Do28gZm9pIGNvbmNsdXNpdm8uIiwgIkQiOiAiQWNlaXRhciAkSF8wJCBjb21vIHZlcmRhZGVpcmEsIHVtYSB2ZXogcXVlICRaX3tcXHRleHR7Y2FsY319JCDDqSBtYWlvciBxdWUgJDAkLiIsICJFIjogIlJlZHV6aXIgbyB2YWxvciBkZSAkXFxhbHBoYSQgcGFyYSAkMCwwMSQgcGFyYSB0b3JuYXIgbyB0ZXN0ZSBtYWlzIHJpZ29yb3NvIGUgY29uZmlybWFyIGEgcmVqZWnDp8Ojby4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk8gcHJvY2VkaW1lbnRvIHNpc3RlbcOhdGljbyDDqSByw61naWRvOiBzZSBhIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSBjYWkgZGVudHJvIGRhIHJlZ2nDo28gY3LDrXRpY2EsIG8gcHJvdG9jb2xvIGRpdGEgYSByZWplacOnw6NvIGRlICRIXzAkIGluZGVwZW5kZW50ZW1lbnRlIGRhIHByb3hpbWlkYWRlIG51bcOpcmljYSBjb20gbyB2YWxvciBjcsOtdGljby4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgZXRhcGEgNSDDqSBjbGFyYTogc2UgJFxcaGF0e1xcdGhldGF9X3tcXHRleHR7Y2FsY319IFxcaW4gUkMkLCByZWplaXRhbW9zICRIXzAkLiBObyBjYXNvIGFwcmVzZW50YWRvLCBjb21vICRaX3tcXHRleHR7Y2FsY319ID0gMSw2OCQgZSAkWl97XFx0ZXh0e2NyaXR9fSA9IDEsNjQ1JCwgdGVtb3MgcXVlICQxLDY4ID4gMSw2NDUkLCBwb3J0YW50byBvIHZhbG9yIGNhbGN1bGFkbyBwZXJ0ZW5jZSDDoCBSZWdpw6NvIENyw610aWNhLiBTZWd1aW5kbyBhIG1ldG9kb2xvZ2lhIGNpZW50w61maWNhIG9iamV0aXZhLCBkZXZlbW9zIHJlamVpdGFyIGEgaGlww7N0ZXNlIG51bGEgJEhfMCQuIE7Do28gaMOhIG1hcmdlbSBwYXJhIGludGVycHJldGHDp8O1ZXMgc3ViamV0aXZhcyBzb2JyZSAncHJveGltaWRhZGUnIG91ICdpbmNlcnRlemEnOyBvIGNyaXTDqXJpbyBmb2kgZGVmaW5pZG8gcHJldmlhbWVudGUgbmEgZXRhcGEgMy4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH1dLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgbWV0YWzDunJnaWNhIG1vbml0b3JhIG8gbsO6bWVybyBkZSBob3JhcyBwZXJkaWRhcyBwb3IgYWNpZGVudGVzLCBjb20gbcOpZGlhIGhpc3TDs3JpY2EgZGUgNjAgaG9yYXMvYW5vIGUgZGVzdmlvIHBhZHLDo28gZGUgMjAgaG9yYXMvYW5vLiBBcMOzcyB1bSBwcm9ncmFtYSBkZSBwcmV2ZW7Dp8OjbywgdW1hIGFtb3N0cmEgZGUgJG4gPSA5JCBpbmTDunN0cmlhcyBhcHJlc2VudG91IHVtYSBtw6lkaWEgZGUgNTAgaG9yYXMvYW5vLiBUZXN0ZSwgY29tIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSA9IDVcXCUkLCBzZSBow6EgZXZpZMOqbmNpYSBkZSBtZWxob3JpYSAocmVkdcOnw6NvIGRhIG3DqWRpYSkuIERlZmluYSAkSF8wJCBlICRIXzEkLCBlIGNhbGN1bGUgYSAkWl97Y2FsY30kLiIsICJkaWNhIjogIkNvbW8gbyBpbnRlcmVzc2Ugw6kgdmVyaWZpY2FyICdtZWxob3JpYScsIHV0aWxpemUgdW0gdGVzdGUgdW5pbGF0ZXJhbC4gTGVtYnJlLXNlIGRlIHV0aWxpemFyIGEgZsOzcm11bGEgJFpfe2NhbGN9ID0gKFxcYmFye1h9IC0gXFxtdV8wKSAvIChcXHNpZ21hIC8gXFxzcXJ0e259KSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IERlZmluaXIgaGlww7N0ZXNlcy4gJEhfMDogXFxtdSA9IDYwJCB2cyAkSF8xOiBcXG11IDwgNjAkLiIsICJQYXNzbyAyOiBDYWxjdWxhciBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgJEVQKFxcYmFye1h9KSA9IDIwIC8gXFxzcXJ0ezl9ID0gMjAvMyBcXGFwcHJveCA2LDY3JC4iLCAiUGFzc28gMzogQ2FsY3VsYXIgYSBlc3RhdMOtc3RpY2EgZGUgdGVzdGUgJFpfe2NhbGN9ID0gKDUwIC0gNjApIC8gNiw2NyA9IC0xMCAvIDYsNjcgPSAtMSw1JC4iLCAiUGFzc28gNDogRGV0ZXJtaW5hciBvIHZhbG9yIGNyw610aWNvIHBhcmEgJFxcYWxwaGEgPSAwLDA1JCAodW5pbGF0ZXJhbCDDoCBlc3F1ZXJkYSk6ICRaX3tjcml0fSA9IC0xLDY0NSQuIiwgIlBhc3NvIDU6IENvbmNsdXPDo286IENvbW8gJC0xLDUgPiAtMSw2NDUkLCBhIGVzdGF0w61zdGljYSBjYWxjdWxhZGEgbsOjbyBjYWkgbmEgJFJDJC4gTsOjbyByZWplaXRhbW9zICRIXzAkLiBOw6NvIGjDoSBldmlkw6puY2lhIGVzdGF0w61zdGljYSBkZSBtZWxob3JpYSBhbyBuw612ZWwgZGUgNSUuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTMsIDMsIDEwMClcbnkgPSBzdGF0cy5ub3JtLnBkZih4LCAwLCAxKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBuYW1lPSdOKDAsMSknLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnKSkpXG5maWcuYWRkX3ZsaW5lKHg9LTEuNjQ1LCBsaW5lX2Rhc2g9J2Rhc2gnLCBsaW5lX2NvbG9yPScjOTkxQjFCJywgbmFtZT0nWl97Y3JpdH0gKC0xLDY0NSknKVxuZmlnLmFkZF92bGluZSh4PS0xLjUsIGxpbmVfZGFzaD0nc29saWQnLCBsaW5lX2NvbG9yPScjMTBCOTgxJywgbmFtZT0nWl97Y2FsY30gKC0xLDUpJylcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5EaXN0cmlidWnDp8OjbyBOb3JtYWwgUGFkcsOjbyBlIFRlc3RlIFVuaWxhdGVyYWw8L2I+JywgeGF4aXNfdGl0bGU9J0VzdGF0w61zdGljYSBaJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM1MyAoYWRhcHRhZG8gZG8gUHJvYmwuIDcpIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogLTEuNX0sIHsiZW51bmNpYWRvIjogIlVtYSBmw6FicmljYSBhZmlybWEgcXVlIDkwJSBkb3Mgc2V1cyBlcXVpcGFtZW50b3MgZXN0w6NvIGRlIGFjb3JkbyBjb20gYXMgZXNwZWNpZmljYcOnw7Vlcy4gRW0gdW1hIGFtb3N0cmEgZGUgJG4gPSAyMDAkIHBlw6dhcywgZm9yYW0gZW5jb250cmFkYXMgMjUgZGVmZWl0dW9zYXMuIFRlc3RlIGEgaGlww7N0ZXNlIGRvIGZhYnJpY2FudGUgY29tICRcXGFscGhhID0gNVxcJSQuIFF1YWwgw6kgbyB2YWxvciBkYSBwcm9wb3LDp8OjbyBhbW9zdHJhbCAkXFxoYXR7cH0kIGUgYSBjb25jbHVzw6NvIGRvIHRlc3RlPyIsICJkaWNhIjogIkNhbGN1bGUgJFxcaGF0e3B9ID0gWC9uJC4gVXNlIGEgbm9ybWFsIHBhcmEgYXByb3hpbWHDp8OjbyBkYSBiaW5vbWlhbDogJFpfe2NhbGN9ID0gKFxcaGF0e3B9IC0gcF8wKSAvIFxcc3FydHtwXzAoMS1wXzApL259JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogSGlww7N0ZXNlcy4gJEhfMDogcCA9IDAsOTAkIHZzICRIXzE6IHAgXFxuZXEgMCw5MCQuIiwgIlBhc3NvIDI6IFByb3BvcsOnw6NvIGFtb3N0cmFsOiAkbj0yMDAkLCBkZWZlaXRvcz0yNSwgbG9nbyBzdWNlc3NvcyAoY29uZm9ybWVzKT0xNzUuICRcXGhhdHtwfSA9IDE3NS8yMDAgPSAwLDg3NSQuIiwgIlBhc3NvIDM6IEVycm8gcGFkcsOjbyAkRVAoXFxoYXR7cH0pID0gXFxzcXJ0ezAsOTAgXFxjZG90IDAsMTAgLyAyMDB9ID0gXFxzcXJ0ezAsMDkgLyAyMDB9ID0gXFxzcXJ0ezAsMDAwNDV9IFxcYXBwcm94IDAsMDIxMiQuIiwgIlBhc3NvIDQ6ICRaX3tjYWxjfSA9ICgwLDg3NSAtIDAsOTApIC8gMCwwMjEyID0gLTAsMDI1IC8gMCwwMjEyIFxcYXBwcm94IC0xLDE4JC4iLCAiUGFzc28gNTogQ29uY2x1c8OjbzogVmFsb3IgY3LDrXRpY28gcGFyYSAkXFxhbHBoYSA9IDAsMDUkIGJpbGF0ZXJhbCDDqSAkXFxwbSAxLDk2JC4gQ29tbyAkfC0xLDE4fCA8IDEsOTYkLCBuw6NvIHJlamVpdGFtb3MgJEhfMCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM0MSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuODc1fSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIGVtIHRlcm1vcyBjb25jZWl0dWFpcyBlIHNlbSBjw6FsY3Vsb3MgbnVtw6lyaWNvcywgbyBxdWUgc2lnbmlmaWNhIG8gcC12YWxvciBlbSB1bSB0ZXN0ZSBkZSBoaXDDs3Rlc2VzLiBDb21vIGVsZSBhdXhpbGlhIG8gcGVzcXVpc2Fkb3IgYSB0b21hciB1bWEgZGVjaXPDo28gZXN0YXTDrXN0aWNhIGFvIGNvbXBhcmFyIGNvbSBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgcHLDqS1maXhhZG8/IiwgImRpY2EiOiAiTyBwLXZhbG9yIMOpIGEgJ3Byb2JhYmlsaWRhZGUgZGUgc2lnbmlmaWPDom5jaWEgb2JzZXJ2YWRhJy4gRWxlIHF1YW50aWZpY2EgYSBmb3LDp2EgZGEgZXZpZMOqbmNpYSBjb250cmEgJEhfMCQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkRlZmluacOnw6NvOiBPIHAtdmFsb3Igw6kgYSBwcm9iYWJpbGlkYWRlIGRlIG9idGVyIHVtYSBlc3RhdMOtc3RpY2EgZGUgdGVzdGUgdMOjbyBvdSBtYWlzIGV4dHJlbWEgZG8gcXVlIGEgb2JzZXJ2YWRhLCBhc3N1bWluZG8gcXVlIGEgaGlww7N0ZXNlIG51bGEgKCRIXzAkKSDDqSB2ZXJkYWRlaXJhLiIsICJJbnRlcnByZXRhw6fDo286IMOJIHVtYSBtZWRpZGEgZGEgY29tcGF0aWJpbGlkYWRlIGVudHJlIG9zIGRhZG9zIGFtb3N0cmFpcyBlIGEgaGlww7N0ZXNlIG51bGEuIiwgIlJlZ3JhIGRlIERlY2lzw6NvOiBTZSBvIHAtdmFsb3IgZm9yIG1lbm9yIG91IGlndWFsIGFvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgZml4YWRvIHBlbG8gcGVzcXVpc2Fkb3IsIHRlbW9zIGV2aWTDqm5jaWEgc3VmaWNpZW50ZSBwYXJhIHJlamVpdGFyICRIXzAkIChvcyBkYWRvcyBzw6NvIGNvbnNpZGVyYWRvcyBtdWl0byBpbXByb3bDoXZlaXMgc29iICRIXzAkKS4iLCAiVmFudGFnZW06IE8gdXNvIGRvIHAtdmFsb3IgcGVybWl0ZSBxdWUgbyBwZXNxdWlzYWRvciBzYWliYSBxdcOjbyBmb3J0ZSDDqSBhIGV2aWTDqm5jaWEsIHNlbSBhIHJpZ2lkZXogZGUgdW0gdmFsb3IgY3LDrXRpY28gZml4by4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiwgcC4gMzQ3IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBvIHRlc3RlIGRlIGhpcMOzdGVzZSBwYXJhIGEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQgZGUgdW1hIHZhcmnDoXZlbCBhbGVhdMOzcmlhIG5vcm1hbG1lbnRlIGRpc3RyaWJ1w61kYSAkTihcXG11LCBcXHNpZ21hXjIpJCBjb20gJFxcc2lnbWEkIGNvbmhlY2lkby4gRGVzY3JldmEgYSBsw7NnaWNhIG1hdGVtw6F0aWNhIHBhcmEgYSBjb25zdHJ1w6fDo28gZGEgUmVnacOjbyBDcsOtdGljYSAoJFJDJCkgZW0gdW0gdGVzdGUgdW5pbGF0ZXJhbCDDoCBlc3F1ZXJkYSwgb25kZSAkSF8wOiBcXG11ID0gXFxtdV8wJCBlICRIXzE6IFxcbXUgPCBcXG11XzAkLiBDb21vIGEgZXNjb2xoYSBkbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkIGltcGFjdGEgYSBsb2NhbGl6YcOnw6NvIGRvIHZhbG9yIGNyw610aWNvPyIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgZW0gdW0gdGVzdGUgdW5pbGF0ZXJhbCwgYWxvY2Ftb3MgdG9kbyBvIHZhbG9yIGRlICRcXGFscGhhJCBuYSBjYXVkYSByZWxldmFudGUuIFBlbnNlIG5hIGRpc3RyaWJ1acOnw6NvIGRlIHByb2JhYmlsaWRhZGUgZGUgJFxcYmFye1h9JCBzb2IgYSBoaXDDs3Rlc2UgbnVsYS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gU29iICRIXzAkLCBhIG3DqWRpYSBhbW9zdHJhbCB0ZW0gZGlzdHJpYnVpw6fDo28gJFxcYmFye1h9IFxcc2ltIE4oXFxtdV8wLCBcXGZyYWN7XFxzaWdtYV4yfXtufSkkLiIsICIyLiBQYWRyb25pemFtb3MgYSBlc3RhdMOtc3RpY2EgZGUgdGVzdGU6ICRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdV8wfXtcXHNpZ21hIC8gXFxzcXJ0e259fSQuIiwgIjMuIEVtIHVtIHRlc3RlIHVuaWxhdGVyYWwgw6AgZXNxdWVyZGEsIHJlamVpdGFtb3MgJEhfMCQgcXVhbmRvICRaX3tcXHRleHR7Y2FsY319IDwgLVpfe1xcdGV4dHtjcml0fX0kLiIsICI0LiBPIHZhbG9yIGNyw610aWNvICQtWl97XFx0ZXh0e2NyaXR9fSQgw6kgYXF1ZWxlIHF1ZSBkZWl4YSB1bWEgcHJvYmFiaWxpZGFkZSBhY3VtdWxhZGEgJFxcYWxwaGEkIG5hIGNhdWRhIGluZmVyaW9yLCB0YWwgcXVlICRQKFogPCAtWl97XFx0ZXh0e2NyaXR9fSkgPSBcXGFscGhhJC4iLCAiNS4gQ29uc2VxdWVudGVtZW50ZSwgYSAkUkMkIMOpIGRlZmluaWRhIHBlbG8gaW50ZXJ2YWxvICQoLVxcaW5mdHksIC1aX3tcXHRleHR7Y3JpdH19XSQgcGFyYSBhIGVzdGF0w61zdGljYSBwYWRyb25pemFkYS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiwgcC4gMzM1IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtYSBlbXByZXNhIGRlIG1hbnVmYXR1cmEgcHJvZHV6IGNhYm9zIG1ldMOhbGljb3MgY29tIHVtYSByZXNpc3TDqm5jaWEgbcOpZGlhIGRlICQyNTAkIGtnL2NtwrIuIERldmlkbyBhIHVtYSBhbHRlcmHDp8OjbyBubyBwcm9jZXNzbywgbyBlbmdlbmhlaXJvIGRlIHByb2R1w6fDo28gcXVlciB2ZXJpZmljYXIgc2UgYSByZXNpc3TDqm5jaWEgbXVkb3UuIEEgYW1vc3RyYSBkZSAkbiA9IDM2JCBjYWJvcyBhcHJlc2VudG91IHVtYSBtw6lkaWEgJFxcYmFye1h9ID0gMjQ1JCBrZy9jbcKyLiBTYWJlLXNlIHF1ZSAkXFxzaWdtYSA9IDE4JCBrZy9jbcKyLiBUZXN0ZSBhIGhpcMOzdGVzZSAkSF8wOiBcXG11ID0gMjUwJCBjb250cmEgJEhfMTogXFxtdSBcXG5lcSAyNTAkIGFvIG7DrXZlbCBkZSAkXFxhbHBoYSA9IDAsMDUkLiBDYWxjdWxlIG8gdmFsb3IgZGEgZXN0YXTDrXN0aWNhICRaX3tcXHRleHR7Y2FsY319JCBlIHRvbWUgYSBkZWNpc8Ojby4iLCAiZGljYSI6ICJVc2UgYSBmw7NybXVsYSBkbyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhICRFUChcXGJhcntYfSkgPSBcXHNpZ21hIC8gXFxzcXJ0e259JCBlIGNhbGN1bGUgbyB2YWxvciBaIHBhZHJvbml6YWRvLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBJZGVudGlmaWNhw6fDo28gZG9zIHBhcsOibWV0cm9zOiAkXFxtdV8wID0gMjUwJCwgJFxcYmFye3h9ID0gMjQ1JCwgJFxcc2lnbWEgPSAxOCQsICRuID0gMzYkLiIsICIyLiBFcnJvIHBhZHLDo28gZGEgbcOpZGlhOiAkRVAoXFxiYXJ7WH0pID0gXFxmcmFjezE4fXtcXHNxcnR7MzZ9fSA9IFxcZnJhY3sxOH17Nn0gPSAzLjAkLiIsICIzLiBDw6FsY3VsbyBkYSBlc3RhdMOtc3RpY2E6ICRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFjezI0NSAtIDI1MH17My4wfSA9IFxcZnJhY3stNX17M30gXFxhcHByb3ggLTEuNjY3JC4iLCAiNC4gUmVnacOjbyBjcsOtdGljYSBwYXJhICRcXGFscGhhID0gMC4wNSQgKGJpbGF0ZXJhbCk6ICRaX3tcXHRleHR7Y3JpdH19ID0gXFxwbSAxLjk2JC4iLCAiNS4gQ29uY2x1c8OjbzogQ29tbyAkfC0xLjY2N3wgPCAxLjk2JCwgbsOjbyByZWplaXRhbW9zICRIXzAkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNDAiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAtMS42Njd9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSBhIGRpZmVyZW7Dp2EgY29uY2VpdHVhbCBlIHByw6F0aWNhIGVudHJlIG8gcG9kZXIgZGUgdW0gdGVzdGUgZXN0YXTDrXN0aWNvIGVtIGZvcm11bGHDp8O1ZXMgdW5pbGF0ZXJhaXMgZSBiaWxhdGVyYWlzLiBQb3IgcXVlIHVtIHRlc3RlIHVuaWxhdGVyYWwgcG9kZSBzZXIgY29uc2lkZXJhZG8gdW1hICdmZXJyYW1lbnRhIGRlIHByZWNpc8OjbycgZW0gY29tcGFyYcOnw6NvIGNvbSB1bSB0ZXN0ZSBiaWxhdGVyYWwgZW0gZXN0dWRvcyBkZSBlZmljw6FjaWEgY2zDrW5pY2E/IiwgImRpY2EiOiAiQ29uc2lkZXJlIG8gY29uY2VpdG8gZGUgYWxvY2HDp8OjbyBkZSAkXFxhbHBoYSQgZSBhIGJhcnJlaXJhIGRlIHNpZ25pZmljw6JuY2lhIGltcG9zdGEgcGVsYSByZWdpw6NvIGRlIHJlamVpw6fDo28uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIE5vIHRlc3RlIGJpbGF0ZXJhbCwgbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkIMOpIGRpdmlkaWRvLCBzZW5kbyAkXFxhbHBoYS8yJCBwYXJhIGNhZGEgY2F1ZGEsIG8gcXVlIHRvcm5hIG1haXMgZGlmw61jaWwgYSByZWplacOnw6NvIGRlICRIXzAkIHBhcmEgdW0gdmFsb3IgZXh0cmVtbyBlbSB1bWEgw7puaWNhIGRpcmXDp8Ojby4iLCAiMi4gTm8gdGVzdGUgdW5pbGF0ZXJhbCwgbyBuw612ZWwgJFxcYWxwaGEkIMOpIGludGVncmFsbWVudGUgYWxvY2FkbyBlbSB1bWEgZGFzIGNhdWRhcywgbyBxdWUgcmVkdXogbyB2YWxvciBkbyBxdWFudGlsIGNyw610aWNvIChtYWlzIHByw7N4aW1vIGRlIDApLiIsICIzLiBDb25zZXF1ZW50ZW1lbnRlLCBhIHJlZ2nDo28gZGUgcmVqZWnDp8OjbyB0b3JuYS1zZSBtYWlzIGFtcGxhIG5hIGRpcmXDp8OjbyBkZSBpbnRlcmVzc2UsIGF1bWVudGFuZG8gYSBwcm9iYWJpbGlkYWRlIGRlIGRldGVjdGFyIGVmZWl0b3MgcmVhaXMgKHBvZGVyIGRvIHRlc3RlKS4iLCAiNC4gRW0gZW5zYWlvcyBjbMOtbmljb3MsIHF1YW5kbyBzZSBlc3BlcmEgcXVlIG8gZsOhcm1hY28gYXBlbmFzIGF1bWVudGUgbyBlZmVpdG8sIHV0aWxpemFyIHVtIHRlc3RlIHVuaWxhdGVyYWwgw6kgbWFpcyBlZmljaWVudGUsIHBvaXMgbsOjbyBzZSBkZXNwZXJkacOnYSBjYXBhY2lkYWRlIGRlIGRldGVjw6fDo28gJ2ludmVzdGlnYW5kbycgdW1hIHJlZHXDp8OjbyBxdWUgbsOjbyDDqSBjbGluaWNhbWVudGUgZXNwZXJhZGEuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM0MyIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyB0ZXN0ZSBkZSBoaXDDs3Rlc2UgcGFyYSBhIG3DqWRpYSBkZSB1bWEgcG9wdWxhw6fDo28gJE4oXFxtdSwgMTAwKSQgY29tICRuPTI1JCBlICRIXzA6IFxcbXUgPSAxMDAkIGNvbnRyYSAkSF8xOiBcXG11ID0gMTA1JC4gQSByZWdpw6NvIGNyw610aWNhIGRlZmluaWRhIMOpICRSQyA9IFxce1xcYmFye1h9IFxcZ2UgMTAzLDI5XFx9JC4gQ2FsY3VsZSBhIHByb2JhYmlsaWRhZGUgZG8gRXJybyBUaXBvIEkgKCRcXGFscGhhJCkgZSBhIHByb2JhYmlsaWRhZGUgZG8gRXJybyBUaXBvIElJICgkXFxiZXRhJCkgY2FzbyBvIHZhbG9yIHZlcmRhZGVpcm8gZGUgJFxcbXUkIHNlamEgMTA1LiIsICJkaWNhIjogIlVzZSBvIGZhdG8gZGUgcXVlIHNvYiAkSF8wJCwgJFxcYmFye1h9IFxcc2ltIE4oMTAwLCAxMDAvMjUpJCBlIHNvYiAkSF8xJCAoY29tICRcXG11PTEwNSQpLCAkXFxiYXJ7WH0gXFxzaW0gTigxMDUsIDEwMC8yNSkkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBJZGVudGlmaWNhciBvIGVycm8gcGFkcsOjbzogJEVQKFxcYmFye1h9KSA9IFxcc3FydHtcXHNpZ21hXjIvbn0gPSBcXHNxcnR7MTAwLzI1fSA9IDIkLiIsICIyLiBDYWxjdWxhciAkXFxhbHBoYSA9IFAoXFxiYXJ7WH0gXFxnZSAxMDMsMjkgfCBcXG11PTEwMCkgPSBQKFogXFxnZSAoMTAzLDI5LTEwMCkvMikgPSBQKFogXFxnZSAxLDY0NSkgPSAwLDA1JC4iLCAiMy4gQ2FsY3VsYXIgJFxcYmV0YSA9IFAoXFxiYXJ7WH0gPCAxMDMsMjkgfCBcXG11PTEwNSkgPSBQKFogPCAoMTAzLDI5LTEwNSkvMikgPSBQKFogPCAtMCw4NTUpIFxcYXBwcm94IDAsMTk2MyQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDMzNCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMTk2M30sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCB1dGlsaXphbmRvIGEgYW5hbG9naWEganVyw61kaWNhIChoaXDDs3Rlc2UgbnVsYSBjb21vIHByZXN1bsOnw6NvIGRlIGlub2PDqm5jaWEpLCBhIGRpZmVyZW7Dp2EgZnVuZGFtZW50YWwgZW50cmUgbyBFcnJvIFRpcG8gSSBlIG8gRXJybyBUaXBvIElJLiBDb21vIG8gcGVzcXVpc2Fkb3IsIGFvIHBsYW5lamFyIG8gZXhwZXJpbWVudG8sIHBvZGUgcmVkdXppciBhIHByb2JhYmlsaWRhZGUgZGUgYW1ib3Mgb3MgZXJyb3Mgc2ltdWx0YW5lYW1lbnRlPyIsICJkaWNhIjogIkxlbWJyZS1zZSBkbyAnY2FibyBkZSBndWVycmEnIG1lbmNpb25hZG8gbmEgYXVsYSBlIG8gcGFwZWwgZG8gdGFtYW5obyBhbW9zdHJhbCAkbiQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIERlZmluacOnw6NvOiBFcnJvIFRpcG8gSSDDqSBjb25kZW5hciB1bSBpbm9jZW50ZSAocmVqZWl0YXIgJEhfMCQgdmVyZGFkZWlyYSk7IEVycm8gVGlwbyBJSSDDqSBhYnNvbHZlciB1bSBjdWxwYWRvIChuw6NvIHJlamVpdGFyICRIXzAkIGZhbHNhKS4iLCAiMi4gTyAnY2FibyBkZSBndWVycmEnOiBGaXhhZG8gJG4kLCByZWR1emlyICRcXGFscGhhJCAoc2VyIG1haXMgcmlnb3Jvc28pIGF1bWVudGEgJFxcYmV0YSQgKHBlcmRhIGRlIHBvZGVyKS4iLCAiMy4gUmVkdcOnw6NvIHNpbXVsdMOibmVhOiBBIMO6bmljYSBmb3JtYSBkZSByZWR1emlyIGFtYm9zIG9zIGVycm9zIHNlbSBjb21wcm9tZXRlciBvIG91dHJvIMOpIGF0cmF2w6lzIGRvIGF1bWVudG8gZG8gdGFtYW5obyBhbW9zdHJhbCAkbiQsIHF1ZSBkaW1pbnVpIG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSBlIGF1bWVudGEgYSBwcmVjaXPDo28gZG8gZXN0aW1hZG9yLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlNlamEgJFggXFxzaW0gTihcXG11LCA0MDApJCBvIHRlbXBvIGRlIHByb2Nlc3NhbWVudG8gZGUgdW0gc2lzdGVtYS4gUGFyYSB0ZXN0YXIgJEhfMDogXFxtdSA9IDUwJCBjb250cmEgJEhfMTogXFxtdSA+IDUwJCBjb20gJG49MTYkLCBmaXhhbW9zICRcXGFscGhhID0gMCwwMSQuIERldGVybWluZSBvIHZhbG9yIGNyw610aWNvICRcXGJhcnt4fV9jJCBxdWUgZGVmaW5lIGEgcmVnacOjbyBjcsOtdGljYSBlIGNhbGN1bGUgbyBwb2RlciBkbyB0ZXN0ZSAoJDEtXFxiZXRhJCkgc2UgbyB2ZXJkYWRlaXJvIHZhbG9yIGRlICRcXG11JCBmb3IgNTUuIiwgImRpY2EiOiAiTyB2YWxvciBjcsOtdGljbyAkWl97Y3JpdH0kIHBhcmEgJFxcYWxwaGE9MCwwMSQgKHVuaWxhdGVyYWwpIMOpICQyLDMyNiQuIE8gZXJybyBwYWRyw6NvIMOpICRFUChcXGJhcntYfSkgPSAyMCAvIFxcc3FydHsxNn0gPSA1JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gRW5jb250cmFyICRcXGJhcnt4fV9jJDogJFxcYmFye3h9X2MgPSBcXG11XzAgKyBaX3tjcml0fSBcXGNkb3QgRVAoXFxiYXJ7WH0pID0gNTAgKyAyLDMyNiBcXGNkb3QgNSA9IDYxLDYzJC4iLCAiMi4gQ2FsY3VsYXIgbyBwb2RlciAoJDEtXFxiZXRhJCkgc29iICRcXG11PTU1JDogJFAoXFxiYXJ7WH0gXFxnZSA2MSw2MyB8IFxcbXU9NTUpID0gUChaIFxcZ2UgKDYxLDYzLTU1KS81KSA9IFAoWiBcXGdlIDEsMzI2KSQuIiwgIjMuIFJlc3VsdGFkbzogJDEgLSAwLDkwNzYgPSAwLDA5MjQkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNDAiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjA5MjR9LCB7ImVudW5jaWFkbyI6ICJVbSBhbmFsaXN0YSBkZSBUSSBtb25pdG9yYSBvIHRlbXBvIGRlIHJlc3Bvc3RhIGRlIHVtIHNlcnZpZG9yLiBTYWJlLXNlIHF1ZSwgc29iIGNvbmRpw6fDtWVzIG5vcm1haXMsIG8gdGVtcG8gbcOpZGlvIGRlIHJlc3Bvc3RhIMOpIGRlICRcXG11ID0gMjAwJCBtcywgY29tIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCAkXFxzaWdtYSA9IDIwJCBtcy4gRW0gdW1hIG5vdmEgY29uZmlndXJhw6fDo28sIHVtYSBhbW9zdHJhIGRlICRuID0gNjQkIHJlcXVpc2nDp8O1ZXMgYXByZXNlbnRvdSB1bSB0ZW1wbyBtw6lkaW8gZGUgJFxcYmFye1h9ID0gMjA1JCBtcy4gVXRpbGl6ZSBhcyA1IGV0YXBhcyBkbyBwcm9jZWRpbWVudG8gc2lzdGVtw6F0aWNvIHBhcmEgdGVzdGFyIHNlIGEgbm92YSBjb25maWd1cmHDp8OjbyBhbHRlcm91IG8gdGVtcG8gbcOpZGlvIGRlIHJlc3Bvc3RhIGFvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSA9IDAsMDUkICh0ZXN0ZSBiaWxhdGVyYWwpLiBDYWxjdWxlIGEgZXN0YXTDrXN0aWNhICRaX3tcXHRleHR7Y2FsY319JCBlIGFwcmVzZW50ZSBzdWEgY29uY2x1c8Ojby4iLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlIHBhcmEgYSBtw6lkaWEgcG9wdWxhY2lvbmFsIHF1YW5kbyAkXFxzaWdtYSQgw6kgY29uaGVjaWRvOiAkWl97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXVfMH17XFxzaWdtYSAvIFxcc3FydHtufX0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJFdGFwYSAxOiBGb3JtdWxhciAkSF8wOiBcXG11ID0gMjAwJCB2cyAkSF8xOiBcXG11IFxcbmVxIDIwMCQuIiwgIkV0YXBhIDI6IEVzY29saGVyIGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlOiAkWl97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXVfMH17XFxzaWdtYSAvIFxcc3FydHtufX0kLiIsICJFdGFwYSAzOiBGaXhhciAkXFxhbHBoYSA9IDAsMDUkLiBQYXJhIHVtIHRlc3RlIGJpbGF0ZXJhbCwgJFJDID0gXFx7IFogOiB8WnwgPiAxLDk2IFxcfSQuIiwgIkV0YXBhIDQ6IENhbGN1bGFyICRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFjezIwNSAtIDIwMH17MjAgLyBcXHNxcnR7NjR9fSA9IFxcZnJhY3s1fXsyMCAvIDh9ID0gXFxmcmFjezV9ezIsNX0gPSAyLDAkLiIsICJFdGFwYSA1OiBDb21vICR8MiwwfCA+IDEsOTYkLCBvIHZhbG9yICQyLDAgXFxpbiBSQyQuIENvbmNsdXPDo286IFJlamVpdGFyICRIXzAkIGFvIG7DrXZlbCBkZSAkNVxcJSQuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTQsIDQsIDEwMClcbnkgPSBzdGF0cy5ub3JtLnBkZih4LCAwLCAxKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0yKSwgbmFtZT0nRGVuc2lkYWRlJykpXG5maWcuYWRkX3ZsaW5lKHg9Mi4wLCBsaW5lX2Rhc2g9J2Rhc2gnLCBsaW5lX2NvbG9yPScjOTkxQjFCJywgYW5ub3RhdGlvbl90ZXh0PSdaX3tjYWxjfSA9IDIuMCcpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+VGVzdGUgZGUgSGlww7N0ZXNlIHBhcmEgbyBTZXJ2aWRvcjwvYj4nLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDIuMH0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCBzb2IgYSDDs3RpY2EgZG8gcHJvY2VkaW1lbnRvIHNpc3RlbcOhdGljbywgcG9yIHF1ZSBhIGRlZmluacOnw6NvIGRhIFJlZ2nDo28gQ3LDrXRpY2EgKEV0YXBhIDMpIGRldmUgc2VyIHJlYWxpemFkYSAqYW50ZXMqIGRvIGPDoWxjdWxvIGRhIGVzdGF0w61zdGljYSBhbW9zdHJhbCAoRXRhcGEgNCkuIFF1YWlzIHPDo28gb3MgcmlzY29zIG1ldG9kb2zDs2dpY29zIGRlIHNlIGludmVydGVyIGVzc2Egb3JkZW0/IiwgImRpY2EiOiAiUmVmbGl0YSBzb2JyZSBhIG5lY2Vzc2lkYWRlIGRlIG1hbnRlciBhIG9iamV0aXZpZGFkZSBjaWVudMOtZmljYSBlIGV2aXRhciBvIHZpw6lzIGRlIGNvbmZpcm1hw6fDo28gZG8gcGVzcXVpc2Fkb3IuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgZml4YcOnw6NvIGRhIFJlZ2nDo28gQ3LDrXRpY2EgKCRSQyQpIGFudGVzIGRhIGNvbGV0YS9jw6FsY3VsbyBnYXJhbnRlIHF1ZSBvIGxpbWlhciBkZSBkZWNpc8OjbyBzZWphIGJhc2VhZG8gZXN0cml0YW1lbnRlIG5vIGNvbnRyb2xlIGRvIGVycm8gdGlwbyBJICgkXFxhbHBoYSQpLiIsICJBbyBkZWZpbmlyICRSQyQgcHJpbWVpcm8sIG8gcGVzcXVpc2Fkb3IgZXN0YWJlbGVjZSB1bSBwYWRyw6NvIGRlIGV2aWTDqm5jaWEgZXhpZ2lkbyBwYXJhIHJlamVpdGFyICRIXzAkIGRlIGZvcm1hIGluZGVwZW5kZW50ZSBkb3MgZGFkb3MgcXVlIHNlcsOjbyBvYnNlcnZhZG9zLiIsICJTZSBhIG9yZGVtIGZvc3NlIGludmVydGlkYSAoRXRhcGEgNCBhbnRlcyBkYSBFdGFwYSAzKSwgbyBwZXNxdWlzYWRvciBwb2RlcmlhIHNlciB0ZW50YWRvIGEgYWp1c3RhciBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgb3UgYSByZWdpw6NvICRSQyQgcGFyYSBnYXJhbnRpciBxdWUgbyByZXN1bHRhZG8gZGEgc3VhIGFtb3N0cmEgKGrDoSBjYWxjdWxhZG8pIGNhaWEgbmEgcmVnacOjbyBxdWUgZWxlIGRlc2VqYSAocmVqZWl0YXIgb3UgbsOjbyAkSF8wJCksIGdlcmFuZG8gdW0gdmnDqXMgZGUgc2VsZcOnw6NvLiIsICJBIG9yZGVtIHNpc3RlbcOhdGljYSBwcm90ZWdlIG8gcmlnb3IgY2llbnTDrWZpY28gZSBhIGludGVncmlkYWRlIGRhIGNvbmNsdXPDo28gZXN0YXTDrXN0aWNhLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSBlbnNhaW8gY2zDrW5pY28gb25kZSBhIGhpcMOzdGVzZSBudWxhIMOpIHF1ZSB1bSBtZWRpY2FtZW50byBub3ZvIHRlbSBhIG1lc21hIGVmaWPDoWNpYSBkZSB1bSBwYWRyw6NvLCAkSF8wOiBwID0gMCw1MCQuIE8gcGVzcXVpc2Fkb3IgZGVmaW5lICRIXzE6IHAgPiAwLDUwJCAodW5pbGF0ZXJhbCDDoCBkaXJlaXRhKS4gQ29tIGJhc2UgZW0gdW1hIGFtb3N0cmEsIG8gcGVzcXVpc2Fkb3IgY2FsY3Vsb3UgdW1hIGVzdGF0w61zdGljYSAkWl97XFx0ZXh0e2NhbGN9fSA9IDEsNDUkLiBTZW5kbyAkXFxhbHBoYSA9IDAsMDUkIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhLCBkZXRlcm1pbmUgYSBkZWNpc8OjbyBmb3JtYWwgZSBjYWxjdWxlIG8gdmFsb3IgY3LDrXRpY28gJFpfe1xcdGV4dHtjcml0fX0kIHBhcmEgZXN0ZSB0ZXN0ZS4iLCAiZGljYSI6ICJQYXJhIHVtIHRlc3RlIHVuaWxhdGVyYWwgw6AgZGlyZWl0YSwgYSAkUkMkIMOpIGEgY2F1ZGEgc3VwZXJpb3Igb25kZSAkUChaID4gWl97XFx0ZXh0e2NyaXR9fSkgPSBcXGFscGhhJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRXRhcGEgMTogJEhfMDogcCA9IDAsNTAkIHZzICRIXzE6IHAgPiAwLDUwJC4iLCAiRXRhcGEgMjogRXN0YXTDrXN0aWNhIGRlIHRlc3RlICRaX3tcXHRleHR7Y2FsY319ID0gMSw0NSQuIiwgIkV0YXBhIDM6IFBhcmEgdW0gdGVzdGUgdW5pbGF0ZXJhbCBjb20gJFxcYWxwaGEgPSAwLDA1JCwgbyB2YWxvciBjcsOtdGljbyAkWl97XFx0ZXh0e2NyaXR9fSQgw6kgYXF1ZWxlIHF1ZSBkZWl4YSAkNVxcJSQgbmEgY2F1ZGEgZGlyZWl0YTogJFpfe1xcdGV4dHtjcml0fX0gPSAxLDY0NSQuIiwgIkV0YXBhIDQ6IFZhbG9yIG9ic2VydmFkbyAkWl97XFx0ZXh0e2NhbGN9fSA9IDEsNDUkLiIsICJFdGFwYSA1OiBDb21vICQxLDQ1IDwgMSw2NDUkLCBvIHZhbG9yIG7Do28gcGVydGVuY2Ugw6AgUmVnacOjbyBDcsOtdGljYSAoJFpfe1xcdGV4dHtjYWxjfX0gXFxub3RpbiBSQyQpLiBEZWNpc8OjbzogTsOjbyByZWplaXRhciAkSF8wJC4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgtMywgMywgMTAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgsIDAsIDEpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTIpLCBuYW1lPSdEaXN0cmlidWnDp8OjbyBOb3JtYWwnKSlcbmZpZy5hZGRfdmxpbmUoeD0xLjY0NSwgbGluZV9jb2xvcj0nIzk5MUIxQicsIG5hbWU9J1pfe2NyaXR9ID0gMS42NDUnKVxuZmlnLmFkZF92bGluZSh4PTEuNDUsIGxpbmVfY29sb3I9JyMxMEI5ODEnLCBuYW1lPSdaX3tjYWxjfSA9IDEuNDUnKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkNvbXBhcmHDp8OjbyBlbnRyZSBaX3tjYWxjfSBlIFpfe2NyaXR9PC9iPicsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMS42NDV9XX0=').decode('utf-8'))


    # Gerenciamento de estado para gamificação
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo do progresso
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discursivas = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcqs) + len(discursivas)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    # Dashboard de progresso
    st.markdown("---")
    st.markdown(f"### 📊 Painel de Desempenho")
    if total_exercicios > 0:
        progresso = acertos / total_exercicios
        st.progress(progresso)
        st.markdown(f"🏆 **Seu Progresso:** {acertos} de {total_exercicios} desafios concluídos!")
    st.markdown("---")
    
    # Renderização das questões de múltipla escolha
    st.header("🎯 Questões de Múltipla Escolha")
    for i, questao in enumerate(mcqs):
        with st.container(border=True):
            st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
            
            # Referência bibliográfica
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
                
            # Plotly dinâmico
            cod_plot = questao.get("codigo_plotly")
            if cod_plot:
                try:
                    local_vars = {"__builtins__": __builtins__, "np": np, "stats": stats, "go": go}
                    exec(cod_plot, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True)
                except Exception as e:
                    st.warning(f"Erro ao carregar gráfico: {e}")
    
            # Alternativas
            opcoes = questao.get("alternativas", {})
            escolha = st.radio(
                "Selecione sua alternativa:", 
                list(opcoes.keys()), 
                format_func=lambda x: f"{x}) {opcoes[x]}",
                key=f"radio_mcq_{i}"
            )
            
            # Botões de controle
            col_dica, col_verif = st.columns([1, 1])
            with col_dica:
                if st.button("💡 Dica", key=f"btn_dica_mcq_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
            
            with col_verif:
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
    
    # Renderização das questões discursivas
    st.header("📝 Questões Discursivas e de Cálculo")
    for i, questao in enumerate(discursivas):
        with st.container(border=True):
            st.markdown(f"**Desafio {i+1}:** {questao.get('enunciado', '')}")
            
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
                
            cod_plot = questao.get("codigo_plotly")
            if cod_plot:
                try:
                    local_vars = {"__builtins__": __builtins__, "np": np, "stats": stats, "go": go}
                    exec(cod_plot, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True)
                except Exception as e:
                    st.warning("Erro ao carregar visualização.")
    
            st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
            
            esperado = questao.get("resposta_numerica_esperada")
            if esperado is not None:
                valor_user = st.number_input("Digite o resultado numérico calculado:", format="%.4f", key=f"num_disc_{i}")
                if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                    if abs(valor_user - esperado) <= max(0.01, 0.01 * abs(esperado)):
                        st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                        st.rerun()
                    else:
                        st.error("O valor calculado difere do gabarito oficial. Tente novamente.")
                        st.session_state.respostas_certas[f"disc_{i}"] = False
                        st.rerun()
            else:
                if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.session_state.respostas_certas[f"disc_{i}"] = False
            
            if st.button("💡 Dica", key=f"btn_dica_disc_{i}"):
                st.info(questao.get("dica", "Dica indisponível"))
                
            with st.expander("✅ Ver Resolução Detalhada"):
                for passo in questao.get("gabarito_passo_a_passo", []):
                    st.markdown(f"- {passo}")
