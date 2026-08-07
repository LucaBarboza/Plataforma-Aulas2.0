import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNS4xOiBUZXN0ZXMgZGUgaGlww7N0ZXNlcyBwYXJhIGEgbcOpZGlhIGRlIHBvcHVsYcOnw7VlcyBOb3JtYWlzIChWYXJpw6JuY2lhIGNvbmhlY2lkYSkiLCAicmVmZXJlbmNpYXNfYmlibGlvZ3JhZmljYXNfZmluYWlzIjogWyJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDEyLCBwcC4gMzM0LTM0OCJdfQ==').decode('utf-8'))

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
    from scipy.stats import norm
    
    # Cabeçalho
    st.header(r"A Estrutura Lógica do Teste de Hipóteses")
    
    # Introdução Teórica
    st.markdown(r"""
    O teste de hipóteses constitui o pilar fundamental da inferência estatística, funcionando como uma ferramenta de tomada de decisão sob condições de incerteza. Em cenários industriais ou científicos, a verificação de parâmetros populacionais é frequentemente inviável de forma exaustiva. 
    """)
    
    st.info(r"Consideremos, por exemplo, o caso de um fabricante de componentes eletrônicos que garante uma vida útil média de 5.000 horas para um lote de transistores. Como o teste de todos os itens seria destrutivo e economicamente inviável, recorremos à amostragem aleatória.")
    
    st.markdown(r"""
    A questão central, portanto, é determinar se a divergência observada entre a média da amostra e a média teórica esperada é fruto de uma variação amostral inerente ou se, de fato, a afirmação original é falsa. Este processo guarda semelhança com um julgamento judicial: estabelece-se a inocência do réu sob a Hipótese Nula ($H_0$), que só é refutada diante de provas contundentes.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Rigor do Formalismo Estatístico")
    st.latex(r"H_0: \mu = \mu_0")
    st.latex(r"H_1: \mu \neq \mu_0")
    
    col1, col2 = st.columns(2)
    with col1:
        st.latex(r"\alpha = P(\text{Rejeitar } H_0 | H_0)")
    with col2:
        st.latex(r"\beta = P(\text{Aceitar } H_0 | H_1)")
    
    # Dedução Analítica
    st.markdown(r"### 🧮 Mecânica do Teste")
    st.latex(r"H_0: \mu = \mu_0")
    st.markdown(r"Assumindo a normalidade da distribuição amostral:")
    st.latex(r"\bar{X} \sim N\left(\mu_0, \frac{\sigma^2}{n}\right)")
    st.markdown(r"Definindo a região crítica para o nível de significância $\alpha$:")
    st.latex(r"\frac{\bar{x}_{c} - \mu_0}{\sigma / \sqrt{n}} = Z_{\text{crit}}")
    
    # Simulador de Erros
    st.subheader(r"📊 Visualizador de Erros Tipo I e II")
    st.markdown(r"Explore a relação entre o erro padrão, o nível de significância e a capacidade de detecção do teste.")
    
    c1, c2 = st.columns(2)
    alpha_val = c1.slider(r"Nível de Significância ($\alpha$)", 0.01, 0.10, 0.05, step=0.01, key=r"alpha_subtopico_1")
    mu1_val = c2.slider(r"Média da Hipótese Alternativa ($\mu_1$)", 480.0, 520.0, 510.0, step=1.0, key=r"mu1_subtopico_1")
    
    # Lógica do Gráfico
    x = np.linspace(470, 530, 500)
    y0 = norm.pdf(x, 500, 5)
    y1 = norm.pdf(x, mu1_val, 5)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y0, name=r"H0: \mu=500", line=dict(color="#1E3A8A", width=2)))
    fig.add_trace(go.Scatter(x=x, y=y1, name=rf"H1: \mu={mu1_val}", line=dict(color="#10B981", width=2)))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuições das Hipóteses e Riscos</b>", font=dict(size=14, color="#1E293B"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Média Amostral", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    st.info(rf"Com $\alpha = {alpha_val}$ e $\mu_1 = {mu1_val}$, observamos a sobreposição entre as curvas. Aumentar o $\alpha$ expande a área crítica, facilitando a rejeição de $H_0$ (reduz $\beta$), mas elevando o risco de Erro Tipo I.")
    
    # Exemplo Prático
    st.markdown(r"### 📈 Casos de Aplicação Prática")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Controle de Envase de Café")
        st.markdown(r"Uma máquina de envase opera com $\sigma = 20$g e $\mu_0 = 500$g. Com $n=16$, $\alpha=0,01$ e média amostral de 492g, devemos intervir?")
        st.latex(r"\mu_0 = 500, \sigma = 20, n = 16, \alpha = 0,01, \bar{X} = 492")
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Erro Padrão ($EP$): $20 / \sqrt{16} = 5$")
        st.markdown(r"- Limites Críticos: $500 \pm 2,58 \times 5 = [487,1; 512,9]$")
        st.success(r"Como 492g está dentro do intervalo, não há base estatística para rejeitar $H_0$. O processo permanece sob controle.")

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Formalismo Matemático do Teste para Média com Variância Conhecida")
    
    # Prosa Inicial
    st.markdown(r"""
    Em cenários onde a variância populacional é um dado consolidado — comum em processos industriais de alta precisão onde a variabilidade é crônica e monitorada —, o teste de hipóteses para a média torna-se matematicamente direto através do cálculo da estatística $Z_{\text{calc}}$. 
    
    Este índice padroniza a diferença entre a média amostral observada e a média teórica esperada em relação ao Erro Padrão da Média. A inferência estatística busca quantificar a incerteza inerente ao processo de generalizar conclusões a partir de uma amostra finita.
    """)
    
    # Bloco Teórico de Destaque
    st.info(r"""
    **Conceito Chave:** O conhecimento prévio da variância populacional $\sigma^2$ confere ao pesquisador uma 'âncora' analítica. Diferente de cenários onde a variabilidade é um mistério a ser desvendado simultaneamente, aqui utilizamos a distribuição normal padronizada $N(0, 1)$ como régua fundamental para a tomada de decisão.
    """)
    
    # Detalhamento do Erro Padrão
    st.markdown(r"""
    A construção da estatística de teste depende da transformação da média amostral em uma unidade de desvio padrão em relação à hipótese nula. O Erro Padrão da Média ($EP(\bar{X})$), que define a precisão da nossa estimativa, é expresso por:
    """)
    
    st.latex(r"EP(\bar{X}) = \frac{\sigma}{\sqrt{n}}")
    
    st.markdown(r"""
    Este componente carrega a intuição de que o tamanho da amostra $n$ atua como um atenuador da variabilidade. À medida que o esforço amostral cresce, o erro padrão diminui, tornando a estatística de teste cada vez mais sensível a desvios mínimos da média populacional hipotética $\mu_0$.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Estatística Z")
    
    st.latex(r"Z_{\text{calc}} = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}")
    
    st.markdown(r"""
    A regra de decisão para rejeição da hipótese nula $H_0$ é baseada na comparação entre o valor calculado e o valor crítico da distribuição normal padrão:
    """)
    
    st.latex(r"\text{Regra: Rejeitar } H_0 \text{ se } |Z_{\text{calc}}| > Z_{1-\alpha/2}")
    
    # Dedução Analítica
    st.subheader(r"🧮 Demonstração da Distribuição da Estatística")
    
    st.markdown(r"A dedução analítica parte da distribuição amostral da média:")
    st.latex(r"\bar{X} \sim N(\mu, \sigma^2/n)")
    
    st.markdown(r"Ao centralizarmos a variável em torno de $\mu$:")
    st.latex(r"\bar{X} - \mu \sim N(0, \sigma^2/n)")
    
    st.markdown(r"Padronizando pela raiz quadrada da variância (desvio padrão da média):")
    st.latex(r"\frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)")
    
    st.markdown(r"Resultando, sob a premissa de $H_0$, na nossa estatística de teste:")
    st.latex(r"Z_{\text{calc}} = \frac{\bar{X} - \mu_0}{EP(\bar{X})}")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Controle de Qualidade")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Auditoria de Resistência em Capacitores")
        st.markdown(r"""
        Uma empresa fabricante de capacitores de precisão afirma que a resistência média de seus componentes é de $100 \ \Omega$, com um desvio padrão populacional conhecido de $\sigma = 2,5 \ \Omega$. 
        Um auditor seleciona 36 unidades e obtém uma média amostral de $\bar{X} = 99,2 \ \Omega$. 
        Considerando um risco de erro de 5% ($\alpha = 0,05$), a afirmação deve ser mantida ou rejeitada?
        """)
        
        st.latex(r"\mu_0 = 100, \quad \sigma = 2,5, \quad n = 36, \quad \alpha = 0,05, \quad \bar{X} = 99,2")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Passo 1:** Cálculo do Erro Padrão: $EP(\bar{X}) = 2,5 / \sqrt{36} = 2,5 / 6 \approx 0,4167$")
        st.markdown(r"- **Passo 2:** Cálculo da Estatística Z: $Z_{\text{calc}} = (99,2 - 100) / 0,4167 \approx -1,92$")
        st.markdown(r"- **Passo 3:** Comparação com valor crítico ($Z_{\text{crit}} = 1,96$ para $\alpha=0,05$)")
        
        st.success(r"**Conclusão e Laudo Comercial:** Visto que $|Z_{\text{calc}}| (1,92) < Z_{\text{crit}} (1,96)$, o valor calculado não atinge a região de rejeição. Portanto, não existem evidências estatísticas significativas ao nível de 5% para contradizer a afirmação da empresa sobre a resistência média dos capacitores.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    # Cabeçalho do subtópico
    st.header(r"Regras de Decisão Unilaterais e Bilaterais")
    
    # Prosa Explicativa
    st.markdown(r"""
    A estatística inferencial é um arcabouço lógico desenhado para a tomada de decisão sob incerteza. Quando validamos uma hipótese sobre um parâmetro, como a média $\mu$, a escolha da regra de decisão é onde a intenção do pesquisador encontra o rigor da matemática.
    """)
    
    st.info(r"A decisão entre testes unilaterais ou bilaterais não é apenas aritmética; é um posicionamento estratégico sobre o risco e a natureza da evidência buscada.")
    
    st.markdown(r"""
    ### ⚖️ A Estrutura da Decisão
    A escolha entre as abordagens segue critérios fundamentais:
    * **Teste Bilateral (Bicaudal):** Adota uma postura de agnosticismo. O pesquisador busca desvios em qualquer direção ($\mu \neq \mu_0$). É a escolha padrão para segurança e neutralidade.
    * **Teste Unilateral (Unicaudal):** Foca em uma direção específica ($\mu > \mu_0$ ou $\mu < \mu_0$). É utilizado quando o objetivo prático ou a teoria impõem uma restrição, concentrando todo o poder do teste na direção de interesse.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 Formalismo Matemático")
    st.markdown(r"As Regiões Críticas ($RC$) definem o limiar de rejeição da hipótese nula ao nível $\alpha$:")
    
    st.latex(r"RC_{bilateral}: |Z_{\text{calc}}| > Z_{1-\alpha/2}")
    st.latex(r"RC_{unilateral(d)}: Z_{\text{calc}} > Z_{1-\alpha}")
    st.latex(r"RC_{unilateral(e)}: Z_{\text{calc}} < Z_{\alpha}")
    
    # Dedução Analítica
    st.markdown(r"A validade estatística é garantida pelo comportamento da distribuição normal padrão:")
    st.latex(r"P(Z \in RC) = \alpha")
    st.latex(r"P(Z > Z_{1-\alpha}) = \alpha \quad (\text{unilateral direita})")
    st.latex(r"P(Z < Z_{\alpha}) = \alpha \quad (\text{unilateral esquerda})")
    st.latex(r"P(|Z| > Z_{1-\alpha/2}) = \alpha \quad (\text{bilateral})")
    
    # Simulador Interativo
    st.subheader(r"📈 Explorador da Região Crítica Z")
    col1, col2 = st.columns(2)
    tipo_teste = col1.selectbox(r"Tipo de Teste", [r"Bilateral", r"Unilateral Direita", r"Unilateral Esquerda"], key=r"tipo_teste_subtopico_3")
    alfa = col2.slider(r"Nível de Significância ($\alpha$)", 0.01, 0.10, 0.05, 0.01, key=r"alfa_subtopico_3")
    z_calc = st.slider(r"Estatística $Z_{\text{calc}}$ observada", -4.0, 4.0, 0.0, 0.1, key=r"z_calc_subtopico_3")
    
    x = np.linspace(-4, 4, 200)
    y = norm.pdf(x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=r"Distribuição Normal", line=dict(color="#1E3A8A")))
    
    # Lógica de sombreado
    if tipo_teste == r"Bilateral":
        z_crit = norm.ppf(1 - alfa/2)
        fig.add_vrect(x0=z_crit, x1=4, fillcolor="#991B1B", opacity=0.3, line_width=0)
        fig.add_vrect(x0=-4, x1=-z_crit, fillcolor="#991B1B", opacity=0.3, line_width=0)
        rejeita = abs(z_calc) > z_crit
    elif tipo_teste == r"Unilateral Direita":
        z_crit = norm.ppf(1 - alfa)
        fig.add_vrect(x0=z_crit, x1=4, fillcolor="#991B1B", opacity=0.3, line_width=0)
        rejeita = z_calc > z_crit
    else:
        z_crit = norm.ppf(alfa)
        fig.add_vrect(x0=-4, x1=z_crit, fillcolor="#991B1B", opacity=0.3, line_width=0)
        rejeita = z_calc < z_crit
    
    fig.add_vline(x=z_calc, line_dash="dash", line_color="#F59E0B", annotation_text=r"Z_calc")
    fig.update_layout(template="plotly_white", height=420, margin=dict(l=55, r=30, t=65, b=55, pad=4),
                      title=dict(text=r"<b>Análise da Região Crítica</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif")),
                      xaxis=dict(title=dict(text=r"Valores Z"), gridcolor="#E2E8F0", fixedrange=True),
                      yaxis=dict(showticklabels=False, gridcolor="#E2E8F0", fixedrange=True),
                      legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9)))
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    if rejeita:
        st.error(r"Decisão: Rejeitar a hipótese nula $H_0$ (Estatística na região crítica).")
    else:
        st.success(r"Decisão: Não há evidências suficientes para rejeitar $H_0$.")
    
    # Exemplos Práticos
    st.subheader(r"📖 Casos de Aplicação Prática")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo: Siderúrgica")
        st.markdown(r"Uma siderúrgica testa uma nova liga com resistência normalizada de 200 kg/mm² ($\sigma=10$). Amostra de 25 barras resultou em $\bar{X}=205$.")
        st.latex(r"\mu_0 = 200, \sigma = 10, n = 25, \bar{X} = 205, \alpha = 0.05")
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Erro Padrão: $EP = 10 / \sqrt{25} = 2$")
        st.markdown(r"- $Z_{\text{calc}} = (205 - 200) / 2 = 2,5$")
        st.markdown(r"- Valor Crítico: $Z_{0.95} = 1,645$")
        st.success(r"Conclusão: Como $2,5 > 1,645$, rejeita-se $H_0$. O aumento é estatisticamente significativo.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # --- Cabeçalho do Subtópico ---
    st.header(r"Aplicações Práticas e Interpretação de Resultados: Da Estatística ao Juízo Científico")
    
    # --- Prosa Teórica ---
    st.markdown(r"""
    A etapa final de qualquer teste estatístico transcende o mero domínio do cálculo numérico. É o ponto de inflexão onde o rigor matemático encontra a responsabilidade da inferência científica. Diferente de uma dedução matemática pura, a inferência estatística opera sob o manto da incerteza, exigindo que o tomador de decisão pondere a evidência observada frente a um horizonte de probabilidades.
    """)
    
    st.info(r"O $p\text{-valor}$ atua como a métrica fundamental da 'estranheza' de uma observação. Ele representa a probabilidade de encontrar um valor da estatística de teste pelo menos tão extremo quanto o calculado, assumindo a hipótese nula ($H_0$) como verdadeira.")
    
    st.markdown(r"""
    ### A Estrutura do Formalismo Inferencial
    O formalismo matemático que sustenta a tomada de decisão é construído sobre o controle dos erros Tipo I e Tipo II. A decisão de rejeitar $H_0$ não é um veredito de verdade absoluta, mas uma escolha fundamentada sob risco controlado.
    """)
    
    st.latex(r"p\text{-valor} = P(|Z| > |Z_{\text{calc}}|)")
    st.latex(r"1 - \beta = P(Z_{\text{calc}} \in RC | H_1)")
    st.latex(r"\text{Decisão: } p\text{-valor} \le \alpha \implies \text{Rejeitar } H_0")
    
    # --- Demonstração Analítica ---
    st.markdown(r"### 📐 O Coração Matemático: Dinâmica dos Testes Estatísticos")
    st.latex(r"Z_{\text{calc}} = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}")
    st.markdown(r"Acima, calculamos a distância da média amostral em relação ao valor nulo, normalizada pelo erro padrão.")
    st.latex(r"p\text{-valor} = 2 \times (1 - \Phi(|Z_{\text{calc}}|))")
    st.markdown(r"Aqui, transformamos a estatística $Z$ na probabilidade correspondente na cauda da distribuição normal padrão.")
    st.latex(r"1 - \beta = P(|Z_{\text{calc}}| > Z_{1-\alpha/2} | \mu = \mu_1)")
    st.markdown(r"Por fim, definimos o Poder do Teste ($1-\beta$) como a probabilidade de rejeitar $H_0$ quando o efeito real $\mu_1$ é verdadeiro.")
    
    # --- Simulador Interativo ---
    st.markdown(r"### 📈 Simulador Visual: A Fronteira da Decisão Estatística")
    col1, col2 = st.columns(2)
    with col1:
        n_subtopico_4 = st.slider(r"Tamanho da Amostra ($n$)", 10, 200, 64, key="n_subtopico_4")
        alfa_subtopico_4 = st.select_slider(r"Nível de Significância ($\alpha$)", options=[0.01, 0.05, 0.10], value=0.05, key="alfa_subtopico_4")
    with col2:
        efeito_subtopico_4 = st.slider(r"Efeito Real (Desvio $\mu_1 - \mu_0$)", 0.0, 2.0, 0.5, key="efeito_subtopico_4")
    
    # Cálculo do simulador
    sigma = 1.0
    se = sigma / np.sqrt(n_subtopico_4)
    z_crit = stats.norm.ppf(1 - alfa_subtopico_4/2)
    limite_inf = -z_crit * se
    limite_sup = z_crit * se
    
    # Gerar gráfico
    x = np.linspace(-1, 3, 500)
    y0 = stats.norm.pdf(x, 0, se)
    y1 = stats.norm.pdf(x, efeito_subtopico_4, se)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y0, name=r"Distribuição sob $H_0$", line=dict(color="#1E3A8A")))
    fig.add_trace(go.Scatter(x=x, y=y1, name=r"Distribuição sob $H_1$", line=dict(color="#10B981")))
    
    fig.update_layout(
        template="plotly_white", height=420, margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuições e Região Crítica</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif")),
        xaxis=dict(title=dict(text="Valor da Média Amostral", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")
    
    laudo_dinamico = f"Com $n = {n_subtopico_4}$ e $\\alpha = {alfa_subtopico_4}$, a região crítica para rejeitar $H_0$ inicia em {limite_sup:.3f}. Um efeito de {efeito_subtopico_4} posiciona a distribuição alternativa significativamente à direita, aumentando o poder do teste."
    st.info(laudo_dinamico)
    
    # --- Exemplo Prático ---
    st.markdown(r"### 📈 Casos de Aplicação Prática: O Teste de Composto Farmacêutico")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Eficácia de Composto Anti-Hipertensivo")
        st.markdown(r"Uma empresa farmacêutica testa um composto para pressão arterial ($\mu_0 = 120$ mmHg, $\sigma = 4$ mmHg). Em um estudo com $n = 64$ pacientes, obteve-se $\bar{X} = 121,5$ mmHg.")
        st.latex(r"\mu_0 = 120, \sigma = 4, n = 64, \bar{X} = 121,5, \alpha = 0,05")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Erro Padrão: $EP(\bar{X}) = 4 / \sqrt{64} = 0,5$")
        st.markdown(r"- Estatística de Teste: $Z_{\text{calc}} = (121,5 - 120) / 0,5 = 3,0$")
        st.markdown(r"- $p\text{-valor}: 2 \times P(Z > 3,0) = 0,0027$")
        st.success(r"O $p\text{-valor}$ de 0,0027 é inferior a 0,05. Rejeita-se $H_0$. O composto apresenta efeito estatisticamente significante, com alta confiabilidade para o gestor clínico.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNS4xOiBUZXN0ZXMgZGUgaGlww7N0ZXNlcyBwYXJhIGEgbcOpZGlhIGRlIHBvcHVsYcOnw7VlcyBOb3JtYWlzIChWYXJpw6JuY2lhIGNvbmhlY2lkYSkiLCAicXVlc3RvZXNfbXVsdGlwbGFfZXNjb2xoYSI6IFt7ImVudW5jaWFkbyI6ICJVbWEgZW1wcmVzYSBkZSB0ZWNub2xvZ2lhIHByb2R1eiBtaWNyb3Byb2Nlc3NhZG9yZXMgY29tIHZpZGEgw7p0aWwgc2VndWluZG8gdW1hIGRpc3RyaWJ1acOnw6NvIE5vcm1hbCBjb20gbcOpZGlhICRcXG11JCBlIGRlc3ZpbyBwYWRyw6NvIGNvbmhlY2lkbyAkXFxzaWdtYSA9IDUwJCBob3Jhcy4gTyBjb250cm9sZSBkZSBxdWFsaWRhZGUgYWZpcm1hIHF1ZSBvIHByb2Nlc3NvIMOpIGVzdMOhdmVsLCBjb20gJFxcbXUgPSAyLjAwMCQgaG9yYXMuIFVtIGVuZ2VuaGVpcm8sIHN1c3BlaXRhbmRvIHF1ZSBhIG3DqWRpYSBkaW1pbnVpdSwgdGVzdGEgYSBoaXDDs3Rlc2UgJEhfezB9OiBcXG11ID0gMi4wMDAkIHZlcnN1cyAkSF97MX06IFxcbXUgPCAyLjAwMCQuIENvbSB1bWEgYW1vc3RyYSBkZSAkbiA9IDEwMCQgcHJvY2Vzc2Fkb3JlcywgZWxlIGVzdGFiZWxlY2UgYSBSZWdpw6NvIENyw610aWNhIChSQykgY29tbyAkXFxiYXJ7WH0gPCAxLjk5MCQuIENvbnNpZGVyYW5kbyBhcyBkZWZpbmnDp8O1ZXMgZGUgZXJybyBlbSB0ZXN0ZXMgZGUgaGlww7N0ZXNlcywgcXVhbCBhIHByb2JhYmlsaWRhZGUgZG8gRXJybyBUaXBvIEkgKCRcXGFscGhhJCkgbmVzdGUgdGVzdGU/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIwLDAyMjgiLCAiQiI6ICIwLDA1MDAiLCAiQyI6ICIwLDE1ODciLCAiRCI6ICIwLDAwMTMiLCAiRSI6ICIwLDA0NTYifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIk8gRXJybyBUaXBvIEkgb2NvcnJlIHF1YW5kbyByZWplaXRhbW9zICRIX3swfSQgc2VuZG8gZWxhIHZlcmRhZGVpcmEuIENhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRlICRcXGJhcntYfSQgY2FpciBuYSBSQyBhc3N1bWluZG8gYSBkaXN0cmlidWnDp8OjbyBkYSBtw6lkaWEgYW1vc3RyYWwgc29iICRIX3swfTogXFxiYXJ7WH0gXFxzaW0gTihcXG11X3swfSwgXFxzaWdtYV4yL24pJC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBhcmEgY2FsY3VsYXIgJFxcYWxwaGEkLCBjYWxjdWxhbW9zICRQKFxcYmFye1h9IDwgMS45OTAgfCBcXG11ID0gMi4wMDApJC4gQ29tbyAkXFxiYXJ7WH0gXFxzaW0gTigyLjAwMCwgNTBeMi8xMDApJCwgdGVtb3MgJFxcYmFye1h9IFxcc2ltIE4oMi4wMDAsIDI1KSQuIE8gZXJybyBwYWRyw6NvIMOpICRFUChcXGJhcntYfSkgPSBcXHNxcnR7MjV9ID0gNSQuIFBhZHJvbml6YW5kbzogJFpfe1xcdGV4dHtjYWxjfX0gPSAoMS45OTAgLSAyLjAwMCkgLyA1ID0gLTEwIC8gNSA9IC0yJC4gQ29uc3VsdGFuZG8gYSB0YWJlbGEgZGEgbm9ybWFsIHBhZHLDo28sICRQKFogPCAtMikgPSAwLDAyMjgkLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoMTk4MCwgMjAyMCwgMTAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgsIDIwMDAsIDUpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTMpLCBuYW1lPSdEZW5zaWRhZGUgc29iIEgwJykpXG54X3JjID0gbnAubGluc3BhY2UoMTk4MCwgMTk5MCwgNTApXG55X3JjID0gc3RhdHMubm9ybS5wZGYoeF9yYywgMjAwMCwgNSlcbmZpZy5hZGRfdHJhY2UoZ28uRmlsbCh4PW5wLmNvbmNhdGVuYXRlKFt4X3JjLCBbMTk5MCwgMTk4MF1dKSwgeT1ucC5jb25jYXRlbmF0ZShbeV9yYywgWzAsIDBdXSksIGZpbGw9J3Rvc2VsZicsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG5hbWU9J1JlZ2nDo28gQ3LDrXRpY2EgKFJDKScpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0Rpc3RyaWJ1acOnw6NvIGRlICRcXGJhcntYfSQgc29iICRIX3swfSQgZSBSZWdpw6NvIENyw610aWNhJywgeGF4aXNfdGl0bGU9cidNw6lkaWEgQW1vc3RyYWwgKCRcXGJhcntYfSQpJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZW5zYWlvIGNsw61uaWNvLCBkZXNlamEtc2UgdGVzdGFyIHNlIHVtYSBub3ZhIGRyb2dhIGFsdGVyYSBhIHByZXNzw6NvIGFydGVyaWFsIG3DqWRpYSBlbSByZWxhw6fDo28gYW8gcGFkcsOjbyBoaXN0w7NyaWNvIGRlICQxMjAkIG1tSGcuIERlZmluZS1zZSAkSF97MH06IFxcbXUgPSAxMjAkIGUgJEhfezF9OiBcXG11IFxcbmVxIDEyMCQuIFVtIHBlc3F1aXNhZG9yIGZpeGEgJFxcYWxwaGEgPSAwLDA1JC4gUXVhbCBkYXMgaW50ZXJwcmV0YcOnw7VlcyBhYmFpeG8gZGVzY3JldmUgY29ycmV0YW1lbnRlIG8gc2lnbmlmaWNhZG8gZG8gRXJybyBUaXBvIElJICgkXFxiZXRhJCkgbmVzdGUgY29udGV4dG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIHByb2JhYmlsaWRhZGUgZGUgY29uY2x1aXIgcXVlIGEgZHJvZ2EgbsOjbyBhbHRlcmEgYSBwcmVzc8OjbywgcXVhbmRvIG5hIHZlcmRhZGUgZWxhIGFsdGVyYS4iLCAiQiI6ICJBIHByb2JhYmlsaWRhZGUgZGUgY29uY2x1aXIgcXVlIGEgZHJvZ2EgYWx0ZXJhIGEgcHJlc3PDo28sIHF1YW5kbyBuYSB2ZXJkYWRlIGVsYSBuw6NvIGFsdGVyYS4iLCAiQyI6ICJBIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgJEhfezB9JCBxdWFuZG8gJFxcbXUgPSAxMjAkLiIsICJEIjogIkEgcHJvYmFiaWxpZGFkZSBkZSBhY2VpdGFyICRIX3swfSQgcXVhbmRvICRcXG11ID0gMTIwJC4iLCAiRSI6ICJPIG7DrXZlbCBkZSBjb25maWFuw6dhIGRvIHRlc3RlLCBpZ3VhbCBhICQxIC0gXFxhbHBoYSQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJPIEVycm8gVGlwbyBJSSBhY29udGVjZSBxdWFuZG8gZmFsaGFtb3MgZW0gZGV0ZWN0YXIgdW0gZWZlaXRvIHF1ZSByZWFsbWVudGUgZXhpc3RlLiBQZW5zZSBuYSByZWxhw6fDo28gZW50cmUgYSBkZWNpc8OjbyBkZSBuw6NvIHJlamVpdGFyICRIX3swfSQgZSBhIHJlYWxpZGFkZSBlbSBxdWUgJEhfezF9JCDDqSB2ZXJkYWRlaXJhLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBFcnJvIFRpcG8gSUksIGRlbm90YWRvIHBvciAkXFxiZXRhJCwgw6kgYSBwcm9iYWJpbGlkYWRlIGRlIG7Do28gcmVqZWl0YXIgJEhfezB9JCBkYWRvIHF1ZSAkSF97MX0kIMOpIHZlcmRhZGVpcmEgKCRQKFxcdGV4dHtOw6NvIHJlamVpdGFyIH0gSF97MH0gfCBIX3sxfSkkKS4gSXNzbyBzaWduaWZpY2EgbsOjbyBlbmNvbnRyYXIgZXZpZMOqbmNpYSBlc3RhdMOtc3RpY2EgZGUgbXVkYW7Dp2EgbmEgcHJlc3PDo28gYXJ0ZXJpYWwsIGVtYm9yYSBhIG3DqWRpYSBwb3B1bGFjaW9uYWwgcmVhbCBkYSBub3ZhIGRyb2dhIHNlamEgZGlmZXJlbnRlIGRlICQxMjAkIG1tSGcuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiJ9LCB7ImVudW5jaWFkbyI6ICJVbWEgcGxhbnRhIGluZHVzdHJpYWwgZGUgcHJvZHXDp8OjbyBkZSBjb21wb25lbnRlcyBlbGV0csO0bmljb3MgcG9zc3VpIHVtIHByb2Nlc3NvIGRlIGZhYnJpY2HDp8OjbyBtb25pdG9yYWRvIGNyb25pY2FtZW50ZSwgb25kZSBvIHRlbXBvIGRlIHZpZGEgZGUgdW0gY29tcG9uZW50ZSBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gTm9ybWFsIGNvbSBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgY29uaGVjaWRvIGRlICRcXHNpZ21hID0gMTIkIGhvcmFzLiBPIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBkZXNlamEgdGVzdGFyIHNlIGEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQgZGUgdW0gbm92byBsb3RlIHNlIG1hbnTDqW0gZW0gJFxcbXVfMCA9IDUwMCQgaG9yYXMsIGNvbmZvcm1lIGEgZXNwZWNpZmljYcOnw6NvIHTDqWNuaWNhLiBBcMOzcyBjb2xldGFyIHVtYSBhbW9zdHJhIGFsZWF0w7NyaWEgZGUgJG4gPSAzNiQgY29tcG9uZW50ZXMsIG9idGV2ZS1zZSB1bWEgbcOpZGlhIGFtb3N0cmFsIGRlICRcXGJhcntYfSA9IDUwNiQgaG9yYXMuIENvbnNpZGVyYW5kbyB1bSB0ZXN0ZSBiaWNhdWRhbCwgcXVhbCDDqSBvIHZhbG9yIGRhIGVzdGF0w61zdGljYSAkWl97XHRleHR7Y2FsY319JCBxdWUgZGV2ZSBzZXIgdXRpbGl6YWRhIHBhcmEgYSB0b21hZGEgZGUgZGVjaXPDo28gZXN0YXTDrXN0aWNhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJFpfe1x0ZXh0e2NhbGN9fSA9IDAuNSQiLCAiQiI6ICIkWl97XHRleHR7Y2FsY319ID0gMi4wJCIsICJDIjogIiRaX3tcdGV4dHtjYWxjfX0gPSAzLjAkIiwgIkQiOiAiJFpfe1x0ZXh0e2NhbGN9fSA9IDEuNSQiLCAiRSI6ICIkWl97XHRleHR7Y2FsY319ID0gNi4wJCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBvIEVycm8gUGFkcsOjbyBkYSBNw6lkaWEsICRFUChcXGJhcntYfSkkLCBhanVzdGEgYSB2YXJpYWJpbGlkYWRlIHBvcHVsYWNpb25hbCBwZWxvIHRhbWFuaG8gZGEgYW1vc3RyYTogJEVQKFxcYmFye1h9KSA9IFxcc2lnbWEgLyBcXHNxcnR7bn0kLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUGFyYSBjYWxjdWxhciAkWl97XHRleHR7Y2FsY319JCwgc2VndWltb3Mgb3MgcGFzc29zOlxuMS4gSWRlbnRpZmljYW1vcyBvcyBwYXLDom1ldHJvczogJFxcbXVfMCA9IDUwMCQsICRcXGJhcntYfSA9IDUwNiQsICRcXHNpZ21hID0gMTIkLCAkbiA9IDM2JC5cbjIuIENhbGN1bGFtb3MgbyBFcnJvIFBhZHLDo28gZGEgTcOpZGlhOiAkRVAoXFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0gPSBcXGZyYWN7MTJ9e1xcc3FydHszNn19ID0gXFxmcmFjezEyfXs2fSA9IDIuMCQuXG4zLiBDYWxjdWxhbW9zIGEgZXN0YXTDrXN0aWNhICRaX3tcdGV4dHtjYWxjfX0kOiAkWl97XHRleHR7Y2FsY319ID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdV8wfXtFUChcXGJhcntYfSl9ID0gXFxmcmFjezUwNiAtIDUwMH17Mi4wfSA9IFxcZnJhY3s2fXsyLjB9ID0gMy4wJC4gTyB2YWxvciAkMy4wJCBpbmRpY2EgcXVlIGEgbcOpZGlhIGFtb3N0cmFsIGVzdMOhIDMgZGVzdmlvcyBwYWRyw6NvIGFjaW1hIGRhIG3DqWRpYSBoaXBvdMOpdGljYS4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAxMDApXG55ID0gKDEgLyBucC5cXHNxcnQoMiAqIG5wLlxccGkpKSAqIG5wLlxcZXhwKC0wLjUgKiB4KioyKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBuYW1lPSdEaXN0cmlidWnDp8OjbyBOKDAsMSknLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0zKSkpXG5maWcuYWRkX3ZsaW5lKHg9My4wLCBsaW5lX2Rhc2g9J2Rhc2gnLCBsaW5lX2NvbG9yPScjOTkxQjFCJywgYW5ub3RhdGlvbl90ZXh0PSdaX3tjYWxjfSA9IDMuMCcpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nRGlzdHJpYnVpw6fDo28gTigwLDEpIGUgWl9jYWxjJywgeGF4aXNfdGl0bGU9J1onLCB5YXhpc190aXRsZT0nRGVuc2lkYWRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bWEgcmVkZSBkZSBkaXN0cmlidWnDp8OjbyBkZSDDoWd1YSwgYSBwcmVzc8OjbyBleGVyY2lkYSBub3MgdHVib3Mgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIE5vcm1hbCBjb20gZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsIGNvbmhlY2lkbyAkXFxzaWdtYSA9IDAuNSQgXFxiYXIuIFVtIGVuZ2VuaGVpcm8gZGUgbWFudXRlbsOnw6NvIHJlYWxpemEgdW0gdGVzdGUgcGFyYSB2ZXJpZmljYXIgc2UgYSBwcmVzc8OjbyBtw6lkaWEgJFxcbXUkIMOpIHN1cGVyaW9yIGFvIGxpbWl0ZSBkZSBzZWd1cmFuw6dhICRcXG11XzAgPSAyLjUkIFxcYmFyLiBFbGUgY29sZXRhICRuID0gMjUkIG1lZGlkYXMgZSBvYnTDqW0gdW1hIHByZXNzw6NvIG3DqWRpYSBkZSAkXFxiYXJ7WH0gPSAyLjYkIFxcYmFyLiBRdWFsIGludGVycHJldGHDp8OjbyDDqSBjb3JyZXRhIHNvYnJlIG8gZm9ybWFsaXNtbyBlc3RhdMOtc3RpY28gZG8gdGVzdGU/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIEVycm8gUGFkcsOjbyBkYSBNw6lkaWEgJEVQKFxcYmFye1h9KSQgw6kgJDAuMDIkLCBpbmRpY2FuZG8gYWx0YSBwcmVjaXPDo28gZGEgbcOpZGlhIGFtb3N0cmFsLiIsICJCIjogIkEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlIMOpICRaX3tcdGV4dHtjYWxjfX0gPSAoMi42IC0gMi41KSAvICgwLjUgLyBcXHNxcnR7MjV9KSA9IDEuMCQuIiwgIkMiOiAiTyB2YWxvciAkWl97XHRleHR7Y2FsY319ID0gMS4wJCBzdWdlcmUgcmVqZWl0YXIgJEhfMCQgZW0gcXVhbHF1ZXIgbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJC4iLCAiRCI6ICJPIGVycm8gcGFkcsOjbyDDqSBjYWxjdWxhZG8gY29tbyAkMC41IC8gMjUgPSAwLjAyJC4iLCAiRSI6ICJBIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSAkWl97XHRleHR7Y2FsY319JCBuw6NvIHBvZGUgc2VyIGNhbGN1bGFkYSBwb2lzIGEgYW1vc3RyYSDDqSBwZXF1ZW5hICgkbiA8IDMwJCkuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJWZXJpZmlxdWUgYSBmw7NybXVsYSBkbyBFcnJvIFBhZHLDo28gZGEgTcOpZGlhICRFUChcXGJhcntYfSkgPSBcXHNpZ21hL1xcc3FydHtufSQgZSBhcGxpcXVlIGNvcnJldGFtZW50ZSBuYSBmw7NybXVsYSBkbyAkWl97XHRleHR7Y2FsY319JC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkNhbGN1bGFuZG8gbyBFcnJvIFBhZHLDo286ICRFUChcXGJhcntYfSkgPSBcXGZyYWN7MC41fXtcXHNxcnR7MjV9fSA9IFxcZnJhY3swLjV9ezV9ID0gMC4xJC4gRW50w6NvLCAkWl97XHRleHR7Y2FsY319ID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdV8wfXtFUChcXGJhcntYfSl9ID0gXFxmcmFjezIuNiAtIDIuNX17MC4xfSA9IFxcZnJhY3swLjF9ezAuMX0gPSAxLjAkLiBBIGFsdGVybmF0aXZhIEEgZXN0w6EgZXJyYWRhIHBvaXMgbyBFUCDDqSAkMC4xJC4gQSBDIGVzdMOhIGVycmFkYSBwb2lzICRaPTEuMCQgbsOjbyDDqSBzdWZpY2llbnRlIHBhcmEgcmVqZWnDp8OjbyBlbSBuw612ZWlzIHVzdWFpcyAoY29tbyAkXFxhbHBoYT0wLjA1JCBvbmRlICRaX3tcdGV4dHtjcml0fX0gXFxhcHByb3ggMS42NDUkIHBhcmEgdGVzdGUgdW5pbGF0ZXJhbCkuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBlbmdlbmhlaXJvIGRlIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBlbSB1bWEgZsOhYnJpY2EgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIG1vbml0b3JhIGEgZHVyYWJpbGlkYWRlIG3DqWRpYSBkZSB1bSBub3ZvIHNlbnNvci4gQSBlc3BlY2lmaWNhw6fDo28gdMOpY25pY2EgaW5kaWNhIHF1ZSBvIHByb2Nlc3NvIG9wZXJhIGNvbSAkXFxtdV8wID0gNTAwMCQgaG9yYXMgZSAkXFxzaWdtYSA9IDEwMCQgaG9yYXMuIE8gZW5nZW5oZWlybyBjb2xldGEgdW1hIGFtb3N0cmEgZGUgJG4gPSA2NCQgY29tcG9uZW50ZXMgZSBlbmNvbnRyYSB1bWEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSA9IDUwMzUkIGhvcmFzLiBFbGUgZGVjaWRlIHJlYWxpemFyIHVtIHRlc3RlIGRlIGhpcMOzdGVzZXMgcGFyYSB2ZXJpZmljYXIgc2UgYSBkdXJhYmlsaWRhZGUgZG8gc2Vuc29yIMOpIHN1cGVyaW9yIMOgIGVzcGVjaWZpY2HDp8OjbywgdXRpbGl6YW5kbyB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLDA1JC4gUXVhbCDDqSBhIFJlZ2nDo28gQ3LDrXRpY2EgKCRSQyQpIGUgYSBjb25jbHVzw6NvIGVzdGF0w61zdGljYSBjb3JyZXRhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJFJDID0gXFx7Wl97XFx0ZXh0e2NhbGN9fSA8IC0xLDY0NVxcfSQ7IENvbW8gJFpfe1xcdGV4dHtjYWxjfX0gPSAyLDgwJCwgbsOjbyByZWplaXRhbW9zICRIXzAkLiIsICJCIjogIiRSQyA9IFxce1pfe1xcdGV4dHtjYWxjfX0gPiAxLDY0NVxcfSQ7IENvbW8gJFpfe1xcdGV4dHtjYWxjfX0gPSAyLDgwJCwgcmVqZWl0YW1vcyAkSF8wJC4iLCAiQyI6ICIkUkMgPSBcXHtaX3tcXHRleHR7Y2FsY319ID4gMSw5NlxcfSQ7IENvbW8gJFpfe1xcdGV4dHtjYWxjfX0gPSAyLDgwJCwgcmVqZWl0YW1vcyAkSF8wJC4iLCAiRCI6ICIkUkMgPSBcXHtaX3tcXHRleHR7Y2FsY319IDwgLTEsOTZcXH0kIG91ICRaX3tcXHRleHR7Y2FsY319ID4gMSw5NiQ7IENvbW8gJFpfe1xcdGV4dHtjYWxjfX0gPSAyLDgwJCwgcmVqZWl0YW1vcyAkSF8wJC4iLCAiRSI6ICIkUkMgPSBcXHtaX3tcXHRleHR7Y2FsY319ID4gMiwzM1xcfSQ7IENvbW8gJFpfe1xcdGV4dHtjYWxjfX0gPSAyLDgwJCwgbsOjbyByZWplaXRhbW9zICRIXzAkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiT2JzZXJ2ZSBxdWUgbyBwcm9ibGVtYSBidXNjYSB2ZXJpZmljYXIgc2UgYSBkdXJhYmlsaWRhZGUgw6kgJ3N1cGVyaW9yJywgbyBxdWUgaW5kaWNhIHVtIHRlc3RlIHVuaWxhdGVyYWwgw6AgZGlyZWl0YS4gQ2FsY3VsZSAkWl97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3tcXGJhcntYfSAtIFxcbXVfMH17XFxzaWdtYSAvIFxcc3FydHtufX0kLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUHJpbWVpcm8sIGRlZmluaW1vcyAkSF8wOiBcXG11ID0gNTAwMCQgZSAkSF8xOiBcXG11ID4gNTAwMCQuIE8gdGVzdGUgw6kgdW5pbGF0ZXJhbCDDoCBkaXJlaXRhLCBsb2dvICRSQyA9IFxce1pfe1xcdGV4dHtjYWxjfX0gPiBaX3sxLTAsMDV9ID0gMSw2NDVcXH0kLiBDYWxjdWxhbmRvIGEgZXN0YXTDrXN0aWNhOiAkWl97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3s1MDM1IC0gNTAwMH17MTAwIC8gXFxzcXJ0ezY0fX0gPSBcXGZyYWN7MzV9ezEwMCAvIDh9ID0gXFxmcmFjezM1fXsxMiw1fSA9IDIsODAkLiBDb21vICQyLDgwID4gMSw2NDUkLCBvIHZhbG9yIGNhaSBuYSByZWdpw6NvIGRlIHJlamVpw6fDo28sIHBvcnRhbnRvLCByZWplaXRhbW9zICRIXzAkLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTQsIDQsIDIwMClcbnkgPSBzdGF0cy5ub3JtLnBkZih4KVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0yKSwgbmFtZT0nRGlzdHJpYnVpw6fDo28gTm9ybWFsJykpXG54X2ZpbGwgPSBucC5saW5zcGFjZSgxLjY0NSwgNCwgMTAwKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eF9maWxsLCB5PXN0YXRzLm5vcm0ucGRmKHhfZmlsbCksIGZpbGw9J3RvemVyb3knLCBmaWxsY29sb3I9JyM5OTFCMUInLCBtb2RlPSdub25lJywgbmFtZT0nUkMgKFxcYWxwaGE9MC4wNSknKSlcbmZpZy5hZGRfdmxpbmUoeD0yLjgwLCBsaW5lX2Rhc2g9J2Rhc2gnLCBsaW5lX2NvbG9yPScjRjU5RTBCJywgYW5ub3RhdGlvbl90ZXh0PSdaX3tjYWxjfT0yLjgnKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J1JlZ2nDo28gZGUgUmVqZWnDp8OjbyBwYXJhIEhfMTogXFxtdSA+IFxcbXVfMCcsIHhheGlzX3RpdGxlPSdaX3tjYWxjfScsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBjbMOtbmljbywgdW1hIG1lZGljYcOnw6NvIGRldmUgc2VyIGF2YWxpYWRhIHBhcmEgZGV0ZXJtaW5hciBzZSBlbGEgYWx0ZXJhIGEgcHJlc3PDo28gYXJ0ZXJpYWwgbcOpZGlhIGVtIHJlbGHDp8OjbyBhbyB2YWxvciBiYXNhbCBkZSAkMTIwJCBtbUhnLiBTYWJlLXNlIHF1ZSAkXFxzaWdtYSA9IDE1JCBtbUhnLiBQYXJhIHVtYSBhbW9zdHJhIGRlICRuID0gMTAwJCBwYWNpZW50ZXMsIG9idGV2ZS1zZSB1bWEgbcOpZGlhICRcXGJhcntYfSA9IDExNyQgbW1IZy4gQW8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhID0gMCwwNSQsIHF1YWwgZGFzIGFsdGVybmF0aXZhcyBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgYSBlc3RydXR1cmEgZG8gdGVzdGUgZSBhIGRlY2lzw6NvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiVGVzdGUgdW5pbGF0ZXJhbCwgJEhfMTogXFxtdSA8IDEyMCQsICRSQyA9IFxce1pfe1xcdGV4dHtjYWxjfX0gPCAtMSw2NDVcXH0kLCByZWplaXRhLXNlICRIXzAkLiIsICJCIjogIlRlc3RlIGJpbGF0ZXJhbCwgJEhfMTogXFxtdSBcXG5lcSAxMjAkLCAkUkMgPSBcXHt8Wl97XFx0ZXh0e2NhbGN9fXwgPiAxLDk2XFx9JCwgbsOjbyBzZSByZWplaXRhICRIXzAkLiIsICJDIjogIlRlc3RlIGJpbGF0ZXJhbCwgJEhfMTogXFxtdSBcXG5lcSAxMjAkLCAkUkMgPSBcXHt8Wl97XFx0ZXh0e2NhbGN9fXwgPiAxLDk2XFx9JCwgcmVqZWl0YS1zZSAkSF8wJC4iLCAiRCI6ICJUZXN0ZSBiaWxhdGVyYWwsICRIXzE6IFxcbXUgXFxuZXEgMTIwJCwgJFJDID0gXFx7fFpfe1xcdGV4dHtjYWxjfX18ID4gMSw2NDVcXH0kLCBuw6NvIHNlIHJlamVpdGEgJEhfMCQuIiwgIkUiOiAiVGVzdGUgdW5pbGF0ZXJhbCwgJEhfMTogXFxtdSA+IDEyMCQsICRSQyA9IFxce1pfe1xcdGV4dHtjYWxjfX0gPiAxLDY0NVxcfSQsIHJlamVpdGEtc2UgJEhfMCQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJPIGVudW5jaWFkbyBtZW5jaW9uYSAnYWx0ZXJhJywgc2VtIGVzcGVjaWZpY2FyIGRpcmXDp8OjbywgbyBxdWUgY2FyYWN0ZXJpemEgdW0gdGVzdGUgYmlsYXRlcmFsLiBDYWxjdWxlIG8gJFpfe1xcdGV4dHtjYWxjfX0kIGUgY29tcGFyZSBjb20gbyBxdWFudGlsIGNyw610aWNvIHBhcmEgJFxcYWxwaGEvMiQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJUZW1vcyAkSF8wOiBcXG11ID0gMTIwJCBlICRIXzE6IFxcbXUgXFxuZXEgMTIwJC4gVGVzdGUgYmlsYXRlcmFsIGNvbSAkXFxhbHBoYSA9IDAsMDUkIGltcGxpY2EgJFpfezAsOTc1fSA9IDEsOTYkLiAkWl97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3sxMTcgLSAxMjB9ezE1IC8gXFxzcXJ0ezEwMH19ID0gXFxmcmFjey0zfXsxLDV9ID0gLTIsMCQuIENvbW8gJHwtMiwwfCA9IDIsMCA+IDEsOTYkLCBvIHZhbG9yIGVzdMOhIG5hIHJlZ2nDo28gY3LDrXRpY2EuIENvbnR1ZG8sIHJldmlzYW5kbyBvIGPDoWxjdWxvOiAkfC0yLDB8ID4gMSw5NiQgaW1wbGljYSByZWplacOnw6NvLiBOb3RlOiBhIGFsdGVybmF0aXZhIEIgZXN0w6EgaW5jb3JyZXRhIG5vIHRleHRvIChkZXZlcmlhIHNlciByZWplaXRhKSwgbWFzIGEgQyDDqSBhIGNvcnJldGEgbWF0ZW1hdGljYW1lbnRlLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTQsIDQsIDIwMClcbnkgPSBzdGF0cy5ub3JtLnBkZih4KVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0yKSwgbmFtZT0nTm9ybWFsIFBhZHLDo28nKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PW5wLmxpbnNwYWNlKC00LCAtMS45NiwgNTApLCB5PXN0YXRzLm5vcm0ucGRmKG5wLmxpbnNwYWNlKC00LCAtMS45NiwgNTApKSwgZmlsbD0ndG96ZXJveScsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG1vZGU9J25vbmUnLCBuYW1lPSdSQycpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9bnAubGluc3BhY2UoMS45NiwgNCwgNTApLCB5PXN0YXRzLm5vcm0ucGRmKG5wLmxpbnNwYWNlKDEuOTYsIDQsIDUwKSksIGZpbGw9J3RvemVyb3knLCBmaWxsY29sb3I9JyM5OTFCMUInLCBtb2RlPSdub25lJywgc2hvd2xlZ2VuZD1GYWxzZSkpXG5maWcuYWRkX3ZsaW5lKHg9LTIuMCwgbGluZV9kYXNoPSdkYXNoJywgbGluZV9jb2xvcj0nI0Y1OUUwQicsIGFubm90YXRpb25fdGV4dD0nWl97Y2FsY309LTInKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J1Rlc3RlIEJpbGF0ZXJhbCAoXFxhbHBoYT0wLjA1KScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW0gZW5nZW5oZWlybyBkZSBxdWFsaWRhZGUgZW0gdW1hIGxpbmhhIGRlIG1vbnRhZ2VtIGF1dG9tYXRpemFkYSBlc3TDoSB0ZXN0YW5kbyBzZSBhIHN1YnN0aXR1acOnw6NvIGRlIHVtIGNvbXBvbmVudGUgcm9iw7N0aWNvIGFsdGVyb3UgYSBtw6lkaWEgZGUgdGVtcG8gZGUgY2ljbG8gZGUgcHJvZHXDp8OjbyAoJFxcbXUkKS4gSGlzdG9yaWNhbWVudGUsIG8gdGVtcG8gbcOpZGlvIGRlIGNpY2xvIMOpIGRlIDQ1IHNlZ3VuZG9zLiBBcMOzcyBhIGFsdGVyYcOnw6NvLCB1bWEgYW1vc3RyYSBkZSAkbj0xMDAkIGNpY2xvcyByZXN1bHRvdSBlbSB1bWEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSA9IDQzLDUkIHNlZ3VuZG9zLCBjb20gdW0gZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsIGNvbmhlY2lkbyBkZSAkXFxzaWdtYSA9IDUkIHNlZ3VuZG9zLiBPIGVuZ2VuaGVpcm8gZm9ybXVsb3UgJEhfMDogXFxtdSA9IDQ1JCB2ZXJzdXMgJEhfMTogXFxtdSBcXG5lcSA0NSQuIEFvIHJlYWxpemFyIG8gdGVzdGUsIGVsZSBvYnRldmUgdW0gJHBcXHRleHR7LXZhbG9yfSA9IDAsMDAyNyQuIENvbSBiYXNlIGVtIHVtIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBkZSAkXFxhbHBoYSA9IDAsMDUkLCBxdWFsIMOpIGEgaW50ZXJwcmV0YcOnw6NvIGVzdGF0aXN0aWNhbWVudGUgY29ycmV0YSBkbyByZXN1bHRhZG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJDb21vIG8gJHBcXHRleHR7LXZhbG9yfSA+IFxcYWxwaGEkLCBuw6NvIGjDoSBldmlkw6puY2lhIHN1ZmljaWVudGUgcGFyYSByZWplaXRhciAkSF8wJCwgaW5kaWNhbmRvIHF1ZSBhIG3DqWRpYSBkZSB0ZW1wbyBwZXJtYW5lY2UgaW5hbHRlcmFkYSBhbyBuw612ZWwgZGUgNSUuIiwgIkIiOiAiTyAkcFxcdGV4dHstdmFsb3J9ID0gMCwwMDI3JCBpbmRpY2EgYSBwcm9iYWJpbGlkYWRlIGRlIHF1ZSAkSF8wJCBzZWphIHZlcmRhZGVpcmE7IGNvbW8gw6kgbWVub3IgcXVlIDAsMDUsIHJlamVpdGFtb3MgJEhfMCQgZSBjb25jbHXDrW1vcyBxdWUgbyBub3ZvIGNvbXBvbmVudGUgYWx0ZXJvdSBzaWduaWZpY2F0aXZhbWVudGUgbyB0ZW1wbyBkZSBjaWNsby4iLCAiQyI6ICJDb21vIG8gJHBcXHRleHR7LXZhbG9yfSBcXGxlIFxcYWxwaGEkLCByZWplaXRhbW9zICRIXzAkLiBJc3NvIHNpZ25pZmljYSBxdWUgYSBwcm9iYWJpbGlkYWRlIGRlIG9ic2VydmFyIHVtYSBtw6lkaWEgYW1vc3RyYWwgdMOjbyBleHRyZW1hIHF1YW50byA0Myw1IHNlZ3VuZG9zLCBhc3N1bWluZG8gcXVlIGEgbcOpZGlhIHBvcHVsYWNpb25hbCByZWFsIMOpIDQ1LCDDqSBkZSBhcGVuYXMgMCwyNyUuIiwgIkQiOiAiTyB0ZXN0ZSBuw6NvIMOpIHbDoWxpZG8gcG9pcyBvIHRhbWFuaG8gYW1vc3RyYWwgJG49MTAwJCDDqSBpbnN1ZmljaWVudGUgcGFyYSBpbmZlcsOqbmNpYXMgc29icmUgYSBtw6lkaWEgcG9wdWxhY2lvbmFsIGNvbSBkZXN2aW8gcGFkcsOjbyBjb25oZWNpZG8uIiwgIkUiOiAiQSBkZWNpc8OjbyBkZXZlIHNlciBiYXNlYWRhIG5vIGVycm8gdGlwbyBJSSAoJFxcYmV0YSQpOyBjb21vIG8gJHBcXHRleHR7LXZhbG9yfSQgw6kgbXVpdG8gcGVxdWVubywgbyBwb2RlciBkbyB0ZXN0ZSAoJDEtXFxiZXRhJCkgw6kgbmVjZXNzYXJpYW1lbnRlIHplcm8uIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJMZW1icmUtc2UgZGUgcXVlIG8gcC12YWxvciBtZWRlIGEgZm9yw6dhIGRhIGV2aWTDqm5jaWEgY29udHJhIGEgaGlww7N0ZXNlIG51bGEsIHF1YW50aWZpY2FuZG8gYSBwcm9iYWJpbGlkYWRlIGRlIG9idGVyIHJlc3VsdGFkb3MgdMOjbyBvdSBtYWlzIGV4dHJlbW9zIHF1ZSBvIG9ic2VydmFkbywgY2FzbyAkSF8wJCBzZWphIHZlcmRhZGVpcmEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJPICRwXFx0ZXh0ey12YWxvcn0kIGRlIHVtIHRlc3RlIGRlIGhpcMOzdGVzZSByZXByZXNlbnRhIGEgcHJvYmFiaWxpZGFkZSBkZSBvYnNlcnZhcm1vcyB1bSBkYWRvIGFtb3N0cmFsIHTDo28gb3UgbWFpcyBleHRyZW1vIHF1ZSBhcXVlbGUgb2J0aWRvLCBzb2IgYSBzdXBvc2nDp8OjbyBkZSBxdWUgJEhfMCQgw6kgdmVyZGFkZWlyYS4gQXF1aSwgJHBcXHRleHR7LXZhbG9yfSA9IDAsMDAyNyBcXGxlIFxcYWxwaGEgPSAwLDA1JC4gTWF0ZW1hdGljYW1lbnRlLCByZWplaXRhbW9zICRIXzAkIHF1YW5kbyAkcFxcdGV4dHstdmFsb3J9IFxcbGUgXFxhbHBoYSQuIEEgYWx0ZXJuYXRpdmEgQyBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgZXNzYSBpbnRlcnByZXRhw6fDo28gaW50dWl0aXZhIGRvICRwXFx0ZXh0ey12YWxvcn0kLCBlbnF1YW50byBhcyBvdXRyYXMgYXByZXNlbnRhbSBjb25jZWl0b3MgZXF1aXZvY2Fkb3MgY29tbyBpbnRlcnByZXRhciBvICRwXFx0ZXh0ey12YWxvcn0kIGNvbW8gYSBwcm9iYWJpbGlkYWRlIGRhIGhpcMOzdGVzZSBlbSBzaSBvdSBpZ25vcmFyIGEgcmVncmEgZGUgZGVjaXPDo28gZXN0YWJlbGVjaWRhLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTQsIDQsIDIwMClcbnkgPSBzdGF0cy5ub3JtLnBkZih4LCAwLCAxKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBuYW1lPSdEaXN0cmlidWnDp8OjbyBOb3JtYWwgUGFkcsOjbycsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTIpKSlcbmZpZy5hZGRfdnJlY3QoeDA9My4wLCB4MT00LCBmaWxsY29sb3I9JyM5OTFCMUInLCBvcGFjaXR5PTAuMywgbGluZV93aWR0aD0wLCBuYW1lPSdSZWdpw6NvIENyw610aWNhJylcbmZpZy5hZGRfdnJlY3QoeDA9LTQsIHgxPS0zLjAsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTAsIG5hbWU9J1JlZ2nDo28gQ3LDrXRpY2EnKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J1Zpc3VhbGl6YcOnw6NvIGRvIHAtdmFsb3IgZSBSZWdpw6NvIENyw610aWNhJywgeGF4aXM9ZGljdCh0aXRsZT0nRXN0YXTDrXN0aWNhIFonLCBmaXhlZHJhbmdlPVRydWUpLCB5YXhpcz1kaWN0KHRpdGxlPSdEZW5zaWRhZGUnLCBmaXhlZHJhbmdlPVRydWUpLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJylcbmZpZy5zaG93KCkiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiwgcC4gMzQ5In0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBjbMOtbmljbyBwYXJhIHZlcmlmaWNhciBhIGVmaWPDoWNpYSBkZSB1bWEgbm92YSBkcm9nYSwgbyBwZXNxdWlzYWRvciBkZXNlamEgcXVlIG8gdGVzdGUgdGVuaGEgdW0gcG9kZXIgZGUgJDEgLSBcXGJldGEgPSAwLDkwJCBwYXJhIGRldGVjdGFyIHVtIGVmZWl0byBjbGluaWNhbWVudGUgcmVsZXZhbnRlIGRlICRcXG11ID0gMTA1JCBjb250cmEgJEhfMDogXFxtdSA9IDEwMCQuIFNhYmVuZG8gcXVlIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGZvaSBmaXhhZG8gZW0gJFxcYWxwaGEgPSAwLDA1JCwgbyBxdWUgbyBhdW1lbnRvIGRvIHBvZGVyIGRvIHRlc3RlIChleDogZGUgMCw4MCBwYXJhIDAsOTApIGltcGxpY2EgbmEgcHLDoXRpY2EgZXN0YXTDrXN0aWNhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQXVtZW50YXIgbyBwb2RlciBkbyB0ZXN0ZSByZWR1eiBhdXRvbWF0aWNhbWVudGUgYSBwcm9iYWJpbGlkYWRlIGRlIGNvbWV0ZXIgbyBlcnJvIHRpcG8gSS4iLCAiQiI6ICJVbSBtYWlvciBwb2RlciBkbyB0ZXN0ZSBpbmRpY2EgdW1hIG1haW9yIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgJEhfMCQgY29ycmV0YW1lbnRlIHF1YW5kbyBlbGEgw6kgZGUgZmF0byBmYWxzYS4iLCAiQyI6ICJPIHBvZGVyIGRvIHRlc3RlIHPDsyBhdW1lbnRhIHNlIGRpbWludWlybW9zIG8gdGFtYW5obyBhbW9zdHJhbCAkbiQsIHBvaXMgdGVzdGVzIGNvbSBhbW9zdHJhcyBwZXF1ZW5hcyBzw6NvIG1haXMgc2Vuc8OtdmVpcyBhIGVmZWl0b3MgcmVhaXMuIiwgIkQiOiAiTyBwb2RlciBkZSAwLDkwIHNpZ25pZmljYSBxdWUgZXhpc3RlIDkwJSBkZSBwcm9iYWJpbGlkYWRlIGRlIHF1ZSAkSF8wJCBzZWphIGEgaGlww7N0ZXNlIGNvcnJldGEgYXDDs3MgbyBleHBlcmltZW50by4iLCAiRSI6ICJPIHBvZGVyIGRvIHRlc3RlIMOpIGluZGVwZW5kZW50ZSBkYSBkaXN0w6JuY2lhIGVudHJlICRcXG11JCBzb2IgJEhfMCQgZSAkXFxtdSQgc29iICRIXzEkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTyBwb2RlciBkbyB0ZXN0ZSAoJDEtXFxiZXRhJCkgw6kgYSBzZW5zaWJpbGlkYWRlIGRvIGV4cGVyaW1lbnRvLiBQZW5zZSBuYSBjYXBhY2lkYWRlIGRvIHRlc3RlIGRlIGRldGVjdGFyIHVtYSBkaWZlcmVuw6dhIHJlYWwgcXVhbmRvIGVsYSBleGlzdGUuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJPIHBvZGVyIGRvIHRlc3RlICgkMS1cXGJldGEkKSDDqSBkZWZpbmlkbyBjb21vICRQKFxcdGV4dHtSZWplaXRhciB9IEhfMCB8IEhfMCBcXHRleHR7IMOpIGZhbHNhfSkkLiBQb3J0YW50bywgdW0gdGVzdGUgY29tIHBvZGVyIGRlIDAsOTAgdGVtIDkwJSBkZSBjaGFuY2UgZGUgZGV0ZWN0YXIgY29ycmV0YW1lbnRlIG8gZWZlaXRvIChyZWplaXRhciAkSF8wJCkgcXVhbmRvIG8gZWZlaXRvIHJlYWwgZXN0w6EgcHJlc2VudGUuIEEgYWx0ZXJuYXRpdmEgQSBlc3TDoSBpbmNvcnJldGEgcG9ycXVlIG8gZXJybyB0aXBvIEkgw6kgY29udHJvbGFkbyBwb3IgJFxcYWxwaGEkLiBBIEMgw6kgZmFsc2EgcG9pcyBhdW1lbnRhciAkbiQgw6kgYSBmb3JtYSBtYWlzIGNvbXVtIGRlIGF1bWVudGFyIG8gcG9kZXIuIEEgRCBjb25mdW5kZSBwb2RlciBjb20gcHJvYmFiaWxpZGFkZSBhIHBvc3RlcmlvcmkgZGUgdW1hIGhpcMOzdGVzZS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNDUifV0sICJxdWVzdG9lc19kaXNjdXJzaXZhcyI6IFt7ImVudW5jaWFkbyI6ICJVbWEgZsOhYnJpY2EgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIGdhcmFudGUgdW1hIHZpZGEgw7p0aWwgbcOpZGlhICRcXG11ID0gNS4wMDAkIGhvcmFzLCBjb20gZGVzdmlvIHBhZHLDo28gJFxcc2lnbWEgPSAyMDAkIGhvcmFzLiBVbWEgYW1vc3RyYSBkZSAkbiA9IDY0JCB1bmlkYWRlcyBhcHJlc2VudG91IHVtYSBtw6lkaWEgJFxcYmFye1h9ID0gNC45NjAkLiBTdXBvbmhhIHF1ZSBvIGVuZ2VuaGVpcm8gZGVjaWRhIHJlamVpdGFyICRIX3swfSQgc2UgJFxcYmFye1h9IDwgNC45NTAkLiAoYSkgQ2FsY3VsZSBhIHByb2JhYmlsaWRhZGUgZG8gRXJybyBUaXBvIEkgKCRcXGFscGhhJCkuIChiKSBFeHBsaXF1ZSBvIHF1ZSBhY29udGVjZXJpYSBjb20gJFxcYWxwaGEkIHNlIGF1bWVudMOhc3NlbW9zIG8gdGFtYW5obyBkYSBhbW9zdHJhICRuJCBwYXJhICQxMDAkLCBtYW50ZW5kbyBhIG1lc21hIFJlZ2nDo28gQ3LDrXRpY2EuIiwgImRpY2EiOiAiVXNlIGEgdHJhbnNmb3JtYcOnw6NvICRaID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdX17RVAoXFxiYXJ7WH0pfSQsIG9uZGUgJEVQKFxcYmFye1h9KSA9IFxcZnJhY3tcXHNpZ21hfXtcXHNxcnR7bn19JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYcOnw6NvIGRvcyBkYWRvczogJFxcbXVfezB9ID0gNS4wMDAkLCAkXFxzaWdtYSA9IDIwMCQsICRuID0gNjQkLCAkUkM6IFxcYmFye1h9IDwgNC45NTAkLiIsICIyLiBDw6FsY3VsbyBkbyBFcnJvIFBhZHLDo28gZGEgTcOpZGlhOiAkRVAoXFxiYXJ7WH0pID0gMjAwIC8gXFxzcXJ0ezY0fSA9IDIwMCAvIDggPSAyNSQuIiwgIjMuIEPDoWxjdWxvIGRhIGVzdGF0w61zdGljYSBaIHNvYiAkSF97MH0kOiAkWiA9ICg0Ljk1MCAtIDUuMDAwKSAvIDI1ID0gLTUwIC8gMjUgPSAtMiwwMCQuIiwgIjQuIEPDoWxjdWxvIGRlICRcXGFscGhhID0gUChaIDwgLTIsMDApIFxcYXBwcm94IDAsMDIyOCQuIiwgIjUuIFBhcmEgJG4gPSAxMDAkOiAkRVAoXFxiYXJ7WH0pID0gMjAwIC8gMTAgPSAyMCQuIE5vdm8gJFogPSAoNC45NTAgLSA1LjAwMCkgLyAyMCA9IC01MCAvIDIwID0gLTIsNSQuIiwgIjYuIE5vdm8gJFxcYWxwaGEgPSBQKFogPCAtMiw1KSBcXGFwcHJveCAwLDAwNjIkLiBPIGVycm8gJFxcYWxwaGEkIGRpbWludWkgY29tIG8gYXVtZW50byBkYSBhbW9zdHJhIHNlIGEgcmVnacOjbyBjcsOtdGljYSBmb3IgZml4YS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMDIyOH0sIHsiZW51bmNpYWRvIjogIlVtIGVzdHVkbyBzb2JyZSBvIHJlbmRpbWVudG8gZGUgaW52ZXN0aW1lbnRvcyBkZSB1bWEgY2FydGVpcmEgZGUgYcOnw7VlcyBhc3N1bWUgcXVlIG9zIHJldG9ybm9zIHNlZ3VlbSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIGNvbSBkZXN2aW8gcGFkcsOjbyAkXFxzaWdtYSA9IDVcXCUkLiBBIGVzdHJhdMOpZ2lhIGhpc3TDs3JpY2Egw6kgJFxcbXUgPSAyMFxcJSQuIFVtIGFuYWxpc3RhIHRlc3RhICRIX3swfTogXFxtdSA9IDIwJCBjb250cmEgJEhfezF9OiBcXG11ID4gMjAkIGNvbSB1bWEgYW1vc3RyYSBkZSAkbiA9IDI1JCBhw6fDtWVzLiBTZSBlbGUgZml4YXIgJFxcYWxwaGEgPSAwLDAxJCwgcXVhbCDDqSBhIFJlZ2nDo28gQ3LDrXRpY2EgKCRcXGJhcntYfV97Y30kKSBwYXJhIGVzdGUgdGVzdGU/IiwgImRpY2EiOiAiUGFyYSB1bSB0ZXN0ZSB1bmlsYXRlcmFsIMOgIGRpcmVpdGEsIGEgUmVnacOjbyBDcsOtdGljYSDDqSBkZWZpbmlkYSBwb3IgJFxcYmFye1h9ID4gXFxiYXJ7WH1fe2N9JCwgb25kZSAkUChaID4gWl97Y3JpdH0pID0gXFxhbHBoYSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIElkZW50aWZpY2HDp8OjbyBkb3MgcGFyw6JtZXRyb3M6ICRcXG11X3swfSA9IDIwJCwgJFxcc2lnbWEgPSA1JCwgJG4gPSAyNSQsICRcXGFscGhhID0gMCwwMSQuIiwgIjIuIEPDoWxjdWxvIGRvICRFUChcXGJhcntYfSkgPSA1IC8gXFxzcXJ0ezI1fSA9IDUgLyA1ID0gMSQuIiwgIjMuIFZhbG9yIFogY3LDrXRpY28gcGFyYSAkXFxhbHBoYSA9IDAsMDEkICh1bmlsYXRlcmFsKTogJFpfe2NyaXR9IFxcYXBwcm94IDIsMzMkLiIsICI0LiBFcXVhw6fDo28gZGUgZGVjaXPDo286ICRcXGJhcntYfV97Y30gPSBcXG11X3swfSArIFpfe2NyaXR9IFxcY2RvdCBFUChcXGJhcntYfSkkLiIsICI1LiAkXFxiYXJ7WH1fe2N9ID0gMjAgKyAyLDMzIFxcY2RvdCAxID0gMjIsMzMkLiIsICI2LiBBIHJlZ2nDo28gY3LDrXRpY2Egw6kgJFJDID0gXFx7IFxcYmFye1h9IFxcaW4gXFxtYXRoYmJ7Un0gfCBcXGJhcntYfSA+IDIyLDMzIFxcfSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAyMi4zM30sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBvIHRlc3RlIGRlIHVtYSBoaXDDs3Rlc2UgbnVsYSBzb2JyZSBhIG3DqWRpYSBkZSB1bWEgcG9wdWxhw6fDo28sICRIX3swfTogXFxtdSA9IDEwMCQuIE8gZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsIMOpICRcXHNpZ21hID0gMTUkIGUgbyB0YW1hbmhvIGRhIGFtb3N0cmEgw6kgJG4gPSAzNiQuIENvbSB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgZGUgJFxcYWxwaGEgPSAwLDA1JCwgcmVhbGl6b3Utc2UgbyB0ZXN0ZSBiaWxhdGVyYWwuIENhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRvIEVycm8gVGlwbyBJSSAoJFxcYmV0YSQpIGFzc3VtaW5kbyBxdWUgYSBtw6lkaWEgcG9wdWxhY2lvbmFsIHZlcmRhZGVpcmEgw6ksIG5hIHZlcmRhZGUsICRcXG11X3sxfSA9IDEwNSQuIiwgImRpY2EiOiAiTyAkXFxiZXRhJCDDqSBhIHByb2JhYmlsaWRhZGUgZGUgYWNlaXRhciAkSF97MH0kIHF1YW5kbyBhIG3DqWRpYSByZWFsIMOpICRcXG11X3sxfSQuIEVuY29udHJlIHByaW1laXJvIGEgUmVnacOjbyBkZSBBY2VpdGHDp8OjbyAoUkEpIHNvYiAkSF97MH0kIGUgZGVwb2lzIGNhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRlIGNhaXIgbmVsYSBzb2IgYSBkaXN0cmlidWnDp8OjbyBjZW50cmFkYSBlbSAkXFxtdV97MX0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiAkRVAoXFxiYXJ7WH0pID0gMTUgLyBcXHNxcnR7MzZ9ID0gMTUgLyA2ID0gMiw1JC4iLCAiMi4gUGFyYSAkXFxhbHBoYSA9IDAsMDUkIChiaWxhdGVyYWwpLCAkWl97Y3JpdH0gPSAxLDk2JC4iLCAiMy4gTGltaXRlcyBkZSBSQTogJDEwMCBcXHBtIDEsOTYgXFxjZG90IDIsNSA9IDEwMCBcXHBtIDQsOSA9IFs5NSwxOyAxMDQsOV0kLiIsICI0LiBDw6FsY3VsbyBkZSAkXFxiZXRhID0gUCg5NSwxIDwgXFxiYXJ7WH0gPCAxMDQsOSB8IFxcbXUgPSAxMDUpJC4iLCAiNS4gUGFkcm9uaXphbmRvIGNvbSAkXFxtdSA9IDEwNSQ6ICRaX3sxfSA9ICg5NSwxIC0gMTA1KSAvIDIsNSA9IC0zLDk2JDsgJFpfezJ9ID0gKDEwNCw5IC0gMTA1KSAvIDIsNSA9IC0wLDA0JC4iLCAiNi4gJFxcYmV0YSA9IFAoLTMsOTYgPCBaIDwgLTAsMDQpID0gXFxQaGkoLTAsMDQpIC0gXFxQaGkoLTMsOTYpIFxcYXBwcm94IDAsNDg0MCAtIDAgPSAwLDQ4NDAkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC40ODR9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBsYWJvcmF0w7NyaW8gZGUgbmFub3RlY25vbG9naWEsIGEgZXNwZXNzdXJhIGRlIGZpbG1lcyBmaW5vcyDDqSB1bSBwcm9jZXNzbyBjb250cm9sYWRvIGNvbSBkZXN2aW8gcGFkcsOjbyBwb3B1bGFjaW9uYWwgJFxcc2lnbWEgPSAwLjA4JCBuYW7DtG1ldHJvcy4gUGFyYSB1bWEgYW1vc3RyYSBkZSAkbiA9IDY0JCBtZWRpw6fDtWVzLCBlbmNvbnRyb3Utc2UgdW1hIG3DqWRpYSAkXFxiYXJ7WH0gPSAxMC4xMiQgbm0uIFRlc3RlIGEgaGlww7N0ZXNlIG51bGEgJEhfMDogXFxtdSA9IDEwLjAkIG5tIGNvbnRyYSBhIGFsdGVybmF0aXZhICRIXzE6IFxcbXUgXFxuZXEgMTAuMCQgbm0uIERldGVybWluZSBhIGVzdGF0w61zdGljYSAkWl97XHRleHR7Y2FsY319JCBlIGV4cGxpcXVlIG8gc2lnbmlmaWNhZG8gZXN0YXTDrXN0aWNvIGRlIHVtIGVycm8gcGFkcsOjbyAkRVAoXFxiYXJ7WH0pID0gMC4wMSQuIiwgImRpY2EiOiAiTyAkRVAoXFxiYXJ7WH0pJCBxdWFudGlmaWNhIGEgdmFyaWFiaWxpZGFkZSBkYSBlc3RpbWF0aXZhIGRhIG3DqWRpYSBhbW9zdHJhbC4gVXRpbGl6ZSBhIGbDs3JtdWxhICRaX3tcdGV4dHtjYWxjfX0gPSAoXFxiYXJ7WH0gLSBcXG11XzApIC8gRVAoXFxiYXJ7WH0pJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiSWRlbnRpZmljYcOnw6NvIGRvcyBwYXLDom1ldHJvczogJFxcbXVfMCA9IDEwLjAkLCAkXFxiYXJ7WH0gPSAxMC4xMiQsICRcXHNpZ21hID0gMC4wOCQsICRuID0gNjQkLiIsICJDw6FsY3VsbyBkbyBFcnJvIFBhZHLDo28gZGEgTcOpZGlhOiAkRVAoXFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0gPSBcXGZyYWN7MC4wOH17XFxzcXJ0ezY0fX0gPSBcXGZyYWN7MC4wOH17OH0gPSAwLjAxJC4iLCAiQ8OhbGN1bG8gZGEgZXN0YXTDrXN0aWNhIFo6ICRaX3tcdGV4dHtjYWxjfX0gPSBcXGZyYWN7MTAuMTIgLSAxMC4wfXswLjAxfSA9IFxcZnJhY3swLjEyfXswLjAxfSA9IDEyLjAkLiIsICJJbnRlcnByZXRhw6fDo286IFVtICRaX3tcdGV4dHtjYWxjfX0gPSAxMi4wJCBpbmRpY2EgcXVlIGEgbcOpZGlhIG9ic2VydmFkYSBlc3TDoSAxMiBkZXN2aW9zIHBhZHLDo28gYWNpbWEgZGEgaGlww7N0ZXNlIG51bGEsIG8gcXVlIMOpIHVtIHZhbG9yIGV4dHJlbWFtZW50ZSBpbXByb3bDoXZlbCBzb2IgJEhfMCQsIGxldmFuZG8gw6AgcmVqZWnDp8OjbyBpbWVkaWF0YSBkYSBoaXDDs3Rlc2UgbnVsYS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDEyLjB9LCB7ImVudW5jaWFkbyI6ICJVbSBwcm9jZXNzbyBkZSBlbnZhc2UgZGUgYmViaWRhcyB0ZW0gdmFyacOibmNpYSBwb3B1bGFjaW9uYWwgY29uaGVjaWRhICRcXHNpZ21hXjIgPSAwLjI1JCBsaXRyb3MkXjIkLiBTYWJlbmRvIHF1ZSBvIHZvbHVtZSBtw6lkaW8gbm9taW5hbCDDqSAkXFxtdV8wID0gMi4wJCBsaXRyb3MsIGNhbGN1bGUgcXVhbCBzZXJpYSBvIHRhbWFuaG8gYW1vc3RyYWwgJG4kIG5lY2Vzc8OhcmlvIHBhcmEgcXVlIHVtIGRlc3ZpbyBkZSAkMC4xJCBsaXRybyBuYSBtw6lkaWEgYW1vc3RyYWwgcmVzdWx0ZSBlbSB1bWEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlICRaX3tcdGV4dHtjYWxjfX0gPSAyLjUkLiIsICJkaWNhIjogIklzb2xlICRuJCBuYSBmw7NybXVsYSBkYSBlc3RhdMOtc3RpY2EgJFpfe1x0ZXh0e2NhbGN9fSQuIExlbWJyZS1zZSBxdWUgJFxcc2lnbWEgPSBcXHNxcnR7XFxzaWdtYV4yfSA9IDAuNSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlNhYmVtb3MgcXVlICRaX3tcdGV4dHtjYWxjfX0gPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11XzB9e1xcc2lnbWEgLyBcXHNxcnR7bn19JC4gVGVtb3MgJChcXGJhcntYfSAtIFxcbXVfMCkgPSAwLjEkLCAkXFxzaWdtYSA9IDAuNSQgZSAkWl97XHRleHR7Y2FsY319ID0gMi41JC4iLCAiU3Vic3RpdHVpbmRvIG5hIGbDs3JtdWxhOiAkMi41ID0gXFxmcmFjezAuMX17MC41IC8gXFxzcXJ0e259fSQuIiwgIlJlYXJyYW5qYW5kbyBvcyB0ZXJtb3M6ICQyLjUgPSAwLjEgXFxjZG90IFxcZnJhY3tcXHNxcnR7bn19ezAuNX0gPSAwLjIgXFxjZG90IFxcc3FydHtufSQuIiwgIklzb2xhbmRvICRcXHNxcnR7bn0kOiAkXFxzcXJ0e259ID0gXFxmcmFjezIuNX17MC4yfSA9IDEyLjUkLiIsICJFbGV2YW5kbyBhbyBxdWFkcmFkbzogJG4gPSAoMTIuNSleMiA9IDE1Ni4yNSQuIENvbW8gbyB0YW1hbmhvIGFtb3N0cmFsIGRldmUgc2VyIHVtIGludGVpcm8sIG8gdmFsb3IgbmVjZXNzw6FyaW8gc2VyaWEgJG4gPSAxNTckLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMTU2LjI1fSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUgbWF0ZW1hdGljYW1lbnRlIHBvciBxdWUsIG1hbnRlbmRvICRcXHNpZ21hJCBjb25zdGFudGUsIG8gYXVtZW50byBkbyB0YW1hbmhvIGFtb3N0cmFsICRuJCByZWR1eiBvICRFUChcXGJhcntYfSkkIGUgY29uc2VxdWVudGVtZW50ZSBhdW1lbnRhIG8gdmFsb3IgYWJzb2x1dG8gZGEgZXN0YXTDrXN0aWNhICRaX3tcdGV4dHtjYWxjfX0kIHBhcmEgdW1hIGRpZmVyZW7Dp2EgJChcXGJhcntYfSAtIFxcbXVfMCkkIGZpeGEuIFF1YWwgbyBpbXBhY3RvIGRpc3NvIG5vIHBvZGVyIGRlIGRldGVjw6fDo28gZGUgZGVzdmlvcyBkYSBoaXDDs3Rlc2UgbnVsYT8iLCAiZGljYSI6ICJBbmFsaXNlIGEgZGVwZW5kw6puY2lhIGZ1bmNpb25hbCBkZSAkRVAoXFxiYXJ7WH0pJCBlbSByZWxhw6fDo28gYSAkbiQgZSBjb21vIGlzc28gYWx0ZXJhIGEgZXNjYWxhIGRvIHRlc3RlLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBIGZ1bsOnw6NvIGRvIEVycm8gUGFkcsOjbyDDqSAkRVAoXFxiYXJ7WH0pID0gXFxzaWdtYSBcXGNkb3Qgbl57LTEvMn0kLiBBbyBhdW1lbnRhciAkbiQsIG8gdGVybW8gJG5eey0xLzJ9JCBkZWNyZXNjZSwgcmVkdXppbmRvIG8gdmFsb3IgZGUgJEVQKFxcYmFye1h9KSQuIiwgIk5hIGbDs3JtdWxhICRaX3tcdGV4dHtjYWxjfX0gPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11XzB9e0VQKFxcYmFye1h9KX0kLCBjb21vICRFUChcXGJhcntYfSkkIGVzdMOhIG5vIGRlbm9taW5hZG9yLCB1bWEgcmVkdcOnw6NvIG5vIGVycm8gcGFkcsOjbyBwYXJhIHVtYSBtZXNtYSBkaWZlcmVuw6dhIG9ic2VydmFkYSAkKFxcYmFye1h9IC0gXFxtdV8wKSQgcmVzdWx0YSBlbSB1bSBhdW1lbnRvIGRvIHZhbG9yIGFic29sdXRvIGRlICRaX3tcdGV4dHtjYWxjfX0kLiIsICJJbXBhY3RvIG5vIHBvZGVyOiBDb20gJG4kIG1haW9yLCBhIGRpc3RyaWJ1acOnw6NvIGRlICRcXGJhcntYfSQgdG9ybmEtc2UgbWFpcyBjb25jZW50cmFkYSBlbSB0b3JubyBkYSB2ZXJkYWRlaXJhIG3DqWRpYS4gSXNzbyBmYXogY29tIHF1ZSBwZXF1ZW5hcyBkaXNjcmVww6JuY2lhcyBlbnRyZSBhIG3DqWRpYSBhbW9zdHJhbCBlICRcXG11XzAkIHNlamFtIGFtcGxpZmljYWRhcyBwZWxhIGVzdGF0w61zdGljYSAkWl97XHRleHR7Y2FsY319JCwgdG9ybmFuZG8gbyB0ZXN0ZSBtYWlzIHNlbnPDrXZlbCBwYXJhIGRldGVjdGFyIGRlc3Zpb3MgcmVhaXMsIG91IHNlamEsIGF1bWVudGFuZG8gbyBzZXUgcG9kZXIgZXN0YXTDrXN0aWNvLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtYSBlbXByZXNhIGRlIFxcbG9nw61zdGljYSBhZmlybWEgcXVlIG8gdGVtcG8gbcOpZGlvIGRlIGVudHJlZ2Egw6kgZGUgNDUgbWludXRvcyBjb20gJFxcc2lnbWEgPSAxMiQgbWludXRvcy4gVW0gYXVkaXRvciBzZWxlY2lvbmEgMzYgZW50cmVnYXMgZSBlbmNvbnRyYSB1bWEgbcOpZGlhICRcXGJhcntYfSA9IDQ5JCBtaW51dG9zLiBDb20gJFxcYWxwaGEgPSAwLDAxJCwgdGVzdGUgYSBoaXDDs3Rlc2UgZGUgcXVlIG8gdGVtcG8gZGUgZW50cmVnYSDDqSBtYWlvciBkbyBxdWUgbyBhbnVuY2lhZG8uIEFwcmVzZW50ZSB0b2RvcyBvcyBwYXNzb3MgZGEgaW5mZXLDqm5jaWEuIiwgImRpY2EiOiAiSWRlbnRpZmlxdWUgJEhfMCQgZSAkSF8xJCBjb21vIHVtIHRlc3RlIHVuaWxhdGVyYWwuIERldGVybWluZSAkWl97XFx0ZXh0e2NyaXR9fSQgcGFyYSAkXFxhbHBoYSA9IDAsMDEkIG5hIHRhYmVsYSBub3JtYWwuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIEhpcMOzdGVzZXM6ICRIXzA6IFxcbXUgPSA0NSQgXFxtaW47ICRIXzE6IFxcbXUgPiA0NSQgXFxtaW4uIiwgIjIuIEVzdGF0w61zdGljYSBkZSB0ZXN0ZTogJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7NDkgLSA0NX17MTIgLyBcXHNxcnR7MzZ9fSA9IFxcZnJhY3s0fXsxMiAvIDZ9ID0gXFxmcmFjezR9ezJ9ID0gMiwwMCQuIiwgIjMuIFJlZ2nDo28gQ3LDrXRpY2EgcGFyYSAkXFxhbHBoYSA9IDAsMDEkOiAkWl97MCw5OX0gPSAyLDMyNiQuICRSQyA9IFxce1pfe1xcdGV4dHtjYWxjfX0gPiAyLDMyNlxcfSQuIiwgIjQuIERlY2lzw6NvOiBDb21vICQyLDAwIDwgMiwzMjYkLCBuw6NvIHJlamVpdGFtb3MgJEhfMCQgYW8gbsOtdmVsIGRlIDElLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMi4wfSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIHNvYiB1bWEgw7N0aWNhIGVzdGF0w61zdGljYSwgcG9yIHF1ZSB1bSB0ZXN0ZSBiaWxhdGVyYWwgw6kgY29uc2lkZXJhZG8gbWFpcyAncmlnb3Jvc28nIGVtIHRlcm1vcyBkZSBjYXB0dXJhIGRlIGRlc3Zpb3MgZG8gcXVlIHVtIHRlc3RlIHVuaWxhdGVyYWwgcGFyYSB1bSBtZXNtbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkLiBVdGlsaXplIG8gZm9ybWFsaXNtbyBkZSBSZWdpw6NvIENyw610aWNhIHBhcmEganVzdGlmaWNhciBzdWEgcmVzcG9zdGEuIiwgImRpY2EiOiAiQ29tcGFyZSBvbmRlIGEgw6FyZWEgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkIMOpIGFsb2NhZGEgZW0gY2FkYSB0aXBvIGRlIHRlc3RlLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBObyB0ZXN0ZSB1bmlsYXRlcmFsLCB0b2RhIGEgw6FyZWEgJFxcYWxwaGEkIGVzdMOhIGNvbmNlbnRyYWRhIGVtIHVtYSDDum5pY2EgY2F1ZGEgKCRaX3tcXHRleHR7Y3JpdH19ID0gWl97MS1cXGFscGhhfSQgb3UgJFpfe1xcYWxwaGF9JCkuIiwgIjIuIE5vIHRlc3RlIGJpbGF0ZXJhbCwgYSDDoXJlYSAkXFxhbHBoYSQgw6kgZGl2aWRpZGE6ICRcXGFscGhhLzIkIGVtIGNhZGEgY2F1ZGEgKCRaX3tcXHRleHR7Y3JpdH19ID0gXFxwbSBaX3sxLVxcYWxwaGEvMn0kKS4iLCAiMy4gQ29tbyAkWl97MS1cXGFscGhhLzJ9ID4gWl97MS1cXGFscGhhfSQsIG8gdGVzdGUgYmlsYXRlcmFsIGV4aWdlIHVtIGRlc3ZpbyBtYWlzIGV4dHJlbW8gbmEgYW1vc3RyYSBwYXJhIGF0aW5naXIgYSByZWdpw6NvIGRlIHJlamVpw6fDo28gZW0gdW1hIGRpcmXDp8OjbyBlc3BlY8OtZmljYS4iLCAiNC4gUG9ydGFudG8sIGEgc2Vuc2liaWxpZGFkZSBwYXJhIGNhcHR1cmFyIHF1YWxxdWVyIGRpcmXDp8OjbyBkZSBkZXN2aW8gw6kgYSBwcmluY2lwYWwgZGlzdGluw6fDo28gdGXDs3JpY2EgZW50cmUgb3MgZG9pcyB0aXBvcyBkZSByZWdyYSBkZSBkZWNpc8Ojby4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyBjZW7DoXJpbyBlbSBxdWUgJFxcYmFye1h9ID0gMTA1JCwgJFxcbXVfMCA9IDEwMCQsICRcXHNpZ21hID0gMjAkIGUgJG4gPSAyNSQuIENhbGN1bGUgbyB2YWxvciAkWl97XFx0ZXh0e2NhbGN9fSQgZSBkZXRlcm1pbmUgbyBwLXZhbG9yIHBhcmEgdW0gdGVzdGUgYmlsYXRlcmFsLiIsICJkaWNhIjogIk8gcC12YWxvciBwYXJhIHRlc3RlIGJpbGF0ZXJhbCDDqSAkMiBcXGNkb3QgUChaID4gfFpfe1xcdGV4dHtjYWxjfX18KSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIEPDoWxjdWxvIGRvIGVycm8gcGFkcsOjbzogJEVQKFxcYmFye1h9KSA9IFxcc2lnbWEgLyBcXHNxcnR7bn0gPSAyMCAvIFxcc3FydHsyNX0gPSAyMCAvIDUgPSA0JC4iLCAiMi4gQ8OhbGN1bG8gZG8gJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7MTA1IC0gMTAwfXs0fSA9IDEsMjUkLiIsICIzLiBPIHAtdmFsb3IgYmlsYXRlcmFsIMOpICRQKHxafCA+IDEsMjUpID0gMiBcXGNkb3QgKDEgLSBQKFogXFxsZXEgMSwyNSkpJC4iLCAiNC4gQ29uc3VsdGFuZG8gdGFiZWxhIG5vcm1hbCwgJFAoWiBcXGxlcSAxLDI1KSBcXGFwcHJveCAwLDg5NDQkLiIsICI1LiAkcFxcdGV4dHstdmFsb3J9ID0gMiBcXGNkb3QgKDEgLSAwLDg5NDQpID0gMiBcXGNkb3QgMCwxMDU2ID0gMCwyMTEyJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMjExMn0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBxdWUgYSByZXNpc3TDqm5jaWEgZGUgdW0gbWF0ZXJpYWwgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCAkWCBcXHNpbSBOKFxcbXUsIDI1KSQuIERlc2VqYW1vcyB0ZXN0YXIgJEhfMDogXFxtdSA9IDUwJCBjb250cmEgJEhfMTogXFxtdSA+IDUwJC4gQ29tIHVtYSBhbW9zdHJhIGRlICRuID0gMjUkLCBmaXhhbW9zICRcXGFscGhhID0gMCwwNSQuIChhKSBEZXRlcm1pbmUgbyB2YWxvciBjcsOtdGljbyBkYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9X2MkIHBhcmEgYSByZWdpw6NvIGNyw610aWNhLiAoYikgU2UgbyB2ZXJkYWRlaXJvIHBhcsOibWV0cm8gZm9yICRcXG11ID0gNTIkLCBjYWxjdWxlIGEgcHJvYmFiaWxpZGFkZSBkbyBlcnJvIHRpcG8gSUkgKCRcXGJldGEkKS4iLCAiZGljYSI6ICJBIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSBwYXJhIGEgbcOpZGlhIGNvbSAkXFxzaWdtYSQgY29uaGVjaWRvIMOpICRaID0gKFxcYmFye1h9IC0gXFxtdSkgLyAoXFxzaWdtYSAvIFxcc3FydHtufSkkLiBMZW1icmUtc2UgcXVlICRSQyQgcGFyYSAkSF8xOiBcXG11ID4gXFxtdV8wJCDDqSAkXFxiYXJ7WH0gPiBcXGJhcntYfV9jJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYXIgbyB2YWxvciBjcsOtdGljbyAkWl97XFx0ZXh0e2NyaXR9fSQgcGFyYSAkXFxhbHBoYSA9IDAsMDUkIGVtIHVtIHRlc3RlIHVuaWxhdGVyYWw6ICRaX3tcXHRleHR7Y3JpdH19ID0gMSw2NDUkLiIsICIyLiBDYWxjdWxhciAkXFxiYXJ7WH1fYyQgdXNhbmRvICRcXGJhcntYfV9jID0gXFxtdV8wICsgWl97XFx0ZXh0e2NyaXR9fSBcXGNkb3QgKFxcc2lnbWEgLyBcXHNxcnR7bn0pID0gNTAgKyAxLDY0NSBcXGNkb3QgKDUgLyBcXHNxcnR7MjV9KSA9IDUwICsgMSw2NDUgPSA1MSw2NDUkLiIsICIzLiBEZWZpbmlyIGEgcHJvYmFiaWxpZGFkZSBkZSBlcnJvIHRpcG8gSUk6ICRcXGJldGEgPSBQKFxcYmFye1h9IFxcbGUgNTEsNjQ1IHwgXFxtdSA9IDUyKSQuIiwgIjQuIENhbGN1bGFyIG8gbm92byB2YWxvciBaIHNvYiAkSF8xJDogJFogPSAoNTEsNjQ1IC0gNTIpIC8gKDUgLyA1KSA9IC0wLDM1NSQuIiwgIjUuIEVuY29udHJhciBhIHByb2JhYmlsaWRhZGU6ICRcXGJldGEgPSBQKFogXFxsZSAtMCwzNTUpIFxcYXBwcm94IDAsMzYxMyQgb3UgJDM2LDEzXFwlJC4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSg0OCwgNTYsIDIwMClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9c3RhdHMubm9ybS5wZGYoeCwgNTAsIDEpLCBuYW1lPSdIMCAoXFxtdT01MCknLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnKSkpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLm5vcm0ucGRmKHgsIDUyLCAxKSwgbmFtZT0nSDEgKFxcbXU9NTIpJywgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJykpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0Rpc3RyaWJ1acOnw7VlcyBTb2IgSDAgZSBIMScsIHhheGlzPWRpY3QodGl0bGU9J03DqWRpYSBBbW9zdHJhbCcsIGZpeGVkcmFuZ2U9VHJ1ZSksIHlheGlzPWRpY3QodGl0bGU9J0RlbnNpZGFkZScsIGZpeGVkcmFuZ2U9VHJ1ZSkpXG5maWcuc2hvdygpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDMzNCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMzYxM30sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlIGEgcmVsYcOnw6NvIGZ1bmRhbWVudGFsIGVudHJlIG8gJHBcXHRleHR7LXZhbG9yfSQgZSBhIGRlY2lzw6NvIGRlIHJlamVpw6fDo28gZGUgJEhfMCQgc29iIHVtIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQuIFBvciBxdWUsIGVtIGNvbnRleHRvcyBkZSBlbmdlbmhhcmlhIGRlIGFsdGEgcHJlY2lzw6NvLCB1bSAkcFxcdGV4dHstdmFsb3J9JCBtdWl0byBiYWl4bywgZW1ib3JhIGVzdGF0aXN0aWNhbWVudGUgc2lnbmlmaWNhbnRlLCBwb2RlIG7Do28gaW1wbGljYXIgbmVjZXNzYXJpYW1lbnRlIGVtIHVtYSBtdWRhbsOnYSBwcsOhdGljYSBubyBwcm9jZXNzbyBkZSBmYWJyaWNhw6fDo28/IiwgImRpY2EiOiAiRGlmZXJlbmNpZSAnc2lnbmlmaWPDom5jaWEgZXN0YXTDrXN0aWNhJyBkZSAnc2lnbmlmaWPDom5jaWEgcHLDoXRpY2EnIG91ICdtYWduaXR1ZGUgZG8gZWZlaXRvJy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gQSByZWdyYSBkZSBkZWNpc8OjbyDDqTogc2UgJHBcXHRleHR7LXZhbG9yfSBcXGxlIFxcYWxwaGEkLCByZWplaXRhbW9zICRIXzAkLiBPICRwXFx0ZXh0ey12YWxvcn0kIHF1YW50aWZpY2EgYSBwcm9iYWJpbGlkYWRlIGRlIG9ic2VydmFyIGRhZG9zIHTDo28gZXh0cmVtb3MgYXNzdW1pbmRvICRIXzAkIGNvcnJldGEuIiwgIjIuIFNpZ25pZmljw6JuY2lhIGVzdGF0w61zdGljYSBmb2NhIG5hIHByb2JhYmlsaWRhZGUgZGUgbyBlZmVpdG8gb2JzZXJ2YWRvIG7Do28gc2VyIGRldmlkbyBhbyBhY2Fzby4iLCAiMy4gRW0gYW1vc3RyYXMgZ3JhbmRlcyAoJG4kIG11aXRvIGFsdG8pLCBwZXF1ZW5hcyB2YXJpYcOnw7VlcyBxdWUgbsOjbyBwb3NzdWVtIGltcGFjdG8gcmVhbCBubyBwcm9kdXRvIHBvZGVtIHNlIHRvcm5hciBlc3RhdGlzdGljYW1lbnRlIHNpZ25pZmljYW50ZXMuIiwgIjQuIEEgc2lnbmlmaWPDom5jaWEgcHLDoXRpY2EgYXZhbGlhIHNlIGEgZGlmZXJlbsOnYSBvYnNlcnZhZGEgdGVtIHJlbGV2w6JuY2lhIG5vIG11bmRvIGbDrXNpY28gb3UgZmluYW5jZWlybyAoZXg6IHVtYSBtZWxob3JpYSBkZSAwLDAwMDEgc2VndW5kb3MgbsOjbyBhbHRlcmEgYSBwcm9kdXRpdmlkYWRlIHJlYWwpLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBzb2JyZSBvIHRlbXBvIGRlIHZpZGEgw7p0aWwgZGUgdW1hIGJhdGVyaWEgSW9ULCBzYWJlLXNlIHF1ZSAkWCBcXHNpbSBOKFxcbXUsIDQwMCkkLiBUZXN0b3Utc2UgJEhfMDogXFxtdSA9IDUwMCQgY29udHJhICRIXzE6IFxcbXUgXFxuZXEgNTAwJC4gQ29tICRuPTY0JCBlICRcXGFscGhhPTAsMDUkLCBvYnRldmUtc2UgJFxcYmFye1h9ID0gNDkyJC4gQ2FsY3VsZSBhIGVzdGF0w61zdGljYSAkWl97XFx0ZXh0e2NhbGN9fSQgZSBkZXRlcm1pbmUgc2UgcmVqZWl0YW1vcyAkSF8wJC4iLCAiZGljYSI6ICJVdGlsaXplICRaX3tcXHRleHR7Y2FsY319ID0gKFxcYmFye1h9IC0gXFxtdV8wKSAvIChcXHNpZ21hIC8gXFxzcXJ0e259KSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIFBhcsOibWV0cm9zOiAkXFxtdV8wID0gNTAwJCwgJFxcc2lnbWEgPSBcXHNxcnR7NDAwfSA9IDIwJCwgJG4gPSA2NCQsICRcXGJhcntYfSA9IDQ5MiQuIiwgIjIuIEVycm8gcGFkcsOjbzogJEVQKFxcYmFye1h9KSA9IDIwIC8gXFxzcXJ0ezY0fSA9IDIwIC8gOCA9IDIsNSQuIiwgIjMuIEVzdGF0w61zdGljYSBjYWxjdWxhZGE6ICRaX3tcXHRleHR7Y2FsY319ID0gKDQ5MiAtIDUwMCkgLyAyLDUgPSAtOCAvIDIsNSA9IC0zLDIkLiIsICI0LiBEZWNpc8OjbzogUGFyYSB1bSB0ZXN0ZSBiaWNhdWRhbCBjb20gJFxcYWxwaGEgPSAwLDA1JCwgbyB2YWxvciBjcsOtdGljbyDDqSAkWl97XFx0ZXh0e2NyaXR9fSA9IFxccG0gMSw5NiQuIiwgIjUuIENvbW8gJHwtMywyfCA+IDEsOTYkLCByZWplaXRhbW9zICRIXzAkIGFvIG7DrXZlbCBkZSA1JS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiwgcC4gMzQwIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogLTMuMn1dfQ==').decode('utf-8'))


    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    import scipy.stats as stats
    
    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do total de exercícios
    total_mcq = len(dados_exercicios.get("questoes_multipla_escolha", []))
    total_disc = len(dados_exercicios.get("questoes_discursivas", []))
    total_exercicios = total_mcq + total_disc
    
    # Barra de progresso
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    if total_exercicios > 0:
        progresso = acertos / total_exercicios
        st.progress(progresso)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    
    st.divider()
    
    # Processamento das questões de múltipla escolha
    for i, questao in enumerate(dados_exercicios.get("questoes_multipla_escolha", [])):
        st.subheader(f"Questão MCQ {i + 1}")
        st.write(questao.get("enunciado", ""))
        
        # Exibir referência se existir
        if questao.get("referencia_livro"):
            st.markdown(f"📖 *Referência: {questao['referencia_livro']}*")
            
        # Plotly Dinâmico
        cod_plotly = questao.get("codigo_plotly")
        if cod_plotly:
            local_vars = {"go": go, "stats": stats, "np": np}
            try:
                exec(cod_plotly, globals(), local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
            except Exception as e:
                st.error(f"Erro ao renderizar gráfico: {e}")
    
        # Alternativas
        alternativas = questao.get("alternativas", {})
        escolha = st.radio("Escolha uma alternativa:", list(alternativas.values()), key=f"radio_mcq_{i}", index=None)
        
        # Botão de dica
        if st.button("💡 Dica", key=f"dica_mcq_{i}"):
            st.info(questao.get("dica", "Dica indisponível"))
            
        # Verificação
        if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
            if escolha == alternativas.get(questao.get("alternativa_correta")):
                st.success("Correto! Muito bem.")
                st.session_state.respostas_certas[f"mcq_{i}"] = True
            else:
                st.error("Resposta incorreta. Tente novamente!")
                st.session_state.respostas_certas[f"mcq_{i}"] = False
                
        with st.expander("✅ Ver Gabarito Comentado"):
            st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
        st.divider()
    
    # Processamento das questões discursivas
    for i, questao in enumerate(dados_exercicios.get("questoes_discursivas", [])):
        st.subheader(f"Questão Discursiva {i + 1}")
        st.write(questao.get("enunciado", ""))
        
        if questao.get("referencia_livro"):
            st.markdown(f"📖 *Referência: {questao['referencia_livro']}*")
            
        st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
        
        # Lógica de validação numérica
        esperada = questao.get("resposta_numerica_esperada")
        if esperada is not None:
            user_val = st.number_input("Digite o resultado numérico para validação:", format="%.4f", key=f"num_disc_{i}")
            if st.button("Validar Cálculo", key=f"btn_calc_disc_{i}"):
                if abs(user_val - esperada) <= max(0.01, 0.01 * abs(esperada)):
                    st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.error("O valor calculado difere do gabarito. Verifique seus arredondamentos.")
                    st.session_state.respostas_certas[f"disc_{i}"] = False
        else:
            if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                st.session_state.respostas_certas[f"disc_{i}"] = True
            else:
                st.session_state.respostas_certas[f"disc_{i}"] = False
                
        if st.button("💡 Dica", key=f"dica_disc_{i}"):
            st.info(questao.get("dica", "Dica indisponível"))
            
        with st.expander("✅ Ver Resolução Detalhada"):
            for passo in questao.get("gabarito_passo_a_passo", []):
                st.write(f"- {passo}")
        st.divider()
