import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4yOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogRXJyb3MgdGlwbyBJIGUgdGlwbyBJSSIsICJyZWZlcmVuY2lhc19iaWJsaW9ncmFmaWNhc19maW5haXMiOiBbIlBhcmHDrWJhLCBDLiBDLiBNLiAtIE1BVEQzOCBFc3RhdMOtc3RpY2EgQsOhc2ljYSBCIiwgIkJ1c3NhYiwgV2lsdG9uIE8uIGUgTW9yZXR0aW4sIFBlZHJvIEEuIC0gRXN0YXTDrXN0aWNhIELDoXNpY2EiXX0=').decode('utf-8'))

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
            background: linear-gradient(135deg, #78350F 0%, #3B82F6 100%);
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
            border-top: 3px solid #78350F !important;
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
            background: linear-gradient(90deg, #78350F 0%, #D97706 100%) !important;
            border-radius: 10px !important;
        }
        
        /* Inputs e Sliders na aula */
        div.stSlider [data-testid="stSliderTickBar"] {
            background-color: #78350F !important;
        }
        
        /* Botões na aula */
        div.stButton > button {
            background: linear-gradient(135deg, #78350F 0%, #3B82F6 100%) !important;
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
PRIMARY_BLUE = "#78350F"
SECONDARY_GREEN = "#D97706"
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
    
    # --- Cabeçalho e Introdução ---
    st.header(r"A Arquitetura da Decisão: Hipóteses e o Espaço de Erros")
    
    st.markdown(r"""
    A tomada de decisão baseada em dados, longe de ser um exercício trivial de cálculo aritmético, constitui o pilar central do método científico moderno, transformando a incerteza inerente à variabilidade amostral em uma estrutura de julgamento rigorosa e transparente. Quando nos deparamos com um problema de inferência, estamos, na verdade, tentando decidir entre dois caminhos excludentes sobre o comportamento de um parâmetro populacional desconhecido.
    """)
    
    st.info(r"A hipótese nula ($H_0$) atua como o conservadorismo científico, representando o estado de neutralidade ou o status quo, enquanto a hipótese alternativa ($H_1$) corporifica a novidade ou o efeito sob investigação.")
    
    st.markdown(r"""
    A arquitetura dessa decisão exige que estabeleçamos um campo de batalha lógico onde a verdade, embora oculta, seja delimitada por duas proposições mutuamente exclusivas. O objetivo do estatístico é definir uma Região de Rejeição ($RC$) para uma estatística de teste calculada a partir dos dados.
    """)
    
    # --- Formalismo ---
    st.latex(r"H_0: \theta = \theta_0 \quad \text{vs} \quad H_1: \theta \neq \theta_0")
    
    st.markdown(r"""
    Ao operarmos com amostras, estamos sujeitos a dois equívocos fundamentais. A escolha do nível de significância $\alpha$ e a análise do poder do teste ($1-\beta$) equilibram a sensibilidade do nosso experimento.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.latex(r"P(\text{Erro I}) = P(\text{Rejeitar } H_0 | H_0 \text{ verdadeira}) = \alpha")
    with col2:
        st.latex(r"P(\text{Erro II}) = P(\text{Não rejeitar } H_0 | H_1 \text{ verdadeira}) = \beta")
    
    # --- Simulador Interativo ---
    st.subheader(r"Simulador de Decisão: O Espaço de Erros")
    st.markdown(r"Explore como a variação no nível de significância $\alpha$ altera a Região de Rejeição ($RC$) em uma distribuição normal.")
    
    col_a, col_b = st.columns(2)
    alpha_val = col_a.slider(r"Nível de Significância ($\alpha$)", 0.01, 0.20, 0.05, step=0.01, key="alpha_sim_subtopico_1")
    n_val = col_b.slider(r"Tamanho Amostral ($n$)", 10, 100, 16, step=1, key="n_sim_subtopico_1")
    
    # Lógica do Gráfico
    x = np.linspace(-4, 4, 500)
    y = stats.norm.pdf(x, 0, 1)
    z_crit = stats.norm.ppf(1 - alpha_val/2)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Distribuição', line=dict(color='#1E293B')))
    # Regiões de Rejeição
    fig.add_vrect(x0=z_crit, x1=4, fillcolor="#991B1B", opacity=0.3, line_width=0)
    fig.add_vrect(x0=-4, x1=-z_crit, fillcolor="#991B1B", opacity=0.3, line_width=0)
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Região de Rejeição e Erro Tipo I</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    fig.update_xaxes(title=dict(text="Valor da Estatística de Teste", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True)
    fig.update_yaxes(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True)
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    st.info(f"Com $\\alpha = {alpha_val}$, as áreas sombreadas em vermelho representam a probabilidade de rejeitar $H_0$ incorretamente (Erro Tipo I).")
    
    # --- Exemplo Prático ---
    st.markdown(r"#### 📖 Exemplo Prático: Controle de Qualidade")
    
    with st.container(border=True):
        st.markdown(r"**Contexto:** Máquina de envase com peso médio nominal de 500g e variância conhecida de 400g². Teste: $H_0: \mu = 500$ contra $H_1: \mu \neq 500$ com $n=16$.")
        
        data_resumo = pd.DataFrame({
            "Parâmetro": ["Média H0", "Variância", "Amostras (n)", "Nível de Significância"],
            "Valor": [500, 400, 16, 0.05]
        })
        st.table(data_resumo)
        
        st.markdown(r"**Desenvolvimento:**")
        st.latex(r"\sigma_{\bar{X}} = \sqrt{\frac{400}{16}} = 5")
        st.markdown(r"Para um $\alpha=0.05$, o valor crítico $Z$ é 1,96. Os limites da Região de Rejeição são dados por $500 \pm 1,96 \times 5$.")
        
        st.success(r"**Laudo:** A máquina será considerada desregulada se a média amostral observada for inferior a 490,2g ou superior a 509,8g. Esta regra minimiza a probabilidade de paradas injustificadas.")

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    from scipy import stats
    
    # Título do Subtópico
    st.header(r"Funções de Poder e Característica de Operação (Função CO)")
    
    # Prosa Inicial
    st.markdown(r"""
    A análise profunda do desempenho de um teste exige a compreensão de como ele se comporta diante de diferentes valores possíveis do parâmetro populacional. 
    A **Função Característica de Operação (Função CO)**, denotada por $\beta(\mu)$, mapeia a probabilidade de aceitação da hipótese nula em função do valor verdadeiro do parâmetro.
    """)
    
    st.info(r"Complementarmente, a função poder, $\pi(\mu) = 1 - \beta(\mu)$, fornece a probabilidade de rejeição correta quando $H_0$ é falsa. Estas funções dependem criticamente do tamanho amostral $n$, do nível de significância $\alpha$ e da magnitude do desvio paramétrico.")
    
    # Formalismo
    st.subheader(r"Formalismo Matemático")
    st.latex(r"\beta(\mu) = P(\bar{X} \in RA | \mu)")
    st.latex(r"\pi(\mu) = 1 - \beta(\mu) = P(\bar{X} \in RC | \mu)")
    
    # Prosa Expandida (Fragmentada)
    st.markdown(r"### A Dinâmica do Teste")
    st.markdown(r"""
    A Função Característica de Operação funciona como um mapa da aceitação. Quando $\mu$ se afasta do valor hipotetizado em $H_0$, $\beta(\mu)$ representa a probabilidade de cometermos o erro do Tipo II, a **falha em detectar um desvio existente**.
    """)
    
    st.warning(r"Enquanto $\beta(\mu)$ revela a 'cegueira' do teste, a função poder $\pi(\mu)$ demonstra a sua 'agudeza'. Um teste com alto poder é aquele que, para desvios significativos, possui alta probabilidade de rejeitar $H_0$ corretamente.")
    
    # Dedução Analítica
    st.markdown(r"### Dedução Analítica")
    with st.container(border=True):
        st.latex(r"\pi(\mu) = P(\bar{X} \in RC | \mu)")
        st.latex(r"\pi(\mu) = P(\bar{X} < \bar{x}_{c1} | \mu) + P(\bar{X} > \bar{x}_{c2} | \mu)")
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"Z_1 = \frac{\bar{x}_{c1} - \mu}{\sigma_{\bar{X}}}")
        with col2:
            st.latex(r"Z_2 = \frac{\bar{x}_{c2} - \mu}{\sigma_{\bar{X}}}")
    
    # Exemplo Prático
    st.markdown(r"### 📖 Estudo de Caso: Máquina de Envase")
    with st.container(border=True):
        st.markdown(r"**Cenário**: Avaliação da capacidade de detecção ($n=16, \mu_0=500, \sigma^2=400, RC = \{ \bar{X} < 487,1 \cup \bar{X} > 512,9 \}$) para $\mu=505g$.")
        
        st.latex(r"\bar{X} \sim N(505, 25), \bar{x}_{c1} = 487,1, \bar{x}_{c2} = 512,9")
        
        col1, col2 = st.columns(2)
        col1.metric(r"Z_1", "-3,58")
        col2.metric(r"Z_2", "1,58")
        
        st.markdown(r"Cálculo: $\pi(505) = P(Z < -3,58) + P(Z > 1,58) \approx 0,00017 + 0,05705 = 0,05722$")
        
        st.success(r"**Laudo**: O poder de detecção é de apenas 5,72%. O teste é insensível para desvios de 5g. Recomenda-se aumentar $n$ para reduzir o Erro Tipo II (94,28%).")
    
    # Simulador Interativo
    st.markdown(r"### 📊 Simulador: Sensibilidade da Curva de Poder")
    col1, col2 = st.columns(2)
    mu_alt = col1.slider(r"Valor Real de \mu", 490, 520, 505, key=r"mu_sim_subtopico_2")
    n_val = col2.slider(r"Tamanho Amostral (n)", 10, 100, 16, key=r"n_sim_subtopico_2")
    
    # Lógica do Gráfico
    x = np.linspace(480, 520, 200)
    std_err = 20 / np.sqrt(n_val)
    y_dist = stats.norm.pdf(x, mu_alt, std_err)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y_dist, fill='tozeroy', fillcolor='rgba(120, 53, 15, 0.2)', line=dict(color='#78350F'), name=r"Distribuição da Amostra"))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição Amostral e Sensibilidade</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Valor da Média Amostral", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    st.info(f"Ao ajustar o tamanho amostral para {n_val}, o erro padrão reduz-se para {std_err:.2f}. Isso comprime a distribuição em torno de {mu_alt}, tornando o teste mais agudo para distinguir a média verdadeira do valor hipotetizado.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4yOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogRXJyb3MgdGlwbyBJIGUgdGlwbyBJSSIsICJxdWVzdG9lc19tdWx0aXBsYV9lc2NvbGhhIjogW3siZW51bmNpYWRvIjogIlVtYSBlbXByZXNhIGRlIHRlY25vbG9naWEgZXN0w6EgYXZhbGlhbmRvIGEgaW1wbGVtZW50YcOnw6NvIGRlIHVtIG5vdm8gYWxnb3JpdG1vIGRlIGNvbXByZXNzw6NvIGRlIGRhZG9zLiBPIHBhcsOibWV0cm8gZGUgaW50ZXJlc3NlICRcXG11JCDDqSBhIHRheGEgbcOpZGlhIGRlIGxhdMOqbmNpYSAoZW0gbWlsaXNzZWd1bmRvcykgZG9zIHNlcnZpZG9yZXMuIEF0dWFsbWVudGUsIGEgbGF0w6puY2lhIHNlZ3VlICROKDEwMCwgMjUpJC4gQSBnZXLDqm5jaWEgYWZpcm1hIHF1ZSBvIG5vdm8gYWxnb3JpdG1vIHJlZHV6aXLDoSBhIGxhdMOqbmNpYSBtw6lkaWEuIE8gZW5nZW5oZWlybyBkZWZpbmUgbyB0ZXN0ZSBjb21vICRIXzA6IFxcbXUgPSAxMDAkIHZzICRIXzE6IFxcbXUgPCAxMDAkLiBVbWEgYW1vc3RyYSBkZSAkbj0yNSQgc2Vydmlkb3JlcyDDqSBjb2xldGFkYS4gQSByZWdpw6NvIGRlIHJlamVpw6fDo28gKCRSQyQpIGZvaSBkZWZpbmlkYSBjb21vICRcXGJhcntYfSBcXGxlIDk4LDM1JC4gUXVhbCDDqSBhIHByb2JhYmlsaWRhZGUgZGUgY29tZXRlciB1bSBFcnJvIFRpcG8gSSAoJFxcYWxwaGEkKSBuZXN0ZSB0ZXN0ZT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjAsMDI1MCIsICJCIjogIjAsMDUwMCIsICJDIjogIjAsMDEwMCIsICJEIjogIjAsMTAwMCIsICJFIjogIjAsMDY2OCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBzb2IgJEhfMCQsICRcXGJhcntYfSBcXHNpbSBOKFxcbXVfMCwgXFxzaWdtYV4yL24pJC4gQ2FsY3VsZSBvIHZhbG9yICRaX3tcXHRleHR7Y2FsY319JCB0cmFuc2Zvcm1hbmRvIGEgYmFycmVpcmEgZGEgcmVnacOjbyBjcsOtdGljYS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlNvYiAkSF8wJCwgdGVtb3MgJFxcYmFye1h9IFxcc2ltIE4oMTAwLCA1XjIvMjUpID0gTigxMDAsIDEpJC4gQSBwcm9iYWJpbGlkYWRlIGRvIEVycm8gVGlwbyBJIMOpICRcXGFscGhhID0gUChcXGJhcntYfSBcXGxlIDk4LDM1IHwgXFxtdT0xMDApJC4gUGFkcm9uaXphbmRvOiAkWiA9IFxcZnJhY3s5OCwzNSAtIDEwMH17MX0gPSAtMSw2NSQuIENvbnN1bHRhbmRvIGEgdGFiZWxhIGRhIG5vcm1hbCBwYWRyw6NvLCAkUChaIFxcbGUgLTEsNjUpIFxcYXBwcm94IDAsMDUkLiBBbHRlcm5hdGl2YXMgaW5jb3JyZXRhczogQSAoY29uZnVuZGl1IGNvbSAkWj0tMSw5NiQpLCBDICh1c28gaW5jb3JyZXRvIGRlIG7DrXZlbCksIEQgKHVzbyBpbmNvcnJldG8gZGUgbsOtdmVsKSwgRSAoY8OhbGN1bG8gc2VtIGRpdmlzw6NvIHBlbG8gZXJybyBwYWRyw6NvKS4iLCAiY29kaWdvX3Bsb3RseSI6ICJpbXBvcnQgcGxvdGx5LmdyYXBoX29iamVjdHMgYXMgZ29cbmltcG9ydCBudW1weSBhcyBucFxueCA9IG5wLmxpbnNwYWNlKDk3LCAxMDMsIDIwMClcbnkgPSAoMSAvIG5wLlxcc3FydCgyICogbnAuXFxwaSkpICogbnAuXFxleHAoLTAuNSAqICh4IC0gMTAwKSoqMilcbmZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9J0Rpc3RyaWJ1acOnw6NvIHNvYiAkSF8wJCcsIGxpbmU9ZGljdChjb2xvcj0nIzc4MzUwRicsIHdpZHRoPTIpKSlcbmZpbGxfeCA9IG5wLmxpbnNwYWNlKDk3LCA5OC4zNSwgMTAwKVxuZmlsbF95ID0gKDEgLyBucC5cXHNxcnQoMiAqIG5wLlxccGkpKSAqIG5wLlxcZXhwKC0wLjUgKiAoZmlsbF94IC0gMTAwKSoqMilcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PW5wLmNvbmNhdGVuYXRlKFtmaWxsX3gsIFs5OC4zNSwgOTddXSksIHk9bnAuY29uY2F0ZW5hdGUoW2ZpbGxfeSwgWzAsIDBdXSksIGZpbGw9J3Rvc2VsZicsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG5hbWU9J1JDICgkXFxhbHBoYT0wLDA1JCknKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnLCB0aXRsZT0nUmVnacOjbyBkZSBSZWplacOnw6NvIGUgRXJybyBUaXBvIEknLCB4YXhpc190aXRsZT1yJ03DqWRpYSBBbW9zdHJhbCAoJFxiYXJ7WH0kKScsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnLCBzaG93bGVnZW5kPVRydWUpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAidTFxMjUzYW4zZzNkLCBwLiAzMzQifSwgeyJlbnVuY2lhZG8iOiAiTm8gY29udGV4dG8gZG8gdGVzdGUgZGUgaGlww7N0ZXNlcywgbyAnUG9kZXIgZG8gVGVzdGUnICgkMS1cXGJldGEkKSDDqSB1bWEgbWVkaWRhIGZ1bmRhbWVudGFsIGRlIGVmaWNpw6puY2lhLiBDb25zaWRlcmUgdW0gdGVzdGUgJEhfMDogXFxtdSA9IDUwJCBjb250cmEgJEhfMTogXFxtdSA+IDUwJC4gU2UgYSBwcm9iYWJpbGlkYWRlIGRlIGZhbGhhciBhbyByZWplaXRhciAkSF8wJCBxdWFuZG8gYSBtw6lkaWEgcmVhbCDDqSAkXFxtdSA9IDUyJCBmb3IgZGUgJDIwXFwlJCwgcXVhbCDDqSBhIGNvbmNsdXPDo28gY29ycmV0YSBzb2JyZSBvIHBvZGVyIGRvIHRlc3RlIHBhcmEgZXN0ZSBjZW7DoXJpbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gcG9kZXIgw6kgZGUgMjAlLCBpbmRpY2FuZG8gYWx0YSBzZW5zaWJpbGlkYWRlLiIsICJCIjogIk8gcG9kZXIgw6kgZGUgODAlLCBpbmRpY2FuZG8gYSBwcm9iYWJpbGlkYWRlIGRlIGRldGVjdGFyIG8gZWZlaXRvIHF1YW5kbyBlbGUgZXhpc3RlLiIsICJDIjogIk8gcG9kZXIgw6kgZGUgODAlLCBtYXMgbyBFcnJvIFRpcG8gSSDDqSBkZXNjb25oZWNpZG8uIiwgIkQiOiAiTyBwb2RlciDDqSBkZSAyMCUsIGluZGljYW5kbyBiYWl4YSBzZW5zaWJpbGlkYWRlIGFvIGVmZWl0by4iLCAiRSI6ICJPIHBvZGVyIMOpIGRlZmluaWRvIHBvciAkMSAtIFxcYWxwaGEkLCBsb2dvIMOpIDk1JS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIk8gUG9kZXIgZG8gVGVzdGUgw6kgYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIHF1YW5kbyAkSF8xJCDDqSB2ZXJkYWRlaXJhICgkMSAtIFxcYmV0YSQpLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBFcnJvIFRpcG8gSUkgw6kgJFxcYmV0YSA9IFAoXFx0ZXh0e27Do28gcmVqZWl0YXIgfSBIXzAgfCBIXzEgXHRleHR7IMOpIHZlcmRhZGVpcmF9KSQuIERhZG8gcXVlICRcXGJldGEgPSAwLDIwJCwgbyBwb2RlciDDqSAkMSAtIFxcYmV0YSA9IDEgLSAwLDIwID0gMCw4MCQuIElzc28gc2lnbmlmaWNhIHF1ZSBvIHRlc3RlIHRlbSAkODBcXCUkIGRlIHByb2JhYmlsaWRhZGUgZGUgZGV0ZWN0YXIgY29ycmV0YW1lbnRlIGEgbXVkYW7Dp2EgbmEgbcOpZGlhLiBBcyBvdXRyYXMgYWx0ZXJuYXRpdmFzIGVycmFtIG5hIGludGVycHJldGHDp8OjbyBkbyBjb21wbGVtZW50byBvdSBuYSBkZWZpbmnDp8OjbyBkb3MgY29uY2VpdG9zLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAidTFxMjUzYW4zZzNkLCBwLiAzNDYifSwgeyJlbnVuY2lhZG8iOiAiVW1hIGluZMO6c3RyaWEgZmFybWFjw6p1dGljYSBlc3TDoSB2YWxpZGFuZG8gdW0gbm92byBwcm9jZXNzbyBkZSBkb3NhZ2VtIGF1dG9tYXRpemFkYS4gTyBwcm9jZXNzbyDDqSBjb25zaWRlcmFkbyBzZWd1cm8gc2UgYSBkb3NhZ2VtIG3DqWRpYSAkXFxtdSQgZm9yIGV4YXRhbWVudGUgJDUwJCBtZy4gQSBoaXDDs3Rlc2UgbnVsYSDDqSAkSF8wOiBcXG11ID0gNTAkIGUgYSBoaXDDs3Rlc2UgYWx0ZXJuYXRpdmEgw6kgJEhfMTogXFxtdSBcXG5lcSA1MCQuIEEgZXF1aXBlIGRlIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBkZWZpbmUgdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhID0gMC4wNSQuIENvbnNpZGVyYW5kbyBvIGZvcm1hbGlzbW8gbWF0ZW3DoXRpY28gZG9zIGVycm9zLCBxdWFsIGRhcyBzZW50ZW7Dp2FzIGFiYWl4byBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgYSBwcm9iYWJpbGlkYWRlICRcXGJldGEkIG5lc3RlIGNlbsOhcmlvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJFxcYmV0YSA9IFAoXFx0ZXh0e1JlamVpdGFyIH0gSF8wIHwgXFxtdSA9IDUwKSQsIHJlcHJlc2VudGFuZG8gYSBwcm9iYWJpbGlkYWRlIGRlIHBhcmFyIGEgbGluaGEgZGUgcHJvZHXDp8OjbyBpbmRldmlkYW1lbnRlLiIsICJCIjogIiRcXGJldGEgPSBQKFxcdGV4dHtOw6NvIHJlamVpdGFyIH0gSF8wIHwgXFxtdSBcXG5lcSA1MCkkLCByZXByZXNlbnRhbmRvIGEgcHJvYmFiaWxpZGFkZSBkZSBsaWJlcmFyIHVtIGxvdGUgY29tIGRvc2FnZW0gZm9yYSBkYSBlc3BlY2lmaWNhw6fDo28uIiwgIkMiOiAiJFxcYmV0YSA9IDEgLSBcXGFscGhhJCwgc2VuZG8gbyBjb21wbGVtZW50byBkaXJldG8gZG8gcmlzY28gZGUgcHJpbWVpcmEgZXNww6ljaWUuIiwgIkQiOiAiJFxcYmV0YSA9IFAoXFxiYXJ7WH0gXFxpbiBSQyB8IFxcbXUgPSA1MCkkLCBvbmRlICRSQyQgw6kgYSByZWdpw6NvIGNyw610aWNhIGJhc2VhZGEgbm8gZXJybyBkZSBwcmltZWlyYSBlc3DDqWNpZS4iLCAiRSI6ICIkXFxiZXRhJCDDqSBhIHByb2JhYmlsaWRhZGUgZGUgZGV0ZWN0YXIgY29ycmV0YW1lbnRlIHVtIGRlc3ZpbyBuYSBtw6lkaWEsIGdhcmFudGluZG8gYSBlZmljw6FjaWEgZG8gZsOhcm1hY28uIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIG8gZXJybyBkZSBzZWd1bmRhIGVzcMOpY2llIG9jb3JyZSBxdWFuZG8gZmFsaGFtb3MgZW0gZGV0ZWN0YXIgdW1hIHJlYWxpZGFkZSBxdWUgZGl2ZXJnZSBkYSBoaXDDs3Rlc2UgbnVsYS4gTyBxdWUgYWNvbnRlY2UgY29tIG8gbG90ZSBzZSBuw6NvIHJlamVpdGFybW9zICRIXzAkLCBtYXMgJEhfMCQgZm9yIGZhbHNhPyIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiTyBlcnJvIGRlIHNlZ3VuZGEgZXNww6ljaWUgKCRcXGJldGEkKSDDqSBkZWZpbmlkbyBjb21vIGEgcHJvYmFiaWxpZGFkZSBkZSBuw6NvIHJlamVpdGFyICRIXzAkIHF1YW5kbyAkSF8xJCDDqSB2ZXJkYWRlaXJhICgkUChcXHRleHR7TsOjbyByZWplaXRhciB9IEhfMCB8IEhfMSkkKS4gTm8gY29udGV4dG8gaW5kdXN0cmlhbCwgaXNzbyBzaWduaWZpY2EgcXVlIGEgZW1wcmVzYSBhY2VpdGEgbyBsb3RlIChuw6NvIHJlamVpdGEgJEhfMCQpIG1lc21vIHF1YW5kbyBhIG3DqWRpYSBlc3TDoSBmb3JhIGRvIHBhZHLDo28gKCRcXG11IFxcbmVxIDUwJCksIG8gcXVlIGNvbmZpZ3VyYSB1bSBmYWxzbyBuZWdhdGl2byAoZmFsaGEgbmEgZGV0ZWPDp8OjbyBkbyBwcm9ibGVtYSkuIEEgYWx0ZXJuYXRpdmEgQSBkZWZpbmUgJFxcYWxwaGEkIChFcnJvIEkpLCBhIEMgY29uZnVuZGUgb3MgY29uY2VpdG9zIGRlIGNvbXBsZW1lbnRvIGRlIHByb2JhYmlsaWRhZGUgKG8gY29tcGxlbWVudG8gZGUgJDEtXFxhbHBoYSQgw6kgbyBQb2RlciBkbyBUZXN0ZSwgJDEtXFxiZXRhJCksIGUgYSBEIGRlc2NyZXZlIG8gY8OhbGN1bG8gZG8gZXJybyBkZSBwcmltZWlyYSBlc3DDqWNpZS4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDQ4LCA1MiwgMjAwKVxueV9oMCA9IHN0YXRzLm5vcm0ucGRmKHgsIDUwLCAwLjUpXG55X2gxID0gc3RhdHMubm9ybS5wZGYoeCwgNTAuOCwgMC41KVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15X2gwLCBuYW1lPXJcIiRIXzA6IFxcbXU9NTAkXCIsIGxpbmU9ZGljdChjb2xvcj1cIiM3ODM1MEZcIiwgd2lkdGg9MikpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15X2gxLCBuYW1lPXJcIiRIXzE6IFxcbXU9NTAuOCRcIiwgbGluZT1kaWN0KGNvbG9yPVwiIzk5MUIxQlwiLCB3aWR0aD0yKSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT1cIkRpc3RyaWJ1acOnw7VlcyBzb2IgJEhfMCQgZSAkSF8xJCBwYXJhIHZpc3VhbGl6YcOnw6NvIGRvIGVycm9cIiwgeGF4aXNfdGl0bGU9XCJNw6lkaWEgQW1vc3RyYWwgKCRcXGJhcntYfSQpXCIsIHlheGlzX3RpdGxlPVwiRGVuc2lkYWRlXCIpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gdGVzdGUgZGUgaGlww7N0ZXNlcyBiaWNhdWRhbCBjb20gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCwgcXVhbCDDqSBvIGVmZWl0byBwcsOhdGljbyBkbyBhdW1lbnRvIGRvIHRhbWFuaG8gYW1vc3RyYWwgJG4kIHNvYnJlIG9zIGVycm9zIGRlIGRlY2lzw6NvLCBhc3N1bWluZG8gcXVlIGEgcmVnacOjbyBjcsOtdGljYSAkUkMkIHNlamEgYWp1c3RhZGEgcGFyYSBtYW50ZXIgJFxcYWxwaGEkIGNvbnN0YW50ZT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gdmFsb3IgZGUgJFxcYmV0YSQgYXVtZW50YSwgcG9pcyBhIHZhcmnDom5jaWEgZGEgbcOpZGlhIGFtb3N0cmFsIHRvcm5hLXNlIG1haXMgaW5zdMOhdmVsLiIsICJCIjogIk8gdmFsb3IgZGUgJFxcYmV0YSQgZGltaW51aSwgcG9pcyBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgJEVQKFxcYmFye1h9KSA9IFxcc2lnbWEvXFxzcXJ0e259JCByZWR1eiwgYXVtZW50YW5kbyBvIHBvZGVyIGRvIHRlc3RlLiIsICJDIjogIk9zIHZhbG9yZXMgZGUgJFxcYWxwaGEkIGUgJFxcYmV0YSQgZGltaW51ZW0gc2ltdWx0YW5lYW1lbnRlLCB0b3JuYW5kbyBvIHRlc3RlIG1haXMgY29uc2VydmFkb3IuIiwgIkQiOiAiTyB2YWxvciBkZSAkXFxhbHBoYSQgYXVtZW50YSwgZXhpZ2luZG8gdW1hIGNvcnJlw6fDo28gdmlhIEJvbmZlcnJvbmkgcGFyYSBtYW50ZXIgYSB2YWxpZGFkZSBlc3RhdMOtc3RpY2EuIiwgIkUiOiAiTsOjbyBow6EgaW1wYWN0byBlbSAkXFxiZXRhJCwgcG9pcyBlc3RlIGRlcGVuZGUgZXhjbHVzaXZhbWVudGUgZGEgdmFyacOibmNpYSBwb3B1bGFjaW9uYWwgJFxcc2lnbWFeMiQuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJQZW5zZSBuYSBkaXNwZXJzw6NvIGRhIGRpc3RyaWJ1acOnw6NvIGFtb3N0cmFsIGRhIG3DqWRpYSBxdWFuZG8gJG4kIGNyZXNjZS4gQ29tbyBhIHNvYnJlcG9zacOnw6NvIGRhcyBjdXJ2YXMgZGUgJEhfMCQgZSAkSF8xJCBtdWRhPyIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQXVtZW50YXIgJG4kIHJlZHV6IG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSAoJEVQKFxcYmFye1h9KSA9IFxcc2lnbWEvXFxzcXJ0e259JCksIG8gcXVlIGVzdHJlaXRhIGFzIGRpc3RyaWJ1acOnw7VlcyBhbW9zdHJhaXMgdGFudG8gc29iICRIXzAkIHF1YW50byBzb2IgJEhfMSQuIENvbW8gcmVzdWx0YWRvLCBhIHJlZ2nDo28gZGUgc29icmVwb3Npw6fDo28gKG9uZGUgb2NvcnJlIG8gZXJybyAkXFxiZXRhJCkgZGltaW51aSwgYXVtZW50YW5kbyBhIGNhcGFjaWRhZGUgZG8gdGVzdGUgZGUgZGlzdGluZ3VpciBlbnRyZSBhIGhpcMOzdGVzZSBudWxhIGUgYSBhbHRlcm5hdGl2YSwgcmVkdXppbmRvIGEgcHJvYmFiaWxpZGFkZSBkZSBlcnJvIGRlIHNlZ3VuZGEgZXNww6ljaWUgKGF1bWVudGFuZG8gbyBQb2RlciAkMS1cXGJldGEkKS4gQSBhbHRlcm5hdGl2YSBBIGVzdMOhIGluY29ycmV0YSBwb2lzIGEgbcOpZGlhIHRvcm5hLXNlIG1haXMgZXN0w6F2ZWw7IGEgRCBlc3TDoSBlcnJhZGEgcG9pcyAkXFxhbHBoYSQgw6kgZml4YWRvIHBlbG8gcGVzcXVpc2Fkb3I7IGEgRSBlc3TDoSBlcnJhZGEgcG9pcyAkXFxiZXRhJCBkZXBlbmRlIGRpcmV0YW1lbnRlIGRvIHRhbWFuaG8gZGEgYW1vc3RyYS4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIlVtYSBpbmTDunN0cmlhIGRlIHNlbWljb25kdXRvcmVzIG1vbml0b3JhIGEgcmVzaXN0w6puY2lhIG3DqWRpYSBkZSBzZXVzIGNvbXBvbmVudGVzLCBxdWUgc2VndWVtIHVtYSBkaXN0cmlidWnDp8OjbyBOb3JtYWwgY29tICRcXHNpZ21hID0gMi4wIFxcT21lZ2EkLiBPIHByb2Nlc3NvIMOpIGNvbnNpZGVyYWRvIGVtIGNvbnRyb2xlIHNlIGEgbcOpZGlhIGZvciAkXFxtdV8wID0gNTAgXFxPbWVnYSQuIEEgZ2Vyw6puY2lhIGVzdGFiZWxlY2UgdW0gdGVzdGUgZGUgaGlww7N0ZXNlcyBjb20gJG49MjUkLCBvbmRlICRIXzA6IFxcbXUgPSA1MCQgY29udHJhICRIXzE6IFxcbXUgPiA1MCQsIGNvbSB1bSBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgJFxcYWxwaGEgPSAwLjA1JC4gQ29uc2lkZXJhbmRvIGEgRnVuw6fDo28gQ2FyYWN0ZXLDrXN0aWNhIGRlIE9wZXJhw6fDo28gKEZ1bsOnw6NvIENPKSwgcXVhbCBzZXJpYSBvIGltcGFjdG8gbmEgcHJvYmFiaWxpZGFkZSBkZSBuw6NvIHJlamVpdGFyICRIXzAkIHNlIG8gcHJvY2Vzc28gc29mcmVzc2UgdW0gZGVzdmlvIHJlYWwgcGFyYSAkXFxtdV8xID0gNTEgXFxPbWVnYSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIHByb2JhYmlsaWRhZGUgZGUgbsOjbyByZWplaXRhciAkSF8wJCBhdW1lbnRhLCBwb2lzIG8gbm92byAkXFxtdV8xJCBlc3TDoSBtYWlzIGRpc3RhbnRlIGRhIGhpcMOzdGVzZSBudWxhLiIsICJCIjogIkEgcHJvYmFiaWxpZGFkZSBkZSBuw6NvIHJlamVpdGFyICRIXzAkIGRpbWludWksIHBvaXMgYSByZWdpw6NvIGNyw610aWNhIMOpIGRlZmluaWRhIHBhcmEgdmFsb3JlcyBtYWlvcmVzIHF1ZSAkNTAkIGUgbyBkZXN2aW8gcGFyYSAkNTEkIGF1bWVudGEgYSBwcm9iYWJpbGlkYWRlIGRlIGNhaXIgbmEgcmVnacOjbyBkZSByZWplacOnw6NvLiIsICJDIjogIkEgcHJvYmFiaWxpZGFkZSBkZSBuw6NvIHJlamVpdGFyICRIXzAkIHBlcm1hbmVjZSBpbmFsdGVyYWRhLCB1bWEgdmV6IHF1ZSBhIEZ1bsOnw6NvIENPIGRlcGVuZGUgZXhjbHVzaXZhbWVudGUgZG8gdmFsb3IgZGUgJFxcYWxwaGEkIGUgbsOjbyBkYSBtw6lkaWEgcG9wdWxhY2lvbmFsLiIsICJEIjogIkEgcHJvYmFiaWxpZGFkZSBkZSBuw6NvIHJlamVpdGFyICRIXzAkIHRvcm5hLXNlIGlndWFsIGEgJDAuOTUkLCBwb2lzIGVzdGUgw6kgbyB2YWxvciBkZWZpbmlkbyBwZWxvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYS4iLCAiRSI6ICJBIHByb2JhYmlsaWRhZGUgZGUgbsOjbyByZWplaXRhciAkSF8wJCBkb2JyYSwgdmlzdG8gcXVlIGEgbcOpZGlhIGF1bWVudG91IGVtIHVtYSB1bmlkYWRlIGRlIGRlc3ZpbyBwYWRyw6NvLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBhIEZ1bsOnw6NvIENPLCAkXFxiZXRhKFxcbXUpJCwgZGVzY3JldmUgYSBwcm9iYWJpbGlkYWRlIGRlIGFjZWl0YXIgJEhfMCQgZGFkbyB1bSB2YWxvciByZWFsIGRvIHBhcsOibWV0cm8uIFNlIG8gcGFyw6JtZXRybyBzZSBhZmFzdGEgZGEgbcOpZGlhIG51bGEgbmEgZGlyZcOnw6NvIGRhIGhpcMOzdGVzZSBhbHRlcm5hdGl2YSwgYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIChQb2RlcikgZGV2ZSBhdW1lbnRhci4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgRnVuw6fDo28gQ08sICRcXGJldGEoXFxtdSkgPSBQKFxcYmFye1h9IDwgYyB8IFxcbXUpJCwgb25kZSAkYyQgw6kgbyB2YWxvciBjcsOtdGljby4gUGFyYSAkSF8wOiBcXG11PTUwJCBlICRIXzE6IFxcbXU+NTAkLCBhIHJlZ2nDo28gZGUgcmVqZWnDp8OjbyDDqSAkXFxiYXJ7WH0gPiBjJC4gQ29tbyAkXFxtdV8xID0gNTEgPiA1MCQsIGEgZGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgZGVzbG9jYS1zZSBwYXJhIGEgZGlyZWl0YSwgYXVtZW50YW5kbyBhIMOhcmVhIHNvYiBhIGNhdWRhIHN1cGVyaW9yIChyZWdpw6NvIGNyw610aWNhKS4gQ29uc2VxdWVudGVtZW50ZSwgYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIGF1bWVudGEgZSwgcG9yIGNvbXBsZW1lbnRvLCBhIHByb2JhYmlsaWRhZGUgZGUgYWNlaXRhciAkSF8wJCAoJFxcYmV0YShcXG11XzEpJCkgZGltaW51aS4gQSBhbHRlcm5hdGl2YSBBIGVycmEgYW8gYWZpcm1hciBhdW1lbnRvOyBDIGlnbm9yYSBhIGRlcGVuZMOqbmNpYSBkYSBtw6lkaWEgbmEgRnVuw6fDo28gQ087IEQgY29uZnVuZGUgJFxcYmV0YSQgY29tICQxLVxcYWxwaGEkOyBFIMOpIHVtYSBzdXBvc2nDp8OjbyBhcml0bcOpdGljYSBzZW0gYmFzZSBlc3RhdMOtc3RpY2EuIiwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKCk7IHggPSBucC5saW5zcGFjZSg0OCwgNTMsIDIwMCk7IFxcbXUwID0gNTA7IFxcbXUxID0gNTE7IFxcc2lnbWFfeCA9IDIuMCAvIG5wLlxcc3FydCgyNSk7IHpfY3JpdCA9IDEuNjQ1OyBjID0gXFxtdTAgKyB6X2NyaXQgKiBcXHNpZ21hX3g7IFxcYmV0YSA9IHN0YXRzLm5vcm0uY2RmKGMsIGxvYz14LCBzY2FsZT1cXHNpZ21hX3gpOyBcXHBpID0gMSAtIFxcYmV0YTsgZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT1cXGJldGEsIG5hbWU9cidGdW7Dp8OjbyBDTyAoJFxiXFxldGEoXFxtdSkkKScsIGxpbmU9ZGljdChjb2xvcj0nIzc4MzUwRicsIHdpZHRoPTMpKSk7IGZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9XFxwaSwgbmFtZT1yJ0Z1bsOnw6NvIFBvZGVyICgkXFxwaShcXG11KSQpJywgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJywgd2lkdGg9MykpKTsgZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0N1cnZhcyBkZSBQb2RlciBlIENPJywgeGF4aXNfdGl0bGU9cidNw6lkaWEgUmVhbCAoJFxcbXUkKScsIHlheGlzX3RpdGxlPSdQcm9iYWJpbGlkYWRlJyk7IGZpZy51cGRhdGVfbGF5b3V0KHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnLCBtYXJnaW49ZGljdChsPTIwLCByPTIwLCB0PTUwLCBiPTIwKSkiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJBbyBwbGFuZWphciB1bSB0ZXN0ZSBkZSBoaXDDs3Rlc2VzLCBvIHBlc3F1aXNhZG9yIGRlc2VqYSBhdW1lbnRhciBvIHBvZGVyIGRvIHRlc3RlICgkMS1cXGJldGEkKSBwYXJhIGRldGVjdGFyIHVtIGRlc3ZpbyBlc3BlY8OtZmljbyBubyBwYXLDom1ldHJvIHBvcHVsYWNpb25hbC4gQXNzdW1pbmRvIHF1ZSBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgc2VqYSBtYW50aWRvIGNvbnN0YW50ZSwgcXVhbCDDqSBhIMO6bmljYSBhw6fDo28gbWF0ZW1hdGljYW1lbnRlIGNvcnJldGEgcGFyYSBhdGluZ2lyIGVzdGUgb2JqZXRpdm8/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJSZWR1emlyIG8gdGFtYW5obyBkYSBhbW9zdHJhICRuJC4iLCAiQiI6ICJBdW1lbnRhciBvIHRhbWFuaG8gZGEgYW1vc3RyYSAkbiQuIiwgIkMiOiAiU3Vic3RpdHVpciBhIGRpc3RyaWJ1acOnw6NvIE5vcm1hbCBwZWxhIERpc3RyaWJ1acOnw6NvIHQgZGUgU3R1ZGVudCwgaW5kZXBlbmRlbnRlbWVudGUgZG8gdGFtYW5obyBhbW9zdHJhbC4iLCAiRCI6ICJEaW1pbnVpciBhIHZhcmnDom5jaWEgcG9wdWxhY2lvbmFsICRcXHNpZ21hXjIkIHBvciBtZWlvIGRlIHVtYSBub3ZhIG1lZGnDp8Ojbywgc2VtIGFsdGVyYXIgbyBkZXNlbmhvIGV4cGVyaW1lbnRhbC4iLCAiRSI6ICJUb3JuYXIgYSBoaXDDs3Rlc2UgbnVsYSAkSF8wJCBtYWlzIGNvbXBsZXhhIGFkaWNpb25hbmRvIG3Dumx0aXBsb3MgcGFyw6JtZXRyb3MuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJBbmFsaXNlIGEgZsOzcm11bGEgZG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSwgJEVQKFxcYmFye1h9KSA9IFxcc2lnbWEgLyBcXHNxcnR7bn0kLiBDb21vIG8gcG9kZXIgZXN0w6EgbGlnYWRvIMOgIHNlcGFyYcOnw6NvIGVudHJlIGFzIGRpc3RyaWJ1acOnw7VlcyBzb2IgJEhfMCQgZSAkSF8xJCwgbyBxdWUgYWNvbnRlY2UgY29tIGEgc29icmVwb3Npw6fDo28gZGFzIGN1cnZhcyBxdWFuZG8gJG4kIGF1bWVudGE/IiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJPIHBvZGVyIGRvIHRlc3RlLCAkMS1cXGJldGEoXFxtdSkkLCDDqSBhIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgJEhfMCQgcXVhbmRvIGVsYSDDqSBmYWxzYS4gQXVtZW50YXIgbyB0YW1hbmhvIGFtb3N0cmFsICRuJCByZWR1eiBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEsIHRvcm5hbmRvIGEgZGlzdHJpYnVpw6fDo28gYW1vc3RyYWwgZGUgJFxcYmFye1h9JCBtYWlzIGNvbmNlbnRyYWRhLiBJc3NvIHJlZHV6IGEgc29icmVwb3Npw6fDo28gZW50cmUgYXMgZGlzdHJpYnVpw6fDtWVzIHNvYiAkSF8wJCBlICRIXzEkLCBwZXJtaXRpbmRvIHF1ZSBvIHRlc3RlIGRldGVjdGUgZGVzdmlvcyBtZW5vcmVzIGNvbSBtYWlvciBwcm9iYWJpbGlkYWRlLiBBIGFsdGVybmF0aXZhIEEgcmVkdXppcmlhIG8gcG9kZXI7IEMgw6kgdGVjbmljYW1lbnRlIGluY29ycmV0byBwYXJhIGdhbmhvIGRlIHBvZGVyOyBEIGRlcGVuZGUgZGUgZmF0b3JlcyBmw61zaWNvcyBleHRlcm5vcyBhbyBwbGFuZWphbWVudG8gZXN0YXTDrXN0aWNvOyBFIMOpIHVtIGVycm8gZGUgZm9ybXVsYcOnw6NvIGRlIGhpcMOzdGVzZXMuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJVbSBlbmdlbmhlaXJvIGRlIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBtb25pdG9yYSBvIGRpw6JtZXRybyBkZSBwZcOnYXMgZGUgcHJlY2lzw6NvIGVtIHVtYSBsaW5oYSBkZSBtb250YWdlbSBhdXRvbWF0aXphZGEuIE8gcHJvY2Vzc28gZXN0w6Egb3BlcmFuZG8gY29ycmV0YW1lbnRlIHF1YW5kbyBvIGRpw6JtZXRybyBtw6lkaW8gw6kgZGUgJDIwLDAwJCBtbS4gVW1hIG11ZGFuw6dhIG5vIGFqdXN0ZSBkYSBtw6FxdWluYSBwb2RlIGNhdXNhciB0YW50byBvIGF1bWVudG8gcXVhbnRvIGEgZGltaW51acOnw6NvIGRlc3NlIGRpw6JtZXRybywgbyBxdWUgY29tcHJvbWV0ZSBhIG1vbnRhZ2VtLiBPIGVuZ2VuaGVpcm8gY29sZXRhIHVtYSBhbW9zdHJhIGRlICRuPTEwMCQgcGXDp2FzIGUgZGVzZWphIHJlYWxpemFyIHVtIHRlc3RlIGRlIGhpcMOzdGVzZXMgcGFyYSB2ZXJpZmljYXIgc2UgYSBtw6FxdWluYSBuZWNlc3NpdGEgZGUgcmVjYWxpYnJhZ2VtICgkSF8wOiBcXG11ID0gMjAsMDAkIGNvbnRyYSAkSF8xOiBcXG11IFxcbmVxIDIwLDAwJCkuIFNlIG8gZW5nZW5oZWlybyBvcHRhciBwb3IgdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhID0gMCwwNSQgZSBkZWNpZGlyIHJlYWxpemFyIHVtIHRlc3RlIFVOSUxBVEVSQUwgw6AgZGlyZWl0YSBwb3IgZXJybyBkZSBwcm9jZWRpbWVudG8sIHF1YWwgw6kgYSBwcmluY2lwYWwgY29uc2VxdcOqbmNpYSBlc3RhdMOtc3RpY2EgZSBwcsOhdGljYSBkZXNzYSBlc2NvbGhhIGVycsO0bmVhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyBwb2RlciBkbyB0ZXN0ZSAoJDEtXFxiZXRhJCkgYXVtZW50YSwgcG9pcyBhIHJlZ2nDo28gY3LDrXRpY2EgZXN0w6EgdG90YWxtZW50ZSBjb25jZW50cmFkYSBlbSB1bWEgY2F1ZGEsIHRvcm5hbmRvIG1haXMgZsOhY2lsIHJlamVpdGFyICRIXzAkLiIsICJCIjogIkEgcHJvYmFiaWxpZGFkZSBkZSBjb21ldGVyIG8gRXJybyBUaXBvIEkgYXVtZW50YSBzaWduaWZpY2F0aXZhbWVudGUsIHBvaXMgbyB0ZXN0ZSBwYXNzYSBhIGlnbm9yYXIgdmFyaWHDp8O1ZXMgbmVnYXRpdmFzLCBtYW50ZW5kbyBvICRcXGFscGhhJCB0b3RhbCBhcGVuYXMgZG8gbGFkbyBkaXJlaXRvLiIsICJDIjogIk8gdGVzdGUgdG9ybmEtc2UgaW5jYXBheiBkZSBkZXRlY3RhciBkZXN2aW9zIGRhIG3DqWRpYSBwYXJhIHZhbG9yZXMgaW5mZXJpb3JlcyBhICQyMCwwMCQgbW0sIGZhbGhhbmRvIGVtIGlkZW50aWZpY2FyIGZhbGhhcyBkZSBzdWJkaW1lbnNpb25hbWVudG8gZGEgcGXDp2EuIiwgIkQiOiAiTyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhIMOpIHN1YmVzdGltYWRvLCBsZXZhbmRvIGEgdW1hIGNvbmNsdXPDo28gZXF1aXZvY2FkYSBzb2JyZSBhIHByZWNpc8OjbyBkbyBwcm9jZXNzbyBpbmR1c3RyaWFsLiIsICJFIjogIkEgcHJvYmFiaWxpZGFkZSBkZSBFcnJvIFRpcG8gSUkgKCRcXGJldGEkKSBkaW1pbnVpLCB1bWEgdmV6IHF1ZSBhIHJlZ2nDo28gZGUgcmVqZWnDp8OjbyBtYWlzIGFtcGxhIGZhY2lsaXRhIGEgYWNlaXRhw6fDo28gZGEgaGlww7N0ZXNlIGFsdGVybmF0aXZhLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiUmVmbGl0YSBzb2JyZSBhIGdlb21ldHJpYSBkYSBSZWdpw6NvIENyw610aWNhICgkUkMkKTogZW0gdW0gdGVzdGUgYmlsYXRlcmFsLCBvICRcXGFscGhhJCDDqSByZXBhcnRpZG8uIEVtIHVtIHVuaWxhdGVyYWwsIGVsZSDDqSBjb25jZW50cmFkby4gU2UgbyBwcm9ibGVtYSBleGlnZSBkZXRlY8Onw6NvIGRlIGRlc3ZpbyBlbSBxdWFscXVlciBkaXJlw6fDo28sIG8gcXVlIGFjb250ZWNlIGNvbSBhIGNhcGFjaWRhZGUgZGUgZGV0ZWPDp8OjbyBubyBsYWRvIG9wb3N0byBhbyBkYSBjYXVkYSBlc2NvbGhpZGE/IiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGVzY29saGEgY29ycmV0YSDDqSBhIEMuIEVtIHVtIHRlc3RlIGJpbGF0ZXJhbCAoJEhfMTogXFxtdSBcXG5lcSAyMCwwMCQpLCBhIHJlZ2nDo28gY3LDrXRpY2EgJFJDJCBkZXZlIGNvYnJpciBhbWJhcyBhcyBjYXVkYXMgKCRcXGFscGhhLzIkIGVtIGNhZGEpLiBBbyB1dGlsaXphciB1bSB0ZXN0ZSB1bmlsYXRlcmFsLCBvIGVuZ2VuaGVpcm8gY29uY2VudHJhIHRvZG8gbyAkXFxhbHBoYSQgZW0gYXBlbmFzIHVtYSBjYXVkYSAoZXg6IHN1cGVyaW9yKS4gQ29uc2VxdWVudGVtZW50ZSwgcGFyYSBxdWFscXVlciB2YWxvciBhbW9zdHJhbCAkXFxiYXJ7WH0gPCAyMCwwMCQsIG8gdGVzdGUgdW5pbGF0ZXJhbCBudW5jYSByZWplaXRhcsOhICRIXzAkLCBtZXNtbyBxdWUgYSBtw6lkaWEgcmVhbCBzZWphIHNpZ25pZmljYXRpdmFtZW50ZSBpbmZlcmlvciBhICQyMCwwMCQgbW0uIEEgYWx0ZXJuYXRpdmEgQSBlc3TDoSBpbmNvcnJldGEgcG9pcyBvIHBvZGVyIGRvIHRlc3RlIGRlcGVuZGUgZG8gdmFsb3IgcmVhbCBkZSAkXFxtdSQgZSBkYSBkaXJlw6fDo28gZG8gZGVzdmlvOyBhIEIgZXN0w6EgaW5jb3JyZXRhIHBvaXMgbyAkXFxhbHBoYSQgZm9pIGZpeGFkby4gQSBhbHRlcm5hdGl2YSBEIGUgRSByZWZlcmVtLXNlIGEgaW50ZXJwcmV0YcOnw7VlcyBlcXVpdm9jYWRhcyBkZSBlcnJvIHBhZHLDo28gZSBwb2Rlci4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAxMDAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgsIDAsIDEpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9J0Rpc3RyaWJ1acOnw6NvIE4oMCwxKScsIGxpbmU9ZGljdChjb2xvcj0nIzc4MzUwRicsIHdpZHRoPTIpKSlcbiMgw4FyZWEgZGUgcmVqZWnDp8OjbyB1bmlsYXRlcmFsIChhcGVuYXMgZGlyZWl0YSlcbnJjX3ggPSBucC5saW5zcGFjZSgxLjY0NSwgNCwgMTAwKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9cmNfeCwgeT1zdGF0cy5ub3JtLnBkZihyY194LCAwLCAxKSwgZmlsbD0ndG96ZXJveScsIG5hbWU9J1JDIFVuaWxhdGVyYWwnLCBmaWxsY29sb3I9JyM5OTFCMUInLCBvcGFjaXR5PTAuNSkpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nPGI+RGlzdHJpYnVpw6fDo28gTm9ybWFsOiBUZXN0ZSBVbmlsYXRlcmFsIHZzIEJpbGF0ZXJhbDwvYj4nLCB4YXhpcz1kaWN0KHRpdGxlPXInRXN0YXTDrXN0aWNhICRaX3tcdGV4dHtjYWxjfX0kJyksIHlheGlzPWRpY3QodGl0bGU9J0RlbnNpZGFkZScpKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtYSBwZXNxdWlzYSBkZSBtZXJjYWRvLCBkZXNlamEtc2UgdGVzdGFyIHNlIGEgbm92YSBlc3RyYXTDqWdpYSBkZSBwcmVjaWZpY2HDp8OjbyBkZSB1bSBwcm9kdXRvIGF1bWVudG91IG8gdGlja2V0IG3DqWRpbyBkZSBjb21wcmEsIHF1ZSBhbnRlcyBlcmEgZGUgUiQgMTUwLDAwLiBBcyBoaXDDs3Rlc2VzIHPDo28gJEhfMDogXFxtdSA9IDE1MCQgZSAkSF8xOiBcXG11ID4gMTUwJC4gQSBkZWNpc8OjbyBlc3RhdMOtc3RpY2Egw6kgdG9tYWRhIGNvbSBiYXNlIGVtIHVtYSBhbW9zdHJhIGRlIHRhbWFuaG8gJG49NjQkIGNvbSBkZXN2aW8gcGFkcsOjbyBjb25oZWNpZG8gJFxcc2lnbWE9MjAkLiBTZSBvIHBlc3F1aXNhZG9yIGZpeGFyICRcXGFscGhhID0gMCwwMSQgcGFyYSBtaW5pbWl6YXIgbyBFcnJvIFRpcG8gSSwgbWFzIG8gZWZlaXRvIHJlYWwgZG8gYXVtZW50byBkZSBwcmXDp28gZm9yIG11aXRvIHBlcXVlbm8sIHF1YWwgZmVuw7RtZW5vIMOpIG9ic2VydmFkbyBuYSBkaW7Dom1pY2EgZW50cmUgJFxcYWxwaGEkIGUgJFxcYmV0YSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJBIHJlZHXDp8OjbyBkZSAkXFxhbHBoYSQgcGFyYSAkMCwwMSQgY2F1c2EgdW0gYXVtZW50byBkaXJldG8gbmEgcHJvYmFiaWxpZGFkZSAkXFxiZXRhJCBkZSBuw6NvIHJlamVpdGFyICRIXzAkIHF1YW5kbyBvIHRpY2tldCByZWFsbWVudGUgYXVtZW50b3UuIiwgIkIiOiAiTyBlcnJvICRcXGJldGEkIHBlcm1hbmVjZSBjb25zdGFudGUsIHBvaXMgYSBwcm9iYWJpbGlkYWRlIGRlIGZhbGhhciBlbSByZWplaXRhciAkSF8wJCBkZXBlbmRlIGV4Y2x1c2l2YW1lbnRlIGRvIHRhbWFuaG8gZGEgYW1vc3RyYSAkbiQuIiwgIkMiOiAiTyBwb2RlciBkbyB0ZXN0ZSAoJDEtXFxiZXRhJCkgYXVtZW50YSBhdXRvbWF0aWNhbWVudGUsIGrDoSBxdWUgdW1hIHJlZ2nDo28gY3LDrXRpY2EgbWVub3IgdG9ybmEgYSBldmlkw6puY2lhIG1haXMgcm9idXN0YSBlIGNvbmZpw6F2ZWwuIiwgIkQiOiAiTyBFcnJvIFRpcG8gSSBkaW1pbnVpLCBtYXMgbyB0YW1hbmhvIGFtb3N0cmFsICRuPTY0JCB0b3JuYSBvIHRlc3RlIGltdW5lIMOgIHZhcmlhw6fDo28gZG8gZXJybyAkXFxiZXRhJCBuZXN0ZSBjZW7DoXJpbyBlc3BlY8OtZmljby4iLCAiRSI6ICJPICRcXGFscGhhJCBlIG8gJFxcYmV0YSQgZGltaW51ZW0gc2ltdWx0YW5lYW1lbnRlLCBwb2lzIG8gdGVzdGUgdW5pbGF0ZXJhbCDDqSBzZW1wcmUgbWFpcyBlZmljaWVudGUgcXVlIG8gYmlsYXRlcmFsIHBhcmEgcXVhbHF1ZXIgbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIHJlbGHDp8OjbyBkZSB0cmFkZS1vZmYgZW50cmUgZXJyb3MuIFBhcmEgdW0gJG4kIGZpeG8sIHNlIHZvY8OqIHRvcm5hIG8gc2V1IGNyaXTDqXJpbyBkZSByZWplacOnw6NvICgnbyBzYXJyYWZvJykgbXVpdG8gbWFpcyByaWdvcm9zbyBwYXJhIGV2aXRhciBvIEVycm8gVGlwbyBJLCBvIHF1ZSBhY29udGVjZSBjb20gYSBzZW5zaWJpbGlkYWRlIGRvIHRlc3RlIGVtIGRldGVjdGFyIGVmZWl0b3MgdmVyZGFkZWlyb3M/IiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGFsdGVybmF0aXZhIEEgw6kgYSBjb3JyZXRhLiBFbSBpbmZlcsOqbmNpYSBlc3RhdMOtc3RpY2EsIGV4aXN0ZSB1bSBjb21wcm9taXNzbyBhbnRhZ8O0bmljbyBlbnRyZSAkXFxhbHBoYSQgZSAkXFxiZXRhJC4gQW8gZGltaW51aXIgJFxcYWxwaGEkIChvIGxpbWlhciBkZSBzaWduaWZpY8OibmNpYSksIGEgcmVnacOjbyBjcsOtdGljYSAoJFJDJCkgdG9ybmEtc2UgbWVub3IgZSBtYWlzIGRpZsOtY2lsIGRlIGF0aW5naXIuIElzc28gZGltaW51aSBhIHByb2JhYmlsaWRhZGUgZGUgdW0gZmFsc28gcG9zaXRpdm8gKEVycm8gVGlwbyBJKSwgbWFzIGF1bWVudGEgYSBwcm9iYWJpbGlkYWRlIGRlIHVtIGZhbHNvIG5lZ2F0aXZvIChFcnJvIFRpcG8gSUksICRcXGJldGEkKSwgcG9pcyBvIHRlc3RlIHNlIHRvcm5hICdtZW5vcyBzZW5zw612ZWwnIHBhcmEgZGV0ZWN0YXIgcGVxdWVuYXMgbXVkYW7Dp2FzIG5hIG3DqWRpYS4gQSBhbHRlcm5hdGl2YSBCIMOpIGZhbHNhIHBvaXMgJFxcYmV0YSQgZGVwZW5kZSBkZSAkbiQsICRcXGFscGhhJCBlIGRvIGVmZWl0byByZWFsICgkXFxtdV8xJCkuIEMgZSBFIGRlc2NyZXZlbSBjb21wb3J0YW1lbnRvcyBpbmNvcnJldG9zIGRlIHBvZGVyIGVzdGF0w61zdGljby4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbH1dLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbeyJlbnVuY2lhZG8iOiAiVW0gY29udHJvbGUgZGUgcXVhbGlkYWRlIG1vbml0b3JhIG8gZGnDom1ldHJvIGRlIHBlw6dhcyBkZSBwcmVjaXPDo28uIE8gZGnDom1ldHJvIGVzcGVyYWRvIHNvYiAkSF8wJCDDqSAkXFxtdSA9IDEwLDAkIG1tLiBBIHZhcmnDom5jaWEgw6kgY29uaGVjaWRhICRcXHNpZ21hXjIgPSAwLDA0JC4gVW1hIGFtb3N0cmEgZGUgJG49MTYkIHBlw6dhcyBhcHJlc2VudGEgbcOpZGlhICRcXGJhcntYfSA9IDEwLDE1JCBtbS4gKGEpIEZvcm11bGUgJEhfMCQgZSAkSF8xJCBwYXJhIHZlcmlmaWNhciBzZSBvIGRpw6JtZXRybyBhdW1lbnRvdS4gKGIpIENhbGN1bGUgYSBlc3RhdMOtc3RpY2EgJFpfe1xcdGV4dHtjYWxjfX0kIGUgbyBwLXZhbG9yLiAoYykgQ29tICRcXGFscGhhID0gMCwwNSQsIHRvbWUgYSBkZWNpc8OjbyBlc3RhdMOtc3RpY2EuIiwgImRpY2EiOiAiVXNlIGEgZsOzcm11bGEgJFpfe1xcdGV4dHtjYWxjfX0gPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11XzB9e1xcc2lnbWEvXFxzcXJ0e259fSQuIExlbWJyZS1zZSBxdWUgJFxcc2lnbWEgPSBcXHNxcnR7MCwwNH0gPSAwLDIkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAoYSk6ICRIXzA6IFxcbXUgPSAxMCwwJCB2cyAkSF8xOiBcXG11ID4gMTAsMCQuIiwgIlBhc3NvIChiKTogRXJybyBwYWRyw6NvICRFUChcXGJhcntYfSkgPSBcXGZyYWN7MCwyfXtcXHNxcnR7MTZ9fSA9IDAsMDUkLiBMb2dvLCAkWl97XFx0ZXh0e2NhbGN9fSA9IFxcZnJhY3sxMCwxNSAtIDEwLDB9ezAsMDV9ID0gMywwJC4iLCAiUGFzc28gKGMpOiAkcFxcdGV4dHstdmFsb3J9ID0gUChaID4gMywwKSA9IDEgLSAwLDk5ODcgPSAwLDAwMTMkLiIsICJQYXNzbyAoZCk6IENvbW8gJHBcXHRleHR7LXZhbG9yfSA8IDAsMDUkLCByZWplaXRhbW9zICRIXzAkLiBIw6EgZXZpZMOqbmNpYXMgZGUgcXVlIG8gZGnDom1ldHJvIG3DqWRpbyDDqSBzdXBlcmlvciBhIDEwLDAgbW0uIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjAwMTN9LCB7ImVudW5jaWFkbyI6ICJVbSBwZXNxdWlzYWRvciBlc3R1ZGEgYSBlZmljw6FjaWEgZGUgdW0gbm92byBtw6l0b2RvIGRlIHRyZWluYW1lbnRvIGVtIHZlbmRhcy4gTyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgZGVmaW5pZG8gw6kgJFxcYWxwaGEgPSAwLDA1JC4gTyB0ZXN0ZSBzZWd1ZSB1bWEgZGlzdHJpYnVpw6fDo28gbm9ybWFsIHBhZHLDo28gYXDDs3Mgbm9ybWFsaXphw6fDo28uIChhKSBEZWZpbmEgYSByZWdpw6NvIGNyw610aWNhIHBhcmEgdW0gdGVzdGUgYmljYXVkYWwgKCRIXzE6IFxcbXUgXFxuZXEgXFxtdV8wJCkuIChiKSBFeHBsaXF1ZSBvIHF1ZSByZXByZXNlbnRhIGEgw6FyZWEgc29tYnJlYWRhIG5hIHJlZ2nDo28gZGUgcmVqZWnDp8OjbyBzb2IgbyBwb250byBkZSB2aXN0YSBkZSB0b21hZGEgZGUgZGVjaXPDo28uIChjKSBTZSBvIHJlc3VsdGFkbyBleHBlcmltZW50YWwgcmVzdWx0YXIgZW0gJFpfe1xcdGV4dHtjYWxjfX0gPSAxLDc1JCwgbyBxdWUgZGV2ZSBzZXIgZmVpdG8/IiwgImRpY2EiOiAiUGFyYSB1bSB0ZXN0ZSBiaWNhdWRhbCBjb20gJFxcYWxwaGE9MCwwNSQsIGEgcmVqZWnDp8OjbyBvY29ycmUgc2UgJHxaX3tcXHRleHR7Y2FsY319fCA+IFpfezAsMDI1fSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIChhKTogJFJDID0gXFx7WiBcXGluIFxcbWF0aGJie1J9IDogWiA8IC0xLDk2IFxcdGV4dHsgb3UgfSBaID4gMSw5NlxcfSQuIiwgIlBhc3NvIChiKTogQSDDoXJlYSBzb21icmVhZGEgcmVwcmVzZW50YSBhIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgJEhfMCQgc2VuZG8gZXN0YSB2ZXJkYWRlaXJhIChFcnJvIFRpcG8gSSksIGZpeGFkYSBlbSAkNVxcJSQuIiwgIlBhc3NvIChjKTogQ29tbyAkMSw3NSA8IDEsOTYkLCBuw6NvIHJlamVpdGFtb3MgJEhfMCQuIE8gdmFsb3Igb2JzZXJ2YWRvIG7Do28gw6kgZXN0YXRpc3RpY2FtZW50ZSBzaWduaWZpY2FudGUgYW8gbsOtdmVsIGRlICQ1XFwlJC4iXSwgImNvZGlnb19wbG90bHkiOiAiaW1wb3J0IHBsb3RseS5ncmFwaF9vYmplY3RzIGFzIGdvXG5pbXBvcnQgbnVtcHkgYXMgbnBcbnggPSBucC5saW5zcGFjZSgtNCwgNCwgMjAwKVxueSA9ICgxL25wLlxcc3FydCgyKm5wLlxccGkpKSAqIG5wLlxcZXhwKC0wLjUqeCoqMilcbmZpZyA9IGdvLkZpZ3VyZSgpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIG5hbWU9J05vcm1hbCAoMCwxKScsIGxpbmU9ZGljdChjb2xvcj0nIzc4MzUwRicpKSlcbmZpZy5hZGRfdnJlY3QoeDA9MS45NiwgeDE9NCwgZmlsbGNvbG9yPScjOTkxQjFCJywgb3BhY2l0eT0wLjMsIGxpbmVfd2lkdGg9MClcbmZpZy5hZGRfdnJlY3QoeDA9LTQsIHgxPS0xLjk2LCBmaWxsY29sb3I9JyM5OTFCMUInLCBvcGFjaXR5PTAuMywgbGluZV93aWR0aD0wKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J1JlZ2nDo28gQ3LDrXRpY2EgQmljYXVkYWwnLCB4YXhpc190aXRsZT0nWicsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnLCB0ZW1wbGF0ZT0ncGxvdGx5X3doaXRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBlc3R1ZG8gZGUgY2FtcG8sIG8gY3VzdG8gbcOpZGlvIGRlIG1hbnV0ZW7Dp8OjbyBkZSB1bSBlcXVpcGFtZW50byDDqSAkXFxtdSA9IDIwMCQgZSBkZXN2aW8gcGFkcsOjbyAkXFxzaWdtYSA9IDIwJC4gU3VzcGVpdGEtc2UgZGUgdW0gYXVtZW50byBubyBjdXN0by4gVW1hIGFtb3N0cmEgZGUgJG49MjUkIGZvcm5lY2UgJFxcYmFye1h9ID0gMjA4JC4gKGEpIERldGVybWluZSBhIHByb2JhYmlsaWRhZGUgZG8gRXJybyBUaXBvIEkgc2UgYSByZWdyYSBkZSBkZWNpc8OjbyBmb3IgcmVqZWl0YXIgJEhfMCQgc2UgJFxcYmFye1h9ID4gMjA2JC4gKGIpIENhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRvIEVycm8gVGlwbyBJSSAoJFxcYmV0YSQpIHNlIG8gY3VzdG8gcmVhbCBmb3IgJFxcbXUgPSAyMTAkLiAoYykgQ29tZW50ZSBzb2JyZSBvIHBvZGVyIGRvIHRlc3RlLiIsICJkaWNhIjogIlNvYiAkSF8wJCwgJFxcYmFye1h9IFxcc2ltIE4oMjAwLCA0XjIpJC4gU29iICRIXzEkICgkXFxtdT0yMTAkKSwgJFxcYmFye1h9IFxcc2ltIE4oMjEwLCA0XjIpJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gKGEpOiAkXFxhbHBoYSA9IFAoXFxiYXJ7WH0gPiAyMDYgfCBcXG11PTIwMCkgPSBQKFogPiBcXGZyYWN7MjA2LTIwMH17NH0pID0gUChaID4gMSw1KSA9IDEgLSAwLDkzMzIgPSAwLDA2NjgkLiIsICJQYXNzbyAoYik6ICRcXGJldGEgPSBQKFxcYmFye1h9IFxcbGUgMjA2IHwgXFxtdT0yMTApID0gUChaIFxcbGUgXFxmcmFjezIwNi0yMTB9ezR9KSA9IFAoWiBcXGxlIC0xLDApID0gMCwxNTg3JC4iLCAiUGFzc28gKGMpOiBPIHBvZGVyIGRvIHRlc3RlIMOpICQxIC0gXFxiZXRhID0gMSAtIDAsMTU4NyA9IDAsODQxMyQuIE8gdGVzdGUgdGVtICQ4NCwxM1xcJSQgZGUgY2hhbmNlIGRlIGRldGVjdGFyIG8gYXVtZW50byBkZSBjdXN0byBwYXJhICRcXG11PTIxMCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAidTFxMjUzYW4zZzNkLCBwLiAzMzgiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjg0MTN9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgdW0gdGVzdGUgZGUgaGlww7N0ZXNlcyBzb2JyZSBhIG3DqWRpYSBkZSB1bWEgcG9wdWxhw6fDo28gY29tIHZhcmnDom5jaWEgY29uaGVjaWRhICRcXHNpZ21hXjIgPSAxMDAkLiBUZW1vcyAkSF8wOiBcXG11ID0gMTAwJCBlICRIXzE6IFxcbXUgPSAxMDUkLiBDb20gdW1hIGFtb3N0cmEgZGUgJG49MjUkLCBkZWZpbmltb3MgYSByZWdpw6NvIGNyw610aWNhICRSQyA9IFxceyBcXGJhcntYfSA+IDEwMy4yOSBcXH0kLiAoYSkgQ2FsY3VsZSBhIHByb2JhYmlsaWRhZGUgZG8gZXJybyBkZSBwcmltZWlyYSBlc3DDqWNpZSAkXFxhbHBoYSQuIChiKSBDYWxjdWxlIGEgcHJvYmFiaWxpZGFkZSBkbyBlcnJvIGRlIHNlZ3VuZGEgZXNww6ljaWUgJFxcYmV0YSQgcGFyYSBhIG3DqWRpYSBzb2IgJEhfMSQuIChjKSBRdWFsIHNlcmlhIG8gcG9kZXIgZG8gdGVzdGU/IiwgImRpY2EiOiAiVXRpbGl6ZSBhIHBhZHJvbml6YcOnw6NvICRaID0gKFxcYmFye1h9IC0gXFxtdSkgLyAoXFxzaWdtYSAvIFxcc3FydHtufSkkLiBMZW1icmUtc2UgcXVlIHNvYiAkSF8wJCwgJFxcbXU9MTAwJCwgZSBzb2IgJEhfMSQsICRcXG11PTEwNSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIChhKTogU29iICRIXzAkLCAkXFxiYXJ7WH0gXFxzaW0gTigxMDAsIDEwMC8yNSkgPSBOKDEwMCwgNCkkLiAkXFxhbHBoYSA9IFAoXFxiYXJ7WH0gPiAxMDMuMjkgfCBcXG11PTEwMCkgPSBQKFogPiAoMTAzLjI5IC0gMTAwKSAvIDIpID0gUChaID4gMS42NDUpIFxcYXBwcm94IDAuMDUkLiIsICJQYXNzbyAoYik6IFNvYiAkSF8xJCwgJFxcYmFye1h9IFxcc2ltIE4oMTA1LCA0KSQuICRcXGJldGEgPSBQKFxcYmFye1h9IFxcbGUgMTAzLjI5IHwgXFxtdT0xMDUpID0gUChaIFxcbGUgKDEwMy4yOSAtIDEwNSkgLyAyKSA9IFAoWiBcXGxlIC0wLjg1NSkgXFxhcHByb3ggMC4xOTYzJC4iLCAiUGFzc28gKGMpOiBPIHBvZGVyIGRvIHRlc3RlIMOpICQxIC0gXFxiZXRhID0gMSAtIDAuMTk2MyA9IDAuODAzNyQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjE5NjN9LCB7ImVudW5jaWFkbyI6ICJVbSBjaWVudGlzdGEgZGUgZGFkb3MgYXZhbGlhIHVtIG1vZGVsbyBkZSBjaHVybiBjb20gJEhfMCQ6IFRheGEgZGUgcmV0ZW7Dp8OjbyAkXFxnZSA4MFxcJSQgdnMgJEhfMSQ6IFRheGEgZGUgcmV0ZW7Dp8OjbyAkPCA4MFxcJSQuIFNhYmVuZG8gcXVlIG8gY3VzdG8gZGUgdW1hIGRlY2lzw6NvIGVycmFkYSAocmVqZWl0YXIgJEhfMCQgc2VuZG8gdmVyZGFkZWlyYSkgw6kgYWx0w61zc2ltbywgZWxlIGRlZmluZSAkXFxhbHBoYSA9IDAuMDEkLiAoYSkgRXhwbGlxdWUgZm9ybWFsbWVudGUgbyBxdWUgJFxcYWxwaGEkIHJlcHJlc2VudGEgYXF1aS4gKGIpIENvbW8gbyBmb3JtYWxpc21vIG1hdGVtw6F0aWNvIGdhcmFudGUgcXVlIGVzdGUgZXJybyBwZXJtYW5lw6dhIGFiYWl4byBkbyBsaW1pdGUgZGVmaW5pZG8/IChjKSBEaXNjdXRhIGEgcmVsYcOnw6NvIGVudHJlIG8gYXVtZW50byBkZSAkXFxhbHBoYSQgZSBhIHJlZHXDp8OjbyBkZSAkXFxiZXRhJC4iLCAiZGljYSI6ICJPIHZhbG9yIGRlICRcXGFscGhhJCBsaW1pdGEgYSDDoXJlYSBzb2IgYSBjYXVkYSBkYSBkaXN0cmlidWnDp8OjbyBudWxhLiBBdW1lbnRhciAkXFxhbHBoYSQgZXhwYW5kZSBhIHJlZ2nDo28gY3LDrXRpY2EuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIihhKSAkXFxhbHBoYSQgw6kgbyByaXNjbyBkZSBjb25jbHVpciBlcnJvbmVhbWVudGUgcXVlIGEgdGF4YSBkZSByZXRlbsOnw6NvIGNhaXUgYWJhaXhvIGRlICQ4MFxcJSQsIHF1YW5kbyBuYSB2ZXJkYWRlIGVsYSBhaW5kYSBlc3TDoSBlbSBuw612ZWwgYWNlaXTDoXZlbCwgbGV2YW5kbyBhIGHDp8O1ZXMgY29ycmV0aXZhcyBkZXNuZWNlc3PDoXJpYXMuIiwgIihiKSBPIGZvcm1hbGlzbW8gdXRpbGl6YSBhIGRpc3RyaWJ1acOnw6NvIGFtb3N0cmFsIGRvIGVzdGltYWRvciAkXFxoYXR7cH0kIHNvYiBhIGhpcMOzdGVzZSAkcD0wLjgwJC4gQSByZWdpw6NvIGNyw610aWNhICRSQyQgw6kgZGV0ZXJtaW5hZGEgdGFsIHF1ZSAkUChcXGhhdHtwfSBcXGluIFJDIHwgcD0wLjgwKSBcXGxlIDAuMDEkLiIsICIoYykgRXhpc3RlIHVtYSByZWxhw6fDo28gZGUgdHJvY2EgKHRyYWRlLW9mZik6IGFvIGF1bWVudGFyICRcXGFscGhhJCwgYSByZWdpw6NvIGNyw610aWNhICRSQyQgZXhwYW5kZSwgZmFjaWxpdGFuZG8gYSByZWplacOnw6NvIGRlICRIXzAkLiBJc3NvIHJlZHV6IGEgY2hhbmNlIGRlIGZhbGhhciBlbSBkZXRlY3RhciB1bWEgcXVlZGEgcmVhbCAoZGltaW51aSAkXFxiZXRhJCksIHBvcsOpbSBhdW1lbnRhIG8gcmlzY28gZGUgZmFsc29zIHBvc2l0aXZvcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJOdW0gZXN0dWRvIGRlIGVmaWPDoWNpYSBkZSB1bSBub3ZvIGZlcnRpbGl6YW50ZSwgYXNzdW1hICRIXzA6IFxcbXVfe1xcdGV4dHtub3ZvfX0gPSBcXG11X3tcXHRleHR7YXR1YWx9fSQgZSAkSF8xOiBcXG11X3tcXHRleHR7bm92b319ID4gXFxtdV97XFx0ZXh0e2F0dWFsfX0kLiBBIHZhcmnDom5jaWEgY29tdW0gw6kgJDE2JCBlIG8gdGFtYW5obyBhbW9zdHJhbCAkbj0xNiQgcGFyYSBjYWRhIGdydXBvLiBDb20gJFxcYWxwaGEgPSAwLjA1JCwgbyB2YWxvciBjcsOtdGljbyBwYXJhICRcXGJhcntYfV97bm92b30gLSBcXGJhcntYfV97YXR1YWx9JCDDqSAkMi4zMjYkLiAoYSkgQ2FsY3VsZSBvIGVycm8gJFxcYmV0YSQgc2UgYSBkaWZlcmVuw6dhIHJlYWwgZW50cmUgYXMgbcOpZGlhcyBmb3IgJFxcRGVsdGEgPSAyJC4gKGIpIFF1YWwgbyBwb2RlciBkbyB0ZXN0ZSBuZXN0YSBjb25kacOnw6NvPyIsICJkaWNhIjogIlVzZSBhIGRpc3RyaWJ1acOnw6NvIGRhIGRpZmVyZW7Dp2EgZGUgbcOpZGlhczogJFxcYmFye1h9XzEgLSBcXGJhcntYfV8yIFxcc2ltIE4oMCwgXFxzaWdtYV4yL25fMSArIFxcc2lnbWFeMi9uXzIpJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQSB2YXJpw6JuY2lhIGRhIGRpZmVyZW7Dp2Egw6kgJFxcc2lnbWFeMl9EID0gMTYvMTYgKyAxNi8xNiA9IDIkLiBPIGRlc3ZpbyBwYWRyw6NvIMOpICRcXHNxcnR7Mn0gXFxhcHByb3ggMS40MTQkLiIsICJTb2IgJEhfMSQsIGEgZGlmZXJlbsOnYSByZWFsIMOpICRcXERlbHRhID0gMiQuIEEgZGlzdHJpYnVpw6fDo28gZGEgZGlmZXJlbsOnYSBzb2IgJEhfMSQgw6kgJE4oMiwgMikkLiIsICIkXFxiZXRhID0gUChcXHRleHR7RGlmZXJlbsOnYX0gXFxsZSAyLjMyNiB8IFxcRGVsdGE9MikgPSBQKFogXFxsZSAoMi4zMjYgLSAyKSAvIDEuNDE0KSA9IFAoWiBcXGxlIDAuMjMpIFxcYXBwcm94IDAuNTkxJC4iLCAiTyBwb2RlciBkbyB0ZXN0ZSDDqSAkMSAtIDAuNTkxID0gMC40MDkkLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKC0zLCA2LCAyMDApXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLm5vcm0ucGRmKHgsIDAsIG5wLlxcc3FydCgyKSksIG5hbWU9XCJTb2IgJEhfMCRcIiwgZmlsbD0ndG96ZXJveScsIGxpbmU9ZGljdChjb2xvcj0nIzc4MzUwRicpKSlcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9c3RhdHMubm9ybS5wZGYoeCwgMiwgbnAuXFxzcXJ0KDIpKSwgbmFtZT1cIlNvYiAkSF8xJFwiLCBmaWxsPSd0b3plcm95JywgbGluZT1kaWN0KGNvbG9yPScjOTkxQjFCJykpKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9XCJWaXN1YWxpemHDp8OjbyBkbyBQb2RlciBkbyBUZXN0ZVwiLCB4YXhpc190aXRsZT1cIkRpZmVyZW7Dp2EgZGUgTcOpZGlhc1wiLCB5YXhpc190aXRsZT1cIkRlbnNpZGFkZVwiKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC41OTF9LCB7ImVudW5jaWFkbyI6ICJVbWEgcmVmaW5hcmlhIHRlc3RhIHNlIG8gdGVvciBkZSBlbnhvZnJlIGVtIHVtIGNvbWJ1c3TDrXZlbCDDqSAkXFxtdV8wID0gMC41XFwlJC4gU2FiZS1zZSBxdWUgJFxcc2lnbWEgPSAwLjA4XFwlJC4gQ29tIHVtYSBhbW9zdHJhIGRlICRuID0gMTYkLCB0ZXN0YS1zZSAkSF8wOiBcXG11ID0gMC41JCB2cyAkSF8xOiBcXG11IFxcbmVxIDAuNSQgY29tICRcXGFscGhhID0gMC4wNSQuIChhKSBEZXRlcm1pbmUgYSBSZWdpw6NvIGRlIEFjZWl0YcOnw6NvIChSQSkuIChiKSBDYWxjdWxlIGEgcHJvYmFiaWxpZGFkZSBkZSBlcnJvIFRpcG8gSUkgKEZ1bsOnw6NvIENPKSBwYXJhIHVtIHZhbG9yIHJlYWwgJFxcbXVfMSA9IDAuNTRcXCUkLiAoYykgUXVhbCBvIHBvZGVyIGRvIHRlc3RlIHBhcmEgZXN0ZSBkZXN2aW8/IiwgImRpY2EiOiAiUGFyYSB0ZXN0ZXMgYmljYXVkYWlzLCBhIHJlZ2nDo28gZGUgYWNlaXRhw6fDo28gw6kgZGVmaW5pZGEgcG9yICRcXGJhcntYfSBcXGluIFtcXG11XzAgLSBaX3tcXGFscGhhLzJ9IFxcY2RvdCAoXFxzaWdtYS9cXHNxcnR7bn0pLCBcXG11XzAgKyBaX3tcXGFscGhhLzJ9IFxcY2RvdCAoXFxzaWdtYS9cXHNxcnR7bn0pXSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIihhKSBPIGVycm8gcGFkcsOjbyDDqSAkRVAgPSAwLjA4IC8gXFxzcXJ0ezE2fSA9IDAuMDIkLiBQYXJhICRcXGFscGhhID0gMC4wNSQsICRaX3swLjAyNX0gPSAxLjk2JC4gQSBSQSDDqSAkMC41IFxccG0gMS45NiBcXGNkb3QgMC4wMiQsIHJlc3VsdGFuZG8gZW0gJFswLjQ2MDgsIDAuNTM5Ml0kLiIsICIoYikgQSBGdW7Dp8OjbyBDTyDDqSAkXFxiZXRhKDAuNTQpID0gUCgwLjQ2MDggPCBcXGJhcntYfSA8IDAuNTM5MiB8IFxcbXUgPSAwLjU0KSQuIFBhZHJvbml6YW5kbyBwYXJhICRaJDogJFAoKDAuNDYwOC0wLjU0KS8wLjAyIDwgWiA8ICgwLjUzOTItMC41NCkvMC4wMikgPSBQKC0zLjk2IDwgWiA8IC0wLjA0KSQuIiwgIkNhbGN1bGFuZG86ICRcXFBoaSgtMC4wNCkgLSBcXFBoaSgtMy45NikgXFxhcHByb3ggMC40ODQwIC0gMC4wMDAwMzcgPSAwLjQ4NDAkLiIsICIoYykgTyBwb2RlciDDqSAkXFxwaSgwLjU0KSA9IDEgLSBcXGJldGEoMC41NCkgPSAxIC0gMC40ODQwID0gMC41MTYwJC4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKCk7IHggPSBucC5saW5zcGFjZSgwLjQyLCAwLjYyLCA1MDApOyB5MCA9IHN0YXRzLm5vcm0ucGRmKHgsIDAuNSwgMC4wMik7IHkxID0gc3RhdHMubm9ybS5wZGYoeCwgMC41NCwgMC4wMik7IGZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eTAsIG5hbWU9cickSF8wIChcXG11PTAuNSkkJywgZmlsbD0ndG96ZXJveScpKTsgZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15MSwgbmFtZT1yJyRIXzEgKFxcbXU9MC41NCkkJywgZmlsbD0ndG96ZXJveScpKTsgZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J0Rpc3RyaWJ1acOnw7VlcyBkZSBBbW9zdHJhZ2VtJywgeGF4aXNfdGl0bGU9cidNw6lkaWEgQW1vc3RyYWwgKCRcXGJhcntYfSQpJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScsIHRlbXBsYXRlPSdwbG90bHlfd2hpdGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC41MTZ9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgdW0gcHJvY2Vzc28gaW5kdXN0cmlhbCBlbSBxdWUgYSB2YXJpw6F2ZWwgZGUgaW50ZXJlc3NlIHRlbSBkaXN0cmlidWnDp8OjbyBOb3JtYWwgY29tIHZhcmnDom5jaWEgY29uaGVjaWRhLiBEZW1vbnN0cmUgYWxnZWJyaWNhbWVudGUgY29tbyBhIEZ1bsOnw6NvIFBvZGVyICRcXHBpKFxcbXUpJCBzZSBjb21wb3J0YSBxdWFuZG8gbyBwYXLDom1ldHJvIHJlYWwgJFxcbXUkIHRlbmRlIGFvIGluZmluaXRvIChwYXJhIHVtIHRlc3RlIHVuaWxhdGVyYWwgc3VwZXJpb3IpLiBFeHBsaXF1ZSBhIGltcGxpY2HDp8OjbyBwcsOhdGljYSBkZXNzZSBsaW1pdGUgcGFyYSBvIGRlc2VuaG8gZG8gY29udHJvbGUgZGUgcXVhbGlkYWRlLiIsICJkaWNhIjogIkFuYWxpc2UgbyBjb21wb3J0YW1lbnRvIGRlICRcXHBpKFxcbXUpID0gUChcXGJhcntYfSA+IGMgfCBcXG11KSQgcXVhbmRvICRcXG11IFxcdG8gXFxpbmZ0eSQuIExlbWJyZS1zZSBxdWUgJFAoWiA+IChjLVxcbXUpL0VQKSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIkEgRnVuw6fDo28gUG9kZXIgw6kgZGFkYSBwb3IgJFxccGkoXFxtdSkgPSBQKFxcYmFye1h9ID4gYyB8IFxcbXUpJCwgb25kZSAkYyA9IFxcbXVfMCArIFpfe1xcYWxwaGF9IFxcY2RvdCAoXFxzaWdtYS9cXHNxcnR7bn0pJC4iLCAiU3Vic3RpdHVpbmRvLCB0ZW1vcyAkXFxwaShcXG11KSA9IFAoXFxmcmFje1xcYmFye1h9IC0gXFxtdX17XFxzaWdtYS9cXHNxcnR7bn19ID4gXFxmcmFje2MgLSBcXG11fXtcXHNpZ21hL1xcc3FydHtufX0pID0gUChaID4gXFxmcmFje1xcbXVfMCArIFpfe1xcYWxwaGF9KFxcc2lnbWEvXFxzcXJ0e259KSAtIFxcbXV9e1xcc2lnbWEvXFxzcXJ0e259fSkkLiIsICJSZW9yZ2FuaXphbmRvOiAkXFxwaShcXG11KSA9IFAoWiA+IFpfe1xcYWxwaGF9ICsgXFxmcmFje1xcbXVfMCAtIFxcbXV9e1xcc2lnbWEvXFxzcXJ0e259fSkkLiIsICLDgCBtZWRpZGEgcXVlICRcXG11IFxcdG8gXFxpbmZ0eSQsIG8gdGVybW8gJFxcZnJhY3tcXG11XzAgLSBcXG11fXtcXHNpZ21hL1xcc3FydHtufX0gXFx0byAtXFxpbmZ0eSQuIiwgIkxvZ28sICRQKFogPiAtXFxpbmZ0eSkgPSAxJC4gTyBwb2RlciB0ZW5kZSBhIDEsIGluZGljYW5kbyBxdWUgbyB0ZXN0ZSB0ZW0gcHJvYmFiaWxpZGFkZSB0b3RhbCBkZSBkZXRlY3RhciBkZXN2aW9zIHNldmVyb3MgKG11aXRvIGdyYW5kZXMpLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGVzdHVkbyBjbMOtbmljbywgZGVzZWphLXNlIHRlc3RhciBhIGVmaWPDoWNpYSBkZSB1bSBub3ZvIGbDoXJtYWNvIGNvbXBhcmFkbyBhIHVtIHBhZHLDo28gKCRcXG11XzAgPSAxMDAkKS4gTyBkZXN2aW8gcGFkcsOjbyDDqSAkMTAkLiBDb20gJG4gPSAyNSQgZSAkXFxhbHBoYSA9IDAuMDEkICh1bmlsYXRlcmFsKSwgZGVmaW5hIGEgcmVnacOjbyBkZSByZWplacOnw6NvLiBTZSBhIHZlcmRhZGVpcmEgbcOpZGlhIHNvYiBvIHVzbyBkbyBmw6FybWFjbyDDqSAkXFxtdV8xID0gMTA1JCwgY2FsY3VsZSBvIFBvZGVyIGRvIHRlc3RlLiIsICJkaWNhIjogIk8gdmFsb3IgY3LDrXRpY28gJFpfezAuMDF9JCBwYXJhIHVtYSBjYXVkYSBzdXBlcmlvciDDqSAkMi4zMyQuIFVzZSAkYyA9IFxcbXVfMCArIFpfezAuMDF9IFxcY2RvdCAoXFxzaWdtYS9cXHNxcnR7bn0pJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiQ8OhbGN1bG8gZG8gZXJybyBwYWRyw6NvOiAkRVAgPSAxMCAvIFxcc3FydHsyNX0gPSAyJC4iLCAiVmFsb3IgY3LDrXRpY286ICRjID0gMTAwICsgMi4zMyBcXGNkb3QgMiA9IDEwMCArIDQuNjYgPSAxMDQuNjYkLiIsICJSZWdpw6NvIGRlIFJlamVpw6fDo286ICRcXGJhcntYfSA+IDEwNC42NiQuIiwgIkPDoWxjdWxvIGRvIFBvZGVyOiAkXFxwaSgxMDUpID0gUChcXGJhcntYfSA+IDEwNC42NiB8IFxcbXUgPSAxMDUpJC4iLCAiUGFkcm9uaXphw6fDo286ICRQKFogPiAoMTA0LjY2IC0gMTA1KSAvIDIpID0gUChaID4gLTAuMzQgLyAyKSA9IFAoWiA+IC0wLjE3KSQuIiwgIlBlbGEgdGFiZWxhIG5vcm1hbDogJDEgLSBcXFBoaSgtMC4xNykgPSAxIC0gMC40MzI1ID0gMC41Njc1JC4iXSwgImNvZGlnb19wbG90bHkiOiAiZmlnID0gZ28uRmlndXJlKCk7IHggPSBucC5saW5zcGFjZSg5NSwgMTE1LCAyMDApOyB5MCA9IHN0YXRzLm5vcm0ucGRmKHgsIDEwMCwgMik7IHkxID0gc3RhdHMubm9ybS5wZGYoeCwgMTA1LCAyKTsgZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15MCwgbmFtZT1yJyRIXzAkJykpOyBmaWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXkxLCBuYW1lPXInJEhfMSQnKSk7IGZpZy5hZGRfc2hhcGUodHlwZT0nbGluZScsIHgwPTEwNC42NiwgeTA9MCwgeDE9MTA0LjY2LCB5MT0wLjI1LCBsaW5lPWRpY3QoY29sb3I9J3JlZCcpKTsgZmlnLnVwZGF0ZV9sYXlvdXQodGVtcGxhdGU9J3Bsb3RseV93aGl0ZScsIHRpdGxlPSdSZWdpw6NvIENyw610aWNhIGUgUG9kZXInKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC41Njc1fSwgeyJlbnVuY2lhZG8iOiAiVW0gbGFib3JhdMOzcmlvIGZhcm1hY8OqdXRpY28gdGVzdGEgYSBlZmljw6FjaWEgZGUgdW0gbm92byBmw6FybWFjbyBwYXJhIHJlZHXDp8OjbyBkYSBwcmVzc8OjbyBhcnRlcmlhbCBzaXN0w7NsaWNhLiBPIG9iamV0aXZvIMOpIHByb3ZhciBxdWUgYSByZWR1w6fDo28gbcOpZGlhIMOpIHN1cGVyaW9yIGEgMTAgbW1IZy4gKGEpIERlZmluYSBhcyBoaXDDs3Rlc2VzICRIXzAkIGUgJEhfMSQuIChiKSBTZW5kbyAkXFxiYXJ7WH0gPSAxMiQgbW1IZywgJG49MjUkLCAkXFxzaWdtYT01JCBtbUhnIGUgJFxcYWxwaGE9MCwwNSQsIGNhbGN1bGUgbyAkWl97XHRleHR7Y2FsY319JCBlIGRldGVybWluZSBzZSBow6EgZXZpZMOqbmNpYSBwYXJhIHJlamVpdGFyICRIXzAkIChkYWRvICRaX3tcdGV4dHtjcml0fX0gPSAxLDY0NSQpLiAoYykgSW50ZXJwcmV0ZSBvIHNpZ25pZmljYWRvIGRvIEVycm8gVGlwbyBJIG5lc3RlIGNvbnRleHRvIG3DqWRpY28uIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBwYXJhIHRlc3RlcyBkZSBtw6lkaWEgY29tIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCBjb25oZWNpZG8sIGEgZXN0YXTDrXN0aWNhIMOpICRaID0gXFxmcmFje1xcYmFye1h9IC0gXFxtdV8wfXtcXHNpZ21hIC8gXFxzcXJ0e259fSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIihhKSAkSF8wOiBcXG11ID0gMTAkIGNvbnRyYSAkSF8xOiBcXG11ID4gMTAkLiIsICIoYikgQ8OhbGN1bG8gZG8gZXJybyBwYWRyw6NvOiAkRVAoXFxiYXJ7WH0pID0gXFxmcmFje1xcc2lnbWF9e1xcc3FydHtufX0gPSBcXGZyYWN7NX17XFxzcXJ0ezI1fX0gPSBcXGZyYWN7NX17NX0gPSAxJC4iLCAiKGMpIEPDoWxjdWxvIGRlICRaX3tcdGV4dHtjYWxjfX0gPSBcXGZyYWN7XFxiYXJ7WH0gLSBcXG11XzB9e0VQKFxcYmFye1h9KX0gPSBcXGZyYWN7MTIgLSAxMH17MX0gPSAyLDAkLiIsICIoZCkgQ29tcGFyYcOnw6NvOiAkMiwwID4gMSw2NDUkLCBsb2dvIHJlamVpdGFtb3MgJEhfMCQgYW8gbsOtdmVsIGRlICQ1XFwlJC4iLCAiKGUpIE8gRXJybyBUaXBvIEkgc2lnbmlmaWNhcmlhIGNvbmNsdWlyIHF1ZSBvIGbDoXJtYWNvIHJlZHV6IG1haXMgcXVlIDEwIG1tSGcgcXVhbmRvLCBuYSByZWFsaWRhZGUsIGVsZSByZWR1eiBhcGVuYXMgMTAgbW1IZyAob3UgbWVub3MpLCBwb2RlbmRvIGxldmFyIMOgIGNvbWVyY2lhbGl6YcOnw6NvIGRlIHVtIG1lZGljYW1lbnRvIG1lbm9zIGVmaWNheiBkbyBxdWUgbyBwcm9tZXRpZG8uIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAyLjB9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyBjdXN0byBvcGVyYWNpb25hbCBkZSB1bSBzZXJ2aWRvciBkZSBkYWRvcy4gTyBjdXN0byBtZW5zYWwgbcOpZGlvIMOpIGRlIFIkIDUuMDAwLDAwLiBVbWEgZXF1aXBlIGRlIFRJIGltcGxlbWVudGEgdW1hIG90aW1pemHDp8OjbyBlIHN1c3BlaXRhIHF1ZSBvIGN1c3RvIG11ZG91LiAoYSkgRm9ybXVsZSAkSF8wJCBlICRIXzEkIHBhcmEgdW0gdGVzdGUgYmlsYXRlcmFsLiAoYikgQ2FsY3VsZSBvICRwJC12YWxvciBzZSBhIGVzdGF0w61zdGljYSBkZSB0ZXN0ZSBmb3IgJFpfe1x0ZXh0e2NhbGN9fSA9IC0yLDU4JC4gKGMpIENvbnNpZGVyYW5kbyAkXFxhbHBoYSA9IDAsMDEkLCBxdWFsIGEgZGVjaXPDo28/IiwgImRpY2EiOiAiUGFyYSB0ZXN0ZXMgYmlsYXRlcmFpcywgbyAkcCQtdmFsb3Igw6kgJDIgXFx0aW1lcyBQKFogPiB8Wl97XHRleHR7Y2FsY319fCkkLiBVc2UgYSBzaW1ldHJpYSBkYSBOb3JtYWwuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIihhKSAkSF8wOiBcXG11ID0gNTAwMCQgZSAkSF8xOiBcXG11IFxcbmVxIDUwMDAkLiIsICIoYikgUGFyYSAkWl97XHRleHR7Y2FsY319ID0gLTIsNTgkLCBvIHZhbG9yIGRlICRQKFogPCAtMiw1OCkgXFxhcHByb3ggMCwwMDQ5JC4iLCAiKGMpIENvbW8gw6kgdW0gdGVzdGUgYmlsYXRlcmFsLCAkcFx0ZXh0ey12YWxvcn0gPSAyIFxcdGltZXMgMCwwMDQ5ID0gMCwwMDk4JC4iLCAiKGQpIERlY2lzw6NvOiBDb21vICRwXHRleHR7LXZhbG9yfSA9IDAsMDA5OCA8IDAsMDEkLCByZWplaXRhbW9zICRIXzAkLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKC00LCA0LCAxMDApXG55ID0gc3RhdHMubm9ybS5wZGYoeClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eSwgbmFtZT0nTigwLDEpJywgbGluZT1kaWN0KGNvbG9yPScjNzgzNTBGJykpKVxuZmlnLmFkZF92bGluZSh4PS0yLjU4LCBsaW5lX2Rhc2g9J2Rhc2gnLCBsaW5lX2NvbG9yPScjOTkxQjFCJywgbmFtZT0nWl9jYWxjJylcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSc8Yj5EaXN0cmlidWnDp8OjbyBOb3JtYWwgZSBQLVZhbG9yPC9iPicpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjAwOTh9LCB7ImVudW5jaWFkbyI6ICJVbSBwcm9jZXNzbyBpbmR1c3RyaWFsIHByb2R1eiBjYWJvcyBjb20gcmVzaXN0w6puY2lhIMOgIHRyYcOnw6NvIG3DqWRpYSBkZSA1MDAga2dmLiBVbSBjb250cm9sZSBkZSBxdWFsaWRhZGUgZGVzZWphIGdhcmFudGlyIHF1ZSBhIG3DqWRpYSBuw6NvIHNlamEgaW5mZXJpb3IgYSBlc3NlIHBhZHLDo28uIChhKSBEZWZpbmEgYXMgaGlww7N0ZXNlcy4gKGIpIFNlIG8gcG9kZXIgZG8gdGVzdGUgKCQxLVxcYmV0YSQpIGZvciAkMCw4MCQgcGFyYSB1bWEgYWx0ZXJuYXRpdmEgJFxcbXUgPSA0OTAkIGtnZiwgZXhwbGlxdWUgbyBxdWUgZXN0ZSB2YWxvciByZXByZXNlbnRhIGVtIHRlcm1vcyBkZSBwcm9iYWJpbGlkYWRlLiAoYykgQ29tbyB1bSBhdW1lbnRvIGRlICRuJCBhZmV0YSBvIEVycm8gVGlwbyBJSSAoJFxcYmV0YSQpPyIsICJkaWNhIjogIk8gcG9kZXIgZG8gdGVzdGUgw6kgYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIGRhZG8gcXVlIGVsYSDDqSByZWFsbWVudGUgZmFsc2EuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIihhKSAkSF8wOiBcXG11ID0gNTAwJCBjb250cmEgJEhfMTogXFxtdSA8IDUwMCQgKHRlc3RlIHVuaWxhdGVyYWwgw6AgZXNxdWVyZGEpLiIsICIoYikgTyBwb2RlciBkZSAkMCw4MCQgc2lnbmlmaWNhIHF1ZSwgc2UgYSByZXNpc3TDqm5jaWEgcmVhbCBkbyBjYWJvIGZvciBkZSA0OTAga2dmLCBvIHRlc3RlIHRlbSAkODBcXCUkIGRlIGNoYW5jZSBkZSBjb3JyZXRhbWVudGUgcmVqZWl0YXIgYSBoaXDDs3Rlc2UgbnVsYSBkZSA1MDAga2dmLiIsICIoYykgTyBhdW1lbnRvIGRlICRuJCByZWR1eiBvIGVycm8gcGFkcsOjbyBkYSBtw6lkaWEgKCRFUChcXGJhcntYfSkgPSBcXHNpZ21hL1xcc3FydHtufSQpLCBkaW1pbnVpbmRvIGEgc29icmVwb3Npw6fDo28gZW50cmUgYSBkaXN0cmlidWnDp8OjbyBzb2IgJEhfMCQgZSBhIGRpc3RyaWJ1acOnw6NvIHNvYiAkSF8xJCwgbyBxdWUgcmVkdXogbyAkXFxiZXRhJCBlIGF1bWVudGEgbyBwb2RlciBkbyB0ZXN0ZS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuOH1dfQ==').decode('utf-8'))


    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    import scipy.stats as stats
    
    # Garantir persistência de estado para gamificação
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dos totais de exercícios
    total_mcq = len(dados_exercicios.get("questoes_multipla_escolha", []))
    total_disc = len(dados_exercicios.get("questoes_discursivas", []))
    total_ex = total_mcq + total_disc
    acertos = sum(1 for v in st.session_state.respostas_certas.values() if v is True)
    
    # Interface de Gamificação
    st.markdown("### 🎯 Centro de Exercícios de Inferência")
    if total_ex > 0:
        st.progress(acertos / total_ex)
        st.info(f"🏆 **Seu Placar de Aprendizado:** {acertos} de {total_ex} desafios concluídos com sucesso!")
    
    # --- Seção de Múltipla Escolha ---
    if "questoes_multipla_escolha" in dados_exercicios:
        for i, questao in enumerate(dados_exercicios["questoes_multipla_escolha"]):
            with st.container(border=True):
                st.markdown(f"#### Questão {i+1} (Múltipla Escolha)")
                st.markdown(questao.get("enunciado", ""))
                
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência RAG: {ref}*")
                
                # Renderização Plotly se existir
                codigo_plotly = questao.get("codigo_plotly")
                if codigo_plotly:
                    try:
                        local_vars = {"go": go, "np": np, "stats": stats}
                        exec(codigo_plotly, {}, local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"fig_mcq_{i}")
                    except Exception as e:
                        st.warning("Visualização interativa indisponível.")
    
                # Alternativas
                opcoes = questao.get("alternativas", {})
                selecao = st.radio(
                    "Escolha uma alternativa:",
                    options=list(opcoes.keys()),
                    format_func=lambda x: f"{x}: {opcoes[x]}",
                    key=f"radio_mcq_{i}"
                )
                
                if st.button("✅ Confirmar Resposta", key=f"btn_mcq_{i}"):
                    if selecao == questao.get("alternativa_correta"):
                        st.success("🎉 Correto! Resposta excelente.")
                        st.session_state.respostas_certas[f"mcq_{i}"] = True
                    else:
                        st.error("❌ Resposta Incorreta. Reveja os conceitos e tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
                    st.rerun()
                
                if st.button("💡 Ver Dica", key=f"dica_mcq_{i}"):
                    st.info(questao.get("dica", "Sem dica disponível."))
                
                with st.expander("🔍 Ver Gabarito Comentado e Explicação"):
                    st.markdown(questao.get("gabarito_comentado", ""))
    
    # --- Seção de Questões Discursivas ---
    if "questoes_discursivas" in dados_exercicios:
        for i, questao in enumerate(dados_exercicios["questoes_discursivas"]):
            with st.container(border=True):
                st.markdown(f"#### Questão {i+1} (Discursiva de Cálculo / Análise)")
                st.markdown(questao.get("enunciado", ""))
                
                if questao.get("referencia_livro"):
                    st.markdown(f"📖 *Referência RAG: {questao['referencia_livro']}*")
                
                # Execução Plotly se houver
                if questao.get("codigo_plotly"):
                    try:
                        local_vars = {"go": go, "np": np, "stats": stats}
                        exec(questao["codigo_plotly"], {}, local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"fig_disc_{i}")
                    except:
                        pass
    
                st.text_area("Sua Resposta em Prosa / Raciocínio:", key=f"text_disc_{i}")
                
                valor_esperado = questao.get("resposta_numerica_esperada")
                if valor_esperado is not None:
                    valor_aluno = st.number_input("Digite o resultado numérico exato calculado para validação automática:", format="%.4f", key=f"num_disc_{i}")
                    if st.button("Validar Cálculo Numérico", key=f"btn_val_disc_{i}"):
                        if abs(valor_aluno - valor_esperado) <= max(0.01, 0.01 * abs(valor_esperado)):
                            st.success("🎉 Resultado Numérico Correto! Cálculo impecável.")
                            st.session_state.respostas_certas[f"disc_{i}"] = True
                            st.rerun()
                        else:
                            st.error("❌ O valor calculado difere do gabarito oficial. Confira as substituições numéricas!")
                            st.session_state.respostas_certas[f"disc_{i}"] = False
                else:
                    if st.checkbox("Marque aqui após estudar e responder este desafio", key=f"check_disc_{i}"):
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                    else:
                        st.session_state.respostas_certas[f"disc_{i}"] = False
                
                with st.expander("✅ Ver Resolução Detalhada Passo a Passo"):
                    for passo in questao.get("gabarito_passo_a_passo", []):
                        st.markdown(f"- {passo}")
