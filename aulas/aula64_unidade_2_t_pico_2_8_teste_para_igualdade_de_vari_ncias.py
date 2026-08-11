import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuODogVGVzdGUgcGFyYSBpZ3VhbGRhZGUgZGUgdmFyacOibmNpYXMiLCAicmVmZXJlbmNpYXNfYmlibGlvZ3JhZmljYXNfZmluYWlzIjogWyJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EgLSBDYXAuIDEzLCBwcC4gMzY1LTM2OCJdfQ==').decode('utf-8'))

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
    
    # Título do Subtópico
    st.header(r"Fundamentação Teórica: Homocedasticidade e a Necessidade de Comparação de Variâncias")
    
    # Introdução e Contextualização
    st.markdown(r"""
    A comparação de populações é um dos pilares da inferência estatística, sendo o ponto de partida para conclusões rigorosas sobre fenômenos empíricos. Antes de comparar médias, é imperativo avaliar as propriedades de dispersão.
    """)
    
    st.markdown(r"""
    - **Homocedasticidade:** Define o estado de estabilidade onde a variabilidade dos dados é constante, independentemente das subpopulações ou níveis experimentais.
    - **Heterocedasticidade:** Representa uma variação inconsistente, introduzindo disparidades estruturais que podem comprometer a validade da inferência.
    """)
    
    st.info(r"A homocedasticidade assegura que a margem de erro, a precisão das medidas e o ruído intrínseco aos processos sejam uniformes. Sem essa premissa, testes clássicos como o teste t de Student podem gerar conclusões enviesadas e inflar o erro tipo I.")
    
    # Formalismo Matemático
    st.subheader(r"📐 Estrutura Matemática: O Teste de Igualdade de Variâncias")
    
    st.markdown(r"Para diagnosticar a homocedasticidade, utilizamos a distribuição F de Snedecor, testando a razão entre as variâncias populacionais sob as seguintes hipóteses:")
    
    st.latex(r"H_{0}: \sigma_{1}^{2} = \sigma_{2}^{2} = \sigma^{2}")
    st.latex(r"H_{1}: \sigma_{1}^{2} \neq \sigma_{2}^{2}")
    
    st.markdown(r"A estatística de teste é definida pela razão das variâncias amostrais:")
    
    st.latex(r"W = \frac{S_{1}^{2}}{S_{2}^{2}} \sim F(n_{1}-1, n_{2}-1)")
    
    # Dedução Analítica
    st.subheader(r"🧮 Detalhamento Analítico: Distribuição da Razão")
    
    st.markdown(r"Abaixo, demonstramos a construção da estatística W baseada na relação entre distribuições qui-quadrado:")
    
    st.latex(r"U = \frac{(n_{1}-1)S_{1}^{2}}{\sigma_{1}^{2}} \sim \chi^{2}(n_{1}-1)")
    st.latex(r"V = \frac{(n_{2}-1)S_{2}^{2}}{\sigma_{2}^{2}} \sim \chi^{2}(n_{2}-1)")
    
    st.markdown(r"Ao realizar o quociente destas variáveis normalizadas por seus graus de liberdade, obtemos a estatística F:")
    
    st.latex(r"W = \frac{U/(n_{1}-1)}{V/(n_{2}-1)} = \frac{S_{1}^{2}/\sigma_{1}^{2}}{S_{2}^{2}/\sigma_{2}^{2}} \sim F(n_{1}-1, n_{2}-1)")
    
    st.markdown(r"Sob a hipótese nula, simplificamos a expressão para o diagnóstico final:")
    
    st.latex(r"W = \frac{S_{1}^{2}}{S_{2}^{2}} \sim F(n_{1}-1, n_{2}-1) \quad \text{sob} \quad H_{0}: \sigma_{1}^{2} = \sigma_{2}^{2}")
    
    # Casos de Aplicação Prática
    st.subheader(r"📈 Casos de Aplicação Prática: Controle de Processos")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Comparação de Máquinas de Precisão")
        st.markdown(r"Duas máquinas de precisão (A e B) fabricam componentes. Para verificar se operam com o mesmo nível de controle, coletamos amostras de 6 componentes de cada linha de produção.")
        
        st.latex(r"n_{A} = 6, n_{B} = 6, S_{A}^{2} = 40, S_{B}^{2} = 37, \alpha = 0,10")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo da estatística: $F_{calc} = \frac{S_{A}^{2}}{S_{B}^{2}} = \frac{40}{37} = 1,081$")
        st.markdown(r"- Graus de liberdade: $gl_{num} = 5, gl_{den} = 5$")
        st.markdown(r"- Valor crítico: $F_{crit} (\alpha=0,10) = 5,05$")
        st.markdown(r"- Comparação: $1,081 < 5,05$")
        
        st.success(r"Conclusão: Como a estatística calculada não excede o limiar crítico, não rejeitamos a hipótese nula. Não há evidência estatística, ao nível de 10%, de que as máquinas apresentem variabilidades distintas, validando o uso de testes de médias combinadas.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do subtópico
    st.header(r"A Engenharia da Distribuição F de Snedecor")
    
    # Introdução e Contexto Teórico
    st.markdown(r"""
    A distribuição F de Snedecor constitui o motor matemático da comparação de variabilidades. Ao investigar se a diferença entre duas variâncias amostrais é meramente acidental ou estrutural, utilizamos a razão das somas de quadrados normalizadas por seus respectivos graus de liberdade.
    """)
    
    st.info(r"A distribuição F de Snedecor atua como uma balança que quantifica quão extremo é um quociente observado em relação ao que seria esperado sob a premissa de variâncias populacionais iguais.")
    
    st.markdown(r"""
    Historicamente, a gênese deste conceito está profundamente entrelaçada com o desenvolvimento do design de experimentos. George W. Snedecor, ao formalizar esta distribuição, prestou uma homenagem fundamental ao trabalho pioneiro de Sir Ronald A. Fisher.
    """)
    
    st.subheader(r"📐 O Coração Matemático: Distribuição F")
    
    st.markdown(r"A construção da distribuição F fundamenta-se na razão de duas variáveis aleatórias independentes que seguem distribuições qui-quadrado ($\chi^2$), cada uma dividida pelos seus respectivos graus de liberdade:")
    
    st.latex(r"F(gl_{\text{num}}, gl_{\text{den}}) = \frac{U / gl_{\text{num}}}{V / gl_{\text{den}}}")
    
    st.markdown(r"O valor esperado da distribuição é sensível à estabilidade do denominador, sendo definido pela relação:")
    
    st.latex(r"E[F] = \frac{gl_{\text{den}}}{gl_{\text{den}} - 2}")
    
    st.markdown(r"Nota-se que, para $gl_{\text{den}} \leq 2$, a cauda da distribuição torna-se excessivamente pesada, impedindo a convergência do primeiro momento estatístico.")
    
    # Demonstração Analítica
    st.subheader(r"📊 Dedução Analítica do Quociente")
    
    st.latex(r"F = \frac{U/gl_{\text{num}}}{V/gl_{\text{den}}}")
    st.markdown(r"Substituindo pelas estimativas amostrais normalizadas pelas variâncias populacionais:")
    st.latex(r"F = \frac{[(n_1-1)S_1^2 / \sigma_1^2] / (n_1-1)}{[(n_2-1)S_2^2 / \sigma_2^2] / (n_2-1)}")
    st.markdown(r"Simplificando os termos de graus de liberdade:")
    st.latex(r"F = \frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2}")
    st.markdown(r"Sob a hipótese nula de igualdade de variâncias ($\sigma_1^2 = \sigma_2^2$), a estatística reduz-se a:")
    st.latex(r"F = \frac{S_1^2}{S_2^2}")
    
    # Simulador
    st.subheader(r"⚙️ Visualizador de Densidade F")
    
    col1, col2 = st.columns(2)
    with col1:
        gl_num = st.slider(r"Graus de Liberdade Numerador ($gl_{\text{num}}$)", 1, 50, 10, key=r"gl_num_subtopico_2")
    with col2:
        gl_den = st.slider(r"Graus de Liberdade Denominador ($gl_{\text{den}}$)", 3, 50, 10, key=r"gl_den_subtopico_2")
    
    f_calc = st.slider(r"Estatística $F_{\text{calc}}$ observada", 0.0, 5.0, 1.5, step=0.1, key=r"f_calc_subtopico_2")
    show_critical = st.toggle(r"Sombrear Região Crítica ($\alpha=0.05$)", key=r"toggle_crit_subtopico_2")
    
    x = np.linspace(0.01, 5, 500)
    y = stats.f.pdf(x, gl_num, gl_den)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Densidade F', line=dict(color='#1E3A8A', width=2)))
    
    if show_critical:
        f_crit = stats.f.ppf(0.95, gl_num, gl_den)
        x_fill = np.linspace(f_crit, 5, 100)
        fig.add_trace(go.Scatter(x=x_fill, y=stats.f.pdf(x_fill, gl_num, gl_den), fill='tozeroy', fillcolor='rgba(153, 27, 27, 0.3)', line=dict(color='rgba(0,0,0,0)'), name='Região Crítica'))
    
    fig.add_vline(x=f_calc, line_dash="dash", line_color="#991B1B", annotation_text="F_calc")
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Densidade F e Estatística Observada</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valor de F", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    p_valor = 1 - stats.f.cdf(f_calc, gl_num, gl_den)
    st.info(f"Para $gl_{{num}}={gl_num}$ e $gl_{{den}}={gl_den}$, uma estatística $F_{{calc}}={f_calc}$ resulta em um p-valor de {p_valor:.4f}. Isso indica a probabilidade de observar tal variabilidade sob a hipótese de igualdade.")
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática: Análise de Volatilidade")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Comparação de Ativos Financeiros")
        st.markdown(r"Para modelar a volatilidade de dois ativos financeiros, um analista observa a dispersão dos retornos diários ao longo de 21 dias úteis. A amostra do Ativo 1 apresentou uma variância de 0,025, enquanto o Ativo 2 apresentou 0,015.")
        st.latex(r"S_1^2 = 0,025, S_2^2 = 0,015, n_1=21, n_2=21, gl=20")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo da estatística: $F_{\text{calc}} = 0,025 / 0,015 = 1,667$")
        st.markdown(r"- Identificação dos graus de liberdade: $gl_{num}=20, gl_{den}=20$")
        st.markdown(r"- Valor crítico para $\alpha=0,05$: $F_{\text{crit}}(0,975, 20, 20) = 2,46$")
        st.success(r"Com uma estatística $F_{\text{calc}}$ de 1,667, verificamos que o valor está abaixo do limite crítico. Não há evidência robusta para afirmar que a volatilidade do Ativo 1 é superior à do Ativo 2.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título Principal
    st.header(r"Protocolo do Teste de Hipóteses para Igualdade de Variâncias")
    
    # Prosa Teórica - Parte 1
    st.markdown(r"""
    O protocolo para testar a igualdade de variâncias é um procedimento metódico essencial para a engenharia estatística. Ao estabelecer as hipóteses nula e alternativa, define-se um cenário de referência que será comparado contra a razão empírica das variâncias amostrais. Este teste valida a homocedasticidade como pré-requisito para comparações de médias e atua como ferramenta diagnóstica autônoma para a precisão de processos.
    """)
    
    st.info(r"Ao assumir que duas populações compartilham a mesma dispersão, declaramos que a incerteza associada aos fenômenos é intrinsecamente equivalente. Submeter essa presunção ao crivo estatístico é uma salvaguarda obrigatória contra inferências espúrias.")
    
    # Prosa Teórica - Parte 2 (Organizada em tópicos)
    st.markdown(r"""
    **Fundamentos do Protocolo:**
    * **Definição de Hipóteses:** A hipótese nula $H_0$ postula $\sigma_1^2 = \sigma_2^2$, enquanto a hipótese alternativa $H_1$ assume a heterocedasticidade ($\sigma_1^2 \neq \sigma_2^2$).
    * **Estatística de Teste:** O quociente $F_{calc} = S_{1}^{2}/S_{2}^{2}$ traduz a volatilidade das amostras em uma métrica de probabilidade.
    * **Critério de Decisão:** Comparamos a estatística calculada contra a distribuição $F$ de Snedecor, utilizando os graus de liberdade $gl_1 = n_1 - 1$ e $gl_2 = n_2 - 1$.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Formalismo do Teste F")
    st.latex(r"RC = \{ F \in \mathbb{R} \mid F > F_{crit} \}")
    st.latex(r"F_{calc} = \frac{S_{1}^{2}}{S_{2}^{2}} \geq 1")
    
    # Dedução Analítica
    st.markdown(r"A dedução do procedimento segue os passos abaixo:")
    st.latex(r"P(F_{calc} > F_{crit}) = \alpha")
    st.latex(r"F_{crit} = F(1-\alpha, gl_1, gl_2)")
    st.latex(r"\text{Se } F_{calc} > F_{crit}, \text{rejeita-se } H_{0}")
    
    # Simulador de Hipóteses
    st.subheader(r"⚙️ Painel de Controle de Hipóteses")
    col1, col2 = st.columns(2)
    with col1:
        s1_sq = st.number_input(r"Variância Amostral 1 ($S_1^2$)", value=20.25, step=0.1, key=r"s1_subtopico_3")
        n1 = st.number_input(r"Tamanho Amostra 1 ($n_1$)", value=16, step=1, key=r"n1_subtopico_3")
    with col2:
        s2_sq = st.number_input(r"Variância Amostral 2 ($S_2^2$)", value=10.24, step=0.1, key=r"s2_subtopico_3")
        n2 = st.number_input(r"Tamanho Amostra 2 ($n_2$)", value=16, step=1, key=r"n2_subtopico_3")
    
    alfa = st.slider(r"Nível de Significância ($\alpha$)", 0.01, 0.10, 0.05, key=r"alfa_subtopico_3")
    
    # Cálculos do Simulador
    f_calc = s1_sq / s2_sq
    gl1 = n1 - 1
    gl2 = n2 - 1
    f_crit = stats.f.ppf(1 - alfa, gl1, gl2)
    
    # Gráfico Plotly
    x = np.linspace(0, 4, 200)
    y = stats.f.pdf(x, gl1, gl2)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=r"Distribuição F", line=dict(color="#1E3A8A")))
    fig.add_vline(x=f_calc, line_dash="dash", line_color="#991B1B", annotation_text=r"F_{calc}")
    fig.add_vline(x=f_crit, line_dash="solid", line_color="#F59E0B", annotation_text=r"F_{crit}")
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição da Razão de Variâncias e Região Crítica</b>", font=dict(size=14, color="#1E293B"), x=0.0),
        xaxis=dict(title=dict(text="Razão F", font=dict(size=11)), tickfont=dict(size=9), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11)), tickfont=dict(size=9), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9))
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    # Laudo Dinâmico
    decisao = "Rejeitar $H_0$" if f_calc > f_crit else "Manter $H_0$"
    cor_laudo = "error" if f_calc > f_crit else "success"
    if cor_laudo == "success":
        st.success(f"### Decisão: {decisao}\nCom um $F_{calc}$ de {f_calc:.3f} e $F_{crit}$ de {f_crit:.3f}, as dispersões são estatisticamente equivalentes.")
    else:
        st.error(f"### Decisão: {decisao}\nCom um $F_{calc}$ de {f_calc:.3f} acima do limiar {f_crit:.3f}, há evidências de heterocedasticidade.")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Comparação de Fornalhas")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Eficiência de Fornalhas")
        st.markdown(r"Em uma fábrica de engrenagens, duas fornalhas de tratamento térmico são comparadas. Após 16 medições em cada, $S_{1}=4,5$ e $S_{2}=3,2$. Teste a igualdade ao nível $\alpha = 0,05$.")
        st.latex(r"S_1^2 = 20,25, \quad S_2^2 = 10,24, \quad n_1=16, \quad n_2=16")
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- $F_{calc} = 20,25 / 10,24 = 1,977$")
        st.markdown(r"- $F_{crit}(0,95, 15, 15) = 2,40$")
        st.success(r"Como $1,977 < 2,40$, a hipótese de igualdade de variâncias é mantida. Ambas as fornalhas possuem o mesmo nível de consistência técnica.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Inferência Complementar: Intervalos de Confiança para a Razão de Variâncias")
    
    # Prosa Teórica e Contextualização
    st.markdown(r"""
    Para além do teste binário de hipóteses, a construção de intervalos de confiança para a razão de variâncias oferece uma perspectiva mais rica sobre a magnitude e a precisão da comparação entre dois processos. 
    
    Enquanto o teste fornece um veredito sobre a igualdade, o intervalo de confiança ($IC$) delimita o espectro onde a verdadeira razão das variâncias populacionais se encontra com $1-\alpha$ de probabilidade.
    """)
    
    st.info(r"A precisão de um intervalo reside na sua capacidade de quantificar a incerteza. Diferente de uma conclusão binária, o $IC$ nos permite visualizar a robustez da compatibilidade entre variabilidades.")
    
    st.markdown(r"""
    **Implicações Práticas do Intervalo:**
    - **Inclusão da Unidade:** Se o intervalo contiver o valor 1, reforça-se a tese de variabilidades compatíveis entre os processos.
    - **Deslocamento do Intervalo:** Intervalos inteiramente deslocados para além de 1 indicam disparidades substanciais na volatilidade ou precisão dos fenômenos analisados.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Formalismo Matemático: Razão de Variâncias")
    st.latex(r"IC = \left[ \frac{S_{1}^{2}}{S_{2}^{2}} \cdot \frac{1}{F_{1-\alpha/2}}, \frac{S_{1}^{2}}{S_{2}^{2}} \cdot \frac{1}{F_{\alpha/2}} \right]")
    
    # Dedução Analítica
    st.markdown(r"### 🔍 Demonstração Analítica e Propriedades")
    st.markdown(r"A derivação do intervalo fundamenta-se na distribuição F de Snedecor. Acompanhe a sequência lógica:")
    
    st.latex(r"P\left(F_{\alpha/2} \leq \frac{S_1^2}{S_2^2} \cdot \frac{\sigma_2^2}{\sigma_1^2} \leq F_{1-\alpha/2}\right) = 1-\alpha")
    
    st.markdown(r"Ao isolarmos a razão das variâncias populacionais, realizamos a inversão dos termos:")
    st.latex(r"\frac{1}{F_{1-\alpha/2}} \leq \frac{S_2^2}{S_1^2} \cdot \frac{\sigma_1^2}{\sigma_2^2} \leq \frac{1}{F_{\alpha/2}}")
    
    st.markdown(r"Chegamos, finalmente, à expressão que delimita a incerteza da razão populacional:")
    st.latex(r"\frac{S_1^2}{S_2^2} \cdot \frac{1}{F_{1-\alpha/2}} \leq \frac{\sigma_1^2}{\sigma_2^2} \leq \frac{S_1^2}{S_2^2} \cdot \frac{1}{F_{\alpha/2}}")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Avaliação de Sensores")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Comparação de Sensores de Temperatura")
        st.markdown(r"Um engenheiro de controle avalia dois sensores de temperatura, X e Y, com 11 medições cada. As variâncias amostrais são $S_{X}^{2} = 15$ e $S_{Y}^{2} = 9$. Construa um intervalo de confiança de 90% para a razão entre as variâncias dos dois sensores.")
        
        st.latex(r"S_X^2=15, \quad S_Y^2=9, \quad gl_1=10, \quad gl_2=10, \quad 1-\alpha=0,90")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Determinação dos valores críticos: $F_{0,05} = 0,348$ e $F_{0,95} = 2,978$")
        st.markdown(r"- Cálculo da razão amostral: $Ratio = 15 / 9 = 1,667$")
        st.markdown(r"- Limite Inferior: $Inf = 1,667 \cdot (1 / 2,978) = 0,560$")
        st.markdown(r"- Limite Superior: $Sup = 1,667 \cdot (1 / 0,348) = 4,790$")
        
        st.success(r"Com 90% de confiança, a razão entre as variâncias populacionais está contida no intervalo [0,560; 4,790]. A inclusão do valor 1 neste intervalo ratifica que, ao nível de 90%, não é possível discernir uma diferença significativa entre a precisão dos sensores, permitindo a substituição de um pelo outro sem perda de rigor.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuODogVGVzdGUgcGFyYSBpZ3VhbGRhZGUgZGUgdmFyacOibmNpYXMiLCAicXVlc3RvZXNfbXVsdGlwbGFfZXNjb2xoYSI6IFt7ImVudW5jaWFkbyI6ICJVbSBlbmdlbmhlaXJvIGRlIHF1YWxpZGFkZSBlbSB1bWEgcGxhbnRhIGRlIHNlbWljb25kdXRvcmVzIGRlc2VqYSBjb21wYXJhciBhIGVzdGFiaWxpZGFkZSBkZSBkdWFzIG3DoXF1aW5hcyBkZSBsaXRvZ3JhZmlhLCBBIGUgQiwgcXVlIG9wZXJhbSBzb2IgY29uZGnDp8O1ZXMgZGUgYWx0YSBwcmVjaXPDo28uIEEgaG9tb2NlZGFzdGljaWRhZGUgw6kgdW1hIHByZW1pc3NhIGZ1bmRhbWVudGFsIHBhcmEgYSB2YWxpZGFkZSBkb3MgdGVzdGVzIGRlIGNvbXBhcmHDp8OjbyBkZSBtw6lkaWFzIHF1ZSBzZXLDo28gcmVhbGl6YWRvcyBwb3N0ZXJpb3JtZW50ZS4gTyBlbmdlbmhlaXJvIGNvbGV0b3UgdW1hIGFtb3N0cmEgZGUgJG5fezF9ID0gMTYkIHVuaWRhZGVzIHByb2R1emlkYXMgcGVsYSBtw6FxdWluYSBBIGUgJG5fezJ9ID0gMTYkIHBlbGEgbcOhcXVpbmEgQiwgb2J0ZW5kbyB2YXJpw6JuY2lhcyBhbW9zdHJhaXMgJFNfezF9XnsyfSA9IDQ1LDAkIGUgJFNfezJ9XnsyfSA9IDI1LDAkLiBDb25zaWRlcmFuZG8gbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgZGUgJFxcYWxwaGEgPSAwLDEwJCwgcXVhbCBkYXMgYWx0ZXJuYXRpdmFzIGRlc2NyZXZlIGNvcnJldGFtZW50ZSBhIGzDs2dpY2EgZXN0YXTDrXN0aWNhIHBhcmEgdGVzdGFyICRIX3swfTogXFxzaWdtYV97MX1eezJ9ID0gXFxzaWdtYV97Mn1eezJ9JCBjb250cmEgJEhfezF9OiBcXHNpZ21hX3sxfV57Mn0gXFxuZXEgXFxzaWdtYV97Mn1eezJ9JD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIlV0aWxpemEtc2UgYSBlc3RhdMOtc3RpY2EgJFcgPSBTX3sxfV57Mn0gLyBTX3syfV57Mn0gPSAxLDgkLCBxdWUgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvICR0KG5fezF9K25fezJ9LTIpJCwgZSByZWplaXRhLXNlICRIX3swfSQgc2UgbyB2YWxvciBjcsOtdGljbyBmb3Igc3VwZXJhZG8uIiwgIkIiOiAiVXRpbGl6YS1zZSBhIGVzdGF0w61zdGljYSAkVyA9IFNfezF9XnsyfSAvIFNfezJ9XnsyfSA9IDEsOCQsIHF1ZSBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gJEYoMTUsIDE1KSQsIGUgbsOjbyBow6EgZXZpZMOqbmNpYXMgc3VmaWNpZW50ZXMgcGFyYSByZWplaXRhciAkSF97MH0kIHNlIG8gdmFsb3IgY3LDrXRpY28gYmlsYXRlcmFsIHBhcmEgJFxcYWxwaGE9MCwxMCQgZm9yIGFwcm94aW1hZGFtZW50ZSAyLDMzLiIsICJDIjogIk8gdGVzdGUgZGUgaG9tb2dlbmVpZGFkZSBkZSB2YXJpw6JuY2lhcyDDqSBkZXNuZWNlc3PDoXJpbyBuZXN0ZSBjYXNvLCBwb2lzLCBjb21vICRuX3sxfSA9IG5fezJ9JCwgYSBob21vY2VkYXN0aWNpZGFkZSDDqSBnYXJhbnRpZGEgYXV0b21hdGljYW1lbnRlIHBlbG8gdGVvcmVtYSBkbyBsaW1pdGUgY2VudHJhbC4iLCAiRCI6ICJBIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSDDqSBvIHF1b2NpZW50ZSAkU197MX1eezJ9L1NfezJ9XnsyfSQsIG1hcywgZGV2aWRvIMOgIGlndWFsZGFkZSBkb3MgdGFtYW5ob3MgYW1vc3RyYWlzLCBhIGRpc3RyaWJ1acOnw6NvIGRlIHJlZmVyw6puY2lhIMOpIGEgbm9ybWFsIHBhZHLDo28gJE4oMCwxKSQuIiwgIkUiOiAiQSBlc3RhdMOtc3RpY2EgZGUgdGVzdGUgY29ycmV0YSBzZXJpYSAkVyA9IFNfezF9XnsyfSAtIFNfezJ9XnsyfSQsIHBvaXMgYSBob21vY2VkYXN0aWNpZGFkZSBleGlnZSBxdWUgYSBkaWZlcmVuw6dhIGRhcyB2YXJpw6JuY2lhcyBzZWphIGVzdGF0aXN0aWNhbWVudGUgaWd1YWwgYSB6ZXJvIHNvYiAkSF97MH0kLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBwYXJhIGNvbXBhcmFyIGR1YXMgdmFyacOibmNpYXMgcG9wdWxhY2lvbmFpcyBzb2IgYSBwcmVtaXNzYSBkZSBub3JtYWxpZGFkZSwgdXRpbGl6YW1vcyBvIHF1b2NpZW50ZSBkYXMgdmFyacOibmNpYXMgYW1vc3RyYWlzLCBjdWphIGRpc3RyaWJ1acOnw6NvIGFtb3N0cmFsIHNvYiAkSF97MH0kIMOpIGEgZGlzdHJpYnVpw6fDo28gJEYkIGRlIFNuZWRlY29yLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBlc3RhdMOtc3RpY2EgZGUgdGVzdGUgcGFyYSBhIGlndWFsZGFkZSBkZSBkdWFzIHZhcmnDom5jaWFzIHBvcHVsYWNpb25haXMgw6kgZGFkYSBwb3IgJFcgPSBTX3sxfV57Mn0vU197Mn1eezJ9JC4gU29iIGEgaGlww7N0ZXNlIG51bGEgJEhfezB9OiBcXHNpZ21hX3sxfV57Mn0gPSBcXHNpZ21hX3syfV57Mn0kLCBlIGFzc3VtaW5kbyBub3JtYWxpZGFkZSwgZXNzYSB2YXJpw6F2ZWwgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvICRGJCBjb20gJGdsX3tcXHRleHR7bnVtfX0gPSBuX3sxfS0xID0gMTUkIGUgJGdsX3tcXHRleHR7ZGVufX0gPSBuX3syfS0xID0gMTUkLiBDb20gJHdfezB9ID0gNDUvMjUgPSAxLDgkIGUgdW0gdmFsb3IgY3LDrXRpY28gZGUgYXByb3hpbWFkYW1lbnRlIDIsMzMgcGFyYSAkXFxhbHBoYT0wLDEwJCAoYmlsYXRlcmFsKSwgY29tbyAkMSw4IDwgMiwzMyQsIG7Do28gcmVqZWl0YW1vcyAkSF97MH0kLCBpbmRpY2FuZG8gcXVlIG7Do28gaMOhIGV2aWTDqm5jaWEgZGUgaGV0ZXJvY2VkYXN0aWNpZGFkZS4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDAsIDQsIDIwMClcbnkgPSBzdGF0cy5mLnBkZih4LCAxNSwgMTUpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9J0Rpc3RyaWJ1acOnw6NvIEYoMTUsMTUpJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJywgd2lkdGg9MikpKVxuZmlnLmFkZF92bGluZSh4PTEuOCwgbGluZT1kaWN0KGNvbG9yPScjMTBCOTgxJywgZGFzaD0nZGFzaCcpLCBuYW1lPSdFc3RhdMOtc3RpY2EgVz0xLjgnKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0Rpc3RyaWJ1acOnw6NvIEYgc29iICRIX3swfSQgZSBFc3RhdMOtc3RpY2EgT2JzZXJ2YWRhJywgeGF4aXNfdGl0bGU9J0VzdGF0w61zdGljYSBkZSBUZXN0ZSAoJEYkKScsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMywgcC4gMzY1In0sIHsiZW51bmNpYWRvIjogIkVtIHVtYSBhbsOhbGlzZSBkZSByZXPDrWR1b3MgZGUgdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIHBhcmEgcHJldmVyIGEgZWZpY2nDqm5jaWEgZW5lcmfDqXRpY2EgZGUgbW90b3JlcywgbyBwZXNxdWlzYWRvciBzdXNwZWl0YSBkZSBoZXRlcm9jZWRhc3RpY2lkYWRlLiBTZSBlbGUgZGVzZWphIHJlYWxpemFyIHVtIHRlc3RlIGRlIGlndWFsZGFkZSBkZSB2YXJpw6JuY2lhcyBlbnRyZSBkb2lzIGdydXBvcyBkaXN0aW50b3MgZGUgbW90b3JlcyAoR3J1cG8gMSBlIEdydXBvIDIpIGNvbSB2YXJpw6JuY2lhcyBhbW9zdHJhaXMgJFNfezF9XnsyfSQgZSAkU197Mn1eezJ9JCwgcG9yIHF1ZSBhIHZpb2xhw6fDo28gZGEgcHJlbWlzc2EgZGUgaG9tb2NlZGFzdGljaWRhZGUgw6kgY29uc2lkZXJhZGEgdW0gcHJvYmxlbWEgXFxncmF2ZT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgaGV0ZXJvY2VkYXN0aWNpZGFkZSBpbnZhbGlkYSBhIG3DqWRpYSBkYXMgYW1vc3RyYXMsIHRvcm5hbmRvIG9zIGVzdGltYWRvcmVzICRcXGJhcntYfV97MX0kIGUgJFxcYmFye1h9X3syfSQgdmljaWFkb3MuIiwgIkIiOiAiQSBoZXRlcm9jZWRhc3RpY2lkYWRlIHRvcm5hIGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlICR0JCBcXGluw7p0aWwsIHBvaXMgYSB2YXJpw6JuY2lhIHBvbmRlcmFkYSB1dGlsaXphZGEgbm8gdGVzdGUgJHQkIGRlaXhhIGRlIHNlciB1bWEgZXN0aW1hdGl2YSBjb25zaXN0ZW50ZSBkYSB2YXJpw6JuY2lhIGNvbXVtICRcXHNpZ21hXnsyfSQuIiwgIkMiOiAiQSBob21vY2VkYXN0aWNpZGFkZSDDqSBuZWNlc3PDoXJpYSBhcGVuYXMgc2UgbyB0YW1hbmhvIGFtb3N0cmFsICRuJCBmb3IgaW5mZXJpb3IgYSAzMCwgc2VuZG8gaXJyZWxldmFudGUgcGFyYSBncmFuZGVzIGFtb3N0cmFzLiIsICJEIjogIlNlIGFzIHZhcmnDom5jaWFzIGZvcmVtIGRpZmVyZW50ZXMsIG8gcXVvY2llbnRlICRTX3sxfV57Mn0vU197Mn1eezJ9JCBkZWl4YSBkZSBzZWd1aXIgdW1hIGRpc3RyaWJ1acOnw6NvICRGJCBlIHBhc3NhIGEgc2VndWlyIHVtYSBkaXN0cmlidWnDp8OjbyBiaW5vbWlhbC4iLCAiRSI6ICJBIGhldGVyb2NlZGFzdGljaWRhZGUgaW1wbGljYSBxdWUgYSBzb21hIGRvcyByZXPDrWR1b3MgZGV2ZSBzZXIgb2JyaWdhdG9yaWFtZW50ZSBkaWZlcmVudGUgZGUgemVybywgbyBxdWUgcXVlYnJhIGEgaGlww7N0ZXNlIGRlIG5vcm1hbGlkYWRlLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiUGVuc2Ugbm8gdGVzdGUgJHQkIHBhcmEgYW1vc3RyYXMgaW5kZXBlbmRlbnRlcyBlIG5hIGVzdGltYXRpdmEgZGEgdmFyacOibmNpYSBjb25qdW50YSAocG9uZGVyYWRhKSBxdWUgcHJlc3N1cMO1ZSAkXFxzaWdtYV97MX1eezJ9ID0gXFxzaWdtYV97Mn1eezJ9ID0gXFxzaWdtYV57Mn0kLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBzdXBvc2nDp8OjbyBkZSBob21vY2VkYXN0aWNpZGFkZSDDqSBjcnVjaWFsIHBhcmEgbyB0ZXN0ZSAkdCQgZGUgU3R1ZGVudCBwYXJhIGFtb3N0cmFzIGluZGVwZW5kZW50ZXMsIHBvaXMgYSB2YXJpw6JuY2lhIHBvbmRlcmFkYSAoJFNfe3B9XnsyfSQpIGFzc3VtZSBxdWUgYW1iYXMgYXMgcG9wdWxhw6fDtWVzIHBvc3N1ZW0gYSBtZXNtYSB2YXJpw6JuY2lhIHBvcHVsYWNpb25hbCAkXFxzaWdtYV57Mn0kLiBTZSBlc3RhIHByZW1pc3NhIMOpIHZpb2xhZGEsIG8gZXJybyBwYWRyw6NvIGVzdGltYWRvIHRvcm5hLXNlIGluYXByb3ByaWFkbywgY29tcHJvbWV0ZW5kbyBvIHZhbG9yIGRlICR0X3tcXHRleHR7Y2FsY319JCBlIGEgdmFsaWRhZGUgZG9zIGludGVydmFsb3MgZGUgY29uZmlhbsOnYSBlIHAtdmFsb3JlcywgcG9kZW5kbyBsZXZhciBhIGNvbmNsdXPDtWVzIGZhbHNhcyBzb2JyZSBhcyBtw6lkaWFzLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTUsIHAuIDQyNiJ9LCB7ImVudW5jaWFkbyI6ICJVbSBlbmdlbmhlaXJvIGRlIHF1YWxpZGFkZSBlbSB1bWEgcGxhbnRhIGRlIG1vbnRhZ2VtIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyBkZXNlamEgY29tcGFyYXIgYSBlc3RhYmlsaWRhZGUgZGUgZHVhcyBtw6FxdWluYXMgZGUgcHJlY2lzw6NvIChBIGUgQikuIEEgbcOhcXVpbmEgQSBwcm9kdXppdSB1bWEgYW1vc3RyYSBkZSAkbl9BID0gMTAkIHBlw6dhcyBjb20gdmFyacOibmNpYSBhbW9zdHJhbCAkU19BXjIgPSAyNSQsIGVucXVhbnRvIGEgbcOhcXVpbmEgQiwgb3BlcmFuZG8gc29iIGNvbmRpw6fDtWVzIGlkw6pudGljYXMsIHByb2R1eml1ICRuX0IgPSA4JCBwZcOnYXMgY29tIHZhcmnDom5jaWEgYW1vc3RyYWwgJFNfQl4yID0gMTAkLiBDb25zaWRlcmFuZG8gYSBzdXBvc2nDp8OjbyBkZSBxdWUgYXMgbWVkaWRhcyBkZSByZXNpc3TDqm5jaWEgZGFzIHBlw6dhcyBzZWd1ZW0gZGlzdHJpYnVpw6fDtWVzIG5vcm1haXMsIHF1YWwgw6kgbyB2YWxvciBkYSBlc3RhdMOtc3RpY2EgJEZfe1x0ZXh0e2NhbGN9fSQgcGFyYSB0ZXN0YXIgYSBoaXDDs3Rlc2UgZGUgaWd1YWxkYWRlIGRlIHZhcmnDom5jaWFzIHBvcHVsYWNpb25haXMgKCRIXzA6IFxmcmFje1x0ZXh0e03DoXF1aW5hIEF9fXtcdGV4dHtNw6FxdWluYSBCfX0kKSwgY29uc2lkZXJhbmRvICRTX0FeMiQgbm8gbnVtZXJhZG9yPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiMCw0MCIsICJCIjogIjIsNTAiLCAiQyI6ICIwLDgwIiwgIkQiOiAiMSwyNSIsICJFIjogIjAsNjAifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgYSBlc3RhdMOtc3RpY2EgRiBkZSBTbmVkZWNvciBwYXJhIG8gdGVzdGUgZGUgcmF6w6NvIGRlIHZhcmnDom5jaWFzIMOpIGRhZGEgcGVsbyBxdW9jaWVudGUgZGFzIHZhcmnDom5jaWFzIGFtb3N0cmFpcyAkRiA9IFNfMV4yIC8gU18yXjIkIHNvYiBhIGhpcMOzdGVzZSBudWxhIGRlIGlndWFsZGFkZSBkYXMgdmFyacOibmNpYXMgcG9wdWxhY2lvbmFpcy4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgZXN0YXTDrXN0aWNhICRGJCBkZSBTbmVkZWNvciDDqSBkZWZpbmlkYSBwZWxhIHJhesOjbyBkZSBkdWFzIGVzdGltYXRpdmFzIGRlIHZhcmnDom5jaWEgbsOjbyB2aWNpYWRhcywgbm9ybWFsaXphZGFzIHBlbG9zIHNldXMgcmVzcGVjdGl2b3MgZ3JhdXMgZGUgbGliZXJkYWRlLiBTb2IgYSBoaXDDs3Rlc2UgbnVsYSBkZSBpZ3VhbGRhZGUgZGFzIHZhcmnDom5jaWFzIHBvcHVsYWNpb25haXMgKCRIXzA6IFxmcmFje1x0ZXh0e03DoXF1aW5hIEF9fXtcdGV4dHtNw6FxdWluYSBCfX0gPSAxJCksIGEgZXN0YXTDrXN0aWNhIMOpIHNpbXBsZXNtZW50ZSBhIHJhesOjbyBkYXMgdmFyacOibmNpYXMgYW1vc3RyYWlzOiAkJEZfe1x0ZXh0e2NhbGN9fSA9IFxcZnJhY3tTX0FeMn17U19CXjJ9JCQuIFN1YnN0aXR1aW5kbyBvcyB2YWxvcmVzIGZvcm5lY2lkb3M6ICQkRl97XHRleHR7Y2FsY319ID0gXFxmcmFjezI1fXsxMH0gPSAyLDUkJC4gUG9ydGFudG8sIGEgYWx0ZXJuYXRpdmEgY29ycmV0YSDDqSBhIEIuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMywgcC4gMzY2In0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBkdWFzIHZhcmnDoXZlaXMgYWxlYXTDs3JpYXMgaW5kZXBlbmRlbnRlcyAkVSBcdGV4dHsgZSB9IFYkLCBvbmRlICRVIFx0ZXh0eyBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gUXVpLVF1YWRyYWRvIGNvbSB9IGdsX3tcdGV4dHtudW19fSA9IDUgXHRleHR7IGdyYXVzIGRlIGxpYmVyZGFkZSBlIH0gViBcdGV4dHsgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIFF1aS1RdWFkcmFkbyBjb20gfSBnbF97XHRleHR7ZGVufX0gPSA3IFx0ZXh0eyBncmF1cyBkZSBsaWJlcmRhZGV9JC4gU2UgZGVmaW5pcm1vcyAkVyA9IFxcZnJhY3tVIC8gNX17ViAvIDd9JCwgcXVhbCBkYXMgcHJvcHJpZWRhZGVzIGFiYWl4byBjYXJhY3Rlcml6YSBjb3JyZXRhbWVudGUgYSBkaXN0cmlidWnDp8OjbyBkZSAkVyQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIGRpc3RyaWJ1acOnw6NvIGRlIFcgw6kgXFxzaW3DqXRyaWNhIGVtIHJlbGHDp8OjbyDDoCBtw6lkaWEgMS4iLCAiQiI6ICJBIHZhcmnDoXZlbCBXIHBvZGUgYXNzdW1pciB2YWxvcmVzIG5lZ2F0aXZvcyBjb25mb3JtZSBhIG5hdHVyZXphIGRhcyBkaXN0cmlidWnDp8O1ZXMgcXVpLXF1YWRyYWRvLiIsICJDIjogIkEgZGVuc2lkYWRlIGRlIFcgw6kgZGVzY3JpdGEgcGVsYSBkaXN0cmlidWnDp8OjbyBGIGRlIFNuZWRlY29yIGNvbSBwYXLDom1ldHJvcyA1IGUgNywgc2VuZG8gY29uZmluYWRhIGFvIGRvbcOtbmlvIGRvcyBuw7ptZXJvcyBwb3NpdGl2b3MuIiwgIkQiOiAiQSBtw6lkaWEgZGUgVyDDqSBzZW1wcmUgaWd1YWwgYSAwLCBpbmRlcGVuZGVudGVtZW50ZSBkb3MgZ3JhdXMgZGUgbGliZXJkYWRlLiIsICJFIjogIkEgdmFyacOhdmVsIFcgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIE5vcm1hbCBwYWRyw6NvIGRhZG8gbyBjb21wb3J0YW1lbnRvIGFzc2ludMOzdGljbyBkb3MgZ3JhdXMgZGUgbGliZXJkYWRlLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiUmV2aXNlIGEgZGVmaW5pw6fDo28gZm9ybWFsIGRhIGRpc3RyaWJ1acOnw6NvIEYgZGUgU25lZGVjb3IgY29tbyBhIHJhesOjbyBlbnRyZSBkdWFzIHZhcmnDoXZlaXMgUXVpLVF1YWRyYWRvIG5vcm1hbGl6YWRhcyBwb3Igc2V1cyByZXNwZWN0aXZvcyBncmF1cyBkZSBsaWJlcmRhZGUuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGRpc3RyaWJ1acOnw6NvIEYgZGUgU25lZGVjb3Igw6ksIHBvciBkZWZpbmnDp8OjbywgYSBkaXN0cmlidWnDp8OjbyBkbyBxdW9jaWVudGUgZGUgZHVhcyB2YXJpw6F2ZWlzIGFsZWF0w7NyaWFzIGluZGVwZW5kZW50ZXMgY29tIGRpc3RyaWJ1acOnw6NvIFF1aS1RdWFkcmFkbywgY2FkYSB1bWEgZGl2aWRpZGEgcGVsb3Mgc2V1cyByZXNwZWN0aXZvcyBncmF1cyBkZSBsaWJlcmRhZGUgKCRGID0gXFxmcmFje1UvZ2xfe1x0ZXh0e251bX19fXtWL2dsX3tcdGV4dHtkZW59fX0kKS4gQ29tbyAkVSBcXHNpbSBcXGNoaV4yKDUpJCBlICRWIFxcc2ltIFxcY2hpXjIoNykkLCB0ZW1vcyBxdWUgJFcgXFxzaW0gRig1LCA3KSQuIEVzdGEgZGlzdHJpYnVpw6fDo28gw6kgY2FyYWN0ZXJpemFkYSBwb3Igc2VyIGFzc2ltw6l0cmljYSDDoCBkaXJlaXRhIGUgZXN0YXIgZGVmaW5pZGEgZXN0cml0YW1lbnRlIG5vIGludGVydmFsbyAkWzAsICtcYlxcZXRhWyQsIGV4Y2x1aW5kbyBhIHBvc3NpYmlsaWRhZGUgZGUgdmFsb3JlcyBuZWdhdGl2b3MsIG8gcXVlIHRvcm5hIGEgYWx0ZXJuYXRpdmEgQyBhIMO6bmljYSBjb3JyZXRhLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoMC4wMSwgNSwgMjAwKVxueSA9IHN0YXRzLmYucGRmKHgsIDUsIDcpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9J0YoNSw3KScsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTMpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5EaXN0cmlidWnDp8OjbyBGIGRlIFNuZWRlY29yICg1LCA3KTwvYj4nLCB4YXhpc190aXRsZT0neCcsIHlheGlzX3RpdGxlPSdmKHgpJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgNywgcC4gMTkxIn0sIHsiZW51bmNpYWRvIjogIkVtIHVtYSBsaW5oYSBkZSBtb250YWdlbSBhdXRvbWF0aXphZGEsIGRlc2VqYS1zZSBjb21wYXJhciBhIGVzdGFiaWxpZGFkZSBkZSBkb2lzIGJyYcOnb3Mgcm9iw7N0aWNvcywgQSBlIEIuIEEgdmFyacOibmNpYSBhbW9zdHJhbCBkbyB0ZW1wbyBkZSBjaWNsbyBkbyBicmHDp28gQSBmb2kgJFNfe0F9XnsyfSA9IDE1LjIkIG1zJF4yJCAoY29tICRuX3tBfSA9IDIxJCkgZSBkbyBicmHDp28gQiBmb2kgJFNfe0J9XnsyfSA9IDEyLjgkIG1zJF4yJCAoY29tICRuX3tCfSA9IDIxJCkuIFBhcmEgdW0gbsOtdmVsIGRlIGNvbmZpYW7Dp2EgZGUgOTUlLCBmb2kgY29uc3RydcOtZG8gbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBwYXJhIGEgcmF6w6NvIGRlIHZhcmnDom5jaWFzICRcXHNpZ21hX3tBfV57Mn0gLyBcXHNpZ21hX3tCfV57Mn0kLCByZXN1bHRhbmRvIGVtICRbMC40OCwgMi41Nl0kLiBDb20gYmFzZSBuZXNzZSByZXN1bHRhZG8sIHF1YWwgw6kgYSBjb25jbHVzw6NvIGVzdGF0w61zdGljYSBtYWlzIGFkZXF1YWRhIHBhcmEgYSBnZXN0w6NvIGRhIHF1YWxpZGFkZT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk7Do28gaMOhIGV2aWTDqm5jaWFzIGVzdGF0w61zdGljYXMgcGFyYSBhZmlybWFyIHF1ZSBhcyB2YXJpYWJpbGlkYWRlcyBkb3MgYnJhw6dvcyByb2LDs3RpY29zIHPDo28gZGlmZXJlbnRlcywgcG9pcyBvIGludGVydmFsbyBpbmNsdWkgYSB1bmlkYWRlLiIsICJCIjogIk8gYnJhw6dvIHJvYsOzdGljbyBBIMOpIHNpZ25pZmljYXRpdmFtZW50ZSBtYWlzIGluc3TDoXZlbCBxdWUgbyBicmHDp28gQiwgZGFkbyBxdWUgYSByYXrDo28gZGFzIHZhcmnDom5jaWFzIGFtb3N0cmFpcyDDqSBtYWlvciBxdWUgMS4iLCAiQyI6ICJPIGludGVydmFsbyBpbmRpY2EgcXVlIGEgdmFyacOibmNpYSBkbyBicmHDp28gQiDDqSwgb2JyaWdhdG9yaWFtZW50ZSwgbWFpb3IgcXVlIGEgZG8gYnJhw6dvIEEuIiwgIkQiOiAiTyBwcm9jZWRpbWVudG8gZGUgaW5mZXLDqm5jaWEgZXN0w6EgaW5jb3JyZXRvLCBwb2lzIG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgZGV2ZXJpYSBzZXIgY2VudHJhZG8gZW0gemVybyBwYXJhIGluZGljYXIgaWd1YWxkYWRlLiIsICJFIjogIkEgdmFyaWFiaWxpZGFkZSBkb3MgYnJhw6dvcyDDqSBpZMOqbnRpY2EsIHZpc3RvIHF1ZSBhIG3DqWRpYSBkb3MgZXh0cmVtb3MgZG8gaW50ZXJ2YWxvIMOpIHN1cGVyaW9yIGEgMS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBwcm9wcmllZGFkZSBmdW5kYW1lbnRhbCBkb3MgaW50ZXJ2YWxvcyBkZSBjb25maWFuw6dhIHBhcmEgcmF6w7VlczogcXVhbmRvIG8gdmFsb3IgMSBlc3TDoSBjb250aWRvIG5vIGludGVydmFsbywgYSBoaXDDs3Rlc2UgZGUgaWd1YWxkYWRlIGRhcyB2YXJpw6JuY2lhcyBuw6NvIHBvZGUgc2VyIGRlc2NhcnRhZGEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBbyByZWFsaXphciBhIGluZmVyw6puY2lhIHNvYnJlIGEgcmF6w6NvIGRlIGR1YXMgdmFyacOibmNpYXMgcG9wdWxhY2lvbmFpcyAkXFxzaWdtYV97MX1eezJ9IC8gXFxzaWdtYV97Mn1eezJ9JCwgbyB2YWxvciAxIHJlcHJlc2VudGEgbyBjYXNvIGRlIGlndWFsZGFkZSAoJFxcc2lnbWFfezF9XnsyfSA9IFxcc2lnbWFfezJ9XnsyfSQpLiBDb21vIG8gaW50ZXJ2YWxvIGNhbGN1bGFkbyAkWzAuNDgsIDIuNTZdJCBjb2JyZSBvIHZhbG9yIDEsIGlzc28gaW1wbGljYSBxdWUsIGFvIG7DrXZlbCBkZSA5NSUgZGUgY29uZmlhbsOnYSwgbsOjbyBleGlzdGVtIGV2aWTDqm5jaWFzIHN1ZmljaWVudGVzIHBhcmEgcmVqZWl0YXIgYSBoaXDDs3Rlc2UgZGUgcXVlIGFzIHZhcmnDom5jaWFzIHBvcHVsYWNpb25haXMgc8OjbyBpZ3VhaXMuIFBvcnRhbnRvLCBuw6NvIHBvZGVtb3MgYWZpcm1hciBxdWUgdW0gYnJhw6dvIMOpIGludHJpbnNlY2FtZW50ZSBtYWlzIHZvbMOhdGlsIHF1ZSBvIG91dHJvLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3NoYXBlKHR5cGU9J2xpbmUnLCB4MD0xLCB5MD0tMC41LCB4MT0xLCB5MT0wLjUsIGxpbmU9ZGljdChjb2xvcj0nIzk5MUIxQicsIHdpZHRoPTIsIGRhc2g9J2Rhc2gnKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVswLjQ4LCAyLjU2XSwgeT1bMCwgMF0sIG1vZGU9J2xpbmVzK21hcmtlcnMnLCBuYW1lPSdJQyA5NSUnLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD00KSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+SW50ZXJ2YWxvIGRlIENvbmZpYW7Dp2EgcGFyYSBhIFJhesOjbyBkZSBWYXJpw6JuY2lhczwvYj4nLCB4YXhpcz1kaWN0KHRpdGxlPSdSYXrDo28gJFxcc2lnbWFfe0F9XnsyfSAvIFxcc2lnbWFfe0J9XnsyfSQnKSwgeWF4aXM9ZGljdChzaG93dGlja2xhYmVscz1GYWxzZSwgcmFuZ2U9Wy0xLCAxXSkpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW0gYW5hbGlzdGEgZGUgcmlzY28gZGVzZWphIGNvbXBhcmFyIGEgdm9sYXRpbGlkYWRlIGRlIGR1YXMgYcOnw7VlcywgUEVUUjQgZSBWQUxFMywgY29sZXRhbmRvIGRhZG9zIGRlIDI2IGRpYXMgw7p0ZWlzIHBhcmEgY2FkYSB1bWEuIEFww7NzIG8gY8OhbGN1bG8gZGFzIHZhcmnDom5jaWFzIGFtb3N0cmFpcywgb2J0ZXZlLXNlICRTX3sxfV57Mn0gPSA0LjAkIGUgJFNfezJ9XnsyfSA9IDIuNSQuIFV0aWxpemFuZG8gYSBkaXN0cmlidWnDp8OjbyAkRiQgZGUgU25lZGVjb3IgY29tICRnbF97MX0gPSAyNSQgZSAkZ2xfezJ9ID0gMjUkLCBlIGNvbnNpZGVyYW5kbyAkXFxhbHBoYSA9IDAuMDUkICh2YWxvcmVzIGNyw610aWNvcyAkRl97MC4wMjUsIDI1LCAyNX0gXFxhcHByb3ggMi4zNyQgZSAkRl97MC45NzUsIDI1LCAyNX0gXFxhcHByb3ggMC40MiQpLCBxdWFsIGRhcyBvcMOnw7VlcyBhYmFpeG8gcmVwcmVzZW50YSBjb3JyZXRhbWVudGUgb3MgbGltaXRlcyBkbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBwYXJhIGEgcmF6w6NvICRcXHNpZ21hX3sxfV57Mn0gLyBcXHNpZ21hX3syfV57Mn0kPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJFswLjY3LCAzLjgxXSQiLCAiQiI6ICIkWzAuNTUsIDMuMjVdJCIsICJDIjogIiRbMC40MiwgMi4zN10kIiwgIkQiOiAiJFswLjYwLCAzLjc1XSQiLCAiRSI6ICIkWzAuODUsIDQuMTBdJCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiQXBsaXF1ZSBhIGbDs3JtdWxhICRJQyA9IFxcbGVmdFsgXFxmcmFje1NfezF9XnsyfX17U197Mn1eezJ9fSBcXGNkb3QgXFxmcmFjezF9e0Zfe1xcYWxwaGEvMiwgZ2xfezF9LCBnbF97Mn19fSwgXFxmcmFje1NfezF9XnsyfX17U197Mn1eezJ9fSBcXGNkb3QgXFxmcmFjezF9e0ZfezEtXFxhbHBoYS8yLCBnbF97MX0sIGdsX3syfX19IFxccmlnaHRdJC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkRhZG8gcXVlICRTX3sxfV57Mn0vU197Mn1eezJ9ID0gNC4wIC8gMi41ID0gMS42JC4gQXBsaWNhbmRvIG9zIHZhbG9yZXMgY3LDrXRpY29zOiBMaW1pdGUgSW5mZXJpb3IgPSAkMS42IFxcY2RvdCAoMSAvIDIuMzcpIFxcYXBwcm94IDAuNjc1JDsgTGltaXRlIFN1cGVyaW9yID0gJDEuNiBcXGNkb3QgKDEgLyAwLjQyKSBcXGFwcHJveCAzLjgwOSQuIEFycmVkb25kYW5kbyBwYXJhIGR1YXMgY2FzYXMgZGVjaW1haXMsIG9idGVtb3MgbyBpbnRlcnZhbG8gJFswLjY3LCAzLjgxXSQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9XSwgInF1ZXN0b2VzX2Rpc2N1cnNpdmFzIjogW3siZW51bmNpYWRvIjogIkNvbnNpZGVyZSBkb2lzIHByb2Nlc3NvcyBkZSBmYWJyaWNhw6fDo28gZGUgY29tcG9uZW50ZXMgw7NwdGljb3MuIE8gUHJvY2Vzc28gQSBnZXJvdSB1bWEgdmFyacOibmNpYSBhbW9zdHJhbCAkU197QX1eezJ9ID0gMTIwJCBjb20gJG5fe0F9ID0gMTEkIGUgbyBQcm9jZXNzbyBCIGdlcm91ICRTX3tCfV57Mn0gPSA0MCQgY29tICRuX3tCfSA9IDExJC4gVGVzdGUgYSBoaXDDs3Rlc2UgZGUgaG9tb2NlZGFzdGljaWRhZGUgJEhfezB9OiBcXHNpZ21hX3tBfV57Mn0gPSBcXHNpZ21hX3tCfV57Mn0kIGFvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBkZSAkXFxhbHBoYSA9IDAsMDUkLiBBcHJlc2VudGUgbyBjw6FsY3VsbyBkYSBlc3RhdMOtc3RpY2EgJEZfe1xcdGV4dHtjYWxjfX0kIGUgYSBjb25jbHVzw6NvIGNvbXBhcmFuZG8gY29tIG8gdmFsb3IgY3LDrXRpY28gZGEgdGFiZWxhICRGKDEwLCAxMCkkLiIsICJkaWNhIjogIkEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlIMOpICRGID0gU197QX1eezJ9IC8gU197Qn1eezJ9JCBjb20gJGdsX3tcXHRleHR7bnVtfX0gPSBuX3tBfS0xJCBlICRnbF97XFx0ZXh0e2Rlbn19ID0gbl97Qn0tMSQuIENvbnN1bHRlIGEgdGFiZWxhIEYgcGFyYSAkMTAsIDEwJCBnLmwuIGNvbSAkXFxhbHBoYS8yID0gMCwwMjUkIHBhcmEgdW0gdGVzdGUgYmljYXVkYWwuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIERlZmluaXIgYXMgaGlww7N0ZXNlczogJEhfezB9OiBcXHNpZ21hX3tBfV57Mn0gPSBcXHNpZ21hX3tCfV57Mn0kIGUgJEhfezF9OiBcXHNpZ21hX3tBfV57Mn0gXFxuZXEgXFxzaWdtYV97Qn1eezJ9JC4iLCAiMi4gQ2FsY3VsYXIgYSBlc3RhdMOtc3RpY2EgZGUgdGVzdGU6ICRGX3tcXHRleHR7Y2FsY319ID0gU197QX1eezJ9IC8gU197Qn1eezJ9ID0gMTIwIC8gNDAgPSAzLDAkLiIsICIzLiBEZXRlcm1pbmFyIG9zIGdyYXVzIGRlIGxpYmVyZGFkZTogJGdsX3tcXHRleHR7bnVtfX0gPSAxMS0xID0gMTAkIGUgJGdsX3tcXHRleHR7ZGVufX0gPSAxMS0xID0gMTAkLiIsICI0LiBFbmNvbnRyYXIgbyB2YWxvciBjcsOtdGljbyBkYSBkaXN0cmlidWnDp8OjbyBGOiBQYXJhICRcXGFscGhhPTAsMDUkIGJpY2F1ZGFsLCB1c2Ftb3MgbyB2YWxvciBjcsOtdGljbyBzdXBlcmlvciAkRl97MCwwMjV9KDEwLCAxMCkgXFxhcHByb3ggMyw3MiQuIiwgIjUuIENvbmNsdXPDo286IENvbW8gJDMsMCA8IDMsNzIkLCBuw6NvIHJlamVpdGFtb3MgJEhfezB9JC4gTsOjbyBow6EgZXZpZMOqbmNpYXMgc3VmaWNpZW50ZXMgcGFyYSBhZmlybWFyIHF1ZSBhcyB2YXJpw6JuY2lhcyBkb3MgcHJvY2Vzc29zIHPDo28gZGlmZXJlbnRlcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMywgcC4gMzY1IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMy4wfSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIHNvYiBhIMOzdGljYSBkYSBpbmZlcsOqbmNpYSBlc3RhdMOtc3RpY2EsIHBvciBxdWUgYSBjb21wYXJhw6fDo28gZGUgdmFyacOibmNpYXMgZGV2ZSBzZXIgcmVhbGl6YWRhICphbnRlcyogZGUgcHJvY2VkZXIgY29tIG8gdGVzdGUgZGUgY29tcGFyYcOnw6NvIGRlIG3DqWRpYXMgZW50cmUgZG9pcyBncnVwb3MuIFF1YWlzIHPDo28gYXMgY29uc2VxdcOqbmNpYXMgZGUgaWdub3JhciB1bWEgaGV0ZXJvY2VkYXN0aWNpZGFkZSBzZXZlcmEgbm8gdGVzdGUgJHQkIGRlIFN0dWRlbnQgdHJhZGljaW9uYWw/IiwgImRpY2EiOiAiRm9xdWUgbm8gaW1wYWN0byBkYSB2YXJpw6JuY2lhIG5vcyBkZW5vbWluYWRvcmVzIGRhcyBlc3RhdMOtc3RpY2FzIGRlIHRlc3RlIGUgbmEgZXN0aW1hdGl2YSBkYSB2YXJpw6JuY2lhIGNvbWJpbmFkYS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gQSBzdXBvc2nDp8OjbyBkZSBob21vZ2VuZWlkYWRlIGRlIHZhcmnDom5jaWFzIChob21vY2VkYXN0aWNpZGFkZSkgw6kgdW0gcHLDqS1yZXF1aXNpdG8gcGFyYSB1dGlsaXphciBhIHZhcmnDom5jaWEgcG9uZGVyYWRhICgkU197cH1eezJ9JCkgbm8gdGVzdGUgJHQkIGRlIFN0dWRlbnQuIiwgIjIuIFNlIGFzIHZhcmnDom5jaWFzIHPDo28gZGVzaWd1YWlzLCBhIGVzdGltYXRpdmEgJFNfe3B9XnsyfSQgbsOjbyDDqSB1bSBlc3RpbWFkb3IgY29uc2lzdGVudGUgcGFyYSB1bWEgdmFyacOibmNpYSBjb211bSAkXFxzaWdtYV57Mn0kLCBwb2lzIHRhbCB2YWxvciBjb211bSBuw6NvIGV4aXN0ZS4iLCAiMy4gSWdub3JhciBhIGhldGVyb2NlZGFzdGljaWRhZGUgbGV2YSBhIHVtYSBlc3RpbWF0aXZhIGluY29ycmV0YSBkbyBlcnJvIHBhZHLDo28gZGEgZGlmZXJlbsOnYSBkYXMgbcOpZGlhcyAkRVAoXFxiYXJ7WH1fezF9LVxcYmFye1h9X3syfSkgPSBcXHNxcnR7U197cH1eezJ9KDEvbl97MX0gKyAxL25fezJ9KX0kLiIsICI0LiBDb25zZXF1ZW50ZW1lbnRlLCBvICR0X3tcXHRleHR7Y2FsY319JCByZXN1bHRhbnRlIHRvcm5hLXNlIGludsOhbGlkbywgZGlzdG9yY2VuZG8gbyAkcFxcdGV4dHstdmFsb3J9JCBlIGF1bWVudGFuZG8gbyByaXNjbyBkZSBjb21ldGVyIEVycm8gVGlwbyBJIG91IFRpcG8gSUkgaW5qdXN0aWZpY2FkYW1lbnRlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEzLCBwLiAzNjkiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIHNvYnJlIG8gdGVtcG8gZGUgcmVhw6fDo28sIHZvY8OqIHBvc3N1aSB0csOqcyBncnVwb3MgY29tIG9zIHNlZ3VpbnRlcyB0YW1hbmhvcyBhbW9zdHJhaXMgZSB2YXJpw6JuY2lhczogR3J1cG8gMSAoJG5fezF9PTEwLCBTX3sxfV57Mn09MjAkKSwgR3J1cG8gMiAoJG5fezJ9PTEwLCBTX3syfV57Mn09MjUkKSBlIEdydXBvIDMgKCRuX3szfT0xMCwgU197M31eezJ9PTMwJCkuIENhbGN1bGUgYSB2YXJpw6JuY2lhIHBvbmRlcmFkYSAoJFNfe2V9XnsyfSQpIHBhcmEgbyBtb2RlbG8gQU5PVkEsIHF1ZSBwcmVzc3Vww7VlIGhvbW9jZWRhc3RpY2lkYWRlLiIsICJkaWNhIjogIkEgdmFyacOibmNpYSBwb25kZXJhZGEgw6kgZGFkYSBwZWxhIG3DqWRpYSBhcml0bcOpdGljYSBkYXMgdmFyacOibmNpYXMgYW1vc3RyYWlzIHF1YW5kbyBvcyB0YW1hbmhvcyBhbW9zdHJhaXMgc8OjbyBpZ3VhaXM6ICRTX3tlfV57Mn0gPSBcXGZyYWN7XFxzdW0gKG5fe2l9LTEpU197aX1eezJ9fXtcXHN1bSAobl97aX0tMSl9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gRsOzcm11bGEgZGEgdmFyacOibmNpYSBwb25kZXJhZGE6ICRTX3tlfV57Mn0gPSBcXGZyYWN7KG5fezF9LTEpU197MX1eezJ9ICsgKG5fezJ9LTEpU197Mn1eezJ9ICsgKG5fezN9LTEpU197M31eezJ9fXsobl97MX0tMSkgKyAobl97Mn0tMSkgKyAobl97M30tMSl9JC4iLCAiMi4gU3Vic3RpdHVpw6fDo28gZG9zIHZhbG9yZXM6ICRTX3tlfV57Mn0gPSBcXGZyYWN7KDkgXFx0aW1lcyAyMCkgKyAoOSBcXHRpbWVzIDI1KSArICg5IFxcdGltZXMgMzApfXs5ICsgOSArIDl9JC4iLCAiMy4gQ8OhbGN1bG8gZG8gbnVtZXJhZG9yOiAkMTgwICsgMjI1ICsgMjcwID0gNjc1JC4iLCAiNC4gQ8OhbGN1bG8gZG8gZGVub21pbmFkb3I6ICQyNyQuIiwgIjUuIFJlc3VsdGFkbyBmaW5hbDogJFNfe2V9XnsyfSA9IDY3NSAvIDI3ID0gMjUsMCQuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZShkYXRhPVtnby5CYXIoeD1bJ0dydXBvIDEnLCAnR3J1cG8gMicsICdHcnVwbyAzJ10sIHk9WzIwLCAyNSwgMzBdLCBtYXJrZXJfY29sb3I9JyMxRTNBOEEnKV0pXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nVmFyacOibmNpYXMgQW1vc3RyYWlzIHBvciBHcnVwbycsIHlheGlzX3RpdGxlPSdWYXJpw6JuY2lhICgkU157Mn0kKScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDE1LCBwLiA0MzciLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAyNS4wfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIGVuZ2VuaGFyaWEgaW5kdXN0cmlhbCwgZHVhcyBsaW5oYXMgZGUgcHJvZHXDp8OjbyBvcGVyYW0gZW0gcmVnaW1lIGRlIGFsdGEgcHJlY2lzw6NvLiBBIExpbmhhIEEsIGNvbSAkbl9BID0gMTYkIGNvbXBvbmVudGVzLCBhcHJlc2VudG91IHZhcmnDom5jaWEgYW1vc3RyYWwgJFNfQV4yID0gNDgkLiBBIExpbmhhIEIsIGNvbSAkbl9CID0gMTEkIGNvbXBvbmVudGVzLCBhcHJlc2VudG91ICRTX0JeMiA9IDEyJC4gVGVzdGUgYSBoaXDDs3Rlc2UgJEhfMDogXGZyYWN7XHRleHR7TcOhcXVpbmEgQX19e1x0ZXh0e03DoXF1aW5hIEJ9fSA9IDEkIGNvbnRyYSAkSF8xOiBcZnJhY3tcdGV4dHtNw6FxdWluYSBBfX17XHRleHR7TcOhcXVpbmEgQn19IFxcbmVxIDEkIGFvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBkZSAkXFxhbHBoYSA9IDAsMTAkLiBFeHBsaXF1ZSBvIHByb2NlZGltZW50byBlIG9zIGdyYXVzIGRlIGxpYmVyZGFkZSBlbnZvbHZpZG9zLiIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgJEZfe1x0ZXh0e2NhbGN9fSA9IFNfMV4yIC8gU18yXjIkIGUgcXVlIHZvY8OqIGRldmUgdmVyaWZpY2FyIHNlIG8gdmFsb3IgY2FsY3VsYWRvIHVsdHJhcGFzc2Egb3MgbGltaXRlcyBjcsOtdGljb3MgZGEgdGFiZWxhIEYgcGFyYSAkXFxhbHBoYS8yJCAoYmlsYXRlcmFsKS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gRGVmaW5pciBhcyBoaXDDs3Rlc2VzOiAkSF8wOiBcXHNpZ21hX0FeMiA9IFxcc2lnbWFfQl4yJCBlICRIXzE6IFxcc2lnbWFfQV4yIFxcbmVxIFxcc2lnbWFfQl4yJC4iLCAiMi4gQ2FsY3VsYXIgYSBlc3RhdMOtc3RpY2EgRjogJEZfe1x0ZXh0e2NhbGN9fSA9IFxcZnJhY3tTX0FeMn17U19CXjJ9ID0gXFxmcmFjezQ4fXsxMn0gPSA0LDAkLiIsICIzLiBEZXRlcm1pbmFyIG9zIGdyYXVzIGRlIGxpYmVyZGFkZTogJGdsX3tcdGV4dHtudW19fSA9IG5fQSAtIDEgPSAxNSQgZSAkZ2xfe1x0ZXh0e2Rlbn19ID0gbl9CIC0gMSA9IDEwJC4iLCAiNC4gQ29tcGFyYXIgY29tIG8gdmFsb3IgY3LDrXRpY286IFBhcmEgJFxcYWxwaGE9MCwxMCQgKGJpbGF0ZXJhbCksIGNvbnN1bHRhbW9zIGEgdGFiZWxhIEYgcGFyYSAkRigxNSwgMTApJCBuYSBjYXVkYSBzdXBlcmlvciAoJDAsMDUkKS4gTyB2YWxvciB0YWJlbGFkbyDDqSBhcHJveGltYWRhbWVudGUgJDIsODUkLiIsICI1LiBDb25jbHVzw6NvOiBDb21vICQ0LDAgPiAyLDg1JCwgcmVqZWl0YW1vcyAkSF8wJCBhbyBuw612ZWwgZGUgMTAlIGRlIHNpZ25pZmljw6JuY2lhLCBpbmRpY2FuZG8gcXVlIGFzIHZhcmlhYmlsaWRhZGVzIGRhcyBsaW5oYXMgZGUgcHJvZHXDp8OjbyBzw6NvIGVzdGF0aXN0aWNhbWVudGUgZGlmZXJlbnRlcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMywgcC4gMzY2IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogNC4wfSwgeyJlbnVuY2lhZG8iOiAiRGVtb25zdHJlLCB1dGlsaXphbmRvIGEgcmVsYcOnw6NvIGVudHJlIG9zIGdyYXVzIGRlIGxpYmVyZGFkZSBkZSB1bWEgZGlzdHJpYnVpw6fDo28gRiBkZSBTbmVkZWNvciwgY29tbyBwb2RlbW9zIGVuY29udHJhciBvIHF1YW50aWwgaW5mZXJpb3IgZGUgdW1hIGRpc3RyaWJ1acOnw6NvICRGKGdsX3tcdGV4dHtudW19fSwgZ2xfe1x0ZXh0e2Rlbn19KSQgYSBwYXJ0aXIgZGUgdmFsb3JlcyBkYSB0YWJlbGEgcGFyYSBhIGNhdWRhIHN1cGVyaW9yLiIsICJkaWNhIjogIlV0aWxpemUgYSBpZGVudGlkYWRlIGRlIGludmVyc8OjbzogJEYoZ2xfe1x0ZXh0e251bX19LCBnbF97XHRleHR7ZGVufX0pID0gMSAvIEYoZ2xfe1x0ZXh0e2Rlbn19LCBnbF97XHRleHR7bnVtfX0pJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gQSBkaXN0cmlidWnDp8OjbyBGIG7Do28gw6kgXFxzaW3DqXRyaWNhLCBzZW5kbyByZXN0cml0YSBhIHZhbG9yZXMgcG9zaXRpdm9zLiIsICIyLiBQYXJhIGVuY29udHJhciB1bSB2YWxvciAkZl8wJCB0YWwgcXVlICRQKEYgPCBmXzApID0gXFxhbHBoYSQsIHV0aWxpemFtb3MgYSBwcm9wcmllZGFkZSBkYSByZWPDrXByb2NhLiIsICIzLiBBIGlkZW50aWRhZGUgZm9ybWFsIMOpICRQKEYoZ2xfe1x0ZXh0e251bX19LCBnbF97XHRleHR7ZGVufX0pIDwgZl8wKSA9IFAoMSAvIEYoZ2xfe1x0ZXh0e2Rlbn19LCBnbF97XHRleHR7bnVtfX0pIDwgZl8wKSQuIiwgIjQuIElzc28gZXF1aXZhbGUgYSAkUChGKGdsX3tcdGV4dHtkZW59fSwgZ2xfe1x0ZXh0e251bX19KSA+IDEvZl8wKSA9IFxcYWxwaGEkLiIsICI1LiBQb3J0YW50bywgbyBxdWFudGlsIGluZmVyaW9yICRmXzAkIMOpIG8gaW52ZXJzbyBkbyBxdWFudGlsIHN1cGVyaW9yIGRhIGRpc3RyaWJ1acOnw6NvIEYgY29tIGdyYXVzIGRlIGxpYmVyZGFkZSBpbnZlcnRpZG9zICgkZ2xfe1x0ZXh0e2Rlbn19LCBnbF97XHRleHR7bnVtfX0kKS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCA3LCBwLiAxOTIiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGFkbyBxdWUgdW1hIHZhcmnDoXZlbCBhbGVhdMOzcmlhICRUJCBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gJHQkIGRlIFN0dWRlbnQgY29tICR2JCBncmF1cyBkZSBsaWJlcmRhZGUsIG1vc3RyZSBmb3JtYWxtZW50ZSwgYXRyYXbDqXMgZGFzIGRlZmluacOnw7VlcyBkZSAkVSQgZSAkViQgKFF1aS1RdWFkcmFkbyksIHF1ZSAkVF4yJCBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gJEYkIGRlIFNuZWRlY29yIGNvbSAkZ2xfe1x0ZXh0e251bX19ID0gMSQgZSAkZ2xfe1x0ZXh0e2Rlbn19ID0gdiQuIiwgImRpY2EiOiAiQ29uc2lkZXJlICRUID0gXFxmcmFje1p9e1xcc3FydHtZL3Z9fSQsIG9uZGUgJFogXFxzaW0gTigwLDEpJCBlICRZIFxcc2ltIFxcY2hpXjIodikkLiBMZW1icmUtc2UgcXVlIG8gcXVhZHJhZG8gZGUgdW1hIE5vcm1hbCBwYWRyw6NvIMOpIHVtYSBRdWktUXVhZHJhZG8gY29tIDEgZ3JhdSBkZSBsaWJlcmRhZGUuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIFRlbW9zICRUID0gXFxmcmFje1p9e1xcc3FydHtZL3Z9fSQsIGxvZ28gJFReMiA9IFxcZnJhY3taXjJ9e1kvdn0kLiIsICIyLiBQZWxhIHByb3ByaWVkYWRlIGRhcyBkaXN0cmlidWnDp8O1ZXMsIG8gcXVhZHJhZG8gZGUgdW1hIG5vcm1hbCBwYWRyw6NvIMOpIHVtYSBRdWktUXVhZHJhZG8gY29tIDEgZ3JhdSBkZSBsaWJlcmRhZGU6ICRaXjIgXFxzaW0gXFxjaGleMigxKSQuIiwgIjMuIEFzc2ltLCAkVF4yID0gXFxmcmFje1xcY2hpXjIoMSkgLyAxfXtZIC8gdn0kLiIsICI0LiBFc3RhIGV4cHJlc3PDo28gY29ycmVzcG9uZGUgZXhhdGFtZW50ZSDDoCBkZWZpbmnDp8OjbyBkZSB1bWEgdmFyacOhdmVsIEYgY29tIDEgZ3JhdSBkZSBsaWJlcmRhZGUgbm8gbnVtZXJhZG9yIGUgJHYkIGdyYXVzIGRlIGxpYmVyZGFkZSBubyBkZW5vbWluYWRvci4iLCAiNS4gUG9ydGFudG8sICRUXjIgXFxzaW0gRigxLCB2KSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTMsIHAuIDM2OSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gY2zDrW5pY28sIGR1YXMgdMOpY25pY2FzIGRlIGRvc2FnZW0gZGUgZ2xpY29zZSBzw6NvIGNvbXBhcmFkYXMuIEEgdMOpY25pY2EgQSB0ZXZlIHVtYSB2YXJpw6JuY2lhIGFtb3N0cmFsICRTX3tBfV57Mn0gPSAwLjgkIGNvbSAkbl97QX0gPSAxNiQgb2JzZXJ2YcOnw7VlcywgZW5xdWFudG8gYSB0w6ljbmljYSBCIHRldmUgJFNfe0J9XnsyfSA9IDAuMyQgY29tICRuX3tCfSA9IDE2JC4gRGV0ZXJtaW5lIG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgZGUgOTAlIHBhcmEgYSByYXrDo28gZGFzIHZhcmnDom5jaWFzIHBvcHVsYWNpb25haXMgJFxcc2lnbWFfe0F9XnsyfSAvIFxcc2lnbWFfe0J9XnsyfSQuIChDb25zaWRlcmUgcGFyYSAkZ2xfezF9PTE1LCBnbF97Mn09MTUkIG9zIHZhbG9yZXMgY3LDrXRpY29zICRGX3swLjA1LCAxNSwgMTV9IFxcYXBwcm94IDIuNDAkIGUgJEZfezAuOTUsIDE1LCAxNX0gXFxhcHByb3ggMC40MTckKSIsICJkaWNhIjogIkxlbWJyZS1zZSBxdWUgJDEgLSBcXGFscGhhID0gMC45MCQsIGxvZ28gJFxcYWxwaGEgPSAwLjEwJCBlICRcXGFscGhhLzIgPSAwLjA1JC4gTyBpbnRlcnZhbG8gw6kgZGVmaW5pZG8gcG9yICRcXGZyYWN7U197QX1eezJ9fXtTX3tCfV57Mn19IFxcY2RvdCBcXGZyYWN7MX17Rl97XFxhbHBoYS8yfX0gXFxsZXEgXFxmcmFje1xcc2lnbWFfe0F9XnsyfX17XFxzaWdtYV97Qn1eezJ9fSBcXGxlcSBcXGZyYWN7U197QX1eezJ9fXtTX3tCfV57Mn19IFxcY2RvdCBcXGZyYWN7MX17Rl97MS1cXGFscGhhLzJ9fSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IENhbGN1bGFyIGEgcmF6w6NvIGRhcyB2YXJpw6JuY2lhcyBhbW9zdHJhaXM6ICRTX3tBfV57Mn0vU197Qn1eezJ9ID0gMC44IC8gMC4zIFxcYXBwcm94IDIuNjY3JC4iLCAiUGFzc28gMjogSWRlbnRpZmljYXIgb3MgdmFsb3JlcyBjcsOtdGljb3MgZGEgZGlzdHJpYnVpw6fDo28gRjogJEZfezAuMDUsIDE1LCAxNX0gPSAyLjQwJCBlICRGX3swLjk1LCAxNSwgMTV9ID0gMC40MTckLiIsICJQYXNzbyAzOiBDYWxjdWxhciBvIGxpbWl0ZSBpbmZlcmlvcjogJDIuNjY3IFxcY2RvdCAoMSAvIDIuNDApIFxcYXBwcm94IDEuMTExJC4iLCAiUGFzc28gNDogQ2FsY3VsYXIgbyBsaW1pdGUgc3VwZXJpb3I6ICQyLjY2NyBcXGNkb3QgKDEgLyAwLjQxNykgXFxhcHByb3ggNi4zOTUkLiIsICJDb25jbHVzw6NvOiBPIGludGVydmFsbyBkZSA5MCUgZGUgY29uZmlhbsOnYSBwYXJhIGEgcmF6w6NvIGRlIHZhcmnDom5jaWFzIMOpICRbMS4xMSwgNi40MF0kLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkludGVycHJldGUgbyBzaWduaWZpY2FkbyBkZSB1bSBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBwYXJhIGEgcmF6w6NvIGRlIHZhcmnDom5jaWFzIHF1ZSBhcHJlc2VudGEgbGltaXRlcyBlc3RyaXRhbWVudGUgbWFpb3JlcyBxdWUgMSwgcG9yIGV4ZW1wbG8sICRbMS41LCAzLjJdJC4gTyBxdWUgaXNzbyBpbXBsaWNhIHNvYnJlIGEgcHJlY2lzw6NvIGRhcyBkdWFzIHBvcHVsYcOnw7VlcyBzb2IgYW7DoWxpc2U/IiwgImRpY2EiOiAiUGVuc2Ugbm8gcXVlIHNpZ25pZmljYSBhIHJhesOjbyAkXFxzaWdtYV97MX1eezJ9IC8gXFxzaWdtYV97Mn1eezJ9JCBzZXIgbWFpb3IgcXVlIDEgZSBjb21vIG8gaW50ZXJ2YWxvIGRlIGNvbmZpYW7Dp2EgcXVhbnRpZmljYSBhIGluY2VydGV6YSBkZXNzYSBlc3RpbWF0aXZhLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJPIHBhcsOibWV0cm8gZGUgaW50ZXJlc3NlIMOpIGEgcmF6w6NvICRcXHRoZXRhID0gXFxzaWdtYV97MX1eezJ9IC8gXFxzaWdtYV97Mn1eezJ9JC4iLCAiU2UgbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBkZSAkMS1cXGFscGhhJCBlc3TDoSBpbnRlaXJhbWVudGUgY29udGlkbyBubyBpbnRlcnZhbG8gJCgxLCBcXGluZnR5KSQsIHNpZ25pZmljYSBxdWUsIGNvbSBuw612ZWwgZGUgY29uZmlhbsOnYSAkMS1cXGFscGhhJCwgcG9kZW1vcyBhZmlybWFyIHF1ZSAkXFxzaWdtYV97MX1eezJ9ID4gXFxzaWdtYV97Mn1eezJ9JC4iLCAiTmEgcHLDoXRpY2EsIGlzc28gaW5kaWNhIHF1ZSBhIHBvcHVsYcOnw6NvIDEgcG9zc3VpIHVtYSB2YXJpYWJpbGlkYWRlIChkaXNwZXJzw6NvKSBzaWduaWZpY2F0aXZhbWVudGUgbWFpb3IgZG8gcXVlIGEgcG9wdWxhw6fDo28gMi4iLCAiRW0gdGVybW9zIGRlIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSwgYSBwb3B1bGHDp8OjbyAyIHNlcmlhIGNvbnNpZGVyYWRhIG1haXMgJ2VzdMOhdmVsJyBvdSAncHJlY2lzYScgZG8gcXVlIGEgcG9wdWxhw6fDo28gMS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJBbmFsaXNlIG8gaW1wYWN0byBkbyBhdW1lbnRvIGRvIHRhbWFuaG8gZGEgYW1vc3RyYSAoJG5fezF9JCBlICRuX3syfSQpIG5hIGFtcGxpdHVkZSBkbyBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBkYSByYXrDo28gZGUgdmFyacOibmNpYXMuIEV4cGxpcXVlLCBtYW50ZW5kbyBvIG7DrXZlbCBkZSBjb25maWFuw6dhIGNvbnN0YW50ZSwgcG9yIHF1ZSBhbW9zdHJhcyBtYWlvcmVzIHRlbmRlbSBhIHByb2R1emlyIGludGVydmFsb3MgbWFpcyBpbmZvcm1hdGl2b3MuIiwgImRpY2EiOiAiQ29uc2lkZXJlIG8gY29tcG9ydGFtZW50byBkb3MgdmFsb3JlcyBjcsOtdGljb3MgZGEgZGlzdHJpYnVpw6fDo28gJEYkIGUgbyBlcnJvIHBhZHLDo28gZGEgZXN0aW1hdGl2YSBkYSB2YXJpw6JuY2lhIMOgIG1lZGlkYSBxdWUgJG4kIGF1bWVudGEuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgbGFyZ3VyYSBkbyBpbnRlcnZhbG8gw6kgZGFkYSBwZWxhIGRpZmVyZW7Dp2EgZW50cmUgb3MgbGltaXRlcyBzdXBlcmlvciBlIGluZmVyaW9yOiAkTCA9IFxcZnJhY3tTX3sxfV57Mn19e1NfezJ9XnsyfX0gXFxjZG90IChcXGZyYWN7MX17Rl97MS1cXGFscGhhLzJ9fSAtIFxcZnJhY3sxfXtGX3tcXGFscGhhLzJ9fSkkLiIsICJDb25mb3JtZSAkbl97MX0kIGUgJG5fezJ9JCBhdW1lbnRhbSwgb3MgZ3JhdXMgZGUgbGliZXJkYWRlICgkZ2xfezF9LCBnbF97Mn0kKSB0YW1iw6ltIGF1bWVudGFtLiIsICJBIGRpc3RyaWJ1acOnw6NvICRGJCB0ZW5kZSBhIHNlIGNvbmNlbnRyYXIgZW0gdG9ybm8gZGUgMSDDoCBtZWRpZGEgcXVlIG9zIGdyYXVzIGRlIGxpYmVyZGFkZSBjcmVzY2VtLiIsICJDb25zZXF1ZW50ZW1lbnRlLCBhIGRpc3TDom5jaWEgZW50cmUgb3MgdmFsb3JlcyBjcsOtdGljb3MgJEZfezEtXFxhbHBoYS8yfSQgZSAkRl97XFxhbHBoYS8yfSQgZGltaW51aS4iLCAiSXNzbyByZWR1eiBhIGluY2VydGV6YSBlc3RhdMOtc3RpY2EsIHJlc3VsdGFuZG8gZW0gdW1hIGVzdGltYXRpdmEgbWFpcyBwcmVjaXNhIGUsIHBvcnRhbnRvLCB1bSBpbnRlcnZhbG8gZGUgY29uZmlhbsOnYSBtYWlzIGVzdHJlaXRvIGUgaW5mb3JtYXRpdm8uIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfV19').decode('utf-8'))


    import streamlit as st
    import numpy as np
    from scipy import stats
    import plotly.graph_objects as go
    
    # Configuração inicial de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do total de exercícios
    mcq_list = dados_exercicios.get("questoes_multipla_escolha", [])
    disc_list = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcq_list) + len(disc_list)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    # Interface de Progresso
    st.subheader(f"Exercícios: {dados_exercicios.get('topico_aula', 'Aula')}")
    if total_exercicios > 0:
        progresso = acertos / total_exercicios
        st.progress(progresso)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    
    # Seção de Múltipla Escolha
    if mcq_list:
        st.markdown("---")
        st.header("📝 Questões de Múltipla Escolha")
        for i, q in enumerate(mcq_list):
            with st.container():
                st.markdown(f"**Questão {i+1}:** {q.get('enunciado', '')}")
                
                # Gráfico Plotly
                codigo = q.get("codigo_plotly")
                if codigo:
                    try:
                        local_vars = {"np": np, "stats": stats, "go": go}
                        exec(codigo, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
                    except Exception as e:
                        st.warning("O gráfico não pôde ser carregado.")
    
                # Referência
                ref = q.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                # Alternativas
                alternativas = q.get("alternativas", {})
                opcao = st.radio("Escolha uma alternativa:", options=list(alternativas.keys()), format_func=lambda x: f"{x}: {alternativas[x]}", key=f"radio_mcq_{i}")
                
                # Botão Dica
                if st.button("💡 Dica", key=f"dica_mcq_{i}"):
                    st.info(q.get("dica", "Dica indisponível"))
                
                # Verificação
                if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
                    if opcao == q.get("alternativa_correta"):
                        st.success("Correto! Muito bem.")
                        st.session_state.respostas_certas[f"mcq_{i}"] = True
                        st.rerun()
                    else:
                        st.error("Resposta incorreta. Tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
                        st.rerun()
                
                # Gabarito Comentado
                with st.expander("✅ Ver Gabarito Comentado"):
                    st.write(q.get("gabarito_comentado", "Gabarito indisponível"))
            st.markdown("---")
    
    # Seção de Questões Discursivas
    if disc_list:
        st.header("✍️ Questões Discursivas")
        for i, q in enumerate(disc_list):
            with st.container():
                st.markdown(f"**Questão {i+1}:** {q.get('enunciado', '')}")
                
                # Gráfico Plotly
                codigo = q.get("codigo_plotly")
                if codigo:
                    try:
                        local_vars = {"np": np, "stats": stats, "go": go}
                        exec(codigo, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
                    except Exception as e:
                        pass
    
                # Referência
                ref = q.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                # Entrada de Resposta
                st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
                
                # Validação Numérica ou Qualitativa
                resposta_esperada = q.get("resposta_numerica_esperada")
                if resposta_esperada is not None:
                    user_val = st.number_input("Digite o resultado numérico calculado para validação:", key=f"num_disc_{i}", value=0.0, format="%.2f")
                    if st.button("Validar Cálculo", key=f"btn_validar_disc_{i}"):
                        if abs(user_val - resposta_esperada) <= max(0.01, 0.01 * abs(resposta_esperada)):
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
                
                # Dica
                if st.button("💡 Dica", key=f"dica_disc_{i}"):
                    st.info(q.get("dica", "Dica indisponível"))
                
                # Resolução Detalhada
                with st.expander("✅ Ver Resolução Detalhada"):
                    for passo in q.get("gabarito_passo_a_passo", []):
                        st.write(f"- {passo}")
            st.markdown("---")
