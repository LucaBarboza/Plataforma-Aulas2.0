import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDMgLSBUw7NwaWNvIDMuMjogVGVzdGUgZGUgYXNzb2NpYcOnw6NvIiwgInJlZmVyZW5jaWFzX2JpYmxpb2dyYWZpY2FzX2ZpbmFpcyI6IFsiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhIC0gQ2FwLiAxMjogVGVzdGVzIGRlIEhpcMOzdGVzZXMsIHBwLiAzMzktMzQ0IiwgIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSAtIENhcC4gMTQ6IEFuw6FsaXNlIGRlIEFkZXLDqm5jaWEgZSBBc3NvY2lhw6fDo28sIHBwLiA0MDctNDEyIl19').decode('utf-8'))

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
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"A Lógica das Tabelas de Contingência e a Hipótese de Independência")
    
    # Introdução
    st.markdown(r"""
    A análise de dados estatísticos transcende a descrição de variáveis isoladas, alcançando sua plenitude quando investigamos a relação intrínseca entre dois fenômenos qualitativos. No cerne dessa investigação encontra-se a **tabela de contingência**, uma ferramenta robusta, também denominada tabulação cruzada.
    """)
    
    st.info(r"Historicamente, a necessidade de estruturar frequências categóricas surgiu diante da limitação dos modelos contínuos em explicar fenômenos sociais e biológicos onde a observação se dá, fundamentalmente, por classificação.")
    
    st.markdown(r"""
    Ao estruturarmos um conjunto de dados sob o formato de uma tabela de contingência, nosso objetivo primordial é testar a existência de uma dependência estrutural entre variáveis. A pergunta fundamental que orienta o pesquisador é:
    - As frequências observadas divergem significativamente do modelo de independência?
    - A categoria de um indivíduo em uma variável informa sobre sua categoria na outra?
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Formalismo da Independência Estatística")
    st.markdown(r"Sob o paradigma da independência, a probabilidade de uma observação cair na célula $ij$ é o produto das probabilidades marginais:")
    
    st.latex(r"H_0: p_{ij} = p_{i.} \cdot p_{.j}, \quad \forall i=1, \dots, r; \, j=1, \dots, s")
    
    st.markdown(r"Para verificar esta hipótese, calculamos as frequências esperadas $E_{ij}$:")
    
    st.latex(r"E_{ij} = \frac{n_{i.} \cdot n_{.j}}{n}")
    
    # Dedução Analítica
    st.subheader(r"🔍 A Dedução do Modelo")
    st.markdown(r"O processo dedutivo que nos leva ao teste qui-quadrado de Pearson segue uma lógica de probabilidade composta:")
    
    st.latex(r"P(X=A_i \cap Y=B_j) = P(X=A_i) \cdot P(Y=B_j)")
    st.latex(r"E_{ij} = n \cdot P(X=A_i) \cdot P(Y=B_j) = n \cdot \frac{n_{i.}}{n} \cdot \frac{n_{.j}}{n} = \frac{n_{i.} \cdot n_{.j}}{n}")
    st.latex(r"\chi^2_{\text{calc}} = \sum_{i=1}^{r} \sum_{j=1}^{s} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}")
    
    st.warning(r"O uso desta metodologia pressupõe que as observações sejam independentes e que a amostra seja grande o suficiente. Em frequências esperadas muito reduzidas, a aproximação pelo qui-quadrado perde validade, sendo recomendado o teste exato de Fisher.")
    
    # Exemplo Prático
    st.subheader(r"📈 Caso de Aplicação: Avaliação de Métodos de Ensino")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Influência do Método de Ensino")
        st.markdown(r"Uma instituição educacional busca avaliar a associação entre o método de ensino e o desempenho. Em uma amostra de 200 discentes, analisou-se se o método (Tradicional vs. Interativo) influencia a satisfação.")
        
        st.latex(r"n=200, n_{1.}=100, n_{2.}=100, n_{.1}=140, n_{.2}=60")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Cálculo das frequências esperadas: $E_{11}=70, E_{12}=30, E_{21}=70, E_{22}=30$")
        st.markdown(r"- Cálculo da estatística: $\chi^2_{\text{calc}} = \frac{(60-70)^2}{70} + \frac{(40-30)^2}{30} + \frac{(80-70)^2}{70} + \frac{(20-30)^2}{30} = 9.522$")
        
        st.success(r"Com um valor de $\chi^2_{\text{calc}} = 9.522$ superior ao valor crítico tabelado, rejeitamos a hipótese de independência. O laudo técnico confirma que o método de ensino possui uma associação estatisticamente significativa com a satisfação do aluno, recomendando a adoção do método interativo.")
    
    # Conclusão Final
    st.markdown(r"""
    Dominar a lógica das tabelas de contingência não é apenas aplicar fórmulas; é compreender a transição do caos das frequências puras para a ordem da inferência estatística, permitindo ao pesquisador separar o ruído do acaso das associações que carregam significado científico e prático.
    """)

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    from scipy.stats import chi2
    
    # Título do Subtópico
    st.header(r"A Estatística Qui-Quadrado de Pearson: Derivação e Intuição")
    
    # Discussão Teórica
    st.markdown(r"""
    A estatística de Pearson quantifica a divergência entre observação e teoria através do desvio quadrático normalizado. Esta métrica é robusta por uma série de fundamentos:
    """)
    
    st.info(r"Pondera cada célula da tabela pelo seu valor esperado, assegurando que variações em categorias menos frequentes não sejam negligenciadas, mantendo a proporcionalidade necessária para uma inferência válida.")
    
    st.markdown(r"""
    - **Natureza da Métrica:** O valor calculado é escalar.
    - **Interpretação:** Serve como medida da 'surpresa' da amostra perante a independência teórica.
    """)
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Estatística Qui-Quadrado")
    st.latex(r"\chi^2_{\text{calc}} = \sum_{i=1}^{r} \sum_{j=1}^{s} \frac{(O_{ij} - E_{ij})^2}{E_{ij}} \sim \chi^2((r-1)(s-1))")
    
    # Dedução Analítica
    st.markdown(r"A dedução segue o princípio do desvio normalizado:")
    st.latex(r"D_{ij} = O_{ij} - E_{ij}")
    st.latex(r"Z_{ij}^2 = \frac{(O_{ij} - E_{ij})^2}{E_{ij}}")
    st.latex(r"\chi^2_{\text{calc}} = \sum_{i=1}^{r} \sum_{j=1}^{s} Z_{ij}^2")
    
    # Simulador: Mapa de Calor de Resíduos
    st.markdown(r"### 🧪 Mapa de Calor de Resíduos Padronizados")
    col1, col2 = st.columns(2)
    with col1:
        o11 = st.slider(r"Observado Linha 1, Col 1", 0, 100, 20, key=r"o11_subtopico_2")
        o12 = st.slider(r"Observado Linha 1, Col 2", 0, 100, 30, key=r"o12_subtopico_2")
    with col2:
        o21 = st.slider(r"Observado Linha 2, Col 1", 0, 100, 30, key=r"o21_subtopico_2")
        o22 = st.slider(r"Observado Linha 2, Col 2", 0, 100, 20, key=r"o22_subtopico_2")
    
    # Lógica do Simulador
    data = np.array([[o11, o12], [o21, o22]])
    row_totals = data.sum(axis=1)
    col_totals = data.sum(axis=0)
    grand_total = data.sum()
    expected = np.outer(row_totals, col_totals) / grand_total
    residuals = (data - expected)
    chi2_val = np.sum((residuals**2) / expected)
    
    # Plotagem
    fig = go.Figure(data=go.Heatmap(
        z=residuals,
        x=[r"Col 1", r"Col 2"],
        y=[r"Linha 1", r"Linha 2"],
        colorscale='RdBu',
        zmid=0
    ))
    fig.update_layout(
        template="plotly_white", height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Mapa de Calor dos Resíduos (O - E)</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Coluna", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Linha", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True)
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    st.info(rf"O valor da estatística Qui-Quadrado calculada para esta configuração é: **{chi2_val:.4f}**. Quanto maior o desvio entre observado e esperado, maior a 'surpresa' estatística captada pelo heatmap.")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Controle Industrial")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Controle de Qualidade")
        st.markdown(r"Em um controle de qualidade de uma linha industrial, verificamos a associação entre linha de produção (A ou B) e a ocorrência de defeitos. Com 500 unidades, buscamos validar se a taxa de defeito é independente do processo produtivo a 5% de significância.")
        st.latex(r"n=500, n_{1.}=250, n_{2.}=250, n_{.1}=50, n_{.2}=450")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- $E_{11} = E_{21} = (250 \cdot 50) / 500 = 25$")
        st.markdown(r"- $E_{12} = E_{22} = (250 \cdot 450) / 500 = 225$")
        st.success(r"O valor de $\chi^2_{\text{calc}} = 2.222$ não atinge o limiar crítico de 3.841. Portanto, não há evidências suficientes para rejeitar a independência, sugerindo que o controle de qualidade é estável entre as duas linhas de produção.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy.stats import chi2
    
    # Cabeçalho do Subtópico
    st.header(r"Procedimentos Inferenciais para Testes de Associação")
    
    # Discussão Teórica
    st.markdown(r"""
    A estatística inferencial não é apenas um conjunto de ferramentas computacionais, mas uma lente rigorosa que observa o caos dos dados para extrair a ordem latente sob a forma de associações. 
    Ao investigar variáveis categóricas, o desafio central reside em distinguir entre flutuações amostrais — o ruído estocástico — e uma associação real, sistemática e biologicamente ou socialmente plausível.
    """)
    
    st.info(r"A formulação das hipóteses constitui o pilar deste processo: a hipótese nula ($H_0$) postula a independência, enquanto a alternativa ($H_1$) sugere a violação desta, implicando dependência entre as variáveis.")
    
    st.markdown(r"""
    - **Erro Tipo I**: O nível de significância $\alpha$ define a tolerância máxima para rejeitar $H_0$ quando esta for verdadeira.
    - **Região Crítica ($RC$)**: Conjunto de valores da estatística de teste que, por sua raridade sob $H_0$, exigem a rejeição da hipótese nula.
    - **P-valor**: Probabilidade de obter uma estatística de teste tão ou mais extrema que a observada, assumindo que $H_0$ é verdadeira.
    """)
    
    # Formalismo Matemático e Dedução Analítica
    st.markdown(r"### 📐 O Coração Matemático: Testes de Associação")
    
    st.latex(r"p\text{-valor} = P(\chi^2_{gl} \geq \chi^2_{\text{calc}} | H_0) \leq \alpha")
    
    st.markdown(r"Para a tomada de decisão, operamos sobre os seguintes critérios analíticos:")
    
    st.latex(r"RC = \{\chi^2 : \chi^2 > \chi^2_{\text{crit}}(\alpha, gl)\}")
    st.latex(r"p\text{-valor} = \int_{\chi^2_{\text{calc}}}^{\infty} f_{\chi^2(gl)}(x) dx")
    st.latex(r"\text{Decisão: } p\text{-valor} < \alpha \implies \text{Rejeição de } H_0")
    
    # Simulador: Visualizador de Região Crítica (Qui-Quadrado)
    st.markdown(r"### 📊 Simulador: Visualizador de Região Crítica (Qui-Quadrado)")
    
    col1, col2 = st.columns(2)
    with col1:
        gl = st.slider(r"Graus de Liberdade (gl)", 1, 10, 3, key=r"gl_simulador_subtopico_3")
    with col2:
        alfa = st.select_slider(r"Nível de Significância ($\alpha$)", options=[0.01, 0.05, 0.10], value=0.05, key=r"alfa_simulador_subtopico_3")
    
    chi2_calc = st.slider(r"Valor da Estatística $\chi^2_{\text{calc}}$", 0.0, 20.0, 5.0, step=0.1, key=r"chi2_calc_subtopico_3")
    
    # Cálculo do plot
    x = np.linspace(0, 25, 500)
    y = chi2.pdf(x, gl)
    chi2_crit = chi2.ppf(1 - alfa, gl)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name=r"Distribuição $\chi^2$", line=dict(color="#1E3A8A")))
    fig.add_vline(x=chi2_crit, line_dash="dash", line_color="#991B1B", annotation_text=r"RC")
    fig.add_vline(x=chi2_calc, line_dash="solid", line_color="#10B981", annotation_text=r"Calc")
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição Qui-Quadrado e Região Crítica</b>", font=dict(size=14, color="#1E293B"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valor Qui-Quadrado", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    # Laudo dinâmico
    if chi2_calc > chi2_crit:
        st.success(f"Como $\chi^2_{{calc}} ({chi2_calc}) > \chi^2_{{crit}} ({chi2_crit:.2f})$, a evidência é estatisticamente significativa ao nível de {alfa*100}%. Rejeitamos $H_0$.")
    else:
        st.warning(f"Como $\chi^2_{{calc}} ({chi2_calc}) < \chi^2_{{crit}} ({chi2_crit:.2f})$, não há evidência suficiente para rejeitar $H_0$ ao nível de {alfa*100}%.")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Análise de Qualidade Operacional")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Turnos e Defeitos")
        st.markdown(r"Analise a associação entre o turno de trabalho (A vs B) e a produção de componentes defeituosos. Com 400 peças analisadas e uma suspeita de ineficiência no Turno B, avaliamos a dependência com $\alpha=0.05$.")
        st.latex(r"n=400, n_{1.}=200, n_{2.}=200, n_{.1}=40, n_{.2}=360")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Identificação de Frequências Esperadas: $E = 20, 180, 20, 180$")
        st.markdown(r"- Cálculo do Qui-Quadrado: $\chi^2_{\text{calc}} = \frac{(10-20)^2}{20} + \frac{(190-180)^2}{180} + \frac{(30-20)^2}{20} + \frac{(170-180)^2}{180} = 11.11$")
        st.success(r"Com $\chi^2_{\text{calc}} = 11.11 > 3.841$, rejeitamos $H_0$. Conclui-se que o turno de trabalho impacta significativamente a qualidade, sendo imperativo investigar as causas operacionais do Turno B.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    
    # --- Cabeçalho do Subtópico ---
    st.header(r"Métricas de Intensidade e Extensões do Teste: Indo além da Significância")
    
    # --- Prosa: O Problema da Amostra ---
    st.markdown(r"""
    Ao iniciarmos nossa incursão pela análise categórica, é imperativo que superemos a visão puramente dicotômica da inferência estatística, 
    que frequentemente se reduz à pergunta simplista: **"Existe uma associação estatisticamente significativa entre estas duas variáveis?"**. 
    Embora o teste qui-quadrado de independência seja uma ferramenta robusta para descartar a hipótese nula de independência, ele padece 
    de uma limitação intrínseca quando utilizado isoladamente: a estatística $\chi^2_{\text{calc}}$ é, em última instância, uma função direta do tamanho amostral $n$.
    """)
    
    st.warning(r"Em amostras de grande magnitude, mesmo disparidades ínfimas e clinicamente irrelevantes entre frequências observadas e esperadas podem levar a uma rejeição de $H_0$.")
    
    st.markdown(r"""
    Por essa razão, o pesquisador rigoroso não deve se satisfazer apenas com a verificação de significância, mas deve buscar a quantificação da magnitude 
    desse efeito, movendo-se do terreno da inferência para o campo das medidas de associação.
    """)
    
    # --- Formalismo Matemático ---
    st.subheader(r"📐 O Coração Matemático: Normalização e Intensidade")
    st.markdown(r"Para quantificar a força da associação, empregamos métricas que isolam o tamanho amostral, permitindo uma interpretação padronizada:")
    
    st.latex(r"C = \sqrt{\frac{\chi^2_{\text{calc}}}{\chi^2_{\text{calc}} + n}}")
    st.latex(r"T = \sqrt{\frac{\chi^2_{\text{calc}} / n}{\sqrt{(r-1)(s-1)}}}")
    
    st.markdown(r"""
    *   **Coeficiente de Contingência ($C$):** Uma medida de normalização que ajusta a dispersão pela massa total da observação.
    *   **Coeficiente de Tschuprow ($T$):** Um refinamento superior, que corrige a disparidade das dimensões da tabela através dos graus de liberdade, tornando-o ideal para matrizes heterogêneas.
    """)
    
    # --- Dedução Analítica ---
    st.subheader(r"🧮 Demonstração da Estrutura de Cálculo")
    
    st.markdown(r"A base de toda métrica de intensidade reside na divergência entre observados e esperados:")
    st.latex(r"\chi^2_{\text{calc}} = \sum_{i=1}^{r} \sum_{j=1}^{s} \frac{(O_{ij} - E_{ij})^2}{E_{ij}}")
    
    st.markdown(r"Onde o Valor Esperado para cada célula é obtido pela proporção das marginais:")
    st.latex(r"E_{ij} = \frac{n_{i.} n_{.j}}{n}")
    
    st.markdown(r"Com esses valores, normalizamos os resultados para o domínio [0, 1] conforme apresentado nas fórmulas de $C$ e $T$ acima.")
    
    # --- Exemplos Práticos ---
    st.subheader(r"📈 Casos de Aplicação Prática: Homogeneidade entre Regiões")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Escolaridade por Região")
        st.markdown(r"Comparamos a escolaridade (Fundamental, Médio, Superior) entre duas regiões (A e B) com amostras de 100 indivíduos por região ($n=200$).")
        
        st.latex(r"n=200, \quad n_{A}=100, \quad n_{B}=100, \quad \text{Totais: } n_{.1}=60, n_{.2}=90, n_{.3}=50")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- **Cálculo dos Esperados:** $E = 30, 45, 25$ para cada região (baseado na distribuição conjunta).")
        st.markdown(r"- **Estatística Qui-Quadrado:** $\chi^2_{\text{calc}} = 3.333 + 0.555 + 1.000 + 3.333 + 0.555 + 1.000 = 9.776$.")
        
        st.success(r"**Laudo Comercial:** O valor de $\chi^2_{\text{calc}} = 9.776$ ultrapassa o valor crítico de 5.991 ($gl=2$). A hipótese de homogeneidade é rejeitada. A diferença na distribuição de escolaridade entre as regiões é estatisticamente significante, sugerindo a necessidade de políticas públicas regionalizadas.")
    
    # --- Nota Final ---
    st.info(r"Lembre-se: A estatística $\chi^2_{\text{calc}}$ quantifica o desvio da independência, enquanto os coeficientes de intensidade medem a magnitude desse desvio. Ambos, contudo, permanecem no domínio da associação, não implicando causalidade direta.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDMgLSBUw7NwaWNvIDMuMjogVGVzdGUgZGUgYXNzb2NpYcOnw6NvIiwgInF1ZXN0b2VzX211bHRpcGxhX2VzY29saGEiOiBbeyJlbnVuY2lhZG8iOiAiVW1hIGVtcHJlc2EgZGUgdGVjbm9sb2dpYSBkZXNlamEgYXZhbGlhciBzZSBhIHByZWZlcsOqbmNpYSBkZSBzZXVzIHVzdcOhcmlvcyBwb3IgZG9pcyBzaXN0ZW1hcyBvcGVyYWNpb25haXMgKEFuZHJvaWQgb3UgaU9TKSDDqSBpbmZsdWVuY2lhZGEgcGVsbyBuw612ZWwgZGUgZXNjb2xhcmlkYWRlIGRvcyBtZXNtb3MuIEZvcmFtIGNvbGV0YWRvcyBkYWRvcyBkZSA1MDAgY2xpZW50ZXMsIGNsYXNzaWZpY2Fkb3MgZW0gdHLDqnMgbsOtdmVpcyBkZSBlc2NvbGFyaWRhZGUgKEVuc2lubyBNw6lkaW8sIFN1cGVyaW9yLCBQw7NzLUdyYWR1YcOnw6NvKS4gU29iIGEgaGlww7N0ZXNlIG51bGEgKCRIXzAkKSBkZSBxdWUgYSBwcmVmZXLDqm5jaWEgcGVsbyBzaXN0ZW1hIG9wZXJhY2lvbmFsIGluZGVwZW5kZSBkbyBuw612ZWwgZGUgZXNjb2xhcmlkYWRlLCBjb21vIGRldmVtb3MgY2FsY3VsYXIgYSBmcmVxdcOqbmNpYSBlc3BlcmFkYSAoJEVfe2lqfSQpIHBhcmEgYSBjYXNlbGEgcXVlIHJlcHJlc2VudGEgJ0Vuc2lubyBNw6lkaW8nIGUgJ0FuZHJvaWQnPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJEVfe2lqfSA9IFxcZnJhY3tuX3tpLn0gXFxjZG90IG5fey5qfX17bn0kIiwgIkIiOiAiJEVfe2lqfSA9IG4gXFxjZG90IChwX3tpLn0gKyBwX3suan0pJCIsICJDIjogIiRFX3tpan0gPSBuX3tpLn0gXFxjZG90IG5fey5qfSQiLCAiRCI6ICIkRV97aWp9ID0gXFxmcmFje25fe2kufSArIG5fey5qfX17bn0kIiwgIkUiOiAiJEVfe2lqfSA9IFxcZnJhY3tufXtuX3tpLn0gXFxjZG90IG5fey5qfX0kIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkEiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlLCBzb2IgaW5kZXBlbmTDqm5jaWEsIGEgcHJvYmFiaWxpZGFkZSBjb25qdW50YSDDqSBvIHByb2R1dG8gZGFzIG1hcmdpbmFpczogJHBfe2lqfSA9IHBfe2kufSBcXGNkb3QgcF97Lmp9JC4gTXVsdGlwbGlxdWUgZXNzYSBwcm9iYWJpbGlkYWRlIHBlbG8gdGFtYW5obyBhbW9zdHJhbCB0b3RhbCAkbiQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGhpcMOzdGVzZSBkZSBpbmRlcGVuZMOqbmNpYSBlc3RhdMOtc3RpY2EgZXN0YWJlbGVjZSBxdWUgYSBwcm9iYWJpbGlkYWRlIGRlIHVtYSBvYnNlcnZhw6fDo28gY2FpciBuYSBjYXNlbGEgJChpLCBqKSQgw6kgbyBwcm9kdXRvIGRhcyBwcm9iYWJpbGlkYWRlcyBtYXJnaW5haXM6ICRwX3tpan0gPSBwX3tpLn0gXFxjZG90IHBfey5qfSQuIENvbW8gYXMgcHJvYmFiaWxpZGFkZXMgbWFyZ2luYWlzIHPDo28gZXN0aW1hZGFzIHBvciAkcF97aS59ID0gXFxmcmFje25fe2kufX17bn0kIGUgJHBfey5qfSA9IFxcZnJhY3tuX3suan19e259JCwgYSBmcmVxdcOqbmNpYSBlc3BlcmFkYSAkRV97aWp9JCDDqSBvYnRpZGEgbXVsdGlwbGljYW5kby1zZSBhIHByb2JhYmlsaWRhZGUgZXN0aW1hZGEgcGVsbyB0b3RhbCAkbiQsIHJlc3VsdGFuZG8gZW0gJEVfe2lqfSA9IG4gXFxjZG90IFxcbGVmdChcXGZyYWN7bl97aS59fXtufVxccmlnaHQpIFxcY2RvdCBcXGxlZnQoXFxmcmFje25fey5qfX17bn1cXHJpZ2h0KSA9IFxcZnJhY3tuX3tpLn0gXFxjZG90IG5fey5qfX17bn0kLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgNCwgcC4gNzgifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gdGVzdGUgZGUgaW5kZXBlbmTDqm5jaWEgZGUgcXVpLXF1YWRyYWRvIHBhcmEgdW1hIHRhYmVsYSBkZSBjb250aW5nw6puY2lhIGRlIGRpbWVuc8O1ZXMgJDMgXFx0aW1lcyA0JCAoMyBsaW5oYXMgZSA0IGNvbHVuYXMpLCBhbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLjA1JCwgcXVhbCDDqSBvIG7Dum1lcm8gZGUgZ3JhdXMgZGUgbGliZXJkYWRlICgkZ2wkKSBjb3JyZXRvIHBhcmEgY29uc3VsdGFyIGEgZGlzdHJpYnVpw6fDo28gJFxcY2hpXjIkIG5hIHRhYmVsYSBlc3RhdMOtc3RpY2E/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIxMiIsICJCIjogIjYiLCAiQyI6ICI3IiwgIkQiOiAiNSIsICJFIjogIjIifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk8gbsO6bWVybyBkZSBncmF1cyBkZSBsaWJlcmRhZGUgcGFyYSB0YWJlbGFzIGRlIGNvbnRpbmfDqm5jaWEgw6kgZGFkbyBwZWxhIGbDs3JtdWxhICRnbCA9IChyLTEpKHMtMSkkLCBvbmRlICRyJCDDqSBvIG7Dum1lcm8gZGUgbGluaGFzIGUgJHMkIG8gbsO6bWVybyBkZSBjb2x1bmFzLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUGFyYSB1bWEgdGFiZWxhIGNvbSAkciQgbGluaGFzIGUgJHMkIGNvbHVuYXMsIG9zIGdyYXVzIGRlIGxpYmVyZGFkZSBzw6NvIGNhbGN1bGFkb3MgY29tbyAkZ2wgPSAoci0xKShzLTEpJC4gU3Vic3RpdHVpbmRvIG9zIHZhbG9yZXMgZm9ybmVjaWRvcyAoJHI9Mywgcz00JCk6ICRnbCA9ICgzLTEpKDQtMSkgPSAyIFxcY2RvdCAzID0gNiQuIEVzdGUgdmFsb3IgZGV0ZXJtaW5hIGEgZm9ybWEgZGEgZGlzdHJpYnVpw6fDo28gJFxcY2hpXjIoZ2wpJCBzb2IgYSBoaXDDs3Rlc2UgbnVsYS4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDAsIDI1LCAyMDApXG55ID0gc3RhdHMuXFxjaGkyLnBkZih4LCBkZj02KVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBuYW1lPSdEaXN0cmlidWnDp8OjbyAkXFxjaGleMig2KSQnLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnLCB3aWR0aD0zKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+RGlzdHJpYnVpw6fDo28gUXVpLVF1YWRyYWRvIChnbD02KTwvYj4nLCB4YXhpc190aXRsZT1yJyRcXGNoaV4yX3tcXHRleHR7Y2FsY319JCcsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxNCwgcC4gNDEwIn0sIHsiZW51bmNpYWRvIjogIlVtYSByZWRlIGRlIHZhcmVqbyBkZXNlamEgYXZhbGlhciBzZSBhIHByZWZlcsOqbmNpYSBkb3MgY2xpZW50ZXMgcG9yIHRyw6pzIHRpcG9zIGRlIGZvcm1hcyBkZSBwYWdhbWVudG8gKENhcnTDo28gZGUgQ3LDqWRpdG8sIETDqWJpdG8sIERpbmhlaXJvKSDDqSBpbmRlcGVuZGVudGUgZGEgcmVnacOjbyBnZW9ncsOhZmljYSBkZSBzdWFzIGxvamFzIChOb3J0ZSwgU3VsKS4gRW0gdW1hIGFtb3N0cmEgYWxlYXTDs3JpYSBkZSA1MDAgdHJhbnNhw6fDtWVzLCBmb3JhbSByZWdpc3RyYWRhcyBhcyBmcmVxdcOqbmNpYXMgb2JzZXJ2YWRhcy4gU29iIGEgaGlww7N0ZXNlIG51bGEgJEhfMCQgZGUgaW5kZXBlbmTDqm5jaWEsIG8gY8OhbGN1bG8gZGFzIGZyZXF1w6puY2lhcyBlc3BlcmFkYXMgJEVfe2lqfSQgw6kgcmVhbGl6YWRvIHBhcmEgY2FkYSBjw6lsdWxhIGRhIHRhYmVsYSBkZSBjb250aW5nw6puY2lhLiBRdWFsIGRhcyBzZWd1aW50ZXMgYWZpcm1hw6fDtWVzIG1lbGhvciBkZXNjcmV2ZSBhIGludHVpw6fDo28gcG9yIHRyw6FzIGRvIHRlcm1vICRcXGZyYWN7KE9fe2lqfSAtIEVfe2lqfSleMn17RV97aWp9fSQgbmEgZXN0YXTDrXN0aWNhICRcXGNoaV4yX3tcXHRleHR7Y2FsY319JD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkVsZSBtZWRlIG8gZGVzdmlvIGFic29sdXRvIGRhcyBmcmVxdcOqbmNpYXMsIHBvbmRlcmFuZG8gbyBlcnJvIHBlbGEgbcOpZGlhIGFyaXRtw6l0aWNhIGdsb2JhbCBkZSB0cmFuc2HDp8O1ZXMgcG9yIGNhdGVnb3JpYS4iLCAiQiI6ICJFbGUgcXVhbnRpZmljYSBhIHZhcmnDom5jaWEgYW1vc3RyYWwgdG90YWwgZGFzIHByZWZlcsOqbmNpYXMgZG9zIGNvbnN1bWlkb3JlcyBkZW50cm8gZGUgY2FkYSByZWdpw6NvLCBpZ25vcmFuZG8gYXMgZnJlcXXDqm5jaWFzIGVzcGVyYWRhcy4iLCAiQyI6ICJFbGUgcmVwcmVzZW50YSBvIHF1YWRyYWRvIGRvIGRlc3ZpbyByZWxhdGl2byBkZSBjYWRhIGPDqWx1bGEsIG5vcm1hbGl6YW5kbyBhIGRpc2NyZXDDom5jaWEgcGVsYSBmcmVxdcOqbmNpYSBlc3BlcmFkYSBwYXJhIGdhcmFudGlyIHF1ZSBjw6lsdWxhcyBjb20gcG91Y2FzIG9ic2VydmHDp8O1ZXMgdGVuaGFtIGltcGFjdG8gcHJvcG9yY2lvbmFsIG5vIHRlc3RlLiIsICJEIjogIkVsZSBjYWxjdWxhIGEgcHJvYmFiaWxpZGFkZSBleGF0YSBkZSBvY29ycsOqbmNpYSBkZSBjYWRhIGPDqWx1bGEgc29iIGEgaGlww7N0ZXNlIGRlIHF1ZSBhcyBmcmVxdcOqbmNpYXMgb2JzZXJ2YWRhcyBzw6NvIGlkZW50aWNhbWVudGUgZGlzdHJpYnXDrWRhcyDDoHMgZXNwZXJhZGFzLiIsICJFIjogIkVsZSBkZWZpbmUgYSBjb3JyZWxhw6fDo28gbGluZWFyIGVudHJlIGFzIHZhcmnDoXZlaXMgY2F0ZWfDs3JpY2FzLCBpbmRpY2FuZG8gYSBmb3LDp2EgZGEgYXNzb2NpYcOnw6NvIHNlbSBuZWNlc3NpZGFkZSBkZSBub3JtYWxpemHDp8OjbyBwZWxvcyB2YWxvcmVzIGVzcGVyYWRvcy4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIkxlbWJyZS1zZSBkZSBxdWUgYSBlc3RhdMOtc3RpY2EgZGUgUGVhcnNvbiBzZXJ2ZSBwYXJhIG1lZGlyICdzdXJwcmVzYScuIFBvciBxdWUgZGl2aWRpciBwZWxvIHZhbG9yIGVzcGVyYWRvICRFX3tpan0kPyIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBlc3RhdMOtc3RpY2EgJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0gPSBcXHN1bSBcXHN1bSBcXGZyYWN7KE9fe2lqfSAtIEVfe2lqfSleMn17RV97aWp9fSQgZm9pIGRlc2VuaGFkYSBwYXJhIG1lZGlyIGEgZGlzdMOibmNpYSBlbnRyZSBvIHF1ZSBvYnNlcnZhbW9zICgkT197aWp9JCkgZSBvIHF1ZSBzZXJpYSBlc3BlcmFkbyBzb2IgaW5kZXBlbmTDqm5jaWEgKCRFX3tpan0kKS4gQSBub3JtYWxpemHDp8OjbyBwZWxhIGRpdmlzw6NvIHBvciAkRV97aWp9JCDDqSBmdW5kYW1lbnRhbDogZGVzdmlvcyBlbSBjw6lsdWxhcyBjb20gcG91Y2FzIG9jb3Jyw6puY2lhcyBlc3BlcmFkYXMgdGVyaWFtIHVtIGltcGFjdG8gYXJ0aWZpY2lhbG1lbnRlIGJhaXhvIHNlIG7Do28gZm9zc2VtIHBvbmRlcmFkb3MsIGUgZGVzdmlvcyBlbSBjw6lsdWxhcyBjb20gbXVpdGFzIG9jb3Jyw6puY2lhcyB0ZXJpYW0gdW0gaW1wYWN0byBkZXNwcm9wb3JjaW9uYWwuIEFzc2ltLCBhIGRpdmlzw6NvIGFqdXN0YSBvIHBlc28gZGUgY2FkYSBkZXN2aW8sIHBlcm1pdGluZG8gdW1hIG3DqXRyaWNhIGRlICdzdXJwcmVzYScgY29tcGFyw6F2ZWwgZW50cmUgZGlmZXJlbnRlcyBlc2NhbGFzIGRlIGZyZXF1w6puY2lhLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgNCwgcC4gNzgifSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gdGVzdGUgZGUgaW5kZXBlbmTDqm5jaWEgZW0gdW1hIHRhYmVsYSBkZSBjb250aW5nw6puY2lhIGNvbSAkcj0zJCBsaW5oYXMgZSAkcz00JCBjb2x1bmFzLiBTZSBhIGVzdGF0w61zdGljYSBjYWxjdWxhZGEgZm9yICRcXGNoaV4yX3tcXHRleHR7Y2FsY319ID0gMTUuMjAkIGUgbyB2YWxvciBjcsOtdGljbyBwYXJhICRcXGFscGhhID0gMC4wNSQgZm9yICRcXGNoaV4yX3tcXHRleHR7Y3JpdH19ID0gMTIuNTkkLCBxdWFsIMOpIGEgY29uY2x1c8OjbyBlc3RhdMOtc3RpY2EgY29ycmV0YSBzb2JyZSBhIHJlbGHDp8OjbyBlbnRyZSBhcyB2YXJpw6F2ZWlzPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTsOjbyBow6EgZXZpZMOqbmNpYXMgc3VmaWNpZW50ZXMgcGFyYSByZWplaXRhciAkSF8wJCwgcG9ydGFudG8sIGFzIHZhcmnDoXZlaXMgc8OjbyBpbmRlcGVuZGVudGVzIGFvIG7DrXZlbCBkZSA1JS4iLCAiQiI6ICJBIGhpcMOzdGVzZSBudWxhIGRlIGluZGVwZW5kw6puY2lhIMOpIHJlamVpdGFkYSwgaW5kaWNhbmRvIGV2aWTDqm5jaWFzIGRlIGFzc29jaWHDp8OjbyBlbnRyZSBhcyB2YXJpw6F2ZWlzIGFvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBkZSA1JS4iLCAiQyI6ICJPIG7Dum1lcm8gZGUgZ3JhdXMgZGUgbGliZXJkYWRlIMOpIDEyLCBvIHF1ZSBpbnZhbGlkYSBvIHRlc3RlIHBhcmEgdW1hIGFtb3N0cmEgbWVub3IgcXVlIDMwIG9ic2VydmHDp8O1ZXMuIiwgIkQiOiAiTyB2YWxvciBkZSAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSQgw6kgbXVpdG8gcHLDs3hpbW8gZGUgemVybywgc3VnZXJpbmRvIHVtYSBkZXBlbmTDqm5jaWEgcGVyZmVpdGEgZW50cmUgYXMgdmFyacOhdmVpcy4iLCAiRSI6ICJBIGNvbmNsdXPDo28gZGVwZW5kZSBkYSBzb21hIHRvdGFsIGRlIGZyZXF1w6puY2lhcywgcXVlIGRldmUgc2VyIG9icmlnYXRvcmlhbWVudGUgc3VwZXJpb3IgYSAxMDAwIHBhcmEgcXVlIG8gdGVzdGUgc2VqYSByb2J1c3RvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiQ29tcGFyZSBvIHZhbG9yIGNhbGN1bGFkbyBjb20gYSByZWdpw6NvIGNyw610aWNhIGRlZmluaWRhIHBlbG8gdmFsb3IgY3LDrXRpY28uIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIHVtIHRlc3RlIGRlIGluZGVwZW5kw6puY2lhIGNvbSAkcj0zJCBlICRzPTQkLCBvcyBncmF1cyBkZSBsaWJlcmRhZGUgc8OjbyAkZ2wgPSAoci0xKShzLTEpID0gKDIpKDMpID0gNiQuIENvbW8gbyB2YWxvciBjYWxjdWxhZG8gJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0gPSAxNS4yMCQgw6kgc3VwZXJpb3IgYW8gdmFsb3IgY3LDrXRpY28gJFxcY2hpXjJfe1xcdGV4dHtjcml0fX0gPSAxMi41OSQgKHF1ZSBkZWxpbWl0YSBhIHJlZ2nDo28gZGUgcmVqZWnDp8OjbyBwYXJhICRcXGFscGhhPTAuMDUkKSwgbyB2YWxvciBjYWkgbmEgcmVnacOjbyBjcsOtdGljYS4gUG9ydGFudG8sIHJlamVpdGFtb3MgYSBoaXDDs3Rlc2UgbnVsYSAkSF8wJCBkZSBpbmRlcGVuZMOqbmNpYSwgY29uY2x1aW5kbyBxdWUgZXhpc3RlIHVtYSBhc3NvY2lhw6fDo28gZXN0YXRpc3RpY2FtZW50ZSBzaWduaWZpY2F0aXZhIGVudHJlIGFzIHZhcmnDoXZlaXMuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgwLCAyMCwgMjAwKVxueSA9IHN0YXRzLlxcY2hpMi5wZGYoeCwgZGY9NilcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbmFtZT0nRGlzdHJpYnVpw6fDo28gJFxcY2hpXjIoNikkJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJywgd2lkdGg9MikpKVxuZmlnLmFkZF92bGluZSh4PTEyLjU5MiwgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJywgZGFzaD0nZGFzaCcpLCBhbm5vdGF0aW9uX3RleHQ9JyRcXGNoaV4yX3tcXHRleHR7Y3JpdH19JCcpXG5maWcuYWRkX3ZsaW5lKHg9MTUuMjAsIGxpbmU9ZGljdChjb2xvcj0nI0Y1OUUwQicsIHdpZHRoPTMpLCBhbm5vdGF0aW9uX3RleHQ9JyRcXGNoaV4yX3tcXHRleHR7Y2FsY319JCcpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nRGlzdHJpYnVpw6fDo28gZGUgUXVpLVF1YWRyYWRvICgkZ2w9NiQpJywgeGF4aXNfdGl0bGU9JyRcXGNoaV4yJCcsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDE0LCBwLiA0MTAifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIGVyZ29ub21pYSwgb2JzZXJ2b3Utc2UgYSByZWxhw6fDo28gZW50cmUgYSBwb3N0dXJhIGRvIHRyYWJhbGhhZG9yIChFcmdvbsO0bWljYSB2cy4gSW5hZGVxdWFkYSkgZSBhIG9jb3Jyw6puY2lhIGRlIGRvcmVzIGxvbWJhcmVzIChQcmVzZW50ZSB2cy4gQXVzZW50ZSkuIENvbSB1bWEgYW1vc3RyYSBkZSAkbiA9IDIwMCQgZnVuY2lvbsOhcmlvcywgZGVzZWphLXNlIHRlc3RhciBzZSBhIHBvc3R1cmEgZSBhIGRvciBsb21iYXIgc8OjbyBpbmRlcGVuZGVudGVzIGFvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSA9IDAsMDUkLiBBIHRhYmVsYSBkZSBjb250aW5nw6puY2lhIHJlc3VsdGFudGUgZ2Vyb3UgdW1hIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSA9IDQsODUkLiBTYWJlbmRvIHF1ZSBwYXJhICRnbCA9IDEkIG8gdmFsb3IgY3LDrXRpY28gw6kgJFxcY2hpXjJfe1xcdGV4dHtjcml0fX0oMCwwNTsgMSkgPSAzLDg0JCwgcXVhbCBkZXZlIHNlciBhIGRlY2lzw6NvIGVzdGF0w61zdGljYSBlIHN1YSBqdXN0aWZpY2F0aXZhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiUmVqZWl0YS1zZSAkSF8wJCwgcG9pcyAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSA8IFxcY2hpXjJfe1xcdGV4dHtjcml0fX0kLCBpbmRpY2FuZG8gaW5kZXBlbmTDqm5jaWEgZW50cmUgb3MgZmF0b3Jlcy4iLCAiQiI6ICJOw6NvIHNlIHJlamVpdGEgJEhfMCQsIHBvaXMgYSBlc3RhdMOtc3RpY2EgZGUgdGVzdGUgbsOjbyB1bHRyYXBhc3NvdSBvIGxpbWlhciBkZSBzaWduaWZpY8OibmNpYSBkZWZpbmlkbyBwZWxhIHJlZ2nDo28gY3LDrXRpY2EuIiwgIkMiOiAiUmVqZWl0YS1zZSAkSF8wJCwgcG9pcyAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSA+IFxcY2hpXjJfe1xcdGV4dHtjcml0fX0kLCBzdWdlcmluZG8gZXZpZMOqbmNpYSBlc3RhdMOtc3RpY2EgZGUgYXNzb2NpYcOnw6NvIGVudHJlIHBvc3R1cmEgZSBkb3IgbG9tYmFyLiIsICJEIjogIk7Do28gc2UgcmVqZWl0YSAkSF8wJCwgcG9pcyBvIHRhbWFuaG8gYW1vc3RyYWwgJG49MjAwJCDDqSBpbnN1ZmljaWVudGUgcGFyYSByZWFsaXphciB0ZXN0ZXMgZGUgYXNzb2NpYcOnw6NvIHZpYSAkXFxjaGleMiQuIiwgIkUiOiAiTyB0ZXN0ZSDDqSBpbmNvbmNsdXNpdm8sIHBvaXMgbyAkcFxcdGV4dHstdmFsb3J9JCDDqSBleGF0YW1lbnRlIGlndWFsIGEgJFxcYWxwaGEgPSAwLDA1JC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSByZWdyYSBkZSBkZWNpc8OjbzogYSByZWdpw6NvIGNyw610aWNhICRSQyQgcGFyYSBvIHRlc3RlIHF1aS1xdWFkcmFkbyDDqSBjb21wb3N0YSBwZWxvcyB2YWxvcmVzIHF1ZSBzdXBlcmFtIG8gdmFsb3IgY3LDrXRpY28gdGFiZWxhZG8uIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIHVtIHRlc3RlIGRlIGluZGVwZW5kw6puY2lhIHF1aS1xdWFkcmFkbywgZGVmaW5pbW9zICRIXzAkIGNvbW8gYSBoaXDDs3Rlc2UgZGUgaW5kZXBlbmTDqm5jaWEgZW50cmUgYXMgdmFyacOhdmVpcy4gQSByZWdpw6NvIGNyw610aWNhIMOpIGRlZmluaWRhIGNvbW8gJFJDID0gXFx7IFxcY2hpXjIgOiBcXGNoaV4yID4gXFxjaGleMl97XFx0ZXh0e2NyaXR9fSBcXH0kLiBDb21vICRcXGNoaV4yX3tcXHRleHR7Y2FsY319ID0gNCw4NSQgZSAkXFxjaGleMl97XFx0ZXh0e2NyaXR9fSA9IDMsODQkLCB0ZW1vcyAkNCw4NSA+IDMsODQkLCBvIHF1ZSBzaWduaWZpY2EgcXVlIG8gdmFsb3IgY2FsY3VsYWRvIGNhaSBkZW50cm8gZGEgcmVnacOjbyBkZSByZWplacOnw6NvLiBQb3J0YW50bywgcmVqZWl0YW1vcyBhIGhpcMOzdGVzZSBudWxhICRIXzAkIGVtIGZhdm9yIGRhIGV4aXN0w6puY2lhIGRlIHVtYSBhc3NvY2lhw6fDo28gZW50cmUgYSBwb3N0dXJhIGVyZ29uw7RtaWNhIGUgYSBwcmVzZW7Dp2EgZGUgZG9yZXMgbG9tYmFyZXMuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgwLCAxMCwgMTAwKVxueSA9IHN0YXRzLlxcY2hpMi5wZGYoeCwgZGY9MSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbmFtZT0nRGVuc2lkYWRlICRcXGNoaV4yKDEpJCcsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTIpKSlcbnhfZmlsbCA9IG5wLmxpbnNwYWNlKDMuODQsIDEwLCAxMDApXG55X2ZpbGwgPSBzdGF0cy5cXGNoaTIucGRmKHhfZmlsbCwgZGY9MSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PW5wLmNvbmNhdGVuYXRlKChbMy44NF0sIHhfZmlsbCwgWzEwXSkpLCB5PW5wLmNvbmNhdGVuYXRlKChbMF0sIHlfZmlsbCwgWzBdKSksIGZpbGw9J3RvemVyb3knLCBuYW1lPSdSZWdpw6NvIENyw610aWNhIChSQyknLCBsaW5lPWRpY3QoY29sb3I9JyM5OTFCMUInKSwgZmlsbGNvbG9yPScjOTkxQjFCJykpXG5maWcuYWRkX3ZsaW5lKHg9NC44NSwgbGluZV9kYXNoPSdkYXNoJywgbGluZV9jb2xvcj0nIzFFMjkzQicsIGFubm90YXRpb25fdGV4dD0nJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX09NC44NSQnKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkRpc3RyaWJ1acOnw6NvICRcXGNoaV4yJCBjb20gJGdsPTEkPC9iPicsIHhheGlzX3RpdGxlPXInJFxcY2hpXjIkJywgeWF4aXNfdGl0bGU9cidEZW5zaWRhZGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkFvIGF2YWxpYXIgYSBlZmljw6FjaWEgZGUgdW0gbm92byBsYXlvdXQgZGUgc2l0ZSwgY29tcGFyb3Utc2UgYSB0YXhhIGRlIGNsaXF1ZXMgZGUgZG9pcyBncnVwb3MgKEdydXBvIEEgZSBHcnVwbyBCKSBlbSB1bWEgdGFiZWxhIGRlIGNvbnRpbmfDqm5jaWEgJDIgXFx0aW1lcyAyJC4gTyB0ZXN0ZSBkZSBpbmRlcGVuZMOqbmNpYSByZXN1bHRvdSBlbSB1bSAkcFxcdGV4dHstdmFsb3J9ID0gMCwwMjUkLiBDb25zaWRlcmFuZG8gdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGRlICRcXGFscGhhID0gMCwwNSQsIHF1YWwgZGFzIGFmaXJtYcOnw7VlcyBhYmFpeG8gbWVsaG9yIGludGVycHJldGEgbyByZXN1bHRhZG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIHByb2JhYmlsaWRhZGUgZGUgJEhfMCQgc2VyIHZlcmRhZGVpcmEgw6kgZGUgMiw1JS4iLCAiQiI6ICJDb21vICRwXFx0ZXh0ey12YWxvcn0gPCBcXGFscGhhJCwgb3MgZGFkb3MgZm9ybmVjZW0gZXZpZMOqbmNpYSBzdWZpY2llbnRlIHBhcmEgcmVqZWl0YXIgYSBoaXDDs3Rlc2UgZGUgaW5kZXBlbmTDqm5jaWEgZW50cmUgbyBsYXlvdXQgZSBhIHRheGEgZGUgY2xpcXVlcy4iLCAiQyI6ICJPIHZhbG9yICQwLDAyNSQgcmVwcmVzZW50YSBhIHByb2JhYmlsaWRhZGUgZGUgY29tZXRlciBvIGVycm8gdGlwbyBJSS4iLCAiRCI6ICJPIHRlc3RlIGZhbGhvdSBlbSBkZXRlY3RhciB1bWEgYXNzb2NpYcOnw6NvLCBwb2lzIG8gJHBcXHRleHR7LXZhbG9yfSQgw6kgbXVpdG8gYmFpeG8uIiwgIkUiOiAiQSBhc3NvY2lhw6fDo28gb2JzZXJ2YWRhIGVudHJlIG8gZ3J1cG8gZSBhIHRheGEgZGUgY2xpcXVlcyDDqSBwdXJhbWVudGUgZGV2aWRhIGFvIGFjYXNvIGFtb3N0cmFsLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTyAkcFxcdGV4dHstdmFsb3J9JCDDqSBhIHByb2JhYmlsaWRhZGUgZGUgb2J0ZXIgcmVzdWx0YWRvcyB0w6NvIG91IG1haXMgZXh0cmVtb3Mgc29iIGEgdmlnw6puY2lhIGRhIGhpcMOzdGVzZSBudWxhLiBDb21wYXJlIGVzdGUgdmFsb3IgY29tIG8gbGltaWFyICRcXGFscGhhJC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIk8gJHBcXHRleHR7LXZhbG9yfSQgbWVkZSBhIHByb2JhYmlsaWRhZGUgZGUgb2JzZXJ2YXIgdW1hIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSBwZWxvIG1lbm9zIHTDo28gZXh0cmVtYSBxdWFudG8gYSBvYnRpZGEsIGFzc3VtaW5kbyBxdWUgYSBoaXDDs3Rlc2UgbnVsYSAoJEhfMCQpIMOpIHZlcmRhZGVpcmEuIFF1YW5kbyAkcFxcdGV4dHstdmFsb3J9IFxcbGVxIFxcYWxwaGEkLCBhIGV2aWTDqm5jaWEgY29udHJhICRIXzAkIMOpIGZvcnRlIG8gc3VmaWNpZW50ZSBwYXJhIHJlamVpdMOhLWxhLiBObyBjYXNvLCAkMCwwMjUgPCAwLDA1JCwgY29uZmlybWFuZG8gcXVlIGEgYXNzb2NpYcOnw6NvIGVudHJlIG8gbGF5b3V0IGUgbyBjb21wb3J0YW1lbnRvIGRlIGNsaXF1ZXMgw6kgZXN0YXRpc3RpY2FtZW50ZSBzaWduaWZpY2FudGUuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbWEgZW1wcmVzYSBkZSBjb25zdWx0b3JpYSByZWFsaXpvdSB1bSBlc3R1ZG8gZGUgbWVyY2FkbyBwYXJhIGF2YWxpYXIgYSBhc3NvY2lhw6fDo28gZW50cmUgbyBuw612ZWwgZGUgZXNjb2xhcmlkYWRlIChFbnNpbm8gRnVuZGFtZW50YWwsIEVuc2lubyBNw6lkaW8sIEVuc2lubyBTdXBlcmlvcikgZSBvIGludGVyZXNzZSBlbSB1bSBub3ZvIHNlcnZpw6dvIGRpZ2l0YWwgZGUgYXNzaW5hdHVyYSAoQmFpeG8sIE3DqWRpbywgQWx0bykuIENvbSBiYXNlIGVtIHVtYSBhbW9zdHJhIGRlICRuID0gNTAwJCBjb25zdW1pZG9yZXMsIG8gdGVzdGUgcXVpLXF1YWRyYWRvIGRlIFBlYXJzb24gcmVzdWx0b3UgZW0gdW1hIGVzdGF0w61zdGljYSAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSA9IDQ1JC4gQ29uc2lkZXJhbmRvIHVtYSB0YWJlbGEgZGUgY29udGluZ8OqbmNpYSBkZSAkMyBcXHRpbWVzIDMkLCBxdWFsIMOpIGEgaW50ZXJwcmV0YcOnw6NvIGNvcnJldGEgdXRpbGl6YW5kbyBvIENvZWZpY2llbnRlIGRlIENvbnRpbmfDqm5jaWEgZGUgUGVhcnNvbiAoJEMkKSBwYXJhIG1lZGlyIGEgaW50ZW5zaWRhZGUgZGVzdGEgYXNzb2NpYcOnw6NvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyBjb2VmaWNpZW50ZSAkQyQgw6kgYXByb3hpbWFkYW1lbnRlICQwLDI4NyQsIGluZGljYW5kbyB1bWEgYXNzb2NpYcOnw6NvIG1vZGVyYWRhLiIsICJCIjogIk8gdmFsb3IgZGUgJEMkIMOpICQwLDA4MjUkLCBvIHF1ZSBjb21wcm92YSBxdWUgYXMgdmFyacOhdmVpcyBzw6NvIGluZGVwZW5kZW50ZXMuIiwgIkMiOiAiTyBjb2VmaWNpZW50ZSAkQyQgcmVzdWx0YSBlbSAkMCw0NSQsIGluZGljYW5kbyB1bWEgYXNzb2NpYcOnw6NvIHBlcmZlaXRhIGVudHJlIGFzIHZhcmnDoXZlaXMuIiwgIkQiOiAiTyB2YWxvciBkZSAkQyQgw6kgJDAsMjEkLCBvIHF1ZSBkZW1vbnN0cmEgcXVlIGEgYW1vc3RyYSDDqSBpbnN1ZmljaWVudGUgcGFyYSBvIHRlc3RlLiIsICJFIjogIk8gY29lZmljaWVudGUgJEMkIG7Do28gcG9kZSBzZXIgY2FsY3VsYWRvLCBwb2lzICRuJCBkZXZlIHNlciBuZWNlc3NhcmlhbWVudGUgc3VwZXJpb3IgYSAxMDAwLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGbDs3JtdWxhICRDID0gXFxzcXJ0e1xcZnJhY3tcXGNoaV4yX3tcXHRleHR7Y2FsY319fXtcXGNoaV4yX3tcXHRleHR7Y2FsY319ICsgbn19JC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgZsOzcm11bGEgZG8gY29lZmljaWVudGUgZGUgY29udGluZ8OqbmNpYSDDqSAkQyA9IFxcc3FydHtcXGZyYWN7XFxjaGleMl97XFx0ZXh0e2NhbGN9fX17XFxjaGleMl97XFx0ZXh0e2NhbGN9fSArIG59fSQuIFN1YnN0aXR1aW5kbyBvcyB2YWxvcmVzIGRhZG9zOiAkQyA9IFxcc3FydHtcXGZyYWN7NDV9ezQ1ICsgNTAwfX0gPSBcXHNxcnR7XFxmcmFjezQ1fXs1NDV9fSBcXGFwcHJveCBcXHNxcnR7MCwwODI1N30gXFxhcHByb3ggMCwyODckLiBFc3RlIHZhbG9yLCBlc3RhbmRvIGRpc3RhbnRlIGRlIHplcm8sIGFwb250YSBwYXJhIHVtYSBhc3NvY2lhw6fDo28gcmVsZXZhbnRlLCBzZW5kbyBjb211bSBpbnRlcnByZXRhciB2YWxvcmVzIHByw7N4aW1vcyBhIDAsMyBjb21vIGluZGljYXRpdm9zIGRlIGludGVuc2lkYWRlIG1vZGVyYWRhIHBhcmEgZXN0ZSB0aXBvIGRlIG3DqXRyaWNhLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgNCwgcC4gNzkifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSwgZGVzZWphLXNlIGNvbXBhcmFyIHNlIGEgcHJvcG9yw6fDo28gZGUgcHJvZHV0b3MgZGVmZWl0dW9zb3Mgw6kgYSBtZXNtYSBlbSB0csOqcyBkaWZlcmVudGVzIGxpbmhhcyBkZSBwcm9kdcOnw6NvICgkUF8xLCBQXzIsIFBfMyQpLiBGb3JhbSBjb2xldGFkYXMgYW1vc3RyYXMgaW5kZXBlbmRlbnRlcyBkZSBjYWRhIGxpbmhhIGUgY2xhc3NpZmljYWRvcyBvcyBwcm9kdXRvcyBlbSAnQ29uZm9ybWUnIGUgJ07Do28tY29uZm9ybWUnLiBTb2JyZSBvIHRlc3RlIGVzdGF0w61zdGljbyBhIHNlciBhcGxpY2FkbywgYXNzaW5hbGUgYSBhbHRlcm5hdGl2YSBjb3JyZXRhOiIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiRGV2ZS1zZSB1dGlsaXphciBvIHRlc3RlIGRlIGluZGVwZW5kw6puY2lhLCB0ZXN0YW5kbyBzZSBhIGxpbmhhIGRlIHByb2R1w6fDo28gZXN0w6EgYXNzb2NpYWRhIMOgIHF1YWxpZGFkZSBkbyBwcm9kdXRvLCBvIHF1ZSDDqSBjb25jZWl0dWFsbWVudGUgZXF1aXZhbGVudGUgYW8gdGVzdGUgZGUgaG9tb2dlbmVpZGFkZSAkSF8wOiBQXzEgPSBQXzIgPSBQXzMkLiIsICJCIjogIk8gdGVzdGUgZGUgaG9tb2dlbmVpZGFkZSByZXF1ZXIgcXVlIGFzIHBvcHVsYcOnw7VlcyBzZWphbSBkZXBlbmRlbnRlcyBlbnRyZSBzaSBwYXJhIHF1ZSBhIGVzdGF0w61zdGljYSAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSQgc2VqYSB2w6FsaWRhLiIsICJDIjogIkEgaGlww7N0ZXNlIGRlIGhvbW9nZW5laWRhZGUgcG9zdHVsYSBxdWUgYXMgdmFyacOibmNpYXMgcG9wdWxhY2lvbmFpcyBkZXZlbSBzZXIgaWd1YWlzLCBpbmRlcGVuZGVudGVtZW50ZSBkYXMgcHJvcG9yw6fDtWVzIGRlIGRlZmVpdG9zLiIsICJEIjogIk8gdGVzdGUgZGUgaG9tb2dlbmVpZGFkZSBzw7Mgw6kgYXBsaWPDoXZlbCBzZSBvIHRhbWFuaG8gZGEgYW1vc3RyYSAkbiQgZm9yIGlkw6pudGljbyBwYXJhIGFzIHRyw6pzIGxpbmhhcyBkZSBwcm9kdcOnw6NvLiIsICJFIjogIkEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlIHBhcmEgaG9tb2dlbmVpZGFkZSBuw6NvIHV0aWxpemEgYSBkaXN0cmlidWnDp8OjbyAkXFxjaGleMiQsIG1hcyBcXHNpbSBhIGRpc3RyaWJ1acOnw6NvICRGJCBkZSBTbmVkZWNvciBkZXZpZG8gw6AgY29tcGFyYcOnw6NvIGRlIHZhcmnDom5jaWFzLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiUmVmbGl0YSBzb2JyZSBhIGRpZmVyZW7Dp2EgZW50cmUgdGVzdGFyIGFzc29jaWHDp8OjbyBlbSB1bWEgw7puaWNhIHBvcHVsYcOnw6NvIChpbmRlcGVuZMOqbmNpYSkgZSBjb21wYXJhciBhIGRpc3RyaWJ1acOnw6NvIGVudHJlIHbDoXJpYXMgcG9wdWxhw6fDtWVzIChob21vZ2VuZWlkYWRlKS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIk8gdGVzdGUgZGUgaG9tb2dlbmVpZGFkZSAoJEhfMDogUF8xID0gUF8yID0gXFxkb3RzID0gUF9yJCkgdmVyaWZpY2Egc2UgYSBkaXN0cmlidWnDp8OjbyBkZSB1bWEgdmFyacOhdmVsIGNhdGVnw7NyaWNhIChxdWFsaWRhZGUpIMOpIGEgbWVzbWEgZW0gZGlmZXJlbnRlcyBwb3B1bGHDp8O1ZXMgKGxpbmhhcyBkZSBwcm9kdcOnw6NvKS4gTWF0ZW1hdGljYW1lbnRlLCBhIGVzdHJ1dHVyYSBkbyB0ZXN0ZSBkZSBob21vZ2VuZWlkYWRlIGVtIHRhYmVsYXMgZGUgY29udGluZ8OqbmNpYSBjb21wYXJ0aWxoYSBhIG1lc21hIGVzdGF0w61zdGljYSBkZSBQZWFyc29uICRcXGNoaV4yX3tcXHRleHR7Y2FsY319ID0gXFxzdW0gXFxmcmFjeyhPIC0gRSleMn17RX0kIGUgb3MgbWVzbW9zIGdyYXVzIGRlIGxpYmVyZGFkZSAkKHItMSkocy0xKSQgcXVlIG8gdGVzdGUgZGUgaW5kZXBlbmTDqm5jaWEsIHNlbmRvIGNvbmNlaXR1YWxtZW50ZSBpbnRlcmNhbWJpw6F2ZWlzIG5hIGZvcm1hIGRlIGPDoWxjdWxvLCBlbWJvcmEgY29tIGludGVycHJldGHDp8O1ZXMgcG9wdWxhY2lvbmFpcyBkaXN0aW50YXMuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9XSwgInF1ZXN0b2VzX2Rpc2N1cnNpdmFzIjogW3siZW51bmNpYWRvIjogIlVtYSBpbmTDunN0cmlhIGZhcm1hY8OqdXRpY2EgdGVzdG91IGEgZWZpY8OhY2lhIGRlIGR1YXMgZHJvZ2FzIChBIGUgQikgZW0gMjAwIHBhY2llbnRlcy4gT3MgcmVzdWx0YWRvcyBmb3JhbTogRHJvZ2EgQSAoNjAgZWZpY2F6ZXMsIDQwIG7Do28gZWZpY2F6ZXMpLCBEcm9nYSBCICg0MCBlZmljYXplcywgNjAgbsOjbyBlZmljYXplcykuIFRlc3RlIGEgaGlww7N0ZXNlIGRlIGluZGVwZW5kw6puY2lhIGVudHJlIG8gdGlwbyBkZSBkcm9nYSBlIGEgZWZpY8OhY2lhIGFvIG7DrXZlbCAkXFxhbHBoYSA9IDAuMDUkLiBBcHJlc2VudGUgbyBjw6FsY3VsbyBkYSBlc3RhdMOtc3RpY2EgJFxcY2hpXjJfe1x0ZXh0e2NhbGN9fSQsIG8gdmFsb3IgZGUgJGdsJCBlIGEgY29uY2x1c8OjbyBkbyB0ZXN0ZS4iLCAiZGljYSI6ICJNb250ZSBhIHRhYmVsYSBkZSBjb250aW5nw6puY2lhLCBjYWxjdWxlIGFzIGZyZXF1w6puY2lhcyBlc3BlcmFkYXMgJEVfe2lqfSQgYXNzdW1pbmRvICRIXzAkIHZlcmRhZGVpcmEsIGUgYXBsaXF1ZSBhIGbDs3JtdWxhICRcXGNoaV4yX3tcdGV4dHtjYWxjfX0gPSBcXHN1bSBcXGZyYWN7KE9fe2lqfSAtIEVfe2lqfSleMn17RV97aWp9fSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIFRhYmVsYSBPYnNlcnZhZGEgKCRPX3tpan0kKTogRHJvZ2EgQSAoRWZpY2F6PTYwLCBOw6NvPTQwKSwgRHJvZ2EgQiAoRWZpY2F6PTQwLCBOw6NvPTYwKS4gVG90YWlzOiBMaW5oYSBBPTEwMCwgTGluaGEgQj0xMDAsIENvbHVuYSBFZmljYXo9MTAwLCBDb2x1bmEgTsOjbz0xMDAsIFRvdGFsICRuPTIwMCQuIiwgIjIuIEZyZXF1w6puY2lhcyBFc3BlcmFkYXMgKCRFX3tpan0kKTogQ29tbyB0b2RvcyBvcyB0b3RhaXMgbWFyZ2luYWlzIHPDo28gaWd1YWlzIGEgMTAwIGUgJG49MjAwJCwgJEVfe2lqfSA9ICgxMDAgXFxjZG90IDEwMCkgLyAyMDAgPSA1MCQgcGFyYSB0b2RhcyBhcyBxdWF0cm8gY8OpbHVsYXMuIiwgIjMuIEPDoWxjdWxvIGRhIEVzdGF0w61zdGljYTogJFxcY2hpXjJfe1x0ZXh0e2NhbGN9fSA9IFxcZnJhY3soNjAtNTApXjJ9ezUwfSArIFxcZnJhY3soNDAtNTApXjJ9ezUwfSArIFxcZnJhY3soNDAtNTApXjJ9ezUwfSArIFxcZnJhY3soNjAtNTApXjJ9ezUwfSA9IFxcZnJhY3sxMDB9ezUwfSArIFxcZnJhY3sxMDB9ezUwfSArIFxcZnJhY3sxMDB9ezUwfSArIFxcZnJhY3sxMDB9ezUwfSA9IDIgKyAyICsgMiArIDIgPSA4LjAkLiIsICI0LiBHcmF1cyBkZSBMaWJlcmRhZGU6ICRnbCA9ICgyLTEpKDItMSkgPSAxJC4iLCAiNS4gQ29uY2x1c8OjbzogUGFyYSAkXFxhbHBoYT0wLjA1JCBlICRnbD0xJCwgbyB2YWxvciBjcsOtdGljbyAkXFxjaGleMl97XHRleHR7Y3JpdH19ID0gMy44NDEkLiBDb21vICQ4LjAgPiAzLjg0MSQsIHJlamVpdGFtb3MgJEhfMCQsIGluZGljYW5kbyBkZXBlbmTDqm5jaWEgZW50cmUgZHJvZ2EgZSBlZmljw6FjaWEuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTQsIHAuIDQwOC00MTAiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiA4LjB9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgbMOzZ2ljYSBkYSBoaXDDs3Rlc2UgZGUgaW5kZXBlbmTDqm5jaWEsIG8gcXVlIHNpZ25pZmljYSB1bSB2YWxvciBvYnNlcnZhZG8gZGEgZXN0YXTDrXN0aWNhICRcXGNoaV4yX3tcdGV4dHtjYWxjfX0kIHByw7N4aW1vIGRlIHplcm8gdmVyc3VzIHVtIHZhbG9yIG11aXRvIGdyYW5kZS4gQ29tbyBpc3NvIHNlIHJlbGFjaW9uYSBjb20gYSBjb21wYXJhw6fDo28gZW50cmUgZnJlcXXDqm5jaWFzIG9ic2VydmFkYXMgKCRPX3tpan0kKSBlIGVzcGVyYWRhcyAoJEVfe2lqfSQpPyIsICJkaWNhIjogIkNvbnNpZGVyZSBhIGVzdHJ1dHVyYSBkYSBmw7NybXVsYSAkXFxjaGleMl97XHRleHR7Y2FsY319ID0gXFxzdW0gXFxmcmFjeyhPX3tpan0gLSBFX3tpan0pXjJ9e0Vfe2lqfX0kIGUgbyBwYXBlbCBkYXMgZGlmZXJlbsOnYXMgcXVhZHLDoXRpY2FzLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBIGVzdGF0w61zdGljYSAkXFxjaGleMl97XHRleHR7Y2FsY319JCBtZWRlIG8gZGVzdmlvIGFjdW11bGFkbyBlbnRyZSBvcyBkYWRvcyBvYnNlcnZhZG9zIGUgb3MgZXNwZXJhZG9zLiIsICJTZSAkXFxjaGleMl97XHRleHR7Y2FsY319IFxcYXBwcm94IDAkLCBlbnTDo28gJChPX3tpan0gLSBFX3tpan0pIFxcYXBwcm94IDAkIHBhcmEgdG9kb3Mgb3MgcGFyZXMgJChpLCBqKSQsIHNpZ25pZmljYW5kbyBxdWUgb3MgZGFkb3Mgb2JzZXJ2YWRvcyBlc3TDo28gbXVpdG8gcHLDs3hpbW9zIGRvIHF1ZSBzZXJpYSBlc3BlcmFkbyBzb2IgaW5kZXBlbmTDqm5jaWEgcGVyZmVpdGEsIGxvZ28sIG7Do28gaMOhIGV2aWTDqm5jaWEgcGFyYSByZWplaXRhciAkSF8wJC4iLCAiU2UgJFxcY2hpXjJfe1x0ZXh0e2NhbGN9fSQgw6kgbXVpdG8gZ3JhbmRlLCBzaWduaWZpY2EgcXVlIGV4aXN0ZSBwZWxvIG1lbm9zIHVtYSBjYXNlbGEgb25kZSAkKE9fe2lqfSAtIEVfe2lqfSleMiQgw6kgc3Vic3RhbmNpYWwsIGluZGljYW5kbyBxdWUgYSBmcmVxdcOqbmNpYSBvYnNlcnZhZGEgZGVzdmlhIHNpZ25pZmljYXRpdmFtZW50ZSBkbyBjZW7DoXJpbyBkZSBpbmRlcGVuZMOqbmNpYSB0ZcOzcmljYSwgc3VnZXJpbmRvIHF1ZSBhcyB2YXJpw6F2ZWlzIHPDo28gYXNzb2NpYWRhcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCA0LCBwLiA3OSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgdW1hIHRhYmVsYSBkZSBjb250aW5nw6puY2lhIG9uZGUgYSB2YXJpw6F2ZWwgJFgkIHRlbSAzIGNhdGVnb3JpYXMgZSBhIHZhcmnDoXZlbCAkWSQgdGVtIDIgY2F0ZWdvcmlhcy4gTyB2YWxvciBkYSBlc3RhdMOtc3RpY2EgY2FsY3VsYWRhIMOpICRcXGNoaV4yX3tcdGV4dHtjYWxjfX0gPSA1LjI1JC4gRGV0ZXJtaW5lIHNlIHJlamVpdGFtb3MgYSBoaXDDs3Rlc2UgbnVsYSBkZSBpbmRlcGVuZMOqbmNpYSBhIHVtIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBkZSAkXFxhbHBoYSA9IDAuMTAkLiAoRGFkbzogVmFsb3IgY3LDrXRpY28gZGEgJFxcY2hpXjIkIHBhcmEgJGdsPTIkIGUgJFxcYWxwaGE9MC4xMCQgw6kgJDQuNjA1JCkuIiwgImRpY2EiOiAiQ29tcGFyZSAkXFxjaGleMl97XHRleHR7Y2FsY319JCBjb20gJFxcY2hpXjJfe1x0ZXh0e2NyaXR9fSQgZSBhcGxpcXVlIGEgcmVncmEgZGUgZGVjaXPDo28gZG8gdGVzdGUgZGUgaGlww7N0ZXNlcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYXIgJGdsJDogUGFyYSAkcj0zJCBlICRzPTIkLCB0ZW1vcyAkZ2wgPSAoMy0xKSgyLTEpID0gMiQuIiwgIjIuIElkZW50aWZpY2FyIGNyaXTDqXJpbzogTyB2YWxvciBjcsOtdGljbyDDqSAkXFxjaGleMl97XHRleHR7Y3JpdH19ID0gNC42MDUkIHBhcmEgJFxcYWxwaGE9MC4xMCQuIiwgIjMuIERlY2lzw6NvOiBDb21wYXJhbW9zICRcXGNoaV4yX3tcdGV4dHtjYWxjfX0gPSA1LjI1JCBjb20gJFxcY2hpXjJfe1x0ZXh0e2NyaXR9fSA9IDQuNjA1JC4iLCAiNC4gQ29uY2x1c8OjbzogQ29tbyAkNS4yNSA+IDQuNjA1JCwgbyB2YWxvciBjYWkgbmEgcmVnacOjbyBkZSByZWplacOnw6NvICgkUkMkKS4gUG9ydGFudG8sIHJlamVpdGFtb3MgJEhfMCQgYSB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgZGUgMTAlLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDAsIDEwLCAyMDApXG55ID0gc3RhdHMuXFxjaGkyLnBkZih4LCBkZj0yKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBuYW1lPSdEZW5zaWRhZGUgJFxcY2hpXjIoMikkJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJywgd2lkdGg9MikpKVxuZmlnLmFkZF92bGluZSh4PTQuNjA1LCBsaW5lX2Rhc2g9J2Rhc2gnLCBsaW5lX2NvbG9yPScjOTkxQjFCJywgbmFtZT0nJFxcY2hpXjJfe1xcdGV4dHtjcml0fX0gPSA0LjYwNSQnKVxuZmlnLmFkZF92bGluZSh4PTUuMjUsIGxpbmVfZGFzaD0nc29saWQnLCBsaW5lX2NvbG9yPScjMTBCOTgxJywgbmFtZT0nJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0gPSA1LjI1JCcpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+VGVzdGUgZGUgSW5kZXBlbmTDqm5jaWEgKGdsPTIpPC9iPicsIHhheGlzX3RpdGxlPXInJFxcY2hpXjIkJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiA1LjI1fSwgeyJlbnVuY2lhZG8iOiAiRW0gdW1hIGbDoWJyaWNhLCBvYnNlcnZvdS1zZSBvIG7Dum1lcm8gZGUgZmFsaGFzIGVtIHRyw6pzIGxpbmhhcyBkZSBtb250YWdlbSAoQSwgQiwgQykgZHVyYW50ZSB1bWEgc2VtYW5hLiBPcyBkYWRvcyBvYnNlcnZhZG9zIGZvcmFtOiBMaW5oYSBBICgxMCBmYWxoYXMpLCBMaW5oYSBCICgxNSBmYWxoYXMpLCBMaW5oYSBDICgyNSBmYWxoYXMpLCB0b3RhbGl6YW5kbyA1MCBmYWxoYXMuIFRlc3RlIGEgaGlww7N0ZXNlIGRlIHF1ZSBhcyBmYWxoYXMgc8OjbyBlcXVpcHJvdsOhdmVpcyBlbnRyZSBhcyB0csOqcyBsaW5oYXMgdXNhbmRvIHVtIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBkZSAkXFxhbHBoYT0wLjA1JC4iLCAiZGljYSI6ICJTb2IgYSBoaXDDs3Rlc2UgbnVsYSAkSF8wJCBkZSBxdWUgYXMgZmFsaGFzIHPDo28gZXF1aXByb3bDoXZlaXMsIHF1YWwgYSBmcmVxdcOqbmNpYSBlc3BlcmFkYSAkRV9pJCBwYXJhIGNhZGEgdW1hIGRhcyAzIGxpbmhhcz8iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gRGVmaW5pciAkSF8wOiBwX0EgPSBwX0IgPSBwX0MgPSAxLzMkIChmYWxoYXMgZXF1aXByb3bDoXZlaXMpLiIsICIyLiBDYWxjdWxhciBhIGZyZXF1w6puY2lhIGVzcGVyYWRhICRFX2kgPSA1MCAvIDMgXFxhcHByb3ggMTYuNjckIHBhcmEgY2FkYSBsaW5oYS4iLCAiMy4gQ2FsY3VsYXIgYSBlc3RhdMOtc3RpY2E6ICRcXGNoaV4yX3tcXHRleHR7Y2FsY319ID0gXFxmcmFjeygxMC0xNi42NyleMn17MTYuNjd9ICsgXFxmcmFjeygxNS0xNi42NyleMn17MTYuNjd9ICsgXFxmcmFjeygyNS0xNi42NyleMn17MTYuNjd9JC4iLCAiNC4gUmVzdWx0YWRvIGFyaXRtw6l0aWNvOiAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3s0NC40OX17MTYuNjd9ICsgXFxmcmFjezIuNzl9ezE2LjY3fSArIFxcZnJhY3s2OS4zOX17MTYuNjd9ID0gMi42NjggKyAwLjE2NyArIDQuMTYyID0gNi45OTckLiIsICI1LiBDb21wYXJhciBjb20gbyB2YWxvciBjcsOtdGljbyBkYSB0YWJlbGEgJFxcY2hpXjIoZ2w9MikkIHBhcmEgJFxcYWxwaGE9MC4wNSQ6ICRcXGNoaV4yX3tcXHRleHR7Y3JpdH19ID0gNS45OTEkLiIsICI2LiBDb21vICQ2Ljk5NyA+IDUuOTkxJCwgcmVqZWl0YW1vcyAkSF8wJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDYuOTk3fSwgeyJlbnVuY2lhZG8iOiAiVW1hIHRhYmVsYSBkZSBjb250aW5nw6puY2lhICQyIFxcdGltZXMgMiQgYXByZXNlbnRhIGFzIHNlZ3VpbnRlcyBmcmVxdcOqbmNpYXMgb2JzZXJ2YWRhczogQ8OpbHVsYSAoMSwxKT0yMCwgQ8OpbHVsYSAoMSwyKT0zMCwgQ8OpbHVsYSAoMiwxKT0zMCwgQ8OpbHVsYSAoMiwyKT0yMC4gQ2FsY3VsZSBhIGVzdGF0w61zdGljYSAkXFxjaGleMl97XHRleHR7Y2FsY319JCBlIGRldGVybWluZSBzZSBhcyB2YXJpw6F2ZWlzIHPDo28gaW5kZXBlbmRlbnRlcy4iLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgZsOzcm11bGEgJEVfe2lqfSA9IFxcZnJhY3tuX3tpLn0gXFxjZG90IG5fey5qfX17bn0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBUb3RhbCAkbiA9IDIwKzMwKzMwKzIwID0gMTAwJC4iLCAiMi4gVG90YWlzIG1hcmdpbmFpczogbGluaGEgMT01MCwgbGluaGEgMj01MCwgY29sdW5hIDE9NTAsIGNvbHVuYSAyPTUwLiIsICIzLiBWYWxvcmVzIGVzcGVyYWRvcyAkRV97aWp9JDogJEVfezExfSA9ICg1MCo1MCkvMTAwID0gMjUkLCAkRV97MTJ9ID0gMjUkLCAkRV97MjF9ID0gMjUkLCAkRV97MjJ9ID0gMjUkLiIsICI0LiBDw6FsY3VsbzogJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7KDIwLTI1KV4yfXsyNX0gKyBcXGZyYWN7KDMwLTI1KV4yfXsyNX0gKyBcXGZyYWN7KDMwLTI1KV4yfXsyNX0gKyBcXGZyYWN7KDIwLTI1KV4yfXsyNX0kLiIsICI1LiBSZXN1bHRhZG86ICRcXGNoaV4yX3tcXHRleHR7Y2FsY319ID0gMSArIDEgKyAxICsgMSA9IDQuMCQuIiwgIjYuIENvbmNsdXPDo286IENvbXBhcmFuZG8gY29tICRcXGNoaV4yX3tcXHRleHR7Y3JpdH19KGdsPTEsIFxcYWxwaGE9MC4wNSkgPSAzLjg0MSQsIGNvbW8gJDQuMCA+IDMuODQxJCwgcmVqZWl0YW1vcyAkSF8wJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDQuMH0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCBzb2IgYSDDs3RpY2EgZGEgJ3N1cnByZXNhIGVzdGF0w61zdGljYScsIHBvciBxdWUgbyB2YWxvciBkYSBlc3RhdMOtc3RpY2EgJFxcY2hpXjJfe1x0ZXh0e2NhbGN9fSQgdGVuZGUgYSBzZXIgbWFpb3IgcXVhbmRvIGFzIGZyZXF1w6puY2lhcyBvYnNlcnZhZGFzIGRpdmVyZ2VtIGRhcyBmcmVxdcOqbmNpYXMgZXNwZXJhZGFzIHNvYiBhIGhpcMOzdGVzZSBudWxhIGRlIGluZGVwZW5kw6puY2lhLiIsICJkaWNhIjogIkNvbnNpZGVyZSBvIHRlcm1vICQoT197aWp9IC0gRV97aWp9KV4yJC4gTyBxdWUgYWNvbnRlY2UgY29tIGVsZSBxdWFuZG8gYSBkaWZlcmVuw6dhIGF1bWVudGE/IiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIEEgaGlww7N0ZXNlIG51bGEgZGUgaW5kZXBlbmTDqm5jaWEgcHJlc3N1cMO1ZSBxdWUgYXMgZnJlcXXDqm5jaWFzIG9ic2VydmFkYXMgZGV2ZW0gc2VyIHByw7N4aW1hcyBkYXMgZXNwZXJhZGFzICgkT197aWp9IFxcYXBwcm94IEVfe2lqfSQpLiIsICIyLiBPIHRlcm1vIG5vIG51bWVyYWRvciAkKE9fe2lqfSAtIEVfe2lqfSleMiQgY2FwdHVyYSBhIG1hZ25pdHVkZSBkbyBlcnJvLiBTZSBhcyBmcmVxdcOqbmNpYXMgb2JzZXJ2YWRhcyBzw6NvIG11aXRvIGRpZmVyZW50ZXMgZGFzIGVzcGVyYWRhcywgZXNzYSBkaWZlcmVuw6dhIGVsZXZhIGFvIHF1YWRyYWRvIHRvcm5hLXNlIHVtIHZhbG9yIHBvc2l0aXZvIGdyYW5kZS4iLCAiMy4gQSBlc3RhdMOtc3RpY2EgJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0kIMOpIGEgc29tYSBkZSB0b2RvcyBlc3NlcyBlcnJvcyBub3JtYWxpemFkb3MuIiwgIjQuIENvbnNlcXVlbnRlbWVudGUsIHF1YW50byBtYWlvciBhIGRpdmVyZ8OqbmNpYSwgbWFpb3IgYSAnc3VycHJlc2EnIGUsIHBvcnRhbnRvLCBtYWlvciBvIHZhbG9yIGRhIGVzdGF0w61zdGljYS4iLCAiNS4gVmFsb3JlcyBhbHRvcyBkYSBlc3RhdMOtc3RpY2EgaW5kaWNhbSBxdWUgYSBoaXDDs3Rlc2UgZGUgaW5kZXBlbmTDqm5jaWEgw6kgcG91Y28gdmVyb3Nzw61taWwgZnJlbnRlIGFvcyBkYWRvcyBvYnNlcnZhZG9zLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGV4cGVyaW1lbnRvIGNvbSAzMDAgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zLCBjbGFzc2lmaWNvdS1zZSBhIGZhbGhhIGNvbW8gJ1ByZWNvY2UnIG91ICdUYXJkaWEnIGUgYSBvcmlnZW0gZG8gY29tcG9uZW50ZSBjb21vICdGb3JuZWNlZG9yIFgnIG91ICdGb3JuZWNlZG9yIFknLiBBIGZyZXF1w6puY2lhIGVzcGVyYWRhICRFX3tpan0kIMOpIGNhbGN1bGFkYSBwZWxvIHByb2R1dG8gZGFzIGZyZXF1w6puY2lhcyBtYXJnaW5haXMgZGl2aWRpZGEgcGVsbyB0b3RhbCBkYSBhbW9zdHJhLiBTZSB0ZW1vcyAkMTAwJCBjb21wb25lbnRlcyBkbyBGb3JuZWNlZG9yIFggZSAkMjAwJCBkbyBGb3JuZWNlZG9yIFksIGUgbyB0b3RhbCBkZSBmYWxoYXMgcHJlY29jZXMgw6kgJDE1MCQsIHF1YWwgYSBmcmVxdcOqbmNpYSBlc3BlcmFkYSAkRV97aWp9JCBkZSBmYWxoYXMgcHJlY29jZXMgcGFyYSBvIEZvcm5lY2Vkb3IgWD8iLCAiZGljYSI6ICJBIGbDs3JtdWxhIGRhIGZyZXF1w6puY2lhIGVzcGVyYWRhIMOpICRFX3tpan0gPSBcXGZyYWN7KFxcdGV4dHtUb3RhbCBkYSBMaW5oYSB9IGkpIFxcY2RvdCAoXFx0ZXh0e1RvdGFsIGRhIENvbHVuYSB9IGopfXtufSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIklkZW50aWZpY2Ftb3Mgb3MgdG90YWlzIG1hcmdpbmFpcyBlIGFtb3N0cmFsOiAkbiA9IDMwMCQsICRcXHRleHR7VG90YWwgbGluaGEgKEZhbGhhcyBQcmVjb2Nlcyl9ID0gMTUwJCwgJFxcdGV4dHtUb3RhbCBjb2x1bmEgKEZvcm5lY2Vkb3IgWCl9ID0gMTAwJC4iLCAiQXBsaWNhbW9zIGEgZsOzcm11bGEgZGEgZnJlcXXDqm5jaWEgZXNwZXJhZGE6ICQkRV97aWp9ID0gXFxmcmFjezE1MCBcXGNkb3QgMTAwfXszMDB9JCQiLCAiQ2FsY3VsYW1vcyBvIHZhbG9yIGZpbmFsOiAkJEVfe2lqfSA9IFxcZnJhY3sxNTAwMH17MzAwfSA9IDUwJCQiLCAiQ29uY2x1c8OjbzogQSBmcmVxdcOqbmNpYSBlc3BlcmFkYSBkZSBmYWxoYXMgcHJlY29jZXMgcGFyYSBvIEZvcm5lY2Vkb3IgWCDDqSBkZSA1MCB1bmlkYWRlcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDUwLjB9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgdW1hIHRhYmVsYSBkZSBjb250aW5nw6puY2lhIGRlIGRpbWVuc8OjbyAkMyBcXHRpbWVzIDIkICgzIG7DrXZlaXMgZGUgc2F0aXNmYcOnw6NvIHZzIDIgdGlwb3MgZGUgc2VydmnDp28pLiBEZXRlcm1pbmUgb3MgZ3JhdXMgZGUgbGliZXJkYWRlICgkZ2wkKSBlIGNhbGN1bGUgbyB2YWxvciBjcsOtdGljbyAkXFxjaGleMl97XFx0ZXh0e2NyaXR9fSQgcGFyYSB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLDA1JC4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIHBhcmEgdW1hIHRhYmVsYSAkciBcXHRpbWVzIHMkLCBvcyBncmF1cyBkZSBsaWJlcmRhZGUgc8OjbyBkYWRvcyBwb3IgJGdsID0gKHItMSkocy0xKSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkRlZmluaW1vcyAkcj0zJCAobGluaGFzKSBlICRzPTIkIChjb2x1bmFzKS4iLCAiQ2FsY3VsYW1vcyAkZ2wkOiAkJGdsID0gKDMtMSkgXFxjZG90ICgyLTEpID0gMiBcXGNkb3QgMSA9IDIkJCIsICJDb25zdWx0YW1vcyBhIGRpc3RyaWJ1acOnw6NvICRcXGNoaV4yJCBjb20gJGdsPTIkIHBhcmEgJFxcYWxwaGE9MCwwNSQuIiwgIk8gdmFsb3IgY3LDrXRpY28gY29ycmVzcG9uZGVudGUgbmEgdGFiZWxhIGRlIGRpc3RyaWJ1acOnw6NvIMOpIGFwcm94aW1hZGFtZW50ZSAkNSw5OSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiA1Ljk5fSwgeyJlbnVuY2lhZG8iOiAiRGlzY3V0YSBtYXRlbWF0aWNhbWVudGUgcG9yIHF1ZSwgZW0gdW0gdGVzdGUgcXVpLXF1YWRyYWRvIGRlIGluZGVwZW5kw6puY2lhLCBhIGVzdGF0w61zdGljYSAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSQgc2VtcHJlIHJlc3VsdGEgZW0gdW0gdmFsb3IgbsOjbyBuZWdhdGl2by4gQ29tbyBpc3NvIGltcGFjdGEgYSBmb3JtYSBkYSByZWdpw6NvIGNyw610aWNhPyIsICJkaWNhIjogIkFuYWxpc2UgYSBlc3RydXR1cmEgZGEgZsOzcm11bGE6ICRcXGNoaV4yX3tcXHRleHR7Y2FsY319ID0gXFxzdW0gXFxmcmFjeyhPX3tpan0gLSBFX3tpan0pXjJ9e0Vfe2lqfX0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBIGVzdGF0w61zdGljYSDDqSBjb21wb3N0YSBwb3IgdW1hIHNvbWEgZGUgdGVybW9zIGRhIGZvcm1hICRcXGZyYWN7KE9fe2lqfSAtIEVfe2lqfSleMn17RV97aWp9fSQuIiwgIk8gbnVtZXJhZG9yICQoT197aWp9IC0gRV97aWp9KV4yJCDDqSBvIHF1YWRyYWRvIGRlIHVtYSBkaWZlcmVuw6dhIHJlYWwsIGxvZ28gw6kgc2VtcHJlICRcXGdlcSAwJC4iLCAiTyBkZW5vbWluYWRvciAkRV97aWp9JCDDqSB1bWEgY29udGFnZW0gZXNwZXJhZGEgYmFzZWFkYSBlbSB0b3RhaXMgbWFyZ2luYWlzLCBzZW5kbyBlc3RyaXRhbWVudGUgcG9zaXRpdmEgKCRFX3tpan0gPiAwJCkuIiwgIkNvbW8gYSBzb21hIGRlIHZhbG9yZXMgbsOjbyBuZWdhdGl2b3Mgw6kgbsOjbyBuZWdhdGl2YSwgJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0gXFxnZXEgMCQuIiwgIkNvbmNsdXPDo286IENvbW8gYSBlc3RhdMOtc3RpY2Egw6kgc2VtcHJlIHBvc2l0aXZhLCBhIHJlZ2nDo28gY3LDrXRpY2EgcGFyYSByZWplaXRhciAkSF8wJCDDqSBzZW1wcmUgbG9jYWxpemFkYSBuYSBjYXVkYSBzdXBlcmlvciAoZGlyZWl0YSkgZGEgZGlzdHJpYnVpw6fDo28gcXVpLXF1YWRyYWRvLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBpbmR1c3RyaWFsLCBmb3JhbSBjb2xldGFkb3MgZGFkb3MgZGUgMjAwIGl0ZW5zIHByb2R1emlkb3MsIHNlbmRvIGNsYXNzaWZpY2Fkb3MgcG9yIG9yaWdlbSAoQSwgQiwgQykgZSB0aXBvIGRlIGZhbGhhIChUaXBvIEksIFRpcG8gSUksIFRpcG8gSUlJKS4gQSBlc3RhdMOtc3RpY2EgY2FsY3VsYWRhIGZvaSAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSA9IDMwJC4gQ2FsY3VsZSBvIENvZWZpY2llbnRlIFQgZGUgVHNjaHVwcm93ICgkVCQpIHBhcmEgZXN0YSB0YWJlbGEgZGUgY29udGluZ8OqbmNpYSAkMyBcXHRpbWVzIDMkLiIsICJkaWNhIjogIlVzZSBhIGbDs3JtdWxhICRUID0gXFxzcXJ0e1xcZnJhY3tcXGNoaV4yX3tcXHRleHR7Y2FsY319IC8gbn17XFxzcXJ0eyhyLTEpKHMtMSl9fX0kLCBvbmRlICRuPTIwMCQsICRyPTMkIGUgJHM9MyQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIElkZW50aWZpY2FyIG9zIHBhcsOibWV0cm9zOiAkbiA9IDIwMCQsICRcXGNoaV4yX3tcXHRleHR7Y2FsY319ID0gMzAkLCAkciA9IDMkIChsaW5oYXMpLCAkcyA9IDMkIChjb2x1bmFzKS4iLCAiMi4gQ2FsY3VsYXIgbyB0ZXJtbyAkXFxzcXJ0eyhyLTEpKHMtMSl9ID0gXFxzcXJ0eygzLTEpKDMtMSl9ID0gXFxzcXJ0ezIgXFx0aW1lcyAyfSA9IFxcc3FydHs0fSA9IDIkLiIsICIzLiBDYWxjdWxhciBhIHJhesOjbyAkXFxmcmFje1xcY2hpXjJfe1xcdGV4dHtjYWxjfX19e259ID0gXFxmcmFjezMwfXsyMDB9ID0gMCwxNSQuIiwgIjQuIEFwbGljYXIgYSBmw7NybXVsYSBkZSBUc2NodXByb3c6ICRUID0gXFxzcXJ0e1xcZnJhY3swLDE1fXsyfX0gPSBcXHNxcnR7MCwwNzV9IFxcYXBwcm94IDAsMjczOCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgNCwgcC4gNzkiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjI3Mzh9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSBhIGRpZmVyZW7Dp2EgY29uY2VpdHVhbCBlIHByw6F0aWNhIGVudHJlIG8gdGVzdGUgZGUgaW5kZXBlbmTDqm5jaWEgZSBvIHRlc3RlIGRlIGhvbW9nZW5laWRhZGUsIGFtYm9zIGJhc2VhZG9zIG5hIGVzdGF0w61zdGljYSAkXFxjaGleMl97XFx0ZXh0e2NhbGN9fSQuIEVtIHF1ZSBzaXR1YcOnw6NvIGNhZGEgdW0gw6kgYXBsaWNhZG8/IiwgImRpY2EiOiAiUGVuc2Ugc29icmUgYSBvcmlnZW0gZG9zIGRhZG9zOiBlbGVzIHbDqm0gZGUgdW1hIMO6bmljYSBhbW9zdHJhIChjcnV6YW5kbyBkdWFzIHZhcmnDoXZlaXMpIG91IGRlIHbDoXJpYXMgYW1vc3RyYXMgZGlzdGludGFzIChjb21wYXJhbmRvIGdydXBvcyk/IiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIFRlc3RlIGRlIEluZGVwZW5kw6puY2lhOiBVdGlsaXphZG8gcXVhbmRvIHNlIHRlbSB1bWEgw7puaWNhIGFtb3N0cmEgZGUgdGFtYW5obyAkbiQgZSBkdWFzIHZhcmnDoXZlaXMgcXVhbGl0YXRpdmFzIFggZSBZLCBjb20gbyBvYmpldGl2byBkZSB2ZXJpZmljYXIgc2UgYXMgdmFyacOhdmVpcyBlc3TDo28gYXNzb2NpYWRhcyAoc2UgYSBkaXN0cmlidWnDp8OjbyBkZSBYIGluZGVwZW5kZSBkZSBZKS4iLCAiMi4gVGVzdGUgZGUgSG9tb2dlbmVpZGFkZTogVXRpbGl6YWRvIHF1YW5kbyB0ZW1vcyAkciQgcG9wdWxhw6fDtWVzIGRpc3RpbnRhcyBlIHF1ZXJlbW9zIHZlcmlmaWNhciBzZSBhIGRpc3RyaWJ1acOnw6NvIGRlIHVtYSB2YXJpw6F2ZWwgY2F0ZWfDs3JpY2Egw6kgYSBtZXNtYSAoaG9tb2fDqm5lYSkgZW0gdG9kYXMgZWxhcyAoJEhfMDogUF8xID0gUF8yID0gXFxkb3RzID0gUF9yJCkuIiwgIjMuIFByYXRpY2FtZW50ZSwgYW1ib3MgdXRpbGl6YW0gYSBtZXNtYSBlc3RhdMOtc3RpY2EgJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0gPSBcXHN1bSBcXHN1bSBcXGZyYWN7KG5fe2lqfSAtIG5fe2lqfV4qKV4yfXtuX3tpan1eKn0kIGUgYSBtZXNtYSBkaXN0cmlidWnDp8OjbyAkXFxjaGleMihnbCkkIGNvbSAkZ2wgPSAoci0xKShzLTEpJCBncmF1cyBkZSBsaWJlcmRhZGUuIiwgIjQuIEEgZGlmZXJlbsOnYSBmdW5kYW1lbnRhbCDDqSBvIGRlc2VuaG8gYW1vc3RyYWw6IG8gcHJpbWVpcm8gZm9jYSBlbSBhc3NvY2lhw6fDo28gZGVudHJvIGRlIHVtIGdydXBvLCBvIHNlZ3VuZG8gZW0gY29tcGFyYcOnw6NvIGVudHJlIGdydXBvcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgcXVlIGEgZXN0YXTDrXN0aWNhICRcXGNoaV4yX3tcXHRleHR7Y2FsY319JCBkZXBlbmRlIGZvcnRlbWVudGUgZG8gdGFtYW5obyBkYSBhbW9zdHJhICRuJC4gU2UgdGl2ZXJtb3MgdW0gZXN0dWRvIGRlIGFzc29jaWHDp8OjbyBjb20gJG4gPSAxMDAwJCBlIG91dHJvIGNvbSAkbiA9IDEwMCQsIGFtYm9zIGFwcmVzZW50YW5kbyBvIG1lc21vIHBhZHLDo28gZGUgZGlzdHJpYnVpw6fDo28gcmVsYXRpdmEsIHF1YWwgbcOpdHJpY2Egdm9jw6ogcmVjb21lbmRhcmlhIHBhcmEgY29tcGFyYXIgYSBpbnRlbnNpZGFkZSBkYSBhc3NvY2lhw6fDo28gZW50cmUgZWxlcyBlIHBvciBxdcOqPyIsICJkaWNhIjogIkNvbnNpZGVyZSBhIG5vcm1hbGl6YcOnw6NvIGRhcyBlc3RhdMOtc3RpY2FzIGRlIGFzc29jaWHDp8OjbyAoQyBvdSBUKS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gQSBlc3RhdMOtc3RpY2EgJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0kIGF1bWVudGEgbGluZWFybWVudGUgY29tIG8gdGFtYW5obyBkYSBhbW9zdHJhICRuJCBwYXJhIHVtYSBtZXNtYSBjb25maWd1cmHDp8OjbyBkZSBmcmVxdcOqbmNpYXMgcmVsYXRpdmFzLCB0b3JuYW5kbyBkaWbDrWNpbCBhIGNvbXBhcmHDp8OjbyBkaXJldGEgZGUgaW50ZW5zaWRhZGUgYXBlbmFzIHBlbG8gdmFsb3IgZGUgJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0kLiIsICIyLiBSZWNvbWVuZGEtc2UgdXRpbGl6YXIgbyBDb2VmaWNpZW50ZSBkZSBDb250aW5nw6puY2lhICRDJCBvdSBvIENvZWZpY2llbnRlICRUJCBkZSBUc2NodXByb3cuIiwgIjMuIEVzc2FzIG3DqXRyaWNhcyBub3JtYWxpemFtIG8gdmFsb3IgZGUgJFxcY2hpXjJfe1xcdGV4dHtjYWxjfX0kIHBlbG8gdGFtYW5obyBkYSBhbW9zdHJhICgkbiQpLCBwZXJtaXRpbmRvIHVtYSBpbnRlcnByZXRhw6fDo28gZW50cmUgMCBlIDEuIiwgIjQuIE8gY29lZmljaWVudGUgJFQkLCBlbSBwYXJ0aWN1bGFyLCBhanVzdGEtc2UgY29uZm9ybWUgYSBkaW1lbnPDo28gZGEgdGFiZWxhICQociwgcykkLCBvIHF1ZSBwcm92w6ogdW1hIG1lZGlkYSBkZSBhc3NvY2lhw6fDo28gbWFpcyBlc3TDoXZlbCBwYXJhIGNvbXBhcmHDp8OjbyBlbnRyZSBlc3R1ZG9zIGNvbSBkaWZlcmVudGVzIGVzdHJ1dHVyYXMgYW1vc3RyYWlzLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDQsIHAuIDc5IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH1dfQ==').decode('utf-8'))


    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    from scipy import stats
    
    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do total de exercícios
    total_mcq = len(dados_exercicios.get("questoes_multipla_escolha", []))
    total_disc = len(dados_exercicios.get("questoes_discursivas", []))
    total_exercicios = total_mcq + total_disc
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    # Interface de progresso
    st.subheader("📊 Painel de Desempenho")
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    st.divider()
    
    # Renderização das Questões de Múltipla Escolha
    if "questoes_multipla_escolha" in dados_exercicios:
        for i, q in enumerate(dados_exercicios["questoes_multipla_escolha"]):
            st.markdown(f"### 🎯 Questão {i + 1}")
            st.write(q.get("enunciado", ""))
            
            # Plotly opcional
            codigo_plot = q.get("codigo_plotly")
            if codigo_plot:
                try:
                    local_vars = {"go": go, "np": np, "stats": stats}
                    exec(codigo_plot, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
                except Exception as e:
                    st.error(f"Erro ao renderizar gráfico: {e}")
    
            # Dica e Referência
            if st.button(f"💡 Dica da Questão {i + 1}", key=f"btn_dica_mcq_{i}"):
                st.info(q.get("dica", "Dica indisponível"))
            
            ref = q.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
    
            # Alternativas
            alternativas = q.get("alternativas", {})
            escolha = st.radio(
                "Selecione uma alternativa:",
                options=list(alternativas.keys()),
                format_func=lambda x: f"{x}: {alternativas[x]}",
                key=f"radio_mcq_{i}"
            )
    
            # Verificação
            if st.button("✅ Verificar Resposta", key=f"btn_verify_mcq_{i}"):
                if escolha == q.get("alternativa_correta"):
                    st.success("Correto! Muito bem.")
                    st.session_state.respostas_certas[f"mcq_{i}"] = True
                    st.rerun()
                else:
                    st.error("Resposta incorreta. Tente novamente!")
                    st.session_state.respostas_certas[f"mcq_{i}"] = False
                    st.rerun()
            
            with st.expander("✅ Ver Gabarito Comentado"):
                st.write(q.get("gabarito_comentado", "Gabarito indisponível"))
            st.divider()
    
    # Renderização das Questões Discursivas
    if "questoes_discursivas" in dados_exercicios:
        for i, q in enumerate(dados_exercicios["questoes_discursivas"]):
            st.markdown(f"### 📝 Questão Discursiva {i + 1}")
            st.write(q.get("enunciado", ""))
            
            # Plotly opcional
            codigo_plot = q.get("codigo_plotly")
            if codigo_plot:
                try:
                    local_vars = {"go": go, "np": np, "stats": stats}
                    exec(codigo_plot, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
                except Exception as e:
                    st.error(f"Erro ao renderizar gráfico: {e}")
    
            st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
            
            # Lógica de validação numérica ou checkbox
            valor_esperado = q.get("resposta_numerica_esperada")
            if valor_esperado is not None:
                user_val = st.number_input("Digite o resultado numérico calculado para validação:", format="%.4f", key=f"num_disc_{i}")
                if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                    if abs(user_val - valor_esperado) <= max(0.01, 0.01 * abs(valor_esperado)):
                        st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                        st.rerun()
                    else:
                        st.error("O valor calculado difere do gabarito oficial. Verifique seus arredondamentos e fórmulas e tente novamente.")
                        st.session_state.respostas_certas[f"disc_{i}"] = False
                        st.rerun()
            else:
                if st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}"):
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                else:
                    st.session_state.respostas_certas[f"disc_{i}"] = False
    
            # Dica e Referência
            if st.button(f"💡 Dica da Questão Discursiva {i + 1}", key=f"btn_dica_disc_{i}"):
                st.info(q.get("dica", "Dica indisponível"))
            
            ref = q.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
    
            with st.expander("✅ Ver Resolução Detalhada"):
                for passo in q.get("gabarito_passo_a_passo", []):
                    st.markdown(f"- {passo}")
            st.divider()
