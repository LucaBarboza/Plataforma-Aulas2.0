import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4xOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogQXMgaGlww7N0ZXNlcyBlc3RhdMOtc3RpY2FzIiwgInJlZmVyZW5jaWFzX2JpYmxpb2dyYWZpY2FzX2ZpbmFpcyI6IFsiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhIC0gQ2FwLiAxMiwgcHAuIDMzMS0zNDQiXX0=').decode('utf-8'))

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
    
    # Título do Subtópico
    st.header(r"A Lógica Científica da Inferência: Hipóteses Nula e Alternativa")
    
    # Prosa Teórica - Bloco 1
    st.markdown(r"""
    A lógica da inferência estatística fundamenta-se no método científico para testar afirmações sobre parâmetros populacionais desconhecidos. Este processo estrutura-se em um dualismo contrastante, servindo como o alicerce para a tomada de decisão sob incerteza.
    """)
    
    st.info(r"A hipótese nula ($H_0$) encapsula o status quo ou a ausência de efeito, enquanto a hipótese alternativa ($H_1$) articula o fenômeno novo ou a divergência que buscamos comprovar estatisticamente.")
    
    # Prosa Teórica - Bloco 2
    st.markdown(r"""
    Ao estruturarmos nossa investigação, adotamos uma postura de conservadorismo científico. Assumimos a hipótese nula como verdadeira até que evidências amostrais, quantificadas por probabilidades, tornem tal suposição implausível. Não buscamos verdades absolutas, mas sim o controle rigoroso sobre a incerteza e a quantificação do suporte empírico.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 Estrutura Formal das Hipóteses")
    st.latex(r"H_0: \theta = \theta_0 \quad \text{vs.} \quad H_1: \theta \neq \theta_0 (\text{ou } \theta > \theta_0, \text{ ou } \theta < \theta_0)")
    
    # Demonstração Analítica
    st.subheader(r"🔍 O Coração Matemático: Teste de Hipóteses")
    st.markdown(r"O procedimento de decisão segue uma sequência lógica para validar a plausibilidade dos dados frente ao modelo proposto:")
    
    st.latex(r"H_0: \theta = \theta_0")
    st.markdown(r"Definimos a distribuição do estimador sob a validade da hipótese nula:")
    st.latex(r"\hat{\theta} \sim f(\theta_0)")
    st.markdown(r"Estabelecemos o limiar de decisão através do nível de significância:")
    st.latex(r"\alpha = P(\hat{\theta} \in RC | \theta = \theta_0)")
    st.markdown(r"Calculamos a estatística de teste padronizada:")
    st.latex(r"Z_{\text{calc}} = \frac{\hat{\theta} - \theta_0}{SE(\hat{\theta})}")
    st.markdown(r"Por fim, aplicamos a regra de rejeição:")
    st.latex(r"\text{Rejeitar } H_0 \iff Z_{\text{calc}} \in RC")
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática: Verificação de Resistência")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Indústria de Parafusos")
        st.markdown(r"""
        Uma indústria de parafusos afirma que seus produtos têm uma resistência média à tração de $\mu = 155$ kg. 
        Uma empresa compradora deseja verificar se a resistência é inferior a esse valor. 
        Dada uma amostra de $n = 25$ parafusos com média $\bar{X} = 150$ kg e desvio padrão $\sigma = 20$ kg, 
        teste a afirmação com $\alpha = 5\%$.
        """)
        
        st.latex(r"\mu_0 = 155, \sigma = 20, n = 25, \bar{X} = 150, \alpha = 0,05")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Definição das hipóteses: $H_0: \mu = 155; H_1: \mu < 155$.")
        st.markdown(r"- Cálculo da estatística $Z$: $Z_{\text{calc}} = \frac{150 - 155}{20 / \sqrt{25}} = \frac{-5}{4} = -1,25$.")
        st.markdown(r"- Valor crítico para $\alpha = 0,05$ (unilateral): $Z_{\text{crit}} = -1,645$.")
        st.markdown(r"- Comparação: $-1,25 > -1,645$.")
        
        st.success(r"Como o valor de $Z_{\text{calc}}$ não se encontra na Região Crítica (RC), não possuímos evidências estatísticas suficientes ao nível de significância de $5\%$ para rejeitar a hipótese nula. Concluímos, portanto, que a amostra é consistente com a afirmação do fabricante.")
    
    # Prosa Longa Expandida
    st.subheader(r"💡 Perspectiva Epistemológica")
    st.markdown(r"""
    A inferência estatística, em sua essência, não é apenas um conjunto de algoritmos, mas uma disciplina estruturada sob o rigor epistemológico. Antes da formalização proposta por Jerzy Neyman e Egon Pearson, a avaliação de resultados científicos era frequentemente suscetível a intuições subjetivas. 
    A introdução do paradigma de testes de hipóteses permitiu que pesquisadores estabelecessem, *a priori*, um limiar de evidência, transformando a intuição em cálculo.
    """)
    
    st.warning(r"É crucial compreender que o teste de hipóteses não trata $H_0$ e $H_1$ de forma simétrica. O peso da prova recai inteiramente sobre a hipótese alternativa. Se os dados forem consistentes com $H_0$, não provamos a nula, apenas falhamos em refutá-la.")
    
    st.markdown(r"""
    Ao decidirmos, enfrentamos dois riscos fundamentais:
    1. **Erro Tipo I ($\alpha$):** Rejeitar $H_0$ quando ela é verdadeira (Falso Positivo).
    2. **Erro Tipo II ($\beta$):** Não rejeitar $H_0$ quando ela é falsa (Falso Negativo).
    
    O equilíbrio entre estes erros e o poder do teste ($1 - \beta$) define a qualidade da investigação científica. A significância estatística, embora valiosa, deve sempre ser ponderada pela relevância substantiva dos resultados no contexto industrial ou científico aplicado.
    """)

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"A Taxonomia da Decisão: Hipóteses Unilaterais e Bilaterais")
    
    # Prosa Teórica
    st.markdown(r"""
    A escolha entre um teste unilateral ou bilateral reflete a natureza da suspeita científica e os riscos associados à decisão. 
    Esta taxonomia define os parâmetros ontológicos da investigação estatística, determinando como o rigor do formalismo matemático se traduz em segurança operacional.
    """)
    
    st.info(r"A escolha entre uma via unilateral ou bilateral não é meramente uma formalidade técnica; é uma declaração de intenções sobre o que o pesquisador considera ser uma evidência capaz de refutar a hipótese de estabilidade.")
    
    st.markdown(r"""
    - **Testes Unilaterais:** Empregados quando o interesse prático se concentra estritamente em uma direção. Ao alocar o nível de significância $\alpha$ em uma única cauda, aumenta-se a sensibilidade do teste para detectar efeitos naquele sentido específico.
    - **Testes Bilaterais:** Obrigatórios quando qualquer desvio, para mais ou para menos, compromete a operação. Representam uma postura conservadora frente a processos onde a falha é multidirecional.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Formalismo das Regiões Críticas")
    st.markdown(r"A alocação da Região Crítica (RC) deve ser definida a priori, garantindo a integridade do teste:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.latex(r"RC_{\text{bilateral}} = \{\hat{\theta} : \hat{\theta} < \theta_{c1} \text{ ou } \hat{\theta} > \theta_{c2}\}")
    with col2:
        st.latex(r"RC_{\text{unilateral}} = \{\hat{\theta} : \hat{\theta} > \theta_c\}")
    
    # Demonstração Analítica
    st.markdown(r"---")
    st.markdown(r"**Desenvolvimento Analítico das Hipóteses:**")
    st.latex(r"H_1: \theta \neq \theta_0 \implies P(|Z| > Z_{\text{crit}}) = \alpha")
    st.latex(r"P(Z < -Z_{\alpha/2}) + P(Z > Z_{\alpha/2}) = \alpha")
    st.latex(r"H_1: \theta > \theta_0 \implies P(Z > Z_{\alpha}) = \alpha")
    st.latex(r"t_{\text{calc}} = \frac{\bar{X} - \mu_0}{S/\sqrt{n}}")
    
    # Simulador de Regiões Críticas
    st.markdown(r"---")
    st.markdown(r"### 📊 Simulador: Visualização de Regiões Críticas")
    
    tipo_teste = st.toggle(r"Ativar Teste Unilateral (Direita)", key=r"toggle_tipo_subtopico_2")
    alfa = st.slider(r"Nível de Significância (\alpha)", 0.01, 0.10, 0.05, step=0.01, key=r"slider_alfa_subtopico_2")
    
    x = np.linspace(-4, 4, 200)
    y = stats.norm.pdf(x, 0, 1)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Distribuição Z', line=dict(color='#1E3A8A', width=2)))
    
    if tipo_teste:
        z_crit = stats.norm.ppf(1 - alfa)
        x_fill = np.linspace(z_crit, 4, 100)
        fig.add_trace(go.Scatter(x=x_fill, y=stats.norm.pdf(x_fill, 0, 1), fill='tozeroy', name='RC', fillcolor='#991B1B'))
    else:
        z_crit = stats.norm.ppf(1 - alfa/2)
        x_fill_neg = np.linspace(-4, -z_crit, 100)
        x_fill_pos = np.linspace(z_crit, 4, 100)
        fig.add_trace(go.Scatter(x=x_fill_neg, y=stats.norm.pdf(x_fill_neg, 0, 1), fill='tozeroy', name='RC', fillcolor='#991B1B'))
        fig.add_trace(go.Scatter(x=x_fill_pos, y=stats.norm.pdf(x_fill_pos, 0, 1), fill='tozeroy', name='RC', fillcolor='#991B1B', showlegend=False))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição Z e Regiões Críticas</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Z-Score", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    if tipo_teste:
        st.info(f"Modo Unilateral: Toda a região crítica de {alfa*100:.0f}% está concentrada à direita. Z_crit = {z_crit:.3f}.")
    else:
        st.info(f"Modo Bilateral: A região crítica de {alfa*100:.0f}% está dividida em duas caudas de {alfa/2*100:.1f}%. |Z_crit| = {z_crit:.3f}.")
    
    # Exemplos Práticos
    st.markdown(r"---")
    st.subheader(r"📈 Casos de Aplicação Prática")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Calibração de Máquina de Bebidas")
        st.markdown(r"Uma indústria deseja garantir que seus equipamentos operem em $\mu = 200$ ml. O gerente suspeita de descalibração (para mais ou para menos). Amostra: $n=25, \bar{X}=195, S=10, \alpha=5\%$.")
        st.latex(r"\mu_0 = 200, n = 25, \bar{X} = 195, S = 10, \alpha = 0,05")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- $H_0: \mu = 200; H_1: \mu \neq 200$")
        st.markdown(r"- $t_{\text{calc}} = \frac{195 - 200}{10 / \sqrt{25}} = -2,5$")
        st.markdown(r"- $|t_{\text{calc}}| = 2,5 > 2,064$ (valor crítico para $gl=24$)")
        st.success(r"Visto que $|t_{\text{calc}}| > t_{\text{crit}}$, rejeitamos a hipótese nula. Há evidências estatísticas significativas indicando descalibração, justificando a interrupção técnica.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    # Cabeçalho
    st.header(r"A Engenharia do Erro: Erros Tipo I e Tipo II no Processo Inferencial")
    
    # Introdução
    st.markdown(r"""
    A estatística inferencial não é a busca por certezas absolutas, mas a gestão inteligente da incerteza. Ao confrontarmos a realidade através da modelagem, o $H_0$ atua como nosso estado de referência — a ausência de efeito ou o equilíbrio estável.
    """)
    
    st.info(r"A falibilidade dos dados observados torna a teoria dos erros o pilar central da inferência. Sem a quantificação do risco, a decisão científica carece de rigor.")
    
    st.markdown(r"""
    **Os Pilares da Decisão Estatística:**
    - **Erro Tipo I ($\alpha$):** O "falso positivo". Rejeitar $H_0$ quando esta é verdadeira. Representa um custo de intervenção indevida.
    - **Erro Tipo II ($\beta$):** O "falso negativo". Falhar em rejeitar $H_0$ quando esta é falsa. Representa a negligência de um efeito real.
    - **Poder do Teste ($1 - \beta$):** A capacidade do teste em detectar a existência de um efeito real.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Definição dos Riscos")
    st.latex(r"\alpha = P(\text{Rejeitar } H_0 | H_0 \text{ é verdadeira})")
    st.latex(r"\beta = P(\text{Não rejeitar } H_0 | H_0 \text{ é falsa})")
    
    # Demonstração
    st.markdown(r"A dedução da fronteira crítica $k$ e a subsequente probabilidade de erro seguem o rigor da normalidade amostral:")
    st.latex(r"1 - \beta = P(\text{Rejeitar } H_0 | H_0 \text{ é falsa})")
    st.latex(r"k = \mu_0 + Z_{\text{crit}} \cdot (\sigma / \sqrt{n})")
    st.latex(r"\beta = P(\bar{X} \leq k | \mu = \mu_1)")
    st.latex(r"Z = \frac{k - \mu_1}{\sigma / \sqrt{n}}")
    
    # Simulador
    st.subheader(r"📊 Simulador de Sobreposição de Distribuições")
    col1, col2 = st.columns(2)
    with col1:
        mu1_sim = st.slider(r"Média sob H1", 100.0, 115.0, 105.0, step=0.5, key="mu1_subtopico_3")
    with col2:
        n_sim = st.slider(r"Tamanho da Amostra (n)", 10, 100, 25, step=5, key="n_subtopico_3")
    
    sigma = 10
    mu0 = 100
    alpha = 0.05
    z_crit = 1.645
    se = sigma / np.sqrt(n_sim)
    k = mu0 + z_crit * se
    
    x = np.linspace(80, 120, 500)
    y0 = norm.pdf(x, mu0, se)
    y1 = norm.pdf(x, mu1_sim, se)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y0, name=r"Distribuição H0", line=dict(color="#1E3A8A")))
    fig.add_trace(go.Scatter(x=x, y=y1, name=r"Distribuição H1", line=dict(color="#10B981")))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Simulação de Riscos e Poder</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif")),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B")),
        xaxis=dict(title=dict(text="Valores Médios", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key="plotly_chart_subtopico_3")
    
    beta_calc = norm.cdf((k - mu1_sim) / se)
    st.info(f"Com média de H1 em {mu1_sim} e n={n_sim}, o erro padrão é {se:.3f}. A probabilidade de Erro Tipo II (Beta) calculada é de aproximadamente {beta_calc:.4f}, resultando em um Poder do Teste de {(1-beta_calc)*100:.2f}%.")
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Fábrica de Componentes")
        st.markdown(r"Uma fábrica testa a vida útil das baterias: $\sigma = 10$, $n = 25$, $H_0: \mu=100$ vs $H_1: \mu=105$, com $\alpha=0,05$.")
        st.latex(r"\sigma=10, \mu_0=100, \mu_1=105, n=25, \alpha=0,05, Z_{\text{crit}}=1,645")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- $k = 100 + 1,645 \cdot (10/5) = 103,29$")
        st.markdown(r"- $Z = (103,29 - 105) / 2 = -0,855$")
        st.success(r"A probabilidade de Erro Tipo II é de 19,63%. Há uma chance de 19,6% de falharmos em detectar uma melhoria para 105 horas.")
    
    # Encerramento
    st.markdown(r"""
    A engenharia do erro nos ensina que todo teste estatístico é uma tecnologia de gestão de riscos. A busca pelo equilíbrio entre $\alpha$ e $\beta$ não é apenas um cálculo, mas uma escolha consciente sobre o que estamos dispostos a tolerar em nome da precisão científica.
    """)

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4xOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogQXMgaGlww7N0ZXNlcyBlc3RhdMOtc3RpY2FzIiwgInF1ZXN0b2VzX211bHRpcGxhX2VzY29saGEiOiBbeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIHV0aWxpemEgdW0gcHJvY2Vzc28gYXV0b21hdGl6YWRvIG9uZGUgYSB2aWRhIMO6dGlsIG3DqWRpYSBkb3Mgc2Vuc29yZXMgw6kgZGUgJFxcbXUgPSA1MDAwJCBob3Jhcy4gUGFyYSBtb25pdG9yYXIgYSBxdWFsaWRhZGUsIHVtYSBlcXVpcGUgZGUgZW5nZW5oYXJpYSBzdXNwZWl0YSBxdWUgdW1hIHJlY2VudGUgYWx0ZXJhw6fDo28gbm8gZm9ybmVjZWRvciBkZSBtYXTDqXJpYS1wcmltYSBjYXVzb3UgdW0gZGVzdmlvIG5hIHZpZGEgw7p0aWwuIEVsZXMgZGVjaWRlbSByZWFsaXphciB1bSB0ZXN0ZSBkZSBoaXDDs3Rlc2VzIGEgcGFydGlyIGRlIHVtYSBhbW9zdHJhIGRlICRuID0gMTAwJCBzZW5zb3Jlcy4gUXVhbCBkYXMgZm9ybXVsYcOnw7VlcyBhYmFpeG8gcmVwcmVzZW50YSBjb3JyZXRhbWVudGUgYSBsw7NnaWNhIGNpZW50w61maWNhIGRlIHRlc3RlIHBhcmEgdmVyaWZpY2FyIHNlIGhvdXZlIGFsdGVyYcOnw6NvIG5hIHZpZGEgw7p0aWwgbcOpZGlhIChzZWphIHBhcmEgbWFpcyBvdSBwYXJhIG1lbm9zKT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIiRIXzA6IFxcbXUgPSA1MDAwJCB2cyAkSF8xOiBcXG11ID4gNTAwMCQiLCAiQiI6ICIkSF8wOiBcXG11ID0gNTAwMCQgdnMgJEhfMTogXFxtdSBcXG5lcSA1MDAwJCIsICJDIjogIiRIXzA6IFxcbXUgXFxuZXEgNTAwMCQgdnMgJEhfMTogXFxtdSA9IDUwMDAkIiwgIkQiOiAiJEhfMDogXFxtdSA+IDUwMDAkIHZzICRIXzE6IFxcbXUgPSA1MDAwJCIsICJFIjogIiRIXzA6IFxcbXUgPCA1MDAwJCB2cyAkSF8xOiBcXG11ID0gNTAwMCQifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgYSBoaXDDs3Rlc2UgbnVsYSByZXByZXNlbnRhIG8gc3RhdHVzIHF1byBvdSBhIGF1c8OqbmNpYSBkZSBlZmVpdG8sIGVucXVhbnRvIGEgaGlww7N0ZXNlIGFsdGVybmF0aXZhIGJ1c2NhIGNhcHR1cmFyIHF1YWxxdWVyIGV2aWTDqm5jaWEgZGUgbXVkYW7Dp2Egc2lnbmlmaWNhdGl2YSwgc2VqYSBlbGEgZW0gcXVlIGRpcmXDp8OjbyBmb3IuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGhpcMOzdGVzZSBudWxhICRIXzAkIMOpIG8gcG9udG8gZGUgcGFydGlkYSBxdWUgYXNzdW1lIG8gc3RhdHVzIHF1bywgb3Ugc2VqYSwgcXVlIGEgbcOpZGlhIHBvcHVsYWNpb25hbCBwZXJtYW5lY2UgJFxcbXUgPSA1MDAwJC4gQ29tbyBhIHN1c3BlaXRhIGRvcyBlbmdlbmhlaXJvcyDDqSBkZSBxdWUgaG91dmUgdW1hICdhbHRlcmHDp8OjbycgKHNlbSBlc3BlY2lmaWNhciBzZSBhdW1lbnRvdSBvdSBkaW1pbnVpdSksIGEgaGlww7N0ZXNlIGFsdGVybmF0aXZhICRIXzEkIGRldmUgc2VyIGJpbGF0ZXJhbCwgb3Ugc2VqYSwgJFxcbXUgXFxuZXEgNTAwMCQuIFBvcnRhbnRvLCBhIGFsdGVybmF0aXZhIGNvcnJldGEgw6kgQi4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzMzgifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZW5zYWlvIGNsw61uaWNvLCBwZXNxdWlzYWRvcmVzIHRlc3RhbSBzZSB1bSBub3ZvIG1lZGljYW1lbnRvIHJlZHV6IGEgcHJlc3PDo28gYXJ0ZXJpYWwgc2lzdMOzbGljYS4gTyB2YWxvciBwYWRyw6NvIHNlbSB0cmF0YW1lbnRvIMOpIGRlICQxNDAkIG1tSGcuIEEgaGlww7N0ZXNlIG51bGEgZXN0YWJlbGVjaWRhIMOpICRIXzA6IFxcbXUgPSAxNDAkIGUgYSBhbHRlcm5hdGl2YSDDqSAkSF8xOiBcXG11IDwgMTQwJC4gU2UgbyBwLXZhbG9yIG9idGlkbyBmb3IgaWd1YWwgYSAkMCwwMiQgZSBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBmaXhhZG8gZm9yICRcXGFscGhhID0gMCwwNSQsIHF1YWwgw6kgYSBkZWNpc8OjbyBlc3RhdMOtc3RpY2EgY29ycmV0YSBiYXNlYWRhIG5hIGzDs2dpY2EgZGUgaW5mZXLDqm5jaWE/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJSZWplaXRhciAkSF8wJCBwb3JxdWUgbyBwLXZhbG9yIMOpIG1lbm9yIHF1ZSAkXFxhbHBoYSQuIiwgIkIiOiAiTsOjbyByZWplaXRhciAkSF8wJCBwb3JxdWUgbyBwLXZhbG9yIMOpIG1lbm9yIHF1ZSAkXFxhbHBoYSQuIiwgIkMiOiAiUmVqZWl0YXIgJEhfMCQgcG9ycXVlIG8gcC12YWxvciDDqSBtYWlvciBxdWUgJFxcYWxwaGEkLiIsICJEIjogIk7Do28gcmVqZWl0YXIgJEhfMCQgcG9ycXVlIG8gcC12YWxvciDDqSBtYWlvciBxdWUgJFxcYWxwaGEkLiIsICJFIjogIkNvbmNsdWlyIHF1ZSBvIG1lZGljYW1lbnRvIG7Do28gdGVtIGVmZWl0byBwb2lzIG8gcC12YWxvciDDqSBwcsOzeGltbyBkZSB6ZXJvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTyBwLXZhbG9yIHJlcHJlc2VudGEgYSBwcm9iYWJpbGlkYWRlIGRlIG9ic2VydmFyIHJlc3VsdGFkb3MgdMOjbyBleHRyZW1vcyBxdWFudG8gb3MgZW5jb250cmFkb3MsIGFzc3VtaW5kbyBxdWUgYSBoaXDDs3Rlc2UgbnVsYSDDqSB2ZXJkYWRlaXJhLiBTZSBlc3NhIHByb2JhYmlsaWRhZGUgZm9yIG11aXRvIGJhaXhhIChtZW5vciBxdWUgJFxcYWxwaGEkKSwgdGVtb3MgZXZpZMOqbmNpYXMgcGFyYSBxdWVzdGlvbmFyICRIXzAkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTm8gdGVzdGUgZGUgaGlww7N0ZXNlcywgY29tcGFyYW1vcyBvIHAtdmFsb3IgY29tIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJC4gU2UgJHBcXHRleHR7LXZhbG9yfSBcXGxlIFxcYWxwaGEkLCByZWplaXRhbW9zIGEgaGlww7N0ZXNlIG51bGEsIHBvaXMgYSBwcm9iYWJpbGlkYWRlIGRlIG9ic2VydmFyIHRhbCBldmlkw6puY2lhIHNvYiBhIMOpZ2lkZSBkZSAkSF8wJCDDqSBzdWZpY2llbnRlbWVudGUgcGVxdWVuYSBwYXJhIGNvbnNpZGVyw6EtbGEgaW1wbGF1c8OtdmVsLiBDb21vICQwLDAyIDwgMCwwNSQsIHJlamVpdGFtb3MgJEhfMCQuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVstNCwgLTIsIDAsIDIsIDRdLCB5PVswLjA1LCAwLjI1LCAwLjQsIDAuMjUsIDAuMDVdLCBtb2RlPSdsaW5lcycsIG5hbWU9J0Rpc3RyaWJ1acOnw6NvIHNvYiBIMCcsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScpKSlcbmZpZy5hZGRfc2hhcGUodHlwZT0ncmVjdCcsIHgwPS00LCB5MD0wLCB4MT0tMS45NiwgeTE9MC4wNSwgZmlsbGNvbG9yPScjOTkxQjFCJywgb3BhY2l0eT0wLjUsIGxheWVyPSdiZWxvdycsIG5hbWU9J1JlZ2nDo28gQ3LDrXRpY2EnKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J1Zpc3VhbGl6YcOnw6NvIGRhIFJlZ2nDo28gQ3LDrXRpY2EgKFJDKSBlIFAtdmFsb3InLCB4YXhpc190aXRsZT0nRXN0YXTDrXN0aWNhIGRlIFRlc3RlJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNDAifSwgeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIHV0aWxpemEgdW0gcHJvY2Vzc28gYXV0b21hdGl6YWRvIHBhcmEgYSBzb2xkYWdlbSBkZSBwbGFjYXMgZGUgY2lyY3VpdG8uIE8gcGFkcsOjbyBkZSBxdWFsaWRhZGUgZXhpZ2UgcXVlIGEgdmFyacOibmNpYSBkbyB0ZW1wbyBkZSBzb2xkYWdlbSBzZWphIGV4YXRhbWVudGUgJFxcc2lnbWFeMiA9IDI1JCBtcyReMiQuIEEgZ2Vyw6puY2lhIGRlIHF1YWxpZGFkZSBlc3TDoSBwcmVvY3VwYWRhIGNvbSBhIGVzdGFiaWxpZGFkZSBkbyBwcm9jZXNzbyBlIGRlc2VqYSBpZGVudGlmaWNhciBkZXN2aW9zIGVtIHF1YWxxdWVyIGRpcmXDp8OjbyAodGFudG8gcGFyYSB0ZW1wb3MgZGUgc29sZGFnZW0gbWFpcyBsb25nb3MsIHF1ZSBpbmRpY2FtIGZhbGhhcyBkZSBhcXVlY2ltZW50bywgcXVhbnRvIG1haXMgY3VydG9zLCBxdWUgc3VnZXJlbSByaXNjb3MgZGUgc29sZGEgZnJpYSkuIEVtIHVtYSBhbW9zdHJhIGRlICRuPTEwJCBwbGFjYXMsIGZvaSBjYWxjdWxhZGEgYSB2YXJpw6JuY2lhIGFtb3N0cmFsICRTXjIgPSA0MiQuIFBhcmEgZXN0ZSBjZW7DoXJpbyBkZSBjb250cm9sZSBkZSBxdWFsaWRhZGUsIHF1YWwgZGV2ZSBzZXIgYSBlc3RydXR1cmEgZGFzIGhpcMOzdGVzZXM/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIkSF8wOiBcXHNpZ21hXjIgPSAyNSQgdnMgJEhfMTogXFxzaWdtYV4yID4gMjUkLCB1dGlsaXphbmRvIHVtIHRlc3RlIHVuaWxhdGVyYWwgw6AgZGlyZWl0YS4iLCAiQiI6ICIkSF8wOiBcXHNpZ21hXjIgPSAyNSQgdnMgJEhfMTogXFxzaWdtYV4yIDwgMjUkLCB1dGlsaXphbmRvIHVtIHRlc3RlIHVuaWxhdGVyYWwgw6AgZXNxdWVyZGEuIiwgIkMiOiAiJEhfMDogXFxzaWdtYV4yID0gMjUkIHZzICRIXzE6IFxcc2lnbWFeMiBcXG5lcSAyNSQsIHV0aWxpemFuZG8gdW0gdGVzdGUgYmlsYXRlcmFsIGNvbSByZWdpw6NvIGRlIHJlamVpw6fDo28gZGl2aWRpZGEgZW0gZHVhcyBjYXVkYXMuIiwgIkQiOiAiJEhfMDogXFxzaWdtYV4yIFxcbmVxIDI1JCB2cyAkSF8xOiBcXHNpZ21hXjIgPSAyNSQsIGZvY2FuZG8gbmEgYWNlaXRhw6fDo28gZGEgZXN0YWJpbGlkYWRlLiIsICJFIjogIiRIXzA6IFxcc2lnbWFeMiA9IDQyJCB2cyAkSF8xOiBcXHNpZ21hXjIgPSAyNSQsIHRlc3RhbmRvIGEgaWd1YWxkYWRlIMOgIGFtb3N0cmEgb2JzZXJ2YWRhLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiUmVmbGl0YSBzZSBhIHByZW9jdXBhw6fDo28gZGEgZ2Vyw6puY2lhIMOpIGRpcmVjaW9uYWRhIHBhcmEgdW0gZG9zIGxhZG9zIGRhIG3DqWRpYSBkZSB2YXJpw6JuY2lhIG91IHNlIGFtYm9zIG9zIGRlc3Zpb3MsIHBhcmEgbWFpcyBvdSBwYXJhIG1lbm9zLCBzw6NvIHByZWp1ZGljaWFpcyBhbyBwcm9jZXNzbyBpbmR1c3RyaWFsLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBlc2NvbGhhIGNvcnJldGEgw6kgYSBDLiBFbSBwcm9jZXNzb3MgZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlLCBxdWFuZG8gcXVhbHF1ZXIgZGVzdmlvIGVtIHJlbGHDp8OjbyBhbyB2YWxvciBub21pbmFsIChzZWphIHBhcmEgbWFpcyBvdSBwYXJhIG1lbm9zKSDDqSBpbmRlc2VqYWRvLCBhIGhpcMOzdGVzZSBhbHRlcm5hdGl2YSBkZXZlIGFicmFuZ2VyIHRvZG8gbyBlc3BlY3RybyBkZSB2YXJpYcOnw6NvIHBvc3PDrXZlbCAoJFxuZXEkKS4gQ29uc2VxdWVudGVtZW50ZSwgbyB0ZXN0ZSBkZXZlIHNlciBiaWxhdGVyYWwsIGFsb2NhbmRvIGEgcmVnacOjbyBjcsOtdGljYSAoUkMpIG5hcyBkdWFzIGNhdWRhcyBkYSBkaXN0cmlidWnDp8OjbyBwYXJhIG1vbml0b3JhciBkZXN2aW9zIHNpZ25pZmljYXRpdm9zIGVtIHF1YWxxdWVyIHNlbnRpZG8uIEFsdGVybmF0aXZhcyB1bmlsYXRlcmFpcyAoQSBlIEIpIHNlcmlhbSBhcHJvcHJpYWRhcyBhcGVuYXMgc2UgYSBwcmVvY3VwYcOnw6NvIGZvc3NlIGVzdHJpdGFtZW50ZSBkaXJlY2lvbmFkYSwgbyBxdWUgbsOjbyDDqSBvIGNhc28uIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgwLCA1MCwgMjAwKVxueSA9IHN0YXRzLlxcY2hpMi5wZGYoeCwgZGY9OSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbmFtZT1cIkRpc3RyaWJ1acOnw6NvICRcXGNoaV4yKDkpJFwiLCBsaW5lPWRpY3QoY29sb3I9XCIjMUUzQThBXCIsIHdpZHRoPTMpKSlcbmZpZy5hZGRfdnJlY3QoeDA9MCwgeDE9Mi43LCBmaWxsY29sb3I9XCIjOTkxQjFCXCIsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTAsIG5hbWU9XCJSQyBFc3F1ZXJkYVwiKVxuZmlnLmFkZF92cmVjdCh4MD0xOS4wMiwgeDE9NTAsIGZpbGxjb2xvcj1cIiM5OTFCMUJcIiwgb3BhY2l0eT0wLjMsIGxpbmVfd2lkdGg9MCwgbmFtZT1cIlJDIERpcmVpdGFcIilcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPVwiPGI+UmVnacO1ZXMgQ3LDrXRpY2FzIHBhcmEgVGVzdGUgQmlsYXRlcmFsICgkXFxhbHBoYT0wLjA1JCk8L2I+XCIsIHhheGlzPWRpY3QodGl0bGU9clwiRXN0YXTDrXN0aWNhICRcXGNoaV4yX3tcXHRleHR7Y2FsY319JFwiKSwgeWF4aXM9ZGljdCh0aXRsZT1yXCJEZW5zaWRhZGVcIikpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW0gZW5nZW5oZWlybyBkZSBtYXRlcmlhaXMgdGVzdGEgYSByZXNpc3TDqm5jaWEgw6AgdHJhw6fDo28gZGUgdW1hIG5vdmEgbGlnYSBtZXTDoWxpY2EuIE8gcGFkcsOjbyBkYSBsaWdhIGF0dWFsIHRlbSBtw6lkaWEgZGUgcmVzaXN0w6puY2lhICRcXG11ID0gNTAwJCBNUGEuIEEgZW1wcmVzYSBzw7MgaW52ZXN0aXLDoSBuYSBub3ZhIGxpZ2Egc2UgaG91dmVyIGV2aWTDqm5jaWEgZXN0YXTDrXN0aWNhIGRlIHF1ZSBlbGEgw6kgc3VwZXJpb3IgYW8gcGFkcsOjbyBhdHVhbC4gU2UgbyBlbmdlbmhlaXJvIG9idGl2ZXIgdW1hIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0gPSA1MTUkIE1QYSwgY29tbyBkZXZlIGVzdHJ1dHVyYXIgc3VhcyBoaXDDs3Rlc2VzIHBhcmEgZ2FyYW50aXIgcXVlIG8gdGVzdGUgZm9xdWUgZXhjbHVzaXZhbWVudGUgbmEgaGlww7N0ZXNlIGRlIGdhbmhvIGRlIGRlc2VtcGVuaG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIkSF8wOiBcXG11ID0gNTAwJCB2cyAkSF8xOiBcXG11IFxcbmVxIDUwMCQsIHRlc3RhbmRvIHF1YWxxdWVyIGRpZmVyZW7Dp2EgZGUgcmVzaXN0w6puY2lhLiIsICJCIjogIiRIXzA6IFxcbXUgPSA1MDAkIHZzICRIXzE6IFxcbXUgPiA1MDAkLCB1dGlsaXphbmRvIHVtIHRlc3RlIHVuaWxhdGVyYWwgw6AgZGlyZWl0YSBwYXJhIGNhcHR1cmFyIGEgc3VwZXJpb3JpZGFkZS4iLCAiQyI6ICIkSF8wOiBcXG11ID0gNTAwJCB2cyAkSF8xOiBcXG11IDwgNTAwJCwgdGVzdGFuZG8gc2UgYSBub3ZhIGxpZ2Egw6kgaW5mZXJpb3IuIiwgIkQiOiAiJEhfMDogXFxtdSA+IDUwMCQgdnMgJEhfMTogXFxtdSA9IDUwMCQsIGZvY2FuZG8gbmEgcHJvdmEgZGUgc3VwZXJpb3JpZGFkZS4iLCAiRSI6ICIkSF8wOiBcXG11IFxcbGVxIDUwMCQgdnMgJEhfMTogXFxtdSBcXGdlcSA1MDAkLCBnYXJhbnRpbmRvIGNvYmVydHVyYSB0b3RhbCBkZSByZXN1bHRhZG9zLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTyBvYmpldGl2byBwcsOhdGljbyDDqSB2ZXJpZmljYXIgc2UgYSByZXNpc3TDqm5jaWEgYXVtZW50b3UuIEEgZXN0cnV0dXJhIGRvIHRlc3RlIGRldmUgc2VyIHNlbnPDrXZlbCBhIHZhbG9yZXMgcXVlIGNvbmZpcm1lbSBlc3NhIGNyZW7Dp2EgZXNwZWPDrWZpY2EsIGFsb2NhbmRvIHRvZG8gbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEkIGVtIHVtYSDDum5pY2EgY2F1ZGEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGFsdGVybmF0aXZhIGNvcnJldGEgw6kgYSBCLiBPIHRlc3RlIHVuaWxhdGVyYWwgw6kgYSB0cmFkdcOnw6NvIG1hdGVtw6F0aWNhIGRhIGTDunZpZGEgY2llbnTDrWZpY2E6IG8gZW5nZW5oZWlybyBidXNjYSB2YWxpZGFyIHVtYSBzdXBlcmlvcmlkYWRlLiBDb2xvY2FyICRIXzE6IFxcbXUgPiA1MDAkIHBlcm1pdGUgYWxvY2FyIGEgcmVnacOjbyBjcsOtdGljYSBuYSBjYXVkYSBzdXBlcmlvciwgYXVtZW50YW5kbyBhIHNlbnNpYmlsaWRhZGUgZG8gdGVzdGUgcGFyYSBkZXRlY3RhciBlZmVpdG9zIG5lc3NhIGRpcmXDp8Ojby4gQXMgb3V0cmFzIG9ww6fDtWVzIGZhbGhhbSBvdSBwb3Igc2VyZW0gYmlsYXRlcmFpcyAoZGVzbmVjZXNzw6FyaWFzIGFxdWkpIG91IHBvciBpbnZlcnRlcmVtIGEgZGlyZcOnw6NvIGRhIGhpcMOzdGVzZSBkZSBpbnRlcmVzc2UuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSg0ODAsIDUyMCwgMjAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgsIGxvYz01MDAsIHNjYWxlPTUpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9XCJEaXN0cmlidWnDp8OjbyBzb2IgJEhfMCRcIiwgbGluZT1kaWN0KGNvbG9yPVwiIzFFM0E4QVwiLCB3aWR0aD0zKSkpXG5maWcuYWRkX3ZyZWN0KHgwPTUwOC4yLCB4MT01MjAsIGZpbGxjb2xvcj1cIiM5OTFCMUJcIiwgb3BhY2l0eT0wLjMsIGxpbmVfd2lkdGg9MCwgbmFtZT1cIlJDIFVuaWxhdGVyYWwgKCRcXGFscGhhPTAuMDUkKVwiKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9XCI8Yj5SZWdpw6NvIENyw610aWNhIFVuaWxhdGVyYWwgw6AgRGlyZWl0YTwvYj5cIiwgeGF4aXM9ZGljdCh0aXRsZT1yXCJSZXNpc3TDqm5jaWEgKCRcXGJhcntYfSQpXCIpLCB5YXhpcz1kaWN0KHRpdGxlPXJcIkRlbnNpZGFkZVwiKSkiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiJ9LCB7ImVudW5jaWFkbyI6ICJVbWEgcmVmaW5hcmlhIGRlIHBldHLDs2xlbyB1dGlsaXphIHVtIHNlbnNvciBkZSBwcmVzc8OjbyBlbSBzdWFzIHR1YnVsYcOnw7VlcyBwcmluY2lwYWlzLiBBIGhpcMOzdGVzZSBudWxhICRIXzAkIMOpIHF1ZSBvIHNpc3RlbWEgZXN0w6Egb3BlcmFuZG8gZW0gY29uZGnDp8O1ZXMgbm9ybWFpcyAoJFxcbXUgPSA1MCQgXFxiYXIpLCBlbnF1YW50byBhIGhpcMOzdGVzZSBhbHRlcm5hdGl2YSAkSF8xJCDDqSBxdWUgaMOhIHVtIHZhemFtZW50byBkZXRlY3RhZG8gKCRcXG11ID0gNTUkIFxcYmFyKS4gTyBjdXN0byBkZSBwYXJhciBhIHByb2R1w6fDo28gcGFyYSBpbnNwZcOnw6NvIMOpIGFsdMOtc3NpbW8sIG1hcyBvIGN1c3RvIGRlIHVtIHZhemFtZW50byBuw6NvIGRldGVjdGFkbyDDqSBjYXRhc3Ryw7NmaWNvIHBhcmEgYSBzZWd1cmFuw6dhIGFtYmllbnRhbC4gTyBlbmdlbmhlaXJvIHJlc3BvbnPDoXZlbCBlc3RhYmVsZWNldSB1bWEgcmVncmEgZGUgZGVjaXPDo28gdGFsIHF1ZSByZWplaXRhICRIXzAkIHNlIGEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSA+IDUyJCBcXGJhci4gU2UsIGFvIHRlc3RhciwgYSBtw6lkaWEgcG9wdWxhY2lvbmFsIHJlYWwgZm9yIDUwIFxcYmFyIGUgbyBzZW5zb3IgaW5kaWNhciwgZXJyb25lYW1lbnRlLCB1bSB2YXphbWVudG8sIHF1YWwgdGlwbyBkZSBlcnJvIGZvaSBjb21ldGlkbyBlIGNvbW8gZWxlIMOpIGZvcm1hbG1lbnRlIGRlZmluaWRvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiRXJybyBUaXBvIEk6ICRQKFxcdGV4dHtSZWplaXRhciB9IEhfMCB8IEhfMCBcXHRleHR7IMOpIHZlcmRhZGVpcmF9KSA9IFAoXFxiYXJ7WH0gPiA1MiB8IFxcbXUgPSA1MCkkLiIsICJCIjogIkVycm8gVGlwbyBJSTogJFAoXFx0ZXh0e07Do28gcmVqZWl0YXIgfSBIXzAgfCBIXzAgXFx0ZXh0eyDDqSBmYWxzYX0pID0gUChcXGJhcntYfSBcXGxlIDUyIHwgXFxtdSA9IDU1KSQuIiwgIkMiOiAiRXJybyBUaXBvIEk6ICRQKFxcdGV4dHtOw6NvIHJlamVpdGFyIH0gSF8wIHwgSF8wIFxcdGV4dHsgw6kgZmFsc2F9KSA9IFAoXFxiYXJ7WH0gXFxsZSA1MiB8IFxcbXUgPSA1NSkkLiIsICJEIjogIkVycm8gVGlwbyBJSTogJFAoXFx0ZXh0e1JlamVpdGFyIH0gSF8wIHwgSF8wIFxcdGV4dHsgw6kgdmVyZGFkZWlyYX0pID0gUChcXGJhcntYfSA+IDUyIHwgXFxtdSA9IDUwKSQuIiwgIkUiOiAiTmVuaHVtYSBkYXMgYW50ZXJpb3Jlcy4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIkxlbWJyZS1zZSBkZSBxdWUgbyBFcnJvIFRpcG8gSSBvY29ycmUgcXVhbmRvIHRvbWFtb3MgdW1hIGHDp8OjbyBjb3JyZXRpdmEgKHJlamVpdGFyICRIXzAkKSBxdWFuZG8sIG5hIHZlcmRhZGUsIG8gcHJvY2Vzc28gZXN0YXZhIHNvYiBjb250cm9sZS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIk8gRXJybyBUaXBvIEkgKGZhbHNvIHBvc2l0aXZvKSBjb25zaXN0ZSBlbSByZWplaXRhciBhIGhpcMOzdGVzZSBudWxhICRIXzAkIHF1YW5kbyBlbGEgw6ksIG5hIHZlcmRhZGUsIHZlcmRhZGVpcmEuIE5vIGNvbnRleHRvIGRvIHByb2JsZW1hLCBvIHByb2Nlc3NvIGVzdMOhIHNvYiBjb250cm9sZSAoJFxcbXU9NTAkKSBlIG8gZW5nZW5oZWlybyBlcnJvbmVhbWVudGUgY29uY2x1aSBxdWUgaMOhIHZhemFtZW50byAoJFxcYmFye1h9ID4gNTIkKS4gQSBkZWZpbmnDp8OjbyBmb3JtYWwgw6kgJFxcYWxwaGEgPSBQKFxcdGV4dHtSZWplaXRhciB9IEhfMCB8IEhfMCBcXHRleHR7IMOpIHZlcmRhZGVpcmF9KSQsIHF1ZSBjb3JyZXNwb25kZSBhICRQKFxcYmFye1h9ID4gNTIgfCBcXG11ID0gNTApJC4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDQ1LCA2MCwgMTAwMClcbnlfaDAgPSAoMSAvICgyICogbnAuXFxzcXJ0KDIgKiBucC5cXHBpKSkpICogbnAuXFxleHAoLTAuNSAqICgoeCAtIDUwKSAvIDIpKioyKVxueV9oMSA9ICgxIC8gKDIgKiBucC5cXHNxcnQoMiAqIG5wLlxccGkpKSkgKiBucC5cXGV4cCgtMC41ICogKCh4IC0gNTUpIC8gMikqKjIpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXlfaDAsIG5hbWU9clwiJEhfMCAoXFxtdT01MCkkXCIsIGxpbmU9ZGljdChjb2xvcj1cIiMxRTNBOEFcIiwgd2lkdGg9MykpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15X2gxLCBuYW1lPXJcIiRIXzEgKFxcbXU9NTUpJFwiLCBsaW5lPWRpY3QoY29sb3I9XCIjOTkxQjFCXCIsIHdpZHRoPTMpKSlcbmZpZy5hZGRfc2hhcGUodHlwZT1cImxpbmVcIiwgeDA9NTIsIHkwPTAsIHgxPTUyLCB5MT0wLjI1LCBsaW5lPWRpY3QoY29sb3I9XCIjRjU5RTBCXCIsIHdpZHRoPTIsIGRhc2g9XCJkYXNoXCIpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9XCI8Yj5EaXN0cmlidWnDp8O1ZXMgZSBSZWdyYSBkZSBEZWNpc8OjbzwvYj5cIiwgeGF4aXNfdGl0bGU9clwiTcOpZGlhIEFtb3N0cmFsICgkXFxiYXJ7WH0kKVwiLCB5YXhpc190aXRsZT1cIkRlbnNpZGFkZVwiKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGVtcGxhdGU9XCJwbG90bHlfd2hpdGVcIikiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiwgcC4gMzMyIn0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVuc2FpbyBjbMOtbmljbywgdW1hIG5vdmEgZHJvZ2EgcGFyYSBoaXBlcnRlbnPDo28gZXN0w6Egc2VuZG8gdGVzdGFkYS4gJEhfMCQgYWZpcm1hIHF1ZSBhIGRyb2dhIG7Do28gw6kgc3VwZXJpb3IgYW8gcGxhY2VibyAoJFxcbXVfe1xcdGV4dHtkcm9nYX19ID0gXFxtdV97XFx0ZXh0e3BsYWNlYm99fSQpLCBlICRIXzEkIGFmaXJtYSBxdWUgYSBkcm9nYSDDqSBzdXBlcmlvciAoJFxcbXVfe1xcdGV4dHtkcm9nYX19ID4gXFxtdV97XFx0ZXh0e3BsYWNlYm99fSQpLiBTZSBvcyBwZXNxdWlzYWRvcmVzIGZhbGhhcmVtIGVtIHJlamVpdGFyICRIXzAkIHF1YW5kbyBhIGRyb2dhIMOpLCBkZSBmYXRvLCBtYWlzIGVmaWNheiwgcXVhbCBvIG5vbWUgZG8gZXJybyBlIHF1YWwgYSBzdWEgcmVsYcOnw6NvIGNvbSBvIHBvZGVyIGRvIHRlc3RlPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiRXJybyBUaXBvIEk7IG8gcG9kZXIgZG8gdGVzdGUgw6kgJFxcYWxwaGEkLiIsICJCIjogIkVycm8gVGlwbyBJSTsgbyBwb2RlciBkbyB0ZXN0ZSDDqSAkMSAtIFxcYmV0YSQuIiwgIkMiOiAiRXJybyBUaXBvIEk7IG8gcG9kZXIgZG8gdGVzdGUgw6kgJDEgLSBcXGJldGEkLiIsICJEIjogIkVycm8gVGlwbyBJSTsgbyBwb2RlciBkbyB0ZXN0ZSDDqSAkXFxiZXRhJC4iLCAiRSI6ICJFcnJvIGRlIGRlY2lzw6NvIG51bGE7IG7Do28gcmVsYWNpb25hZG8gYW8gcG9kZXIgZG8gdGVzdGUuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJPIGVycm8gZGUgbsOjbyBkZXRlY3RhciB1bSBlZmVpdG8gcmVhbCAoZmFsc28gbmVnYXRpdm8pIMOpIG8gb3Bvc3RvIGRvIHBvZGVyIGVzdGF0w61zdGljbywgcXVlIG1lZGUgYSBjYXBhY2lkYWRlIGRlIGlkZW50aWZpY2FyIG8gZWZlaXRvLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBFcnJvIFRpcG8gSUkgb2NvcnJlIHF1YW5kbyBmYWxoYW1vcyBhbyByZWplaXRhciAkSF8wJCBlbWJvcmEgZWxhIHNlamEgZmFsc2EgKCRcYlxcZXRhID0gUChcXHRleHR7TsOjbyByZWplaXRhciB9IEhfMCB8IEhfMCBcXHRleHR7IMOpIGZhbHNhfSkkKS4gTyBwb2RlciBkbyB0ZXN0ZSDDqSBhIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgJEhfMCQgY29ycmV0YW1lbnRlIHF1YW5kbyBlbGEgw6kgZmFsc2EsIHNlbmRvIGRlZmluaWRvIGNvbW8gJDEgLSBcXGJldGEkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfV0sICJxdWVzdG9lc19kaXNjdXJzaXZhcyI6IFt7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyBjb250cm9sZSBkZSBxdWFsaWRhZGUgZGUgdW1hIHBlw6dhIGluZHVzdHJpYWwgY3VqYSByZXNpc3TDqm5jaWEgw6AgdHJhw6fDo28gJFgkIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgJE4oXFxtdSwgNDAwKSQuIE8gdmFsb3IgcGFkcsOjbyBlc3BlcmFkbyDDqSAkXFxtdSA9IDIwMCQuIFN1c3BlaXRhLXNlIHF1ZSBvIG5vdm8gbG90ZSB0ZW5oYSB1bWEgcmVzaXN0w6puY2lhIG3DqWRpYSBzdXBlcmlvciBhIDIwMC4gQ29tIHVtYSBhbW9zdHJhIGRlICRuID0gMjUkIHBlw6dhcywgZGVmaW5hIGFzIGhpcMOzdGVzZXMgJEhfMCQgZSAkSF8xJCwgZSBleHBsaXF1ZSBvIHF1ZSByZXByZXNlbnRhbSwgZW0gdGVybW9zIGRlIGVycm8sIG8gRXJybyBUaXBvIEkgZSBvIEVycm8gVGlwbyBJSSBuZXN0ZSBjb250ZXh0by4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIG8gRXJybyBUaXBvIEkgw6kgcmVqZWl0YXIgYSBoaXDDs3Rlc2UgbnVsYSBxdWFuZG8gZWxhIMOpIHZlcmRhZGVpcmEsIGVucXVhbnRvIG8gRXJybyBUaXBvIElJIMOpIG7Do28gcmVqZWl0YXIgYSBudWxhIHF1YW5kbyBlbGEgw6kgZmFsc2EuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IERlZmluacOnw6NvIGRhcyBoaXDDs3Rlc2VzLiAkSF8wOiBcXG11ID0gMjAwJCAoc3RhdHVzIHF1bywgbG90ZSBwYWRyw6NvKSBlICRIXzE6IFxcbXUgPiAyMDAkIChzdXNwZWl0YSBkZSBhdW1lbnRvIG5hIHJlc2lzdMOqbmNpYSkuIiwgIlBhc3NvIDI6IEVycm8gVGlwbyBJLiDDiSBhIHByb2JhYmlsaWRhZGUgZGUgY29uY2x1aXIgcXVlIGEgcmVzaXN0w6puY2lhIGF1bWVudG91IChyZWplaXRhciAkSF8wJCkgcXVhbmRvLCBuYSB2ZXJkYWRlLCBhIHJlc2lzdMOqbmNpYSBtw6lkaWEgYWluZGEgw6kgJDIwMCQgKGxvdGUgcGFkcsOjbykuIMOJIG8gZXJybyBkZSB1bSAnZmFsc28gcG9zaXRpdm8nLiIsICJQYXNzbyAzOiBFcnJvIFRpcG8gSUkuIMOJIGEgcHJvYmFiaWxpZGFkZSBkZSBjb25jbHVpciBxdWUgYSByZXNpc3TDqm5jaWEgw6kgaWd1YWwgYSAyMDAgKG7Do28gcmVqZWl0YXIgJEhfMCQpIHF1YW5kbywgbmEgdmVyZGFkZSwgYSByZXNpc3TDqm5jaWEgbcOpZGlhIMOpIHN1cGVyaW9yIGEgMjAwLiDDiSBvIGVycm8gZGUgdW0gJ2ZhbHNvIG5lZ2F0aXZvJy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiwgcC4gMzMyIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlN1cG9uaGEgcXVlIGVzdGVqYW1vcyB0ZXN0YW5kbyAkSF8wOiBwID0gMCw1JCBjb250cmEgJEhfMTogcCBcXG5lcSAwLDUkIHBhcmEgdW1hIG1vZWRhLCB1dGlsaXphbmRvIHVtYSBhbW9zdHJhIGRlICRuID0gMTAkIGxhbsOnYW1lbnRvcy4gQSBSZWdpw6NvIENyw610aWNhIChSQykgZm9pIGRlZmluaWRhIGNvbW8gJFJDID0gXFx7MCwgMSwgMiwgOCwgOSwgMTBcXH0kIChuw7ptZXJvIGRlIGNhcmFzIG9ic2VydmFkYXMpLiBDYWxjdWxlIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCBkbyB0ZXN0ZS4iLCAiZGljYSI6ICJPIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgw6kgYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIGRhZG8gcXVlIGVsYSDDqSB2ZXJkYWRlaXJhLiBVc2UgYSBkaXN0cmlidWnDp8OjbyBCaW5vbWlhbCBjb20gJG49MTAkIGUgJHA9MCw1JDogJFAoWD1rKSA9IFxcYmlub217bn17a30gcF5rICgxLXApXntuLWt9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSBwcm9iYWJpbGlkYWRlIHNvYiAkSF8wJCDDqSAkUChYPWspID0gXFxiaW5vbXsxMH17a30gKDAsNSleezEwfSQuIiwgIkNhbGN1bGFyIGEgc29tYSBwYXJhICRrIFxcaW4gXFx7MCwgMSwgMiwgOCwgOSwgMTBcXH0kLiIsICIkUChYPTApID0gXFxiaW5vbXsxMH17MH0gKDAsNSleezEwfSA9IDEvMTAyNCQuIiwgIiRQKFg9MSkgPSBcXGJpbm9tezEwfXsxfSAoMCw1KV57MTB9ID0gMTAvMTAyNCQuIiwgIiRQKFg9MikgPSBcXGJpbm9tezEwfXsyfSAoMCw1KV57MTB9ID0gNDUvMTAyNCQuIiwgIkNvbW8gYSBkaXN0cmlidWnDp8OjbyDDqSBcXHNpbcOpdHJpY2EsICRQKFg9OCkgPSBQKFg9MikgPSA0NS8xMDI0JCwgJFAoWD05KSA9IFAoWD0xKSA9IDEwLzEwMjQkLCAkUChYPTEwKSA9IFAoWD0wKSA9IDEvMTAyNCQuIiwgIlNvbWEgJFxcYWxwaGEgPSAyIFxcdGltZXMgKDEgKyAxMCArIDQ1KSAvIDEwMjQgPSAxMTIgLyAxMDI0ID0gMCwxMDkzNzUkLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoZGF0YT1bZ28uQmFyKHg9WzAsIDEsIDIsIDMsIDQsIDUsIDYsIDcsIDgsIDksIDEwXSwgeT1bMS8xMDI0LCAxMC8xMDI0LCA0NS8xMDI0LCAxMjAvMTAyNCwgMjEwLzEwMjQsIDI1Mi8xMDI0LCAyMTAvMTAyNCwgMTIwLzEwMjQsIDQ1LzEwMjQsIDEwLzEwMjQsIDEvMTAyNF0sIG1hcmtlcl9jb2xvcj1bJyM5OTFCMUInLCAnIzk5MUIxQicsICcjOTkxQjFCJywgJyMxMEI5ODEnLCAnIzEwQjk4MScsICcjMTBCOTgxJywgJyMxMEI5ODEnLCAnIzEwQjk4MScsICcjOTkxQjFCJywgJyM5OTFCMUInLCAnIzk5MUIxQiddKV0pXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nRGlzdHJpYnVpw6fDo28gQmlub21pYWwgZSBSZWdpw6NvIENyw610aWNhICgkXFxhbHBoYSBcXGFwcHJveCAwLjExJCknLCB4YXhpc190aXRsZT0nTsO6bWVybyBkZSBDYXJhcycsIHlheGlzX3RpdGxlPSdQcm9iYWJpbGlkYWRlJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM0OCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMTA5Mzc1fSwgeyJlbnVuY2lhZG8iOiAiVW1hIG3DoXF1aW5hIGRlIGVudmFzZSBkZSBjYWbDqSDDqSByZWd1bGFkYSBwYXJhICRcXG11ID0gNTAwJCBnIGNvbSAkXFxzaWdtYV4yID0gNDAwJC4gQ29tICRuID0gMTYkIHBhY290ZXMsIGEgbcOpZGlhIGFtb3N0cmFsIG9ic2VydmFkYSBmb2kgJFxcYmFye1h9ID0gNDg1JCBnLiBTZSBvIHRlc3RlIMOpICRIXzA6IFxcbXUgPSA1MDAkIHZzICRIXzE6IFxcbXUgPCA1MDAkLCBjYWxjdWxlIGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlICRaX3tcXHRleHR7Y2FsY319JCBlIGRldGVybWluZSBzZSwgY29tICRcXGFscGhhID0gMCwwNSQgKCRaX3tcXHRleHR7Y3JpdH19ID0gLTEsNjQ1JCksIHJlamVpdGFtb3MgJEhfMCQuIiwgImRpY2EiOiAiVXNlIGEgZsOzcm11bGEgZGEgZXN0YXTDrXN0aWNhIFogcGFyYSBhIG3DqWRpYTogJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11XzB9e1xcc2lnbWEgLyBcXHNxcnR7bn19JC4gTyBlcnJvIHBhZHLDo28gw6kgJEVQKFxcYmFye1h9KSA9IFxcc2lnbWEgLyBcXHNxcnR7bn0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAxOiBJZGVudGlmaWNhciBwYXLDom1ldHJvcy4gJFxcYmFye1h9ID0gNDg1JCwgJFxcbXVfMCA9IDUwMCQsICRcXHNpZ21hID0gXFxzcXJ0ezQwMH0gPSAyMCQsICRuID0gMTYkLiIsICJQYXNzbyAyOiBDYWxjdWxhciBvIGVycm8gcGFkcsOjbyAkRVAoXFxiYXJ7WH0pID0gMjAgLyBcXHNxcnR7MTZ9ID0gMjAgLyA0ID0gNSQuIiwgIlBhc3NvIDM6IENhbGN1bGFyICRaX3tcXHRleHR7Y2FsY319ID0gKDQ4NSAtIDUwMCkgLyA1ID0gLTE1IC8gNSA9IC0zJC4iLCAiUGFzc28gNDogQ29tcGFyYXIgY29tIG8gdmFsb3IgY3LDrXRpY28gJFpfe1xcdGV4dHtjcml0fX0gPSAtMSw2NDUkLiIsICJQYXNzbyA1OiBDb21vICQtMyA8IC0xLDY0NSQsIGEgZXN0YXTDrXN0aWNhIGNhaSBuYSByZWdpw6NvIGRlIHJlamVpw6fDo28gKFJDID0gJFogPCAtMSw2NDUkKSwgbG9nbyByZWplaXRhbW9zICRIXzAkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNDAiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAtMy4wfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXhwZXJpbWVudG8gc29icmUgbyB0ZW1wbyBkZSB2aWRhIGRlIGNvbXBvbmVudGVzIGRlIElvVCwgYXNzdW1lLXNlIHF1ZSBvIHRlbXBvIGF0w6kgYSBmYWxoYSBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gY29tIG3DqWRpYSAkXFxtdSA9IDEwMDAkIGhvcmFzIGUgJFxcc2lnbWEgPSAyMDAkIGhvcmFzLiBPIGZhYnJpY2FudGUgYWZpcm1hIHF1ZSB1bWEgbm92YSBhdHVhbGl6YcOnw6NvIGRlIGZpcm13YXJlIHByb2xvbmdhIGVzc2EgdmlkYSBtw6lkaWEuIENvbSB1bWEgYW1vc3RyYSBkZSAkbiA9IDY0JCBjb21wb25lbnRlcywgb2J0ZXZlLXNlIHVtYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9ID0gMTA1MCQgaG9yYXMuIERlZmluYSBhcyBoaXDDs3Rlc2VzICRIXzAkIGUgJEhfMSQsIGUgY2FsY3VsZSBhIHJlZ2nDo28gY3LDrXRpY2EgcGFyYSB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLjA1JCAodGVzdGUgdW5pbGF0ZXJhbCkuIiwgImRpY2EiOiAiVXNlIG8gVGVvcmVtYSBkbyBMaW1pdGUgQ2VudHJhbCBwYXJhIGp1c3RpZmljYXIgYSBub3JtYWxpZGFkZSBkYSBtw6lkaWEgYW1vc3RyYWwgZSBjYWxjdWxlIG8gdmFsb3IgY3LDrXRpY28gJFpfe1xcdGV4dHtjcml0fX0kIHBhcmEgJFxcYWxwaGEgPSAwLjA1JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gRGVmaW5pciBhcyBoaXDDs3Rlc2VzOiAkSF8wOiBcXG11ID0gMTAwMCQgZSAkSF8xOiBcXG11ID4gMTAwMCQuIiwgIjIuIENhbGN1bGFyIG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYTogJEVQKFxcYmFye1h9KSA9IFxcZnJhY3tcXHNpZ21hfXtcXHNxcnR7bn19ID0gXFxmcmFjezIwMH17XFxzcXJ0ezY0fX0gPSBcXGZyYWN7MjAwfXs4fSA9IDI1JC4iLCAiMy4gRGV0ZXJtaW5hciBvIHZhbG9yIGNyw610aWNvICRaX3tcXHRleHR7Y3JpdH19JCBwYXJhICRcXGFscGhhID0gMC4wNSQ6IG5hIHRhYmVsYSBkYSBub3JtYWwgcGFkcsOjbywgJFAoWiA+IDEuNjQ1KSA9IDAuMDUkLiIsICI0LiBFbmNvbnRyYXIgYSBtw6lkaWEgY3LDrXRpY2EgJFxcYmFye1h9X2MkOiAkXFxiYXJ7WH1fYyA9IFxcbXVfMCArIFpfe1xcdGV4dHtjcml0fX0gXFx0aW1lcyBFUChcXGJhcntYfSkgPSAxMDAwICsgMS42NDUgXFx0aW1lcyAyNSQuIiwgIjUuIFJlc3VsdGFkbzogJFxcYmFye1h9X2MgPSAxMDAwICsgNDEuMTI1ID0gMTA0MS4xMjUkLiBBIHJlZ2nDo28gY3LDrXRpY2Egw6kgJFJDID0gXFx7IFxcYmFye1h9IDogXFxiYXJ7WH0gPiAxMDQxLjEyNSBcXH0kLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMTA0MS4xMjV9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgw7N0aWNhIGRhIHRheG9ub21pYSBkYSBkZWNpc8OjbywgcG9yIHF1ZSBhIGVzY29saGEgZW50cmUgdW0gdGVzdGUgYmlsYXRlcmFsIGUgdW0gdW5pbGF0ZXJhbCBpbXBhY3RhIGRpcmV0YW1lbnRlIGEgY2FwYWNpZGFkZSBkZSB1bSBwZXNxdWlzYWRvciBlbSByZWplaXRhciBhIGhpcMOzdGVzZSBudWxhLiBVc2UgYSBnZW9tZXRyaWEgZGEgUmVnacOjbyBDcsOtdGljYSAoJFJDJCkgZW0gc2V1cyBhcmd1bWVudG9zLiIsICJkaWNhIjogIkNvbnNpZGVyZSBjb21vIG8gbWVzbW8gdmFsb3IgZGUgJFxcYWxwaGEkIMOpIGRpc3RyaWJ1w61kbyBlbSB0ZXJtb3MgZGUgY2F1ZGFzICgxIG91IDIpIGUgY29tbyBpc3NvIGFsdGVyYSBvIHZhbG9yIGNyw610aWNvIHRhYmVsYWRvICgkWl97XFx0ZXh0e2NyaXR9fSQgb3UgJHRfe1xcdGV4dHtjcml0fX0kKS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gTm8gdGVzdGUgdW5pbGF0ZXJhbCwgdG9kbyBvIHZhbG9yIGRlICRcXGFscGhhJCDDqSBjb25jZW50cmFkbyBlbSBhcGVuYXMgdW1hIGNhdWRhIGRhIGRpc3RyaWJ1acOnw6NvLiBJc3NvIHJlc3VsdGEgZW0gdW0gdmFsb3IgY3LDrXRpY28gKGVtIHZhbG9yIGFic29sdXRvKSBtZW5vciAoZXg6ICRaX3tcXHRleHR7Y3JpdH19ID0gMS42NDUkIHBhcmEgJFxcYWxwaGE9MC4wNSQpLiIsICIyLiBObyB0ZXN0ZSBiaWxhdGVyYWwsIG8gbsOtdmVsICRcXGFscGhhJCDDqSBkaXZpZGlkbyBpZ3VhbG1lbnRlIGVudHJlIGFzIGR1YXMgY2F1ZGFzICgkXFxhbHBoYS8yJCksIGV4aWdpbmRvIHVtIHZhbG9yIGNyw610aWNvIG1haW9yIChleDogJFpfe1xcdGV4dHtjcml0fX0gPSAxLjk2JCBwYXJhICRcXGFscGhhPTAuMDUkKS4iLCAiMy4gQ29uY2x1c8OjbzogUGFyYSB1bWEgbWVzbWEgZXN0YXTDrXN0aWNhIGNhbGN1bGFkYSwgdW0gdGVzdGUgdW5pbGF0ZXJhbCDDqSBtYWlzICdmw6FjaWwnIGRlIHJlamVpdGFyICRIXzAkIHNlIGEgZGlyZcOnw6NvIGRvIGVmZWl0byBmb3IgYSBlc3BlcmFkYSwgcG9pcyBvIHZhbG9yIGNyw610aWNvIGVzdMOhIG1haXMgcHLDs3hpbW8gZGEgbcOpZGlhIHBvcHVsYWNpb25hbCBzb2IgJEhfMCQuIiwgIjQuIFBvciBvdXRybyBsYWRvLCBvIHRlc3RlIGJpbGF0ZXJhbCBwcm90ZWdlIGNvbnRyYSBlcnJvcyBlbSBhbWJhcyBhcyBkaXJlw6fDtWVzLCBzZW5kbyBtYWlzIGNvbnNlcnZhZG9yIGVtIHJlbGHDp8OjbyBhIGRlc3Zpb3MgZGlyZWNpb25haXMuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIENhcCAxMiIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbWEgZW1wcmVzYSBlbnZhc2Fkb3JhIGRlIHN1Y29zIGRldmUgZ2FyYW50aXIgcXVlIGFzIGdhcnJhZmFzIHRlbmhhbSwgZW0gbcOpZGlhLCA1MDAgbWwuIFNlIG8gdm9sdW1lIGZvciBtZW5vciwgaMOhIHByZWp1w616byBhbyBjb25zdW1pZG9yOyBzZSBmb3IgbWFpb3IsIGjDoSBwcmVqdcOtem8gw6AgZW1wcmVzYS4gVW0gaW5zcGV0b3IgY29sZXRhIDI1IGdhcnJhZmFzIGUgZW5jb250cmEgJFxcYmFye1h9ID0gNDk1JCBtbCwgY29tIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCBjb25oZWNpZG8gJFxcc2lnbWEgPSAxMCQgbWwuIENvbSAkXFxhbHBoYSA9IDAuMDUkLCB0ZXN0ZSAkSF8wOiBcXG11ID0gNTAwJCBjb250cmEgJEhfMTogXFxtdSBcXG5lcSA1MDAkIGUgZGV0ZXJtaW5lIHNlIGEgZW1wcmVzYSBkZXZlIHJlYWp1c3RhciBhIG3DoXF1aW5hLiIsICJkaWNhIjogIkNvbW8gbyB0ZXN0ZSDDqSBiaWxhdGVyYWwsIGEgZXN0YXTDrXN0aWNhICRaX3tcXHRleHR7Y2FsY319JCBkZXZlIHNlciBjb21wYXJhZGEgY29tICRcXHBtIFpfe1xcdGV4dHtjcml0fX0kIGNvcnJlc3BvbmRlbnRlIGEgJFxcYWxwaGEvMiA9IDAuMDI1JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSGlww7N0ZXNlczogJEhfMDogXFxtdSA9IDUwMCQsICRIXzE6IFxcbXUgXFxuZXEgNTAwJC4iLCAiMi4gQ8OhbGN1bG8gZGEgZXN0YXTDrXN0aWNhICRaX3tcXHRleHR7Y2FsY319JDogJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11XzB9e1xcc2lnbWEgLyBcXHNxcnR7bn19ID0gXFxmcmFjezQ5NSAtIDUwMH17MTAgLyBcXHNxcnR7MjV9fSA9IFxcZnJhY3stNX17Mn0gPSAtMi41JC4iLCAiMy4gVmFsb3JlcyBjcsOtdGljb3MgcGFyYSAkXFxhbHBoYSA9IDAuMDUkIChiaWxhdGVyYWwpOiAkXFxwbSAxLjk2JC4iLCAiNC4gQ29tcGFyYcOnw6NvOiAkfFpfe1xcdGV4dHtjYWxjfX18ID0gMi41ID4gMS45NiQuIENvbW8gYSBlc3RhdMOtc3RpY2EgY2FpIG5hIHpvbmEgZGUgcmVqZWnDp8OjbywgcmVqZWl0YW1vcyAkSF8wJC4iLCAiNS4gQ29uY2x1c8OjbzogSMOhIGV2aWTDqm5jaWFzIGVzdGF0w61zdGljYXMgc2lnbmlmaWNhdGl2YXMgZGUgcXVlIGEgbcOhcXVpbmEgZXN0w6EgZGVzY2FsaWJyYWRhLCBkZXZlbmRvIHNlciByZWFqdXN0YWRhLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogLTIuNX0sIHsiZW51bmNpYWRvIjogIlVtYSBtw6FxdWluYSBpbmR1c3RyaWFsIGRlIGNvcnRlIHByb2R1eiBwZcOnYXMgY29tIGNvbXByaW1lbnRvICRYIFxcc2ltIE4oXFxtdSwgNCkkLiBPIHN1cGVydmlzb3IgZGUgcXVhbGlkYWRlIGRlc2VqYSB0ZXN0YXIgc2UgYSBtw6FxdWluYSBlc3TDoSBkZXNyZWd1bGFkYSAoJEhfMDogXFxtdSA9IDEwJCB2cyAkSF8xOiBcXG11ID4gMTAkKS4gVW1hIGFtb3N0cmEgZGUgJG4gPSAxNiQgcGXDp2FzIMOpIGNvbGV0YWRhIGUgYSByZWdyYSBkZSBkZWNpc8OjbyBlc3RhYmVsZWNpZGEgw6kgcmVqZWl0YXIgJEhfMCQgc2UgJFxcYmFye1h9ID4gMTEkLiBDYWxjdWxlIGEgcHJvYmFiaWxpZGFkZSBkbyBFcnJvIFRpcG8gSSAoJFxcYWxwaGEkKS4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIHNvYiAkSF8wJCwgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBzZWd1ZSAkTihcXG11LCBcXHNpZ21hXjIvbikkLiBDYWxjdWxlIG8gZXJybyBwYWRyw6NvICRFUChcXGJhcntYfSkgPSBcXHNpZ21hL1xcc3FydHtufSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIklkZW50aWZpY2Ftb3MgYSBkaXN0cmlidWnDp8OjbyBkYSBtw6lkaWEgYW1vc3RyYWwgc29iICRIXzAkOiAkXFxiYXJ7WH0gXFxzaW0gTihcXG11LCBcXHNpZ21hXjIvbikgPSBOKDEwLCA0LzE2KSA9IE4oMTAsIDAuMjUpJC4iLCAiTyBkZXN2aW8gcGFkcsOjbyBkYSBtw6lkaWEgKGVycm8gcGFkcsOjbykgw6kgJEVQKFxcYmFye1h9KSA9IFxcc3FydHswLjI1fSA9IDAuNSQuIiwgIkEgcHJvYmFiaWxpZGFkZSBkbyBFcnJvIFRpcG8gSSDDqSAkXFxhbHBoYSA9IFAoXFxiYXJ7WH0gPiAxMSB8IFxcbXUgPSAxMCkkLiIsICJOb3JtYWxpemFtb3MgbyB2YWxvciBjcsOtdGljbzogJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7MTEgLSAxMH17MC41fSA9IDIuMCQuIiwgIlVzYW5kbyBhIHRhYmVsYSBub3JtYWwgcGFkcsOjbywgJFAoWiA+IDIuMCkgPSAxIC0gMC45NzcyID0gMC4wMjI4JC4iLCAiUG9ydGFudG8sIGEgcHJvYmFiaWxpZGFkZSBkbyBFcnJvIFRpcG8gSSDDqSAkMC4wMjI4JCBvdSAkMi4yOFxcJSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDMzMyIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMDIyOH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyYW5kbyBvIG1lc21vIGNlbsOhcmlvIGRhIHF1ZXN0w6NvIGFudGVyaW9yICgkSF8wOiBcXG11ID0gMTAsIFxcc2lnbWFeMiA9IDQsIG4gPSAxNiwgXFx0ZXh0e1JDfSA9IFxceyBcXGJhcntYfSA+IDExIFxcfSQpLCBjYWxjdWxlIGEgcHJvYmFiaWxpZGFkZSBkbyBFcnJvIFRpcG8gSUkgKCRcXGJldGEkKSBzZSBhIHZlcmRhZGVpcmEgbcOpZGlhIGRhIG3DoXF1aW5hIGZvciwgbmEgdmVyZGFkZSwgJFxcbXUgPSAxMS41JC4iLCAiZGljYSI6ICJPIEVycm8gVGlwbyBJSSBvY29ycmUgcXVhbmRvIG7Do28gcmVqZWl0YW1vcyAkSF8wJCAoYWNlaXRhbW9zIG8gcHJvY2Vzc28gY29tbyBib20pIHF1YW5kbyBuYSB2ZXJkYWRlIGEgbcOpZGlhIMOpIDExLjUuIENhbGN1bGUgJFAoXFxiYXJ7WH0gXFxsZSAxMSB8IFxcbXUgPSAxMS41KSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlNvYiBhIGhpcMOzdGVzZSBhbHRlcm5hdGl2YSAkXFxtdSA9IDExLjUkLCBhIG3DqWRpYSBhbW9zdHJhbCBzZWd1ZSAkXFxiYXJ7WH0gXFxzaW0gTigxMS41LCAwLjI1KSQuIiwgIk8gRXJybyBUaXBvIElJIMOpICRcXGJldGEgPSBQKFxcYmFye1h9IFxcbGUgMTEgfCBcXG11ID0gMTEuNSkkLiIsICJOb3JtYWxpemFtb3MgbyB2YWxvciBwYXJhIFo6ICRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFjezExIC0gMTEuNX17MC41fSA9IC0xLjAkLiIsICJDb25zdWx0YW5kbyBhIHRhYmVsYSBub3JtYWw6ICRQKFogXFxsZSAtMS4wKSA9IDAuMTU4NyQuIiwgIkEgcHJvYmFiaWxpZGFkZSBkZSBjb21ldGVyIHVtIEVycm8gVGlwbyBJSSDDqSAkMC4xNTg3JCBvdSAkMTUuODdcXCUkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzMzIiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjE1ODd9LCB7ImVudW5jaWFkbyI6ICJEaXNjdXRhIHF1YWxpdGF0aXZhbWVudGUgbyBpbXBhY3RvIGRvIGF1bWVudG8gZG8gdGFtYW5obyBhbW9zdHJhbCAoJG4kKSBzb2JyZSBvcyBFcnJvcyBUaXBvIEkgKCRcXGFscGhhJCkgZSBUaXBvIElJICgkXFxiZXRhJCkuIFNlIG8gcGVzcXVpc2Fkb3IgZml4YXIgJFxcYWxwaGEkIGVtIHVtIG7DrXZlbCBtdWl0byBiYWl4byAoZXg6IDAuMDEpIHBhcmEgZXZpdGFyIGZhbHNvcyBwb3NpdGl2b3MsIG8gcXVlIHRlbmRlIGEgYWNvbnRlY2VyIGNvbSBvIHBvZGVyIGRvIHRlc3RlICgkMS1cXGJldGEkKT8iLCAiZGljYSI6ICJSZWZsaXRhIHNvYnJlIGNvbW8gbyBhdW1lbnRvIGRlICRuJCBlc3RyZWl0YSBhIGRpc3RyaWJ1acOnw6NvIGFtb3N0cmFsIChkaW1pbnVpIG8gZXJybyBwYWRyw6NvKSBlIGEgcmVsYcOnw6NvIGRlIGVxdWlsw61icmlvIGVudHJlICRcXGFscGhhJCBlICRcXGJldGEkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBdW1lbnRhciBvIHRhbWFuaG8gYW1vc3RyYWwgJG4kIHJlZHV6IG8gZXJybyBwYWRyw6NvICRFUChcXGJhcntYfSkgPSBcXHNpZ21hL1xcc3FydHtufSQsIHRvcm5hbmRvIGEgZGlzdHJpYnVpw6fDo28gZGUgJFxcYmFye1h9JCBtYWlzIGNvbmNlbnRyYWRhIGFvIHJlZG9yIGRhIG3DqWRpYSByZWFsLiIsICJTZSBtYW50aXZlcm1vcyBhIG1lc21hIFJlZ2nDo28gQ3LDrXRpY2EsIHVtIGF1bWVudG8gZW0gJG4kIGRpbWludWkgJFxcYmV0YSQgZSwgY29uc2VxdWVudGVtZW50ZSwgYXVtZW50YSBvIHBvZGVyIGRvIHRlc3RlICgkMS1cXGJldGEkKS4iLCAiQW8gZml4YXIgJFxcYWxwaGEkIGVtIHVtIG7DrXZlbCBtdWl0byBiYWl4byAoZXg6IDAuMDEpLCBhIFJlZ2nDo28gQ3LDrXRpY2EgdG9ybmEtc2UgbWFpcyByZXN0cml0YSAobWFpcyBkaXN0YW50ZSBkYSBtw6lkaWEgZGUgJEhfMCQpLCBvIHF1ZSByZWR1eiBhIGNhcGFjaWRhZGUgZGUgZGV0ZWN0YXIgZGVzdmlvcyBlbSAkSF8xJC4iLCAiSXNzbyByZXN1bHRhIGVtIHVtIGF1bWVudG8gaW5ldml0w6F2ZWwgZG8gRXJybyBUaXBvIElJICgkXFxiZXRhJCksIGRpbWludWluZG8gbyBwb2RlciBlc3RhdMOtc3RpY28gZG8gdGVzdGUsIGEgbWVub3MgcXVlIG8gdGFtYW5obyBkYSBhbW9zdHJhIHNlamEgYXVtZW50YWRvIHBhcmEgY29tcGVuc2FyIGVzc2EgcGVyZGEgZGUgc2Vuc2liaWxpZGFkZS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9XX0=').decode('utf-8'))


    # Inicialização da estrutura de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo do progresso total dinâmico
    total_mcq = len(dados_exercicios.get("questoes_multipla_escolha", []))
    total_disc = len(dados_exercicios.get("questoes_discursivas", []))
    total_exercicios = total_mcq + total_disc
    
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    # Barra de progresso e status
    st.markdown("---")
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    st.markdown("---")
    
    # Seção de Questões de Múltipla Escolha
    st.subheader("📝 Questões de Múltipla Escolha")
    for i, questao in enumerate(dados_exercicios.get("questoes_multipla_escolha", [])):
        st.markdown(f"**Questão {i + 1}:** {questao.get('enunciado', '')}")
        
        # Referência Bibliográfica
        ref = questao.get("referencia_livro")
        if ref:
            st.markdown(f"📖 *Referência: {ref}*")
    
        # Renderização do gráfico Plotly
        plotly_code = questao.get("codigo_plotly")
        if plotly_code:
            try:
                local_vars = {"go": go, "stats": stats, "np": np}
                exec(plotly_code, globals(), local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
            except Exception as e:
                st.error(f"Erro ao carregar gráfico: {e}")
    
        # Alternativas
        alternativas = questao.get("alternativas", {})
        opcao_selecionada = st.radio(
            "Escolha uma alternativa:",
            options=list(alternativas.keys()),
            format_func=lambda x: f"{x}: {alternativas[x]}",
            key=f"radio_mcq_{i}"
        )
    
        # Botão de Dica
        if st.button("💡 Dica", key=f"dica_mcq_{i}"):
            st.info(questao.get("dica", "Dica indisponível"))
    
        # Verificação
        if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
            if opcao_selecionada == questao.get("alternativa_correta"):
                st.success("Correto! Muito bem.")
                st.session_state.respostas_certas[f"mcq_{i}"] = True
                st.rerun()
            else:
                st.error("Resposta incorreta. Tente novamente!")
                st.session_state.respostas_certas[f"mcq_{i}"] = False
                st.rerun()
    
        # Gabarito
        with st.expander("✅ Ver Gabarito Comentado"):
            st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
        st.markdown("---")
    
    # Seção de Questões Discursivas
    st.subheader("✍️ Questões Discursivas e Práticas")
    for i, questao in enumerate(dados_exercicios.get("questoes_discursivas", [])):
        st.markdown(f"**Questão {i + 1}:** {questao.get('enunciado', '')}")
        
        # Referência
        ref = questao.get("referencia_livro")
        if ref:
            st.markdown(f"📖 *Referência: {ref}*")
        
        # Gráfico Discursiva
        plotly_code = questao.get("codigo_plotly")
        if plotly_code:
            try:
                local_vars = {"go": go, "stats": stats, "np": np}
                exec(plotly_code, globals(), local_vars)
                if "fig" in local_vars:
                    st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
            except Exception as e:
                st.error(f"Erro ao carregar gráfico: {e}")
    
        # Entrada de resposta
        st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
        
        # Lógica para cálculo numérico ou checkbox qualitativo
        esperada = questao.get("resposta_numerica_esperada")
        if esperada is not None:
            user_val = st.number_input("Digite o resultado numérico calculado:", format="%.4f", key=f"num_disc_{i}")
            if st.button("Validar Cálculo", key=f"val_disc_{i}"):
                if abs(user_val - esperada) <= max(0.01, 0.01 * abs(esperada)):
                    st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                    st.rerun()
                else:
                    st.error("O valor calculado difere do gabarito. Verifique arredondamentos e fórmulas.")
                    st.session_state.respostas_certas[f"disc_{i}"] = False
                    st.rerun()
        else:
            concluido = st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}")
            if concluido:
                st.session_state.respostas_certas[f"disc_{i}"] = True
            else:
                st.session_state.respostas_certas[f"disc_{i}"] = False
    
        # Dica e Resolução
        if st.button("💡 Dica", key=f"dica_disc_{i}"):
            st.info(questao.get("dica", "Dica indisponível"))
            
        with st.expander("✅ Ver Resolução Detalhada"):
            for passo in questao.get("gabarito_passo_a_passo", []):
                st.write(f"- {passo}")
        st.markdown("---")
