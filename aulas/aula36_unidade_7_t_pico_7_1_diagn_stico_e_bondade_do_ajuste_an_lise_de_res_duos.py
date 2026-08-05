import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDcgLSBUw7NwaWNvIDcuMTogRGlhZ27Ds3N0aWNvIGUgYm9uZGFkZSBkbyBhanVzdGU6IEFuw6FsaXNlIGRlIHJlc8OtZHVvcyIsICJyZWZlcmVuY2lhc19iaWJsaW9ncmFmaWNhc19maW5haXMiOiBbIkx1bmEgJiBFc3RldmVzLCBNb2RlbG9zIExpbmVhcmVzIC0gQ2FwLiA0LjMsIHBwLiA4My05MCwgMTA5LTExMiIsICJGYXJhd2F5LCBMaW5lYXIgTW9kZWxzIHdpdGggUiAtIENhcC4gNy4xLTcuMiwgcHAuIDcyLTc0IiwgIkZhcmF3YXksIExpbmVhciBNb2RlbHMgd2l0aCBSIC0gQ2FwLiA3LjUtNy42LCBwcC4gODAtODQiLCAiRmFyYXdheSwgTGluZWFyIE1vZGVscyB3aXRoIFIgLSBDYXAuIDcuOCwgcHAuIDg4LTkxIiwgIkx1bmEgJiBFc3RldmVzLCBJbnRyb2R1w6fDo28gYW9zIE1vZGVsb3MgTGluZWFyZXMgLSBDYXAuIDMuNiwgcHAuIDcxLTcyIiwgIkZhcmF3YXksIExpbmVhciBNb2RlbHMgd2l0aCBSIC0gQ2FwLiA3LjQsIHBwLiA3OC03OSJdfQ==').decode('utf-8'))

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
            background: linear-gradient(135deg, #0000FF 0%, #3B82F6 100%);
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
            border-top: 3px solid #0000FF !important;
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
            background: linear-gradient(90deg, #0000FF 0%, #808080 100%) !important;
            border-radius: 10px !important;
        }
        
        /* Inputs e Sliders na aula */
        div.stSlider [data-testid="stSliderTickBar"] {
            background-color: #0000FF !important;
        }
        
        /* Botões na aula */
        div.stButton > button {
            background: linear-gradient(135deg, #0000FF 0%, #3B82F6 100%) !important;
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
PRIMARY_BLUE = "#0000FF"
SECONDARY_GREEN = "#808080"
WARNING_AMBER = "#FFFFFF"
CRITICAL_RED = "#FF0000"

# Criação das Duas Grandes Abas Globais
tab_conteudo, tab_exercicios = st.tabs(["📚 Conteúdo Acadêmico Interativo", "📝 Caderno de Exercícios"])

with tab_conteudo:

    # Cabeçalho do Subtópico
    st.header(r"Definição Formal e Propriedades Estatísticas do Vetor de Resíduos")
    
    # Introdução Teórica
    st.markdown(r"""
    A modelagem estatística é um exercício de mediação entre o determinismo matemático e a imprevisibilidade dos fenômenos naturais. 
    Ao propormos um modelo linear, buscamos comprimir a complexidade do real em uma estrutura analítica tratável, 
    representada pela decomposição do vetor de respostas em uma parcela sistemática e uma estocástica.
    """)
    
    st.markdown(r"""
    Esta formulação nos permite isolar o que é puramente informativo da parcela de ruído, denominada componente delta. 
    A compreensão deste componente é fundamental, pois ele abriga todas as flutuações, variáveis omitidas 
    e erros de mensuração que o modelo não consegue capturar.
    """)
    
    st.info(r"O vetor de resíduos é, portanto, a nossa estimativa observável deste erro inobservável, sendo o espelho da qualidade do ajuste estatístico.")
    
    # Formalismo Matemático
    st.markdown(r"### 📐 O Coração Matemático: Projeção e Ortogonalidade")
    
    st.markdown(r"""
    Abaixo, derivamos a natureza do resíduo como a projeção do vetor y no espaço complementar ao subespaço coluna de X:
    """)
    
    st.latex(r"y = X\theta + \Delta")
    st.latex(r"\hat{y} = X\hat{\theta} = Py, \quad \text{onde } P = X(X^TX)^{-}X^T")
    
    st.markdown(r"O resíduo é definido pela diferença entre a observação real e o valor predito:")
    st.latex(r"e = y - \hat{y} = y - Py = (I_n - P)y")
    
    st.markdown(r"""
    Uma das propriedades mais elegantes do método dos mínimos quadrados é que o resíduo é ortogonal ao espaço dos previsores:
    """)
    st.latex(r"X^T e = X^T(I_n - P)y = (X^T - X^T)y = 0")
    
    st.markdown(r"""
    Finalmente, a soma dos quadrados dos resíduos, que utilizamos para diagnosticar a variância dos erros, é expressa por:
    """)
    st.latex(r"SQ_{Res} = e^Te = y^T(I_n - P)y")
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Diagnóstico de Ajuste")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Experimento de Ganho de Peso em Suínos")
        st.markdown(r"Considerando um experimento com 10 observações e 3 tratamentos, onde o modelo é ajustado para o ganho de peso.")
        
        st.latex(r"n = 10, \quad rank(X) = 3, \quad SQ_{Res} = 6,0")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Graus de Liberdade do Resíduo ($gl_{Res}$):** $10 - 3 = 7$")
        st.markdown(r"- **Soma de Quadrados do Resíduo ($SQ_{Res}$):** $6,0$")
        st.markdown(r"- **Quadrado Médio do Resíduo ($QM_{Res}$):** $6,0 / 7 \approx 0,857$")
        
        st.success(r"O quadrado médio do resíduo, estimado em 0,857, fornece uma medida robusta para a variância dos erros. Este valor indica que o modelo possui uma precisão aceitável, servindo como base para as próximas inferências sobre o ganho de peso dos animais.")
    
    # Reflexão Final
    st.markdown(r"---")
    st.markdown(r"### 💡 Reflexão sobre a Análise de Resíduos")
    st.markdown(r"""
    A análise rigorosa dos resíduos é a etapa diagnóstica que separa o analista amador do estatístico profissional. 
    Ao examinar cada componente, interrogamos a própria integridade das nossas premissas fundamentais:
    """)
    
    st.markdown(r"""
    * **Homocedasticidade:** Ausência de padrões de variabilidade crescente nos resíduos.
    * **Normalidade:** Conformidade dos resíduos com uma distribuição Gaussiana.
    * **Independência:** Ausência de autocorrelação temporal ou espacial.
    """)
    
    st.markdown(r"""
    A persistência de padrões gráficos nestes resíduos é, frequentemente, um sinal de má especificação da forma funcional 
    ou da omissão de variáveis explicativas cruciais para o fenômeno em estudo.
    """)

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    
    # Cabeçalho do Subtópico
    st.header(r"A Geometria dos Resíduos e o Papel da Matriz de Projeção")
    
    # Prosa expandida com ritmo de leitura
    st.markdown(r"""
    Ao realizarmos a modelagem de fenômenos complexos por meio de regressão linear, o objetivo central é capturar a estrutura sistemática dos dados em um subespaço de menor dimensão. O vetor de observações reais raramente pertence perfeitamente a esse subespaço devido à variabilidade aleatória ou fatores não modelados.
    """)
    
    st.info(r"A geometria dos resíduos decompõe o vetor de dados em duas partes ortogonais: uma que reside no espaço do modelo, representando nossa melhor estimativa, e outra que reside no espaço perpendicular, capturando o erro.")
    
    st.markdown(r"""
    Esta interpretação é viabilizada pela **matriz de projeção**, frequentemente denominada 'matriz chapéu'. Os pontos-chave deste formalismo são:
    - **Operador Linear:** Atua projetando o vetor de dados sobre o subespaço das colunas da matriz de delineamento.
    - **Isolamento de Erros:** Permite separar a informação sistemática do ruído.
    - **Idempotência:** A propriedade $P^2 = P$ reforça a natureza geométrica da projeção ortogonal.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Geometria de Projeção")
    st.latex(r"P = X(X^TX)^{-}X^T")
    st.latex(r"e = (I_n - P)y")
    st.latex(r"y = \hat{y} + e")
    
    # Demonstração Analítica Estática
    st.markdown(r"**Passo a passo da decomposição ortogonal:**")
    st.latex(r"y = X\theta + \Delta")
    st.markdown(r"Definimos a estimativa da resposta através do operador de projeção:")
    st.latex(r"\hat{y} = Py")
    st.markdown(r"O resíduo é, portanto, a parcela dos dados que não pertence ao subespaço do modelo:")
    st.latex(r"e = (I_n - P)y")
    st.markdown(r"A natureza idempotente da matriz chapéu garante a consistência do modelo:")
    st.latex(r"(I_n - P)(I_n - P) = I_n - 2P + P^2 = I_n - P")
    st.markdown(r"A ortogonalidade entre o modelo e os resíduos é verificada pela nulidade do produto interno:")
    st.latex(r"X^Te = X^T(I_n - P)y = 0")
    
    # Exemplo Prático Rich
    st.subheader(r"📈 Casos de Aplicação Prática: Predição de Rendimento")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Análise de Rendimento Agrícola")
        st.markdown(r"Considere a predição de rendimento agrícola ($y$) baseada em dois níveis de fertilizante. O objetivo é decompor o vetor observado entre a média do grupo e o resíduo aleatório.")
        
        st.latex(r"X = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & 1 \\ 1 & 0 & 1 \end{pmatrix}, \quad y = \begin{pmatrix} 10 \\ 12 \\ 6 \\ 4 \end{pmatrix}")
        
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- **Cálculo da Matriz Chapéu ($P$):** A aplicação do operador $P = X(X^TX)^{-}X^T$ projeta os dados nas médias dos tratamentos.")
        st.latex(r"P = \begin{pmatrix} 0.5 & 0.5 & 0 & 0 \\ 0.5 & 0.5 & 0 & 0 \\ 0 & 0 & 0.5 & 0.5 \\ 0 & 0 & 0.5 & 0.5 \end{pmatrix}")
        
        st.markdown(r"- **Cálculo das Estimativas e Resíduos:**")
        st.latex(r"\hat{y} = [11, 11, 5, 5]^T, \quad e = [-1, 1, 1, -1]^T")
        
        st.success(r"O vetor de resíduos $[-1, 1, 1, -1]^T$ isola a variação interna de cada grupo de tratamento. A ortogonalidade $X^Te=0$ confirma que o subespaço foi perfeitamente extraído do sinal original.")
    
    # Nota Final de Conclusão
    st.markdown(r"""
    ---
    **Nota Executiva:** A visualização desta estrutura permite detectar fraquezas estruturais no modelo. Se surgirem padrões sistemáticos nos resíduos, o modelo deve ser ajustado para garantir a confiabilidade estatística e evitar o viés de omissão de variáveis relevantes.
    """)

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    import pandas as pd
    
    # Cabeçalho principal do tópico
    st.header(r"Escalonamento de Resíduos: Resíduos Padronizados e Studentizados")
    
    # Introdução teórica parcelada
    st.markdown(r"""
    A análise de resíduos constitui o alicerce sobre o qual se edifica a validade de qualquer modelo de regressão linear. Em sua essência, o resíduo $e_i = Y_i - \hat{Y}_i$ representa o desvio entre o que observamos empiricamente e o que o modelo estima.
    """)
    
    st.info(r"Nota Técnica: A interpretação isolada de resíduos brutos ignora a geometria subjacente ao espaço dos preditores. Pontos com alta alavancagem forçam o modelo a aproximar-se deles, mascarando a magnitude real do erro.")
    
    st.markdown(r"""
    Para mitigar esse enviesamento, adotamos as seguintes práticas de escalonamento:
    - **Padronização:** Divide o resíduo pelo erro padrão estimado da regressão ($\hat{\sigma}$).
    - **Studentização:** Ajusta o resíduo considerando a alavancagem ($h_{ii}$), tornando a medida sensível à variabilidade local do modelo.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Escalonamento e Alavancagem")
    st.latex(r"r_i = \frac{e_i}{\hat{\sigma}\sqrt{1 - h_{ii}}} \quad \text{onde} \quad h_{ii} = H_{ii}")
    
    # Dedução Analítica (Sequencial, sem expander)
    st.markdown(r"A dedução do resíduo studentizado deriva diretamente da matriz de projeção $H$:")
    st.latex(r"e = (I_n - H)y")
    st.markdown(r"Considerando a variância dos resíduos:")
    st.latex(r"Var(e) = \sigma^2(I_n - H)")
    st.markdown(r"Extraindo a variância individual do $i$-ésimo resíduo:")
    st.latex(r"Var(e_i) = \sigma^2(1 - h_{ii})")
    st.markdown(r"Ao normalizarmos pelo erro padrão estimado, obtemos a forma studentizada final:")
    st.latex(r"r_i = \frac{e_i}{\hat{\sigma}\sqrt{1 - h_{ii}}}")
    
    # Simulador de Alavancagem
    st.subheader(r"🎛️ Visualizador de Alavancagem e Resíduos")
    col1, col2 = st.columns(2)
    with col1:
        h_val = st.slider(r"Alavancagem ($h_{ii}$)", 0.01, 0.99, 0.35, key=r"h_subtopico_3")
    with col2:
        e_val = st.slider(r"Resíduo Bruto ($e_i$)", -5.0, 5.0, 1.2, key=r"e_subtopico_3")
    
    sigma_hat = 1.414
    r_student = e_val / (sigma_hat * np.sqrt(1 - h_val))
    cor_ponto = "#FF0000" if abs(r_student) > 2 else "#0000FF"
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[h_val], y=[r_student], mode='markers', marker=dict(size=15, color=cor_ponto)))
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Efeito da Alavancagem no Resíduo Studentizado</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Alavancagem (h_ii)", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Resíduo Studentizado", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_3")
    
    st.info(f"Com alavancagem de {h_val:.2f} e resíduo bruto de {e_val:.2f}, o valor studentizado resultante é {r_student:.4f}. {'Este ponto apresenta indícios de comportamento atípico.' if abs(r_student) > 2 else 'O comportamento do resíduo permanece dentro da faixa de normalidade estatística.'}")
    
    # Exemplo Prático
    st.subheader(r"📈 Casos de Aplicação Prática: Avaliação de Resíduos")
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Frota de Veículos")
        st.markdown(r"Em uma frota com $n=20$, avaliamos o caso 15: alavancagem $h_{15} = 0,35$, resíduo bruto $e_{15} = 1,2$ e $QM_{Res} = 2,0$.")
        st.latex(r"e_{15} = 1,2, \quad h_{15} = 0,35, \quad \hat{\sigma} = \sqrt{2,0} \approx 1,414")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Passo 1: Calcular o denominador utilizando a raiz da variância ajustada pela alavancagem: $1,414 \cdot \sqrt{1 - 0,35}$.")
        st.markdown(r"- Passo 2: Dividir o resíduo bruto pelo valor encontrado: $1,2 / (1,414 \cdot 0,806) \approx 1,053$.")
        st.success(r"Conclusão: Com $r_{15} \approx 1,053$, o ponto encontra-se dentro da faixa de normalidade. O modelo é robusto para esta observação.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Avaliação de Pressuposições: Análise Gráfica de Homocedasticidade")
    
    # Introdução e Contextualização
    st.markdown(r"""
    A premissa da homocedasticidade estabelece que, em um modelo de regressão linear, o termo de erro deve possuir uma variância constante ao longo de todo o espaço de predição. Em termos práticos, isso significa que a incerteza associada às predições não deve ser influenciada pela magnitude dos valores previstos.
    """)
    
    st.markdown(r"""
    **Fundamentos da Estabilidade Estatística:**
    - **Eficiência:** Sob homocedasticidade, os estimadores de Mínimos Quadrados Ordinários (MQO) alcançam a propriedade de eficiência (Teorema de Gauss-Markov).
    - **Confiabilidade:** O erro padrão dos coeficientes permanece não viesado, permitindo testes de hipóteses e intervalos de confiança robustos.
    - **Risco:** A violação (heterocedasticidade) implica que diferentes observações possuem níveis distintos de 'ruído', invalidando inferências se ignorada.
    """)
    
    # O Coração Matemático
    st.markdown(r"### 📐 O Coração Matemático: Variância dos Resíduos")
    st.write(r"A relação entre a precisão da predição e os dados é expressa através da variância dos resíduos:")
    st.latex(r"Var(e_i | \hat{y}_i) \approx \sigma^2(1 - h_{ii})")
    
    st.write(r"Onde $h_{ii}$ representa a alavancagem (leverage) da observação. A derivação teórica segue o desvio da matriz de projeção:")
    st.latex(r"e = (I_n - H)y")
    st.latex(r"Var(e) = \sigma^2(I_n - H)")
    st.latex(r"Var(e_i) = \sigma^2(1 - h_{ii})")
    
    # Simulador Interativo
    st.markdown(r"### 🧪 Gerador de Padrões em Resíduos")
    col1, col2 = st.columns(2)
    with col1:
        k = st.slider(r"Nível de Heterocedasticidade ($k$)", 0.0, 2.0, 0.0, 0.1, key=r"k_subtopico_4")
    with col2:
        mostrar_regiao = st.toggle(r"Sombrear Região Crítica", value=False, key=r"toggle_subtopico_4")
    
    # Geração de dados para o simulador (hardcoded para demonstração)
    np.random.seed(42)
    n_samples = 100
    x = np.linspace(1, 10, n_samples)
    y_verdadeiro = 2 + 1.5 * x
    # Variância heterocedástica: sigma^2 * (1 + k*x)^2
    sigma = 0.5 * (1 + k * x)
    erros = np.random.normal(0, sigma)
    y = y_verdadeiro + erros
    
    # Regressão linear simples
    slope, intercept, _, _, _ = stats.linregress(x, y)
    y_ajustado = intercept + slope * x
    residuos = y - y_ajustado
    
    # Plotagem
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_ajustado, y=residuos, mode='markers', name=r"Resíduos", marker=dict(color=r"#0000FF")))
    
    if mostrar_regiao:
        fig.add_hrect(y0=-1.5*(1+k*5), y1=1.5*(1+k*5), fillcolor=r"#FF0000", opacity=0.1, line_width=0, name=r"Região de Dispersão")
    
    fig.update_layout(
        template=r"plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Análise Visual de Resíduos vs Ajustados</b>", font=dict(size=14, color=r"#1E293B", family=r"Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Valores Ajustados", font=dict(size=11, color=r"#1E293B", family=r"Arial, sans-serif")), tickfont=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Resíduos", font=dict(size=11, color=r"#1E293B", family=r"Arial, sans-serif")), tickfont=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        legend=dict(orientation=r"h", yanchor=r"bottom", y=1.02, xanchor=r"right", x=1.0, font=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), bgcolor=r"rgba(255, 255, 255, 0.8)", bordercolor=r"#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor=r"#FFFFFF", font_size=12, font_color=r"#1E293B", font_family=r"Arial, sans-serif")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_4")
    
    # Laudo Dinâmico
    if k > 0.5:
        st.info(r"O modelo apresenta heterocedasticidade severa. O padrão de 'funil' sugere que a variância dos erros cresce com o aumento dos valores previstos. Recomenda-se transformação logarítmica ou Mínimos Quadrados Ponderados (WLS).")
    else:
        st.success(r"Os resíduos apresentam comportamento aleatório em torno de zero, sugerindo que a pressuposição de homocedasticidade é mantida para o nível atual de variação.")
    
    # Casos de Aplicação Prática
    st.markdown(r"### 📈 Casos de Aplicação Prática: Eficiência Logística")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Logística de Cargas Pesadas")
        st.markdown(r"No estudo de eficiência logística, observamos um padrão de funil nos resíduos: dispersão pequena para cargas leves e alta para cargas pesadas.")
        st.latex(r"Var(e_i) \propto \hat{y}_i")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Identificação:** A variância do erro não é constante, demonstrando dependência da escala da resposta.")
        st.markdown(r"- **Correção:** Aplicar transformação logarítmica $log(y)$ ou utilizar Mínimos Quadrados Ponderados para estabilizar a variância.")
        st.success(r"O padrão detectado exige uma reestimação do modelo via logaritmo ou Mínimos Quadrados Ponderados, corrigindo a heterocedasticidade e restaurando a validade dos intervalos de confiança.")

    # Importação necessária para o simulador interno
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Testes de Normalidade e a Distribuição dos Resíduos")
    
    # Prosa Inicial
    st.markdown(r"""
    A validade das inferências estatísticas fundamentadas em modelos de regressão linear depende, de forma umbilical, da integridade das premissas probabilísticas assumidas sobre os erros do modelo. 
    A pressuposição de que os erros populacionais seguem uma distribuição normal é o que permite a transição do cálculo algébrico para a inferência estatística, viabilizando o cálculo de $p$-valor e a construção de intervalos de confiança rigorosos.
    """)
    
    st.info(r"Sem a normalidade, as distribuições de teste $t$ e $F$ deixam de ser exatas, tornando as conclusões sobre a significância dos parâmetros extremamente frágeis.")
    
    # O Coração Matemático
    st.markdown(r"### 📐 O Coração Matemático: Distribuição dos Resíduos")
    st.markdown(r"A relação fundamental que define a estrutura estocástica dos resíduos em um modelo de regressão linear é dada por:")
    
    st.latex(r"e \sim N_n(0, \sigma^2(I_n - H))")
    
    st.markdown(r"Este formalismo é derivado diretamente do modelo de regressão linear gaussiano:")
    st.latex(r"y \sim N_n(X\theta, \sigma^2 I_n)")
    st.markdown(r"Onde o vetor de resíduos é definido pela projeção no espaço ortogonal ao espaço das colunas de $X$:")
    st.latex(r"e = (I_n - H)y")
    st.markdown(r"Resultando, por propriedade linear, na distribuição:")
    st.latex(r"e \sim N_n(0, \sigma^2(I_n - H))")
    
    # Investigação Visual
    st.markdown(r"### 🔍 Diagnóstico e Investigação Visual")
    st.markdown(r"""
    A verificação da normalidade não deve ser um exercício burocrático, mas um processo investigativo. 
    - **Gráfico Quantil-Quantil (Q-Q plot):** É a ferramenta soberana. Permite identificar desvios sistemáticos nas caudas, como curtose excessiva.
    - **Teste de Shapiro-Wilk:** Útil, porém sensível a desvios triviais em amostras extensas.
    """)
    
    # Exemplos Práticos
    st.markdown(r"### 📈 Casos de Aplicação Prática: Avaliação de Resíduos")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Análise de Tempo de Montagem")
        st.markdown(r"Um modelo de tempo de montagem apresenta desvios no Q-Q plot: caudas que se afastam da reta diagonal.")
        st.latex(r"\text{Desvio observado: caudas pesadas}")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Comparação direta entre quantis teóricos da normal e os resíduos observados.")
        st.markdown(r"- Diagnóstico identificou curtose elevada nas extremidades da distribuição.")
        st.success(r"O modelo apresenta caudas pesadas. Recomenda-se cautela ou transformações estabilizadoras (ex: Box-Cox) para garantir a validade das inferências.")
    
    # Considerações Finais
    st.markdown(r"""
    Quando os resíduos apresentam caudas longas, o erro padrão da média calculado sob a premissa de normalidade pode ser artificialmente reduzido. 
    Isso eleva o risco de **Erro Tipo I**, onde o pesquisador rejeita a hipótese nula indevidamente, tratando ruído aleatório como um efeito estatisticamente significativo.
    """)
    
    # Conclusão Ética
    st.warning(r"O estatístico tem o dever de questionar a aderência dos dados. O modelo de regressão deve ser visto como uma representação iterativa, onde a análise de resíduos funciona como o filtro de qualidade final.")

    # Cabeçalho do subtópico
    st.header(r"Resíduos como Ferramenta de Detecção de Observações Influentes")
    
    # Introdução teórica com ritmo de leitura
    st.markdown(r"""
    As observações influentes possuem impacto desproporcional sobre as estimativas dos coeficientes de um modelo de regressão. Identificá-las é um passo crítico para garantir a robustez e a integridade das inferências estatísticas extraídas.
    """)
    
    st.markdown(r"""
    Para gerenciar esses pontos, utilizamos critérios que transcendem a análise de resíduos simples, focando em:
    - **Alavancagem (Leverage):** O quanto uma observação no espaço dos preditores pode forçar a reta de regressão a se aproximar de si mesma.
    - **Distância de Cook:** Uma medida integrada que avalia a variação nos parâmetros ao remover uma observação específica do conjunto de dados.
    - **Regressão Robusta:** A alternativa analítica para mitigar distorções quando pontos excepcionais não podem ser descartados, mas não devem enviesar a média.
    """)
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: A Distância de Cook")
    st.markdown(r"A Distância de Cook ($D_i$) é definida pela fórmula abaixo, que combina a variabilidade dos resíduos com a alavancagem horizontal:")
    st.latex(r"D_i = \frac{e_i^2}{p \cdot \frac{SQ_{Res}}{n - p}} \cdot \frac{h_{ii}}{(1 - h_{ii})^2}")
    
    st.markdown(r"Abaixo, detalhamos o fluxo dedutivo que conduz a esta métrica de influência:")
    st.latex(r"D_i = \frac{(\theta - \theta_{(i)})^T (X^TX) (\theta - \theta_{(i)})}{p \cdot \hat{\sigma}^2}")
    st.markdown(r"Onde a diferença entre o vetor de parâmetros original e o vetor após a exclusão do caso $i$ é expressa por:")
    st.latex(r"\theta - \theta_{(i)} = \frac{(X^TX)^{-1} x_i e_i}{1 - h_{ii}}")
    st.markdown(r"Resultando, após a simplificação algébrica, no indicador final de influência:")
    st.latex(r"D_i = \frac{e_i^2}{p \hat{\sigma}^2} \frac{h_{ii}}{(1 - h_{ii})^2}")
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática: Avaliação de Influência")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Estudo de Renda e Poupança")
        st.markdown(r"Em um modelo de regressão com $n=50$ observações e $p=2$ parâmetros, o caso 15 apresenta os seguintes valores diagnósticos: $h_{15}=0,40$, $e_{15}=2,0$ e $QM_{Res}=2,5$.")
        
        st.latex(r"D_{15} = \frac{2,0^2}{2 \cdot 2,5} \cdot \frac{0,40}{(1 - 0,40)^2}")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Primeiro, calculamos a razão do erro e a influência da alavancagem: $D_{15} = \frac{4}{5} \cdot \frac{0,40}{0,36}$")
        st.markdown(r"- Finalizando o cálculo: $D_{15} = 0,8 \cdot 1,111 \approx 0,888$")
        
        st.success(r"O valor de 0,888 é indicativo de alta influência. A observação 15 deve ser analisada detalhadamente, pois altera significativamente as estimativas do modelo, podendo ser uma fonte de erro ou um dado excepcional a ser tratado isoladamente.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDcgLSBUw7NwaWNvIDcuMTogRGlhZ27Ds3N0aWNvIGUgYm9uZGFkZSBkbyBhanVzdGU6IEFuw6FsaXNlIGRlIHJlc8OtZHVvcyIsICJxdWVzdG9lc19tdWx0aXBsYV9lc2NvbGhhIjogW3siZW51bmNpYWRvIjogIkVtIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvIGxpbmVhciBjbMOhc3NpY28sICR5ID0gWFx0aGV0YSArIFx0ZXh0e86UfSQsIG9uZGUgJFgkIMOpIHVtYSBtYXRyaXogZGUgY29uc3RhbnRlcyAkbiBcXHRpbWVzIHAkIGRlIHBvc3RvICRrJCwgdXRpbGl6YS1zZSBhIHByb2plw6fDo28gb3J0b2dvbmFsICRQID0gWChYJ1gpXnstfVgnJCBwYXJhIG9idGVyIGFzIHByZWRpw6fDtWVzICRcXGhhdHt5fSA9IFB5JC4gQ29uc2lkZXJhbmRvIG8gdmV0b3IgZGUgcmVzw61kdW9zICRcXGhhdHtlfSA9IChJIC0gUCl5JCwgcXVhbCBkYXMgc2VndWludGVzIHByb3ByaWVkYWRlcyBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgbyBjb21wb3J0YW1lbnRvIGdlb23DqXRyaWNvIGUgZXN0YXTDrXN0aWNvIGRlc3NlIHZldG9yIG5vIG1vZGVsbyBkZSBtw61uaW1vcyBxdWFkcmFkb3M/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIHZldG9yIGRlIHJlc8OtZHVvcyAkXFxoYXR7ZX0kIHBlcnRlbmNlIGFvIGVzcGHDp28gY29sdW5hIGRlICRYJCwgbG9nbyAkXFxoYXR7ZX0nWCA9IDAkLiIsICJCIjogIkEgbWF0cml6ICQoSSAtIFApJCDDqSBzaW3DqXRyaWNhIGUgaWRlbXBvdGVudGUsIHByb2pldGFuZG8gbyB2ZXRvciBkZSBvYnNlcnZhw6fDtWVzICR5JCBubyBlc3Bhw6dvIG9ydG9nb25hbCBhICRDKFgpJCwgdGFsIHF1ZSAkXFxoYXR7ZX0nXFxoYXR7eX0gPSAwJC4iLCAiQyI6ICJPIHZldG9yIGRlIHJlc8OtZHVvcyAkXFxoYXR7ZX0kIMOpIHNlbXByZSBpZGVudGljYW1lbnRlIG51bG8gcXVhbmRvIG8gbW9kZWxvIMOpIG1hbCBlc3BlY2lmaWNhZG8uIiwgIkQiOiAiQSBub3JtYSBhbyBxdWFkcmFkbyBkbyB2ZXRvciBkZSByZXPDrWR1b3MsICRcXHxcXGhhdHtlfVxcfF4yJCwgw6kgc2VtcHJlIGlndWFsIMOgIG5vcm1hIGFvIHF1YWRyYWRvIGRhcyBvYnNlcnZhw6fDtWVzIG9yaWdpbmFpcyAkXFx8eVxcfF4yJC4iLCAiRSI6ICJPIHZldG9yIGRlIHJlc8OtZHVvcyAkXFxoYXR7ZX0kIG7Do28gw6kgb3J0b2dvbmFsIGEgJFxcaGF0e3l9JCwgdW1hIHZleiBxdWUgYW1ib3MgZGVwZW5kZW0gZGEgbWVzbWEgbWF0cml6IGRlIHByb2plw6fDo28uIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgZGVjb21wb3Npw6fDo28gZG8gdmV0b3IgJHkkIGVtIGRvaXMgY29tcG9uZW50ZXMgb3J0b2dvbmFpczogdW0gbm8gZXNwYcOnbyBkbyBtb2RlbG8gKCRDKFgpJCkgZSBvdXRybyBubyBlc3Bhw6dvIGRvIHJlc8OtZHVvICgkQ157XFxwZXJwfShYKSQpLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBtYXRyaXogJChJIC0gUCkkIMOpLCBwb3IgZGVmaW5pw6fDo28sIG8gcHJvamV0b3Igb3J0b2dvbmFsIG5vIGVzcGHDp28gb3J0b2dvbmFsIGFvIGVzcGHDp28gY29sdW5hIGRlICRYJC4gQ29tbyAkUCQgw6kgdW0gcHJvamV0b3Igb3J0b2dvbmFsIGVtICRDKFgpJCwgZWxlIMOpIHNpbcOpdHJpY28gKCRQPVAnJCkgZSBpZGVtcG90ZW50ZSAoJFBeMj1QJCkuIENvbnNlcXVlbnRlbWVudGUsICQoSS1QKSQgdGFtYsOpbSDDqSBzaW3DqXRyaWNvIGUgaWRlbXBvdGVudGUuIFBlbGEgb3J0b2dvbmFsaWRhZGUgZG9zIHN1YmVzcGHDp29zLCBvIHByb2R1dG8gJFAoSS1QKSA9IFAgLSBQXjIgPSAwJCwgbyBxdWUgaW1wbGljYSBxdWUgcXVhbHF1ZXIgdmV0b3IgZW0gJEMoWCkkIMOpIG9ydG9nb25hbCBhIHF1YWxxdWVyIHZldG9yIGVtICRDXntcXHBlcnB9KFgpJCwgbG9nbyAkXFxoYXR7eX0nXFxoYXR7ZX0gPSAoUHkpJyhJLVApeSA9IHknUChJLVApeSA9IDAkLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3NoYXBlKHR5cGU9XCJsaW5lXCIsIHgwPTAsIHkwPTAsIHgxPTQsIHkxPTIsIGxpbmU9ZGljdChjb2xvcj1cIiMwMDAwRkZcIiwgd2lkdGg9MiksIG5hbWU9XCJTdWJlc3Bhw6dvIEMoWClcIilcbmZpZy5hZGRfc2hhcGUodHlwZT1cImxpbmVcIiwgeDA9MCwgeTA9MCwgeDE9MSwgeTE9LTIsIGxpbmU9ZGljdChjb2xvcj1cIiNGRjAwMDBcIiwgd2lkdGg9MiksIG5hbWU9XCJFc3Bhw6dvIFJlc2lkdWFsXCIpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMCwgNF0sIHk9WzAsIDJdLCBtb2RlPVwibGluZXNcIiwgbmFtZT1cIlByZWRpw6fDo28gKHlfaGF0KVwiLCBsaW5lPWRpY3QoY29sb3I9XCIjMDAwMEZGXCIpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVswLCAxXSwgeT1bMCwgLTJdLCBtb2RlPVwibGluZXNcIiwgbmFtZT1cIlJlc8OtZHVvIChlKVwiLCBsaW5lPWRpY3QoY29sb3I9XCIjRkYwMDAwXCIpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPVwiPGI+T3J0b2dvbmFsaWRhZGU6IFByb2plw6fDo28gZGUgUmVzw61kdW9zPC9iPlwiLCB0ZW1wbGF0ZT1cInBsb3RseV93aGl0ZVwiLCB4YXhpcz1kaWN0KGZpeGVkcmFuZ2U9VHJ1ZSksIHlheGlzPWRpY3QoZml4ZWRyYW5nZT1UcnVlKSkiLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgTW9kZWxvcyBMaW5lYXJlcywgQ2FwIDQsIHAuIDg1In0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSBlbnNhaW8gY2zDrW5pY28gb25kZSBhIHJlc3Bvc3RhICR5JCDDqSBtb2RlbGFkYSBwb3IgJHkgPSBYXFx0aGV0YSArIFxcdGV4dHvOlH0kLCBjb20gJFxcdGV4dHvOlH0gXFxzaW0gTigwLCBJXFxzaWdtYV4yKSQuIEFvIGFuYWxpc2FyIGEgcXVhbGlkYWRlIGRvIGFqdXN0ZSwgY2FsY3VsYS1zZSBvIHZldG9yIGRlIHJlc8OtZHVvcyAkXFxoYXR7ZX0gPSAoSSAtIFApeSQuIFF1YWwgw6kgbyB2YWxvciBlc3BlcmFkbyBkYSBzb21hIGRlIHF1YWRyYWRvcyBkb3MgcmVzw61kdW9zICRTUV97UmVzfSA9IFxcaGF0e2V9J1xcaGF0e2V9JD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIiRcXHNpZ21hXjIkIiwgIkIiOiAiJG5cXHNpZ21hXjIkIiwgIkMiOiAiJChuIC0gaylcXHNpZ21hXjIkLCBvbmRlICRrJCDDqSBvIHBvc3RvIGRhIG1hdHJpeiAkWCQuIiwgIkQiOiAiJGtcXHNpZ21hXjIkIiwgIkUiOiAiWmVybywgcG9pcyBvcyByZXPDrWR1b3MgZGV2ZW0gc29tYXIgemVybyBubyBtb2RlbG8gbGluZWFyLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiVXNlIGEgcHJvcHJpZWRhZGUgZGEgZXNwZXJhbsOnYSBkZSBmb3JtYXMgcXVhZHLDoXRpY2FzOiAkRVt5J0F5XSA9IFRyKEFWKSArIFxcbXUnQVxcbXUkLiBBcXVpICRBID0gKEktUCkkLCAkViA9IElcXHNpZ21hXjIkIGUgJFxcbXUgPSBYXFx0aGV0YSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQZWxvIHRlb3JlbWEgZGUgZXNwZXJhbsOnYSBkZSBmb3JtYXMgcXVhZHLDoXRpY2FzLCAkRVtcXGhhdHtlfSdcXGhhdHtlfV0gPSBFW3knKEktUCl5XSA9IFRyKChJLVApSVxcc2lnbWFeMikgKyBcXHRoZXRhJ1gnKEktUClYXFx0aGV0YSQuIENvbW8gJChJLVApWCA9IFggLSBQWCA9IFggLSBYID0gMCQsIG8gdGVybW8gZGUgdmnDqXMgZGVzYXBhcmVjZS4gUmVzdGEgJFxcc2lnbWFeMiBUcihJLVApID0gXFxzaWdtYV4yKFRyKEkpIC0gVHIoUCkpID0gXFxzaWdtYV4yKG4gLSBrKSQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgTW9kZWxvcyBMaW5lYXJlcywgQ2FwIDMsIHAuIDcwIn0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBkZSBlbmdlbmhhcmlhIHBhcmEgbW9kZWxhciBhIHJlc2lzdMOqbmNpYSBkZSBwb2zDrW1lcm9zIGVtIGZ1bsOnw6NvIGRhIHRlbXBlcmF0dXJhLCB2b2PDqiB1dGlsaXphIHVtYSBtYXRyaXogZGUgZGVsaW5lYW1lbnRvICRYJCBkZSBkaW1lbnPDo28gJG4gXFx0aW1lcyAyJCAob25kZSAkaz0yJCkuIEFvIGFwbGljYXIgbyBtb2RlbG8gbGluZWFyICR5ID0gWFxcdGhldGEgKyBcXERlbHRhJCwgdm9jw6ogb2J0w6ltIGEgbWF0cml6IGRlIHByb2plw6fDo28gJFAgPSBYKFgnWCleey0xfVgnJC4gQ29uc2lkZXJlIHVtIHZldG9yIGRlIG9ic2VydmHDp8O1ZXMgJHkkIHF1ZSBuw6NvIHBlcnRlbmNlIGFvIGVzcGHDp28gY29sdW5hIGRlICRYJCwgZGVub3RhZG8gY29tbyAkXFxHYW1tYShYKSQuIFF1YWwgZGFzIGFmaXJtYcOnw7VlcyBhYmFpeG8gZGVzY3JldmUgY29ycmV0YW1lbnRlIGEgbmF0dXJlemEgZ2VvbcOpdHJpY2EgZG8gdmV0b3IgZGUgcmVzw61kdW9zICRlID0gKElfbiAtIFApeSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIHZldG9yIGRlIHJlc8OtZHVvcyAkZSQgcmVzaWRlIG5vIHN1YmVzcGHDp28gJFxcR2FtbWEoWCkkLCBzZW5kbyBhIHByb2plw6fDo28gb3J0b2dvbmFsIGRlICR5JCBzb2JyZSBvIG1vZGVsby4iLCAiQiI6ICJPIHZldG9yIGRlIHJlc8OtZHVvcyAkZSQgw6kgYSBkaXN0w6JuY2lhIHBlcnBlbmRpY3VsYXIgZW50cmUgbyB2ZXRvciAkeSQgZSBvIHN1YmVzcGHDp28gJFxcR2FtbWEoWCkkLCBwb3NzdWluZG8gYSBwcm9wcmllZGFkZSBkZSBzZXIgb3J0b2dvbmFsIGEgdG9kYXMgYXMgY29sdW5hcyBkZSAkWCQuIiwgIkMiOiAiTyB2ZXRvciBkZSByZXPDrWR1b3MgJGUkIMOpIGludmFyaWFudGUgw6AgdHJhbnNmb3JtYcOnw6NvIGRhIG1hdHJpeiAkUCQsIHBvaXMgJChJX24gLSBQKVAgPSBQJC4iLCAiRCI6ICJPIHZldG9yIGRlIHJlc8OtZHVvcyAkZSQgcG9zc3VpIGRpbWVuc8OjbyAkbiBcXHRpbWVzIGskIGUgcmVwcmVzZW50YSBhIHZhcmnDom5jaWEgc2lzdGVtw6F0aWNhIG7Do28gY2FwdHVyYWRhIHBlbG8gbW9kZWxvLiIsICJFIjogIkEgbWF0cml6ICQoSV9uIC0gUCkkIG7Do28gw6kgaWRlbXBvdGVudGUsIG8gcXVlIGltcGVkZSBxdWUgbyByZXPDrWR1byBzZWphIHVtYSBwcm9qZcOnw6NvIG9ydG9nb25hbCB2w6FsaWRhIG5vIGVzcGHDp28gJFxcR2FtbWEoWClee1xccGVycH0kLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBvIHJlc8OtZHVvIHJlcHJlc2VudGEgYSBwYXJ0ZSBkZSAkeSQgcXVlICdzb2Jyb3UnIGFww7NzIHN1YnRyYWlybW9zIGEgcHJvamXDp8OjbyBkbyBkYWRvIG5vIGVzcGHDp28gZG8gbW9kZWxvLiBDb21vIHNlIHJlbGFjaW9uYSBhIG9ydG9nb25hbGlkYWRlIGNvbSBhIG1pbmltaXphw6fDo28gZGUgZGlzdMOibmNpYT8iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgbWF0cml6ICRQJCBwcm9qZXRhICR5JCBlbSAkXFxHYW1tYShYKSQsIHJlc3VsdGFuZG8gZW0gJFxcaGF0e3l9ID0gUHkkLiBPIHJlc8OtZHVvICRlID0geSAtIFxcaGF0e3l9ID0gKElfbiAtIFApeSQgw6ksIHBvciBkZWZpbmnDp8OjbyBnZW9tw6l0cmljYSwgYSBjb21wb25lbnRlIGRlICR5JCBxdWUgcmVzaWRlIG5vIGVzcGHDp28gb3J0b2dvbmFsIGFvIG1vZGVsbywgb3Ugc2VqYSwgJFxcR2FtbWEoWClee1xccGVycH0kLiBQb3Igc2VyIHVtYSBwcm9qZcOnw6NvIG9ydG9nb25hbCwgbyB2ZXRvciBkZSByZXPDrWR1b3MgJGUkIGRldmUgc2F0aXNmYXplciAkWCdlID0gMCQsIHNpZ25pZmljYW5kbyBxdWUgZWxlIMOpIHBlcnBlbmRpY3VsYXIgYSB0b2RhcyBhcyBjb2x1bmFzIGRhIG1hdHJpeiBkZSBkZWxpbmVhbWVudG8gJFgkLiBBcyBvdXRyYXMgYWx0ZXJuYXRpdmFzIGVzdMOjbyBpbmNvcnJldGFzOiAkZSQgbsOjbyBlc3TDoSBlbSAkXFxHYW1tYShYKSQsICQoSV9uIC0gUCkkIMOpIHNpbcOpdHJpY2EgZSBpZGVtcG90ZW50ZSwgZSBvIHJlc8OtZHVvIMOpIHVtIHZldG9yICRuIFxcdGltZXMgMSQuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVswLCAzXSwgeT1bMCwgMF0sIG1vZGU9J2xpbmVzJywgbmFtZT0nRXNwYcOnbyBNb2RlbG8gKM6TKFgpKScsIGxpbmU9ZGljdChjb2xvcj0nIzAwMDBGRicsIHdpZHRoPTQpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVsyLCAyXSwgeT1bMCwgMl0sIG1vZGU9J2xpbmVzJywgbmFtZT0nUmVzw61kdW8gKGUpJywgbGluZT1kaWN0KGNvbG9yPScjRkYwMDAwJywgd2lkdGg9MywgZGFzaD0nZGFzaCcpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVsyXSwgeT1bMl0sIG1vZGU9J21hcmtlcnMnLCBuYW1lPSdWZXRvciB5JywgbWFya2VyPWRpY3Qoc2l6ZT0xMiwgY29sb3I9JyMxRTI5M0InKSkpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bMl0sIHk9WzBdLCBtb2RlPSdtYXJrZXJzJywgbmFtZT0nUHJldmlzw6NvICjFtyknLCBtYXJrZXI9ZGljdChzaXplPTEyLCBjb2xvcj0nIzgwODA4MCcpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5HZW9tZXRyaWEgZGEgUHJvamXDp8OjbyBPcnRvZ29uYWw8L2I+JywgeGF4aXM9ZGljdChyYW5nZT1bLTEsIDRdLCBmaXhlZHJhbmdlPVRydWUpLCB5YXhpcz1kaWN0KHJhbmdlPVstMSwgM10sIGZpeGVkcmFuZ2U9VHJ1ZSksIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtIGFuYWxpc3RhIGRlIGRhZG9zIGRlIElvVCBlc3TDoSB2YWxpZGFuZG8gYSBlZmljw6FjaWEgZGUgdW0gc2Vuc29yIHV0aWxpemFuZG8gcmVncmVzc8OjbyBsaW5lYXIuIEVsZSBvYnNlcnZhIHF1ZSBhIG1hdHJpeiBkZSBwcm9qZcOnw6NvICRQJCB0ZW0gYSBwcm9wcmllZGFkZSBkZSBpZGVtcG90w6puY2lhLCBvdSBzZWphLCAkUF4yID0gUCQuIFNlIG8gYW5hbGlzdGEgZGVjaWRpciBhcGxpY2FyIGEgcHJvamXDp8OjbyAkUCQgZHVhcyB2ZXplcyBjb25zZWN1dGl2YXMgc29icmUgbyB2ZXRvciBkZSBkYWRvcyAkeSQgKG91IHNlamEsICRcXGhhdHt5fV4qID0gUChQeSkkKSwgbyBxdWUgb2NvcnJlcsOhIGNvbSBvIHZldG9yIGRlIHByZXZpc8O1ZXMgcmVzdWx0YW50ZT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gdmV0b3IgZGUgcHJldmlzw7VlcyBzZXLDoSByZWR1emlkbyBwb3IgdW0gZmF0b3IgZGUgZXNjYWxhIGlndWFsIGFvIHBvc3RvIGRhIG1hdHJpeiAkcmFuayhYKSQuIiwgIkIiOiAiTyB2ZXRvciBkZSBwcmV2aXPDtWVzIHNlIHRvcm5hcsOhIHVtIHZldG9yIG51bG8sIHBvaXMgYSBwcm9qZcOnw6NvIHN1YnNlcXVlbnRlIHJlbW92ZSB0b2RhIGEgaW5mb3JtYcOnw6NvLiIsICJDIjogIk8gdmV0b3IgZGUgcHJldmlzw7VlcyByZXN1bHRhbnRlIHBlcm1hbmVjZXLDoSBpbmFsdGVyYWRvLCBwb2lzICRcXGhhdHt5fV4qID0gXFxoYXR7eX0kLCByZWZsZXRpbmRvIHF1ZSBvcyBkYWRvcyBqw6EgcmVzaWRlbSBubyBlc3Bhw6dvIGRvIG1vZGVsbyBhcMOzcyBhIHByaW1laXJhIHByb2plw6fDo28uIiwgIkQiOiAiTyB2ZXRvciBkZSBwcmV2aXPDtWVzIHNlcsOhIHRyYW5zZm9ybWFkbyBlbSB1bWEgbWF0cml6LCBhbHRlcmFuZG8gYSBkaW1lbnPDo28gb3JpZ2luYWwgZG8gZXNwYcOnbyBkZSBidXNjYS4iLCAiRSI6ICJPIHZldG9yIGRlIHByZXZpc8O1ZXMgcGFzc2Fyw6EgYSByZXNpZGlyIG5vIGVzcGHDp28gJFxcR2FtbWEoWClee1xccGVycH0kLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiUGVuc2Ugbm8gc2lnbmlmaWNhZG8gZsOtc2ljbyBkZSAncHJvamV0YXInIGFsZ28gcXVlIGrDoSBlc3TDoSBubyAnY2jDo28nIChvIHN1YmVzcGHDp28gZG8gbW9kZWxvKS4gQSBpZGVtcG90w6puY2lhIMOpIGEgdHJhZHXDp8OjbyBhbGfDqWJyaWNhIGRlc3RlIGNvbmNlaXRvLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBwcm9wcmllZGFkZSBmdW5kYW1lbnRhbCBkZSB1bWEgbWF0cml6IGRlIHByb2plw6fDo28gw6kgc3VhIGlkZW1wb3TDqm5jaWEgKCRQXjIgPSBQJCkuIFF1YW5kbyBjYWxjdWxhbW9zICRQeSQsIHByb2pldGFtb3MgJHkkIG5vIGVzcGHDp28gJFxcR2FtbWEoWCkkLiBTZSBhcGxpY2FybW9zIGEgcHJvamXDp8OjbyBub3ZhbWVudGUsICRQKFB5KSA9IFBeMnkgPSBQeSQuIElzc28gZGVtb25zdHJhIHF1ZSwgdW1hIHZleiBxdWUgbyBkYWRvIMOpIHByb2pldGFkbyBubyBzdWJlc3Bhw6dvIGRlZmluaWRvIHBlbG8gbW9kZWxvLCBlbGUgasOhIGVzdMOhIGNvbnRpZG8gbmVsZSwgZSBwcm9qZcOnw7VlcyBhZGljaW9uYWlzIG7Do28gYWx0ZXJhbSBvIHJlc3VsdGFkby4gSXNzbyBnYXJhbnRlIGEgY29uc2lzdMOqbmNpYSBkbyBvcGVyYWRvciBkZSBwcm9qZcOnw6NvLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIG3Dumx0aXBsYSwgbyBkaWFnbsOzc3RpY28gZGUgcmVzw61kdW9zIMOpIGZ1bmRhbWVudGFsIHBhcmEgdmFsaWRhciBhcyBwcmVtaXNzYXMgZGUgR2F1c3MtTWFya292LiBDb25zaWRlcmUgcXVlIG9ic2VydmFtb3MgcG9udG9zIGNvbSBhbHRhIGFsYXZhbmNhZ2VtICgkaF97aWl9JCBlbGV2YWRvKS4gU29icmUgYSBuZWNlc3NpZGFkZSBkZSB1dGlsaXphciByZXPDrWR1b3Mgc3R1ZGVudGl6YWRvcyAoJHJfaSQgb3UgJHRfaSQpIGVtIHZleiBkZSByZXPDrWR1b3MgYnJ1dG9zICgkZV9pJCksIGFzc2luYWxlIGEgYWx0ZXJuYXRpdmEgY29ycmV0YToiLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIlJlc8OtZHVvcyBicnV0b3Mgc8OjbyBzZW1wcmUgcHJlZmVyw612ZWlzIHBvaXMgcmVmbGV0ZW0gYSB1bmlkYWRlIG9yaWdpbmFsIGRhIHZhcmnDoXZlbCByZXNwb3N0YSwgZW5xdWFudG8gYSBzdHVkZW50aXphw6fDo28gaW50cm9kdXogZGlzdG9yw6fDtWVzIGVzdGF0w61zdGljYXMgZGVzbmVjZXNzw6FyaWFzLiIsICJCIjogIkEgc3R1ZGVudGl6YcOnw6NvIMOpIG5lY2Vzc8OhcmlhIHBvcnF1ZSBhIHZhcmnDom5jaWEgZG8gcmVzw61kdW8gJGVfaSQgw6kgY29uc3RhbnRlIGVtIHRvZG8gbyBjb25qdW50byBkZSBkYWRvcywgbWFzIGEgbcOpZGlhIG7Do28gw6kgY2VudHJhZGEgZW0gemVybywgbyBxdWUgcmVxdWVyIGFqdXN0ZSBwZWxhIGFsYXZhbmNhZ2VtLiIsICJDIjogIkVtIHJlZ2nDtWVzIGRlIGFsdGEgYWxhdmFuY2FnZW0sIG8gbW9kZWxvIMOpICdmb3LDp2FkbycgYSBzZSBhanVzdGFyIGFvcyBkYWRvcywgcmVzdWx0YW5kbyBlbSByZXPDrWR1b3MgYnJ1dG9zIGNvbSB2YXJpw6JuY2lhIHNpc3RlbWF0aWNhbWVudGUgbWVub3IgKCR2YXIoZV9pKSA9IFx0ZXh0e2NvbnN0YW50ZX0gXHRpbWVzICgxIC0gaF97aWl9KSQpLCBvIHF1ZSBtYXNjYXJhIGEgcHJlc2Vuw6dhIGRlIG91dGxpZXJzLiIsICJEIjogIk9zIHJlc8OtZHVvcyBwYWRyb25pemFkb3MgJHpfaSQgasOhIGNvcnJpZ2VtIHRvdGFsbWVudGUgbyBwcm9ibGVtYSBkYSBoZXRlcm9jZWRhc3RpY2lkYWRlIGVzdHJ1dHVyYWwgZGEgbWF0cml6IGRlIHByb2plw6fDo28gJEgkLCB0b3JuYW5kbyBvcyByZXPDrWR1b3Mgc3R1ZGVudGl6YWRvcyByZWR1bmRhbnRlcyBlbSBxdWFscXVlciBhbW9zdHJhLiIsICJFIjogIkEgc3R1ZGVudGl6YcOnw6NvIGV4dGVybmEgKCR0X2kkKSBkZXZlIHNlciBldml0YWRhIHNlbXByZSBxdWUgJG4gPiBwKzEkLCBwb2lzIGEgZXN0aW1hdGl2YSAkXFxoYXR7XFxzaWdtYX1feyhpKX0kIHRvcm5hLXNlIG51bWVyaWNhbWVudGUgaW5zdMOhdmVsIGUgY29udmVyZ2VudGUgYSB6ZXJvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGdlb21ldHJpYSBkYSBtYXRyaXogZGUgcHJvamXDp8OjbyAkSCQgZSBkZSBjb21vIGEgdmFyacOibmNpYSBkbyByZXPDrWR1byBkZXBlbmRlIGRvIGVsZW1lbnRvIGRpYWdvbmFsICRoX3tpaX0kLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBhbHRlcm5hdGl2YSBjb3JyZXRhIMOpIGEgQy4gU29iIGFzIHByZW1pc3NhcyBjbMOhc3NpY2FzLCBhIHZhcmnDom5jaWEgZG8gcmVzw61kdW8gw6kgJHZhcihlX2kpID0gXHRleHR7Y29uc3RhbnRlfSBcdGltZXMgKDEgLSBoX3tpaX0pJC4gQ29tbyAkaF97aWl9JCB2YXJpYSBlbnRyZSAkMS9uJCBlICQxJCwgcG9udG9zIGNvbSBhbGF2YW5jYWdlbSBhbHRhICgkaF97aWl9IFx0byAxJCkgZm9yw6dhbSBvIG1vZGVsbyBhIHBhc3NhciBwcsOzeGltbyBhbyBwb250bywgcmVzdWx0YW5kbyBlbSB1bSByZXPDrWR1byAkZV9pJCBhcnRpZmljaWFsbWVudGUgcGVxdWVuby4gSXNzbyBlc2NvbmRlIHBvdGVuY2lhaXMgb3V0bGllcnMsIHBvaXMgbyByZXPDrWR1byBicnV0byBzdWJlc3RpbWEgbyBlcnJvIGNvbWV0aWRvIHBlbG8gbW9kZWxvLiBBIHN0dWRlbnRpemHDp8OjbyBkaXZpZGUgbyByZXPDrWR1byBwZWxvIGZhdG9yICRcXHNxcnR7MSAtIGhfe2lpfX0kLCBjb3JyaWdpbmRvIGVzc2EgZGlzcGFyaWRhZGUuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgwLCAxLCAxMDApXG55X3JhdyA9IG5wLnNxcnQoMSAtIHgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXlfcmF3LCBtb2RlPSdsaW5lcycsIG5hbWU9cidGYXRvciBkZSBFc2NhbGEgJFxcc3FydHsxLWhfe2lpfX0kJywgbGluZT1kaWN0KGNvbG9yPScjMDAwMEZGJywgd2lkdGg9MykpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0VmZWl0byBkYSBBbGF2YW5jYWdlbSBuYSBWYXJpYWJpbGlkYWRlIGRvIFJlc8OtZHVvJywgeGF4aXNfdGl0bGU9J0FsYXZhbmNhZ2VtICgkaF97aWl9JCknLCB5YXhpc190aXRsZT0nRmF0b3IgZGUgQWp1c3RlJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiRmFyYXdheSwgSi4gSi4sIExpbmVhciBNb2RlbHMgd2l0aCBSLCBDYXAgNywgcC4gNzMifSwgeyJlbnVuY2lhZG8iOiAiQW8gcmVhbGl6YXIgdW1hIGFuw6FsaXNlIGRlIHJlc8OtZHVvcywgdW0gYW5hbGlzdGEgZGUgZGFkb3MgdXRpbGl6YSByZXPDrWR1b3Mgc3R1ZGVudGl6YWRvcyBleHRlcm5vcyAoJHRfaSQpIHBhcmEgcmVhbGl6YXIgdW0gdGVzdGUgZGUgZGV0ZWPDp8OjbyBkZSBvdXRsaWVycy4gUXVhbCDDqSBhIHByaW5jaXBhbCB2YW50YWdlbSB0ZcOzcmljYSBkbyB1c28gZGUgJHRfaSQgZW0gcmVsYcOnw6NvIGFvcyByZXPDrWR1b3Mgc3R1ZGVudGl6YWRvcyBpbnRlcm5vcyAoJHJfaSQpIG5vIGNvbnRleHRvIGRlIHRlc3RlIGRlIGhpcMOzdGVzZXM/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPcyByZXPDrWR1b3MgJHRfaSQgc2VndWVtIGV4YXRhbWVudGUgdW1hIGRpc3RyaWJ1acOnw6NvICROKDAsIDEpJCwgZmFjaWxpdGFuZG8gbyBjw6FsY3VsbyBkZSBwLXZhbG9yZXMgc2VtIG5lY2Vzc2lkYWRlIGRlIGdyYXVzIGRlIGxpYmVyZGFkZS4iLCAiQiI6ICJPcyByZXPDrWR1b3MgJHRfaSQgZWxpbWluYW0gYSBpbmZsdcOqbmNpYSBkZSBvYnNlcnZhw6fDtWVzIGluZmx1ZW50ZXMsIGdhcmFudGluZG8gcXVlIG8gbW9kZWxvIG51bmNhIHNlIGRlc3ZpZSBkYSByZXRhIGRlIG3DrW5pbW9zIHF1YWRyYWRvcyBvcmlnaW5hbC4iLCAiQyI6ICJPcyByZXPDrWR1b3MgJHRfaSQgcG9zc3VlbSB1bWEgZGlzdHJpYnVpw6fDo28gJHQkIGRlIFN0dWRlbnQgY29tICRuIC0gcCAtIDEkIGdyYXVzIGRlIGxpYmVyZGFkZSwgcG9pcyBvIGVycm8gw6kgZXN0aW1hZG8gZXhjbHVpbmRvIGEgb2JzZXJ2YcOnw6NvICRpJCwgdG9ybmFuZG8gbyB0ZXN0ZSBmb3JtYWxtZW50ZSBjb3JyZXRvIHBhcmEgaWRlbnRpZmljYXIgb3V0bGllcnMuIiwgIkQiOiAiT3MgcmVzw61kdW9zICR0X2kkIHPDo28gY2FsY3VsYWRvcyBjb20gYSB2YXJpw6JuY2lhIHBvcHVsYWNpb25hbCAkXFxzaWdtYV4yJCBjb25oZWNpZGEsIG8gcXVlIG9zIHRvcm5hIG11aXRvIG1haXMgcHJlY2lzb3MgZG8gcXVlIHF1YWxxdWVyIGVzdGltYXRpdmEgYW1vc3RyYWwuIiwgIkUiOiAiTsOjbyBow6EgZGlmZXJlbsOnYSB0ZcOzcmljYSwgc2VuZG8gJHRfaSQgYXBlbmFzIHVtIG5vbWUgYWx0ZXJuYXRpdm8gcGFyYSAkcl9pJCB1dGlsaXphZG8gZW0gc29mdHdhcmVzIGRpZmVyZW50ZXMuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJQZW5zZSBubyBjb25jZWl0byBkZSAnamFja2tuaWZlJyBvdSAnZGVpeGFyIHVtYSBvYnNlcnZhw6fDo28gZGUgZm9yYScgcGFyYSBlc3RpbWFyIGEgdmFyaWFiaWxpZGFkZSBzZW0gY29udGFtaW5hw6fDo28gcGVsbyBwb250byBzb2IgdGVzdGUuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGFsdGVybmF0aXZhIEMgw6kgYSBjb3JyZXRhLiBBbyBjYWxjdWxhciByZXPDrWR1b3Mgc3R1ZGVudGl6YWRvcyBleHRlcm5vcyAob3UgSmFja2tuaWZlKSwgdXRpbGl6YW1vcyAkXFxoYXR7XFxzaWdtYX1feyhpKX0kLCBxdWUgw6kgYSBlc3RpbWF0aXZhIGRvIGRlc3ZpbyBwYWRyw6NvIGRvIGVycm8gb21pdGluZG8gYSAkaSQtw6lzaW1hIG9ic2VydmHDp8Ojby4gQ29tbyBlc3NhIG9ic2VydmHDp8OjbyBuw6NvIGNvbnRhbWluYSBhIGVzdGltYXRpdmEgZG8gcGFyw6JtZXRybyBkZSBkaXNwZXJzw6NvLCBhIGVzdGF0w61zdGljYSAkdF9pJCBzZWd1ZSBleGF0YW1lbnRlIGEgZGlzdHJpYnVpw6fDo28gJHQkIGRlIFN0dWRlbnQsIHBlcm1pdGluZG8gdW0gdGVzdGUgZGUgc2lnbmlmaWPDom5jaWEgcmlnb3Jvc28gcGFyYSBvdXRsaWVycywgbyBxdWUgbsOjbyDDqSBwZXJmZWl0YW1lbnRlIGFsY2Fuw6dhZG8gcGVsb3MgcmVzw61kdW9zIGludGVybm9zICRyX2kkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiRmFyYXdheSwgSi4gSi4sIExpbmVhciBNb2RlbHMgd2l0aCBSLCBDYXAgNywgcC4gNzUifSwgeyJlbnVuY2lhZG8iOiAiVW0gYW5hbGlzdGEgZGUgZGFkb3MgZW0gdW1hIGVtcHJlc2EgZGUgbG9nw61zdGljYSBtb2RlbG91IG8gdGVtcG8gZGUgZW50cmVnYSBkZSBtZXJjYWRvcmlhcyAoJHkkLCBlbSBob3JhcykgZW0gZnVuw6fDo28gZGEgZGlzdMOibmNpYSBwZXJjb3JyaWRhICgkeCQsIGVtIGttKSB1dGlsaXphbmRvIHVtYSByZWdyZXNzw6NvIGxpbmVhciBzaW1wbGVzLiBBcMOzcyBhanVzdGFyIG8gbW9kZWxvLCBlbGUgZ2Vyb3UgbyBncsOhZmljbyBkZSByZXPDrWR1b3MgKCRcXGhhdHtlfV9pJCkgY29udHJhIG9zIHZhbG9yZXMgYWp1c3RhZG9zICgkXFxoYXR7eX1faSQpIHBhcmEgdmVyaWZpY2FyIGFzIHByZW1pc3NhcyBkZSBHYXVzcy1NYXJrb3YuIE8gZ3LDoWZpY28gcmVzdWx0YW50ZSBhcHJlc2VudGEgdW1hIGRpc3BlcnPDo28gcXVlIHNlIGFsYXJnYSBzaXN0ZW1hdGljYW1lbnRlIMOgIG1lZGlkYSBxdWUgb3MgdmFsb3JlcyBkZSAkXFxoYXR7eX1faSQgYXVtZW50YW0sIGFzc2VtZWxoYW5kby1zZSBhIHVtIGZvcm1hdG8gZGUgZnVuaWwuIENvbSBiYXNlIG5lc3RhIGV2aWTDqm5jaWEgdmlzdWFsLCBxdWFsIMOpIGEgaW50ZXJwcmV0YcOnw6NvIGVzdGF0w61zdGljYSBjb3JyZXRhIHNvYnJlIG8gZmVuw7RtZW5vIG9ic2VydmFkbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gbW9kZWxvIGFwcmVzZW50YSBob21vY2VkYXN0aWNpZGFkZSwgcG9pcyBhIGRpc3BlcnPDo28gw6kgc2ltw6l0cmljYSBlbSB0b3JubyBkZSB6ZXJvLiIsICJCIjogIk8gbW9kZWxvIHNvZnJlIGRlIGhldGVyb2NlZGFzdGljaWRhZGUsIGluZGljYW5kbyBxdWUgJFZhcihcXERlbHRhKSA9IFxcc2lnbWFeMiBJJCBuw6NvIMOpIGF0ZW5kaWRhLiIsICJDIjogIk8gbW9kZWxvIGFwcmVzZW50YSB1bSBlcnJvIGRlIGVzcGVjaWZpY2HDp8OjbyBlc3RydXR1cmFsIHNldmVybywgc3VnZXJpbmRvIHF1ZSBhIHJlbGHDp8OjbyBlbnRyZSAkeSQgZSAkeCQgw6kgbmVjZXNzYXJpYW1lbnRlIHF1YWRyw6F0aWNhLiIsICJEIjogIk9zIHJlc8OtZHVvcyBleGliZW0gYXV0b2NvcnJlbGHDp8OjbyBzZXJpYWwsIHZpc3RvIHF1ZSBhIHZhcmlhYmlsaWRhZGUgYXVtZW50YSBlbSBmdW7Dp8OjbyBkYSBkaXN0w6JuY2lhLiIsICJFIjogIk8gbW9kZWxvIMOpIHJvYnVzdG8gZSBvcyBlcnJvcyBwYWRyw6NvIGVzdGltYWRvcyBzw6NvIGNvbmZpw6F2ZWlzIHBhcmEgcXVhbHF1ZXIgbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGRlZmluacOnw6NvIGRlIGhvbW9jZWRhc3RpY2lkYWRlLiBPIHF1ZSBhY29udGVjZSBjb20gYSB2YXJpw6JuY2lhIGRvIHJ1w61kbyBxdWFuZG8gb2JzZXJ2YW1vcyBwYWRyw7VlcyBjb21vICdmdW5pcycgbm8gZ3LDoWZpY28gZGUgcmVzw61kdW9zIHZzLiB2YWxvcmVzIGFqdXN0YWRvcz8iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgcHJlbWlzc2EgZnVuZGFtZW50YWwgZGEgaG9tb2NlZGFzdGljaWRhZGUgZXhpZ2UgcXVlIGEgdmFyacOibmNpYSBkb3MgZXJyb3MgKCRcXERlbHRhJCkgc2VqYSBjb25zdGFudGUsIG91IHNlamEsICRWYXIoXFxEZWx0YSkgPSBcXHNpZ21hXjIgSSQuIE8gZ3LDoWZpY28gZGUgcmVzw61kdW9zICRcXGhhdHtlfV9pJCB2ZXJzdXMgdmFsb3JlcyBhanVzdGFkb3MgJFxcaGF0e3l9X2kkIMOpIGEgZmVycmFtZW50YSBkZSBkaWFnbsOzc3RpY28gcGFyYSBpc3NvLiBVbSBwYWRyw6NvIGVtICdmdW5pbCcgaW5kaWNhIHF1ZSBhIHZhcmlhYmlsaWRhZGUgZG9zIHJlc8OtZHVvcyBjcmVzY2UgY29uZm9ybWUgJFxcaGF0e3l9X2kkIGF1bWVudGEsIG8gcXVlIGNhcmFjdGVyaXphIGEgaGV0ZXJvY2VkYXN0aWNpZGFkZS4gQ29uc2VxdWVudGVtZW50ZSwgYSB2YXJpw6JuY2lhIG7Do28gw6kgY29uc3RhbnRlIGVtIHJlbGHDp8OjbyBhb3MgdmFsb3JlcyBwcmV2aXN0b3MsIGludmFsaWRhbmRvIGEgcHJlbWlzc2EgZGUgR2F1c3MtTWFya292IGUgY29tcHJvbWV0ZW5kbyBhIHByZWNpc8OjbyBkYXMgaW5mZXLDqm5jaWFzIChjb21vIGludGVydmFsb3MgZGUgY29uZmlhbsOnYSBlIHRlc3RlcyAkdCQgZG9zIGNvZWZpY2llbnRlcykuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PVsxMCwgMjAsIDMwLCA0MCwgNTAsIDYwLCA3MCwgODBdLCB5PVsxLCAtMSwgMiwgLTIsIDQsIC00LCA2LCAtNl0sIG1vZGU9J21hcmtlcnMnLCBuYW1lPSdSZXPDrWR1b3MnKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdHcsOhZmljbyBkZSBSZXPDrWR1b3MgdnMuIEFqdXN0YWRvcyAoUGFkcsOjbyBGdW5pbCknLCB4YXhpc190aXRsZT0nVmFsb3JlcyBBanVzdGFkb3MgKCRcXGhhdHt5fV9pJCknLCB5YXhpc190aXRsZT0nUmVzw61kdW9zICgkXFxoYXR7ZX1faSQpJywgdGVtcGxhdGU9J3Bsb3RseV93aGl0ZScpXG5maWcuYWRkX2hsaW5lKHk9MCwgbGluZV9kYXNoPSdkYXNoJywgbGluZV9jb2xvcj0nIzAwMDBGRicpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiRmFyYXdheSwgSi4gSi4sIExpbmVhciBNb2RlbHMgd2l0aCBSLCBDYXAgNy41LCBwLiA4Mi04NCJ9LCB7ImVudW5jaWFkbyI6ICJFbSB1bWEgYW7DoWxpc2UgZXN0YXTDrXN0aWNhIGRlIGRhZG9zIGZpbmFuY2Vpcm9zLCB1bSBwZXNxdWlzYWRvciBvYnNlcnZhIHF1ZSwgZW0gc2V1IGdyw6FmaWNvIGRlIHJlc8OtZHVvcyB2ZXJzdXMgdmFsb3JlcyBhanVzdGFkb3MsIG9zIHBvbnRvcyBmb3JtYW0gdW1hICdudXZlbScgYWxlYXTDs3JpYSBlIHVuaWZvcm1lIGFvIHJlZG9yIGRhIHJldGEgaG9yaXpvbnRhbCBlbSAkXFxoYXR7ZX1faSA9IDAkLiBBZGljaW9uYWxtZW50ZSwgbyB0ZXN0ZSBkZSB2YXJpw6JuY2lhIGVudHJlIGRvaXMgZ3J1cG9zIGRlIGRhZG9zIChhbW9zdHJhcyBjb20gJHggPCQgbWVkaWFuYSBlICR4ID4kIG1lZGlhbmEpIG7Do28gYXByZXNlbnRhIGV2aWTDqm5jaWFzIGVzdGF0w61zdGljYXMgZGUgaGV0ZXJvY2VkYXN0aWNpZGFkZSAoJHBcXHRleHR7LXZhbG9yfSA+IDAuMDUkKS4gTyBxdWUgZXN0ZSBkaWFnbsOzc3RpY28gcGVybWl0ZSBjb25jbHVpciBzb2JyZSBvIG1vZGVsbyBkZSByZWdyZXNzw6NvIGxpbmVhciBhZG90YWRvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyBtb2RlbG8gZGV2ZSBzZXIgZGVzY2FydGFkbywgcG9pcyBhIGF1c8OqbmNpYSBkZSBwYWRyw7VlcyBubyBncsOhZmljbyBkZSByZXPDrWR1b3Mgw6kgdW0gc2luYWwgZGUgc3ViYWp1c3RlLiIsICJCIjogIkEgc3Vwb3Npw6fDo28gZGUgaG9tb2NlZGFzdGljaWRhZGUgw6kgc3VzdGVudGFkYSB0YW50byBwZWxhIGFuw6FsaXNlIGdyw6FmaWNhIHF1YW50byBwZWxvcyByZXN1bHRhZG9zIGRvcyB0ZXN0ZXMgZGUgdmFyacOibmNpYS4iLCAiQyI6ICJPIG1vZGVsbyBwb3NzdWkgaGV0ZXJvY2VkYXN0aWNpZGFkZSBtb2RlcmFkYSBlIHJlcXVlciB1bWEgdHJhbnNmb3JtYcOnw6NvIGRlIHZhcmnDoXZlbCBkbyB0aXBvIGxvZ2Fyw610bWljYSBwYXJhIGVzdGFiaWxpemFyIGEgdmFyacOibmNpYS4iLCAiRCI6ICJPcyByZXPDrWR1b3MgbsOjbyBhdGVuZGVtIMOgIG5vcm1hbGlkYWRlLCBleGlnaW5kbyBvIHVzbyBkZSBtw61uaW1vcyBxdWFkcmFkb3MgcG9uZGVyYWRvcyBpbWVkaWF0YW1lbnRlLiIsICJFIjogIk8gbW9kZWxvIGFwcmVzZW50YSBhbHRhIGNvbGluZWFyaWRhZGUsIGRhZG8gcXVlIGEgZGlzcGVyc8OjbyBkb3MgcmVzw61kdW9zIMOpIHBlcmZlaXRhbWVudGUgdW5pZm9ybWUuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJBdmFsaWUgbyBxdWUgbyBncsOhZmljbyBkZSByZXPDrWR1b3MgaWRlYWwgcmVwcmVzZW50YSBuYXMgcHJlbWlzc2FzIGRlIEdhdXNzLU1hcmtvdiBlIGNvbW8gbyBwLXZhbG9yIGNvcnJvYm9yYSBhIGFuw6FsaXNlIHZpc3VhbC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgYW7DoWxpc2UgdmlzdWFsIGRlIHJlc8OtZHVvcyBjb250cmEgdmFsb3JlcyBhanVzdGFkb3MgYnVzY2FuZG8gdW1hICdudXZlbScgYWxlYXTDs3JpYSBzZW0gcGFkcsO1ZXMgw6kgbyBwcm9jZWRpbWVudG8gcGFkcsOjbyBwYXJhIHZlcmlmaWNhciBhIGhvbW9jZWRhc3RpY2lkYWRlLiBRdWFuZG8gZXNzYSBhbsOhbGlzZSBncsOhZmljYSDDqSBhY29tcGFuaGFkYSBwb3IgdGVzdGVzIGRlIHZhcmnDom5jaWEgKGNvbW8gYSBjb21wYXJhw6fDo28gZGUgdmFyacOibmNpYXMgZW50cmUgZ3J1cG9zKSBxdWUgbsOjbyByZWplaXRhbSBhIGhpcMOzdGVzZSBudWxhIGRlIGlndWFsZGFkZSBkZSB2YXJpw6JuY2lhcyAoJHBcXHRleHR7LXZhbG9yfSA+IFxcYWxwaGEkKSwgdGVtb3MgdW1hIGZvcnRlIGV2aWTDqm5jaWEgZGUgcXVlIGEgcHJlbWlzc2EgZGUgdmFyacOibmNpYSBjb25zdGFudGUgKCRWYXIoXFxEZWx0YSkgPSBcXHNpZ21hXjIgSSQpIGVzdMOhIHNlbmRvIHJlc3BlaXRhZGEsIHZhbGlkYW5kbyBvIHVzbyBkZSBNw61uaW1vcyBRdWFkcmFkb3MgT3JkaW7DoXJpb3MgKE1RTykuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PW5wLnJhbmRvbS5yYW5kKDEwMCkqMTAwLCB5PW5wLnJhbmRvbS5ub3JtYWwoMCwgMSwgMTAwKSwgbW9kZT0nbWFya2VycycsIG5hbWU9J1Jlc8OtZHVvcycpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0dyw6FmaWNvIGRlIFJlc8OtZHVvcyAoSG9tb2NlZMOhc3RpY28pJywgeGF4aXNfdGl0bGU9J1ZhbG9yZXMgQWp1c3RhZG9zICgkXFxoYXR7eX1faSQpJywgeWF4aXNfdGl0bGU9J1Jlc8OtZHVvcyAoJFxcaGF0e2V9X2kkKScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKVxuZmlnLmFkZF9obGluZSh5PTAsIGxpbmVfZGFzaD0nZGFzaCcsIGxpbmVfY29sb3I9JyMwMDAwRkYnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtIGVuZ2VuaGVpcm8gZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlIGVzdMOhIGFuYWxpc2FuZG8gb3MgZXJyb3MgZGUgbWVkacOnw6NvIGRlIHVtIHByb2Nlc3NvIGRlIGZhYnJpY2HDp8OjbyBhdXRvbWF0aXphZG8gKGRlbm90YWRvcyBwb3IgJFxcRGVsdGEkKS4gQXDDs3MgYWp1c3RhciB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgcGFyYSBwcmV2ZXIgYSB2YXJpYWJpbGlkYWRlIGRvIHByb2Nlc3NvIGVtIGZ1bsOnw6NvIGRhIHRlbXBlcmF0dXJhLCBlbGUgZXh0cmFpIG9zIHJlc8OtZHVvcyBlIGNvbnN0csOzaSB1bSBncsOhZmljbyBRLVEgcGxvdCBwYXJhIHZlcmlmaWNhciBhIHByZW1pc3NhIGRlIG5vcm1hbGlkYWRlLiBBbyBvYnNlcnZhciBvIGdyw6FmaWNvLCBlbGUgbm90YSBxdWUgb3MgcG9udG9zIHNlIGRlc3ZpYW0gc2lnbmlmaWNhdGl2YW1lbnRlIGRhIGxpbmhhIGRpYWdvbmFsIG5hcyBleHRyZW1pZGFkZXMgKGNhdWRhcykgZGEgZGlzdHJpYnVpw6fDo28uIENvbnNpZGVyYW5kbyBhcyBwcm9wcmllZGFkZXMgZXN0YXTDrXN0aWNhcyBkb3MgcmVzw61kdW9zIG5vIG1vZGVsbyBkZSBHYXVzcy1NYXJrb3YgZSBhIGludGVycHJldGHDp8OjbyBkaWFnbsOzc3RpY2EsIHF1YWwgZGFzIGFsdGVybmF0aXZhcyBhIHNlZ3VpciDDqSBhIG1haXMgYWRlcXVhZGEgcGFyYSBhIHRvbWFkYSBkZSBkZWNpc8Ojbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gbW9kZWxvIGRldmUgc2VyIGltZWRpYXRhbWVudGUgZGVzY2FydGFkbywgcG9pcyBxdWFscXVlciBkZXN2aW8gZGEgbm9ybWFsaWRhZGUgbm9zIHJlc8OtZHVvcyBpbnZhbGlkYSBjb21wbGV0YW1lbnRlIGFzIGVzdGltYXRpdmFzIGRlIG3DrW5pbW9zIHF1YWRyYWRvcywgdG9ybmFuZG8gbyBlc3RpbWFkb3IgJFxcaGF0e1xcYmV0YX0kIHZpZXNhZG8uIiwgIkIiOiAiQSBwcmVzZW7Dp2EgZGUgZGVzdmlvcyBuYXMgY2F1ZGFzIHN1Z2VyZSBhIG5lY2Vzc2lkYWRlIGRlIGNhdXRlbGE7IHNlIG8gdGFtYW5obyBhbW9zdHJhbCAkbiQgZm9yIG11aXRvIGdyYW5kZSwgbyBUZW9yZW1hIENlbnRyYWwgZG8gTGltaXRlIG1pdGlnYSBvIGltcGFjdG8gbmEgaW5mZXLDqm5jaWEsIG1hcyBkZXN2aW9zIHNldmVyb3MgZW0gYW1vc3RyYXMgcGVxdWVuYXMgZGV2ZW0gc2VyIGludmVzdGlnYWRvcyBjb21vIHBvdGVuY2lhaXMgZmFsaGFzIG5vIG1vZGVsby4iLCAiQyI6ICJPIGdyw6FmaWNvIFEtUSBwbG90IMOpIHVtIHRlc3RlIGZvcm1hbDsgc2Ugb3MgcG9udG9zIG7Do28gdG9jYW0gYSBsaW5oYSBkaWFnb25hbCwgYSBoaXDDs3Rlc2UgZGUgbm9ybWFsaWRhZGUgw6kgcmVqZWl0YWRhIGNvbSB1bSBwLXZhbG9yIG1lbm9yIHF1ZSAkMC4wNSQsIGluZGVwZW5kZW50ZW1lbnRlIGRvIHRhbWFuaG8gZGEgYW1vc3RyYS4iLCAiRCI6ICJBIG5vcm1hbGlkYWRlIGRvcyByZXPDrWR1b3Mgw6kgdW1hIHN1cG9zacOnw6NvIGFwZW5hcyBwYXJhIG8gY8OhbGN1bG8gZGEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSQsIG7Do28gdGVuZG8gcXVhbHF1ZXIgcmVsYcOnw6NvIGNvbSBhIHZhbGlkYWRlIGRvcyBpbnRlcnZhbG9zIGRlIGNvbmZpYW7Dp2Egb3UgdGVzdGVzIHQgcGFyYSBvcyBjb2VmaWNpZW50ZXMgJFxcaGF0e1xcYmV0YX1fMSQuIiwgIkUiOiAiTyBncsOhZmljbyBpbmRpY2EgaGV0ZXJvY2VkYXN0aWNpZGFkZSwgcG9pcyByZXPDrWR1b3Mgbm9ybWFsbWVudGUgZGlzdHJpYnXDrWRvcyBzZW1wcmUgYXByZXNlbnRhbSB1bWEgbGluaGEgaG9yaXpvbnRhbCBlbSBncsOhZmljb3MgZGUgZGlzcGVyc8OjbyBjb250cmEgbyB2YWxvciBwcmVkaXRvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBvIFRlb3JlbWEgQ2VudHJhbCBkbyBMaW1pdGUgYXR1YSBzb2JyZSBhIGRpc3RyaWJ1acOnw6NvIGFtb3N0cmFsIGRvcyBlc3RpbWFkb3JlcywgZSBxdWUgdGVzdGVzIHZpc3VhaXMgYWp1ZGFtIGEgZGlhZ25vc3RpY2FyIG8gY29tcG9ydGFtZW50byBkYXMgY2F1ZGFzLCBvbmRlIGEgbm9ybWFsaWRhZGUgw6kgbWFpcyBjcsOtdGljYS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgYWx0ZXJuYXRpdmEgQiDDqSBhIGNvcnJldGEgcG9pcyByZWZsZXRlIG8gZW50ZW5kaW1lbnRvIHByw6F0aWNvIGRlIHF1ZSBhIG5vcm1hbGlkYWRlIGRvcyByZXPDrWR1b3Mgw6kgdW0gYWxpY2VyY2UgcGFyYSBhIHZhbGlkYWRlIGRhIGluZmVyw6puY2lhICh0ZXN0ZXMgdCBlIEYpLiBQZXF1ZW5vcyBkZXN2aW9zIGVtIGdyYW5kZXMgYW1vc3RyYXMgc8OjbyB0b2xlcmFkb3MgZGV2aWRvIMOgIHJvYnVzdGV6IGNvbmZlcmlkYSBwZWxvIFRlb3JlbWEgQ2VudHJhbCBkbyBMaW1pdGUuIEEgYWx0ZXJuYXRpdmEgQSBlc3TDoSBpbmNvcnJldGEgcG9pcyBvcyBlc3RpbWFkb3JlcyBkZSBtw61uaW1vcyBxdWFkcmFkb3MgcGVybWFuZWNlbSBCTFVFIChCZXN0IExpbmVhciBVbmJpYXNlZCBFc3RpbWF0b3IpIG1lc21vIHNlbSBub3JtYWxpZGFkZSwgZW1ib3JhIGFzIGluZmVyw6puY2lhcyAodGVzdGVzIGUgSUNzKSBmaXF1ZW0gY29tcHJvbWV0aWRhcy4gQSBDIGVzdMOhIGluY29ycmV0YSBwb2lzIG8gUS1RIHBsb3Qgw6kgdW1hIGZlcnJhbWVudGEgZGlhZ27Ds3N0aWNhIHZpc3VhbCBlIG7Do28gdW0gdGVzdGUgZGUgaGlww7N0ZXNlcyBmb3JtYWwuIEQgw6kgZmFsc2EgcG9ycXVlIGEgbm9ybWFsaWRhZGUgZG9zIHJlc8OtZHVvcyDDqSBlc3NlbmNpYWwgcGFyYSBhIHZhbGlkYWRlIGRvcyBpbnRlcnZhbG9zIGRlIGNvbmZpYW7Dp2EuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bWEgYW7DoWxpc2UgZGUgcmVncmVzc8OjbyBjb20gJG49MjAkIG9ic2VydmHDp8O1ZXMsIHVtIGVzdGF0w61zdGljbyBkZWNpZGUgcmVhbGl6YXIgdW0gdGVzdGUgZGUgU2hhcGlyby1XaWxrIHBhcmEgZm9ybWFsaXphciBhIHZlcmlmaWNhw6fDo28gZGUgbm9ybWFsaWRhZGUgZG9zIHJlc8OtZHVvcyAkXFxEZWx0YSQuIE8gcC12YWxvciBvYnRpZG8gZm9pIGRlICQwLjAzJC4gQW5hbGlzYW5kbyBhIGxpdGVyYXR1cmEgdMOpY25pY2Egc29icmUgbyB0ZW1hLCBxdWFsIGEgaW50ZXJwcmV0YcOnw6NvIG1haXMgZXF1aWxpYnJhZGEgcGFyYSBlc3RlIHJlc3VsdGFkbyBubyBjb250ZXh0byBkZSBkaWFnbsOzc3RpY28gZGUgbW9kZWxvcz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gcC12YWxvciBkZSAkMC4wMyQgb2JyaWdhIG8gYWJhbmRvbm8gZG8gbW9kZWxvLCBwb2lzIGEgbm9ybWFsaWRhZGUgZm9pIHJlZnV0YWRhIGRlIGZvcm1hIGFic29sdXRhLCBleGlnaW5kbyBhIHRyb2NhIGltZWRpYXRhIHBvciBtb2RlbG9zIG7Do28gcGFyYW3DqXRyaWNvcy4iLCAiQiI6ICJPIHRlc3RlIGZvcm1hbCDDqSBzZW1wcmUgc3VwZXJpb3IgYW8gUS1RIHBsb3QsIGUgdW0gcC12YWxvciBkZSAkMC4wMyQgaW5kaWNhIHF1ZSBhIGRpc3RyaWJ1acOnw6NvIGRvcyBlcnJvcyDDqSBpbmRpc2N1dGl2ZWxtZW50ZSBDYXVjaHksIHRvcm5hbmRvIG8gYWp1c3RlIGRlIG3DrW5pbW9zIHF1YWRyYWRvcyBpbsO6dGlsLiIsICJDIjogIkVtIGFtb3N0cmFzIHBlcXVlbmFzIGNvbW8gJG49MjAkLCB0ZXN0ZXMgZGUgbm9ybWFsaWRhZGUgcG9zc3VlbSBwb2RlciBlc3RhdMOtc3RpY28gbGltaXRhZG8uIE8gZXN0YXTDrXN0aWNvIGRldmUgY29tcGxlbWVudGFyIG8gcmVzdWx0YWRvIGNvbSBvIFEtUSBwbG90IHBhcmEgdmVyaWZpY2FyIHNlIG8gcC12YWxvciBiYWl4byDDqSBmcnV0byBkZSB1bWEgYXNzaW1ldHJpYSBzZXZlcmEgb3UgYXBlbmFzIGRlIHJ1w61kbyBuYXMgY2F1ZGFzIHF1ZSBuw6NvIGludmFsaWRhIGFzIGluZmVyw6puY2lhcyBwcmluY2lwYWlzLiIsICJEIjogIk8gcC12YWxvciBkZSAkMC4wMyQgc2lnbmlmaWNhIHF1ZSBhIHByb2JhYmlsaWRhZGUgZGUgYSBoaXDDs3Rlc2UgbnVsYSBkZSBub3JtYWxpZGFkZSBzZXIgdmVyZGFkZWlyYSDDqSBkZSBleGF0YW1lbnRlICQzXFwlJCwgbyBxdWUgY29uZmlybWEgYSBuZWNlc3NpZGFkZSBkZSBhcGxpY2FyIHVtYSB0cmFuc2Zvcm1hw6fDo28gbG9nYXLDrXRtaWNhIGVtICRZJCBwYXJhIGZvcsOnYXIgYSBub3JtYWxpZGFkZS4iLCAiRSI6ICJDb21vICRuPTIwJCwgbyBlcnJvIHBhZHLDo28gZGEgZXN0aW1hdGl2YSAkXFxzaWdtYV4yJCDDqSBkZXNwcmV6w612ZWwsIGxvZ28gbyByZXN1bHRhZG8gZG8gdGVzdGUgZGUgU2hhcGlyby1XaWxrIG7Do28gcG9zc3VpIGluZmx1w6puY2lhIG5hIHZhbGlkYWRlIGRvIG1vZGVsby4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIkNvbnNpZGVyZSBvIGJhbGFuw6dvIGVudHJlIG8gcG9kZXIgZG8gdGVzdGUgZW0gYW1vc3RyYXMgcGVxdWVuYXMgZSBhIG5hdHVyZXphIGRpYWduw7NzdGljYSBkb3MgbcOpdG9kb3MgdmlzdWFpcy4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlRlc3RlcyBmb3JtYWlzIGNvbW8gU2hhcGlyby1XaWxrIHTDqm0gYmFpeG8gcG9kZXIgZW0gYW1vc3RyYXMgcGVxdWVuYXMgZSBwb2RlbSBzZXIgc2Vuc8OtdmVpcyBkZW1haXMgZW0gYW1vc3RyYXMgbXVpdG8gZ3JhbmRlcy4gTyBkaWFnbsOzc3RpY28gY29ycmV0byBlbnZvbHZlIGEgdHJpYW5ndWxhw6fDo28gY29tIG3DqXRvZG9zIHZpc3VhaXMgKFEtUSBwbG90KS4gQSBhbHRlcm5hdGl2YSBDIMOpIGEgY29ycmV0YS4gQXMgZGVtYWlzIGFsdGVybmF0aXZhcyBzb2JyZXZhbG9yaXphbSBvIHRlc3RlIGZvcm1hbCAoQSwgQikgb3UgdGlyYW0gY29uY2x1c8O1ZXMgZXN0YXTDrXN0aWNhcyBpbmNvcnJldGFzIHNvYnJlIG8gcC12YWxvciAoRCkgb3UgaWdub3JhbSBhIGltcG9ydMOibmNpYSBkYXMgc3Vwb3Npw6fDtWVzIGRvIG1vZGVsbyAoRSkuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gZGUgZW5nZW5oYXJpYSBpbmR1c3RyaWFsIHNvYnJlIG8gdGVtcG8gZGUgbW9udGFnZW0gZGUgY29tcG9uZW50ZXMsIHZvY8OqIGFqdXN0YSB1bSBtb2RlbG8gZGUgcmVncmVzc8OjbyBsaW5lYXIgc2ltcGxlcy4gQW8gYW5hbGlzYXIgb3MgZGlhZ27Ds3N0aWNvcywgdm9jw6ogb2JzZXJ2YSBxdWUgYSBvYnNlcnZhw6fDo28gJGkkIHBvc3N1aSB1bSByZXPDrWR1byAkZV9pJCBleHRyZW1hbWVudGUgcHLDs3hpbW8gZGUgemVybywgbWFzIHVtYSBhbGF2YW5jYWdlbSAkaF97aWl9JCBtdWl0byBwcsOzeGltYSBkZSAxLiBDb20gYmFzZSBuYSBmw7NybXVsYSBkYSBEaXN0w6JuY2lhIGRlIENvb2sgJERfe2l9ID0gXGZyYWN7ZV9pXjJ9e3AgXGZyYWN7U1Ffe1Jlc319e24gLSBwfX0gXGZyYWN7aF97aWl9fXsoMSAtIGhfe2lpfSleMn0kLCBxdWFsIMOpIGEgY29uY2x1c8OjbyBjb3JyZXRhIHNvYnJlIGEgaW5mbHXDqm5jaWEgZGVzdGUgcG9udG8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIHBvbnRvIMOpLCBvYnJpZ2F0b3JpYW1lbnRlLCB1bWEgb2JzZXJ2YcOnw6NvIGluZmx1ZW50ZSwgcG9pcyBxdWFscXVlciBhbGF2YW5jYWdlbSBhbHRhIGltcGxpY2EgYWx0YSBpbmZsdcOqbmNpYS4iLCAiQiI6ICJPIHBvbnRvIHRlbSBpbmZsdcOqbmNpYSBudWxhLCBwb2lzIGEgZGlzdMOibmNpYSBkZSBDb29rIGRlcGVuZGUgZXhjbHVzaXZhbWVudGUgZG8gdmFsb3IgZG8gcmVzw61kdW8gJGVfaSQuIiwgIkMiOiAiTyBwb250byBwb2RlIHBvc3N1aXIgdW1hIGluZmx1w6puY2lhIGFsdMOtc3NpbWEgYXBlc2FyIGRlIHNldSByZXPDrWR1byBzZXIgcGVxdWVubywgcG9pcyBvIHRlcm1vICRcZnJhY3toX3tpaX19eygxIC0gaF97aWl9KV4yfSQgZXhwbG9kZSBxdWFuZG8gJGhfe2lpfSQgc2UgYXByb3hpbWEgZGUgMSwgb2N1bHRhbmRvIGEgaW5mbHXDqm5jaWEgcGVsbyByZXPDrWR1byByZWR1emlkby4iLCAiRCI6ICJPIHBvbnRvIMOpIHVtIG91dGxpZXIgdMOtcGljbyBjb20gcmVzw61kdW8gYWx0bywgbG9nbyBzdWEgaW5mbHXDqm5jaWEgw6kgZGVzcHJlesOtdmVsIG5vIG1vZGVsbyBkZSByZWdyZXNzw6NvLiIsICJFIjogIkEgZGlzdMOibmNpYSBkZSBDb29rIMOpIHNlbXByZSBjb25zdGFudGUsIGluZGVwZW5kZW50ZW1lbnRlIGRhIGFsYXZhbmNhZ2VtLCBpbnZhbGlkYW5kbyBvIGRpYWduw7NzdGljbyBwYXJhIGVzdGUgY2Fzby4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIkNvbnNpZGVyZSBvIGNvbXBvcnRhbWVudG8gZG8gdGVybW8gZGUgYWxhdmFuY2FnZW0gbm8gZGVub21pbmFkb3Igw6AgbWVkaWRhIHF1ZSAkaF97aWl9IFx0byAxJC4gTyByZXPDrWR1byAncGVxdWVubycgw6kgdW1hIGlsdXPDo28gY2F1c2FkYSBwZWxvIGFqdXN0ZSBkYSByZXRhIGFvIHByw7NwcmlvIHBvbnRvLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBhbGF2YW5jYWdlbSAkaF97aWl9JCBtZWRlIGEgZGlzdMOibmNpYSBkbyBwb250byAkaSQgbm8gZXNwYcOnbyBkb3MgcHJlZGl0b3Jlcy4gUXVhbmRvICRoX3tpaX0kIHNlIGFwcm94aW1hIGRlIDEsIGEgcmV0YSBkZSByZWdyZXNzw6NvIMOpICdwdXhhZGEnIHBhcmEgcGFzc2FyIHF1YXNlIGV4YXRhbWVudGUgc29icmUgYSBvYnNlcnZhw6fDo28sIGZhemVuZG8gY29tIHF1ZSAkZV9pIFx0byAwJC4gQ29udHVkbywgYSBEaXN0w6JuY2lhIGRlIENvb2sgY29udMOpbSBvIGZhdG9yICRcZnJhY3toX3tpaX19eygxIC0gaF97aWl9KV4yfSQuIE1lc21vIHF1ZSAkZV9pXjIkIHNlamEgcGVxdWVubywgbyBjcmVzY2ltZW50byBleHBvbmVuY2lhbCBkbyBjb21wb25lbnRlIGRlIGFsYXZhbmNhZ2VtIGZheiBjb20gcXVlIG8gdmFsb3IgZmluYWwgZGUgJERfaSQgc2VqYSBlbGV2YWRvLCBpZGVudGlmaWNhbmRvIGNvcnJldGFtZW50ZSBhIG9ic2VydmHDp8OjbyBjb21vIGluZmx1ZW50ZS4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9WzAuMSwgMC45XSwgeT1bMC4wMSwgMTBdLCBtb2RlPSdsaW5lcycsIG5hbWU9J0luZmx1w6puY2lhIHZzIEFsYXZhbmNhZ2VtJywgbGluZT1kaWN0KGNvbG9yPScjMDAwMEZGJywgd2lkdGg9MykpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9JzxiPkNvbXBvcnRhbWVudG8gZGEgSW5mbHXDqm5jaWEgdnMgQWxhdmFuY2FnZW0gKCRoX3tpaX0kICk8L2I+JywgeGF4aXM9ZGljdCh0aXRsZT0nQWxhdmFuY2FnZW0gKCRoX3tpaX0kKScpLCB5YXhpcz1kaWN0KHRpdGxlPSdUZXJtbyBkZSBJbmZsdcOqbmNpYScpLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBhbmFsaXN0YSBkZSBkYWRvcyB1dGlsaXphIGEgRGlzdMOibmNpYSBkZSBDb29rIHBhcmEgZmlsdHJhciBvYnNlcnZhw6fDtWVzIGVtIHVtIGNvbmp1bnRvIGRlIGRhZG9zIGNvbSAkbj01MCQgZSAkcD0zJCAoaW50ZXJjZXB0byArIDIgcHJlZGl0b3JlcykuIFNlIHVtIHBvbnRvIGFwcmVzZW50YSAkRF9pID4gMSQsIG8gcXVlIGVzc2EgbcOpdHJpY2EgaW5kaWNhIGVzdGF0aXN0aWNhbWVudGU/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJRdWUgYSBvYnNlcnZhw6fDo28gw6kgaW5vZmVuc2l2YSBlIGRldmUgc2VyIG1hbnRpZGEgcGFyYSBhdW1lbnRhciBvICRSXjIkIGRvIG1vZGVsby4iLCAiQiI6ICJRdWUgYSBvYnNlcnZhw6fDo28gY2F1c2EgdW1hIG11ZGFuw6dhIG5vIHZldG9yIGRlIGNvZWZpY2llbnRlcyAkXFxoYXR7XFx0aGV0YX0kIHF1ZSDDqSBjb25zaWRlcmFkYSBudW1lcmljYW1lbnRlIHNpZ25pZmljYXRpdmEgZW0gcmVsYcOnw6NvIMOgIHZhcmnDom5jaWEgZXN0aW1hZGEgZG8gbW9kZWxvLiIsICJDIjogIlF1ZSBvIHZhbG9yIGRlICRZX2kkIMOpIGV4YXRhbWVudGUgaWd1YWwgYW8gdmFsb3IgcHJldmlzdG8gJFxcaGF0e1l9X2kkLiIsICJEIjogIlF1ZSBhIHZhcmnDoXZlbCBleHBsaWNhdGl2YSBjb3JyZXNwb25kZW50ZSBwb3NzdWkgdmFyacOibmNpYSB6ZXJvLiIsICJFIjogIlF1ZSBvIG1vZGVsbyBwb3NzdWkgbXVsdGljb2xpbmVhcmlkYWRlIHBlcmZlaXRhIGVudHJlIG9zIHByZWRpdG9yZXMuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIGEgRGlzdMOibmNpYSBkZSBDb29rIHF1YW50aWZpY2EgYSBtdWRhbsOnYSBubyB2ZXRvciAkXFxoYXR7XFx0aGV0YX0kIHF1YW5kbyB1bWEgb2JzZXJ2YcOnw6NvIMOpIHJlbW92aWRhLiBPIHZhbG9yIDEgw6kgdW0gcG9udG8gZGUgY29ydGUgaGV1csOtc3RpY28gY29tdW0uIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIERpc3TDom5jaWEgZGUgQ29vaywgJERfaSQsIG1lZGUgYSBkaXN0w6JuY2lhIGRlIE1haGFsYW5vYmlzIGVudHJlICRcXGhhdHtcXHRoZXRhfSQgKGVzdGltYXRpdmEgY29tIHRvZG9zIG9zIGRhZG9zKSBlICRcXGhhdHtcXHRoZXRhfV97KGkpfSQgKGVzdGltYXRpdmEgc2VtIGEgb2JzZXJ2YcOnw6NvICRpJCkuIFVtIHZhbG9yIGRlICREX2kgPiAxJCBzdWdlcmUgcXVlIGEgb2JzZXJ2YcOnw6NvICRpJCBleGVyY2UgdW1hIGluZmx1w6puY2lhIGZvcnRlIG8gc3VmaWNpZW50ZSBwYXJhIGRlc2xvY2FyIHNpZ25pZmljYXRpdmFtZW50ZSBhcyBlc3RpbWF0aXZhcyBkb3MgcGFyw6JtZXRyb3MsIGp1c3RpZmljYW5kbyB1bWEgaW5zcGXDp8OjbyBkZXRhbGhhZGEgb3UgYSByZW1vw6fDo28gZG8gZGFkby4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH1dLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbeyJlbnVuY2lhZG8iOiAiRGVtb25zdHJlIGFsZ2VicmljYW1lbnRlIHF1ZSBvIHZldG9yIGRlIHJlc8OtZHVvcyAkXFxoYXR7ZX0gPSAoSSAtIFApeSQgZSBvIHZldG9yIGRlIHZhbG9yZXMgYWp1c3RhZG9zICRcXGhhdHt5fSA9IFB5JCBzw6NvIG9ydG9nb25haXMsIG91IHNlamEsICRcXGhhdHtlfSdcXGhhdHt5fSA9IDAkLiIsICJkaWNhIjogIkxlbWJyZS1zZSBkYXMgcHJvcHJpZWRhZGVzIGRlIHByb2pldG9yZXMgb3J0b2dvbmFpczogJFAgPSBQJyQsICRQXjIgPSBQJCBlICQoSS1QKVAgPSAwJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRGVmaW5pbW9zICRcXGhhdHtlfSdcXGhhdHt5fSA9IFsoSSAtIFApeV0nIChQeSkkIiwgIlBlbGEgcHJvcHJpZWRhZGUgZGEgdHJhbnNwb3N0YSwgJFxcaGF0e2V9J1xcaGF0e3l9ID0geScoSSAtIFApJyBQIHkkIiwgIkNvbW8gJFAkIMOpIHNpbcOpdHJpY28sICQoSSAtIFApJyA9IEknIC0gUCcgPSBJIC0gUCQiLCAiTG9nbywgJFxcaGF0e2V9J1xcaGF0e3l9ID0geScoSSAtIFApUCB5JCIsICJFeHBhbmRpbmRvIG8gcHJvZHV0bywgJChJIC0gUClQID0gUCAtIFBeMiQiLCAiQ29tbyAkUCQgw6kgaWRlbXBvdGVudGUsICRQXjIgPSBQJCwgcG9ydGFudG8gJFAgLSBQXjIgPSBQIC0gUCA9IDAkIiwgIkFzc2ltLCAkXFxoYXR7ZX0nXFxoYXR7eX0gPSB5JygwKXkgPSAwJCJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEgJiBFc3RldmVzLCBNb2RlbG9zIExpbmVhcmVzLCBDYXAgNCwgcC4gMTEwIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4wfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIElvVCwgdGVtb3MgNSBvYnNlcnZhw6fDtWVzICgkbj01JCkgZSAzIHBhcsOibWV0cm9zIG5vIG1vZGVsbyAoJGs9MyQpLiBTZSBhIHNvbWEgZGUgcXVhZHJhZG9zIHRvdGFsICRTUV97VG90fSA9IHkneSA9IDEwMCQgZSBhIHNvbWEgZGUgcXVhZHJhZG9zIGRvcyBwYXLDom1ldHJvcyAkU1Ffe1Bhcn0gPSB5J1B5ID0gODAkLCBkZXRlcm1pbmUgYSBzb21hIGRlIHF1YWRyYWRvcyBkb3MgcmVzw61kdW9zICgkU1Ffe1Jlc30kKSBlIG8gbsO6bWVybyBkZSBncmF1cyBkZSBsaWJlcmRhZGUgZG8gcmVzw61kdW8uIiwgImRpY2EiOiAiVXNlIGEgZGVjb21wb3Npw6fDo28gZGEgc29tYSBkZSBxdWFkcmFkb3M6ICRTUV97VG90fSA9IFNRX3tQYXJ9ICsgU1Ffe1Jlc30kIGUgYSByZWxhw6fDo28gJGdsX3tSZXN9ID0gbiAtIGskLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJBIGRlY29tcG9zacOnw6NvIMOpICRTUV97VG90fSA9IFNRX3tQYXJ9ICsgU1Ffe1Jlc30kIiwgIiQxMDAgPSA4MCArIFNRX3tSZXN9JCIsICIkU1Ffe1Jlc30gPSAyMCQiLCAiR3JhdXMgZGUgbGliZXJkYWRlIGRvIHJlc8OtZHVvOiAkZ2xfe1Jlc30gPSBuIC0gayQiLCAiJGdsX3tSZXN9ID0gNSAtIDMgPSAyJCJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEgJiBFc3RldmVzLCBNb2RlbG9zIExpbmVhcmVzLCBDYXAgNCwgcC4gMTExIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMjAuMH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBvIG1vZGVsbyAkeSA9IFhcXHRoZXRhICsgXFx0ZXh0e86UfSQuIFNlIHVtIGFuYWxpc3RhIGVuY29udHJhIHF1ZSBvIHZldG9yIGRlIHJlc8OtZHVvcyBleGliZSB1bWEgdGVuZMOqbmNpYSBzaXN0ZW3DoXRpY2EgZW0gcmVsYcOnw6NvIGFvIHRlbXBvLCBvIHF1ZSBpc3NvIGltcGxpY2Egc29icmUgYSBwcmVtaXNzYSBkZSBxdWUgb3MgcmVzw61kdW9zIHJlcHJlc2VudGFtICd2YXJpYcOnw7VlcyBhbGVhdMOzcmlhcyBwdXJhcyc/IENvbW8gaXNzbyBzZSByZWxhY2lvbmEgY29tIGEgZXNwZWNpZmljYcOnw6NvIGRvIG1vZGVsbz8iLCAiZGljYSI6ICJQZW5zZSBubyBwcm9ww7NzaXRvIGRvIHZldG9yIGRlIHJlc8OtZHVvcyBjb21vIGNhcnJlZ2Fkb3IgZGUgaW5mb3JtYcOnw6NvIG7Do28gZXhwbGljYWRhIHBlbG8gbW9kZWxvLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJTZSBvIG1vZGVsbyDDqSBiZW0gZXNwZWNpZmljYWRvLCBvcyByZXPDrWR1b3MgZGV2ZW0gY29tcG9ydGFyLXNlIGNvbW8gdmFyaWHDp8O1ZXMgYWxlYXTDs3JpYXMgcHVyYXMsIHNlbSBwYWRyw7Vlcy4iLCAiQSBwcmVzZW7Dp2EgZGUgdW1hIHRlbmTDqm5jaWEgc2lzdGVtw6F0aWNhIGluZGljYSBxdWUgbyBtb2RlbG8gZmFsaG91IGVtIGNhcHR1cmFyIHVtYSBjb21wb25lbnRlIGVzdHJ1dHVyYWwgb3UgdGVtcG9yYWwgbm9zIGRhZG9zLiIsICJJc3NvIHN1Z2VyZSBxdWUgbyBtb2RlbG8gZXN0w6EgbWFsIGVzcGVjaWZpY2FkbyAoZXg6IG9taXNzw6NvIGRlIHZhcmnDoXZlbCByZWxldmFudGUgb3UgZm9ybWEgZnVuY2lvbmFsIGluY29ycmV0YSkuIiwgIkEgYW7DoWxpc2UgZ3LDoWZpY2EgZG9zIHJlc8OtZHVvcyDDqSBmdW5kYW1lbnRhbCwgcG9pcyBxdWFscXVlciBwYWRyw6NvIHZpc3VhbCAoY29tbyB0ZW5kw6puY2lhcyBvdSBhZ3J1cGFtZW50b3MpIHZpb2xhIGEgcHJlbWlzc2EgZGUgZXJybyBhbGVhdMOzcmlvIHB1cm8uIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1saXN0KHJhbmdlKDEwKSksIHk9LCBtb2RlPVwibWFya2VycytsaW5lc1wiLCBuYW1lPVwiUmVzw61kdW9zIGNvbSBUZW5kw6puY2lhXCIsIGxpbmU9ZGljdChjb2xvcj1cIiNGRjAwMDBcIikpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9XCI8Yj5EaWFnbsOzc3RpY286IFJlc8OtZHVvcyBjb20gUGFkcsOjbyAoTWFsIEVzcGVjaWZpY2Fkbyk8L2I+XCIsIHRlbXBsYXRlPVwicGxvdGx5X3doaXRlXCIsIHhheGlzPWRpY3QodGl0bGU9XCJUZW1wb1wiKSwgeWF4aXM9ZGljdCh0aXRsZT1cIlJlc8OtZHVvICgkXFxcXGhhdHtlfV9pJClcIikpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGFkbyBvIG1vZGVsbyAkeSA9IFhcXHRoZXRhICsgXFxEZWx0YSQsIGRlbW9uc3RyZSBmb3JtYWxtZW50ZSBxdWUgYSBtYXRyaXogZGUgcmVzw61kdW9zICRNID0gKElfbiAtIFApJCDDqSBzaW3DqXRyaWNhIGUgaWRlbXBvdGVudGUsIG9uZGUgJFAgPSBYKFgnWCleey0xfVgnJC4iLCAiZGljYSI6ICJMZW1icmUtc2UgZGFzIHByb3ByaWVkYWRlcyBkYSB0cmFuc3Bvc3RhOiAkKEFCKScgPSBCJ0EnJCBlICQoQV57LTF9KScgPSAoQScpXnstMX0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXJhIGEgc2ltZXRyaWEsIGNhbGN1bGFtb3MgYSB0cmFuc3Bvc3RhIGRlICRQJDogJFAnID0gKFgoWCdYKV57LTF9WCcpJyA9IChYJyknKCAoWCdYKV57LTF9ICknIFgnJC4iLCAiQ29tbyAkWCdYJCDDqSBzaW3DqXRyaWNhLCAkKCAoWCdYKV57LTF9ICknID0gKFgnWCleey0xfSQsIGVudMOjbyAkUCcgPSBYKFgnWCleey0xfVgnID0gUCQuIiwgIkxvZ28sICRNJyA9IChJIC0gUCknID0gSScgLSBQJyA9IEkgLSBQID0gTSQuIiwgIlBhcmEgYSBpZGVtcG90w6puY2lhLCBjYWxjdWxhbW9zICRNXjIgPSAoSSAtIFApKEkgLSBQKSA9IEkgLSBQIC0gUCArIFBeMiQuIiwgIlNhYmVtb3MgcXVlICRQXjIgPSBQJCAoZGUgJChYKFgnWCleey0xfVgnKShYKFgnWCleey0xfVgnKSA9IFgoWCdYKV57LTF9KFgnWCkoWCdYKV57LTF9WCcgPSBYKFgnWCleey0xfVgnID0gUCQpLiIsICJTdWJzdGl0dWluZG8sICRNXjIgPSBJIC0gMlAgKyBQID0gSSAtIFAgPSBNJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgdW0gZXhwZXJpbWVudG8gb25kZSAkbj01JCBvYnNlcnZhw6fDtWVzIGUgYSBtYXRyaXogZGUgZGVsaW5lYW1lbnRvICRYJCBwZXJtaXRlIGEgcHJvamXDp8OjbyAkUCQuIFNhYmVuZG8gcXVlIG8gdHJhw6dvIGRhIG1hdHJpeiBkZSBwcm9qZcOnw6NvICR0cihQKSA9IGskLCBvbmRlICRrJCDDqSBvIHBvc3RvIGRhIG1hdHJpeiwgZGV0ZXJtaW5lIG8gZ3JhdSBkZSBsaWJlcmRhZGUgZG9zIHJlc8OtZHVvcyAkZ2xfe3Jlc30kIHNhYmVuZG8gcXVlICRyYW5rKFgpID0gMiQuIiwgImRpY2EiOiAiTyBncmF1IGRlIGxpYmVyZGFkZSBkb3MgcmVzw61kdW9zIMOpIGRhZG8gcGVsYSBkaW1lbnPDo28gZG8gZXNwYcOnbyBvcnRvZ29uYWwgYW8gbW9kZWxvLCBvdSBzZWphLCAkdHIoSV9uIC0gUCkkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJPIGdyYXUgZGUgbGliZXJkYWRlIGRvcyByZXPDrWR1b3Mgw6kgZGFkbyBwZWxhIGRpZmVyZW7Dp2EgZW50cmUgbyBuw7ptZXJvIHRvdGFsIGRlIG9ic2VydmHDp8O1ZXMgZSBvIHBvc3RvIGRhIG1hdHJpeiBkZSBkZWxpbmVhbWVudG86ICRnbF97cmVzfSA9IG4gLSByYW5rKFgpJC4iLCAiU3Vic3RpdHVpbmRvIG9zIHZhbG9yZXMgZGFkb3M6ICRuID0gNSQgZSAkcmFuayhYKSA9IDIkLiIsICJDYWxjdWxhbmRvOiAkZ2xfe3Jlc30gPSA1IC0gMiQuIiwgIlJlc3VsdGFkbzogJGdsX3tyZXN9ID0gMyQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAzLjB9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgdXNhbmRvIGEgZ2VvbWV0cmlhIGRhIHByb2plw6fDo28gb3J0b2dvbmFsLCBwb3IgcXVlIG8gdmV0b3IgZGUgcmVzw61kdW9zICRlJCBkZXZlIHNlciBvYnJpZ2F0b3JpYW1lbnRlIG9ydG9nb25hbCBhbyB2ZXRvciBkZSBwcmV2aXPDtWVzICRcXGhhdHt5fSQuIiwgImRpY2EiOiAiVmVyaWZpcXVlIG8gcHJvZHV0byBpbnRlcm5vICRlJ1xcaGF0e3l9JCB1c2FuZG8gYXMgZGVmaW5pw6fDtWVzIGRlICRlID0gKEktUCl5JCBlICRcXGhhdHt5fSA9IFB5JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiU2VqYSAkXFxoYXR7eX0gPSBQeSQgZSAkZSA9IChJLVApeSQuIiwgIk8gcHJvZHV0byBpbnRlcm5vIMOpICRlJ1xcaGF0e3l9ID0gKChJLVApeSknKFB5KSA9IHknKEktUCknUCB5JC4iLCAiQ29tbyAkSS1QJCDDqSBzaW3DqXRyaWNhLCAkZSdcXGhhdHt5fSA9IHknKEktUClQeSA9IHknKFAgLSBQXjIpeSQuIiwgIkRldmlkbyDDoCBpZGVtcG90w6puY2lhIGRlICRQJCwgdGVtb3MgJFAgLSBQXjIgPSBQIC0gUCA9IDAkLiIsICJQb3J0YW50bywgJGUnXFxoYXR7eX0gPSB5JzB5ID0gMCQsIG8gcXVlIHByb3ZhIGEgb3J0b2dvbmFsaWRhZGUgZW50cmUgbyBtb2RlbG8gZSBvcyByZXPDrWR1b3MuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvIGxpbmVhciBzaW1wbGVzIGNvbSAkbj0yMCQgb2JzZXJ2YcOnw7Vlcy4gUGFyYSBhIG9ic2VydmHDp8OjbyAkaT01JCwgZm9yYW0gb2J0aWRvczogcmVzw61kdW8gJGVfNSA9IDIuNSQsIGRlc3ZpbyBwYWRyw6NvIGVzdGltYWRvIGRvIGVycm8gJFxcaGF0e1xcc2lnbWF9ID0gMS4yJCBlIGFsYXZhbmNhZ2VtICRoX3s1NX0gPSAwLjQkLiBDYWxjdWxlIG8gcmVzw61kdW8gcGFkcm9uaXphZG8gKCR6XzUkKSBlIG8gcmVzw61kdW8gc3R1ZGVudGl6YWRvIGludGVybm8gKCRyXzUkKS4gQ29tZW50ZSBicmV2ZW1lbnRlIHF1YWwgZGVzc2VzIHZhbG9yZXMgbWVsaG9yIHJlZmxldGUgYSBtYWduaXR1ZGUgZG8gZXJybyBlbSByZWxhw6fDo28gw6AgcHJlY2lzw6NvIGxvY2FsLiIsICJkaWNhIjogIlVzZSAkel9pID0gZV9pIC8gXFxoYXR7XFxzaWdtYX0kIGUgJHJfaSA9IGVfaSAvIChcXGhhdHtcXHNpZ21hfVxcc3FydHsxIC0gaF97aWl9fSkkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJDw6FsY3VsbyBkbyByZXPDrWR1byBwYWRyb25pemFkbzogJHpfNSA9IFxcZnJhY3tlXzV9e1xcaGF0e1xcc2lnbWF9fSA9IFxcZnJhY3syLjV9ezEuMn0gXFxhcHByb3ggMi4wODMkLiIsICJDw6FsY3VsbyBkbyByZXPDrWR1byBzdHVkZW50aXphZG8gaW50ZXJubzogJHJfNSA9IFxcZnJhY3tlXzV9e1xcaGF0e1xcc2lnbWF9XFxzcXJ0ezEgLSBoX3s1NX19fSA9IFxcZnJhY3syLjV9ezEuMiBcXHNxcnR7MSAtIDAuNH19ID0gXFxmcmFjezIuNX17MS4yIFxcc3FydHswLjZ9fSBcXGFwcHJveCBcXGZyYWN7Mi41fXswLjkyOTV9IFxcYXBwcm94IDIuNjg5JC4iLCAiQ29tcGFyYcOnw6NvOiBPIHJlc8OtZHVvIHN0dWRlbnRpemFkbyAoJHJfNSBcXGFwcHJveCAyLjY5JCkgw6kgbWFpb3IgcXVlIG8gcGFkcm9uaXphZG8gKCR6XzUgXFxhcHByb3ggMi4wOCQpLCByZWZsZXRpbmRvIHF1ZSBvIHBvbnRvIHBvc3N1aSBhbHRhIGFsYXZhbmNhZ2VtLiBPIHJlc8OtZHVvIHN0dWRlbnRpemFkbyDDqSBtYWlzIGFkZXF1YWRvIHBvaXMgYWp1c3RhIGEgdmFyaWFiaWxpZGFkZSBsb2NhbCBkbyBlcnJvIGNhdXNhZGEgcGVsYSBnZW9tZXRyaWEgZG8gbW9kZWxvLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMi42ODl9LCB7ImVudW5jaWFkbyI6ICJEZW1vbnN0cmUgbWF0ZW1hdGljYW1lbnRlIGEgcmVsYcOnw6NvIGVudHJlIG8gcmVzw61kdW8gc3R1ZGVudGl6YWRvIGV4dGVybm8gKCR0X2kkKSBlIG8gaW50ZXJubyAoJHJfaSQpLiBFeHBsaXF1ZSBwb3IgcXVlIGVzc2EgcmVsYcOnw6NvIGRlcGVuZGUgZG8gdGVybW8gJHJfaV4yJC4iLCAiZGljYSI6ICJVc2UgYSBmw7NybXVsYSBmb3JuZWNpZGEgbm8gY29udGV4dG86ICR0X2kgPSByX2kgXFxzcXJ0e1xcZnJhY3tuIC0gcCAtIDF9e24gLSBwIC0gcl9pXjJ9fSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhcnRpbW9zIGRhIGRlZmluacOnw6NvIGRlIHJlc8OtZHVvIHN0dWRlbnRpemFkbyBleHRlcm5vOiAkdF9pID0gXFxmcmFje2VfaX17XFxoYXR7XFxzaWdtYX1feyhpKX1cXHNxcnR7MSAtIGhfe2lpfX19JC4iLCAiQSByZWxhw6fDo28gZW50cmUgYXMgZXN0aW1hdGl2YXMgZGUgdmFyacOibmNpYSDDqSBkYWRhIHBvciAkKG4gLSBwIC0gMSlcXGhhdHtcXHNpZ21hfV97KGkpfV4yID0gKG4gLSBwKVxcaGF0e1xcc2lnbWF9XjIgLSBlX2leMiAvICgxIC0gaF97aWl9KSQuIiwgIlN1YnN0aXR1aW5kbyBlIHJlYXJyYW5qYW5kbywgb2J0ZW1vczogJHRfaSA9IHJfaSBcXHNxcnR7XFxmcmFje24gLSBwIC0gMX17biAtIHAgLSByX2leMn19JC4iLCAiTyB0ZXJtbyAkcl9pXjIkIG5vIGRlbm9taW5hZG9yIGluZGljYSBxdWUgcXVhbmRvIG8gcmVzw61kdW8gaW50ZXJubyDDqSBncmFuZGUgKGluZGljYW5kbyB1bSBvdXRsaWVyIHBvdGVuY2lhbCksIG8gdGVybW8gJG4gLSBwIC0gcl9pXjIkIGRpbWludWksIGZhemVuZG8gY29tIHF1ZSBvIHJlc8OtZHVvIGV4dGVybm8gJHRfaSQgY3Jlc8OnYSBtYWlzIHJhcGlkYW1lbnRlIHF1ZSBvIGludGVybm8sIGF1bWVudGFuZG8gbyBwb2RlciBkZSBkZXRlY8Onw6NvIGRlIG91dGxpZXJzLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkZhcmF3YXksIEouIEouLCBMaW5lYXIgTW9kZWxzIHdpdGggUiwgQ2FwIDcsIHAuIDc1IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtIHByb2Zlc3NvciBkZXNlamEgYW5hbGlzYXIgYSBpbmZsdcOqbmNpYSBkYSBhbGF2YW5jYWdlbSAoJGhfe2lpfSQpIGVtIHVtIGNvbmp1bnRvIGRlIGRhZG9zIGRlICRuPTUwJCBvYnNlcnZhw6fDtWVzIGNvbSAkcD00JCBwcmVkaXRvcmVzLiBTZSB1bWEgb2JzZXJ2YcOnw6NvIGVzcGVjw61maWNhIGFwcmVzZW50YXIgJGhfe2lpfSA9IDAuMzUkLCBlbGEgZGV2ZSBzZXIgY29uc2lkZXJhZGEgZGUgYWx0YSBhbGF2YW5jYWdlbSBzZWd1bmRvIGEgcmVncmEgZGUgb3VybyAoJDJwL24kKT8gSnVzdGlmaXF1ZSBlIGluZGlxdWUgY29tbyBvIHVzbyBkbyByZXPDrWR1byBzdHVkZW50aXphZG8gYWx0ZXJhIGEgcGVyY2Vww6fDo28gZG8gZXJybyBwYXJhIGVzc2UgcG9udG8uIiwgImRpY2EiOiAiQ29tcGFyZSAkaF97aWl9JCBjb20gbyBsaW1pYXIgJDJwL24kIGUgYW5hbGlzZSBvIGVmZWl0byBkZSAkXFxzcXJ0ezEtaF97aWl9fSQgbm8gZGVub21pbmFkb3IgZG8gcmVzw61kdW8uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkxpbWlhciBkZSBhbGF2YW5jYWdlbTogJDJwL24gPSAyIFxcdGltZXMgNCAvIDUwID0gOCAvIDUwID0gMC4xNiQuIiwgIkFuw6FsaXNlOiBDb21vICQwLjM1ID4gMC4xNiQsIGEgb2JzZXJ2YcOnw6NvIHBvc3N1aSBhbHRhIGFsYXZhbmNhZ2VtIGUgZGV2ZSBzZXIgaW52ZXN0aWdhZGEuIiwgIkltcGFjdG8gbm8gcmVzw61kdW86IE8gcmVzw61kdW8gc3R1ZGVudGl6YWRvIMOpICRyX2kgPSBlX2kgLyAoXFxoYXR7XFxzaWdtYX1cXHNxcnR7MSAtIDAuMzV9KSA9IGVfaSAvIChcXGhhdHtcXHNpZ21hfVxcc3FydHswLjY1fSkgXFxhcHByb3ggZV9pIC8gKDAuODA2XFxoYXR7XFxzaWdtYX0pJC4iLCAiQ29uY2x1c8OjbzogTyBkZW5vbWluYWRvciByZWR1eiBhIGVzY2FsYSBkbyBlcnJvIGVtIGNlcmNhIGRlIDE5LDQlICgkMS0wLjgwNiQpLCBvIHF1ZSBhbXBsaWEgbyB2YWxvciBhYnNvbHV0byBkbyByZXPDrWR1byBzdHVkZW50aXphZG8gZW0gcmVsYcOnw6NvIGFvIHBhZHJvbml6YWRvLCB0b3JuYW5kbyBtYWlzIHZpc8OtdmVsIHF1YWxxdWVyIGRlc3ZpbyBhdMOtcGljbyBuZXNzYSBvYnNlcnZhw6fDo28uIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiRmFyYXdheSwgSi4gSi4sIExpbmVhciBNb2RlbHMgd2l0aCBSLCBDYXAgNywgcC4gNzQiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjE2fSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gJHkgPSBYXFxiZXRhICsgXFxEZWx0YSQuIEV4cGxpcXVlLCB1dGlsaXphbmRvIGEgZm9ybXVsYcOnw6NvIG1hdGVtw6F0aWNhIGRhIHZhcmnDom5jaWEgZG9zIHJlc8OtZHVvcywgcG9yIHF1ZSBhIGFsYXZhbmNhZ2VtICRoX3tpaX0kIChlbGVtZW50byBkYSBtYXRyaXogY2hhcMOpdSAkSCQpIGluZmx1ZW5jaWEgYSB2YXJpYWJpbGlkYWRlIGRvcyByZXPDrWR1b3MgJFxcaGF0e2V9X2kkIG1lc21vIHNvYiBhIHByZW1pc3NhIGRlIGhvbW9jZWRhc3RpY2lkYWRlLiIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSByZWxhw6fDo28gJFZhcihcXGhhdHtlfV9pKSA9IFxcc2lnbWFeMigxIC0gaF97aWl9KSQgZSBvIHF1ZSAkaF97aWl9JCByZXByZXNlbnRhIG5hIG1hdHJpeiBkZSBwcm9qZcOnw6NvICRIID0gWChYJ1gpXnstMX1YJyQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhcnRpbW9zIGRhIGRlZmluacOnw6NvIGRvIHJlc8OtZHVvOiAkXFxoYXR7ZX0gPSAoSSAtIEgpeSQuIiwgIkNvbW8gJHkgPSBYXFxiZXRhICsgXFxEZWx0YSQsIHRlbW9zICRcXGhhdHtlfSA9IChJIC0gSCkoWFxcYmV0YSArIFxcRGVsdGEpID0gKEkgLSBIKVhcXGJldGEgKyAoSSAtIEgpXFxEZWx0YSQuIiwgIkNvbW8gJChJIC0gSClYID0gMCQsIHNpbXBsaWZpY2Ftb3MgcGFyYSAkXFxoYXR7ZX0gPSAoSSAtIEgpXFxEZWx0YSQuIiwgIkEgdmFyacOibmNpYSBkZSB1bSB2ZXRvciDDqSAkVmFyKFxcaGF0e2V9KSA9IChJIC0gSClWYXIoXFxEZWx0YSkoSSAtIEgpJyA9IChJIC0gSCkoXFxzaWdtYV4yIEkpKEkgLSBIKScgPSBcXHNpZ21hXjIgKEkgLSBIKShJIC0gSCkkLiIsICJDb21vICRIJCDDqSBzaW3DqXRyaWNhIGUgaWRlbXBvdGVudGUsICRIXjIgPSBIJCwgbG9nbyAkVmFyKFxcaGF0e2V9KSA9IFxcc2lnbWFeMiAoSSAtIEgpJC4iLCAiUGFyYSB1bSBlbGVtZW50byBlc3BlY8OtZmljbyAkaSQsIHRlbW9zICRWYXIoXFxoYXR7ZX1faSkgPSBcXHNpZ21hXjIgKDEgLSBoX3tpaX0pJC4iLCAiSXNzbyBkZW1vbnN0cmEgcXVlIGEgdmFyaWFiaWxpZGFkZSBkbyByZXPDrWR1byBpbmRpdmlkdWFsICRcXGhhdHtlfV9pJCDDqSByZWR1emlkYSBwZWxhIGFsYXZhbmNhZ2VtICRoX3tpaX0kLCBvIHF1ZSBzaWduaWZpY2EgcXVlIHBvbnRvcyBjb20gYWx0YSBhbGF2YW5jYWdlbSBzw6NvICdmb3LDp2Fkb3MnIGEgdGVyIHJlc8OtZHVvcyBtZW5vcmVzLCBtZXNtbyBlbSBtb2RlbG9zIGhvbW9jZWTDoXN0aWNvcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJGYXJhd2F5LCBKLiBKLiwgTGluZWFyIE1vZGVscyB3aXRoIFIsIENhcCA3LjEsIHAuIDcxLTcyIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtIGVuZ2VuaGVpcm8gZGUgZGFkb3Mgb2JzZXJ2YSBxdWUsIGFvIHBsb3RhciBvcyByZXPDrWR1b3MgY29udHJhIG9zIHZhbG9yZXMgYWp1c3RhZG9zLCBhIGFtcGxpdHVkZSBkb3MgcmVzw61kdW9zIGRvYnJhIHF1YW5kbyBvcyB2YWxvcmVzIGFqdXN0YWRvcyBkb2JyYW0uIFByb3BvbmhhIHVtYSB0cmFuc2Zvcm1hw6fDo28gbWF0ZW3DoXRpY2EgcGFyYSBhIHZhcmnDoXZlbCByZXNwb3N0YSAkeSQgY2FwYXogZGUgZXN0YWJpbGl6YXIgYSB2YXJpw6JuY2lhIGUgZXhwbGlxdWUgbyBwb3JxdcOqIGRlc3RhIGVzY29saGEgYmFzZWFkYSBuYSByZWxhw6fDo28gZW50cmUgJFZhcih5KSQgZSAkRSh5KSQuIiwgImRpY2EiOiAiQ29uc2lkZXJlIHF1ZSBzZSAkVmFyKHkpIFxccHJvcHRvIFtFKHkpXV4yJCwgdW1hIHRyYW5zZm9ybWHDp8OjbyBsb2dhcsOtdG1pY2Egw6kgcmVjb21lbmRhZGEuIFNlICRWYXIoeSkgXFxwcm9wdG8gRSh5KSQsIHVzZSBhIHJhaXogcXVhZHJhZGEuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlNlIGEgYW1wbGl0dWRlIGRvcyByZXPDrWR1b3MgZG9icmEgcXVhbmRvIG8gdmFsb3IgYWp1c3RhZG8gZG9icmEsIHRlbW9zICRTRCh5KSBcXHByb3B0byBFKHkpJCwgbG9nbyAkVmFyKHkpIFxccHJvcHRvIFtFKHkpXV4yJC4iLCAiQSBlc3RhYmlsaXphw6fDo28gZGEgdmFyacOibmNpYSBleGlnZSB1bWEgdHJhbnNmb3JtYcOnw6NvICRoKHkpJCB0YWwgcXVlICRWYXIoaCh5KSkkIHNlamEgY29uc3RhbnRlLiIsICJQZWxvIG3DqXRvZG8gZGVsdGEsICRWYXIoaCh5KSkgXFxhcHByb3ggW2gnKEUoeSkpXV4yIFZhcih5KSQuIiwgIlBhcmEgc2VyIGNvbnN0YW50ZSwgcHJlY2lzYW1vcyBkZSAkaCcoRSh5KSkgXFxwcm9wdG8gW1Zhcih5KV1eey0xLzJ9ID0gW0UoeSldXnstMX0gPSAxL0UoeSkkLiIsICJJbnRlZ3JhbmRvLCBvYnRlbW9zICRoKHkpID0gXFxpbnQgXFxmcmFjezF9e3l9IGR5ID0gXFxsbih5KSQuIiwgIlBvcnRhbnRvLCBhIHRyYW5zZm9ybWHDp8OjbyBsb2dhcsOtdG1pY2Egw6kgYSBtYWlzIGluZGljYWRhIHBhcmEgZXN0YWJpbGl6YXIgdmFyacOibmNpYXMgcXVlIGNyZXNjZW0gcHJvcG9yY2lvbmFsbWVudGUgYW8gcXVhZHJhZG8gZGEgbcOpZGlhLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkZhcmF3YXksIEouIEouLCBMaW5lYXIgTW9kZWxzIHdpdGggUiwgQ2FwIDcuNiwgcC4gODQiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGFkYSBhIGFtb3N0cmEgZGUgcmVzw61kdW9zIGRlIHVtIG1vZGVsbyBkZSByZWdyZXNzw6NvLCByZWFsaXplIGEgYW7DoWxpc2UgZGUgdmFyacOibmNpYSBlbnRyZSBkb2lzIHN1YmdydXBvcyBkZWZpbmlkb3MgcGVsYSBtZWRpYW5hIGRvcyB2YWxvcmVzIGFqdXN0YWRvcyAoJFxcaGF0e3l9X2kkKS4gU2UgYXMgdmFyacOibmNpYXMgYW1vc3RyYWlzIHPDo28gJFNfMV4yID0gMjUkIGUgJFNfMl4yID0gMTAkLCBjb20gJG5fMSA9IDIwJCBlICRuXzIgPSAyMCQgb2JzZXJ2YcOnw7VlcywgY2FsY3VsZSBhIGVzdGF0w61zdGljYSAkRl97XFx0ZXh0e2NhbGN9fSQgZSBpbmRpcXVlIHNlIGjDoSBldmlkw6puY2lhIGRlIGhldGVyb2NlZGFzdGljaWRhZGUgKCRGX3tcXHRleHR7Y3JpdH19IFxcYXBwcm94IDIuMTIkIHBhcmEgJFxcYWxwaGEgPSAwLjA1JCkuIiwgImRpY2EiOiAiQSBlc3RhdMOtc3RpY2EgJEYkIHBhcmEgY29tcGFyYcOnw6NvIGRlIHZhcmnDom5jaWFzIMOpIGEgcmF6w6NvIGVudHJlIGEgbWFpb3IgZSBhIG1lbm9yIHZhcmnDom5jaWE6ICRGID0gU197bWFpb3J9XjIgLyBTX3ttZW5vcn1eMiQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIklkZW50aWZpY2HDp8OjbyBkYXMgdmFyacOibmNpYXM6ICRTXzFeMiA9IDI1JCBlICRTXzJeMiA9IDEwJC4iLCAiQ8OhbGN1bG8gZGEgZXN0YXTDrXN0aWNhICRGX3tcXHRleHR7Y2FsY319ID0gXFxmcmFje1NfMV4yfXtTXzJeMn0gPSBcXGZyYWN7MjV9ezEwfSA9IDIuNSQuIiwgIkdyYXVzIGRlIGxpYmVyZGFkZTogJGdsX3tcXHRleHR7bnVtfX0gPSAxOSQsICRnbF97XFx0ZXh0e2Rlbn19ID0gMTkkLiIsICJDb21wYXJhw6fDo286IENvbW8gJEZfe1xcdGV4dHtjYWxjfX0gPSAyLjUgPiBGX3tcXHRleHR7Y3JpdH19ID0gMi4xMiQsIHJlamVpdGFtb3MgYSBoaXDDs3Rlc2UgbnVsYSBkZSBpZ3VhbGRhZGUgZGUgdmFyacOibmNpYXMuIiwgIkNvbmNsdXPDo286IEjDoSBldmlkw6puY2lhIGVzdGF0w61zdGljYSBkZSBoZXRlcm9jZWRhc3RpY2lkYWRlIGVudHJlIG9zIGRvaXMgZ3J1cG9zLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMi41fSwgeyJlbnVuY2lhZG8iOiAiRGFkbyB1bSBtb2RlbG8gbGluZWFyIGNvbSAkbj0xMDAkIG9ic2VydmHDp8O1ZXMgZSBtYXRyaXogY2hhcMOpdSAkSCQsIG9uZGUgbyB2ZXRvciBkZSByZXPDrWR1b3Mgw6kgZGVmaW5pZG8gcG9yICRlID0gKEkgLSBIKXkkLCBkZW1vbnN0cmUgbWF0ZW1hdGljYW1lbnRlIGEgZXNwZXJhbsOnYSBlIGEgdmFyacOibmNpYSBkbyB2ZXRvciBkZSByZXPDrWR1b3MgJGUkLCBhc3N1bWluZG8gcXVlIG8gbW9kZWxvIHNlZ3VlIGEgc3Vwb3Npw6fDo28gZGUgbm9ybWFsaWRhZGUgJHkgXFxzaW0gTl9uKFhcXHRoZXRhLCBJXFxzaWdtYV4yKSQuIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhcyBwcm9wcmllZGFkZXMgZGUgbGluZWFyaWRhZGUgZGEgZXNwZXJhbsOnYSBlIGRhIHZhcmnDom5jaWEgcGFyYSB0cmFuc2Zvcm1hw6fDtWVzIGxpbmVhcmVzIGRlIHZldG9yZXMgYWxlYXTDs3Jpb3M6ICRWYXIoQXkpID0gQSBWYXIoeSkgQSckLiBVc2UgbyBmYXRvIGRlIHF1ZSAkKEktSClYID0gMCQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhcmEgYSBlc3BlcmFuw6dhOiAkRVtlXSA9IEVbKEktSCl5XSA9IChJLUgpRVt5XSQuIiwgIkNvbW8gJEVbeV0gPSBYXFx0aGV0YSQsIHRlbW9zICQoSS1IKVhcXHRoZXRhID0gKFggLSBIIFgpXFx0aGV0YSQuIiwgIlBlbGEgZGVmaW5pw6fDo28gZGEgbWF0cml6IGNoYXDDqXUsICRIID0gWChYJ1gpXnstMX1YJyQsIGxvZ28gJEhYID0gWChYJ1gpXnstMX1YJ1ggPSBYKEkpID0gWCQuIiwgIkFzc2ltLCAkRVtlXSA9IChYIC0gWClcXHRoZXRhID0gMCQuIiwgIlBhcmEgYSB2YXJpw6JuY2lhOiAkVmFyKGUpID0gVmFyKChJLUgpeSkgPSAoSS1IKSBWYXIoeSkgKEktSCknJC4iLCAiRGFkbyAkVmFyKHkpID0gSVxcc2lnbWFeMiQsIHRlbW9zICRcXHNpZ21hXjIoSS1IKShJLUgpJyQuIiwgIkNvbW8gJEgkIMOpIHNpbcOpdHJpY2EgKCRIPUgnJCkgZSBpZGVtcG90ZW50ZSAoJEheMj1IJCksICQoSS1IKShJLUgpID0gSSAtIDJIICsgSF4yID0gSSAtIEgkLiIsICJQb3J0YW50bywgJFZhcihlKSA9IFxcc2lnbWFeMihJLUgpJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSBvIHByb2NlZGltZW50byBkZSBjb25zdHJ1w6fDo28gZG8gZ3LDoWZpY28gUS1RIHBsb3QgcGFyYSByZXPDrWR1b3MuIENvbW8gc2UgZGV2ZSBpbnRlcnByZXRhciBvIGFsaW5oYW1lbnRvIGRvcyBwb250b3MgJChcXFBoaV57LTF9KFxcZnJhY3tpfXtuKzF9KSwgZV97W2ldfSkkIGNhc28gb3MgcmVzw61kdW9zIGFwcmVzZW50ZW0gdW1hIGRpc3RyaWJ1acOnw6NvIGNvbSBjYXVkYXMgcGVzYWRhcyAoZXg6IGRpc3RyaWJ1acOnw6NvIHQgZGUgU3R1ZGVudCBjb20gcG91Y29zIGdyYXVzIGRlIGxpYmVyZGFkZSk/IiwgImRpY2EiOiAiQ29uc2lkZXJlIG8gY29tcG9ydGFtZW50byBkYSBmdW7Dp8OjbyBxdWFudGlsIGRhIG5vcm1hbCAoJFxcUGhpXnstMX0kKSBlIGNvbW8gZWxhIG1hcGVpYSBvcyBkYWRvcyBvYnNlcnZhZG9zIGVtIHJlbGHDp8OjbyDDoCBkaXN0cmlidWnDp8OjbyB0ZcOzcmljYSBlc3BlcmFkYS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gT3JkZW5hw6fDo286IE9yZGVuYXIgb3MgcmVzw61kdW9zIGNhbGN1bGFkb3MgZGUgZm9ybWEgcXVlICRlX3tbMV19IFxcbGUgZV97WzJdfSBcXGxlIFxcZG90cyBcXGxlIGVfe1tuXX0kLiIsICIyLiBRdWFudGlzIFRlw7NyaWNvczogQ2FsY3VsYXIgJHVfaSA9IFxcUGhpXnstMX0oXFxmcmFje2l9e24rMX0pJCBwYXJhIGNhZGEgJGk9MSwgXFxkb3RzLCBuJCwgcmVwcmVzZW50YW5kbyBvcyBxdWFudGlzIGRhIG5vcm1hbCBwYWRyw6NvLiIsICIzLiBQbG90YWdlbTogQ29uc3RydWlyIG8gZ3LDoWZpY28gZGUgZGlzcGVyc8OjbyBjb20gcGFyZXMgJCh1X2ksIGVfe1tpXX0pJC4iLCAiNC4gSW50ZXJwcmV0YcOnw6NvOiBQb250b3MgYWxpbmhhZG9zIHNvYnJlIHVtYSByZXRhIGluZGljYW0gcXVlIG9zIHJlc8OtZHVvcyBzZWd1ZW0gdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbC4iLCAiNS4gQ2F1ZGFzIFBlc2FkYXM6IFNlIGEgZGlzdHJpYnVpw6fDo28gZG9zIHJlc8OtZHVvcyB0aXZlciBjYXVkYXMgbWFpcyBwZXNhZGFzIHF1ZSBhIG5vcm1hbCwgbyBRLVEgcGxvdCBhcHJlc2VudGFyw6EgdW1hIGZvcm1hIGRlICdTJyAoY3VydmF0dXJhKSwgb25kZSBvcyByZXPDrWR1b3MgbWFpcyBiYWl4b3Mgc8OjbyBtZW5vcmVzIHF1ZSBvIHF1YW50aWwgbm9ybWFsIGNvcnJlc3BvbmRlbnRlIGUgb3MgbWFpcyBhbHRvcyBzw6NvIG1haW9yZXMuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG4jIFNpbXVsYW5kbyByZXPDrWR1b3MgY29tIGNhdWRhcyBwZXNhZGFzIChkaXN0cmlidWnDp8OjbyB0KVxucmVzX3Blc2Fkb3MgPSBucC5yYW5kb20uc3RhbmRhcmRfdChkZj0zLCBzaXplPTEwMClcbnJlc19wZXNhZG9zLnNvcnQoKVxudGhlb3JldGljYWxfcSA9IHN0YXRzLm5vcm0ucHBmKG5wLmxpbnNwYWNlKDAuMDEsIDAuOTksIDEwMCkpXG5cbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXRoZW9yZXRpY2FsX3EsIHk9cmVzX3Blc2Fkb3MsIG1vZGU9J21hcmtlcnMnLCBuYW1lPSdSZXPDrWR1b3MgKENhdWRhcyBQZXNhZGFzKScsIG1hcmtlcj1kaWN0KGNvbG9yPScjMDAwMEZGJykpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9Wy0yLCAyXSwgeT1bLTIsIDJdLCBtb2RlPSdsaW5lcycsIG5hbWU9J05vcm1hbCBUZcOzcmljYScsIGxpbmU9ZGljdChjb2xvcj0nI0ZGMDAwMCcsIGRhc2g9J2Rhc2gnKSkpXG5cbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5RLVEgUGxvdDogRGlzdHJpYnVpw6fDo28gZGUgQ2F1ZGFzIFBlc2FkYXM8L2I+JywgeGF4aXNfdGl0bGU9J1F1YW50aXMgVGXDs3JpY29zJywgeWF4aXNfdGl0bGU9J1Jlc8OtZHVvcyBPcmRlbmFkb3MnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCA3IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bSBjb25qdW50byBkZSBkYWRvcyBvbmRlIHNlIHN1c3BlaXRhIHF1ZSBhIHZhcmnDom5jaWEgZG8gZXJybyBuw6NvIMOpIGNvbnN0YW50ZSwgbWFzIHNpbSB1bWEgZnVuw6fDo28gZGEgbcOpZGlhIHByZWRpdGEgKCRWYXIoXFxEZWx0YSkgXFxwcm9wdG8gRVtZXV4yJCkuIFNlIHZvY8OqIGFwbGljYXNzZSB1bWEgdHJhbnNmb3JtYcOnw6NvIGxvZ2Fyw610bWljYSAoJFleKiA9IFxcbG9nKFkpJCksIHF1YWwgc2VyaWEgbyBpbXBhY3RvIGVzcGVyYWRvIG5hIGRpc3RyaWJ1acOnw6NvIGRvcyByZXPDrWR1b3MgZSBwb3IgcXVlIGlzc28gw6kgcmVsZXZhbnRlIHBhcmEgYSB2ZXJpZmljYcOnw6NvIGRlIG5vcm1hbGlkYWRlIHZpYSBRLVEgcGxvdD8iLCAiZGljYSI6ICJMZW1icmUtc2UgZGEgdMOpY25pY2EgZGUgZXN0YWJpbGl6YcOnw6NvIGRlIHZhcmnDom5jaWEgZSBjb21vIGEgbm9ybWFsaWRhZGUgw6kgdW1hIHN1cG9zacOnw6NvIHF1ZSBwb2RlIHNlciBhZmV0YWRhIHBlbGEgZXNjYWxhIGRhIHZhcmnDoXZlbCByZXNwb3N0YS4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gTyBtb2RlbG8gb3JpZ2luYWwgcG9zc3VpIGhldGVyb2NlZGFzdGljaWRhZGU6ICRWYXIoWSkgXFxhcHByb3ggXFxzaWdtYV4yIFxcbXVeMiQuIiwgIjIuIEEgdHJhbnNmb3JtYcOnw6NvIGxvZ2Fyw610bWljYSAkWV4qID0gXFxsb2coWSkkIGFwbGljYSBhIHByb3ByaWVkYWRlIGRlIGVzdGFiaWxpemHDp8OjbyBkZSB2YXJpw6JuY2lhOiAkVmFyKGxvZyhZKSkgXFxhcHByb3ggKFxcZnJhY3tkfXtkXFxtdX0gbG9nKFxcbXUpKV4yIFZhcihZKSA9IChcXGZyYWN7MX17XFxtdX0pXjIgKFxcc2lnbWFeMiBcXG11XjIpID0gXFxzaWdtYV4yJC4iLCAiMy4gQW8gZXN0YWJpbGl6YXIgYSB2YXJpw6JuY2lhLCBvIGNvbXBvbmVudGUgZGUgZXJybyBkbyBtb2RlbG8gcGFzc2EgYSB0ZXIgdmFyacOibmNpYSBjb25zdGFudGUsIHNhdGlzZmF6ZW5kbyBhIHByZW1pc3NhIGRlIGhvbW9jZWRhc3RpY2lkYWRlLiIsICI0LiBGcmVxdWVudGVtZW50ZSwgYSB0cmFuc2Zvcm1hw6fDo28gbG9nYXLDrXRtaWNhIHRhbWLDqW0gY29ycmlnZSBhc3NpbWV0cmlhcyBwb3NpdGl2YXMsIGFwcm94aW1hbmRvIGEgZGlzdHJpYnVpw6fDo28gZG9zIGVycm9zIGRlIHVtYSBub3JtYWwuIiwgIjUuIENvbnNlcXVlbnRlbWVudGUsIG5vIFEtUSBwbG90LCBvcyByZXPDrWR1b3MgZG8gbW9kZWxvIHRyYW5zZm9ybWFkbyB0ZW5kZW0gYSBhcHJlc2VudGFyIHVtIGFsaW5oYW1lbnRvIGxpbmVhciBtYWlzIHByw7N4aW1vIGFvIGVzcGVyYWRvIHNvYiBub3JtYWxpZGFkZSwgZmFjaWxpdGFuZG8gbyBkaWFnbsOzc3RpY28gdmlzdWFsLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIldvb2xkcmlkZ2UsIEludHJvZHXDp8OjbyDDoCBFY29ub21ldHJpYSwgQ2FwIDYiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGFkYSBhIGbDs3JtdWxhIGRlIGVxdWl2YWzDqm5jaWEgZGEgRGlzdMOibmNpYSBkZSBDb29rOiAkRF97aX0gPSBcXGZyYWN7ZV9pXjJ9e3AgXFxmcmFje1NRX3tSZXN9fXtuIC0gcH19IFxcZnJhY3toX3tpaX19eygxIC0gaF97aWl9KV4yfSQsIGRlbW9uc3RyZSBhbGdlYnJpY2FtZW50ZSBjb21vIGEgYWxhdmFuY2FnZW0gJGhfe2lpfSQgaXNvbGFkYW1lbnRlIHBvZGUgaW5mbGFyIGEgZGlzdMOibmNpYSBkZSBDb29rIG1lc21vIHBhcmEgdW0gcG9udG8gb25kZSBvIHJlc8OtZHVvICRlX2kkIMOpIHBlcXVlbm8uIiwgImRpY2EiOiAiQW5hbGlzZSBvIGxpbWl0ZSBkYSBmdW7Dp8OjbyAkZihoX3tpaX0pID0gXFxmcmFje2hfe2lpfX17KDEgLSBoX3tpaX0pXjJ9JCBxdWFuZG8gJGhfe2lpfSQgdGVuZGUgYSAxLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBPYnNlcnZhbW9zIHF1ZSAkRF9pJCDDqSBwcm9kdXRvIGRlIGRvaXMgdGVybW9zOiAkQSA9IFxcZnJhY3tlX2leMn17cCBcXGZyYWN7U1Ffe1Jlc319e24gLSBwfX0kIChiYXNlYWRvIG5vIHJlc8OtZHVvKSBlICRCID0gXFxmcmFje2hfe2lpfX17KDEgLSBoX3tpaX0pXjJ9JCAoYmFzZWFkbyBuYSBhbGF2YW5jYWdlbSkuIiwgIjIuIFF1YW5kbyBhIGFsYXZhbmNhZ2VtICRoX3tpaX0gXFx0byAxJCwgbyBkZW5vbWluYWRvciBkbyB0ZXJtbyAkQiQsIHF1ZSDDqSAkKDEgLSBoX3tpaX0pXjIkLCB0ZW5kZSBhIDAgbXVpdG8gcmFwaWRhbWVudGUuIiwgIjMuIENvbW8gY29uc2VxdcOqbmNpYSwgbyB0ZXJtbyAkQiQgdGVuZGUgYW8gaW5maW5pdG86ICRcXGxpbV97aF97aWl9IFxcdG8gMX0gXFxmcmFje2hfe2lpfX17KDEgLSBoX3tpaX0pXjJ9ID0gXFxpbmZ0eSQuIiwgIjQuIE1lc21vIHF1ZSBvIHJlc8OtZHVvICRlX2kkIHNlamEgbXVpdG8gcGVxdWVubywgdG9ybmFuZG8gbyB0ZXJtbyAkQSQgcHLDs3hpbW8gZGUgemVybywgbyBwcm9kdXRvICRBIFxcY2RvdCBCJCBwb2RlIHJlc3VsdGFyIGVtIHZhbG9yZXMgZ3JhbmRlcyBzZSBhIGNvbnZlcmfDqm5jaWEgZG8gdGVybW8gZGUgYWxhdmFuY2FnZW0gZm9yIGRvbWluYW50ZSwgY2FyYWN0ZXJpemFuZG8gYSBvYnNlcnZhw6fDo28gY29tbyBpbmZsdWVudGUuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtIG1vZGVsbyBjb20gJG49MjAkIG9ic2VydmHDp8O1ZXMgZSAkcD0yJCBwYXLDom1ldHJvcy4gVW1hIG9ic2VydmHDp8OjbyBlc3BlY8OtZmljYSBwb3NzdWkgJGVfaSA9IDAuNSQsICRTUV97UmVzfSA9IDEwJCwgZSAkaF97aWl9ID0gMC44JC4gQ2FsY3VsZSBhIERpc3TDom5jaWEgZGUgQ29vayAoJERfaSQpIHBhcmEgZXN0YSBvYnNlcnZhw6fDo28uIiwgImRpY2EiOiAiVXNlIGEgZsOzcm11bGEgJERfe2l9ID0gXFxmcmFje2VfaV4yfXtwIFxcZnJhY3tTUV97UmVzfX17biAtIHB9fSBcXGZyYWN7aF97aWl9fXsoMSAtIGhfe2lpfSleMn0kIGUgc3Vic3RpdHVhIG9zIHZhbG9yZXMgZm9ybmVjaWRvcyBjb20gY2F1dGVsYSBuYSBvcmRlbSBkZSBvcGVyYcOnw7Vlcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYXIgb3MgcGFyw6JtZXRyb3M6ICRuID0gMjAsIHAgPSAyLCBlX2kgPSAwLjUsIFNRX3tSZXN9ID0gMTAsIGhfe2lpfSA9IDAuOCQuIiwgIjIuIENhbGN1bGFyIGEgdmFyacOibmNpYSByZXNpZHVhbCBlc3RpbWFkYTogJFxcZnJhY3tTUV97UmVzfX17biAtIHB9ID0gXFxmcmFjezEwfXsyMCAtIDJ9ID0gXFxmcmFjezEwfXsxOH0gXFxhcHByb3ggMC41NTU2JC4iLCAiMy4gQ2FsY3VsYXIgbyB0ZXJtbyBkZSByZXPDrWR1bzogJFxcZnJhY3tlX2leMn17cCBcXGNkb3QgMC41NTU2fSA9IFxcZnJhY3swLjVeMn17MiBcXGNkb3QgMC41NTU2fSA9IFxcZnJhY3swLjI1fXsxLjExMTF9ID0gMC4yMjUkLiIsICI0LiBDYWxjdWxhciBvIHRlcm1vIGRlIGFsYXZhbmNhZ2VtOiAkXFxmcmFje2hfe2lpfX17KDEgLSBoX3tpaX0pXjJ9ID0gXFxmcmFjezAuOH17KDEgLSAwLjgpXjJ9ID0gXFxmcmFjezAuOH17MC4yXjJ9ID0gXFxmcmFjezAuOH17MC4wNH0gPSAyMCQuIiwgIjUuIENhbGN1bGFyICREX2kkOiAkMC4yMjUgXFxjZG90IDIwID0gNC41JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDQuNX0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCBzb2IgYSDDs3RpY2EgZGEgbWF0cml6IGRlIHByb2plw6fDo28gJEggPSBYKFheVFgpXnstMX1YXlQkLCBwb3IgcXVlIGVsZW1lbnRvcyBkYSBkaWFnb25hbCBwcmluY2lwYWwgJGhfe2lpfSQgc8OjbyBsaW1pdGFkb3MgYW8gaW50ZXJ2YWxvICRbMCwgMV0kIGUgcXVhbCBvIHNpZ25pZmljYWRvIGRlIHVtYSBvYnNlcnZhw6fDo28gY29tICRoX3tpaX0gPSAxL24kIGNvbXBhcmFkYSBhIHVtYSBjb20gJGhfe2lpfSBcXGFwcHJveCAxJC4iLCAiZGljYSI6ICJBIG1hdHJpeiAkSCQgw6kgaWRlbXBvdGVudGUgKCRIXjIgPSBIJCkuIFBlbnNlIG5vIHZhbG9yIGVzcGVyYWRvIGRlICRoX3tpaX0gPSBcdGV4dHt0cn0oSCkvbiQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIEEgbWF0cml6ICRIJCDDqSBhIG1hdHJpeiBkZSBwcm9qZcOnw6NvIG9ydG9nb25hbCwgbyBxdWUgaW1wbGljYSBlbSAkSF4yID0gSCQuIiwgIjIuIENvbW8gJEgkIMOpIHNpbcOpdHJpY2EgZSBpZGVtcG90ZW50ZSwgc2V1cyBhdXRvdmFsb3JlcyBzw6NvIDAgb3UgMSwgbyBxdWUgZ2FyYW50ZSBxdWUgJDAgXFxsZSBoX3tpaX0gXFxsZSAxJC4iLCAiMy4gTyB2YWxvciBtw6lkaW8gZGUgJGhfe2lpfSQgw6kgZGFkbyBwb3IgJFxcZnJhY3tcXHRleHR7dHJ9KEgpfXtufSA9IFxcZnJhY3twfXtufSQsIG9uZGUgJHAkIMOpIG8gbsO6bWVybyBkZSBwYXLDom1ldHJvcy4iLCAiNC4gVW0gcG9udG8gY29tICRoX3tpaX0gPSBwL24kIChvdSAkMS9uJCBzZSBjb25zaWRlcmFybW9zIGFwZW5hcyB1bSBwcmVkaXRvciBlIG8gaW50ZXJjZXB0bykgcmVwcmVzZW50YSB1bWEgb2JzZXJ2YcOnw6NvIGNvbSBhbGF2YW5jYWdlbSB0w61waWNhIG91ICdtw6lkaWEnLiIsICI1LiBVbSBwb250byBjb20gJGhfe2lpfSBcXGFwcHJveCAxJCDDqSB1bWEgb2JzZXJ2YcOnw6NvIGV4dHJlbWEgbm8gZXNwYcOnbyBkb3MgcHJlZGl0b3JlcywgcG9zc3VpbmRvIGluZmx1w6puY2lhIGdlb23DqXRyaWNhIG3DoXhpbWEsIG8gcXVlIHNpZ25pZmljYSBxdWUgbyB2YWxvciAkWV9pJCBuZXN0YSBwb3Npw6fDo28gZGl0YSBvIGNvbXBvcnRhbWVudG8gbG9jYWwgZGEgc3VwZXJmw61jaWUgZGUgcmVncmVzc8Ojby4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9XX0=').decode('utf-8'))


    import plotly.graph_objects as go
    import numpy as np
    import scipy.stats as stats
    
    # Garantir que o estado da sessão exista
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Calcular progresso total
    mcq_list = dados_exercicios.get("questoes_multipla_escolha", [])
    disc_list = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcq_list) + len(disc_list)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v is True)
    
    # Barra de progresso e estatísticas
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    
    st.divider()
    
    # --- Seção de Questões de Múltipla Escolha ---
    if mcq_list:
        st.subheader("📝 Questões de Múltipla Escolha")
        for i, questao in enumerate(mcq_list):
            with st.container(border=True):
                st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
                
                # Referência do Livro
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
    
                # Renderização de Gráfico Plotly
                code_plotly = questao.get("codigo_plotly")
                if code_plotly:
                    local_vars = {"go": go, "np": np, "stats": stats, "fig": None}
                    try:
                        exec(code_plotly, globals(), local_vars)
                        if local_vars.get("fig"):
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_mcq_{i}")
                    except Exception as e:
                        st.warning("Gráfico não disponível ou erro na renderização.")
    
                # Alternativas
                opcoes = questao.get("alternativas", {})
                selecao = st.radio(
                    "Escolha uma alternativa:",
                    options=list(opcoes.keys()),
                    format_func=lambda x: f"{x}: {opcoes[x]}",
                    key=f"radio_mcq_{i}",
                    index=None
                )
    
                # Dica
                if st.button("💡 Ver Dica", key=f"btn_dica_mcq_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
    
                # Verificação
                if st.button("✅ Verificar Resposta", key=f"btn_check_mcq_{i}"):
                    if selecao == questao.get("alternativa_correta"):
                        st.success("Correto! Muito bem.")
                        st.session_state.respostas_certas[f"mcq_{i}"] = True
                        st.rerun()
                    else:
                        st.error("Resposta incorreta. Tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
    
                # Gabarito Comentado
                with st.expander("✅ Ver Gabarito Comentado"):
                    st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
    
    st.divider()
    
    # --- Seção de Questões Discursivas ---
    if disc_list:
        st.subheader("✍️ Questões Discursivas e Analíticas")
        for i, questao in enumerate(disc_list):
            with st.container(border=True):
                st.markdown(f"**Desafio {i+1}:** {questao.get('enunciado', '')}")
                
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
    
                st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
    
                # Gráfico Plotly
                code_plotly = questao.get("codigo_plotly")
                if code_plotly:
                    local_vars = {"go": go, "np": np, "stats": stats, "fig": None}
                    try:
                        exec(code_plotly, globals(), local_vars)
                        if local_vars.get("fig"):
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
                    except Exception as e:
                        pass
    
                # Validação Numérica se necessário
                valor_esperado = questao.get("resposta_numerica_esperada")
                if valor_esperado is not None:
                    val_input = st.number_input("Digite o resultado numérico para validação:", key=f"num_disc_{i}", format="%.4f")
                    if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                        if abs(val_input - valor_esperado) <= max(0.01, 0.01 * abs(valor_esperado)):
                            st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                            st.session_state.respostas_certas[f"disc_{i}"] = True
                            st.rerun()
                        else:
                            st.error("O valor calculado difere do gabarito oficial. Revise seus cálculos.")
                            st.session_state.respostas_certas[f"disc_{i}"] = False
                else:
                    # Validação qualitativa simples
                    if st.checkbox("Marque aqui após responder esta questão", key=f"check_disc_{i}"):
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                    else:
                        st.session_state.respostas_certas[f"disc_{i}"] = False
    
                # Dica e Gabarito
                if st.button("💡 Ver Dica", key=f"btn_dica_disc_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
                
                with st.expander("✅ Ver Resolução Detalhada"):
                    for passo in questao.get("gabarito_passo_a_passo", []):
                        st.write(f"- {passo}")
