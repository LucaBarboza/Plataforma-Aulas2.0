import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuMTogRXN0aW1hw6fDo28gcG9udHVhbCBlIGludGVydmFsYXIiLCAicmVmZXJlbmNpYXNfYmlibGlvZ3JhZmljYXNfZmluYWlzIjogWyJCdXNzYWIsIFcuIE8uLCAmIE1vcmV0dGluLCBQLiBBLiBFc3RhdMOtc3RpY2EgQsOhc2ljYSAtIENhcC4gMTAuMSwgcHAuIDI0NS0yNTAiLCAiVHJpb2xhLCBNLiBGLiBJbnRyb2R1w6fDo28gw6AgRXN0YXTDrXN0aWNhIC0gQ2FwLiA3LjIsIHBwLiAzMTAtMzE1Il19').decode('utf-8'))

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
    import pandas as pd
    import plotly.graph_objects as go
    from scipy.stats import norm
    
    # Fundamentos da Estimação Pontual - Layout Acadêmico de Luxo
    
    st.markdown(r"### 🎯 Fundamentos da Estimação Pontual")
    
    st.markdown(r"""
    A inferência estatística fundamenta-se na capacidade de compreender parâmetros populacionais desconhecidos através de evidências amostrais. Enquanto a média populacional ($\mu$) e a variância ($\sigma^2$) permanecem ocultas em grandes populações, utilizamos estimadores como a média amostral ($\bar{X}$) e a variância amostral ($S^2$) para realizar suposições fundamentadas.
    """)
    
    st.info(r"Um estimador pontual é uma função dos dados da amostra que visa fornecer um valor único para o parâmetro de interesse. A qualidade é avaliada pela ausência de vício e pela eficiência.")
    
    st.markdown(r"""
    A inferência estatística surge como uma resposta necessária à limitação intrínseca da ciência experimental: a impossibilidade prática ou econômica de observar a totalidade de um fenômeno. O parâmetro populacional permanece como uma entidade teórica oculta, um valor 'verdadeiro' mas desconhecido.
    """)
    
    st.markdown(r"#### ⚖️ O Formalismo Matemático")
    st.latex(r"E(\bar{X}) = \mu, \quad Var(\bar{X}) = \frac{\sigma^2}{n}, \quad S^2 = \frac{1}{n-1}\sum_{i=1}^{n} (X_i - \bar{X})^2")
    
    st.markdown(r"A ausência de vício garante que, a longo prazo, o estimador não tende a subestimar nem a superestimar o valor real. Abaixo, detalhamos a prova analítica para a esperança da média amostral:")
    
    # Dedução Analítica (Hardcoded conforme solicitado)
    with st.container(border=True):
        st.markdown(r"##### 📝 Passo 1: Definição do estimador")
        st.latex(r"E[\bar{X}] = E\left[\frac{1}{n}\sum_{i=1}^n X_i\right]")
        
        st.markdown(r"##### 📝 Passo 2: Propriedade da linearidade")
        st.latex(r"E[\bar{X}] = \frac{1}{n}\sum_{i=1}^n E[X_i]")
        
        st.markdown(r"##### 📝 Passo 3: Substituição do parâmetro populacional")
        st.latex(r"E[\bar{X}] = \frac{1}{n}(n\mu) = \mu")
    
    st.markdown(r"---")
    
    # Simulador Interativo
    st.markdown(r"#### 📊 Simulador: O impacto do tamanho da amostra (n)")
    col1, col2 = st.columns(2)
    
    with col1:
        n_slider = st.slider(r"Selecione o tamanho da amostra (n):", 1, 100, 10, key=r"n_slider_subtopico_1")
    
    # Cálculo do simulador
    mu_sim = 6.5
    sigma_sim = 1.0
    std_erro = sigma_sim / np.sqrt(n_slider)
    x_vals = np.linspace(mu_sim - 3, mu_sim + 3, 200)
    y_vals = norm.pdf(x_vals, mu_sim, std_erro)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode=r"lines", name=r"Distribuição de $\bar{X}$", line=dict(color=r"#4C1D95", width=3)))
    
    fig.update_layout(
        template=r"plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text=r"<b>Distribuição Amostral da Média</b>", font=dict(size=14, color=r"#1E293B", family=r"Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text=r"Valores da Média Amostral", font=dict(size=11, color=r"#1E293B", family=r"Arial, sans-serif")), tickfont=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text=r"Densidade de Probabilidade", font=dict(size=11, color=r"#1E293B", family=r"Arial, sans-serif")), tickfont=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), gridcolor=r"#E2E8F0", zerolinecolor=r"#CBD5E1", fixedrange=True),
        legend=dict(orientation=r"h", yanchor=r"bottom", y=1.02, xanchor=r"right", x=1.0, font=dict(size=9, color=r"#64748B", family=r"Arial, sans-serif"), bgcolor=r"rgba(255, 255, 255, 0.8)", bordercolor=r"#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor=r"#FFFFFF", font_size=12, font_color=r"#1E293B", font_family=r"Arial, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_1")
    
    st.info(rf"Com um tamanho amostral de n={n_slider}, o erro padrão da estimativa é de {std_erro:.4f}. Note que, à medida que n aumenta, a curva se estreita, refletindo uma maior precisão na estimativa pontual de $\mu=6.5$.")
    
    # Exemplo Prático
    st.markdown(r"#### 📖 Exemplo Prático: Nível de HbA1c")
    with st.container(border=True):
        st.markdown(r"**Contexto:** Estudo clínico com 10 pacientes sobre HbA1c (Média = 6,5%).")
        st.markdown(r"O cálculo da média amostral é realizado pela soma das observações dividida pelo tamanho da amostra:")
        st.latex(r"\bar{X} = \frac{\sum_{i=1}^{10} X_i}{10} = \frac{65,0}{10} = 6,5")
        
        st.success(r"Laudo: O valor de 6,5% atua como o estimador pontual não-viciado para a população em análise, servindo como base para o monitoramento longitudinal do programa nutricional.")

    import streamlit as st
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from scipy import stats
    
    # --- Título do Subtópico ---
    st.header(r"Intervalos de Confiança para a Média")
    
    # --- Prosa Teórica ---
    st.markdown(r"""
    A estimação pontual, embora útil, não fornece a precisão da incerteza associada aos dados. Para complementar a análise, introduzimos os **intervalos de confiança (IC)**, que definem uma faixa de valores dentro da qual esperamos encontrar o parâmetro populacional com um nível de confiança especificado, tipicamente $1 - \alpha = 0,95$.
    """)
    
    st.info(r"A construção do intervalo depende da distribuição amostral da média e do erro padrão $EP(\bar{X})$. Quando o desvio padrão populacional $\sigma$ é conhecido, utilizamos a distribuição normal padrão; na prática, utilizamos a distribuição $t$ de Student devido ao desconhecimento de $\sigma$ e o uso da estimativa amostral $S$.")
    
    st.markdown(r"""
    A inferência estatística é a arte de transitar do particular para o geral. No campo das Ciências da Saúde, frequentemente nos deparamos com a necessidade de estimar parâmetros populacionais — por exemplo, a ingestão média diária de cálcio de um grupo de gestantes. A média amostral $\bar{X}$ é o nosso melhor estimador, mas, isoladamente, ela não nos revela a nossa margem de erro.
    """)
    
    # --- Formalismo Matemático ---
    st.markdown(r"### 📐 Estrutura do Formalismo")
    st.latex(r"IC = \bar{X} \pm t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}}, \quad E = t_{\alpha/2, gl} \cdot \frac{S}{\sqrt{n}}")
    
    # --- Dedução Analítica ---
    st.markdown(r"#### 🧠 Dedução da Margem de Erro")
    with st.container(border=True):
        st.latex(r"P(-Z_{\alpha/2} \le Z \le Z_{\alpha/2}) = 1-\alpha")
        st.markdown(r"Substituindo $Z$ pela estatística de teste da média:")
        st.latex(r"P\left(-Z_{\alpha/2} \le \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \le Z_{\alpha/2}\right) = 1-\alpha")
        st.markdown(r"Isolando o parâmetro $\mu$ no centro:")
        st.latex(r"P\left(\bar{X} - Z_{\alpha/2}\frac{\sigma}{\sqrt{n}} \le \mu \le \bar{X} + Z_{\alpha/2}\frac{\sigma}{\sqrt{n}}\right) = 1-\alpha")
    
    # --- Simulador Interativo ---
    st.markdown(r"---")
    st.subheader(r"📊 Simulador: Visualização do IC")
    col1, col2 = st.columns(2)
    with col1:
        n_sim = st.slider(r"Tamanho Amostral (n)", 5, 100, 25, key=r"n_sim_subtopico_2")
    with col2:
        conf_level = st.selectbox(r"Nível de Confiança", [0.90, 0.95, 0.99], index=1, key=r"conf_sim_subtopico_2")
    
    # Lógica do Simulador (Plotly)
    x_vals = np.linspace(-4, 4, 200)
    y_vals = stats.t.pdf(x_vals, df=n_sim-1)
    t_crit = stats.t.ppf(1 - (1 - conf_level)/2, df=n_sim-1)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name=r"Distribuição t", line=dict(color="#4C1D95", width=2)))
    fig.add_vrect(x0=-t_crit, x1=t_crit, fillcolor="#A78BFA", opacity=0.3, line_width=0)
    
    fig.update_layout(
        template="plotly_white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4),
        title=dict(text="<b>Distribuição Amostral e Área de Confiança</b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        xaxis=dict(title=dict(text="Desvios Padrão", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        yaxis=dict(title=dict(text="Densidade", font=dict(size=11, color="#1E293B", family="Arial, sans-serif")), tickfont=dict(size=9, color="#64748B", family="Arial, sans-serif"), gridcolor="#E2E8F0", zerolinecolor="#CBD5E1", fixedrange=True),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1.0, font=dict(size=9, color="#64748B", family="Arial, sans-serif"), bgcolor="rgba(255, 255, 255, 0.8)", bordercolor="#E2E8F0", borderwidth=1),
        hoverlabel=dict(bgcolor="#FFFFFF", font_size=12, font_color="#1E293B", font_family="Arial, sans-serif")
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    st.info(f"Ao selecionar $n={n_sim}$ e {conf_level*100:.0f}% de confiança, o valor crítico $t$ ajusta a amplitude da zona sombreada para garantir que a estimativa capture o parâmetro populacional com o rigor estatístico definido.")
    
    # --- Exemplo Prático ---
    st.markdown(r"### 📖 Exemplo Prático")
    with st.container(border=True):
        st.markdown(r"**Enunciado:** Nutricionista deseja estimar o consumo médio de sódio (n=25, $\bar{X}=2400$, $S=300$).")
        st.markdown(r"- Margem de erro: $E = 2,064 \cdot (300 / \sqrt{25}) = 123,84$")
        st.markdown(r"- IC = $2400 \pm 123,84$")
        st.success(r"Com 95% de confiança, a média populacional de sódio situa-se entre 2276,16 mg e 2523,84 mg.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDIgLSBUw7NwaWNvIDIuMTogRXN0aW1hw6fDo28gcG9udHVhbCBlIGludGVydmFsYXIiLCAicXVlc3RvZXNfbXVsdGlwbGFfZXNjb2xoYSI6IFtdLCAicXVlc3RvZXNfZGlzY3Vyc2l2YXMiOiBbXX0=').decode('utf-8'))


    # Inicialização de estado para gamificação
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dos totais
    mcq_list = dados_exercicios.get("questoes_multipla_escolha", [])
    disc_list = dados_exercicios.get("questoes_discursivas", [])
    total_ex = len(mcq_list) + len(disc_list)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v is True)
    
    # Barra de progresso e Placar
    st.subheader("📊 Progresso do Aprendizado")
    if total_ex > 0:
        st.progress(acertos / total_ex)
        st.info(f"🏆 **Seu Placar de Aprendizado:** {acertos} de {total_ex} desafios concluídos com sucesso!")
    
    # --- SEÇÃO DE MÚLTIPLA ESCOLHA ---
    if mcq_list:
        st.markdown("---")
        st.header("📝 Exercícios de Múltipla Escolha")
        
        for i, questao in enumerate(mcq_list):
            with st.container(border=True):
                st.markdown(f"#### Questão {i+1}")
                st.markdown(questao.get("enunciado"))
                
                if questao.get("referencia_livro"):
                    st.markdown(f"📖 *Referência RAG: {questao['referencia_livro']}*")
                
                # Plotly Interativo
                if questao.get("codigo_plotly"):
                    local_vars = {}
                    try:
                        exec(questao["codigo_plotly"], globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"fig_mcq_{i}")
                    except Exception as e:
                        st.warning("Não foi possível renderizar o gráfico.")
    
                opcoes = questao.get("alternativas", {})
                selecao = st.radio(
                    "Escolha uma alternativa:",
                    options=list(opcoes.keys()),
                    format_func=lambda x: f"{x}: {opcoes[x]}",
                    key=f"radio_mcq_{i}"
                )
                
                if st.button("💡 Dica", key=f"dica_mcq_{i}"):
                    st.info(questao.get("dica", "Nenhuma dica disponível."))
                
                if st.button("✅ Confirmar Resposta", key=f"btn_mcq_{i}"):
                    if selecao == questao.get("alternativa_correta"):
                        st.success("🎉 Correto! Resposta excelente.")
                        st.session_state.respostas_certas[f"mcq_{i}"] = True
                    else:
                        st.error("❌ Resposta Incorreta. Reveja os conceitos e tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
                    st.rerun()
    
                with st.expander("🔍 Ver Gabarito Comentado e Explicação"):
                    st.markdown(questao.get("gabarito_comentado", "Sem explicação disponível."))
    
    # --- SEÇÃO DE DISCURSIVAS ---
    if disc_list:
        st.markdown("---")
        st.header("🧮 Desafios de Cálculo e Análise")
        
        for i, questao in enumerate(disc_list):
            with st.container(border=True):
                st.markdown(f"#### Questão {i+1} (Discursiva)")
                st.markdown(questao.get("enunciado"))
                
                if questao.get("referencia_livro"):
                    st.markdown(f"📖 *Referência RAG: {questao['referencia_livro']}*")
                
                # Plotly Interativo
                if questao.get("codigo_plotly"):
                    local_vars = {}
                    try:
                        exec(questao["codigo_plotly"], globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True, key=f"fig_disc_{i}")
                    except Exception as e:
                        st.warning("Não foi possível renderizar o gráfico.")
                
                st.text_area("Sua Resposta em Prosa / Raciocínio:", key=f"text_disc_{i}")
                
                # Validação Numérica ou Qualitativa
                valor_esperado = questao.get("resposta_numerica_esperada")
                if valor_esperado is not None:
                    valor_aluno = st.number_input("Digite o resultado numérico exato:", format="%f", key=f"num_disc_{i}")
                    if st.button("Validar Cálculo Numérico", key=f"val_disc_{i}"):
                        if abs(valor_aluno - valor_esperado) <= max(0.01, 0.01 * abs(valor_esperado)):
                            st.success("🎉 Resultado Numérico Correto! Cálculo impecável.")
                            st.session_state.respostas_certas[f"disc_{i}"] = True
                        else:
                            st.error("❌ O valor calculado difere do gabarito oficial.")
                            st.session_state.respostas_certas[f"disc_{i}"] = False
                        st.rerun()
                else:
                    if st.checkbox("Marque aqui após estudar e responder este desafio", key=f"check_disc_{i}"):
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                        st.rerun()
                    else:
                        st.session_state.respostas_certas[f"disc_{i}"] = False
                
                with st.expander("✅ Ver Resolução Detalhada Passo a Passo"):
                    for passo in questao.get("gabarito_passo_a_passo", []):
                        st.markdown(f"- {passo}")
