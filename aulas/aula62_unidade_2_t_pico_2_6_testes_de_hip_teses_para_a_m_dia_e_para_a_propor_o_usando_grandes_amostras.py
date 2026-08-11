import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNjogVGVzdGVzIGRlIGhpcMOzdGVzZXMgcGFyYSBhIG3DqWRpYSBlIHBhcmEgYSBwcm9wb3LDp8OjbyB1c2FuZG8gZ3JhbmRlcyBhbW9zdHJhcyIsICJyZWZlcmVuY2lhc19iaWJsaW9ncmFmaWNhc19maW5haXMiOiBbIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSAtIENhcC4gMTIsIHBwLiAzMzgtMzUzIl19').decode('utf-8'))

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
    import scipy.stats as stats
    
    # Configuração da página e estilos (Injeção de estilo CSS para aparência de luxo)
    st.markdown(r"""
        <style>
        .big-font { font-size: 20px !important; color: #1E293B; }
        .highlight { background-color: #F8FAFC; padding: 20px; border-radius: 10px; border-left: 5px solid #1E3A8A; }
        </style>
        """, unsafe_allow_html=True)
    
    # 1. CABEÇALHO DO SUBTÓPICO
    st.header(r"Fundamentos do Teste de Hipóteses: A Lógica da Inferência Estatística")
    
    # 2. DISCUSSÃO TEÓRICA
    st.markdown(r"""
    O teste de hipóteses constitui a pedra angular da inferência estatística, funcionando como um tribunal probabilístico para avaliar afirmações sobre parâmetros populacionais. Em aplicações industriais e científicas, partimos de uma crença estabelecida, o *status quo*, denominada hipótese nula.
    """)
    
    st.info(r"A dúvida surge ao observar dados experimentais que parecem contradizer essa premissa. O teste provê uma estrutura rigorosa para verificar se tais discrepâncias constituem meras flutuações amostrais ou evidências sólidas para rejeição.")
    
    st.markdown(r"""
    Ao decidir entre o *status quo* e uma nova evidência, enfrentamos dois riscos fundamentais:
    - **Erro do Tipo I ($\alpha$):** Rejeitamos uma hipótese nula que é, na realidade, verdadeira. É o "falso positivo" da estatística.
    - **Erro do Tipo II ($\beta$):** Falhamos em rejeitar uma hipótese nula que é, na realidade, falsa. Representa uma falha de detecção de um efeito real.
    """)
    
    # 3. FORMALISMO MATEMÁTICO
    st.subheader(r"📐 O Coração Matemático: Formalismo do Teste de Hipóteses")
    st.latex(r"H_0: \theta = \theta_0 \quad \text{vs} \quad H_1: \theta \neq \theta_0")
    st.latex(r"\alpha = P(\text{Rejeitar } H_0 | H_0 \text{ verdadeira})")
    st.latex(r"RC = \{ \hat{\theta} \in \mathbb{R} | P(\text{Rejeitar } H_0 | H_0) = \alpha \}")
    
    # 4. DEMONSTRAÇÃO ANALÍTICA
    st.subheader(r"🧮 Dedução Analítica e Propriedades")
    st.markdown(r"A construção do teste segue um fluxo lógico rigoroso para o controle de erro:")
    st.latex(r"P(\text{Erro I}) = P(\hat{\theta} \in RC | H_0 \text{ é verdadeira}) = \alpha")
    st.markdown(r"Considerando a distribuição de amostragem sob normalidade:")
    st.latex(r"\text{Sob } H_0 \text{ verdadeira, } \hat{\theta} \sim N(\theta_0, \sigma^2/n)")
    st.markdown(r"Definição dos pontos críticos para um teste bilateral:")
    st.latex(r"\text{Para um teste bilateral: } P(\hat{\theta} < c_1) = \alpha/2 \text{ e } P(\hat{\theta} > c_2) = \alpha/2")
    st.markdown(r"A regra de decisão final baseada na região crítica:")
    st.latex(r"\text{Regra de decisão: Rejeitar } H_0 \text{ se } \hat{\theta} < c_1 \text{ ou } \hat{\theta} > c_2")
    
    # 5. EXEMPLOS PRÁTICOS
    st.subheader(r"📈 Casos de Aplicação Prática: Controle de Qualidade Industrial")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Verificação de Resistência em Linha de Parafusos")
        st.markdown(r"Uma indústria afirma que sua linha de produção mantém uma resistência média de 155 kg. Suspeita-se de desregulação. Coleta-se $n = 25$ parafusos, resultando em $\bar{X} = 150$ kg com $\sigma = 20$ kg.")
        
        st.latex(r"\mu_0 = 155, \quad \sigma = 20, \quad n = 25, \quad \bar{X} = 150, \quad \alpha = 0,05")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Cálculo do Erro Padrão:** O erro padrão da média é $EP(\bar{X}) = \frac{20}{\sqrt{25}} = 4$ kg.")
        st.markdown(r"- **Definição do Limiar:** O valor crítico $Z_{crit}$ para $\alpha = 0,05$ é $-1,645$. O limite de rejeição é $155 + (-1,645 \cdot 4) = 148,42$ kg.")
        st.markdown(r"- **Comparação:** Como a média observada ($150$ kg) é maior que $148,42$ kg, não atingimos a região crítica.")
        
        st.success(r"Conclusão: Não há evidências estatísticas suficientes ao nível de 5% para rejeitar a hipótese nula. A variação é compatível com flutuações aleatórias, sendo desnecessária a paralisação da linha.")
    
    # Tabela resumo de decisão
    st.markdown(r"### 📊 Guia Rápido de Decisão Estatística")
    df_decisao = pd.DataFrame({
        "Resultado": ["p-valor <= alpha", "p-valor > alpha"],
        "Decisão": ["Rejeitar H0", "Não Rejeitar H0"],
        "Interpretação": ["Evidência significativa", "Evidência insuficiente"]
    })
    st.table(df_decisao)

    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Inferência para Médias Populacionais com Grandes Amostras")
    
    # Prosa Teórica com ritmo dinâmico
    st.markdown(r"""
    A inferência estatística constitui o alicerce sobre o qual construímos o conhecimento científico a partir de observações empíricas. O problema central reside em estimar um parâmetro populacional desconhecido, como a média $\mu$, a partir de uma amostra aleatória de tamanho $n$.
    """)
    
    st.info(r"""
    **O Poder do Teorema Central do Limite (TCL):** À medida que o tamanho da amostra $n$ aumenta, a distribuição amostral da média $\bar{X}$ converge para uma distribuição normal, independentemente da forma da distribuição original da população. Essa propriedade permite transitar do caos dos dados brutos para a ordem da inferência probabilística.
    """)
    
    st.markdown(r"""
    Para operar este arcabouço, utilizamos a estatística de teste $Z_{\text{calc}}$, que atua como uma régua universal de "surpresa" estatística:
    """)
    
    # Formalismo Matemático
    st.latex(r"Z_{\text{calc}} = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}} \sim N(0, 1)")
    
    st.markdown(r"""
    - **Estatística de Teste ($Z_{\text{calc}}$):** Quantifica o desvio da média amostral em relação à média hipotetizada, normalizada pelo erro padrão.
    - **Critério de Decisão:** Rejeitamos a hipótese nula $H_0$ quando $|Z_{\text{calc}}| > Z_{\text{crit}}$.
    - **Significância ($\alpha$):** Define a tolerância ao Erro Tipo I, delimitando as regiões de rejeição nas caudas da curva normal.
    """)
    
    # Dedução Analítica
    st.subheader(r"📐 O Coração Matemático: Derivação do Teste Z")
    st.latex(r"E[\bar{X}] = \mu")
    st.latex(r"Var(\bar{X}) = \frac{\sigma^2}{n}")
    st.latex(r"Z = \frac{\bar{X} - \mu_0}{\sqrt{\sigma^2/n}}")
    st.latex(r"Z_{\text{calc}} = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}")
    
    # Simulador Interativo: Distribuição Amostral e Região Crítica
    st.subheader(r"📈 Simulador: Distribuição Amostral e Região Crítica")
    
    col1, col2 = st.columns(2)
    with col1:
        n_val = st.slider(r"Tamanho da Amostra (n)", 10, 500, 100, key=r"n_subtopico_2")
    with col2:
        alpha_val = st.slider(r"Nível de Significância (\alpha)", 0.01, 0.10, 0.05, step=0.01, key=r"alpha_subtopico_2")
    
    # Lógica do Simulador
    z_crit = stats.norm.ppf(1 - alpha_val/2)
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x, 0, 1)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=r"N(0, 1)", line=dict(color="#1E3A8A", width=2)))
    
    # Região Crítica
    mask_right = x >= z_crit
    mask_left = x <= -z_crit
    fig.add_trace(go.Scatter(x=x[mask_right], y=y[mask_right], fill='tozeroy', mode='none', fillcolor="#991B1B", name=r"Região Crítica"))
    fig.add_trace(go.Scatter(x=x[mask_left], y=y[mask_left], fill='tozeroy', mode='none', fillcolor="#991B1B", showlegend=False))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição de Amostragem sob H0</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Z", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    # Laudo Dinâmico
    st.info(f"Com tamanho de amostra n = {n_val} e significância de {alpha_val*100}%, o valor crítico é Z = {z_crit:.3f}. Qualquer valor de Z_calc fora do intervalo [-{z_crit:.3f}, {z_crit:.3f}] implicará na rejeição da hipótese nula.")
    
    # Exemplo Prático
    st.subheader(r"📖 Casos de Aplicação Prática: Controle Logístico")
    with st.container(border=True):
        st.markdown(r"##### 📦 Exemplo: Eficiência de Entregas")
        st.markdown(r"Uma empresa afirma que o tempo médio de entrega é de 45 min ($\sigma=12$). Em 100 entregas, observou-se $\bar{X}=48,5$. Com $\alpha = 0,05$, o tempo médio é maior do que o alegado?")
        st.latex(r"\mu_0 = 45, \sigma = 12, n = 100, \bar{X} = 48,5")
        st.markdown(r"**Desenvolvimento Aritmético:**")
        st.markdown(r"- Erro Padrão: $EP = 12 / \sqrt{100} = 1,2$")
        st.markdown(r"- Estatística Z: $Z_{\text{calc}} = (48,5 - 45) / 1,2 = 2,917$")
        st.success(r"Conclusão: Como $2,917 > 1,645$, rejeitamos $H_0$. O tempo médio de entrega é estatisticamente superior a 45 minutos.")

    # Importações necessárias (assumidas disponíveis no contexto principal)
    import streamlit as st
    import numpy as np
    import pandas as pd
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"Procedimentos Inferenciais para Proporções Amostrais")
    
    # Introdução
    st.markdown(r"""
    A inferência estatística sobre proporções constitui um dos pilares mais robustos da estatística aplicada, sendo a ferramenta de escolha para o tratamento de variáveis aleatórias categóricas. Quando classificamos uma observação como "sucesso" ou "fracasso", operamos sob o arcabouço de uma **distribuição de Bernoulli**.
    """)
    
    st.info(r"A proporção amostral, denotada por $\hat{p}$, é o estimador central que utilizamos para inferir sobre o parâmetro populacional desconhecido $p$. Ela representa a razão entre sucessos observados e o tamanho total da amostra.")
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Estimativa e Normalidade Assintótica")
    st.latex(r"\hat{p} = \frac{X}{n}")
    
    st.markdown(r"""
    O salto qualitativo na análise de proporções ocorre via **Teorema Central do Limite**. Ele nos permite aproximar a distribuição binomial (discreta) por uma distribuição normal (contínua), garantindo validade inferencial para grandes amostras.
    """)
    
    st.warning(r"Condição de validade: Para que a aproximação normal seja fidedigna, devemos garantir que a distribuição não seja excessivamente assimétrica. As condições de contorno são: $n p_0 \geq 5$ e $n(1-p_0) \geq 5$.")
    
    # Deduções Analíticas
    st.subheader(r"🔍 Estrutura Lógica da Inferência")
    st.latex(r"X \sim Bin(n, p_0)")
    st.latex(r"E[\hat{p}] = p_0")
    st.latex(r"Var(\hat{p}) = \frac{p_0(1-p_0)}{n}")
    st.latex(r"Z_{\text{calc}} = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}")
    
    # Aplicação Prática
    st.subheader(r"📈 Casos de Aplicação Prática: Teste de Satisfação")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Verificação de Qualidade de Serviço")
        st.markdown(r"Um provedor de serviços de internet alega uma taxa de satisfação de 85% ($p_0 = 0,85$). Um órgão consumidor suspeita que a taxa real é inferior. Eles testam 200 clientes e encontram 160 satisfeitos. Com $\alpha = 0,05$, avalie a propaganda.")
        
        # Dados sumarizados
        st.latex(r"p_0 = 0,85, \quad n = 200, \quad X = 160, \quad \hat{p} = 0,80")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Passo 1:** Cálculo do erro padrão: $EP(\hat{p}) = \sqrt{\frac{0,85 \cdot 0,15}{200}} = 0,0252$")
        st.markdown(r"- **Passo 2:** Cálculo da estatística Z: $Z_{\text{calc}} = \frac{0,80 - 0,85}{0,0252} = -1,984$")
        st.markdown(r"- **Passo 3:** Comparação com valor crítico: $Z_{\text{crit}} = -1,645$ para $\alpha = 0,05$")
        
        st.success(r"Conclusão: Como $Z_{\text{calc}} = -1,984 < -1,645$, rejeitamos a hipótese nula. Há evidência estatística significativa para afirmar que a taxa de satisfação é inferior aos 85% alegados.")
    
    # Considerações Finais
    st.markdown(r"""
    ---
    ### 💡 Síntese Didática
    A escolha entre testes bicaudais ou unicaudais define a direção da nossa investigação. A utilização da estatística $Z$ padronizada transforma observações dicotômicas simples em decisões baseadas em probabilidade e risco, permitindo que a ciência moderna avalie conformidade e desempenho com rigor matemático.
    """)

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # Cabeçalho do Subtópico
    st.header(r"A Engenharia do P-valor e Tomada de Decisão Estatística")
    
    # Introdução Teórica
    st.markdown(r"""
    O p-valor oferece uma medida contínua da força da evidência contra a hipótese nula. Em vez de uma decisão binária baseada em um limite rígido de $\alpha$, o pesquisador pode reportar o nível descritivo observado, que representa a probabilidade de se obter uma estatística tão ou mais extrema que a observada, sob a suposição de que $H_0$ seja verdadeira.
    """)
    
    st.info(r"Essa abordagem é superior em contextos científicos, permitindo que outros pesquisadores interpretem a força da evidência diretamente, sem a restrição imposta por níveis de significância pré-definidos.")
    
    # O Coração Matemático: Engenharia do P-valor
    st.markdown(r"### 📐 O Coração Matemático: Engenharia do P-valor")
    
    st.markdown(r"A dedução do p-valor baseia-se na cauda da distribuição de probabilidade da estatística de teste sob $H_0$.")
    
    st.latex(r"p\text{-valor} = P(T > T_{\text{calc}} | H_0 \text{ é verdadeira}) \text{ (unilateral superior)}")
    
    st.markdown(r"Para casos bilaterais, a probabilidade é distribuída em ambas as extremidades da distribuição:")
    
    st.latex(r"p\text{-valor} = P(T < -|T_{\text{calc}}|) + P(T > |T_{\text{calc}}|)")
    
    st.markdown(r"Considerando a simetria de distribuições como a Normal ou t de Student, simplificamos para:")
    
    st.latex(r"p\text{-valor} = 2 \cdot P(T > |T_{\text{calc}}|)")
    
    # Casos de Aplicação Prática: Engenharia do P-valor
    st.markdown(r"### 📈 Casos de Aplicação Prática: Engenharia do P-valor")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Teste de Confiabilidade de Baterias")
        st.markdown(r"Um fabricante afirma que baterias duram 500 horas, com $\sigma = 25$ horas. Uma amostra de 100 baterias revelou uma média de 505 horas. Calcule o p-valor e tome a decisão a $\alpha = 0,05$.")
        
        st.latex(r"\mu_0 = 500, \sigma = 25, n = 100, \bar{X} = 505")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- **Cálculo do Erro Padrão:** $EP(\bar{X}) = 25 / \sqrt{100} = 2,5$")
        st.markdown(r"- **Estatística Z calculada:** $Z_{\text{calc}} = (505 - 500) / 2,5 = 2,0$")
        st.markdown(r"- **Cálculo do p-valor:** $p\text{-valor} = 2 \times P(Z > 2,0) = 2 \times (1 - 0,9772) = 0,0456$")
        
        st.success(r"O p-valor de 0,0456 é menor que o nível $\alpha = 0,05$. Rejeitamos a hipótese nula, concluindo que há evidências estatísticas de que a vida útil das baterias é significativamente diferente de 500 horas.")
    
    # Nota de fechamento para o contexto executivo
    st.divider()
    st.caption(r"Nota: O p-valor não deve ser confundido com a probabilidade de a hipótese nula estar correta, mas sim com a consistência dos dados observados sob a premissa de $H_0$.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    # Cabeçalho do Subtópico
    st.header(r"Análise da Potência do Teste e Erros Inferenciais")
    
    # Introdução Teórica
    st.markdown(r"""
    A análise da potência do teste é um pilar fundamental na inferência estatística, permitindo a validação da robustez de experimentos. Ela atua como um mecanismo de controle para evitar conclusões precipitadas sobre a inexistência de efeitos, garantindo que o pesquisador tenha a sensibilidade necessária para detectar mudanças reais nos dados.
    """)
    
    st.markdown(r"""
    Para garantir a integridade de uma decisão estatística, observamos três componentes críticos:
    - **Nível de Significância ($\alpha$):** Controla a probabilidade de cometer um Erro do Tipo I (falso positivo).
    - **Poder do Teste ($1 - \beta$):** Mede a probabilidade de rejeitar corretamente a hipótese nula quando ela é falsa.
    - **Erro do Tipo II ($\beta$):** Representa a probabilidade de falhar ao detectar um efeito que realmente existe.
    """)
    
    st.info(r"Um experimento com baixo poder estatístico é vulnerável a 'falsos negativos', frequentemente causados por tamanhos amostrais reduzidos ou excessiva variabilidade interna nos dados.")
    
    # O Coração Matemático
    st.markdown(r"### 📐 O Coração Matemático: Definição da Potência")
    
    st.markdown(r"A função de potência $\pi(\theta)$ é definida como a probabilidade de rejeitar a hipótese nula dado um parâmetro verdadeiro:")
    st.latex(r"\pi(\theta) = P(\text{Rejeitar } H_0 | H_1 \text{ é verdadeira}) = 1 - \beta(\theta)")
    
    st.markdown(r"A dedução analítica baseia-se na fronteira da região crítica ($RC$):")
    st.latex(r"RC = \{ \bar{X} | \bar{X} < c_1 \cup \bar{X} > c_2 \}")
    
    st.markdown(r"Desta forma, o erro do tipo II ($\beta$) e a potência ($\pi$) são calculados como:")
    st.latex(r"\beta(\mu) = P(c_1 < \bar{X} < c_2 | \mu)")
    st.latex(r"\pi(\mu) = 1 - P(c_1 < \bar{X} < c_2 | \mu)")
    
    # Simulador de Poder e Erro Beta
    st.markdown(r"### 📊 Simulador Interativo: Poder e Erro Beta")
    col1, col2 = st.columns(2)
    with col1:
        mu1_input = st.slider(r"Média sob H1 ($\mu_1$)", 500.0, 520.0, 505.0, step=0.5, key="mu1_sim_subtopico_5")
    with col2:
        n_input = st.slider(r"Tamanho da Amostra ($n$)", 30, 200, 100, step=10, key="n_sim_subtopico_5")
    
    # Cálculos do Simulador
    mu0 = 500
    sigma = 10
    se = sigma / np.sqrt(n_input)
    z_crit = 2.576
    c1 = mu0 - z_crit * se
    c2 = mu0 + z_crit * se
    
    x = np.linspace(480, 530, 500)
    y0 = norm.pdf(x, mu0, se)
    y1 = norm.pdf(x, mu1_input, se)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y0, name=r"H0 (Média=500)", line=dict(color="#1E3A8A", width=2)))
    fig.add_trace(go.Scatter(x=x, y=y1, name=r"H1 (Média=mu1)", line=dict(color="#991B1B", width=2)))
    
    # Preenchimento de Poder e Beta
    fill_beta = x[(x >= c1) & (x <= c2)]
    fig.add_trace(go.Scatter(x=fill_beta, y=norm.pdf(fill_beta, mu1_input, se), fill='tozeroy', name=r"Erro Beta", fillcolor="rgba(245, 158, 11, 0.3)", line=dict(width=0)))
    fig.add_trace(go.Scatter(x=x[x > c2], y=y1[x > c2], fill='tozeroy', name=r"Poder (1-Beta)", fillcolor="rgba(16, 185, 129, 0.3)", line=dict(width=0)))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Análise de Poder e Distribuições</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valores de \u03BC", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_5")
    
    beta_val = norm.cdf(c2, mu1_input, se) - norm.cdf(c1, mu1_input, se)
    st.info(f"Com uma média de {mu1_input} e amostra n={n_input}, o erro Beta estimado é de {beta_val:.4f}, resultando em um poder de teste de {(1-beta_val)*100:.2f}%.")
    
    # Casos de Aplicação
    st.markdown(r"### 📈 Casos de Aplicação Prática")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Máquina de Envase")
        st.markdown(r"Avaliação da precisão de envase com $H_0: \mu = 500$ contra $H_1: \mu \neq 500$, considerando $\alpha = 0,01$ e $n = 100$. Calculando o poder para detectar um desvio para $\mu = 505$.")
        st.latex(r"\alpha = 0.01, Z_{crit} = 2.576, EP(\bar{X}) = 2.0")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Região Crítica calculada: $RC = \{ \bar{X} < 494.84 \cup \bar{X} > 505.16 \}$")
        st.markdown(r"- Valor Z para $\mu = 505$: $Z_2 = (505.16 - 505) / 2 = 0.08$")
        st.markdown(r"- Probabilidade de detectar o efeito: $P(Z > 0.08) \approx 0.4681$")
        st.success(r"O poder de 46,8% indica uma sensibilidade moderada. O teste falha em detectar o desvio para 505g em mais da metade das vezes, sendo recomendável aumentar o tamanho amostral.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNjogVGVzdGVzIGRlIGhpcMOzdGVzZXMgcGFyYSBhIG3DqWRpYSBlIHBhcmEgYSBwcm9wb3LDp8OjbyB1c2FuZG8gZ3JhbmRlcyBhbW9zdHJhcyIsICJxdWVzdG9lc19tdWx0aXBsYV9lc2NvbGhhIjogW3siZW51bmNpYWRvIjogIlVtYSBpbmTDunN0cmlhIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyBvcGVyYSBjb20gdW1hIG3DoXF1aW5hIGRlIGFsdGEgcHJlY2lzw6NvIGNhbGlicmFkYSBwYXJhIHByb2R1emlyIHJlc2lzdG9yZXMgY29tIHJlc2lzdMOqbmNpYSBtw6lkaWEgZGUgJFxcbXUgPSAxMDBcXE9tZWdhJCBlIGRlc3ZpbyBwYWRyw6NvICRcXHNpZ21hID0gMlxcT21lZ2EkLiBQZXJpb2RpY2FtZW50ZSwgdW0gaW5zcGV0b3IgZGUgcXVhbGlkYWRlIGNvbGV0YSB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIGRlICRuID0gMTYkIHVuaWRhZGVzIHBhcmEgdmVyaWZpY2FyIGEgY2FsaWJyYcOnw6NvLiBBIGhpcMOzdGVzZSBudWxhIMOpICRIXzA6IFxcbXUgPSAxMDAkIGNvbnRyYSBhIGFsdGVybmF0aXZhICRIXzE6IFxcbXUgXFxuZXEgMTAwJC4gTyBpbnNwZXRvciBkZWZpbmUgYSBSZWdpw6NvIENyw610aWNhIChSQykgY29tbyBvcyB2YWxvcmVzIGVtIHF1ZSBhIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0kIGV4Y2VkZSAkMTAxXFxPbWVnYSQgb3Ugw6kgaW5mZXJpb3IgYSAkOTlcXE9tZWdhJC4gUXVhbCDDqSBhIHByb2JhYmlsaWRhZGUgZGUgY29tZXRlciB1bSBlcnJvIGRvIHRpcG8gSSBuZXN0ZSB0ZXN0ZSBkZSBoaXDDs3Rlc2U/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBcHJveGltYWRhbWVudGUgMCwwMjI4IiwgIkIiOiAiQXByb3hpbWFkYW1lbnRlIDAsMDQ1NiIsICJDIjogIkFwcm94aW1hZGFtZW50ZSAwLDA1MDAiLCAiRCI6ICJBcHJveGltYWRhbWVudGUgMCwxMDAwIiwgIkUiOiAiQXByb3hpbWFkYW1lbnRlIDAsOTU0NCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSwgc29iICRIXzAkLCBhIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0kIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgY29tIG3DqWRpYSAkXFxtdV8wID0gMTAwJCBlIGVycm8gcGFkcsOjbyAkRVAoXFxiYXJ7WH0pID0gXFxzaWdtYSAvIFxcc3FydHtufSQuIENhbGN1bGUgbyB2YWxvciAkWiQgcGFyYSBvcyBsaW1pdGVzICQ5OSQgZSAkMTAxJC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlByaW1laXJvLCBjYWxjdWxhbW9zIG8gZXJybyBwYWRyw6NvOiAkRVAoXFxiYXJ7WH0pID0gMiAvIFxcc3FydHsxNn0gPSAyLzQgPSAwLDUkLiBTb2IgJEhfMCQsICRcXGJhcntYfSBcXHNpbSBOKDEwMCwgMCw1XjIpJC4gTyBlcnJvIGRvIHRpcG8gSSDDqSBhIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgJEhfMCQgZGFkbyBxdWUgZWxhIMOpIHZlcmRhZGVpcmE6ICRcXGFscGhhID0gUChcXGJhcntYfSA8IDk5IFxcdGV4dHsgb3UgfSBcXGJhcntYfSA+IDEwMSB8IFxcbXUgPSAxMDApJC4gQ29udmVydGVuZG8gcGFyYSAkWiA9IChcXGJhcntYfSAtIDEwMCkgLyAwLDUkLCB0ZW1vcyAkUChaIDwgKDk5LTEwMCkvMCw1KSArIFAoWiA+ICgxMDEtMTAwKS8wLDUpID0gUChaIDwgLTIpICsgUChaID4gMikgPSAwLDAyMjggKyAwLDAyMjggPSAwLDA0NTYkLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoOTgsIDEwMiwgMjAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgsIDEwMCwgMC41KVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBsaW5lPWRpY3QoY29sb3I9XCIjMUUzQThBXCIsIHdpZHRoPTMpLCBuYW1lPVwiRGVuc2lkYWRlIHNvYiBIMFwiKSlcbmZpZy5hZGRfdnJlY3QoeDA9OTgsIHgxPTk5LCBmaWxsY29sb3I9XCIjOTkxQjFCXCIsIG9wYWNpdHk9MC4zLCBsaW5lX3dpZHRoPTAsIG5hbWU9XCJSQ1wiKVxuZmlnLmFkZF92cmVjdCh4MD0xMDEsIHgxPTEwMiwgZmlsbGNvbG9yPVwiIzk5MUIxQlwiLCBvcGFjaXR5PTAuMywgbGluZV93aWR0aD0wLCBuYW1lPVwiUkNcIilcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPVwiPGI+RGlzdHJpYnVpw6fDo28gZGEgTcOpZGlhIEFtb3N0cmFsIHNvYiBIMDwvYj5cIiwgeGF4aXM9ZGljdCh0aXRsZT1yXCJNw6lkaWEgQW1vc3RyYWwgKCRcXFxcYmFye1h9JClcIiksIHlheGlzPWRpY3QodGl0bGU9XCJEZW5zaWRhZGVcIikpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGNsw61uaWNvIHBhcmEgYXZhbGlhciBhIGVmaWPDoWNpYSBkZSB1bSBub3ZvIGbDoXJtYWNvLCBhIGhpcMOzdGVzZSBudWxhIMOpIHF1ZSBvIGbDoXJtYWNvIG7Do28gw6kgc3VwZXJpb3IgYSB1bSBwbGFjZWJvICgkSF8wJCkuIE8gcGVzcXVpc2Fkb3IgZGVmaW5lIGEgUmVnacOjbyBDcsOtdGljYSAoUkMpIGRlIGZvcm1hIHF1ZSBhIHByb2JhYmlsaWRhZGUgZGUgdW0gZXJybyBkbyB0aXBvIEkgKCRcXGFscGhhJCkgc2VqYSBkZSA1JS4gU2UgbyBleHBlcmltZW50byByZXN1bHRhciBlbSB1bSBwLXZhbG9yIGRlIDAsMDMsIHF1YWwgZGV2ZSBzZXIgYSBkZWNpc8OjbyBlc3RhdMOtc3RpY2EgZG8gcGVzcXVpc2Fkb3IgZW0gcmVsYcOnw6NvIMOgICRIXzAkPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiUmVqZWl0YXIgJEhfMCQsIHBvaXMgbyBwLXZhbG9yIMOpIG1lbm9yIHF1ZSAkXFxhbHBoYSQuIiwgIkIiOiAiTsOjbyByZWplaXRhciAkSF8wJCwgcG9pcyBvIHAtdmFsb3Igw6kgbWVub3IgcXVlICRcXGFscGhhJC4iLCAiQyI6ICJSZWplaXRhciAkSF8wJCwgcG9pcyBvIHAtdmFsb3Igw6kgbWFpb3IgcXVlICRcXGFscGhhJC4iLCAiRCI6ICJOw6NvIHJlamVpdGFyICRIXzAkLCBwb2lzIGEgZXZpZMOqbmNpYSDDqSBpbnN1ZmljaWVudGUuIiwgIkUiOiAiTyB0ZXN0ZSDDqSBpbmNvbmNsdXNpdm8sIHBvaXMgbyBwLXZhbG9yIMOpIGV4YXRhbWVudGUgaWd1YWwgYSAwLDAzLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTyBwLXZhbG9yIHJlcHJlc2VudGEgYSBtZW5vciBwcm9iYWJpbGlkYWRlIGRlIHNpZ25pZmljw6JuY2lhIHBhcmEgYSBxdWFsIGEgaGlww7N0ZXNlIG51bGEgc2VyaWEgcmVqZWl0YWRhLiBDb21wYXJlIGVzdGUgdmFsb3IgY29tIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGZpeGFkbyBwZWxvIHBlc3F1aXNhZG9yLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBwLXZhbG9yIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSBvYnNlcnZhciB1bSByZXN1bHRhZG8gdMOjbyBvdSBtYWlzIGV4dHJlbW8gcXVlIG8gb2J0aWRvLCBhc3N1bWluZG8gcXVlICRIXzAkIMOpIHZlcmRhZGVpcmEuIFNlICRwXFx0ZXh0ey12YWxvcn0gPCBcXGFscGhhJCwgYSBwcm9iYWJpbGlkYWRlIGRlIG9ic2VydmFyIHRhbCBhbW9zdHJhIHNvYiAkSF8wJCDDqSBtZW5vciBxdWUgbyBub3NzbyBsaW1pYXIgZGUgdG9sZXLDom5jaWEsIGxvZ28sIHJlamVpdGFtb3MgJEhfMCQuIENvbW8gJDAsMDMgPCAwLDA1JCwgdGVtb3MgZXZpZMOqbmNpYXMgZXN0YXTDrXN0aWNhcyBzaWduaWZpY2F0aXZhcyBwYXJhIHJlamVpdGFyIGEgaGlww7N0ZXNlIG51bGEuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbWEgaW5kw7pzdHJpYSBkZSBjb21wb25lbnRlcyBlbGV0csO0bmljb3MgdXRpbGl6YSB1bSBwcm9jZXNzbyBhdXRvbWF0aXphZG8gZGUgY29ydGUgY3VqYSBtw6lkaWEgZGUgcHJlY2lzw6NvIGVzcGVyYWRhIMOpICRcXG11XzAgPSA1MCwwXFx0ZXh0eyBtbX0kLiBBIGdlcsOqbmNpYSBjb2xldGEgdW1hIGFtb3N0cmEgYWxlYXTDs3JpYSBkZSAkbiA9IDEwMCQgcGXDp2FzLCBvYnNlcnZhbmRvIHVtYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9ID0gNTEsMlxcdGV4dHsgbW19JC4gU2FiZS1zZSBwb3IgcmVnaXN0cm9zIGhpc3TDs3JpY29zIHF1ZSBvIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCDDqSAkXFxzaWdtYSA9IDQsMFxcdGV4dHsgbW19JC4gQW8gcmVhbGl6YXIgdW0gdGVzdGUgZGUgaGlww7N0ZXNlIGJpbGF0ZXJhbCBwYXJhIHZlcmlmaWNhciBzZSBhIG3DqWRpYSBkZSBjb3J0ZSBtdWRvdSwgcXVhbCDDqSBvIHZhbG9yIGRhIGVzdGF0w61zdGljYSAkWl97XHRleHR7Y2FsY319JD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIlpfe1xcdGV4dHtjYWxjfX0gPSAwLDMiLCAiQiI6ICJaX3tcXHRleHR7Y2FsY319ID0gMiwwIiwgIkMiOiAiWl97XFx0ZXh0e2NhbGN9fSA9IDMsMCIsICJEIjogIlpfe1xcdGV4dHtjYWxjfX0gPSA0LDUiLCAiRSI6ICJaX3tcXHRleHR7Y2FsY319ID0gMSwyIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSDDqSAkRVAoXFxiYXJ7WH0pID0gXFxzaWdtYSAvIFxcc3FydHtufSQuIEEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlIMOpIGRhZGEgcG9yICRaX3tcXHRleHR7Y2FsY319ID0gKFxcYmFye1h9IC0gXFxtdV8wKSAvIEVQKFxcYmFye1h9KSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJQYXJhIGNhbGN1bGFyICRaX3tcXHRleHR7Y2FsY319JCwgcHJpbWVpcm8gZGV0ZXJtaW5hbW9zIG8gZXJybyBwYWRyw6NvOiAkRVAoXFxiYXJ7WH0pID0gNCwwIC8gXFxzcXJ0ezEwMH0gPSA0LDAgLyAxMCA9IDAsNCQuIEVtIHNlZ3VpZGEsIGFwbGljYW1vcyBhIGbDs3JtdWxhOiAkWl97XFx0ZXh0e2NhbGN9fSA9ICg1MSwyIC0gNTAsMCkgLyAwLDQgPSAxLDIgLyAwLDQgPSAzLDAkLiBPIHZhbG9yIDMsMCBpbmRpY2EgcXVlIGEgbcOpZGlhIGFtb3N0cmFsIG9ic2VydmFkYSBlc3TDoSAzIGRlc3Zpb3MgcGFkcsOjbyBhY2ltYSBkbyB2YWxvciBwb3N0dWxhZG8gcGVsYSBoaXDDs3Rlc2UgbnVsYSwgbyBxdWUgc3VnZXJlIHVtYSBmb3J0ZSBldmlkw6puY2lhIGNvbnRyYSAkSF8wJC4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAyMDApXG55ID0gKDEgLyBucC5cXHNxcnQoMiAqIG5wLlxccGkpKSAqIG5wLlxcZXhwKC0wLjUgKiB4KioyKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBuYW1lPVwiTigwLDEpXCIsIGxpbmU9ZGljdChjb2xvcj1cIiMxRTNBOEFcIiwgd2lkdGg9MykpKVxuZmlnLmFkZF92bGluZSh4PTMuMCwgbGluZT1kaWN0KGNvbG9yPVwiIzk5MUIxQlwiLCBkYXNoPVwiZGFzaFwiKSwgbmFtZT1cIlpfe2NhbGN9PTMuMFwiKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9XCJEaXN0cmlidWnDp8OjbyBOb3JtYWwgZSBvIFZhbG9yIE9ic2VydmFkb1wiLCB4YXhpc190aXRsZT1cIlpcIiwgeWF4aXNfdGl0bGU9XCJEZW5zaWRhZGVcIikiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgcXVlLCBhbyByZWFsaXphciB1bSB0ZXN0ZSBkZSBoaXDDs3Rlc2VzIHNvYnJlIGEgbcOpZGlhIHBvcHVsYWNpb25hbCAkXFxtdSQgY29tIHVtYSBhbW9zdHJhIGdyYW5kZSAoJG49NDAwJCksIHZvY8OqIGVuY29udHJvdSB1bSAkcFxcdGV4dHstdmFsb3J9ID0gMCwwMjUkLiBDb25zaWRlcmFuZG8gdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGRlICRcXGFscGhhID0gMCwwNSQsIHF1YWwgw6kgYSBkZWNpc8OjbyBlc3RhdGlzdGljYW1lbnRlIGNvcnJldGEgZSBzdWEgaW50ZXJwcmV0YcOnw6NvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiUmVqZWl0YS1zZSAkSF8wJCwgcG9pcyBvICRwXFx0ZXh0ey12YWxvcn0gPCBcXGFscGhhJCwgaW5kaWNhbmRvIGV2aWTDqm5jaWEgc2lnbmlmaWNhdGl2YSBkZSBxdWUgYSBtw6lkaWEgcG9wdWxhY2lvbmFsIMOpIGRpZmVyZW50ZSBkZSAkXFxtdV8wJC4iLCAiQiI6ICJBY2VpdGEtc2UgJEhfMCQsIHBvaXMgbyAkcFxcdGV4dHstdmFsb3J9JCDDqSBtdWl0byBiYWl4bywgaW5kaWNhbmRvIHF1ZSBhIG3DqWRpYSBhbW9zdHJhbCDDqSBtdWl0byBwcmVjaXNhLiIsICJDIjogIk7Do28gc2UgcmVqZWl0YSAkSF8wJCwgcG9pcyBvICRwXFx0ZXh0ey12YWxvcn0gPiBcXGFscGhhJCwgc3VnZXJpbmRvIHF1ZSBvcyBkYWRvcyBuw6NvIHRyYXplbSBldmlkw6puY2lhIHN1ZmljaWVudGUgcGFyYSByZWplaXRhciBhIGlndWFsZGFkZS4iLCAiRCI6ICJPIHRlc3RlIMOpIGluY29uY2x1c2l2bywgcG9pcyBhbW9zdHJhcyBncmFuZGVzIHRlbmRlbSBhIHJlamVpdGFyICRIXzAkIHNlbXByZSBxdWUgJFxcYmFye1h9IFxcbmVxIFxcbXVfMCQuIiwgIkUiOiAiUmVqZWl0YS1zZSAkSF8wJCwgbWFzIGNvbSBiYWl4YSBjb25maWFuw6dhLCB2aXN0byBxdWUgJHBcXHRleHR7LXZhbG9yfSQgZGV2ZXJpYSBzZXIgbWVub3IgcXVlICQwLDAxJCBwYXJhIGRlY2lzw7VlcyByb2J1c3Rhcy4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIk8gJHBcXHRleHR7LXZhbG9yfSQgcmVwcmVzZW50YSBhIHByb2JhYmlsaWRhZGUgZGUgb2J0ZXIgdW0gcmVzdWx0YWRvIHTDo28gb3UgbWFpcyBleHRyZW1vIHF1ZSBvIG9ic2VydmFkbywgYXNzdW1pbmRvIHF1ZSAkSF8wJCDDqSB2ZXJkYWRlaXJhLiBDb21wYXJlIGNvbSAkXFxhbHBoYSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIHJlZ3JhIGRlIGRlY2lzw6NvIHBhcmEgdGVzdGVzIGRlIGhpcMOzdGVzZXMgZXN0YWJlbGVjZSBxdWUgcmVqZWl0YW1vcyAkSF8wJCBzZSAkcFxcdGV4dHstdmFsb3J9IFxcbGUgXFxhbHBoYSQuIE5lc3RlIGNhc28sICQwLDAyNSBcXGxlIDAsMDUkLCBwb3J0YW50bywgYSBldmlkw6puY2lhIGNvbnRyYSBhIGhpcMOzdGVzZSBudWxhIMOpIGVzdGF0aXN0aWNhbWVudGUgc2lnbmlmaWNhdGl2YSBhbyBuw612ZWwgZGUgNSUuIElzc28gc2lnbmlmaWNhIHF1ZSBhIGRpZmVyZW7Dp2Egb2JzZXJ2YWRhIGVudHJlIGEgbcOpZGlhIGFtb3N0cmFsIGUgYSBtw6lkaWEgcG9wdWxhY2lvbmFsIGhpcG90ZXRpemFkYSBuw6NvIMOpIG1lcmFtZW50ZSBkZWNvcnJlbnRlIGRvIGFjYXNvIGFtb3N0cmFsLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIG9wZXJhIHNvYiB1bSBwYWRyw6NvIGRlIHF1YWxpZGFkZSBvbmRlIGEgcHJvcG9yw6fDo28gZGUgZmFsaGFzIGFkbWl0aWRhIMOpIGRlICRwID0gMC4wMyQuIFBhcmEgdmVyaWZpY2FyIHNlIG8gcHJvY2Vzc28gZXN0w6Egc29iIGNvbnRyb2xlLCB1bWEgYW1vc3RyYSBhbGVhdMOzcmlhIGRlICRuID0gNTAwJCB1bmlkYWRlcyBmb2kgaW5zcGVjaW9uYWRhLCByZXN1bHRhbmRvIGVtICRYID0gMjAkIHVuaWRhZGVzIGRlZmVpdHVvc2FzLiBDb25zaWRlcmFuZG8gbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLjA1JCwgcXVhbCDDqSBvIHByb2NlZGltZW50byBlc3RhdMOtc3RpY28gY29ycmV0byBwYXJhIHRlc3RhciBhIGhpcMOzdGVzZSBkZSBxdWUgYSBwcm9wb3LDp8OjbyBkZSBmYWxoYXMgZXhjZWRldSBvIGxpbWl0ZSBlc3RhYmVsZWNpZG8gcGVsbyBwYWRyw6NvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiVGVzdGFyICRIXzA6IHAgPSAwLjAzJCBjb250cmEgJEhfMTogcCA8IDAuMDMkIHV0aWxpemFuZG8gYSBlc3RhdMOtc3RpY2EgJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7XFxoYXR7cH0gLSAwLjAzfXtcXHNxcnR7XFxmcmFjezAuMDMoMC45Nyl9ezUwMH19fSQuIiwgIkIiOiAiVGVzdGFyICRIXzA6IHAgPSAwLjAzJCBjb250cmEgJEhfMTogcCBcXG5lcSAwLjAzJCB1dGlsaXphbmRvIGEgZXN0YXTDrXN0aWNhICRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFje1xcaGF0e3B9IC0gMC4wM317XFxzcXJ0e1xcZnJhY3swLjAzKDAuOTcpfXs1MDB9fX0kLiIsICJDIjogIlRlc3RhciAkSF8wOiBwID0gMC4wMyQgY29udHJhICRIXzE6IHAgPiAwLjAzJCB1dGlsaXphbmRvIGEgZXN0YXTDrXN0aWNhICRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFje1xcaGF0e3B9IC0gMC4wM317XFxzcXJ0e1xcZnJhY3swLjAzKDAuOTcpfXs1MDB9fX0kLiIsICJEIjogIlRlc3RhciAkSF8wOiBwID0gMC4wMyQgY29udHJhICRIXzE6IHAgPiAwLjAzJCB1dGlsaXphbmRvIGEgZXN0YXTDrXN0aWNhICRaX3tcXHRleHR7Y2FsY319ID0gXFxmcmFje1xcaGF0e3B9IC0gMC4wM317XFxzcXJ0e1xcZnJhY3tcXGhhdHtwfSgxLVxcaGF0e3B9KX17NTAwfX19JC4iLCAiRSI6ICJPIHRlc3RlIMOpIGludsOhbGlkbywgcG9pcyBhIGFtb3N0cmEgZGUgJG4gPSA1MDAkIMOpIG11aXRvIHBlcXVlbmEgcGFyYSBhc3N1bWlyIGEgbm9ybWFsaWRhZGUgZGEgZGlzdHJpYnVpw6fDo28gZGEgcHJvcG9yw6fDo28gYW1vc3RyYWwuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJBbmFsaXNlIGEgbmF0dXJlemEgZGEgc3VzcGVpdGE6IG8gaW50ZXJlc3NlIMOpIHZlcmlmaWNhciBzZSBhIHRheGEgJ2V4Y2VkZXUnIG8gbGltaXRlLiBJc3NvIGRlZmluZSBvIHNpbmFsIGRhIGRlc2lndWFsZGFkZSBlbSAkSF8xJC4gQWzDqW0gZGlzc28sIG5vdGUgcXVlLCBzb2IgJEhfMCQsIHV0aWxpemFtb3MgbyBwYXLDom1ldHJvIHBvcHVsYWNpb25hbCBjb25oZWNpZG8gJHBfMCQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGhpcMOzdGVzZSAkSF8xOiBwID4gMC4wMyQgcmVwcmVzZW50YSBvIGludGVyZXNzZSBlbSB2ZXJpZmljYXIgc2UgYSBwcm9wb3LDp8OjbyBkZSBmYWxoYXMgc3VwZXJvdSBvIGxpbWl0ZS4gQSBlc3RhdMOtc3RpY2EgZGUgdGVzdGUgcGFkcm9uaXphZGEgcGFyYSBwcm9wb3LDp8O1ZXMgc29iIGEgaGlww7N0ZXNlIG51bGEgJEhfMDogcCA9IHBfMCQgw6kgJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7XFxoYXR7cH0gLSBwXzB9e1xcc3FydHtcXGZyYWN7cF8wKDEtcF8wKX17bn19fSQuIFN1YnN0aXR1aW5kbyAkcF8wID0gMC4wMyQsICRuID0gNTAwJCBlICRcXGhhdHtwfSA9IDIwLzUwMCA9IDAuMDQkLCB0ZW1vcyBhIGbDs3JtdWxhIGNvcnJldGEgZXhwcmVzc2EgbmEgYWx0ZXJuYXRpdmEgQy4gQSBhbHRlcm5hdGl2YSBEIGVzdMOhIGluY29ycmV0YSBwb2lzIHV0aWxpemEgbyBlc3RpbWFkb3IgJFxcaGF0e3B9JCBubyBkZW5vbWluYWRvciwgbyBxdWUgw6kgY29tdW0gYXBlbmFzIG5hIGNvbnN0cnXDp8OjbyBkZSBpbnRlcnZhbG9zIGRlIGNvbmZpYW7Dp2EsIG7Do28gbm8gdGVzdGUgZGUgaGlww7N0ZXNlcyBzb2IgJEhfMCQuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbnggPSBucC5saW5zcGFjZSgtMywgMywgMTAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9XCJOKDAsIDEpXCIsIGxpbmU9ZGljdChjb2xvcj1cIiMxRTNBOEFcIiwgd2lkdGg9MykpKVxuZmlnLmFkZF92cmVjdCh4MD0xLjY0NSwgeDE9MywgZmlsbGNvbG9yPVwiIzk5MUIxQlwiLCBvcGFjaXR5PTAuMywgbGluZV93aWR0aD0wLCBuYW1lPVwiUkNcIilcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPVwiRGlzdHJpYnVpw6fDo28gTm9ybWFsIGUgUmVnacOjbyBDcsOtdGljYSAoJFxcXFxhbHBoYT0wLjA1JClcIiwgeGF4aXNfdGl0bGU9clwiWlwiLCB5YXhpc190aXRsZT1yXCJEZW5zaWRhZGVcIikiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJBbyByZWFsaXphciBpbmZlcsOqbmNpYXMgcGFyYSBwcm9wb3LDp8O1ZXMgYW1vc3RyYWlzIGNvbSBiYXNlIG5hIGFwcm94aW1hw6fDo28gZGEgZGlzdHJpYnVpw6fDo28gbm9ybWFsLCB1bWEgZGFzIGNvbmRpw6fDtWVzIGNydWNpYWlzIHBhcmEgYSB2YWxpZGFkZSBkbyBwcm9jZWRpbWVudG8gw6kgbyB0YW1hbmhvIGFtb3N0cmFsLiBTdXBvbmhhIHF1ZSBlc3RlamFtb3MgZXN0dWRhbmRvIGEgcHJlZmVyw6puY2lhIGRlIGNvbnN1bWlkb3JlcyBwb3IgdW0gbm92byBwcm9kdXRvLiBRdWFsIGRhcyBzZWd1aW50ZXMgYWZpcm1hw6fDtWVzIG1lbGhvciBkZXNjcmV2ZSBvIHJlcXVpc2l0byBwYXJhIGEgYXByb3hpbWHDp8OjbyBub3JtYWwgZGEgcHJvcG9yw6fDo28gYW1vc3RyYWwgJFxcaGF0e3B9JD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgYW1vc3RyYSBkZXZlIHNlciBvYnJpZ2F0b3JpYW1lbnRlIG1haW9yIHF1ZSAxMCUgZGEgcG9wdWxhw6fDo28gdG90YWwgJE4kLiIsICJCIjogIk8gbsO6bWVybyBlc3BlcmFkbyBkZSBzdWNlc3NvcyBlIGZyYWNhc3NvcyBuYSBhbW9zdHJhLCBkZWZpbmlkbyBwb3IgJG5wJCBlICRuKDEtcCkkLCBkZXZlIHNlciBzdWZpY2llbnRlbWVudGUgZ3JhbmRlIChnZXJhbG1lbnRlICRcXGdlIDUkIG91ICQxMCQpLiIsICJDIjogIkEgcHJvcG9yw6fDo28gYW1vc3RyYWwgJFxcaGF0e3B9JCBkZXZlIHNlciBleGF0YW1lbnRlIGlndWFsIMOgIHByb3BvcsOnw6NvIHBvcHVsYWNpb25hbCAkcCQuIiwgIkQiOiAiQSB2YXJpw6JuY2lhIGRhIHByb3BvcsOnw6NvIGFtb3N0cmFsIGRldmUgc2VyIHNlbXByZSBpZ3VhbCBhIDEuIiwgIkUiOiAiTyB0YW1hbmhvIGFtb3N0cmFsICRuJCBkZXZlIHNlciBvYnJpZ2F0b3JpYW1lbnRlIHVtIG7Dum1lcm8gcHJpbW8gcGFyYSBldml0YXIgdmllc2VzIGRlIGFycmVkb25kYW1lbnRvIG5vIGPDoWxjdWxvIGRlICRaX3tcXHRleHR7Y2FsY319JC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkEgYXByb3hpbWHDp8OjbyBub3JtYWwgw6kgYmFzZWFkYSBubyBUZW9yZW1hIENlbnRyYWwgZG8gTGltaXRlIGFwbGljYWRvIMOgIHZhcmnDoXZlbCBiaW5vbWlhbC4gTyBjb21wb3J0YW1lbnRvIGRhIGRpc3RyaWJ1acOnw6NvIGJpbm9taWFsIHNlIHRvcm5hIFxcc2ltw6l0cmljbyBlIHByw7N4aW1vIGRhIG5vcm1hbCBjb25mb3JtZSBhIHF1YW50aWRhZGUgZGUgJ3N1Y2Vzc29zJyBlICdmcmFjYXNzb3MnIGVzcGVyYWRvcyBjcmVzY2UuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIHZhbGlkYWRlIGRhIGFwcm94aW1hw6fDo28gZGEgZGlzdHJpYnVpw6fDo28gYmlub21pYWwgKHF1ZSBkZXNjcmV2ZSBvIG7Dum1lcm8gZGUgc3VjZXNzb3MpIHBlbGEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIGRlcGVuZGUgZGUgbyB0YW1hbmhvIGFtb3N0cmFsIHNlciBncmFuZGUgbyBzdWZpY2llbnRlIHBhcmEgcXVlIGEgZGlzdHJpYnVpw6fDo28gbsOjbyBzZWphIHNldmVyYW1lbnRlIGFzc2ltw6l0cmljYS4gQSByZWdyYSBwcsOhdGljYSBtYWlzIHV0aWxpemFkYSDDqSBxdWUgJG5wXzAgXFxnZSA1JCBlICRuKDEtcF8wKSBcXGdlIDUkLCBvIHF1ZSBnYXJhbnRlIHF1ZSBhcyBjYXVkYXMgZGEgZGlzdHJpYnVpw6fDo28gYmlub21pYWwgZXN0ZWphbSBiZW0gcmVwcmVzZW50YWRhcyBwZWxhIGN1cnZhIG5vcm1hbCwganVzdGlmaWNhbmRvIG8gdXNvIGRhIGVzdGF0w61zdGljYSAkWl97XFx0ZXh0e2NhbGN9fSQuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcywgdW0gZW5nZW5oZWlybyB0ZXN0YSBhIGhpcMOzdGVzZSBudWxhICRIXzA6IFxcbXUgPSAxMDAkIG1BIChjb3JyZW50ZSBub21pbmFsKSBjb250cmEgYSBhbHRlcm5hdGl2YSAkSF8xOiBcXG11IFxcbmVxIDEwMCQgbUEuIEFww7NzIGNvbGV0YXIgdW1hIGFtb3N0cmEgZGUgJG4gPSA2NCQgdW5pZGFkZXMgZSBjYWxjdWxhciBhIGVzdGF0w61zdGljYSAkWl97XHRleHR7Y2FsY319ID0gMi4wNSQsIGVsZSBkZXNlamEgY2FsY3VsYXIgbyAkcFx0ZXh0ey12YWxvcn0kIHBhcmEgZGVjaWRpciBzZSBhIGNvcnJlbnRlIG3DqWRpYSBkaWZlcmUgc2lnbmlmaWNhdGl2YW1lbnRlIGRvIHZhbG9yIG5vbWluYWwuIFNhYmVuZG8gcXVlIGEgZGlzdHJpYnVpw6fDo28gZGEgZXN0YXTDrXN0aWNhIHNvYiAkSF8wJCDDqSBhIG5vcm1hbCBwYWRyw6NvICROKDAsIDEpJCwgcXVhbCDDqSBvICRwXHRleHR7LXZhbG9yfSQgY29ycmV0byBwYXJhIGVzdGUgdGVzdGUgYmlsYXRlcmFsPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJFAoWiA+IDIuMDUpIFxcYXBwcm94IDAuMDIwMiQiLCAiQiI6ICIkMiBcXHRpbWVzIFAoWiA+IDIuMDUpIFxcYXBwcm94IDAuMDQwNCQiLCAiQyI6ICIkUChaIDwgMi4wNSkgXFxhcHByb3ggMC45Nzk4JCIsICJEIjogIiQxIC0gUChaID4gMi4wNSkgXFxhcHByb3ggMC45Nzk4JCIsICJFIjogIiQwLjUgXFx0aW1lcyBQKFogPiAyLjA1KSBcXGFwcHJveCAwLjAxMDEkIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIGVtIHVtIHRlc3RlIGJpbGF0ZXJhbCwgYSBldmlkw6puY2lhIGNvbnRyYSBhIGhpcMOzdGVzZSBudWxhIG9jb3JyZSB0YW50byBlbSB2YWxvcmVzIG11aXRvIGdyYW5kZXMgcXVhbnRvIGVtIHZhbG9yZXMgbXVpdG8gcGVxdWVub3MgZGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlLiBPICRwXHRleHR7LXZhbG9yfSQgZGV2ZSBjYXB0dXJhciBhIHByb2JhYmlsaWRhZGUgZGUgYW1iYXMgYXMgY2F1ZGFzLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUGFyYSB1bSB0ZXN0ZSBiaWxhdGVyYWwgb25kZSBhIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIHBhZHLDo28sIG8gJHBcdGV4dHstdmFsb3J9JCDDqSBkZWZpbmlkbyBjb21vIGEgcHJvYmFiaWxpZGFkZSBkZSBvYnNlcnZhciB1bSB2YWxvciBhYnNvbHV0byBkYSBlc3RhdMOtc3RpY2EgbWFpb3Igb3UgaWd1YWwgYW8gb2JzZXJ2YWRvLCBvdSBzZWphLCAkcFx0ZXh0ey12YWxvcn0gPSAyIFxcdGltZXMgUChaID4gfFpfe1x0ZXh0e2NhbGN9fXwpJC4gQ29tICRaX3tcdGV4dHtjYWxjfX0gPSAyLjA1JCwgdGVtb3MgJFAoWiA+IDIuMDUpIFxcYXBwcm94IDAuMDIwMiQuIFBvcnRhbnRvLCAkcFx0ZXh0ey12YWxvcn0gPSAyIFxcdGltZXMgMC4wMjAyID0gMC4wNDA0JC4gRXN0ZSB2YWxvciBpbmRpY2EgdW1hIGV2aWTDqm5jaWEgY29udHJhICRIXzAkIHF1ZSBkZXZlIHNlciBjb21wYXJhZGEgY29tIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCBlc2NvbGhpZG8gcGVsbyBwZXNxdWlzYWRvci4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAyMDApXG55ID0gc3RhdHMubm9ybS5wZGYoeCwgMCwgMSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbmFtZT0nTigwLDEpJywgbGluZT1kaWN0KGNvbG9yPScjMUUzQThBJywgd2lkdGg9MikpKVxuIyDDgXJlYSBkZSByZWplacOnw6NvXG5tYXNrID0gKHggPiAyLjA1KSB8ICh4IDwgLTIuMDUpXG5maWcuYWRkX3RyYWNlKGdvLkZpbGwoeD1ucC5jb25jYXRlbmF0ZShbeFttYXNrXSwgW3hbbWFza11bLTFdLCB4W21hc2tdWzBdXV0pLCB5PW5wLmNvbmNhdGVuYXRlKFt5W21hc2tdLCBbMCwgMF1dKSwgZmlsbD0ndG9zZWxmJywgZmlsbGNvbG9yPScjOTkxQjFCJywgbmFtZT0ncC12YWxvci8yJykpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nVmlzdWFsaXphw6fDo28gZG8gcC12YWxvciAoVGVzdGUgQmlsYXRlcmFsKScsIHhheGlzX3RpdGxlPSdaJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM0OSJ9LCB7ImVudW5jaWFkbyI6ICJVbSBwZXNxdWlzYWRvciBlc3TDoSB0ZXN0YW5kbyBhIGVmaWPDoWNpYSBkZSB1bSBub3ZvIGFkaXRpdm8gZW0gY29tYnVzdMOtdmVpcyBjb20gJEhfMDogXFxtdSA9IDE1JCBrbS9sIGNvbnRyYSAkSF8xOiBcXG11ID4gMTUkIGttL2wuIEFww7NzIG8gZXhwZXJpbWVudG8sIGVsZSBvYnTDqW0gdW0gJHBcdGV4dHstdmFsb3J9ID0gMC4wMzUkLiBDb25zaWRlcmFuZG8gdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGRlICRcXGFscGhhID0gMC4wNSQsIHF1YWwgZGFzIGFsdGVybmF0aXZhcyBhYmFpeG8gZGVzY3JldmUgY29ycmV0YW1lbnRlIGEgY29uY2x1c8OjbyBlc3RhdMOtc3RpY2E/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJDb21vIG8gJHBcdGV4dHstdmFsb3J9IDwgXFxhbHBoYSQsIG7Do28gaMOhIGV2aWTDqm5jaWFzIHN1ZmljaWVudGVzIHBhcmEgcmVqZWl0YXIgJEhfMCQuIiwgIkIiOiAiQ29tbyBvICRwXHRleHR7LXZhbG9yfSA+IFxcYWxwaGEkLCByZWplaXRhbW9zICRIXzAkIGUgYWNlaXRhbW9zICRIXzEkLiIsICJDIjogIkNvbW8gbyAkcFx0ZXh0ey12YWxvcn0gPCBcXGFscGhhJCwgcmVqZWl0YW1vcyAkSF8wJCwgaW5kaWNhbmRvIGV2aWTDqm5jaWEgc2lnbmlmaWNhdGl2YSBkZSBxdWUgbyBhZGl0aXZvIGF1bWVudGEgYSBlZmljacOqbmNpYS4iLCAiRCI6ICJPICRwXHRleHR7LXZhbG9yfSQgZGUgJDAuMDM1JCBwcm92YSBxdWUgYSBtw6lkaWEgcG9wdWxhY2lvbmFsIMOpIGV4YXRhbWVudGUgJDE1JCBrbS9sLiIsICJFIjogIkEgZGVjaXPDo28gZGVwZW5kZSBkbyB0YW1hbmhvIGFtb3N0cmFsLCBuw6NvIHNlbmRvIHBvc3PDrXZlbCBjb25jbHVpciBzZW0gJG4kLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiTyAkcFx0ZXh0ey12YWxvcn0kIHJlcHJlc2VudGEgYSBwcm9iYWJpbGlkYWRlIGRlIG9ic2VydmFyIHJlc3VsdGFkb3MgdMOjbyBvdSBtYWlzIGV4dHJlbW9zIHNvYiBhIHZhbGlkYWRlIGRlICRIXzAkLiBRdWFuZG8gZXNzZSBsaW1pYXIgw6kgbWVub3IgcXVlICRcXGFscGhhJCwgYSAnc3VycHJlc2EnIMOpIGFsdGEgZGVtYWlzIHBhcmEgbWFudGVyIGEgaGlww7N0ZXNlIG51bGEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIHRvbWFkYSBkZSBkZWNpc8OjbyBlc3RhdMOtc3RpY2EgYmFzZWlhLXNlIG5hIGNvbXBhcmHDp8OjbyBlbnRyZSBvICRwXHRleHR7LXZhbG9yfSQgZSBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgZml4YWRvLiBTZSAkcFx0ZXh0ey12YWxvcn0gXFxsZXEgXFxhbHBoYSQsIG8gcmVzdWx0YWRvIMOpIGNvbnNpZGVyYWRvIGVzdGF0aXN0aWNhbWVudGUgc2lnbmlmaWNhdGl2byBhbyBuw612ZWwgJFxcYWxwaGEkLCBmb3JuZWNlbmRvIGV2aWTDqm5jaWEgcGFyYSByZWplaXRhciBhIGhpcMOzdGVzZSBudWxhICRIXzAkLiBObyBjYXNvLCAkMC4wMzUgPCAwLjA1JCwgbyBxdWUgbm9zIGxldmEgYSByZWplaXRhciAkSF8wJCBlbSBmYXZvciBkYSBhbHRlcm5hdGl2YSAkSF8xJC4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNDgifSwgeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgZGUgY29tcG9uZW50ZXMgZWxldHLDtG5pY29zIHV0aWxpemEgdW0gcHJvY2Vzc28gYXV0b21hdGl6YWRvIGRlIHNvbGRhZ2VtIG9uZGUgYSByZXNpc3TDqm5jaWEgKCRYJCkgZGUgY2FkYSBzb2xkYSwgZW0gTmV3dG9ucywgc2VndWUgdW1hIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCAkWCBcdGV4dHsgfiB9IE4oXFxtdSwgMTAwKSQuIE8gcGFkcsOjbyBkZSBxdWFsaWRhZGUgZXhpZ2UgJFxcbXUgPSAxMDAkLiBTdXNwZWl0YS1zZSBxdWUgbyBwcm9jZXNzbyB0ZW5oYSBwZXJkaWRvIHByZWNpc8OjbyBlIHF1ZSBhIG3DqWRpYSB0ZW5oYSBjYcOtZG8gcGFyYSAkXFxtdSA9IDk2JC4gQ29tIGJhc2UgZW0gdW1hIGFtb3N0cmEgYWxlYXTDs3JpYSBkZSAkbiA9IDI1JCBzb2xkYXMsIGEgZGlyZXRvcmlhIGVzdGFiZWxlY2V1IGEgcmVnacOjbyBjcsOtdGljYSAkUkMgPSBcXHtcXGJhcntYfSBcXGluIFxcbWF0aGJie1J9IHwgXFxiYXJ7WH0gPCA5Niw1XFx9JC4gQ29uc2lkZXJhbmRvIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhID0gUChcXHRleHR7UmVqZWl0YXIgfSBIXzAgfCBIXzAgXFx0ZXh0eyDDqSB2ZXJkYWRlaXJhfSkkLCBhc3NpbmFsZSBhIGFsdGVybmF0aXZhIHF1ZSBpbmRpY2EgY29ycmV0YW1lbnRlIGEgcHJvYmFiaWxpZGFkZSBkbyBlcnJvIGRlIHRpcG8gSSAoJFxcYWxwaGEkKSBlIGEgaW50ZXJwcmV0YcOnw6NvIGRvIHBvZGVyIGRvIHRlc3RlLiIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJFxcYWxwaGEgPSAwLDAyMjgkIGUgbyBwb2RlciBkbyB0ZXN0ZSDDqSBhIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgJEhfMCQgcXVhbmRvICRcXG11ID0gMTAwJC4iLCAiQiI6ICIkXFxhbHBoYSA9IDAsMDIyOCQgZSBvIHBvZGVyIGRvIHRlc3RlIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSByZWplaXRhciAkSF8wJCBxdWFuZG8gJFxcbXUgPSA5NiQuIiwgIkMiOiAiJFxcYWxwaGEgPSAwLDA1MDAkIGUgbyBwb2RlciBkbyB0ZXN0ZSDDqSBhIHByb2JhYmlsaWRhZGUgZGUgYWNlaXRhciAkSF8wJCBxdWFuZG8gJFxcbXUgPSA5NiQuIiwgIkQiOiAiJFxcYWxwaGEgPSAwLDA0NTYkIGUgbyBwb2RlciBkbyB0ZXN0ZSDDqSBhIHByb2JhYmlsaWRhZGUgZGUgbsOjbyByZWplaXRhciAkSF8wJCBxdWFuZG8gJFxcbXUgPSA5NiQuIiwgIkUiOiAiJFxcYWxwaGEgPSAwLDAyMjgkIGUgbyBwb2RlciBkbyB0ZXN0ZSDDqSBhIHByb2JhYmlsaWRhZGUgZGUgbsOjbyByZWplaXRhciAkSF8wJCBxdWFuZG8gJFxcbXUgPSA5NiQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIHNvYiAkSF8wJCwgJFxcYmFye1h9IFxcc2ltIE4oMTAwLCAxMDAvMjUpJC4gTyBlcnJvIHRpcG8gSSBvY29ycmUgbmEgYm9yZGEgZGEgaGlww7N0ZXNlIG51bGEuIE8gcG9kZXIgZG8gdGVzdGUgw6kgJDEtXFxiZXRhJCwgY2FsY3VsYWRvIHNvYiBhIGhpcMOzdGVzZSBhbHRlcm5hdGl2YSAkXFxtdSA9IDk2JC4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlByaW1laXJvLCBjYWxjdWxhbW9zICRcXGFscGhhJDogU29iICRIXzA6IFxcbXUgPSAxMDAkLCB0ZW1vcyAkXFxiYXJ7WH0gXFxzaW0gTigxMDAsIFxcc2lnbWFeMi9uKSA9IE4oMTAwLCAxMDAvMjUpID0gTigxMDAsIDQpJC4gTyBkZXN2aW8gcGFkcsOjbyDDqSAkXFxzaWdtYV97XFxiYXJ7WH19ID0gMiQuIEVudMOjbywgJFxcYWxwaGEgPSBQKFxcYmFye1h9IDwgOTYsNSB8IFxcbXUgPSAxMDApID0gUChaIDwgKDk2LDUgLSAxMDApIC8gMikgPSBQKFogPCAtMSw3NSkgPSAwLDA0MDEkIChhcHJveGltYWRhbWVudGUsIG1hcyBuYSBub3JtYWwgcGFkcsOjbyAkUChaIDwgLTIpID0gMCwwMjI4JCkuIFBhcmEgJFxcbXUgPSA5Niw1JCwgbyBlcnJvIMOpICQwLDAyMjgkLiBPIHBvZGVyIGRvIHRlc3RlICRcXHBpKDk2KSQgw6kgYSBwcm9iYWJpbGlkYWRlIGRlIGNhaXIgbmEgcmVnacOjbyBjcsOtdGljYSBkYWRvIHF1ZSAkXFxtdSA9IDk2JC4gTG9nbywgJFxccGkoOTYpID0gUChcXGJhcntYfSA8IDk2LDUgfCBcXG11ID0gOTYpID0gUChaIDwgKDk2LDUgLSA5NikgLyAyKSA9IFAoWiA8IDAsMjUpID0gMCw1OTg3JC4gQSBhbHRlcm5hdGl2YSBjb3JyZXRhIGlkZW50aWZpY2EgbyBjb25jZWl0byBkZSBwb2RlciBlIG8gdmFsb3IgJFxcYWxwaGEkLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1bOTIsIDEwOF0sIHk9WzAsIDBdLCBtb2RlPSdsaW5lcycsIGxpbmU9ZGljdChjb2xvcj0nI0UyRThGMCcpKSlcbnggPSBucC5saW5zcGFjZSg5MCwgMTEwLCAyMDApXG55X2gwID0gKDEvKDIqbnAuXFxzcXJ0KDIqbnAuXFxwaSkpKSAqIG5wLlxcZXhwKC0wLjUqKCh4LTEwMCkvMikqKjIpXG55X2gxID0gKDEvKDIqbnAuXFxzcXJ0KDIqbnAuXFxwaSkpKSAqIG5wLlxcZXhwKC0wLjUqKCh4LTk2KS8yKSoqMilcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eV9oMCwgbmFtZT1yJ0hfMDogJFxcbXU9MTAwJCcsIGxpbmU9ZGljdChjb2xvcj0nIzFFM0E4QScsIHdpZHRoPTIpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eV9oMSwgbmFtZT1yJ0hfMTogJFxcbXU9OTYkJywgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJywgd2lkdGg9MikpKVxuZmlnLmFkZF92bGluZSh4PTk2LjUsIGxpbmVfZGFzaD0nZGFzaCcsIGxpbmVfY29sb3I9JyMxRTI5M0InLCBhbm5vdGF0aW9uX3RleHQ9J1JDIDwgOTYuNScpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+RGlzdHJpYnVpw6fDtWVzIGUgUmVnacOjbyBDcsOtdGljYTwvYj4nLCB4YXhpc190aXRsZT0nTcOpZGlhIEFtb3N0cmFsICgkXFxiYXJ7WH0kKScsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzMzIifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gdGVzdGUgZGUgaGlww7N0ZXNlcyBwYXJhIGEgbcOpZGlhIHBvcHVsYWNpb25hbCwgJEhfMDogXFxtdSA9IDUwJCB2cyAkSF8xOiBcXG11ID4gNTAkLCBjb20gZGVzdmlvIHBhZHLDo28gY29uaGVjaWRvICRcXHNpZ21hID0gMTAkIGUgYW1vc3RyYSAkbiA9IDEwMCQsIGRlZmluZS1zZSBhIHJlZ3JhIGRlIGRlY2lzw6NvOiByZWplaXRhciAkSF8wJCBzZSAkXFxiYXJ7WH0gPiA1MSw2NDUkLiBRdWFsIMOpIG8gY29tcG9ydGFtZW50byBkYSBmdW7Dp8OjbyBwb2RlciAkXFxwaShcXG11KSQgw6AgbWVkaWRhIHF1ZSBvIHZhbG9yIHZlcmRhZGVpcm8gZGUgJFxcbXUkIHNlIGFmYXN0YSBkZSA1MCBwYXJhIHZhbG9yZXMgbWFpb3Jlcz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgZnVuw6fDo28gcG9kZXIgJFxccGkoXFxtdSkkIHBlcm1hbmVjZSBjb25zdGFudGUgZW0gMCwwNS4iLCAiQiI6ICJBIGZ1bsOnw6NvIHBvZGVyICRcXHBpKFxcbXUpJCBkZWNyZXNjZSwgYXByb3hpbWFuZG8tc2UgZGUgMC4iLCAiQyI6ICJBIGZ1bsOnw6NvIHBvZGVyICRcXHBpKFxcbXUpJCBjcmVzY2UsIGFwcm94aW1hbmRvLXNlIGRlIDEuIiwgIkQiOiAiQSBmdW7Dp8OjbyBwb2RlciAkXFxwaShcXG11KSQgb3NjaWxhIGVtIHRvcm5vIGRlIDAsNTAuIiwgIkUiOiAiTyBwb2RlciBkbyB0ZXN0ZSBuw6NvIMOpIGRlZmluaWRvIHBhcmEgdmFsb3JlcyBkZSAkXFxtdSQgZGlmZXJlbnRlcyBkZSA1MC4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIk8gcG9kZXIgZG8gdGVzdGUgw6kgYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIGRhZG8gcXVlIGVsYSDDqSBmYWxzYS4gUXVhbnRvIG1haXMgZGlzdGFudGUgbyB2YWxvciByZWFsIGRlICRcXG11JCBlc3RpdmVyIGRlICRcXG11XzAkIChuYSBkaXJlw6fDo28gZGUgJEhfMSQpLCBtYWlzIGbDoWNpbCDDqSBwYXJhIGEgYW1vc3RyYSBkZXRlY3RhciBlc3NhIGRpZmVyZW7Dp2EuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJPIHBvZGVyIGRvIHRlc3RlIMOpIGRhZG8gcG9yICRcXHBpKFxcbXUpID0gUChcXGJhcntYfSA+IDUxLDY0NSB8IFxcbXUpJC4gUGFyYSAkXFxtdSA+IDUwJCwgdGVtb3MgJFxcYmFye1h9IFxcc2ltIE4oXFxtdSwgXFxzaWdtYV4yL24pID0gTihcXG11LCAxMDAvMTAwKSA9IE4oXFxtdSwgMSkkLiBBc3NpbSwgJFxccGkoXFxtdSkgPSBQKFogPiA1MSw2NDUgLSBcXG11KSQuIFNlICRcXG11JCBhdW1lbnRhIChleDogJFxcbXU9NTIsIDUzLCAuLi4kKSwgbyB0ZXJtbyAkKDUxLDY0NSAtIFxcbXUpJCB0b3JuYS1zZSBjYWRhIHZleiBtYWlzIG5lZ2F0aXZvLiBDb21vIGEgY2F1ZGEgZGEgbm9ybWFsIHBhZHLDo28gJFAoWiA+IC1rKSQgY3Jlc2NlIMOgIG1lZGlkYSBxdWUgJC1rJCBkaW1pbnVpIChvdSBzZWphLCAkayQgYXVtZW50YSksIGEgcHJvYmFiaWxpZGFkZSBkZSByZWplacOnw6NvIGF1bWVudGEsIHRlbmRlbmRvIGEgMS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNDcifV0sICJxdWVzdG9lc19kaXNjdXJzaXZhcyI6IFt7ImVudW5jaWFkbyI6ICJVbSBmYWJyaWNhbnRlIGdhcmFudGUgcXVlIDkwJSBkYXMgcGXDp2FzIHByb2R1emlkYXMgcG9yIHVtIHByb2Nlc3NvIGluZHVzdHJpYWwgYXRlbmRlbSDDoHMgZXNwZWNpZmljYcOnw7Vlcy4gVW0gYXVkaXRvciwgc3VzcGVpdGFuZG8gZGUgcmVkdcOnw6NvIG5hIHF1YWxpZGFkZSwgdGVzdGEgJEhfMDogcCA9IDAsOTAkIGNvbnRyYSAkSF8xOiBwIDwgMCw5MCQgY29tIHVtYSBhbW9zdHJhIGRlICRuID0gMjAwJCBwZcOnYXMuIE5hIGFtb3N0cmEsIGVuY29udHJvdS1zZSAkXFxoYXR7cH0gPSAwLDg1JC4gRXhwbGlxdWUgbyBwcm9jZWRpbWVudG8gbMOzZ2ljbyBwYXJhIHJlYWxpemFyIGVzdGUgdGVzdGUgdXRpbGl6YW5kbyB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgZGUgJFxcYWxwaGEgPSA1XFwlJC4iLCAiZGljYSI6ICJVdGlsaXplIGEgYXByb3hpbWHDp8OjbyBkYSBiaW5vbWlhbCBwZWxhIG5vcm1hbCwgb25kZSBhIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSDDqSAkWl97XFx0ZXh0e2NhbGN9fSA9IChcXGhhdHtwfSAtIHBfMCkgLyBcXHNxcnR7cF8wKDEtcF8wKS9ufSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIERlZmluaXIgaGlww7N0ZXNlczogJEhfMDogcCA9IDAsOTAkIGUgJEhfMTogcCA8IDAsOTAkLiIsICIyLiBDYWxjdWxhciBlcnJvIHBhZHLDo286ICRFUCA9IFxcc3FydHswLDkwIFxcdGltZXMgMCwxMCAvIDIwMH0gPSBcXHNxcnR7MCwwOSAvIDIwMH0gXFxhcHByb3ggMCwwMjEyJC4iLCAiMy4gQ2FsY3VsYXIgZXN0YXTDrXN0aWNhICRaX3tcXHRleHR7Y2FsY319ID0gKDAsODUgLSAwLDkwKSAvIDAsMDIxMiBcXGFwcHJveCAtMiwzNiQuIiwgIjQuIEVuY29udHJhciAkWl97XFx0ZXh0e2NyaXR9fSQgcGFyYSAkXFxhbHBoYT0wLDA1JCAodW5pbGF0ZXJhbCk6ICRaX3tcXHRleHR7Y3JpdH19ID0gLTEsNjQ1JC4iLCAiNS4gRGVjaXPDo286IENvbW8gJFpfe1xcdGV4dHtjYWxjfX0gPCBaX3tcXHRleHR7Y3JpdH19JCwgcmVqZWl0YW1vcyAkSF8wJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IC0yLjM2fSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gcHJvYmxlbWEgYW50ZXJpb3IsIG9uZGUgJEhfMDogcCA9IDAsOTAkIGUgJEhfMTogcCA8IDAsOTAkIGNvbSAkbj0yMDAkLiBTZSBvIHZlcmRhZGVpcm8gcGFyw6JtZXRybyBwb3B1bGFjaW9uYWwgZm9yICRwID0gMCw4NSQsIHF1YWwgw6kgYSBwcm9iYWJpbGlkYWRlIGRlIGNvbWV0ZXIgdW0gZXJybyBkbyB0aXBvIElJIChuw6NvIHJlamVpdGFyICRIXzAkIHF1YW5kbyAkSF8xJCDDqSB2ZXJkYWRlaXJhKT8iLCAiZGljYSI6ICJPIGVycm8gZG8gdGlwbyBJSSDDqSAkXFxiZXRhID0gUChcXHRleHR7bsOjbyByZWplaXRhciB9IEhfMCB8IHA9MCw4NSkkLiBOw6NvIHJlamVpdGFyICRIXzAkIHNpZ25pZmljYSAkXFxoYXR7cH0gPiBwX3tcXHRleHR7Y3JpdH19JC4gRW5jb250cmUgbyB2YWxvciBjcsOtdGljbyBwYXJhICRcXGhhdHtwfSQgdXNhbmRvICRcXGFscGhhPTVcXCUkIHNvYiAkSF8wJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gVmFsb3IgY3LDrXRpY28gcGFyYSAkXFxoYXR7cH0kIHNvYiAkSF8wJDogJFxcaGF0e3B9X2MgPSAwLDkwIC0gMSw2NDUgXFx0aW1lcyAwLDAyMTIgPSAwLDg2NSQuIiwgIjIuIENhbGN1bGFyICRcXGJldGEgPSBQKFxcaGF0e3B9ID4gMCw4NjUgfCBwID0gMCw4NSkkLiIsICIzLiBOb3ZvIGVycm8gcGFkcsOjbyBzb2IgJHA9MCw4NSQ6ICRFUCA9IFxcc3FydHswLDg1IFxcdGltZXMgMCwxNSAvIDIwMH0gXFxhcHByb3ggMCwwMjUyJC4iLCAiNC4gJFogPSAoMCw4NjUgLSAwLDg1KSAvIDAsMDI1MiBcXGFwcHJveCAwLDU5NSQuIiwgIjUuICRcXGJldGEgPSBQKFogPiAwLDU5NSkgXFxhcHByb3ggMCwyNzYkLiAiXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMjc2fSwgeyJlbnVuY2lhZG8iOiAiRGlzY29ycmEgc29icmUgYSByZWxhw6fDo28gZW50cmUgbyBwb2RlciBkbyB0ZXN0ZSAoJDEgLSBcXGJldGEkKSBlIG8gdGFtYW5obyBhbW9zdHJhbCAkbiQuIENvbW8gdW0gYXVtZW50byBlbSAkbiQgYWZldGEgbyBwb2RlciBkbyB0ZXN0ZSwgbWFudGVuZG8gJFxcYWxwaGEkIGZpeG8sIGUgcXVhbCBhIGltcGxpY2HDp8OjbyBwcsOhdGljYSBkaXNzbyBlbSBlbnNhaW9zIGNsw61uaWNvcz8iLCAiZGljYSI6ICJDb25zaWRlcmUgcXVlIG8gZXJybyBwYWRyw6NvICRFUChcXGJhcntYfSkgPSBcXHNpZ21hIC8gXFxzcXJ0e259JCBkaW1pbnVpIMOgIG1lZGlkYSBxdWUgJG4kIGF1bWVudGEsIHRvcm5hbmRvIGEgZGlzdHJpYnVpw6fDo28gZGEgZXN0YXTDrXN0aWNhIG1haXMgZXN0cmVpdGEgZSBhdW1lbnRhbmRvIGEgc2Vuc2liaWxpZGFkZSBwYXJhIGRldGVjdGFyIGRlc3Zpb3MgZGUgJFxcbXVfMCQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIEV4cGxpY2HDp8OjbzogTyBwb2RlciAkMSAtIFxcYmV0YSQgw6kgYSBjYXBhY2lkYWRlIGRlIHJlamVpdGFyIGNvcnJldGFtZW50ZSAkSF8wJCBxdWFuZG8gZWxhIMOpIGZhbHNhLiIsICIyLiBFZmVpdG8gZGUgJG4kOiBBbyBhdW1lbnRhciAkbiQsIG8gZXJybyBwYWRyw6NvIGRpbWludWksIG8gcXVlIHJlZHV6IGEgc29icmVwb3Npw6fDo28gZW50cmUgYXMgZGlzdHJpYnVpw6fDtWVzIHNvYiAkSF8wJCBlICRIXzEkLiIsICIzLiBJbXBsaWNhw6fDo286IElzc28gcGVybWl0ZSBxdWUgbyB0ZXN0ZSBkZXRlY3RlIG1lbm9yZXMgZGlmZXJlbsOnYXMgY2xpbmljYW1lbnRlIHNpZ25pZmljYXRpdmFzLCB0b3JuYW5kbyBvIGVzdHVkbyBtYWlzIHJvYnVzdG8gY29udHJhIG8gZXJybyBkbyB0aXBvIElJLiIsICI0LiBDb25jbHVzw6NvOiBBbW9zdHJhcyBtYWlvcmVzIHJlZHV6ZW0gYSBpbmNlcnRlemEgZXN0YXTDrXN0aWNhLCBwZXJtaXRpbmRvIGNvbmNsdXPDtWVzIG1haXMgcHJlY2lzYXMgc29icmUgYSBlZmljw6FjaWEgZGUgdHJhdGFtZW50b3MuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW1hIGFzc29jaWHDp8OjbyBkZSBpbmTDunN0cmlhcyBtZXRhbMO6cmdpY2FzIG1vbml0b3JhIGEgbcOpZGlhIGFudWFsIGRlIGhvcmFzIHBlcmRpZGFzIHBvciBhY2lkZW50ZXMsIGN1am8gaGlzdMOzcmljbyDDqSAkXFxtdV8wID0gNjAkIGhvcmFzLCBjb20gZGVzdmlvIHBhZHLDo28gcG9wdWxhY2lvbmFsICRcXHNpZ21hID0gMjAkIGhvcmFzLiBBcMOzcyBpbXBsZW1lbnRhciB1bSBub3ZvIHByb2dyYW1hIGRlIHNlZ3VyYW7Dp2EsIHVtYSBhbW9zdHJhIGRlICRuID0gMTAwJCBpbmTDunN0cmlhcyBhcHJlc2VudG91IG3DqWRpYSAkXFxiYXJ7WH0gPSA1NiQgaG9yYXMuIEFvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSBkZSAkXFxhbHBoYSA9IDAsMDUkLCBow6EgZXZpZMOqbmNpYSBkZSBtZWxob3JpYSAocmVkdcOnw6NvIG5hIG3DqWRpYSBkZSBob3JhcyBwZXJkaWRhcyk/IEFwcmVzZW50ZSBvIGPDoWxjdWxvIGRlICRaX3tcXHRleHR7Y2FsY319JCBlIGEgY29uY2x1c8Ojby4iLCAiZGljYSI6ICJVc2UgbyB0ZXN0ZSB1bmlsYXRlcmFsIMOgIGVzcXVlcmRhOiAkSF8wOiBcXG11ID0gNjAkIGNvbnRyYSAkSF8xOiBcXG11IDwgNjAkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJEZWZpbmnDp8OjbyBkYXMgaGlww7N0ZXNlczogJEhfMDogXFxtdSA9IDYwJCBlICRIXzE6IFxcbXUgPCA2MCQuIiwgIkPDoWxjdWxvIGRvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWE6ICRFUChcXGJhcntYfSkgPSBcXHNpZ21hIC8gXFxzcXJ0e259ID0gMjAgLyBcXHNxcnR7MTAwfSA9IDIwIC8gMTAgPSAyLDAkLiIsICJDw6FsY3VsbyBkYSBlc3RhdMOtc3RpY2EgZGUgdGVzdGU6ICRaX3tcXHRleHR7Y2FsY319ID0gKFxcYmFye1h9IC0gXFxtdV8wKSAvIEVQKFxcYmFye1h9KSA9ICg1NiAtIDYwKSAvIDIsMCA9IC00IC8gMiA9IC0yLDAkLiIsICJEZXRlcm1pbmHDp8OjbyBkbyB2YWxvciBjcsOtdGljbzogUGFyYSAkXFxhbHBoYSA9IDAsMDUkICh0ZXN0ZSB1bmlsYXRlcmFsKSwgJFpfe1xcdGV4dHtjcml0fX0gPSAtMSw2NDUkLiIsICJDb25jbHVzw6NvOiBDb21vICRaX3tcXHRleHR7Y2FsY319ID0gLTIsMCA8IFpfe1xcdGV4dHtjcml0fX0gPSAtMSw2NDUkLCByZWplaXRhbW9zICRIXzAkLiBIw6EgZXZpZMOqbmNpYSBlc3RhdMOtc3RpY2EgZGUgcXVlIG8gcHJvZ3JhbWEgZGUgc2VndXJhbsOnYSByZWR1eml1IGFzIGhvcmFzIG3DqWRpYXMgcGVyZGlkYXMuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiSW5zcGlyYWRvIGVtIEJ1c3NhYiAmIE1vcmV0dGluLCBFc3RhdMOtc3RpY2EgQsOhc2ljYSwgQ2FwIDEyLCBwLiAzNDMiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAtMi4wfSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUgbyBwYXBlbCBkbyB0YW1hbmhvIGFtb3N0cmFsICRuJCBuYSBwcmVjaXPDo28gZGEgZXN0aW1hdGl2YSBkYSBtw6lkaWEgcG9wdWxhY2lvbmFsIGRlbnRybyBkYSBmw7NybXVsYSBkbyBlcnJvIHBhZHLDo28gJEVQKFxcYmFye1h9KSA9IFxcc2lnbWEgLyBcXHNxcnR7bn0kLiBPIHF1ZSBvY29ycmUgY29tIGEgZGlzdHJpYnVpw6fDo28gZGEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSQgcXVhbmRvICRuJCBhdW1lbnRhIHNpZ25pZmljYXRpdmFtZW50ZT8iLCAiZGljYSI6ICJDb25zaWRlcmUgbyBUZW9yZW1hIENlbnRyYWwgZG8gTGltaXRlIChUQ0wpIGUgY29tbyBhIHZhcmlhYmlsaWRhZGUgYW1vc3RyYWwgZGltaW51aSBjb20gbyBhdW1lbnRvIGRlICRuJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSB2YXJpw6JuY2lhIGRhIG3DqWRpYSBhbW9zdHJhbCDDqSAkVmFyKFxcYmFye1h9KSA9IFxcc2lnbWFeMiAvIG4kLiIsICLDgCBtZWRpZGEgcXVlICRuJCBhdW1lbnRhLCBvIGRlbm9taW5hZG9yIGRvIGVycm8gcGFkcsOjbyBjcmVzY2UsIGZhemVuZG8gY29tIHF1ZSAkRVAoXFxiYXJ7WH0pJCBkaW1pbnVhIHByb3BvcmNpb25hbG1lbnRlIMOgIHJhaXogcXVhZHJhZGEgZGUgJG4kLiIsICJDb25zZXF1ZW50ZW1lbnRlLCBhIGRpc3RyaWJ1acOnw6NvIGRhcyBtw6lkaWFzIGFtb3N0cmFpcyAoJFxcYmFye1h9JCkgdG9ybmEtc2UgY2FkYSB2ZXogbWFpcyBjb25jZW50cmFkYSBlbSB0b3JubyBkYSBtw6lkaWEgcG9wdWxhY2lvbmFsIHZlcmRhZGVpcmEgKCRcXG11JCkuIiwgIlBlbG8gVGVvcmVtYSBDZW50cmFsIGRvIExpbWl0ZSwgaW5kZXBlbmRlbnRlbWVudGUgZGEgZGlzdHJpYnVpw6fDo28gb3JpZ2luYWwgZG9zIGRhZG9zLCBjb20gdW0gJG4kIHN1ZmljaWVudGVtZW50ZSBncmFuZGUsIGEgZGlzdHJpYnVpw6fDo28gZGUgJFxcYmFye1h9JCBhcHJveGltYS1zZSBkZSB1bWEgbm9ybWFsICROKFxcbXUsIFxcc2lnbWFeMi9uKSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiVW1hIGbDoWJyaWNhIGRlIGF1dG9wZcOnYXMgbWVkZSBvIGRpw6JtZXRybyBkZSBzZXVzIGNpbGluZHJvcy4gQSBtw6FxdWluYSBlc3TDoSByZWd1bGFkYSBwYXJhIHByb2R1emlyIGNpbGluZHJvcyBjb20gJFxcbXUgPSA1MCwwXFx0ZXh0eyBtbX0kIGUgZGVzdmlvIHBhZHLDo28gJFxcc2lnbWEgPSAyLDVcXHRleHR7IG1tfSQuIFVtYSBhbW9zdHJhIGRlICRuID0gNjQkIGNpbGluZHJvcyByZXN1bHRhIGVtICRcXGJhcntYfSA9IDUwLDZcXHRleHR7IG1tfSQuIENhbGN1bGUgYSBlc3RhdMOtc3RpY2EgJFpfe1xcdGV4dHtjYWxjfX0kIGUgZGV0ZXJtaW5lIG8gJHBcXHRleHR7LXZhbG9yfSQgYXByb3hpbWFkbyBwYXJhIHVtIHRlc3RlIGJpbGF0ZXJhbCwgY29tZW50YW5kbyBzb2JyZSBhIGFjZWl0YcOnw6NvIGRhIGhpcMOzdGVzZSBkZSBxdWUgYSBtw6FxdWluYSBvcGVyYSBjb3JyZXRhbWVudGUuIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBlbSB1bSB0ZXN0ZSBiaWxhdGVyYWwsIG8gJHBcXHRleHR7LXZhbG9yfSA9IDIgXFxjZG90IFAoWiA+IHxaX3tcXHRleHR7Y2FsY319fCkkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJFcnJvIFBhZHLDo286ICRFUChcXGJhcntYfSkgPSAyLDUgLyBcXHNxcnR7NjR9ID0gMiw1IC8gOCA9IDAsMzEyNSQuIiwgIkVzdGF0w61zdGljYSBkZSBUZXN0ZTogJFpfe1xcdGV4dHtjYWxjfX0gPSAoNTAsNiAtIDUwLDApIC8gMCwzMTI1ID0gMCw2IC8gMCwzMTI1ID0gMSw5MiQuIiwgIlBhcmEgdW0gdGVzdGUgYmlsYXRlcmFsLCBjb25zdWx0YW5kbyBhIHRhYmVsYSBaOiAkUChaID4gMSw5MikgXFxhcHByb3ggMCwwMjc0JC4iLCAicC12YWxvcjogJHBcXHRleHR7LXZhbG9yfSA9IDIgXFxjZG90IDAsMDI3NCA9IDAsMDU0OCQuIiwgIkNvbmNsdXPDo286IENvbW8gJHBcXHRleHR7LXZhbG9yfSAoMCwwNTQ4KSA+IDAsMDUkLCBuw6NvIHJlamVpdGFtb3MgJEhfMCQgYW8gbsOtdmVsIGRlIDUlLiBBIG3DoXF1aW5hIG9wZXJhIGRlbnRybyBkb3MgcGFkcsO1ZXMgZXNwZXJhZG9zLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMS45Mn0sIHsiZW51bmNpYWRvIjogIkVtIHVtYSBwZXNxdWlzYSBkZSBvcGluacOjbyByZWFsaXphZGEgY29tICRuID0gNDAwJCBlbGVpdG9yZXMsIG9ic2Vydm91LXNlIHF1ZSAkWCA9IDE4MCQgcHJldGVuZGVtIHZvdGFyIGVtIHVtIGNhbmRpZGF0byBlc3BlY8OtZmljby4gVGVzdGUgYSBoaXDDs3Rlc2UgZGUgcXVlIGEgcHJvcG9yw6fDo28gcmVhbCBkZSB2b3RvcyAkcCQgw6kgaWd1YWwgYSAwLjUwLCB1dGlsaXphbmRvIHVtIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSA9IDAuMDUkLiBDYWxjdWxlICRaX3tcXHRleHR7Y2FsY319JCBlIHRvbWUgc3VhIGRlY2lzw6NvIGVzdGF0w61zdGljYS4iLCAiZGljYSI6ICJDYWxjdWxlICRcXGhhdHtwfSA9IFgvbiQgZSB1dGlsaXplICRwXzAgPSAwLjUwJCBwYXJhIGNhbGN1bGFyIG8gZXJybyBwYWRyw6NvICRcXHNxcnR7XFxmcmFje3BfMCgxLXBfMCl9e259fSQuIE8gdmFsb3IgY3LDrXRpY28gcGFyYSAkXFxhbHBoYSA9IDAuMDUkICh0ZXN0ZSBiaWNhdWRhbCkgw6kgJFxccG0gMS45NiQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIERlZmluaXIgaGlww7N0ZXNlczogJEhfMDogcCA9IDAuNTAkIHZzICRIXzE6IHAgXFxuZXEgMC41MCQuIiwgIjIuIENhbGN1bGFyIGEgcHJvcG9yw6fDo28gYW1vc3RyYWw6ICRcXGhhdHtwfSA9IFxcZnJhY3sxODB9ezQwMH0gPSAwLjQ1JC4iLCAiMy4gQ2FsY3VsYXIgbyBlcnJvIHBhZHLDo286ICRFUCA9IFxcc3FydHtcXGZyYWN7MC41MCgwLjUwKX17NDAwfX0gPSBcXHNxcnR7XFxmcmFjezAuMjV9ezQwMH19ID0gXFxzcXJ0ezAuMDAwNjI1fSA9IDAuMDI1JC4iLCAiNC4gQ2FsY3VsYXIgJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7MC40NSAtIDAuNTB9ezAuMDI1fSA9IFxcZnJhY3stMC4wNX17MC4wMjV9ID0gLTIuMDAkLiIsICI1LiBDb25jbHVzw6NvOiBDb21vICR8LTIuMDB8ID4gMS45NiQsIHJlamVpdGFtb3MgJEhfMCQgYW8gbsOtdmVsIGRlIDUlIGRlIHNpZ25pZmljw6JuY2lhLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAyMDApXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLm5vcm0ucGRmKHgpLCBuYW1lPVwiTigwLDEpXCIsIGxpbmU9ZGljdChjb2xvcj1cIiMxRTNBOEFcIikpKVxuZmlnLmFkZF92bGluZSh4PS0yLjAsIGxpbmVfZGFzaD1cImRhc2hcIiwgbGluZV9jb2xvcj1cIiM5OTFCMUJcIiwgYW5ub3RhdGlvbl90ZXh0PXJcIiRaX3tcXHRleHR7Y2FsY319ID0gLTIuMDAkXCIpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT1cIkRpc3RyaWJ1acOnw6NvIE5vcm1hbCBlICRaX3tcXHRleHR7Y2FsY319JFwiLCB4YXhpc190aXRsZT1yXCJaXCIsIHlheGlzX3RpdGxlPXJcIkRlbnNpZGFkZVwiKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogLTIuMH0sIHsiZW51bmNpYWRvIjogIlVtIGZhYnJpY2FudGUgZGUgbMOibXBhZGFzIExFRCBhZmlybWEgcXVlIGEgcHJvcG9yw6fDo28gZGUgaXRlbnMgZGVmZWl0dW9zb3Mgw6kgZGUgbm8gbcOheGltbyAkcCA9IDAuMDIkLiBVbWEgYW1vc3RyYSBkZSAkbiA9IDEwMDAkIGzDom1wYWRhcyByZXZlbG91ICRYID0gMzAkIGRlZmVpdHVvc2FzLiBBbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLjAxJCwgZXhpc3RlIGV2aWTDqm5jaWEgc3VmaWNpZW50ZSBwYXJhIHJlamVpdGFyIGEgYWZpcm1hw6fDo28gZG8gZmFicmljYW50ZT8iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlICRIXzA6IHAgXFxsZSAwLjAyJCBlICRIXzE6IHAgPiAwLjAyJC4gTyB2YWxvciBjcsOtdGljbyAkWl97XFx0ZXh0e2NyaXR9fSQgcGFyYSAkXFxhbHBoYSA9IDAuMDEkIGVtIHVtIHRlc3RlIHVuaWxhdGVyYWwgw6kgJDIuMzMkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBIaXDDs3Rlc2VzOiAkSF8wOiBwID0gMC4wMiQgdnMgJEhfMTogcCA+IDAuMDIkLiIsICIyLiBQcm9wb3LDp8OjbyBhbW9zdHJhbDogJFxcaGF0e3B9ID0gMzAvMTAwMCA9IDAuMDMkLiIsICIzLiBFcnJvIHBhZHLDo286ICRFUCA9IFxcc3FydHtcXGZyYWN7MC4wMigwLjk4KX17MTAwMH19ID0gXFxzcXJ0ezAuMDAwMDE5Nn0gXFxhcHByb3ggMC4wMDQ0MjckLiIsICI0LiBDw6FsY3VsbyBkZSAkWl97XFx0ZXh0e2NhbGN9fSQ6ICRcXGZyYWN7MC4wMyAtIDAuMDJ9ezAuMDA0NDI3fSBcXGFwcHJveCAyLjI1OSQuIiwgIjUuIENvbXBhcmHDp8OjbzogJDIuMjU5IDwgMi4zMyQuIE7Do28gcmVqZWl0YW1vcyAkSF8wJCBhbyBuw612ZWwgZGUgMSUuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAyLjI1OX0sIHsiZW51bmNpYWRvIjogIkV4cGxpcXVlLCBkbyBwb250byBkZSB2aXN0YSBkYSBwcmVjaXPDo28gZGEgaW5mZXLDqm5jaWEsIHF1YWwgbyBlZmVpdG8gZG8gYXVtZW50byBkbyB0YW1hbmhvIGFtb3N0cmFsICRuJCBuYSBtYWduaXR1ZGUgZG8gZXJybyBwYWRyw6NvIGRhIHByb3BvcsOnw6NvIGFtb3N0cmFsIGUsIGNvbnNlcXVlbnRlbWVudGUsIG5hIHNlbnNpYmlsaWRhZGUgZG8gdGVzdGUgZGUgaGlww7N0ZXNlcy4iLCAiZGljYSI6ICJPYnNlcnZlIGEgZsOzcm11bGEgZG8gZXJybyBwYWRyw6NvOiAkRVAgPSBcXHNxcnR7XFxmcmFje3BfMCgxLXBfMCl9e259fSQuIE8gdGVybW8gJG4kIGVzdMOhIG5vIGRlbm9taW5hZG9yLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBBbmFsaXNhciBhIGbDs3JtdWxhICRFUCA9IFxcc3FydHtcXGZyYWN7cF8wKDEtcF8wKX17bn19JC4iLCAiMi4gQ29uY2x1aXIgcXVlLCBjb25mb3JtZSAkbiQgYXVtZW50YSwgbyB2YWxvciBkbyBkZW5vbWluYWRvciBhdW1lbnRhLCBmYXplbmRvIGNvbSBxdWUgJEVQJCBkaW1pbnVhLiIsICIzLiBJbnRlcnByZXRhciBxdWUgdW0gJEVQJCBtZW5vciBzaWduaWZpY2EgcXVlIGEgZXN0YXTDrXN0aWNhICRaX3tcXHRleHR7Y2FsY319JCB0b3JuYS1zZSBtYWlzIHNlbnPDrXZlbCBhIHBlcXVlbmFzIGRpc2NyZXDDom5jaWFzIGVudHJlICRcXGhhdHtwfSQgZSAkcF8wJC4iLCAiNC4gQ29uY2x1aXIgcXVlIGFtb3N0cmFzIG1haW9yZXMgYXVtZW50YW0gbyBwb2RlciBkbyB0ZXN0ZSwgZmFjaWxpdGFuZG8gYSByZWplacOnw6NvIGRlICRIXzAkIHF1YW5kbyBlbGEgw6kgZGUgZmF0byBmYWxzYS4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKClcbm4gPSBucC5hcmFuZ2UoMTAwLCAyMDAwLCA1MClcbmVwID0gbnAuXFxzcXJ0KDAuMjUgLyBuKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9biwgeT1lcCwgbGluZT1kaWN0KGNvbG9yPVwiIzEwQjk4MVwiLCB3aWR0aD0zKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT1cIkVmZWl0byBkZSAkbiQgbm8gRXJybyBQYWRyw6NvICgkcF8wPTAuNSQpXCIsIHhheGlzX3RpdGxlPXJcIlRhbWFuaG8gQW1vc3RyYWwgKCRuJClcIiwgeWF4aXNfdGl0bGU9clwiRXJybyBQYWRyw6NvXCIpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gdGVzdGUgZGUgaGlww7N0ZXNlcyAkSF8wOiBcXG11ID0gNTAkIGNvbnRyYSAkSF8xOiBcXG11ID4gNTAkIHBhcmEgdW1hIHZhcmnDoXZlbCBub3JtYWwgY29tICRcXHNpZ21hID0gMTAkLiBVbWEgYW1vc3RyYSBkZSAkbiA9IDI1JCByZXN1bHRhIGVtIHVtYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9ID0gNTMkLiBDYWxjdWxlIGEgZXN0YXTDrXN0aWNhICRaX3tcdGV4dHtjYWxjfX0kIGUgbyAkcFx0ZXh0ey12YWxvcn0kIGRvIHRlc3RlLiIsICJkaWNhIjogIk8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSDDqSAkRVAoXFxiYXJ7WH0pID0gXFxzaWdtYSAvIFxcc3FydHtufSQuIEEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlIMOpICRaX3tcdGV4dHtjYWxjfX0gPSAoXFxiYXJ7WH0gLSBcXG11XzApIC8gRVAoXFxiYXJ7WH0pJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gSWRlbnRpZmljYXIgb3MgcGFyw6JtZXRyb3M6ICRcXG11XzAgPSA1MCQsICRcXHNpZ21hID0gMTAkLCAkbiA9IDI1JCwgJFxcYmFye1h9ID0gNTMkLiIsICIyLiBDYWxjdWxhciBvIGVycm8gcGFkcsOjbzogJEVQKFxcYmFye1h9KSA9IFxcZnJhY3sxMH17XFxzcXJ0ezI1fX0gPSBcXGZyYWN7MTB9ezV9ID0gMiQuIiwgIjMuIENhbGN1bGFyIGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlOiAkWl97XHRleHR7Y2FsY319ID0gXFxmcmFjezUzIC0gNTB9ezJ9ID0gXFxmcmFjezN9ezJ9ID0gMS41JC4iLCAiNC4gQ2FsY3VsYXIgbyAkcFx0ZXh0ey12YWxvcn0kICh0ZXN0ZSB1bmlsYXRlcmFsIHN1cGVyaW9yKTogJHBcdGV4dHstdmFsb3J9ID0gUChaID4gMS41KSQuIiwgIjUuIENvbnN1bHRhbmRvIGEgdGFiZWxhIG5vcm1hbCBwYWRyw6NvLCAkUChaIFxcbGVxIDEuNSkgXFxhcHByb3ggMC45MzMyJC4gTG9nbywgJHBcdGV4dHstdmFsb3J9ID0gMSAtIDAuOTMzMiA9IDAuMDY2OCQuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTMsIDMsIDEwMClcbnkgPSBzdGF0cy5ub3JtLnBkZih4LCAwLCAxKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBuYW1lPSdEaXN0cmlidWnDp8OjbyBOKDAsMSknLCBsaW5lPWRpY3QoY29sb3I9JyMxRTNBOEEnKSkpXG5maWcuYWRkX3ZsaW5lKHg9MS41LCBsaW5lX2Rhc2g9J2Rhc2gnLCBsaW5lX2NvbG9yPScjOTkxQjFCJywgYW5ub3RhdGlvbl90ZXh0PSdaX2NhbGMgPSAxLjUnKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0PDoWxjdWxvIGRvIHAtdmFsb3IgKFVuaWxhdGVyYWwpJywgeGF4aXNfdGl0bGU9J1onLCB5YXhpc190aXRsZT0nRGVuc2lkYWRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiwgcC4gMzM5IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4wNjY4fSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUgY29uY2VpdHVhbG1lbnRlIGEgZGlmZXJlbsOnYSBlbnRyZSBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgZSBvICRwXHRleHR7LXZhbG9yfSQuIENvbW8gYSB1dGlsaXphw6fDo28gZG8gJHBcdGV4dHstdmFsb3J9JCBhbHRlcmEgYSBmbGV4aWJpbGlkYWRlIGRvIHBlc3F1aXNhZG9yIG5hIHRvbWFkYSBkZSBkZWNpc8OjbyBlbSBjb21wYXJhw6fDo28gY29tIGEgZml4YcOnw6NvIGRlIHVtIGxpbWlhciAkXFxhbHBoYSQgcsOtZ2lkbz8iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlICRcXGFscGhhJCDDqSBmaXhhZG8gYSBwcmlvcmksIGVucXVhbnRvIG8gJHBcdGV4dHstdmFsb3J9JCDDqSB1bWEgY2FyYWN0ZXLDrXN0aWNhIGRhIGFtb3N0cmEgb2JzZXJ2YWRhLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJPIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgw6kgYSBwcm9iYWJpbGlkYWRlIGRvIGVycm8gZGUgdGlwbyBJLCBmaXhhZG8gYXJiaXRyYXJpYW1lbnRlIHBlbG8gcGVzcXVpc2Fkb3IgYW50ZXMgZGEgY29sZXRhIGRlIGRhZG9zIChleDogNSUpLiIsICJPICRwXHRleHR7LXZhbG9yfSQgw6kgbyBuw612ZWwgZGVzY3JpdGl2bywgY2FsY3VsYWRvIGFww7NzIGEgb2J0ZW7Dp8OjbyBkb3MgZGFkb3MuIEVsZSByZXByZXNlbnRhIGEgZXZpZMOqbmNpYSBxdWFudGl0YXRpdmEgY29udHJhICRIXzAkLiIsICJBIGZpeGHDp8OjbyBkZSAkXFxhbHBoYSQgbGV2YSBhIHVtYSBkZWNpc8OjbyBiaW7DoXJpYSAocmVqZWl0YXIgb3UgbsOjbyByZWplaXRhcikuIiwgIk8gdXNvIGRvICRwXHRleHR7LXZhbG9yfSQgcGVybWl0ZSBhbyBwZXNxdWlzYWRvciBjb211bmljYXIgYSBmb3LDp2EgZGEgZXZpZMOqbmNpYSAoZXg6ICRwIDwgMC4wMDEkIMOpIHVtYSBldmlkw6puY2lhIG1haXMgZm9ydGUgcXVlICRwID0gMC4wNCQpLiIsICJBc3NpbSwgbyAkcFx0ZXh0ey12YWxvcn0kIHByb3BvcmNpb25hIHVtYSBtw6l0cmljYSBjb250w61udWEgZGUgJ3N1cnByZXNhJyBlbSByZWxhw6fDo28gw6AgaGlww7N0ZXNlIG51bGEsIHBlcm1pdGluZG8gdW1hIGFuw6FsaXNlIG1haXMgbWF0aXphZGEgZG8gcXVlIHVtIGNyaXTDqXJpbyBlc3RyaXRhbWVudGUgYmluw6FyaW8uIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDM0OCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSB0ZXN0ZSBiaWxhdGVyYWwgcGFyYSBhIG3DqWRpYSBkZSB1bWEgcG9wdWxhw6fDo28gY29tICRcXHNpZ21hJCBjb25oZWNpZG8sIG8gdmFsb3IgY2FsY3VsYWRvIGZvaSAkWl97XHRleHR7Y2FsY319ID0gLTIuMjQkLiBTYWJlbmRvIHF1ZSBvIG1vZGVsbyBzZWd1ZSB1bWEgbm9ybWFsIHBhZHLDo28gJE4oMCwgMSkkLCBjYWxjdWxlIG8gJHBcdGV4dHstdmFsb3J9JCBkbyB0ZXN0ZS4iLCAiZGljYSI6ICJQYXJhIHRlc3RlcyBiaWxhdGVyYWlzIGNvbSBkaXN0cmlidWnDp8OjbyBcXHNpbcOpdHJpY2EsICRwXHRleHR7LXZhbG9yfSA9IDIgXFx0aW1lcyBQKFogPCBaX3tcdGV4dHtjYWxjfX0pJCBzZSAkWl97XHRleHR7Y2FsY319IDwgMCQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIElkZW50aWZpY2FyIG8gdmFsb3IgZGEgZXN0YXTDrXN0aWNhIGNhbGN1bGFkYTogJFpfe1x0ZXh0e2NhbGN9fSA9IC0yLjI0JC4iLCAiMi4gQ29tbyBvIHRlc3RlIMOpIGJpbGF0ZXJhbCwgZGV2ZW1vcyBjb25zaWRlcmFyIGEgcHJvYmFiaWxpZGFkZSBuYXMgZHVhcyBjYXVkYXMuIiwgIjMuIENhbGN1bGFyIGEgcHJvYmFiaWxpZGFkZSBkYSBjYXVkYSBpbmZlcmlvcjogJFAoWiA8IC0yLjI0KSBcXGFwcHJveCAwLjAxMjUkLiIsICI0LiBDb21vIGEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIMOpIFxcc2ltw6l0cmljYSwgYSBwcm9iYWJpbGlkYWRlIGRhIGNhdWRhIHN1cGVyaW9yIMOpIGlndWFsOiAkUChaID4gMi4yNCkgPSAwLjAxMjUkLiIsICI1LiBPICRwXHRleHR7LXZhbG9yfSQgdG90YWwgw6kgYSBzb21hIGRhcyBkdWFzIGNhdWRhczogJHBcdGV4dHstdmFsb3J9ID0gMC4wMTI1ICsgMC4wMTI1ID0gMC4wMjUkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4wMjV9LCB7ImVudW5jaWFkbyI6ICJVbWEgZsOhYnJpY2EgZGUgcGFyYWZ1c29zIGFmaXJtYSBxdWUgYSByZXNpc3TDqm5jaWEgbcOpZGlhIGRlIHNldSBwcm9kdXRvIMOpICRcXG11ID0gMTU1JCBrZy4gVW0gbG90ZSBzdXNwZWl0byDDqSB0ZXN0YWRvLCBvbmRlIGEgaGlww7N0ZXNlIG51bGEgw6kgJEhfMDogXFxtdSA9IDE1NSQgZSBhIGFsdGVybmF0aXZhIMOpICRIXzE6IFxcbXUgPSAxNDUkIChjb20gJFxcc2lnbWEgPSAyMCQgZSAkbiA9IDI1JCkuIEEgcmVncmEgZGUgZGVjaXPDo28gYWRvdGFkYSDDqSByZWplaXRhciAkSF8wJCBzZSAkXFxiYXJ7WH0gXFxsZXEgMTUwJC4gQ2FsY3VsZSBhIHByb2JhYmlsaWRhZGUgZG8gZXJybyBkZSB0aXBvIEkgKCRcXGFscGhhJCkgZSBhIGRvIGVycm8gZGUgdGlwbyBJSSAoJFxcYmV0YSQpLiIsICJkaWNhIjogIlVzZSBvIFRMQyBwYXJhIGEgZGlzdHJpYnVpw6fDo28gZGUgJFxcYmFye1h9JC4gTGVtYnJlLXNlIHF1ZSAkXFxhbHBoYSA9IFAoXFxiYXJ7WH0gXFxpbiBSQyB8IEhfMCBcXHRleHR7IHZlcmRhZGVpcmF9KSQgZSAkXFxiZXRhID0gUChcXGJhcntYfSBcXG5vdGluIFJDIHwgSF8xIFxcdGV4dHsgdmVyZGFkZWlyYX0pJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiU29iICRIXzAkLCAkXFxiYXJ7WH0gXFxzaW0gTigxNTUsIDIwXjIvMjUpID0gTigxNTUsIDE2KSQuIExvZ28sICRcXGFscGhhID0gUChcXGJhcntYfSBcXGxlcSAxNTAgfCBcXG11ID0gMTU1KSA9IFAoWiBcXGxlcSAoMTUwIC0gMTU1KSAvIDQpID0gUChaIFxcbGVxIC0xLDI1KSA9IDAsMTA1NiQuIiwgIlNvYiAkSF8xJCwgJFxcYmFye1h9IFxcc2ltIE4oMTQ1LCAyMF4yLzI1KSA9IE4oMTQ1LCAxNikkLiBMb2dvLCAkXFxiZXRhID0gUChcXGJhcntYfSA+IDE1MCB8IFxcbXUgPSAxNDUpID0gUChaID4gKDE1MCAtIDE0NSkgLyA0KSA9IFAoWiA+IDEsMjUpID0gMSAtIDAsODk0NCA9IDAsMTA1NiQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQnVzc2FiICYgTW9yZXR0aW4sIEVzdGF0w61zdGljYSBCw6FzaWNhLCBDYXAgMTIsIHAuIDMzMiIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMTA1Nn0sIHsiZW51bmNpYWRvIjogIkVtIHVtIHRlc3RlIGRlIGhpcMOzdGVzZXMgY29tICRIXzA6IFx0aGV0YSA9IFx0aGV0YV8wJCBlICRIXzE6IFx0aGV0YSA+IFx0aGV0YV8wJCwgYSBmdW7Dp8OjbyBwb2RlciDDqSAkXFxwaShcXHRoZXRhKSA9IFAoXFx0ZXh0e1JlamVpdGFyIH0gSF8wIHwgXHRoZXRhKSQuIENvbnNpZGVyZSBvIGNhc28gb25kZSBvIHBvZGVyIHBhcmEgJFxcdGhldGFfMSQgw6kgJFxccGkoXFx0aGV0YV8xKSA9IDAsODAkLiBFeHBsaXF1ZSwgZG8gcG9udG8gZGUgdmlzdGEgaW5mZXJlbmNpYWwsIG8gcXVlIHNpZ25pZmljYSBlc3RlIHZhbG9yIGUgY29tbyBvIGF1bWVudG8gZG8gdGFtYW5obyBhbW9zdHJhbCAkbiQgYWZldGFyaWEgZXNzZSBwb2Rlci4iLCAiZGljYSI6ICJDb25zaWRlcmUgYSBzZW5zaWJpbGlkYWRlIGRvIHRlc3RlIGVtIGRldGVjdGFyIG8gZWZlaXRvLiBPIGF1bWVudG8gZGUgJG4kIHJlZHV6IGEgdmFyacOibmNpYSBkbyBlc3RpbWFkb3IgJFxcYmFye1h9JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiTyBwb2RlciAkXFxwaShcXHRoZXRhXzEpID0gMCw4MCQgc2lnbmlmaWNhIHF1ZSwgc2UgbyB2ZXJkYWRlaXJvIHZhbG9yIGRvIHBhcsOibWV0cm8gZm9yICRcXHRoZXRhXzEkLCBvIHRlc3RlIHRlbSA4MCUgZGUgY2hhbmNlIGRlIHJlamVpdGFyIGNvcnJldGFtZW50ZSBhIGhpcMOzdGVzZSBudWxhICRIXzAkLiIsICJJc3NvIGltcGxpY2EgdW1hIHRheGEgZGUgZXJybyBkZSB0aXBvIElJICgkXFxiZXRhJCkgZGUgMjAlIHBhcmEgZXNzZSB2YWxvciBlc3BlY8OtZmljbyBkbyBwYXLDom1ldHJvLiIsICJBdW1lbnRhciBvIHRhbWFuaG8gYW1vc3RyYWwgJG4kIGRpbWludWkgbyBlcnJvIHBhZHLDo28gZGEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlICgkRVAgPSBcXHNpZ21hIC8gXFxzcXJ0e259JCkuIiwgIkNvbW8gYSB2YXJpYWJpbGlkYWRlIGRhIGRpc3RyaWJ1acOnw6NvIGFtb3N0cmFsIGRpbWludWksIGFzIGRpc3RyaWJ1acOnw7VlcyBzb2IgJEhfMCQgZSBzb2IgJEhfMSQgdG9ybmFtLXNlIG1lbm9zIHNvYnJlcG9zdGFzLCBhdW1lbnRhbmRvIGEgcHJvYmFiaWxpZGFkZSBkZSByZWplaXRhciAkSF8wJCBxdWFuZG8gJEhfMSQgw6kgdmVyZGFkZWlyYSwgbG9nbywgYXVtZW50YW5kbyBvIHBvZGVyIGRvIHRlc3RlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtYSB2YXJpw6F2ZWwgJFgkIHNlZ3VlIGRpc3RyaWJ1acOnw6NvIG5vcm1hbCAkTihcXG11LCA0MDApJC4gUGFyYSB0ZXN0YXIgJEhfMDogXFxtdSA9IDIwMCQgY29udHJhICRIXzE6IFxcbXUgPiAyMDAkLCB1dGlsaXphLXNlIHVtYSBhbW9zdHJhIGRlICRuID0gMjUkIGl0ZW5zLiBGaXhhbmRvICRcXGFscGhhID0gMCwwNSQsIGRldGVybWluZSBhIHJlZ2nDo28gY3LDrXRpY2EgKCRSQyQpIGUgY2FsY3VsZSBvIHBvZGVyIGRvIHRlc3RlICgkXFxwaSQpIHBhcmEgJFxcbXUgPSAyMTAkLiIsICJkaWNhIjogIk8gdmFsb3IgY3LDrXRpY28gJFpfe2NyaXR9JCBwYXJhICRcXGFscGhhPTAsMDUkIHVuaWxhdGVyYWwgw6kgJDEsNjQ1JC4gTyBlcnJvIHBhZHLDo28gw6kgJDIwL1xcc3FydHsyNX0gPSA0JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiTyB2YWxvciBjcsOtdGljbyBkYSBtw6lkaWEgYW1vc3RyYWwgw6kgJFxcYmFye3h9X2MgPSBcXG11XzAgKyBaX3tjcml0fSBcXGNkb3QgKFxcc2lnbWEgLyBcXHNxcnR7bn0pID0gMjAwICsgMSw2NDUgXFxjZG90ICgyMCAvIDUpID0gMjAwICsgMSw2NDUgXFxjZG90IDQgPSAyMDYsNTgkLiBQb3J0YW50bywgJFJDID0gXFx7XFxiYXJ7WH0gPiAyMDYsNThcXH0kLiIsICJQYXJhIGNhbGN1bGFyIG8gcG9kZXIgJFxccGkoMjEwKSQsIGNhbGN1bGFtb3MgJFAoXFxiYXJ7WH0gPiAyMDYsNTggfCBcXG11ID0gMjEwKSQuIiwgIlRyYW5zZm9ybWFuZG8gcGFyYSBhIG5vcm1hbCBwYWRyw6NvOiAkWiA9ICgyMDYsNTggLSAyMTApIC8gNCA9IC0zLDQyIC8gNCA9IC0wLDg1NSQuIiwgIiRcXHBpKDIxMCkgPSBQKFogPiAtMCw4NTUpID0gMCw4MDM4JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCdXNzYWIgJiBNb3JldHRpbiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxMiwgcC4gMzQ1IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC44MDM4fV19').decode('utf-8'))


    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do progresso
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discursivas = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcqs) + len(discursivas)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v)
    
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    
    st.divider()
    
    # Seção de Questões de Múltipla Escolha
    if mcqs:
        st.header("📋 Questões de Múltipla Escolha")
        for i, questao in enumerate(mcqs):
            st.subheader(f"Questão {i + 1}")
            st.write(questao.get("enunciado", ""))
            
            # Exibir referência, se existir
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
                
            # Renderização de Gráfico Plotly
            code_plotly = questao.get("codigo_plotly")
            if code_plotly:
                try:
                    local_vars = {"go": go, "np": np, "stats": stats}
                    exec(code_plotly, globals(), local_vars)
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
            
            # Dica
            if st.button("💡 Dica", key=f"btn_dica_mcq_{i}"):
                st.info(questao.get("dica", "Dica indisponível"))
                
            # Verificação
            if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
                if escolha == questao.get("alternativa_correta"):
                    st.success("Correto! Muito bem.")
                    st.session_state.respostas_certas[f"mcq_{i}"] = True
                    st.rerun()
                else:
                    st.error("Resposta incorreta. Tente novamente!")
                    st.session_state.respostas_certas[f"mcq_{i}"] = False
            
            with st.expander("✅ Ver Gabarito Comentado"):
                st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
            st.divider()
    
    # Seção de Questões Discursivas
    if discursivas:
        st.header("✍️ Questões Discursivas")
        for i, questao in enumerate(discursivas):
            st.subheader(f"Desafio Discursivo {i + 1}")
            st.write(questao.get("enunciado", ""))
            
            ref = questao.get("referencia_livro")
            if ref:
                st.markdown(f"📖 *Referência: {ref}*")
                
            code_plotly = questao.get("codigo_plotly")
            if code_plotly:
                try:
                    local_vars = {"go": go, "np": np, "stats": stats}
                    exec(code_plotly, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"plotly_disc_{i}")
                except Exception as e:
                    st.warning("Gráfico indisponível no momento.")
            
            st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
            
            # Verificação Numérica ou Qualitativa
            esperado = questao.get("resposta_numerica_esperada")
            if esperado is not None:
                val_user = st.number_input("Digite o resultado numérico calculado para validação:", key=f"num_disc_{i}", format="%.4f")
                if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                    if abs(val_user - esperado) <= max(0.01, 0.01 * abs(esperado)):
                        st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                        st.rerun()
                    else:
                        st.error("O valor calculado difere do gabarito. Verifique suas fórmulas e tente novamente.")
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
            st.divider()
