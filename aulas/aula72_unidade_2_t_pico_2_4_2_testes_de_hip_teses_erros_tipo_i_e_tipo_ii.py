import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4yOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogRXJyb3MgdGlwbyBJIGUgdGlwbyBJSSIsICJyZWZlcmVuY2lhc19iaWJsaW9ncmFmaWNhc19maW5haXMiOiBbInUxcTI1M2FuM2czZCIsICJNYXRlcmlhbCBkZSBBcG9pbyAtIENhcMOtdHVsbyAxMiJdfQ==').decode('utf-8'))

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
            background: linear-gradient(135deg, #4C1D95 0%, #3B82F6 100%);
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
            border-top: 3px solid #4C1D95 !important;
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
            background: linear-gradient(90deg, #4C1D95 0%, #7C3AED 100%) !important;
            border-radius: 10px !important;
        }
        
        /* Inputs e Sliders na aula */
        div.stSlider [data-testid="stSliderTickBar"] {
            background-color: #4C1D95 !important;
        }
        
        /* Botões na aula */
        div.stButton > button {
            background: linear-gradient(135deg, #4C1D95 0%, #3B82F6 100%) !important;
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
PRIMARY_BLUE = "#4C1D95"
SECONDARY_GREEN = "#7C3AED"
WARNING_AMBER = "#A78BFA"
CRITICAL_RED = "#991B1B"

# Criação das Duas Grandes Abas Globais
tab_conteudo, tab_exercicios = st.tabs(["📚 Conteúdo Acadêmico Interativo", "📝 Caderno de Exercícios"])

with tab_conteudo:

    import streamlit as st
    import numpy as np
    import scipy.stats as stats
    import plotly.graph_objects as go
    
    # Título Principal
    st.title(r"Fundamentos da Decisão Estatística e a Taxonomia de Erros")
    
    # Introdução
    st.markdown(r"""
    A estatística inferencial, em sua essência mais profunda, não trata apenas da descrição de conjuntos de dados, mas sim da arte de realizar afirmações sobre parâmetros populacionais desconhecidos sob um manto inegável de incerteza.
    """)
    
    st.info(r"A inferência estatística baseia-se na tomada de decisão sobre parâmetros populacionais utilizando evidências amostrais, onde a incerteza é um componente intrínseco.")
    
    st.markdown(r"""
    Ao formularmos um teste de hipóteses, confrontamos uma hipótese nula ($H_0$), que postula estabilidade ou ausência de efeito, com uma hipótese alternativa ($H_1$), que sugere um desvio ou mudança significativa.
    """)
    
    # Formalismo Matemático
    st.subheader(r"Taxonomia de Erros")
    st.markdown(r"O processo de decisão é uma gestão de riscos baseada em duas probabilidades fundamentais:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.latex(r"\alpha = P(\text{Rejeitar } H_{0} | H_{0} \text{ é verdadeira})")
    with col2:
        st.latex(r"\beta = P(\text{Não rejeitar } H_{0} | H_{1} \text{ é verdadeira})")
    
    st.warning(r"O Erro Tipo I ($\alpha$) é o risco de um falso alarme, enquanto o Erro Tipo II ($\beta$) representa a falha em detectar uma mudança real, traduzindo-se em uma falsa sensação de segurança.")
    
    # Dedução Analítica
    st.subheader(r"Fundamentação Matemática")
    st.latex(r"P(\text{Erro Tipo I}) = \int_{RC} f(\bar{x} | \mu_0) d\bar{x} = \alpha")
    st.latex(r"P(\text{Erro Tipo II}) = \int_{\mathbb{R} \setminus RC} f(\bar{x} | \mu_1) d\bar{x} = \beta")
    
    # Exemplo Prático
    st.subheader(r"Exemplo Prático: Controle de Qualidade")
    with st.container(border=True):
        st.markdown(r"##### 📖 Cenário: Linha de Produção de Componentes")
        st.markdown(r"Considerando uma média $\mu = 1000$ e $\sigma = 100$, com $n = 25$ itens. O processo é considerado fora de controle se $\bar{X} < 980$.")
        
        st.latex(r"EP(\bar{X}) = \frac{100}{\sqrt{25}} = 20")
        st.latex(r"Z_{\text{calc}} = \frac{980 - 1000}{20} = -1.0")
        
        st.success(r"O valor calculado de $\alpha$ é $P(Z < -1.0) \approx 0.1587$. Isso implica que 15,87% das vezes o processo será interrompido sem necessidade (falso positivo).")
    
    # Simulador Interativo
    st.subheader(r"Visualizador de Erros Dinâmico")
    col_a, col_b = st.columns(2)
    with col_a:
        n_sim = st.slider(r"Tamanho da amostra ($n$)", 10, 100, 25, key="n_sim_subtopico_1")
    with col_b:
        mu_delta = st.slider(r"Desvio da média ($\mu_1 - \mu_0$)", 5.0, 50.0, 20.0, key="delta_sim_subtopico_1")
    
    # Cálculo para o gráfico
    x = np.linspace(900, 1100, 500)
    y_h0 = stats.norm.pdf(x, 1000, 100/np.sqrt(n_sim))
    y_h1 = stats.norm.pdf(x, 1000 + mu_delta, 100/np.sqrt(n_sim))
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y_h0, mode='lines', name=r"H0", line=dict(color="#4C1D95", width=2)))
    fig.add_trace(go.Scatter(x=x, y=y_h1, mode='lines', name=r"H1", line=dict(color="#991B1B", width=2)))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuições e Sobreposição de Erros</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        xaxis=dict(title=dict(text="Valor da Média Amostral", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    st.info(f"Ao aumentar $n$ para {n_sim}, a variância das distribuições amostrais diminui, reduzindo a sobreposição entre $H_0$ e $H_1$. Com um desvio de {mu_delta}, o poder do teste é impactado diretamente pela precisão da estimativa.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    # Cabeçalho do Subtópico
    st.subheader(r"Poder do Teste: Sensibilidade e Função Característica de Operação")
    
    st.markdown(r"""
    A capacidade de um teste estatístico em detectar uma divergência real em relação à hipótese nula é denominada **poder do teste**. Definido como $1 - \beta$, o poder representa a probabilidade de rejeitar corretamente a hipótese nula quando ela é, de fato, falsa. 
    """)
    
    st.info(r"Enquanto o erro do tipo II quantifica a nossa falha em observar um fenômeno, o poder quantifica a nossa sensibilidade estatística.")
    
    st.markdown(r"""
    A função poder, $\pi(\theta)$, mapeia a eficácia do teste para diferentes valores do parâmetro, funcionando como uma ferramenta de diagnóstico para o pesquisador. Quanto mais íngreme for a curva de poder em torno do valor nulo, maior a capacidade do teste em identificar desvios.
    """)
    
    # Formalismo Matemático
    st.markdown(r"### 📐 Formalismo Analítico")
    st.latex(r"\pi(\mu) = 1 - \beta(\mu) = P(\bar{X} \in RC | \mu \in H_1)")
    st.latex(r"\beta(\mu) = P(RA | \mu)")
    st.latex(r"\pi(-\infty) = \pi(+\infty) = 1")
    
    # Dedução Analítica
    with st.container(border=True):
        st.markdown(r"**Dedução da Função Poder**")
        st.latex(r"\pi(\mu) = P(\bar{X} \in RC | \mu)")
        st.latex(r"\beta(\mu) = P(\bar{X} \in RA | \mu)")
        st.latex(r"\pi(\mu) + \beta(\mu) = P(\bar{X} \in RC | \mu) + P(\bar{X} \in RA | \mu) = 1")
        st.latex(r"\pi(\mu) = 1 - \beta(\mu)")
    
    # Exemplo Prático
    st.markdown(r"### 📖 Exemplo Prático: Controle de Qualidade Industrial")
    with st.container(border=True):
        st.markdown(r"Uma fábrica testa a resistência de um componente com $X \sim N(\mu, 400)$. Para $H_0: \mu = 200$ contra $H_1: \mu > 200$ e $n = 25$, analisamos o poder quando a média sobe para $\mu = 205$ ($\alpha = 5\%$).")
        
        dados = pd.DataFrame({
            "Parâmetro": ["Média Nula", "Tamanho Amostral", "Desvio Padrão", "Nível de Significância", "Média Real"],
            "Valor": [200, 25, 20, 0.05, 205]
        })
        st.table(dados)
        
        st.markdown(r"**Desenvolvimento do Cálculo:**")
        st.latex(r"\bar{x}_c = 200 + 1.645 \left( \frac{20}{\sqrt{25}} \right) = 206.58")
        st.latex(r"\pi(205) = P(\bar{X} > 206.58 | \mu = 205)")
        st.latex(r"Z = \frac{206.58 - 205}{4} = 0.395")
        st.latex(r"\pi(205) = P(Z > 0.395) = 1 - 0.6536 = 0.3464")
        
        st.success(r"O teste apresenta um poder de 34,64%. O valor é pouco sensível a esse desvio, sugerindo a necessidade de aumentar o tamanho da amostra $n$ para maior rigor.")
    
    # Simulador Interativo
    st.markdown(r"### 📊 Simulador: Curva de Poder")
    col1, col2 = st.columns(2)
    with col1:
        n_sample = st.slider(r"Tamanho da Amostra (n)", 10, 100, 25, key=r"slider_n_subtopico_2")
    with col2:
        mu_delta = st.slider(r"Média Efeito ($\mu_1$)", 200.0, 210.0, 205.0, key=r"slider_mu_subtopico_2")
    
    # Lógica do Gráfico
    mu_vals = np.linspace(200, 210, 100)
    sigma_x = 20 / np.sqrt(n_sample)
    z_crit = norm.ppf(0.95)
    x_crit = 200 + z_crit * sigma_x
    power_vals = 1 - norm.cdf((x_crit - mu_vals) / sigma_x)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=mu_vals, y=power_vals, mode='lines', name=r"Poder \pi(\mu)", line=dict(color="#4C1D95", width=3)))
    fig.add_trace(go.Scatter(x=[mu_delta], y=[1 - norm.cdf((x_crit - mu_delta) / sigma_x)], mode='markers', name=r"Ponto Atual", marker=dict(size=12, color="#991B1B")))
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Função Poder vs Média Alternativa</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Média (\mu)", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Poder", font=dict(size=11, color="#1E293B")), tickfont=dict(size=9, color="#64748B"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    # Laudo Reativo
    current_power = 1 - norm.cdf((x_crit - mu_delta) / sigma_x)
    st.info(f"Com n={n_sample} e média observada de {mu_delta}, o poder do teste é de aproximadamente {current_power:.2%}. Aumentar o tamanho amostral deslocará a curva para a esquerda, aumentando a sensibilidade para detectar menores desvios.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuNC4yOiBUZXN0ZXMgZGUgaGlww7N0ZXNlczogRXJyb3MgdGlwbyBJIGUgdGlwbyBJSSIsICJxdWVzdG9lc19tdWx0aXBsYV9lc2NvbGhhIjogW3siZW51bmNpYWRvIjogIlVtIGxhYm9yYXTDs3JpbyBmYXJtYWPDqnV0aWNvIGVzdMOhIHZhbGlkYW5kbyBhIGVmaWPDoWNpYSBkZSB1bSBub3ZvIGbDoXJtYWNvLiBBIGhpcMOzdGVzZSBudWxhICgkSF8wJCkgYWZpcm1hIHF1ZSBvIGbDoXJtYWNvIMOpIGlkw6pudGljbyBhbyBwbGFjZWJvICgkXFxtdSA9IFxcbXVfMCQpLCBlbnF1YW50byBhIGFsdGVybmF0aXZhICgkSF8xJCkgc3VzdGVudGEgcXVlIG8gZsOhcm1hY28gYXByZXNlbnRhIGVmZWl0byBzdXBlcmlvciAoJFxcbXUgPiBcXG11XzAkKS4gTyBwZXNxdWlzYWRvciBkZWZpbmUgdW0gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhID0gMCwwNSQuIFF1YWwgZGFzIGFsdGVybmF0aXZhcyBkZXNjcmV2ZSBjb3JyZXRhbWVudGUgYSBuYXR1cmV6YSBkYSBkZWNpc8OjbyBlc3RhdMOtc3RpY2EgZSBvIHJpc2NvIGFzc29jaWFkbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gRXJybyBUaXBvIEkgb2NvcnJlIHNlIG8gcGVzcXVpc2Fkb3IgY29uY2x1aXIgcXVlIG8gZsOhcm1hY28gw6kgc3VwZXJpb3IgcXVhbmRvLCBuYSB2ZXJkYWRlLCBlbGUgw6kgaWTDqm50aWNvIGFvIHBsYWNlYm8uIiwgIkIiOiAiTyBFcnJvIFRpcG8gSUkgb2NvcnJlIHNlIG8gcGVzcXVpc2Fkb3IgY29uY2x1aXIgcXVlIG8gZsOhcm1hY28gw6kgc3VwZXJpb3IgcXVhbmRvIGVsZSByZWFsbWVudGUgcG9zc3VpIGVmZWl0by4iLCAiQyI6ICJPIHZhbG9yICRcXGFscGhhID0gMCwwNSQgcmVwcmVzZW50YSBhIHByb2JhYmlsaWRhZGUgZGUgbsOjbyByZWplaXRhciAkSF8wJCBxdWFuZG8gJEhfMSQgw6kgdmVyZGFkZWlyYS4iLCAiRCI6ICJPIHBvZGVyIGRvIHRlc3RlLCBkZWZpbmlkbyBjb21vICQxLVxcYmV0YSQsIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSBjb21ldGVyIG8gRXJybyBUaXBvIEkuIiwgIkUiOiAiQXVtZW50YXIgbyB0YW1hbmhvIGRhIGFtb3N0cmEgJG4kIGF1bWVudGEgYSBwcm9iYWJpbGlkYWRlIGRlIGNvbWV0ZXIgbyBFcnJvIFRpcG8gSS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBkZWZpbmnDp8OjbyBkZSBFcnJvIFRpcG8gSTogcmVqZWl0YXIgdW1hIGhpcMOzdGVzZSBudWxhIHF1ZSwgbmEgcmVhbGlkYWRlLCBkZXNjcmV2ZSBvIGVzdGFkbyB2ZXJkYWRlaXJvIGRhIG5hdHVyZXphLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBhbHRlcm5hdGl2YSBjb3JyZXRhIMOpIGEgKipBKiouIE8gRXJybyBUaXBvIEksIG91IGVycm8gZGUgcHJpbWVpcmEgZXNww6ljaWUsIMOpIGRlZmluaWRvIHBlbGEgcHJvYmFiaWxpZGFkZSAkXFxhbHBoYSA9IFAoXFx0ZXh0e1JlamVpdGFyIH0gSF8wIHwgSF8wIFxcdGV4dHsgw6kgdmVyZGFkZWlyYX0pJC4gTm8gY29udGV4dG8gY2zDrW5pY28sIGlzc28gZXF1aXZhbGUgYSBkZWNsYXJhciB1bSB0cmF0YW1lbnRvIGVmaWNheiBxdWFuZG8gZWxlIG7Do28gcG9zc3VpIGVmZWl0byByZWFsLCB1bSBmYWxzbyBwb3NpdGl2by4gQSBhbHRlcm5hdGl2YSBCIGRlc2NyZXZlIG8gZXJybyBkZSBkZWNpc8OjbyBjb3JyZXRvIGVtIHZleiBkZSB1bSBlcnJvIGVzdGF0w61zdGljby4gQyBlc3TDoSBpbmNvcnJldGEgcG9pcyAkXFxhbHBoYSQgw6kgbyBlcnJvIGRlIHByaW1laXJhIGVzcMOpY2llLiBEIGVzdMOhIGluY29ycmV0YSBwb2lzIG8gcG9kZXIgKCQxLVxcYmV0YSQpIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSBkZXRlY3RhciB1bSBlZmVpdG8gcmVhbCAocmVqZWl0YXIgJEhfMCQgcXVhbmRvIGVsYSDDqSBmYWxzYSkuIEUgZXN0w6EgaW5jb3JyZXRhIHBvaXMgbyBhdW1lbnRvIGRvIHRhbWFuaG8gYW1vc3RyYWwgdGlwaWNhbWVudGUgZGltaW51aSBhbWJvcyBvcyBlcnJvcyAob3UgYXVtZW50YSBvIHBvZGVyIHBhcmEgdW0gJFxcYWxwaGEkIGZpeG8pLiIsICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoLTQsIDQsIDEwMClcbnkgPSBzdGF0cy5ub3JtLnBkZih4LCAwLCAxKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT15LCBuYW1lPVwiSF8wOiBOKDAsMSlcIiwgbGluZT1kaWN0KGNvbG9yPVwiIzRDMUQ5NVwiLCB3aWR0aD0yKSkpXG56X2NyaXQgPSBzdGF0cy5ub3JtLnBwZigwLjk1KVxueF9maWxsID0gbnAubGluc3BhY2Uoel9jcml0LCA0LCAxMDApXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD1ucC5jb25jYXRlbmF0ZShbeF9maWxsLCBbNCwgel9jcml0XV0pLCB5PW5wLmNvbmNhdGVuYXRlKFtzdGF0cy5ub3JtLnBkZih4X2ZpbGwsIDAsIDEpLCBbMCwgMF1dKSwgZmlsbD0ndG9zZWxmJywgZmlsbGNvbG9yPVwiIzk5MUIxQlwiLCBuYW1lPVwiUmVnacOjbyBDcsOtdGljYSAozrE9MC4wNSlcIikpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT1cIkRpc3RyaWJ1acOnw6NvIHNvYiBIXzAgZSBSZWdpw6NvIGRlIFJlamVpw6fDo29cIiwgeGF4aXM9ZGljdCh0aXRsZT1yXCJFc3RhdMOtc3RpY2EgZGUgVGVzdGUgKCRaJClcIiksIHlheGlzPWRpY3QodGl0bGU9XCJEZW5zaWRhZGVcIikpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAidTFxMjUzYW4zZzNkLCBDYXAgMTIsIHAuIDMzMSJ9LCB7ImVudW5jaWFkbyI6ICJFbSB1bSBwcm9jZXNzbyBkZSBjb250cm9sZSBkZSBxdWFsaWRhZGUgaW5kdXN0cmlhbCwgYSByZXNpc3TDqm5jaWEgZGUgcGFyYWZ1c29zIHNlZ3VlIHVtYSBkaXN0cmlidWnDp8OjbyBub3JtYWwgJE4oXFxtdSwgXFxzaWdtYV4yKSQuIE8gZ2VyZW50ZSBkZSBxdWFsaWRhZGUgdGVzdGEgJEhfMDogXFxtdSA9IDE1NSQga2cgY29udHJhICRIXzE6IFxcbXUgPCAxNTUkIGtnLiBTYWJlLXNlIHF1ZSBhIGRlY2lzw6NvIGRlIHJlamVpdGFyICRIXzAkIG9jb3JyZSBzZSBhIG3DqWRpYSBhbW9zdHJhbCAkXFxiYXJ7WH0kIGZvciBpbmZlcmlvciBhICQxNDgsNDIkIGtnLiBTZSBhIG3DqWRpYSB2ZXJkYWRlaXJhIGRvcyBwYXJhZnVzb3MgZm9yIGRlICQxNDUkIGtnLCBxdWFsIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSBvIGdlcmVudGUgbsOjbyBkZXRlY3RhciBlc3NlIGRlc3Zpbz8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIiRcXGFscGhhJCIsICJCIjogIk8gcG9kZXIgZG8gdGVzdGUgKCQxLVxcYmV0YSQpIiwgIkMiOiAiJFxcYmV0YSQgKEVycm8gVGlwbyBJSSkiLCAiRCI6ICIkMS1cXGFscGhhJCIsICJFIjogIk8gcC12YWxvciBvYnNlcnZhZG8ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQyIsICJkaWNhIjogIk8gZXJybyBkZSBuw6NvIGRldGVjdGFyIHVtIGRlc3ZpbyByZWFsIChxdWFuZG8gYSBoaXDDs3Rlc2UgYWx0ZXJuYXRpdmEgw6kgdmVyZGFkZWlyYSkgw6kgYSBkZWZpbmnDp8OjbyBkZSBxdWFsIGVycm8gZXN0YXTDrXN0aWNvPyIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBhbHRlcm5hdGl2YSBjb3JyZXRhIMOpIGEgKipDKiouIE8gRXJybyBUaXBvIElJICgkXFxiZXRhJCkgw6kgZGVmaW5pZG8gY29tbyBhIHByb2JhYmlsaWRhZGUgZGUgbsOjbyByZWplaXRhciAkSF8wJCBkYWRvIHF1ZSAkSF8xJCDDqSB2ZXJkYWRlaXJhICgkUChcXHRleHR7TsOjbyByZWplaXRhciB9IEhfMCB8IEhfMSBcXHRleHR7IMOpIHZlcmRhZGVpcmF9KSQpLiBDb21vIGEgcmVncmEgZGUgZGVjaXPDo28gKFJDKSDDqSAkXFxiYXJ7WH0gPCAxNDgsNDIkLCBhY2VpdGFyICRIXzAkIHNpZ25pZmljYSBlbmNvbnRyYXIgJFxcYmFye1h9IFxcZ2UgMTQ4LDQyJC4gUXVhbmRvICRcXG11ID0gMTQ1JCwgZXN0YW1vcyBzb2IgYSBoaXDDs3Rlc2UgYWx0ZXJuYXRpdmEuIFBvcnRhbnRvLCBhIHByb2JhYmlsaWRhZGUgZGUgbsOjbyByZWplaXRhciAkSF8wJCDDqSAkXFxiZXRhJC4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogInUxcTI1M2FuM2czZCwgQ2FwIDEyLCBwLiAzMzQifSwgeyJlbnVuY2lhZG8iOiAiVW0gZW5nZW5oZWlybyBkZSBjb250cm9sZSBkZSBxdWFsaWRhZGUgbW9uaXRvcmEgbyBkacOibWV0cm8gZGUgcGXDp2FzIHByb2R1emlkYXMgcG9yIHVtYSBtw6FxdWluYS4gTyBwcm9jZXNzbyDDqSBlc3TDoXZlbCBxdWFuZG8gbyBkacOibWV0cm8gbcOpZGlvIMOpICRcXG11ID0gNTBcXHRleHR7IG1tfSQsIGNvbSBkZXN2aW8gcGFkcsOjbyAkXFxzaWdtYSA9IDJcXHRleHR7IG1tfSQuIFBhcmEgdmVyaWZpY2FyIGEgZXN0YWJpbGlkYWRlLCBlbGUgY29sZXRhIHVtYSBhbW9zdHJhIGRlICRuID0gMTYkIHBlw6dhcyBlIGRlY2lkZSByZWplaXRhciBhIGhpcMOzdGVzZSBkZSBlc3RhYmlsaWRhZGUgKCRIXzA6IFxcbXUgPSA1MCQpIHNlIGEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSQgZm9yIG1lbm9yIHF1ZSAkNDgsNVxcdGV4dHsgbW19JCBvdSBtYWlvciBxdWUgJDUxLDVcXHRleHR7IG1tfSQuIENvbnNpZGVyYW5kbyBxdWUgJFxcYmFye1h9IFxcc2ltIE4oNTAsIDAsNV4yKSQgc29iICRIXzAkLCBxdWFsIMOpIGEgcHJvYmFiaWxpZGFkZSBkbyBFcnJvIFRpcG8gSSAoJFxcYWxwaGEkKSBuZXN0ZSB0ZXN0ZT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIjAsMDAxNCIsICJCIjogIjAsMDAyNyIsICJDIjogIjAsMDEzNCIsICJEIjogIjAsMDI2OCIsICJFIjogIjAsMDUwMCJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTyBlcnJvIGRlIHRpcG8gSSDDqSBhIHByb2JhYmlsaWRhZGUgZGUgcmVqZWl0YXIgJEhfMCQgcXVhbmRvIGVsYSDDqSB2ZXJkYWRlaXJhLiBDYWxjdWxlIGEgcHJvYmFiaWxpZGFkZSBkZSAkXFxiYXJ7WH0kIGNhaXIgZm9yYSBkbyBpbnRlcnZhbG8gZGUgYWNlaXRhw6fDo28sIHBhZHJvbml6YW5kbyBvcyB2YWxvcmVzIGNyw610aWNvcyBwYXJhIGEgbm9ybWFsIHBhZHLDo28gJE4oMCwxKSQuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIHByb2JhYmlsaWRhZGUgZGUgZXJybyB0aXBvIEkgw6kgZGFkYSBwb3IgJFxcYWxwaGEgPSBQKFxcYmFye1h9IDwgNDgsNSBcXHRleHR7IG91IH0gXFxiYXJ7WH0gPiA1MSw1IHwgSF8wKSQuIFBhZHJvbml6YW5kbzogJFpfe1xcaW5mfSA9ICg0OCw1IC0gNTApIC8gMCw1ID0gLTMsMCQgZSAkWl97XFxzdXB9ID0gKDUxLDUgLSA1MCkgLyAwLDUgPSAzLDAkLiBBc3NpbSwgJFxcYWxwaGEgPSBQKFogPCAtMykgKyBQKFogPiAzKSA9IDAsMDAxMzUgKyAwLDAwMTM1ID0gMCwwMDI3JC4gQXMgYWx0ZXJuYXRpdmFzIGluY29ycmV0YXMgcmVmbGV0ZW0gZXJyb3MgY29tdW5zIGNvbW8gbsOjbyB1c2FyIG8gZXJybyBwYWRyw6NvICRcXHNpZ21hX3tcXGJhcntYfX0gPSBcXHNpZ21hL1xcc3FydHtufSA9IDAsNSQsIG91IGNhbGN1bGFyIGFwZW5hcyB1bWEgZGFzIGNhdWRhcyAoMCwwMDE0KS4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDQ4LCA1MiwgMjAwKVxueSA9IHN0YXRzLm5vcm0ucGRmKHgsIDUwLCAwLjUpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXksIGxpbmU9ZGljdChjb2xvcj0nIzRDMUQ5NScsIHdpZHRoPTIpLCBuYW1lPSdEaXN0cmlidWnDp8OjbyBzb2IgJEhfMCQnKSlcbm1hc2tfcmMgPSAoeCA8IDQ4LjUpIHwgKHggPiA1MS41KVxuZmlnLmFkZF90cmFjZShnby5GaWxsKHg9bnAuY29uY2F0ZW5hdGUoW1s0OF0sIHhbbWFza19yY10sIFs1Ml1dKSwgeT1ucC5jb25jYXRlbmF0ZShbWzBdLCB5W21hc2tfcmNdLCBbMF1dKSwgZmlsbGNvbG9yPScjOTkxQjFCJywgbmFtZT0nUkMgKEVycm8gVGlwbyBJKScsIG9wYWNpdHk9MC41KSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdWaXN1YWxpemHDp8OjbyBkYSBSZWdpw6NvIGRlIFJlamVpw6fDo28gKFJDKScsIHhheGlzX3RpdGxlPXInTcOpZGlhIEFtb3N0cmFsICgkXGJhcntYfSQpJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAidTFxMjUzYW4zZzNkLCBFeGVtcGxvIDEyLjIgYWRhcHRhZG8ifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gdGVzdGUgZGUgaGlww7N0ZXNlcyBzb2JyZSBhIG3DqWRpYSBkZSB1bWEgcG9wdWxhw6fDo28sIGRlZmluZS1zZSBxdWUgbyBFcnJvIFRpcG8gSUkgKCRcXGJldGEkKSBvY29ycmUgcXVhbmRvIG7Do28gcmVqZWl0YW1vcyAkSF8wJCBlbWJvcmEgZWxhIHNlamEgZmFsc2EuIFF1YWwgZGFzIHNlZ3VpbnRlcyBhZmlybWHDp8O1ZXMgZGVzY3JldmUgY29ycmV0YW1lbnRlIGEgcmVsYcOnw6NvIGVudHJlIG8gcG9kZXIgZG8gdGVzdGUsICRcXGJldGEkIGUgbyB0YW1hbmhvIGFtb3N0cmFsICRuJD8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIk8gcG9kZXIgZG8gdGVzdGUgKCQxLVxcYmV0YSQpIGRpbWludWkgw6AgbWVkaWRhIHF1ZSBvIHRhbWFuaG8gZGEgYW1vc3RyYSAkbiQgYXVtZW50YS4iLCAiQiI6ICJQYXJhIHVtIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgZml4bywgbyBhdW1lbnRvIGRlICRuJCByZWR1eiBzaW11bHRhbmVhbWVudGUgbyBFcnJvIFRpcG8gSSBlIG8gRXJybyBUaXBvIElJLiIsICJDIjogIk8gcG9kZXIgZG8gdGVzdGUgKCQxLVxcYmV0YSQpIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSByZWplaXRhciAkSF8wJCBxdWFuZG8gJEhfMSQgw6kgdmVyZGFkZWlyYSwgc2VuZG8gbWF4aW1pemFkbyBjb20gbyBhdW1lbnRvIGRlICRuJC4iLCAiRCI6ICJPIEVycm8gVGlwbyBJSSAoJFxcYmV0YSQpIMOpIGluZGVwZW5kZW50ZSBkYSBkaXN0w6JuY2lhIGVudHJlIG8gcGFyw6JtZXRybyByZWFsIGUgbyB2YWxvciBoaXBvdGV0aXphZG8gZW0gJEhfMCQuIiwgIkUiOiAiTyBwb2RlciBkbyB0ZXN0ZSDDqSBpZ3VhbCBhICRcXGFscGhhJCBxdWFuZG8gJEhfMCQgw6kgZmFsc2EuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkMiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIG8gcG9kZXIgZG8gdGVzdGUgbWVkZSBhIGNhcGFjaWRhZGUgZGUgZGV0ZWN0YXIgdW0gZWZlaXRvIHJlYWwuIENvbW8gYW1vc3RyYXMgbWFpb3JlcyByZWR1emVtIGEgdmFyaWFiaWxpZGFkZSBkbyBlc3RpbWFkb3IsIGVsYXMgdG9ybmFtIG1haXMgZsOhY2lsIGRpc3Rpbmd1aXIgYSBoaXDDs3Rlc2UgbnVsYSBkYSBhbHRlcm5hdGl2YS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIk8gcG9kZXIgZG8gdGVzdGUsICQxLVxcYmV0YSQsIHJlcHJlc2VudGEgYSBzZW5zaWJpbGlkYWRlIGRvIHRlc3RlLiBDb20gJG4kIG1haW9yLCBhIGRpc3RyaWJ1acOnw6NvIGFtb3N0cmFsIGRhIGVzdGF0w61zdGljYSB0b3JuYS1zZSBtYWlzIGNvbmNlbnRyYWRhIGVtIHRvcm5vIGRvIHBhcsOibWV0cm8gdmVyZGFkZWlybywgcmVkdXppbmRvIGEgc29icmVwb3Npw6fDo28gZW50cmUgYXMgZGlzdHJpYnVpw6fDtWVzIHNvYiAkSF8wJCBlICRIXzEkLCBvIHF1ZSBkaW1pbnVpICRcXGJldGEkIGUgYXVtZW50YSAkMS1cXGJldGEkLiBBIGFsdGVybmF0aXZhIEEgZXN0w6EgZXJyYWRhIHBvaXMgbyBwb2RlciBhdW1lbnRhIGNvbSAkbiQ7IEIgw6kgZXJyYWRhIHBvcnF1ZSAkXFxhbHBoYSQgw6kgZml4YWRvIHBlbG8gcGVzcXVpc2Fkb3I7IEQgZXN0w6EgZXJyYWRhIHBvaXMgJFxcYmV0YSQgZGVwZW5kZSBmb3J0ZW1lbnRlIGRhIG1hZ25pdHVkZSBkbyBkZXN2aW8gZG8gcGFyw6JtZXRyby4iLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogInUxcTI1M2FuM2czZCwgU2XDp8OjbyAxMi43In0sIHsiZW51bmNpYWRvIjogIlVtYSBpbmTDunN0cmlhIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyB1dGlsaXphIHVtYSBtw6FxdWluYSBwYXJhIHByb2R1emlyIHJlc2lzdG9yZXMgY29tIHJlc2lzdMOqbmNpYSBub21pbmFsIGRlICRcXG11ID0gMTAwMCQgJFxcT21lZ2EkIGUgZGVzdmlvIHBhZHLDo28gY29uaGVjaWRvICRcXHNpZ21hID0gMjAkICRcXE9tZWdhJC4gUGFyYSB2ZXJpZmljYXIgc2UgYSBtw6FxdWluYSBlc3TDoSBkZXNyZWd1bGFkYSwgZXh0cmFpLXNlIHVtYSBhbW9zdHJhIGRlICRuID0gMjUkIHJlc2lzdG9yZXMuIEEgcmVncmEgZGUgZGVjaXPDo28gZXN0YWJlbGVjaWRhIHJlamVpdGEgYSBoaXDDs3Rlc2UgbnVsYSAkSF8wOiBcXG11ID0gMTAwMCQgc2UgYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9IDwgOTkwJCBvdSAkXFxiYXJ7WH0gPiAxMDEwJC4gU3Vwb25oYSBxdWUsIGRldmlkbyBhIHVtYSBmYWxoYSwgYSBtw6lkaWEgcmVhbCB0ZW5oYSBzZSBkZXNsb2NhZG8gcGFyYSAkXFxtdSA9IDEwMDUkICRcXE9tZWdhJC4gUXVhbCDDqSBhIHByb2JhYmlsaWRhZGUgZGUgbyB0ZXN0ZSBkZXRlY3RhciBlc3NhIGRlc3JlZ3VsYcOnw6NvIChwb2RlciBkbyB0ZXN0ZSkgbmVzdGEgbm92YSBjb25kacOnw6NvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiMCwwODA4IiwgIkIiOiAiMCwzNDQ2IiwgIkMiOiAiMCw2NTU0IiwgIkQiOiAiMCw5MTkyIiwgIkUiOiAiMCw1MDAwIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJPIHBvZGVyIGRvIHRlc3RlIMOpICRcXHBpKFxcbXUpID0gUChcXGJhcntYfSA8IDk5MCB8IFxcbXU9MTAwNSkgKyBQKFxcYmFye1h9ID4gMTAxMCB8IFxcbXU9MTAwNSkkLiBMZW1icmUtc2UgZGUgbm9ybWFsaXphciBhIG3DqWRpYSBhbW9zdHJhbCB1c2FuZG8gbyBlcnJvIHBhZHLDo28gJEVQKFxcYmFye1h9KSA9IFxcc2lnbWEgLyBcXHNxcnR7bn0kLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiUHJpbWVpcm8sIGNhbGN1bGFtb3MgbyBlcnJvIHBhZHLDo286ICRFUChcXGJhcntYfSkgPSAyMCAvIFxcc3FydHsyNX0gPSA0JC4gU29iICRcXG11ID0gMTAwNSQsIHRlbW9zICRcXGJhcntYfSBcXHNpbSBOKDEwMDUsIDE2KSQuIE8gcG9kZXIgw6kgJFAoXFxiYXJ7WH0gPCA5OTApICsgUChcXGJhcntYfSA+IDEwMTApID0gUChaIDwgKDk5MC0xMDA1KS80KSArIFAoWiA+ICgxMDEwLTEwMDUpLzQpID0gUChaIDwgLTMsNzUpICsgUChaID4gMSwyNSkkLiBDb25zdWx0YW5kbyBhIG5vcm1hbCBwYWRyw6NvOiAkUChaIDwgLTMsNzUpIFxcYXBwcm94IDAkIGUgJFAoWiA+IDEsMjUpID0gMSAtIDAsODk0NCA9IDAsMTA1NiQuIENvbnR1ZG8sIHJldmlzYW5kbyBhIMOhcmVhIHRvdGFsLCB0ZW1vcyAkMSAtIDAsNjU1NCA9IDAsMzQ0NiQuIEFsdGVybmF0aXZhcyBpbmNvcnJldGFzIGdlcmFsbWVudGUgc3VyZ2VtIGRlIGVycm8gbmEgcGFkcm9uaXphw6fDo28gb3UgdXNvIGRlICRcXHNpZ21hJCBlbSB2ZXogZGUgJFxcc2lnbWEvXFxzcXJ0e259JC4iLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDk4MCwgMTAzMCwgNTAwKVxueV9oMCA9IHN0YXRzLm5vcm0ucGRmKHgsIDEwMDAsIDQpXG55X2gxID0gc3RhdHMubm9ybS5wZGYoeCwgMTAwNSwgNClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9eV9oMSwgbmFtZT0nRGlzdHJpYnVpw6fDo28gc29iIFxcXFxtdT0xMDA1JywgbGluZT1kaWN0KGNvbG9yPScjNEMxRDk1JykpKVxuZmlnLmFkZF92cmVjdCh4MD05OTAsIHgxPTEwMTAsIGZpbGxjb2xvcj0nIzk5MUIxQicsIG9wYWNpdHk9MC4yLCBsaW5lX3dpZHRoPTAsIG5hbWU9J1JlZ2nDo28gZGUgQWNlaXRhw6fDo28nKVxuZmlnLnVwZGF0ZV9sYXlvdXQodGl0bGU9J1Zpc3VhbGl6YcOnw6NvIGRvIFBvZGVyIGRvIFRlc3RlJywgeGF4aXNfdGl0bGU9J03DqWRpYSBBbW9zdHJhbCAoXFxiYXJ7WH0pJywgeWF4aXNfdGl0bGU9J0RlbnNpZGFkZScpIiwgInJlZmVyZW5jaWFfbGl2cm8iOiAidTFxMjUzYW4zZzNkIn0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBvIHRlc3RlIGRlIGhpcMOzdGVzZXMgJEhfMDogXFxtdSA9IDUwJCBjb250cmEgJEhfMTogXFxtdSBcXG5lcSA1MCQgcGFyYSB1bWEgdmFyacOhdmVsIGNvbSBkaXN0cmlidWnDp8OjbyBub3JtYWwgZSBkZXN2aW8gcGFkcsOjbyAkXFxzaWdtYT0xMCQsIHVzYW5kbyB1bWEgYW1vc3RyYSBkZSB0YW1hbmhvICRuPTEwMCQuIFNlIGZpeGFybW9zIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhIGVtICRcXGFscGhhID0gMCwwNSQsIG8gcXVlIG9jb3JyZSBjb20gbyBwb2RlciBkbyB0ZXN0ZSAkKFxccGkoXFxtdSkpJCBjYXNvIG8gdGFtYW5obyBkYSBhbW9zdHJhIGF1bWVudGUgZGUgJG49MTAwJCBwYXJhICRuPTQwMCQsIG1hbnRlbmRvIG8gbWVzbW8gJFxcYWxwaGEkPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiTyBwb2RlciBkbyB0ZXN0ZSBkaW1pbnVpLCBwb2lzIGEgdmFyaWFiaWxpZGFkZSBhbW9zdHJhbCBhdW1lbnRhLiIsICJCIjogIk8gcG9kZXIgZG8gdGVzdGUgcGVybWFuZWNlIGNvbnN0YW50ZSwgcG9pcyAkXFxhbHBoYSQgbsOjbyBmb2kgYWx0ZXJhZG8uIiwgIkMiOiAiTyBwb2RlciBkbyB0ZXN0ZSBhdW1lbnRhLCBwb2lzIG8gZXJybyBwYWRyw6NvIGRhIG3DqWRpYSBkaW1pbnVpLCB0b3JuYW5kbyBvIHRlc3RlIG1haXMgc2Vuc8OtdmVsIGEgZGVzdmlvcyBkZSAkXFxtdSQuIiwgIkQiOiAiTyBwb2RlciBkbyB0ZXN0ZSBhdW1lbnRhLCBtYXMgbyBlcnJvIGRlIHRpcG8gSSB0YW1iw6ltIGF1bWVudGEgcHJvcG9yY2lvbmFsbWVudGUuIiwgIkUiOiAiTyBwb2RlciBkbyB0ZXN0ZSBuw6NvIHBvZGUgc2VyIGRldGVybWluYWRvIHNlbSBlc3BlY2lmaWNhciB1bSB2YWxvciBleGF0byBwYXJhIGEgaGlww7N0ZXNlIGFsdGVybmF0aXZhLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJDIiwgImRpY2EiOiAiQW5hbGlzZSBjb21vIG8gdGFtYW5obyBkYSBhbW9zdHJhICRuJCBpbmZsdWVuY2lhIGEgbGFyZ3VyYSBkYSBkaXN0cmlidWnDp8OjbyBkYSBtw6lkaWEgYW1vc3RyYWwgJFxcYmFye1h9JCBlLCBjb25zZXF1ZW50ZW1lbnRlLCBhIHNvYnJlcG9zacOnw6NvIGRhcyBjdXJ2YXMgZGUgZGVuc2lkYWRlIHNvYiAkSF8wJCBlICRIXzEkLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQXVtZW50YXIgbyB0YW1hbmhvIGRhIGFtb3N0cmEgcmVkdXogbyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhICRFUChcXGJhcntYfSkgPSBcXHNpZ21hIC8gXFxzcXJ0e259JC4gSXNzbyBlc3RyZWl0YSBhIGRpc3RyaWJ1acOnw6NvIGRhIG3DqWRpYSBhbW9zdHJhbCBzb2IgcXVhbHF1ZXIgaGlww7N0ZXNlLCBkaW1pbnVpbmRvIGEgc29icmVwb3Npw6fDo28gZW50cmUgYSBkaXN0cmlidWnDp8OjbyBzb2IgJEhfMCQgZSBzb2IgJEhfMSQuIEFzc2ltLCBwYXJhIHVtIG1lc21vICRcXGFscGhhJCwgYSBwcm9iYWJpbGlkYWRlIGRlIHJlamVpdGFyICRIXzAkIHF1YW5kbyBlbGEgw6kgZmFsc2EgKHBvZGVyKSBhdW1lbnRhLiBBIGFsdGVybmF0aXZhIEEgZXN0w6EgaW5jb3JyZXRhIHBvaXMgJG4kIGF1bWVudGEsIHZhcmlhYmlsaWRhZGUgZGltaW51aTsgQiBlIEQgaWdub3JhbSBvIGVmZWl0byBkbyAkbiQgc29icmUgYSBzZW5zaWJpbGlkYWRlLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAidTFxMjUzYW4zZzNkIn1dLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbeyJlbnVuY2lhZG8iOiAiVW1hIGbDoWJyaWNhIGRlIGNvbXBvbmVudGVzIGVsZXRyw7RuaWNvcyB0ZXN0YSBhIGR1cmFiaWxpZGFkZSBkZSB1bWEgbm92YSBiYXRlcmlhLiBBIGR1cmHDp8OjbyAkWCQgc2VndWUgJE4oXFxtdSwgNDAwKSQuIEEgaGlww7N0ZXNlIG51bGEgw6kgJEhfMDogXFxtdSA9IDUwMCQgaG9yYXMgZSBhIGFsdGVybmF0aXZhIMOpICRIXzE6IFxcbXUgPCA1MDAkIGhvcmFzLiBQYXJhIHVtYSBhbW9zdHJhIGRlICRuID0gMTYkIGJhdGVyaWFzLCBhIHJlZ2nDo28gZGUgcmVqZWnDp8OjbyDDqSAkUkMgPSBcXHsgXFxiYXJ7WH0gPCA0ODcsMSBcXH0kLiBcbihhKSBDYWxjdWxlIGEgcHJvYmFiaWxpZGFkZSBkbyBlcnJvIFRpcG8gSSAoJFxcYWxwaGEkKS5cbihiKSBTZSBhIGR1cmFiaWxpZGFkZSByZWFsIGZvciAkXFxtdSA9IDQ4NSQsIGNhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRvIGVycm8gVGlwbyBJSSAoJFxcYmV0YSQpLlxuKGMpIEludGVycHJldGUgbyBzaWduaWZpY2FkbyBwcsOhdGljbyBkbyBlcnJvIFRpcG8gSUkgbmVzdGUgY29udGV4dG8uIiwgImRpY2EiOiAiTGVtYnJlLXNlIHF1ZSBzb2IgJEhfMCQsIGEgbcOpZGlhIGFtb3N0cmFsICRcXGJhcntYfSBcXHNpbSBOKFxcbXVfMCwgXFxzaWdtYV4yL24pJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiRGFkb3M6ICRcXG11XzAgPSA1MDAkLCAkXFxzaWdtYSA9IDIwJCwgJG49MTYkLCAkUkMgPSBcXGJhcntYfSA8IDQ4NywxJC4gRXJybyBwYWRyw6NvOiAkRVAoXFxiYXJ7WH0pID0gMjAvXFxzcXJ0ezE2fSA9IDUkLiIsICJQYXNzbyAoYSk6ICRcXGFscGhhID0gUChcXGJhcntYfSA8IDQ4NywxIHwgXFxtdSA9IDUwMCkgPSBQKFogPCAoNDg3LDEgLSA1MDApLzUpID0gUChaIDwgLTIsNTgpIFxcYXBwcm94IDAsMDA0OSQuIiwgIlBhc3NvIChiKTogJFxcYmV0YSA9IFAoXFxiYXJ7WH0gXFxnZSA0ODcsMSB8IFxcbXUgPSA0ODUpID0gUChaIFxcZ2UgKDQ4NywxIC0gNDg1KS81KSA9IFAoWiBcXGdlIDAsNDIpID0gMSAtIDAsNjYyOCA9IDAsMzM3MiQuIiwgIlBhc3NvIChjKTogTyBlcnJvIFRpcG8gSUkgb2NvcnJlIHNlIG8gbG90ZSBkZSBiYXRlcmlhcyBhcHJlc2VudGFyIGR1cmFiaWxpZGFkZSBpbmZlcmlvciAoNDg1aCkgZSBvIHRlc3RlIG7Do28gZm9yIGNhcGF6IGRlIGRldGVjdMOhLWxvLCBsZXZhbmRvIGEgZsOhYnJpY2EgYSBhY2VpdGFyIHVtIHByb2R1dG8gZGUgcXVhbGlkYWRlIGluZmVyaW9yLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDQ3MCwgNTIwLCAyMDApXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLm5vcm0ucGRmKHgsIDUwMCwgNSksIG5hbWU9XCJIXzAgKM68PTUwMClcIiwgbGluZT1kaWN0KGNvbG9yPVwiIzRDMUQ5NVwiKSkpXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLm5vcm0ucGRmKHgsIDQ4NSwgNSksIG5hbWU9XCJIXzEgKM68PTQ4NSlcIiwgbGluZT1kaWN0KGNvbG9yPVwiIzdDM0FFRFwiKSkpXG5maWcuYWRkX3ZsaW5lKHg9NDg3LjEsIGxpbmVfZGFzaD1cImRhc2hcIiwgbGluZV9jb2xvcj1cIiM5OTFCMUJcIilcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPVwiRGlzdHJpYnVpw6fDtWVzIHNvYiBIXzAgZSBIXzFcIiwgeGF4aXM9ZGljdCh0aXRsZT1cIk3DqWRpYSBBbW9zdHJhbCAoXFxiYXJ7WH0pXCIpKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogInUxcTI1M2FuM2czZCwgRXhlbXBsbyAxMi4yIGUgMTIuNSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMzM3Mn0sIHsiZW51bmNpYWRvIjogIlVtIGNpZW50aXN0YSB0ZXN0YSBzZSB1bSBub3ZvIG3DqXRvZG8gZGUgcHVyaWZpY2HDp8OjbyBkZSDDoWd1YSBhbHRlcmEgYSBjb25jZW50cmHDp8OjbyBkZSBwb2x1ZW50ZXMuIEEgY29uY2VudHJhw6fDo28gbcOpZGlhIHBvcHVsYWNpb25hbCBhdHVhbCDDqSAkNTAkIG1nL0wuIEVsZSBkZWZpbmUgJEhfMDogXFxtdSA9IDUwJCBlICRIXzE6IFxcbXUgXFxuZXEgNTAkLiBcbihhKSBTZSBvIGNpZW50aXN0YSB1dGlsaXphIHVtYSByZWdyYSBkZSBkZWNpc8OjbyBiaWNhdWRhbCAoZG9pcyBsYWRvcykgY29tICRcXGFscGhhID0gMCwwNSQsIGV4cGxpcXVlIGEgcmVsYcOnw6NvIGVudHJlIG8gcC12YWxvciBlIGEgZGVjaXPDo28gZGUgcmVqZWl0YXIgJEhfMCQuXG4oYikgU3Vwb25oYSBxdWUgbyBwLXZhbG9yIG9idGlkbyBzZWphICQwLDAzJC4gUXVhbCBhIGRlY2lzw6NvIGVzdGF0w61zdGljYT9cbihjKSBRdWFsIGEgaW1wbGljYcOnw6NvIGRlIHJlZHV6aXIgbyBuw612ZWwgZGUgc2lnbmlmaWPDom5jaWEgZGUgJDAsMDUkIHBhcmEgJDAsMDEkIG5vIHBvZGVyIGRvIHRlc3RlPyIsICJkaWNhIjogIk8gcC12YWxvciDDqSBhIHByb2JhYmlsaWRhZGUgZGUgb2JzZXJ2YXIgdW0gdmFsb3IgZGEgZXN0YXTDrXN0aWNhIHTDo28gb3UgbWFpcyBleHRyZW1vIHF1ZSBvIG9idGlkbywgYXNzdW1pbmRvICRIXzAkIHZlcmRhZGVpcmEuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIChhKTogQSBkZWNpc8OjbyBkZSByZWplaXRhciAkSF8wJCBvY29ycmUgcXVhbmRvICRwXFx0ZXh0ey12YWxvcn0gPCBcXGFscGhhJC4iLCAiUGFzc28gKGIpOiBDb21vICQwLDAzIDwgMCwwNSQsIHJlamVpdGFtb3MgJEhfMCQgYW8gbsOtdmVsIGRlICQ1XFwlJC4gSMOhIGV2aWTDqm5jaWFzIHNpZ25pZmljYXRpdmFzIGRlIHF1ZSBhIGNvbmNlbnRyYcOnw6NvIGZvaSBhbHRlcmFkYS4iLCAiUGFzc28gKGMpOiBBbyByZWR1emlyICRcXGFscGhhJCwgcmVzdHJpbmdpbW9zIG1haXMgYSByZWdpw6NvIGRlIHJlamVpw6fDo28gKGRpbWludWluZG8gYSBjaGFuY2UgZGUgRXJybyBUaXBvIEkpLiBDb21vIHJlc3VsdGFkbywgcGFyYSB1bSB0YW1hbmhvIGRlIGFtb3N0cmEgY29uc3RhbnRlLCBhIHByb2JhYmlsaWRhZGUgZGUgRXJybyBUaXBvIElJICgkXFxiZXRhJCkgYXVtZW50YSwgbyBxdWUgcmVkdXogbyBwb2RlciBkbyB0ZXN0ZSAoJDEtXFxiZXRhJCkuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiUGFyYSB0ZXN0YXIgc2UgdW1hIG1vZWRhIMOpIHZpY2lhZGEsIGxhbsOnYW1vcyBhIG1vZWRhICRuPTEwJCB2ZXplcy4gU2VqYSAkWCQgbyBuw7ptZXJvIGRlIGNhcmFzLiAkSF8wOiBwPTAsNSQgZSAkSF8xOiBwPTAsOCQuIEEgcmVnacOjbyBkZSByZWplacOnw6NvIMOpICRSQyA9IFxceyA4LCA5LCAxMCBcXH0kIGNhcmFzLlxuKGEpIENhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRlIEVycm8gVGlwbyBJICgkXFxhbHBoYSQpLlxuKGIpIENhbGN1bGUgYSBwcm9iYWJpbGlkYWRlIGRlIEVycm8gVGlwbyBJSSAoJFxcYmV0YSQpIHF1YW5kbyAkcD0wLDgkLlxuKGMpIFNlIGF1bWVudMOhc3NlbW9zIGEgYW1vc3RyYSBwYXJhICRuPTIwJCwgbyBxdWUgb2NvcnJlcmlhIGNvbSBhIGNhcGFjaWRhZGUgZG8gdGVzdGUgZGUgZGlzdGluZ3VpciBlbnRyZSAkSF8wJCBlICRIXzEkPyIsICJkaWNhIjogIlV0aWxpemUgYSBkaXN0cmlidWnDp8OjbyBCaW5vbWlhbCAkQmluKG4sIHApJC4gTGVtYnJlLXNlIHF1ZSAkUChYPWspID0gXFxiaW5vbXtufXtrfSBwXmsgKDEtcClee24ta30kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAoYSk6IFNvYiAkSF8wJCAoJHA9MCw1JCk6ICRcXGFscGhhID0gUChYIFxcZ2UgOCkgPSBQKFg9OCkgKyBQKFg9OSkgKyBQKFg9MTApID0gXFxiaW5vbXsxMH17OH0oMCw1KV57MTB9ICsgXFxiaW5vbXsxMH17OX0oMCw1KV57MTB9ICsgXFxiaW5vbXsxMH17MTB9KDAsNSleezEwfSA9ICg0NSsxMCsxKS8xMDI0ID0gNTYvMTAyNCBcXGFwcHJveCAwLDA1NDckLiIsICJQYXNzbyAoYik6IFNvYiAkSF8xJCAoJHA9MCw4JCk6ICRcXGJldGEgPSBQKFggPCA4IHwgcD0wLDgpID0gMSAtIFAoWCBcXGdlIDggfCBwPTAsOCkgPSAxIC0gW1xcYmlub217MTB9ezh9KDAsOCleOCgwLDIpXjIgKyBcXGJpbm9tezEwfXs5fSgwLDgpXjkoMCwyKV4xICsgXFxiaW5vbXsxMH17MTB9KDAsOCleezEwfV0gPSAxIC0gWzAsMzAyMCArIDAsMjY4NCArIDAsMTA3NF0gPSAxIC0gMCw2Nzc4ID0gMCwzMjIyJC4iLCAiUGFzc28gKGMpOiBDb20gJG4kIG1haW9yLCBhIHZhcmnDom5jaWEgZGFzIGVzdGltYXRpdmFzIGRpbWludWksIHRvcm5hbmRvIGFzIGRpc3RyaWJ1acOnw7VlcyBkZSAkSF8wJCBlICRIXzEkIG1haXMgY29uY2VudHJhZGFzIGVtIHRvcm5vIGRlIHN1YXMgcmVzcGVjdGl2YXMgbcOpZGlhcywgbyBxdWUgYXVtZW50YSBvIHBvZGVyIGRvIHRlc3RlLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxuZmlnLmFkZF90cmFjZShnby5CYXIoeD1ucC5hcmFuZ2UoMTEpLCB5PVtzdGF0cy5iaW5vbS5wbWYoaywgMTAsIDAuNSkgZm9yIGsgXFxpbiByYW5nZSgxMSldLCBuYW1lPVwiSF8wOiBwPTAuNVwiLCBtYXJrZXJfY29sb3I9XCIjNEMxRDk1XCIpKVxuZmlnLmFkZF90cmFjZShnby5CYXIoeD1ucC5hcmFuZ2UoMTEpLCB5PVtzdGF0cy5iaW5vbS5wbWYoaywgMTAsIDAuOCkgZm9yIGsgXFxpbiByYW5nZSgxMSldLCBuYW1lPVwiSF8xOiBwPTAuOFwiLCBtYXJrZXJfY29sb3I9XCIjN0MzQUVEXCIsIG9wYWNpdHk9MC43KSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPVwiRGlzdHJpYnVpw6fDtWVzIEJpbm9taWFsIHNvYiBIXzAgZSBIXzFcIiwgeGF4aXM9ZGljdCh0aXRsZT1cIk7Dum1lcm8gZGUgQ2FyYXMgKFgpXCIpKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogInUxcTI1M2FuM2czZCwgUHJvYmxlbWEgNCBlIDE0IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC4zMjIyfSwgeyJlbnVuY2lhZG8iOiAiVW1hIGVtcHJlc2EgZmFybWFjw6p1dGljYSB0ZXN0YSBhIGVmaWPDoWNpYSBkZSB1bSBub3ZvIGbDoXJtYWNvIGNvbXBhcmFuZG8gYSByZWR1w6fDo28gZGEgcHJlc3PDo28gYXJ0ZXJpYWwuIEEgaGlww7N0ZXNlIG51bGEgw6kgcXVlIGEgcmVkdcOnw6NvIG3DqWRpYSDDqSAkXFxtdSA9IDEwXHRleHR7IG1tSGd9JCAoJEhfMCQpLiBPIGRlc3ZpbyBwYWRyw6NvIHBvcHVsYWNpb25hbCDDqSAkXFxzaWdtYSA9IDRcdGV4dHsgbW1IZ30kIGUgdXRpbGl6YS1zZSB1bWEgYW1vc3RyYSBkZSAkbiA9IDY0JCBwYWNpZW50ZXMuIChhKSBEZWZpbmEgbWF0ZW1hdGljYW1lbnRlICRIXzEkIHBhcmEgdW0gdGVzdGUgYmlsYXRlcmFsLiAoYikgU2UgZml4YXJtb3MgJFxcYWxwaGEgPSA1XFwlJCwgZGV0ZXJtaW5lIGEgUmVnacOjbyBDcsOtdGljYSAoUkMpIHBhcmEgJFxiYXJ7WH0kLiAoYykgQ2FsY3VsZSBhIHByb2JhYmlsaWRhZGUgZG8gRXJybyBUaXBvIElJICgkXFxiZXRhJCkgc2UgbyB2ZXJkYWRlaXJvIHZhbG9yIGRhIG3DqWRpYSBmb3IgJFxcbXUgPSAxMVx0ZXh0eyBtbUhnfSQuIiwgImRpY2EiOiAiTyBlcnJvIHBhZHLDo28gZGEgbcOpZGlhIMOpICRcXHNpZ21hX3tcXGJhcntYfX0gPSBcXHNpZ21hIC8gXFxzcXJ0e259JC4gQSBSQyBiaWxhdGVyYWwgcGFyYSAkXFxhbHBoYT0wLDA1JCB1dGlsaXphICRaX3tjcml0fSA9IDEsOTYkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQYXNzbyAoYSk6ICRIXzA6IFxcbXUgPSAxMCQgZSAkSF8xOiBcXG11IFxcbmVxIDEwJC4iLCAiUGFzc28gKGIpOiAkRVAoXFxiYXJ7WH0pID0gNCAvIFxcc3FydHs2NH0gPSAwLDUkLiBMaW1pdGVzIGRlIFJDOiAkXFxiYXJ7eH1fYyA9IDEwIFxccG0gMSw5NiBcXGNkb3QgMCw1JC4gTG9nbywgJFJDID0gXFx7IFxcYmFye3h9IDwgOSwwMiBcXHRleHR7IG91IH0gXFxiYXJ7eH0gPiAxMCw5OCBcXH0kLiIsICJQYXNzbyAoYyk6IFNvYiAkSF8xOiBcXG11ID0gMTEkLCAkXFxiYXJ7WH0gXFxzaW0gTigxMSwgMCw1XjIpJC4gJFxcYmV0YSA9IFAoOSwwMiBcXGxlIFxcYmFye1h9IFxcbGUgMTAsOTggfCBcXG11ID0gMTEpJC4iLCAiUGFzc28gKGMgLSBjb250Lik6ICRaXzEgPSAoOSwwMiAtIDExKS8wLDUgPSAtMyw5NiQ7ICRaXzIgPSAoMTAsOTggLSAxMSkvMCw1ID0gLTAsMDQkLiAkXFxiZXRhID0gUCgtMyw5NiBcXGxlIFogXFxsZSAtMCwwNCkgXFxhcHByb3ggMCw0ODQwIC0gMCA9IDAsNDg0MCQuIl0sICJjb2RpZ29fcGxvdGx5IjogImZpZyA9IGdvLkZpZ3VyZSgpXG54ID0gbnAubGluc3BhY2UoOCwgMTMsIDIwMClcbmZpZy5hZGRfdHJhY2UoZ28uU2NhdHRlcih4PXgsIHk9c3RhdHMubm9ybS5wZGYoeCwgMTAsIDAuNSksIG5hbWU9J0Rpc3RyaWJ1acOnw6NvIHNvYiAkSF8wJCcpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT1zdGF0cy5ub3JtLnBkZih4LCAxMSwgMC41KSwgbmFtZT0nRGlzdHJpYnVpw6fDo28gc29iICRIXzEkJykpXG5maWcudXBkYXRlX2xheW91dCh0aXRsZT0nU29icmVwb3Npw6fDo28gZGFzIERpc3RyaWJ1acOnw7VlcyBlIEVycm8gVGlwbyBJSScsIHhheGlzX3RpdGxlPSdNw6lkaWEgQW1vc3RyYWwnLCB5YXhpc190aXRsZT0nRGVuc2lkYWRlJykiLCAicmVmZXJlbmNpYV9saXZybyI6ICJ1MXEyNTNhbjNnM2QsIFNlw6fDo28gMTIuNSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuNDg0fSwgeyJlbnVuY2lhZG8iOiAiVW0gcHJvY2Vzc28gaW5kdXN0cmlhbCBwcm9kdXogZWl4b3MgY29tIGRpw6JtZXRybyAkXFxtdSQuIERlc2VqYS1zZSB0ZXN0YXIgJEhfMDogXFxtdSA9IDIwXFx0ZXh0eyBtbX0kIGNvbnRyYSAkSF8xOiBcXG11ID4gMjBcXHRleHR7IG1tfSQgY29tICRcXHNpZ21hID0gMSwwXFx0ZXh0eyBtbX0kIGUgJG4gPSAyNSQuIChhKSBFbmNvbnRyZSBhIFJlZ2nDo28gQ3LDrXRpY2EgcGFyYSAkXFxhbHBoYSA9IDAsMDEkLiAoYikgQ2FsY3VsZSBvIHBvZGVyIGRvIHRlc3RlICgkXFxwaSQpIHNlIG8gdmFsb3IgcmVhbCBkYSBtw6lkaWEgZm9yICRcXG11ID0gMjAsNVxcdGV4dHsgbW19JC4iLCAiZGljYSI6ICJQYXJhIHVtIHRlc3RlIHVuaWxhdGVyYWwgw6AgZGlyZWl0YSwgJFpfe2NyaXR9ID0gMiwzMyQuIEEgZXN0YXTDrXN0aWNhIGRlIHRlc3RlIMOpICRcXGJhcntYfSBcXHNpbSBOKFxcbXUsIFxcc2lnbWFeMi9uKSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIChhKTogJEVQKFxcYmFye1h9KSA9IDEgLyBcXHNxcnR7MjV9ID0gMCwyJC4gJFxcYWxwaGEgPSAwLDAxIFxcUmlnaHRhcnJvdyBaX3tjcml0fSA9IDIsMzMkLiAkXFxiYXJ7eH1fYyA9IDIwICsgMiwzMyBcXGNkb3QgMCwyID0gMjAsNDY2JC4gJFJDID0gXFx7IFxcYmFye3h9IFxcZ2UgMjAsNDY2IFxcfSQuIiwgIlBhc3NvIChiKTogUG9kZXIgJFxccGkoMjAsNSkgPSBQKFxcYmFye1h9IFxcZ2UgMjAsNDY2IHwgXFxtdSA9IDIwLDUpID0gUChaIFxcZ2UgKDIwLDQ2NiAtIDIwLDUpLzAsMikgPSBQKFogXFxnZSAtMCwxNykgPSAwLDU2NzUkLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogInUxcTI1M2FuM2czZCwgUHJvYmxlbWEgMTUgYWRhcHRhZG8iLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjU2NzV9LCB7ImVudW5jaWFkbyI6ICJTdXBvbmhhIHVtIHRlc3RlIG9uZGUgc2UgZGVjaWRlIHJlamVpdGFyICRIXzA6IHAgPSAwLDUkIGEgZmF2b3IgZGUgJEhfMTogcCBcXG5lcSAwLDUkIGNvbSB1bWEgYW1vc3RyYSBkZSAkbiA9IDEwMCQuIEEgcmVnacOjbyBkZSByZWplacOnw6NvIMOpICRSQyA9IFxceyBcXGhhdHtwfSA8IDAsNDAgXFx0ZXh0eyBvdSB9IFxcaGF0e3B9ID4gMCw2MCBcXH0kLiAoYSkgQ2FsY3VsZSBhIHByb2JhYmlsaWRhZGUgZG8gRXJybyBUaXBvIEkgKCRcXGFscGhhJCkgYXByb3hpbWFuZG8gYSBiaW5vbWlhbCBwZWxhIG5vcm1hbC4gKGIpIEV4cGxpcXVlIG8gaW1wYWN0byBkZSBhdW1lbnRhciBvIG7DrXZlbCBkZSBzaWduaWZpY8OibmNpYSAkXFxhbHBoYSQgc29icmUgbyBFcnJvIFRpcG8gSUkgKCRcXGJldGEkKS4iLCAiZGljYSI6ICJPIGVycm8gcGFkcsOjbyBkZSB1bWEgcHJvcG9yw6fDo28gw6kgJFxcc3FydHtwKDEtcCkvbn0kLiBTb2IgJEhfMCQsICRwID0gMCw1JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gKGEpOiBTb2IgJEhfMCQsICRcXGhhdHtwfSBcXHNpbSBOKDAsNTsgMCw1IFxcY2RvdCAwLDUgLyAxMDApID0gTigwLDU7IDAsMDAyNSkkLiBEZXN2aW8gcGFkcsOjbyAkXFxzaWdtYV97XFxoYXR7cH19ID0gMCwwNSQuIiwgIlBhc3NvIChhIC0gY29udC4pOiAkWl8xID0gKDAsNDAgLSAwLDUpLzAsMDUgPSAtMiwwJDsgJFpfMiA9ICgwLDYwIC0gMCw1KS8wLDA1ID0gMiwwJC4gJFxcYWxwaGEgPSBQKFogPCAtMikgKyBQKFogPiAyKSA9IDAsMDIyOCArIDAsMDIyOCA9IDAsMDQ1NiQuIiwgIlBhc3NvIChiKTogQXVtZW50YXIgJFxcYWxwaGEkIGV4cGFuZGUgYSBSZWdpw6NvIENyw610aWNhIChSQyksIGZhY2lsaXRhbmRvIGEgcmVqZWnDp8OjbyBkZSAkSF8wJC4gQ29uc2VxdWVudGVtZW50ZSwgYSBwcm9iYWJpbGlkYWRlIGRlIGZhbGhhciBhbyByZWplaXRhciAkSF8wJCBxdWFuZG8gZWxhIMOpIGZhbHNhIGRpbWludWksIGxvZ28gJFxcYmV0YSQgZGltaW51aS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMDQ1Nn0sIHsiZW51bmNpYWRvIjogIlVtYSBlbXByZXNhIGRlIFxcbG9nw61zdGljYSB0ZXN0YSBhIGVmaWNpw6puY2lhIGRlIHVtIG5vdm8gc29mdHdhcmUgZGUgcm90ZWlyaXphw6fDo28uIEEgbcOpZGlhIGRlIHRlbXBvIGRlIGVudHJlZ2EgYW50ZXJpb3IgZXJhICRcXG11ID0gNDUkIFxcbWluICgkXFxzaWdtYSA9IDEwJCkuIERlc2VqYS1zZSB0ZXN0YXIgJEhfMDogXFxtdSA9IDQ1JCBjb250cmEgJEhfMTogXFxtdSA8IDQ1JCBjb20gJG49MjUkLiAoYSkgRGV0ZXJtaW5lIGEgUkMgcGFyYSAkXFxhbHBoYSA9IDAsMDUkLiAoYikgQ2FsY3VsZSBvIHBvZGVyIGRvIHRlc3RlIHNlIGEgbm92YSBtw6lkaWEgcmVhbCBmb3IgJFxcbXUgPSA0MCQuIChjKSBJbnRlcnByZXRlIG8gc2lnbmlmaWNhZG8gcHLDoXRpY28gZG8gcmVzdWx0YWRvIGVuY29udHJhZG8gbm8gaXRlbSAoYikuIiwgImRpY2EiOiAiVXRpbGl6ZSBhIGVzdGF0w61zdGljYSAkWiA9IChcXGJhcntYfSAtIFxcbXUpIC8gKFxcc2lnbWEgLyBcXHNxcnR7bn0pJC4gTGVtYnJlLXNlIHF1ZSAkUkMkIGRldmUgc2VyIHVuaWxhdGVyYWwgw6AgZXNxdWVyZGEuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhcmEgJFxcYWxwaGE9MCwwNSQsIG8gdmFsb3IgY3LDrXRpY28gJFpfe1xcdGV4dHtjcml0fX0gPSAtMSw2NDUkLiIsICJDYWxjdWxhbW9zIG8gcG9udG8gY3LDrXRpY286ICRcXGJhcntYfV9jID0gNDUgLSAxLDY0NSBcXGNkb3QgKDEwLzUpID0gNDUgLSAzLDI5ID0gNDEsNzEkLiAkUkMgPSBcXHsgXFxiYXJ7WH0gPCA0MSw3MSBcXH0kLiIsICJQYXJhICRcXG11PTQwJCwgbyBwb2RlciAkXFxwaSg0MCkgPSBQKFxcYmFye1h9IDwgNDEsNzEgfCBcXG11PTQwKSA9IFAoWiA8ICg0MSw3MS00MCkvMikgPSBQKFogPCAwLDg1NSkgXFxhcHByb3ggMCw4MDM4JC4iLCAiTyBwb2RlciBkZSA4MCwzOCUgaW5kaWNhIHF1ZSBvIHRlc3RlIHRlbSB1bWEgYWx0YSBwcm9iYWJpbGlkYWRlIGRlIGRldGVjdGFyIGEgbWVsaG9yYSByZWFsIG5vIHRlbXBvIGRlIGVudHJlZ2EuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAidTFxMjUzYW4zZzNkIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogMC44MDM4fSwgeyJlbnVuY2lhZG8iOiAiU2VqYSAkWCQgdW1hIHZhcmnDoXZlbCBzZWd1aW5kbyB1bWEgZGlzdHJpYnVpw6fDo28gJEJlcm5vdWxsaShwKSQuIFBhcmEgdGVzdGFyICRIXzA6IHAgPSAwLDUkIGNvbnRyYSAkSF8xOiBwIFxcbmVxIDAsNSQgY29tICRuPTEwJCwgZGVmaW5lLXNlIGEgcmVnacOjbyBkZSByZWplacOnw6NvICRSQyA9IFxcezAsIDEsIDksIDEwXFx9JCAobsO6bWVybyBkZSBzdWNlc3NvcykuIChhKSBDYWxjdWxlIG8gbsOtdmVsIGRlIHNpZ25pZmljw6JuY2lhICRcXGFscGhhJCBleGF0byBkbyB0ZXN0ZS4gKGIpIENhbGN1bGUgbyBwb2RlciBkbyB0ZXN0ZSAkXFxwaShwKSQgcGFyYSAkcD0wLDgkLiAoYykgUG9yIHF1ZSBvIHBvZGVyIGRlc3RlIHRlc3RlIMOpIGJhaXhvIHBhcmEgJHAkIHByw7N4aW1vIGRlICQwLDUkPyIsICJkaWNhIjogIlVzZSBhIGRpc3RyaWJ1acOnw6NvIGJpbm9taWFsOiAkUChYPWspID0gXFxiaW5vbXtufXtrfSBwXmsgKDEtcClee24ta30kLiBPIHBvZGVyIMOpIGEgcHJvYmFiaWxpZGFkZSBkZSByZWplaXRhciAkSF8wJCBzb2IgJHA9MCw4JC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiU29iICRIXzAgKHA9MCw1KSQsICRcXGFscGhhID0gUChYIFxcaW4gXFx7MCwxLDksMTBcXH0pID0gMiBcXGNkb3QgKFxcYmlub217MTB9ezB9ICsgXFxiaW5vbXsxMH17MX0pIFxcY2RvdCAwLDVeezEwfSA9IDIgXFxjZG90IDExIC8gMTAyNCBcXGFwcHJveCAwLDAyMTUkLiIsICJTb2IgJHA9MCw4JCwgJFxccGkoMCw4KSA9IFAoWD0wLDEsOSwxMCkgPSBcXGJpbm9tezEwfXswfTAsOF4wIDAsMl57MTB9ICsgXFxiaW5vbXsxMH17MX0wLDheMSAwLDJeOSArIFxcYmlub217MTB9ezl9MCw4XjkgMCwyXjEgKyBcXGJpbm9tezEwfXsxMH0wLDheezEwfSAwLDJeMCQuIiwgIkNhbGN1bGFuZG86ICRQKFg9MCwxKSBcXGFwcHJveCAwJCBlICRQKFg9OSwxMCkgPSAxMCBcXGNkb3QgMCwxMzQyIFxcY2RvdCAwLDIgKyAwLDEwNzM3IFxcYXBwcm94IDAsMjY4NCArIDAsMTA3NCA9IDAsMzc1OCQuIiwgIk8gcG9kZXIgw6kgYmFpeG8gcHLDs3hpbW8gYSAwLDUgcG9pcyBhcyBkaXN0cmlidWnDp8O1ZXMgc29iICRIXzAkIGUgJEhfMSQgc8OjbyBxdWFzZSBpZMOqbnRpY2FzLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogInUxcTI1M2FuM2czZCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMzc1OH0sIHsiZW51bmNpYWRvIjogIkVtIHVtIGNvbnRyb2xlIGRlIHF1YWxpZGFkZSBkZSBwYXJhZnVzb3MsIHRlc3RhLXNlICRIXzA6IFxcbXUgPSAxNTAkIGNvbSAkXFxzaWdtYSA9IDEwJCBlICRuPTI1JC4gQSByZWdyYSBkZSBkZWNpc8OjbyDDqSAkUkMgPSBcXHsgXFxiYXJ7WH0gPCAxNDcgXFx9JC4gKGEpIERldGVybWluZSBhIHByb2JhYmlsaWRhZGUgZG8gZXJybyB0aXBvIEkgKCRcXGFscGhhJCkuIChiKSBDYWxjdWxlIGEgcHJvYmFiaWxpZGFkZSBkbyBlcnJvIHRpcG8gSUkgKCRcXGJldGEkKSBzZSBhIG3DqWRpYSByZWFsIGZvciAkXFxtdSA9IDE0OCQuIChjKSBDYWxjdWxlIG8gcG9kZXIgZG8gdGVzdGUgKCRcXHBpJCkgcGFyYSAkXFxtdSA9IDE0OCQuIiwgImRpY2EiOiAiTyBlcnJvIHRpcG8gSUkgJFxcYmV0YSQgw6kgYSBwcm9iYWJpbGlkYWRlIGRlIG7Do28gcmVqZWl0YXIgJEhfMCQgZGFkbyBxdWUgJEhfMSQgw6kgdmVyZGFkZWlyYSAoJDEgLSBcXHBpJCkuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIiRcXGFscGhhID0gUChcXGJhcntYfSA8IDE0NyB8IFxcbXU9MTUwKSA9IFAoWiA8ICgxNDctMTUwKS8yKSA9IFAoWiA8IC0xLDUpID0gMCwwNjY4JC4iLCAiJFxcYmV0YSA9IFAoXFxiYXJ7WH0gXFxnZSAxNDcgfCBcXG11PTE0OCkgPSBQKFogXFxnZSAoMTQ3LTE0OCkvMikgPSBQKFogXFxnZSAtMCw1KSA9IDAsNjkxNSQuIiwgIiRcXHBpID0gMSAtIFxcYmV0YSA9IDEgLSAwLDY5MTUgPSAwLDMwODUkLiJdLCAiY29kaWdvX3Bsb3RseSI6ICJmaWcgPSBnby5GaWd1cmUoKVxueCA9IG5wLmxpbnNwYWNlKDE0MCwgMTYwLCAxMDApXG5maWcuYWRkX3RyYWNlKGdvLlNjYXR0ZXIoeD14LCB5PXN0YXRzLm5vcm0ucGRmKHgsIDE1MCwgMiksIG5hbWU9J0gwOiBcXFxcbXU9MTUwJywgbGluZT1kaWN0KGNvbG9yPScjNEMxRDk1JykpKVxuZmlnLmFkZF90cmFjZShnby5TY2F0dGVyKHg9eCwgeT1zdGF0cy5ub3JtLnBkZih4LCAxNDgsIDIpLCBuYW1lPSdIMTogXFxcXG11PTE0OCcsIGxpbmU9ZGljdChjb2xvcj0nIzdDM0FFRCcpKSlcbmZpZy51cGRhdGVfbGF5b3V0KHRpdGxlPSdDdXJ2YXMgZGUgSGlww7N0ZXNlJywgeGF4aXNfdGl0bGU9J03DqWRpYSBBbW9zdHJhbCcsIHlheGlzX3RpdGxlPSdEZW5zaWRhZGUnKSIsICJyZWZlcmVuY2lhX2xpdnJvIjogInUxcTI1M2FuM2czZCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IDAuMzA4NX1dfQ==').decode('utf-8'))


    import streamlit as st
    import plotly.graph_objects as go
    import numpy as np
    import scipy.stats as stats
    
    # Inicialização do estado da sessão para gamificação
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dos totais
    mcq_list = dados_exercicios.get("questoes_multipla_escolha", [])
    disc_list = dados_exercicios.get("questoes_discursivas", [])
    total_ex = len(mcq_list) + len(disc_list)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v is True)
    
    # Interface de Placar
    st.subheader("📊 Painel de Progresso")
    if total_ex > 0:
        st.progress(acertos / total_ex)
        st.info(f"🏆 **Seu Placar de Aprendizado:** {acertos} de {total_ex} desafios concluídos com sucesso!")
    
    # Seção de Múltipla Escolha
    st.markdown("---")
    st.header("🧠 Questões de Múltipla Escolha")
    for i, questao in enumerate(mcq_list):
        with st.container(border=True):
            st.markdown(f"#### Questão {i+1}")
            st.markdown(questao["enunciado"])
            
            if questao.get("referencia_livro"):
                st.markdown(f"📖 *Referência: {questao['referencia_livro']}*")
                
            codigo = questao.get("codigo_plotly")
            if codigo:
                try:
                    local_vars = {"go": go, "np": np, "stats": stats}
                    exec(codigo, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"fig_mcq_{i}")
                except Exception as e:
                    st.warning(f"Erro ao renderizar gráfico: {e}")
            
            opcoes = questao.get("alternativas", {})
            escolha = st.radio(
                "Selecione uma alternativa:", 
                options=list(opcoes.keys()), 
                format_func=lambda x: f"{x}) {opcoes[x]}",
                key=f"radio_mcq_{i}"
            )
            
            if st.button("💡 Ver Dica", key=f"dica_mcq_{i}"):
                st.info(questao.get("dica"))
                
            if st.button("✅ Confirmar Resposta", key=f"btn_mcq_{i}"):
                if escolha == questao.get("alternativa_correta"):
                    st.success("🎉 Correto! Resposta excelente.")
                    st.session_state.respostas_certas[f"mcq_{i}"] = True
                else:
                    st.error("❌ Resposta Incorreta. Reveja os conceitos e tente novamente!")
                    st.session_state.respostas_certas[f"mcq_{i}"] = False
                st.rerun()
                
            with st.expander("🔍 Ver Gabarito Comentado e Explicação"):
                st.markdown(questao.get("gabarito_comentado"))
    
    # Seção de Questões Discursivas
    st.markdown("---")
    st.header("📝 Desafios de Cálculo")
    for i, questao in enumerate(disc_list):
        with st.container(border=True):
            st.markdown(f"#### Questão {i+1} (Análise Técnica)")
            st.markdown(questao["enunciado"])
            
            if questao.get("referencia_livro"):
                st.markdown(f"📖 *Referência: {questao['referencia_livro']}*")
                
            codigo = questao.get("codigo_plotly")
            if codigo:
                try:
                    local_vars = {"go": go, "np": np, "stats": stats}
                    exec(codigo, globals(), local_vars)
                    if "fig" in local_vars:
                        st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"fig_disc_{i}")
                except Exception as e:
                    st.warning(f"Erro ao renderizar gráfico: {e}")
            
            st.text_area("Sua Resposta em Prosa / Raciocínio:", key=f"text_disc_{i}")
            
            resp_esperada = questao.get("resposta_numerica_esperada")
            if resp_esperada is not None:
                valor_aluno = st.number_input("Digite o resultado numérico exato:", key=f"num_disc_{i}", format="%.4f")
                if st.button("Validar Cálculo Numérico", key=f"btn_disc_{i}"):
                    if abs(valor_aluno - resp_esperada) <= max(0.01, 0.01 * abs(resp_esperada)):
                        st.success("🎉 Resultado Numérico Correto! Cálculo impecável.")
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                    else:
                        st.error("❌ O valor calculado difere do gabarito. Confira as substituições!")
                        st.session_state.respostas_certas[f"disc_{i}"] = False
                    st.rerun()
            else:
                if st.checkbox("Marque aqui após concluir sua reflexão", key=f"check_disc_{i}"):
                    st.session_state.respostas_certas[f"disc_{i}"] = True
                    st.rerun()
                else:
                    st.session_state.respostas_certas[f"disc_{i}"] = False
            
            with st.expander("✅ Ver Resolução Detalhada Passo a Passo"):
                for passo in questao.get("gabarito_passo_a_passo", []):
                    st.markdown(f"- {passo}")
