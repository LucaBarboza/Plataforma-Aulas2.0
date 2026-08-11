import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as stats
from scipy.stats import norm
import base64
import json

# Carregamento seguro dos metadados da aula para evitar SyntaxError
metadata = json.loads(base64.b64decode('eyJ0ZW1hX2dsb2JhbCI6ICJVbmlkYWRlIDQgLSBUw7NwaWNvIDQuMjogTyB1c28gZGUgbWF0cml6IGludmVyc2EgZ2VuZXJhbGl6YWRhIiwgInJlZmVyZW5jaWFzX2JpYmxpb2dyYWZpY2FzX2ZpbmFpcyI6IFsiTHVuYSwgSi4gRy4gJiBFc3RldmVzLCBFLiBNLiwgSW52ZXJzYXMgZ2VuZXJhbGl6YWRhcyBkZSBtYXRyaXplcyByZWFpcyAtIENhcC4gMS42LCBwcC4gMzQtNDIuIiwgIkJpc3BvLCBOLiwgw4FsZ2VicmEgTGluZWFyIEFwbGljYWRhIChOb3RhcyBkZSBBdWxhKSAtIENhcC4gOSwgcHAuIDYtMTUuIl19').decode('utf-8'))

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
    
    # Cabeçalho do Subtópico
    st.header(r"Limitações da Inversão de Matrizes e o Conceito de Inversa Condicional")
    
    # Introdução
    st.markdown(r"""
    No campo da álgebra linear aplicada, a operação de inversão de matrizes é fundamental para resolver sistemas de equações e encontrar estimadores ótimos em modelos lineares. Contudo, a definição clássica exige condições rígidas: a matriz deve ser quadrada e não singular (determinante diferente de zero e posto completo).
    """)
    
    st.markdown(r"""
    Na prática estatística e científica, essas condições são frequentemente violadas:
    - **Multicolinearidade:** Variáveis preditoras altamente correlacionadas em modelos de regressão.
    - **Dados Desbalanceados:** Planejamentos de experimentos onde a ortogonalidade é perdida.
    - **Posto Deficiente:** Matrizes retangulares ou sistemas superdeterminados/subdeterminados.
    """)
    
    st.info(r"Para contornar tais limitações, a matemática desenvolveu as inversas generalizadas, permitindo que operadores inversos sejam calculados mesmo para matrizes que não possuem inversa tradicional.")
    
    # Formalismo Matemático
    st.subheader(r"📐 O Coração Matemático: Definição da Inversa Condicional")
    
    st.markdown(r"A condição fundamental que define uma inversa generalizada (ou inversa condicional) $A^{-}$ de uma matriz $A_{n \times m}$ com posto $r(A)=k$ é expressa pelo seguinte formalismo:")
    
    st.latex(r"A A^{-} A = A")
    
    st.markdown(r"""
    Diferente da inversa clássica, a inversa condicional não possui a propriedade de unicidade. Esta característica, longe de ser um defeito, confere flexibilidade estatística para escolher a solução que melhor satisfaz as restrições de identificabilidade do modelo.
    """)
    
    # Dedução Analítica
    st.subheader(r"🔗 Dedução Analítica: A Preservação da Consistência")
    
    st.markdown(r"Para verificar a validade do operador no contexto da resolução de sistemas lineares $Ax=g$, observe a sequência lógica da aplicação da inversa condicional:")
    
    st.markdown(r"1. Partimos do sistema linear original:")
    st.latex(r"Ax = g")
    
    st.markdown(r"2. Multiplicamos ambos os lados pela inversa condicional $A^{-}$:")
    st.latex(r"A^{-}Ax = A^{-}g")
    
    st.markdown(r"3. Multiplicamos pela esquerda pela matriz $A$:")
    st.latex(r"A(A^{-}Ax) = A(A^{-}g)")
    
    st.markdown(r"4. Associando os termos, aplicamos a definição fundamental $AA^{-}A = A$:")
    st.latex(r"(AA^{-}A)x = A A^{-}g")
    
    st.markdown(r"5. Resultando na consistência do sistema:")
    st.latex(r"Ax = A A^{-}g")
    
    st.markdown(r"6. Logo, concluímos que o sistema é resolvido dentro do espaço coluna de $A$:")
    st.latex(r"g = A A^{-}g")
    
    # Exemplos Práticos
    st.subheader(r"📈 Casos de Aplicação Prática: Inversão em Sistemas Singulares")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Matriz Singular de Posto 2")
        st.markdown(r"Considere o sistema linear com matriz singular $A$ e vetor de resultados $g$:")
        
        st.latex(r"A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & 1 \\ 2 & 2 & 2 \end{pmatrix}, \quad g = \begin{pmatrix} 3 \\ 1 \\ 6 \end{pmatrix}")
        
        st.markdown(r"Dados sumarizados: $r(A) = 2$ e $det(A) = 0$.")
        
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Escolhemos a submatriz $M = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ para realizar a inversão parcial.")
        st.markdown(r"- Calculamos a inversa de $M$: $M^{-1} = \begin{pmatrix} 0.5 & 0.5 \\ 0.5 & -0.5 \end{pmatrix}$.")
        st.markdown(r"- Construímos $A^{-}$ através da transposição e expansão dos elementos, resultando em:")
        st.latex(r"A^{-} = \begin{pmatrix} 0.5 & 0.5 & 0 \\ 0.5 & -0.5 & 0 \\ 0 & 0 & 0 \end{pmatrix}")
        
        st.success(r"Laudo: A matriz $A^{-}$ obtida satisfaz a condição $AA^{-}A = A$, permitindo isolar a informação essencial do sistema mesmo com a redundância linear identificada na terceira linha.")
    
    # Conclusão Teórica
    st.markdown(r"""
    ---
    **Nota Final:** A transição da rigidez da inversão quadrada para a flexibilidade da inversa condicional é a transição da matemática idealizada para a estatística aplicada. O uso de decomposições como SVD (Singular Value Decomposition) em implementações computacionais modernas garante a estabilidade necessária para lidar com essas matrizes singulares no dia a dia do cientista de dados.
    """)

    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
    
    # --- Cabeçalho do Subtópico ---
    st.header(r"A Arquitetura da Inversa de Moore-Penrose: Definição, Existência e Unicidade")
    
    # --- Prosa Teórica - Parte 1 ---
    st.markdown(r"""
    A álgebra linear clássica nos ensina que a operação de inversão é um privilégio de operadores quadrados e não singulares. Contudo, na estatística aplicada, enfrentamos frequentemente matrizes de design que, devido à multicolinearidade ou dimensões inadequadas, carecem de posto completo. 
    
    Nesse cenário, a inversa de Moore-Penrose surge como a solução fundamental que não apenas generaliza a noção de inversa, mas a impõe sob um rigor geométrico estrito.
    """)
    
    st.info(r"A pseudoinversa A^{+} seleciona, entre o conjunto infinito de soluções para um sistema Ax = y, aquela que minimiza simultaneamente a norma do resíduo e a norma do vetor solução.")
    
    # --- Formalismo Matemático ---
    st.subheader(r"📐 O Coração Matemático: Propriedades da Pseudoinversa")
    st.markdown(r"A definição formal do operador A^{+} repousa sobre quatro propriedades geométricas inegociáveis, que garantem sua unicidade como projetor ortogonal:")
    
    st.latex(r"AA^{+}A = A")
    st.latex(r"A^{+}AA^{+} = A^{+}")
    st.latex(r"(A^{+}A)^{\top} = A^{+}A")
    st.latex(r"(AA^{+})^{\top} = AA^{+}")
    
    # --- Demonstração Analítica ---
    st.markdown(r"""
    **Fundamentação da Unicidade:**
    A unicidade da inversa de Moore-Penrose deriva de um processo de demonstração estruturado. Considere duas matrizes, A_1^{+} e A_2^{+}, que satisfazem as condições listadas acima:
    """)
    
    st.latex(r"A_{1}^{+}A = A_{1}^{+}AA_{1}^{+}A")
    st.latex(r"A_{1}^{+}A = A_{1}^{+}A(A_{1}^{+})^{\top}A^{\top}")
    st.latex(r"A_{1}^{+}A = A_{2}^{+}A")
    st.latex(r"A_{1}^{+} = A_{1}^{+}AA_{1}^{+} = A_{2}^{+}AA_{1}^{+} = A_{2}^{+}AA_{2}^{+} = A_{2}^{+}")
    
    # --- Simulador: Visualizador de Projeções Ortogonais ---
    st.subheader(r"📊 Simulador: Visualizador de Projeções Ortogonais")
    st.markdown(r"Ajuste os coeficientes da matriz A para observar o comportamento do projetor AA^{+} no espaço 2D.")
    
    col1, col2 = st.columns(2)
    with col1:
        a11 = st.slider(r"a11", -2.0, 2.0, 1.0, key=r"a11_subtopico_2")
        a21 = st.slider(r"a21", -2.0, 2.0, 0.0, key=r"a21_subtopico_2")
    with col2:
        a12 = st.slider(r"a12", -2.0, 2.0, 0.0, key=r"a12_subtopico_2")
        a22 = st.slider(r"a22", -2.0, 2.0, 1.0, key=r"a22_subtopico_2")
    
    A = np.array([[a11, a12], [a21, a22]])
    A_pinv = np.linalg.pinv(A)
    P = A @ A_pinv
    
    fig = go.Figure()
    fig.add_trace(go.Heatmap(z=P, colorscale="Blues", showscale=False))
    fig.update_layout(
        title=dict(text=r"<b>Projetor AA<sup>+</sup></b>", font=dict(size=14, color="#1E293B", family="Arial, sans-serif"), x=0.0, y=0.95),
        plot_bgcolor="white",
        paper_bgcolor="white",
        height=420,
        margin=dict(l=55, r=30, t=65, b=55, pad=4)
    )
    st.plotly_chart(fig, use_container_width=True, key=r"plotly_chart_subtopico_2")
    
    st.info(r"O gráfico exibe a matriz de projeção resultante. Quando a matriz original A possui posto deficiente, o determinante de AA^{+} reflete o colapso de dimensões no espaço coluna.")
    
    # --- Exemplos Práticos ---
    st.subheader(r"📈 Casos de Aplicação Prática")
    
    with st.container(border=True):
        st.markdown(r"##### 📖 Exemplo Resolvido: Matriz de Design com Redundância")
        st.markdown(r"Seja a matriz de design X = [[1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 0, 1]]. Esta matriz descreve observações com redundância.")
        st.latex(r"r(X) = 2, \quad X^{\top}X = \begin{pmatrix} 4 & 2 & 2 \\ 2 & 2 & 0 \\ 2 & 0 & 2 \end{pmatrix}")
        st.markdown(r"**Desenvolvimento Aritmético Passo a Passo:**")
        st.markdown(r"- Decompomos X = BC.")
        st.markdown(r"- Calculamos (B^{\top}B)^{-1} e (CC^{\top})^{-1} para isolar o posto.")
        st.markdown(r"- Aplicamos X^{+} = C^{\top}(CC^{\top})^{-1}(B^{\top}B)^{-1}B^{\top} = \frac{1}{6} \begin{pmatrix} 1 & 1 & 1 & 1 \\ 2 & 2 & -1 & -1 \\ -1 & -1 & 2 & 2 \end{pmatrix}.")
        st.success(r"A pseudoinversa X^{+} permite obter a estimativa de mínimos quadrados $\hat{\beta} = X^{+}Y$, garantindo estabilidade em modelos de posto incompleto.")

    st.markdown('---')
    st.markdown('##### 📚 Referências Bibliográficas Consolidadas (Rodapé da Aula)')
    for ref in metadata['referencias_bibliograficas_finais']:
        st.markdown(f'- {ref}')

with tab_exercicios:
    import json, base64
    dados_exercicios = json.loads(base64.b64decode('eyJ0b3BpY29fYXVsYSI6ICJVbmlkYWRlIDQgLSBUw7NwaWNvIDQuMjogTyB1c28gZGUgbWF0cml6IGludmVyc2EgZ2VuZXJhbGl6YWRhIiwgInF1ZXN0b2VzX211bHRpcGxhX2VzY29saGEiOiBbeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXN0dWRvIGRlIG1vZGVsYWdlbSBsaW5lYXIgcGFyYSBwcmV2ZXIgbyBjb25zdW1vIGRlIGVuZXJnaWEgZW0gdW5pZGFkZXMgaW5kdXN0cmlhaXMsIG9idGV2ZS1zZSB1bWEgbWF0cml6IGRlIHBsYW5lamFtZW50byAkWF97KG4gXHRpbWVzIG0pfSQgcXVlIGFwcmVzZW50YSBhbHRhIG11bHRpY29saW5lYXJpZGFkZSwgcmVzdWx0YW5kbyBlbSB1bSBwb3N0byBkZWZpY2llbnRlLCBpc3RvIMOpLCAkcihYKSA8IG0kLiBDb25zaWRlcmFuZG8gYSBpbXBvc3NpYmlsaWRhZGUgZGUgY2FsY3VsYXIgYSBpbnZlcnNhIHRyYWRpY2lvbmFsICQoWF57XFxwcmltZX1YKV57LTF9JCwgcXVhbCBkYXMgc2VndWludGVzIHNlbnRlbsOnYXMgZGVzY3JldmUgY29ycmV0YW1lbnRlIGEgbGltaXRhw6fDo28gdGXDs3JpY2EgZSBhIGFsdGVybmF0aXZhIG1hdGVtw6F0aWNhIHBhcmEgbyBwcm9ibGVtYT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgaW52ZXJzYSAkQV57LTF9JCDDqSBkZWZpbmlkYSBhcGVuYXMgcGFyYSBtYXRyaXplcyBxdWFkcmFkYXMgZGUgcG9zdG8gY29sdW5hIGNvbXBsZXRvLCBzZW5kbyBuZWNlc3PDoXJpbyBvIHVzbyBkZSB1bWEgaW52ZXJzYSBjb25kaWNpb25hbCAkQV57LX0kIHF1ZSBzYXRpc2Zhw6dhICRBIEFeey19IEEgPSBBJC4iLCAiQiI6ICJBIG1hdHJpeiAkWF57XFxwcmltZX1YJCDDqSBzZW1wcmUgaW52ZXJ0w612ZWwgcG9yIGRlZmluacOnw6NvIGVtIG1vZGVsb3MgbGluZWFyZXMsIGJhc3RhbmRvIGF1bWVudGFyIG8gdGFtYW5obyBhbW9zdHJhbCAkbiQgYXTDqSBxdWUgJHIoWCkgPSBtJC4iLCAiQyI6ICJBIGludmVyc2EgZGUgTW9vcmUtUGVucm9zZSDDqSBhIMO6bmljYSBzb2x1w6fDo28gcG9zc8OtdmVsIHBhcmEgcXVhbHF1ZXIgbWF0cml6LCBpbmRlcGVuZGVudGVtZW50ZSBkZSBzdWEgZXN0cnV0dXJhLCBlIHNlbXByZSBjb2luY2lkZSBjb20gYSBpbnZlcnNhIGNsw6Fzc2ljYSAkQV57LTF9JCBwYXJhIG1hdHJpemVzIHNpbmd1bGFyZXMuIiwgIkQiOiAiTyB1c28gZGUgJEFeey19JCBpbnZhbGlkYSBhIHNvbHXDp8OjbyBkZSBzaXN0ZW1hcyBsaW5lYXJlcyBjb25zaXN0ZW50ZXMsIGRldmVuZG8tc2UgZGVzY2FydGFyIGNvbHVuYXMgZGEgbWF0cml6ICRYJCBhdMOpIHF1ZSBvIGRldGVybWluYW50ZSBzZWphIGRpZmVyZW50ZSBkZSB6ZXJvLiIsICJFIjogIkEgaW52ZXJzYSAkQV57LX0kIHBlcm1pdGUgb2J0ZXIgdW1hIHNvbHXDp8OjbyDDum5pY2EgcGFyYSBvIHZldG9yIGRlIHBhcsOibWV0cm9zLCBpbmRlcGVuZGVudGVtZW50ZSBkYSBjb25zaXN0w6puY2lhIGRvIHNpc3RlbWEgbGluZWFyIG9yaWdpbmFsLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJBIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhIGNvbmRpw6fDo28gZGUgZXhpc3TDqm5jaWEgZGUgJEFeey0xfSQgYmFzZWFkYSBubyBkZXRlcm1pbmFudGUgZSBubyBwb3N0by4gTyBxdWUgb2NvcnJlIHF1YW5kbyBvIHBvc3RvIG7Do28gw6kgY29tcGxldG8/IiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGludmVyc2EgY2zDoXNzaWNhICQoQV57XFxwcmltZX1BKV57LTF9JCByZXF1ZXIgcXVlICRBJCB0ZW5oYSBwb3N0byBjb2x1bmEgY29tcGxldG8uIFF1YW5kbyBow6EgbXVsdGljb2xpbmVhcmlkYWRlICgkcihBKSA8IG0kKSwgJEFee1xccHJpbWV9QSQgw6kgc2luZ3VsYXIgKFxcZGV0ID0gMCkuIEEgaW52ZXJzYSBjb25kaWNpb25hbCwgZGVmaW5pZGEgcGVsYSBwcm9wcmllZGFkZSAkQSBBXnstfSBBID0gQSQsIMOpIHVtYSBleHRlbnPDo28gbmVjZXNzw6FyaWEgcG9pcywgZW1ib3JhIG7Do28gw7puaWNhLCBwZXJtaXRlIGNvbnRvcm5hciBhIHNpbmd1bGFyaWRhZGUgZGEgbWF0cml6LCBwb3NzaWJpbGl0YW5kbyBhIG9idGVuw6fDo28gZGUgc29sdcOnw7VlcyBwYXJhIHNpc3RlbWFzICRBeD1nJCBxdWFuZG8gZXN0ZXMgc8OjbyBjb25zaXN0ZW50ZXMuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzLCBDYXAgMiwgcC4gMzcifSwgeyJlbnVuY2lhZG8iOiAiU2VqYSAkQV97KG4gXFx0aW1lcyBtKX0kIHVtYSBtYXRyaXogY29tIHBvc3RvICRyKEEpID0gayQuIE5hIHByw6F0aWNhIGVzdGF0w61zdGljYSwgYSBpbnZlcnNhIGNvbmRpY2lvbmFsICRBXnstfSQgZGVzZW1wZW5oYSB1bSBwYXBlbCBmdW5kYW1lbnRhbC4gUXVhbCBkYXMgY29uZGnDp8O1ZXMgYWJhaXhvIMOpIGEgZGVmaW5pw6fDo28gZnVuZGFtZW50YWwgZXhpZ2lkYSBwYXJhIHF1ZSB1bWEgbWF0cml6ICRBXnstfSQgc2VqYSBjb25zaWRlcmFkYSB1bWEgaW52ZXJzYSBjb25kaWNpb25hbCAob3UgZ2VuZXJhbGl6YWRhKSBkZSAkQSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICIkQV57LX0gQSBBXnstfSA9IEFeey19JCIsICJCIjogIiRBIEFeey19IEEgPSBBJCIsICJDIjogIiRBXnstfSBBID0gSV97KG4pfSQiLCAiRCI6ICIkQSBBXnstfSA9IEFeey19IEEkIiwgIkUiOiAiJEFeey19ID0gKEFee1xccHJpbWV9IEEpXnstMX0gQV57XFxwcmltZX0kIChzZW1wcmUgdsOhbGlkYSkifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkEgZGVmaW5pw6fDo28gZGUgaW52ZXJzYSBjb25kaWNpb25hbCBmb2NhIGVtIHByZXNlcnZhciBhIGVzdHJ1dHVyYSBvcmlnaW5hbCBkYSBtYXRyaXogYW8gc2VyIHByw6kgZSBww7NzLW11bHRpcGxpY2FkYS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlBvciBkZWZpbmnDp8OjbyAoU2VhcmxlLCAxOTcyKSwgdW1hIG1hdHJpeiAkQV57LX0kIMOpIGNoYW1hZGEgZGUgaW52ZXJzYSBjb25kaWNpb25hbCBvdSBnZW5lcmFsaXphZGEgZGUgJEEkIHNlLCBlIHNvbWVudGUgc2UsIHNhdGlzZmF6IGEgY29uZGnDp8OjbyBmdW5kYW1lbnRhbCAkQSBBXnstfSBBID0gQSQuIEFzIG91dHJhcyBjb25kacOnw7VlcyBsaXN0YWRhcyAoY29tbyBhcyBkZSBNb29yZS1QZW5yb3NlKSBzw6NvIG1haXMgcmVzdHJpdGl2YXMgZSBuw6NvIGRlZmluZW0gYSBpbnZlcnNhIGNvbmRpY2lvbmFsIGLDoXNpY2EuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzLCBDYXAgMiwgcC4gMzkifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gc2lzdGVtYSBkZSBtb25pdG9yYW1lbnRvIGRlIElvVCBpbmR1c3RyaWFsLCB1bSBzZW5zb3IgZW52aWEgdW0gc2luYWwgcmVwcmVzZW50YWRvIHBlbGEgbWF0cml6IGRlIG9ic2VydmHDp8O1ZXMgJEEkICQobiBcdGltZXMgbSkkLCBvbmRlICRuID4gbSQgZSBvIHBvc3RvIGRhIG1hdHJpeiDDqSAkcihBKSA9IG0kIChwb3N0byBjb2x1bmEgY29tcGxldG8pLiBQYXJhIHJlYWxpemFyIGEgY2FsaWJyYcOnw6NvIGRvIHNpbmFsIGUgZW5jb250cmFyIG8gdmV0b3IgZGUgcGFyw6JtZXRyb3MgZXN0aW1hZG9zIHF1ZSBtaW5pbWl6YSBvIGVycm8gcXVhZHLDoXRpY28sIHV0aWxpemEtc2UgYSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgJEFeeyt9JC4gUXVhbCBkYXMgYWx0ZXJuYXRpdmFzIGFwcmVzZW50YSBhIHJlbGHDp8OjbyBjb3JyZXRhIHBhcmEgYSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgbmVzdGUgY2Vuw6FyaW8gZGUgcG9zdG8gY29sdW5hIGNvbXBsZXRvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiJEFeeyt9ID0gKEFee1xcdG9wfUEpXnstMX1BXntcXHRvcH0kIGUgJEFeeyt9QSA9IElfeyhtKX0kIiwgIkIiOiAiJEFeeyt9ID0gQV57XFx0b3B9KEFBXntcXHRvcH0pXnstMX0kIGUgJEFBXnsrfSA9IElfeyhuKX0kIiwgIkMiOiAiJEFeeyt9ID0gKEFBXntcXHRvcH0pXnstMX1BXntcXHRvcH0kIGUgJEFeeyt9QSA9IElfeyhuKX0kIiwgIkQiOiAiJEFeeyt9ID0gQShBXntcXHRvcH1BKV57LTF9JCBlICRBXnsrfUEgPSBJX3sobil9JCIsICJFIjogIiRBXnsrfSA9IChBXntcXHRvcH1BKUFee1xcdG9wfSQgZSAkQUFeeyt9ID0gSV97KG0pfSQifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQSIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBkZWZpbmnDp8OjbyBkZSBwb3N0byBjb2x1bmEgY29tcGxldG8gZSBjb21vIGEgaW52ZXJzw6NvIGRlIEdyYW1pYW5vcyBhdXhpbGlhIG5hIGNvbnN0cnXDp8OjbyBkYSBwc2V1ZG8taW52ZXJzYS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIlF1YW5kbyB1bWEgbWF0cml6ICRBJCAkKG4gXHRpbWVzIG0pJCBwb3NzdWkgcG9zdG8gY29sdW5hIGNvbXBsZXRvLCBpc3RvIMOpLCAkcihBKSA9IG0kLCBhIG1hdHJpeiAkQV57XFx0b3B9QSQgw6kgdW1hIG1hdHJpeiAkKG0gXHRpbWVzIG0pJCBpbnZlcnTDrXZlbC4gTmVzc2UgY2FzbywgYSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2Ugw6kgZGVmaW5pZGEgY29tbyAkQV57K30gPSAoQV57XFx0b3B9QSleey0xfUFee1xcdG9wfSQuIEFvIG11bHRpcGxpY2FyIHBvciAkQSQgw6AgZXNxdWVyZGEsIHRlbW9zICRBXnsrfUEgPSAoQV57XFx0b3B9QSleey0xfUFee1xcdG9wfUEgPSBJX3sobSl9JCwgbyBxdWUgc2F0aXNmYXogYXMgY29uZGnDp8O1ZXMgZGUgUGVucm9zZSwgZXNwZWNpZmljYW1lbnRlIGEgcHJvamXDp8OjbyBubyBlc3Bhw6dvIGNvbHVuYXIgZGUgJEEkLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTHVuYSAmIEVzdGV2ZXMsIEludmVyc2EgR2VuZXJhbGl6YWRhIGRlIE1hdHJpemVzLCBDYXAgMSwgcC4gMzcifSwgeyJlbnVuY2lhZG8iOiAiQSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2Ugw6kgYW1wbGFtZW50ZSBhcGxpY2FkYSBkZXZpZG8gw6Agc3VhIHVuaWNpZGFkZSBlIHByb3ByaWVkYWRlcyBxdWUgZXN0ZW5kZW0gbyBjb25jZWl0byBkZSBpbnZlcnNhIHRyYWRpY2lvbmFsLiBDb25zaWRlcmUgdW1hIG1hdHJpeiAkQSQgZSBzdWEgc3Vwb3N0YSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgJEFeeyt9JC4gUXVhbCBkYXMgc2VndWludGVzIGNvbmRpw6fDtWVzIGFiYWl4byBmYXogcGFydGUgZG8gY29uanVudG8gcmlnb3Jvc28gZGUgY29uZGnDp8O1ZXMgZGUgUGVucm9zZSBxdWUgZ2FyYW50ZSBxdWUgJEFeeyt9JCBzZWphLCBkZSBmYXRvLCBhIGludmVyc2EgZGUgTW9vcmUtUGVucm9zZT8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIiRBQV57K31BID0gQSQgZSAkQV57K31BQV57K30gPSBBXnsrfSQiLCAiQiI6ICIkKEFeeyt9QSlee1xcdG9wfSA9IEFeeyt9QSQgZSAkKEFBXnsrfSlee1xcdG9wfSA9IEFBXnsrfSQiLCAiQyI6ICIkQSQgZGV2ZSBzZXIgb2JyaWdhdG9yaWFtZW50ZSB1bWEgbWF0cml6IHF1YWRyYWRhIGUgbsOjby1zaW5ndWxhci4iLCAiRCI6ICJUb2RhcyBhcyBhbnRlcmlvcmVzIGVzdMOjbyBjb3JyZXRhcyAoQSBlIEIpLiIsICJFIjogIkFwZW5hcyAkQV57K31BID0gSSQgw6kgc3VmaWNpZW50ZS4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiRCIsICJkaWNhIjogIkEgZGVmaW5pw6fDo28gZGUgUGVucm9zZSDDqSBjb21wb3N0YSBwb3IgcXVhdHJvIGNvbmRpw6fDtWVzIGF4aW9tw6F0aWNhcy4gUmV2aXNlIHNlIGVsYXMgaW5jbHVlbSB0YW50byBhIHJlbGHDp8OjbyBkZSAnaW52ZXJzYScgcXVhbnRvIGEgZXhpZ8OqbmNpYSBkZSBzaW1ldHJpYSBwYXJhIG9zIHByb2R1dG9zIHByb2pldGl2b3MuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGludmVyc2EgZGUgTW9vcmUtUGVucm9zZSBkZSB1bWEgbWF0cml6ICRBJCDDqSBkZWZpbmlkYSBwZWxhIHNhdGlzZmHDp8OjbyBkZSBxdWF0cm8gY29uZGnDp8O1ZXMgc2ltdWx0w6JuZWFzOiAoMSkgJEFBXnsrfUEgPSBBJDsgKDIpICRBXnsrfUFBXnsrfSA9IEFeeyt9JDsgKDMpICQoQV57K31BKV57XFx0b3B9ID0gQV57K31BJDsgZSAoNCkgJChBQV57K30pXntcXHRvcH0gPSBBQV57K30kLiBDb21vIGFzIGFsdGVybmF0aXZhcyBBIGUgQiBkZXNjcmV2ZW0gZXhhdGFtZW50ZSBlc3RhcyBjb25kacOnw7VlcywgYSBhbHRlcm5hdGl2YSBEIMOpIGEgY29ycmV0YS4gRXN0YXMgY29uZGnDp8O1ZXMgZ2FyYW50ZW0gcXVlICRBXnsrfSQgc2VqYSDDum5pY2EgZSBxdWUgYXMgbWF0cml6ZXMgJEFBXnsrfSQgZSAkQV57K31BJCBmdW5jaW9uZW0gY29tbyBwcm9qZXRvcmVzIG9ydG9nb25haXMuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCaXNwbywgTi4sIEF1bGEgOTogSW52ZXJzYSBHZW5lcmFsaXphZGEgZGUgTWF0cml6ZXMsIHAuIDYifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gZXhwZXJpbWVudG8gZGUgY29udHJvbGUgZGUgcXVhbGlkYWRlIGF1dG9tYXRpemFkbyBlbSB1bWEgaW5kw7pzdHJpYSwgdW0gc2lzdGVtYSBkZSBzZW5zb3JpYW1lbnRvIGdlcmEgdW1hIG1hdHJpeiBkZSBkYWRvcyAkWF97KG4gXHRpbWVzIG0pfSQgY29tICRuID4gbSQsIHJlcHJlc2VudGFuZG8gb2JzZXJ2YcOnw7VlcyBkZSAkbSQgdmFyacOhdmVpcyBlbSAkbiQgaW5zdGFudGVzIGRlIHRlbXBvLiBEZXZpZG8gYSBmYWxoYXMgdGVtcG9yw6FyaWFzIG5vcyBzZW5zb3Jlcywgb2JzZXJ2YS1zZSBxdWUgYXMgY29sdW5hcyBkYSBtYXRyaXogJFgkIHBvc3N1ZW0gZGVwZW5kw6puY2lhIGxpbmVhciwgcmVzdWx0YW5kbyBlbSB1bSBwb3N0byAkcihYKSA9IGsgPCBtJC4gUGFyYSB2aWFiaWxpemFyIGEgYW7DoWxpc2UgZGUgZXN0YWJpbGlkYWRlIGUgbyBjw6FsY3VsbyBkZSBlc3RpbWFkb3JlcyBkZSBtw61uaW1vcyBxdWFkcmFkb3MsIG8gZW5nZW5oZWlybyBwcmVjaXNhIGVuY29udHJhciBhIGludmVyc2EgZGUgTW9vcmUtUGVucm9zZSAkWF57K30kLiBDb25zaWRlcmFuZG8gYXMgcHJvcHJpZWRhZGVzIHRlw7NyaWNhcyBkYSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UsIHF1YWwgZGFzIGFsdGVybmF0aXZhcyBhYmFpeG8gZGVzY3JldmUgY29ycmV0YW1lbnRlIHVtYSBjb25kacOnw6NvIGZ1bmRhbWVudGFsIHF1ZSBhIG1hdHJpeiAkWF57K30kIGRldmUgc2F0aXNmYXplcj8iLCAiYWx0ZXJuYXRpdmFzIjogeyJBIjogIkEgbWF0cml6ICRYXnsrfSQgZGV2ZSBzZXIgb2JyaWdhdG9yaWFtZW50ZSBhIGludmVyc2EgY29tdW0gJFheey0xfSQsIG1lc21vIHF1ZSAkWCQgc2VqYSBzaW5ndWxhci4iLCAiQiI6ICJBIG1hdHJpeiAkWF57K30kIGRldmUgc2F0aXNmYXplciBhIGNvbmRpw6fDo28gJFggWF57K30gWCA9IFgkIGUgZ2FyYW50aXIgcXVlIHRhbnRvICRYIFheeyt9JCBxdWFudG8gJFheeyt9IFgkIHNlamFtIG1hdHJpemVzIFxcc2ltw6l0cmljYXMuIiwgIkMiOiAiQSBtYXRyaXogJFheeyt9JCBuw6NvIHByZWNpc2Egc2VyIMO6bmljYSwgZXhpc3RpbmRvIGluZmluaXRhcyBpbnZlcnNhcyBkZSBNb29yZS1QZW5yb3NlIHBhcmEgcXVhbHF1ZXIgbWF0cml6IGRhZGEuIiwgIkQiOiAiQSBtYXRyaXogJFheeyt9JCBkZXZlIHNhdGlzZmF6ZXIgJFheeyt9IFggPSBJX3sobil9JCwgaW5kZXBlbmRlbnRlbWVudGUgZG8gcG9zdG8gZGUgJFgkLiIsICJFIjogIkEgY29uZGnDp8OjbyBkZSBzaW1ldHJpYSBzw7Mgw6kgbmVjZXNzw6FyaWEgcGFyYSBhIG1hdHJpeiAkWF57K30kLCBuw6NvIHNlbmRvIGV4aWdpZGEgcGFyYSBvcyBwcm9kdXRvcyAkWCBYXnsrfSQgb3UgJFheeyt9IFgkLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiTGVtYnJlLXNlIGRhcyBxdWF0cm8gY29uZGnDp8O1ZXMgZGUgUGVucm9zZSBxdWUgZGVmaW5lbSBhIHVuaWNpZGFkZSBlIGEgZXhpc3TDqm5jaWEgZGEgaW52ZXJzYSBnZW5lcmFsaXphZGEuIiwgImdhYmFyaXRvX2NvbWVudGFkbyI6ICJBIGludmVyc2EgZGUgTW9vcmUtUGVucm9zZSAkWF57K30kIGRlIHVtYSBtYXRyaXogJFgkIMOpIGRlZmluaWRhIGNvbW8gYSDDum5pY2EgbWF0cml6IHF1ZSBzYXRpc2ZheiBxdWF0cm8gY29uZGnDp8O1ZXMsIGVudHJlIGVsYXM6IChpKSAkWCBYXnsrfSBYID0gWCQ7IChpaSkgJFheeyt9IFggWF57K30gPSBYXnsrfSQ7IChpaWkpICQoWCBYXnsrfSlee1x0b3B9ID0gWCBYXnsrfSQ7IGUgKGl2KSAkKFheeyt9IFgpXntcdG9wfSA9IFheeyt9IFgkLiBBcyBjb25kacOnw7VlcyAoaWlpKSBlIChpdikgZ2FyYW50ZW0gcXVlIG9zIHByb2R1dG9zICRYIFheeyt9JCBlICRYXnsrfSBYJCBzZWphbSBcXHNpbcOpdHJpY29zLCBvIHF1ZSDDqSBmdW5kYW1lbnRhbCBwYXJhIGEgZXN0YWJpbGlkYWRlIG51bcOpcmljYSBlIHByb3ByaWVkYWRlcyBkZSBwcm9qZcOnw6NvIGVtIG1vZGVsb3MgbGluZWFyZXMgWzEuMTBdLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTHVuYSAmIEVzdGV2ZXMsIEludHJvZHXDp8OjbyBhb3MgTW9kZWxvcyBMaW5lYXJlcywgQ2FwIDEsIHAuIDMzIn0sIHsiZW51bmNpYWRvIjogIlVtIGNpZW50aXN0YSBkZSBkYWRvcyB0cmFiYWxoYSBjb20gYSBkZWNvbXBvc2nDp8OjbyBkZSB1bWEgbWF0cml6IGRlIGdyYW5kZXMgZGltZW5zw7VlcyAkQV97KG4gXHRpbWVzIG0pfSQgZGUgcG9zdG8gJGskIHBhcmEgb3RpbWl6YXIgbyBjw6FsY3VsbyBkZSBzdWEgaW52ZXJzYSBnZW5lcmFsaXphZGEuIEVsZSBkZWNpZGUgdXRpbGl6YXIgYSBEZWNvbXBvc2nDp8OjbyBlbSBWYWxvcmVzIFNpbmd1bGFyZXMgKERWUyksIGRhZGEgcG9yICRBID0gVSBcdGV4dHtkaWFnfShcdGV4dHtzdn0pIFZee1x0b3B9JCwgb25kZSAkXHRleHR7c3Z9JCBzw6NvIG9zIHZhbG9yZXMgc2luZ3VsYXJlcy4gU2FiZW5kbyBxdWUgYSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2Ugw6kgY2FsY3VsYWRhIGF0cmF2w6lzIGRlc3NhIGRlY29tcG9zacOnw6NvIGNvbW8gJEFeeyt9ID0gViBcdGV4dHtkaWFnfShcdGV4dHtzdn1eeyt9KSBVXntcdG9wfSQsIG9uZGUgJFx0ZXh0e2RpYWd9KFx0ZXh0e3N2fV57K30pJCBjb250w6ltIG9zIGludmVyc29zIGRvcyB2YWxvcmVzIHNpbmd1bGFyZXMgbsOjbyBudWxvcywgcXVhbCBvIGltcGFjdG8gZGlyZXRvIGRhIHV0aWxpemHDp8OjbyBkYSBEVlMgcGFyYSBvIGPDoWxjdWxvIGRlICRBXnsrfSQgZW0gdGVybW9zIGNvbXB1dGFjaW9uYWlzIGUgdGXDs3JpY29zPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBEVlMgcmVkdXogbyBwb3N0byBkYSBtYXRyaXosIHRvcm5hbmRvIG8gY8OhbGN1bG8gZGUgJEFeeyt9JCBpbXByZWNpc28gZSBpbnN0w6F2ZWwuIiwgIkIiOiAiQSBEVlMgcGVybWl0ZSBpZGVudGlmaWNhciBjb21wb25lbnRlcyBudWxvcyBvdSBwcsOzeGltb3MgZGUgemVybyBub3MgdmFsb3JlcyBzaW5ndWxhcmVzLCBmYWNpbGl0YW5kbyBvIHRyYXRhbWVudG8gZGUgc2luZ3VsYXJpZGFkZXMgZSBnYXJhbnRpbmRvIGEgdW5pY2lkYWRlIGRlICRBXnsrfSQgYXRyYXbDqXMgZGUgdW1hIGRlY29tcG9zacOnw6NvIHJvYnVzdGEuIiwgIkMiOiAiTyBjw6FsY3VsbyB2aWEgRFZTIMOpIGNvbXB1dGFjaW9uYWxtZW50ZSBwcm9pYml0aXZvIHBhcmEgcXVhbHF1ZXIgbWF0cml6LCBzZW5kbyBzZW1wcmUgcHJlZmVyw612ZWwgdXNhciBhIGludmVyc8OjbyBkaXJldGEgZGUgc3VibWF0cml6ZXMuIiwgIkQiOiAiQSBEVlMgdHJhbnNmb3JtYSBhIG1hdHJpeiBvcmlnaW5hbCBlbSB1bWEgbWF0cml6IHRyaWFuZ3VsYXIsIG8gcXVlIGltcGVkZSBhIG9idGVuw6fDo28gZGEgaW52ZXJzYSBnZW5lcmFsaXphZGEuIiwgIkUiOiAiQSBpbnZlcnNhIGNhbGN1bGFkYSB2aWEgRFZTIG7Do28gc2F0aXNmYXogYSBjb25kacOnw6NvICRBIEFeeyt9IEEgPSBBJCBzZSBob3V2ZXIgdmFsb3JlcyBzaW5ndWxhcmVzIG51bG9zLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiQSBEVlMgZGVjb21ww7VlIGEgbWF0cml6IGVtIGVzcGHDp29zIG9ydG9nb25haXMsIHBlcm1pdGluZG8gaXNvbGFyIGEgaW5mb3JtYcOnw6NvIMO6dGlsICh2YWxvcmVzIHNpbmd1bGFyZXMgbsOjbyBudWxvcykgZG8gcnXDrWRvIG91IHJlZHVuZMOibmNpYSAodmFsb3JlcyBzaW5ndWxhcmVzIG51bG9zIG91IHF1YXNlIG51bG9zKS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgRFZTIMOpIHVtYSBmZXJyYW1lbnRhIHJvYnVzdGEgcG9pcyBwZXJtaXRlIGRlZmluaXIgY2xhcmFtZW50ZSBvIHBvc3RvIGRhIG1hdHJpeiBhdHJhdsOpcyBkb3MgdmFsb3JlcyBzaW5ndWxhcmVzIG7Do28gbnVsb3MuIEFvIGRlZmluaXIgJEFeeyt9ID0gViBcdGV4dHtkaWFnfShcdGV4dHtzdn1eeyt9KSBVXntcdG9wfSQsIGNvbSAkXHRleHR7c3Z9XnsrfSA9IDEvXHRleHR7c3Z9X2kkIHBhcmEgJFx0ZXh0e3N2fV9pID4gMCQgZSAkMCQgY2FzbyBjb250csOhcmlvLCBnYXJhbnRlLXNlIHF1ZSB0b2RhcyBhcyBwcm9wcmllZGFkZXMgZGUgTW9vcmUtUGVucm9zZSBzZWphbSBtYW50aWRhcywgbWVzbW8gZW0gbWF0cml6ZXMgbWFsIGNvbmRpY2lvbmFkYXMgb3UgY29tIGNvbHVuYXMgbGluZWFybWVudGUgZGVwZW5kZW50ZXMuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzLCBDYXAgMSwgcC4gMzcifSwgeyJlbnVuY2lhZG8iOiAiRW0gdW0gbW9kZWxvIGRlIHJlZ3Jlc3PDo28gbGluZWFyIGNsw6Fzc2ljbyAkWSA9IFhcYlxcZXRhICsgXFx2YXJlcHNpbG9uJCwgb25kZSAkWCQgw6kgdW1hIG1hdHJpeiBkZSBkZXNpZ24gZGUgZGltZW5zw6NvICQobiBcXHRpbWVzIHApJCBjb20gJFxcdGV4dHtwb3N0b30oWCkgPSBrIDwgcCQsIG8gc2lzdGVtYSBkZSBlcXVhw6fDtWVzIG5vcm1haXMgJFhee1xcdG9wfVhcXGhhdHtcYlxcZXRhfSA9IFhee1xcdG9wfVkkIG7Do28gcG9zc3VpIHVtYSBzb2x1w6fDo28gw7puaWNhLiBQYXJhIGNvbnRvcm5hciBhIHNpbmd1bGFyaWRhZGUgZGUgJFhee1xcdG9wfVgkLCB1dGlsaXphbW9zIHVtYSBpbnZlcnNhIGdlbmVyYWxpemFkYSAkRyQuIENvbnNpZGVyZSBxdWUgdW0gYW5hbGlzdGEgZGUgZGFkb3Mgb2J0ZXZlIGR1YXMgc29sdcOnw7VlcyBkaXN0aW50YXMgcGFyYSBvIHBhcsOibWV0cm8gJFxcYmV0YSQsIGRlbm90YWRhcyBwb3IgJFxcaGF0e1xiXFxldGF9XzEgPSBHXzEgWF57XFx0b3B9WSQgZSAkXFxoYXR7XGJcXGV0YX1fMiA9IEdfMiBYXntcXHRvcH1ZJCwgdXRpbGl6YW5kbyBkaWZlcmVudGVzIGludmVyc2FzIGdlbmVyYWxpemFkYXMgJEdfMSQgZSAkR18yJC4gUXVhbCBkYXMgc2VndWludGVzIHByb3ByaWVkYWRlcyBwZXJtYW5lY2UgaW52YXJpYW50ZSBwYXJhIHF1YWxxdWVyIGVzY29saGEgZGUgc29sdcOnw6NvICRcXGhhdHtcYlxcZXRhfSQ/IiwgImFsdGVybmF0aXZhcyI6IHsiQSI6ICJPIHZhbG9yIGVzdGltYWRvIGRvIHZldG9yIGRlIHBhcsOibWV0cm9zICRcXGhhdHtcYlxcZXRhfSQsIHF1ZSDDqSBzZW1wcmUgbyBtZXNtbyBpbmRlcGVuZGVudGVtZW50ZSBkZSAkRyQuIiwgIkIiOiAiQSBzb21hIGRlIHF1YWRyYWRvcyBkb3MgcmVzw61kdW9zICRTUUUgPSB8fFkgLSBYXFxoYXR7XGJcXGV0YX18fF4yJCwgcXVlIMOpIGNvbnN0YW50ZSBwYXJhIHF1YWxxdWVyIHNvbHXDp8OjbyBkbyBzaXN0ZW1hIGRlIGVxdWHDp8O1ZXMgbm9ybWFpcy4iLCAiQyI6ICJPIHZhbG9yIGRhIG5vcm1hICR8XFxoYXR7XGJcXGV0YX18XjIkLCBxdWUgw6kgaWTDqm50aWNvIHBhcmEgcXVhbHF1ZXIgaW52ZXJzYSBnZW5lcmFsaXphZGEuIiwgIkQiOiAiQSBtYXRyaXogJChJIC0gWEcgWF57XFx0b3B9KSQsIHF1ZSBzZSB0b3JuYSBpZGVudGlkYWRlIHBhcmEgcXVhbHF1ZXIgaW52ZXJzYSBnZW5lcmFsaXphZGEuIiwgIkUiOiAiTyBwb3N0byBkbyB2ZXRvciAkXFxoYXR7XGJcXGV0YX0kLCBxdWUgZGV2ZSBzZXIgaWd1YWwgYSAkcCQgZW0gdG9kb3Mgb3MgY2Fzb3MuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlLCBlbWJvcmEgYSBzb2x1w6fDo28gJFxcaGF0e1xiXFxldGF9JCBuw6NvIHNlamEgw7puaWNhIGVtIG1vZGVsb3MgZGUgcG9zdG8gaW5jb21wbGV0bywgYSBwcm9qZcOnw6NvIGRvIHZldG9yIGRlIG9ic2VydmHDp8O1ZXMgJFkkIG5vIGVzcGHDp28gY29sdW5hIGRhIG1hdHJpeiBkZSBkZXNpZ24sICRcXGhhdHtZfSA9IFhcXGhhdHtcYlxcZXRhfSQsIMOpIMO6bmljYS4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkVtIG1vZGVsb3MgZGUgcG9zdG8gaW5jb21wbGV0bywgbyBzaXN0ZW1hIGRlIGVxdWHDp8O1ZXMgbm9ybWFpcyAkWF57XFx0b3B9WFxcaGF0e1xiXFxldGF9ID0gWF57XFx0b3B9WSQgw6kgY29uc2lzdGVudGUsIG1hcyBwb3NzdWkgaW5maW5pdGFzIHNvbHXDp8O1ZXMuIEEgYXByb3hpbWHDp8OjbyBkZSBtw61uaW1vcyBxdWFkcmFkb3MgJFxcaGF0e1l9ID0gWFxcaGF0e1xiXFxldGF9JCDDqSDDum5pY2EgZSBpbnZhcmlhbnRlIHBhcmEgcXVhbHF1ZXIgc29sdcOnw6NvICRcXGhhdHtcYlxcZXRhfSQgZGFzIGVxdWHDp8O1ZXMgbm9ybWFpcywgcG9pcyAkWFxcaGF0e1xiXFxldGF9ID0gUCBZJCwgb25kZSAkUCA9IFgoWF57XFx0b3B9WCleey19WF57XFx0b3B9JCDDqSBvIHByb2pldG9yIG9ydG9nb25hbCDDum5pY28gc29icmUgbyBlc3Bhw6dvIGNvbHVuYSBkZSAkWCQuIENvbW8gJFxcaGF0e1l9JCDDqSDDum5pY28sIG8gdmV0b3IgZGUgcmVzw61kdW9zICRcXGhhdHtlfSA9IFkgLSBcXGhhdHtZfSQgZSBzdWEgbm9ybWEgYW8gcXVhZHJhZG8gJFNRRSA9IHx8XFxoYXR7ZX18fF4yJCB0YW1iw6ltIHPDo28gaW52YXJpYW50ZXMuIiwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hLCBKLiBHLiAmIEVzdGV2ZXMsIEUuIE0uLCBDYXAgMiwgcC4gNTUtNTcifSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIG8gc2lzdGVtYSBkZSBlcXVhw6fDtWVzIG5vcm1haXMgJFhee1xcdG9wfVhcXGhhdHtcYlxcZXRhfSA9IFhee1xcdG9wfVkkIGVtIHVtIG1vZGVsbyBsaW5lYXIgb25kZSAkWCQgdGVtIHBvc3RvIGluY29tcGxldG8gKCRyKFgpID0gayA8IHAkKS4gU2VqYSAkRyQgdW1hIGludmVyc2EgZ2VuZXJhbGl6YWRhIGRlICRYXntcXHRvcH1YJC4gQSBzb2x1w6fDo28gZ2VyYWwgcGFyYSBvIHZldG9yIGRlIHBhcsOibWV0cm9zIMOpIGRhZGEgcG9yICRcXGhhdHtcYlxcZXRhfSA9IEdYXntcXHRvcH1ZICsgKEkgLSBHWF57XFx0b3B9WCl6JCwgb25kZSAkeiQgw6kgdW0gdmV0b3IgYXJiaXRyw6FyaW8gZGUgZGltZW5zw6NvICQocCBcXHRpbWVzIDEpJC4gU2UgdW0gcGVzcXVpc2Fkb3IgZGVzZWphIG9idGVyIHVtYSBzb2x1w6fDo28gZXNwZWPDrWZpY2EgY29tIG5vcm1hIG3DrW5pbWEsIGVsZSBkZXZlOiIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiRXNjb2xoZXIgdW0gdmV0b3IgJHokIHRhbCBxdWUgJChJIC0gR1hee1xcdG9wfVgpeiA9IDAkLiIsICJCIjogIlV0aWxpemFyIGEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlICQoWF57XFx0b3B9WCleeyt9JCwgcXVlIGdhcmFudGUgYSBzb2x1w6fDo28gZGUgbm9ybWEgbcOtbmltYSBlbnRyZSB0b2RhcyBhcyBzb2x1w6fDtWVzIHBvc3PDrXZlaXMuIiwgIkMiOiAiU2VtcHJlIGRlZmluaXIgJHokIGNvbW8gdW0gdmV0b3IgZGUgemVyb3MsIHBvaXMgcXVhbHF1ZXIgc29sdcOnw6NvIGZvcm5lY2UgbyBtZXNtbyB2YWxvciBwYXJhICR8XFxoYXR7XGJcXGV0YX18XjIkLiIsICJEIjogIkF1bWVudGFyIG8gdGFtYW5obyBhbW9zdHJhbCAkbiQgYXTDqSBxdWUgJFhee1xcdG9wfVgkIHNlIHRvcm5lIGludmVyc8OtdmVsLiIsICJFIjogIlN1YnN0aXR1aXIgJEckIHBlbGEgbWF0cml6IGlkZW50aWRhZGUgJElfeyhwKX0kLCBvIHF1ZSBzZW1wcmUgbWluaW1pemEgYSBub3JtYSBkZSAkXFxoYXR7XGJcXGV0YX0kLiJ9LCAiYWx0ZXJuYXRpdmFfY29ycmV0YSI6ICJCIiwgImRpY2EiOiAiQSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgcG9zc3VpIHByb3ByaWVkYWRlcyDDum5pY2FzIHF1ZSBlc3RlbmRlbSBvIGNvbmNlaXRvIGRlIGludmVyc2EgdXN1YWwsIGluY2x1c2l2ZSBwYXJhIHNpc3RlbWFzIGluZGV0ZXJtaW5hZG9zLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiQSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgJChYXntcXHRvcH1YKV57K30kIMOpIMO6bmljYSBlLCBxdWFuZG8gdXRpbGl6YWRhIG5hIGZvcm1hICRcXGhhdHtcYlxcZXRhfSA9IChYXntcXHRvcH1YKV57K31YXntcXHRvcH1ZJCwgZm9ybmVjZSBhIHNvbHXDp8OjbyBwYXJ0aWN1bGFyIHF1ZSBtaW5pbWl6YSBhIG5vcm1hIGV1Y2xpZGlhbmEgJHxcXGhhdHtcYlxcZXRhfXxeMiQgZW50cmUgdG9kYXMgYXMgc29sdcOnw7VlcyBkbyBzaXN0ZW1hIGRlIGVxdWHDp8O1ZXMgbm9ybWFpcy4gQXMgb3V0cmFzIGludmVyc2FzIGdlbmVyYWxpemFkYXMgJEckIHByb2R1emVtIHNvbHXDp8O1ZXMgZGlmZXJlbnRlcywgZGVwZW5kZW5kbyBkYSBlc2NvbGhhIGRlICR6JCwgbWFzIG7Do28gZ2FyYW50ZW0gZXNzYSBwcm9wcmllZGFkZSBkZSBub3JtYSBtw61uaW1hLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTHVuYSwgSi4gRy4gJiBFc3RldmVzLCBFLiBNLiwgQ2FwIDIsIHAuIDUwLTUxIn0sIHsiZW51bmNpYWRvIjogIkVtIHVtIHNpc3RlbWEgZGUgbW9uaXRvcmFtZW50byBkZSBzZW5zb3JlcyBJb1QsIGEgbWF0cml6IGRlIGNvbmZpZ3VyYcOnw6NvICRBX3s0IFx0aW1lcyAzfSQgcG9zc3VpIHBvc3RvIGNvbHVuYSBjb21wbGV0byAkcihBKSA9IDMkLiBBbyB0ZW50YXIgcmVzb2x2ZXIgbyBzaXN0ZW1hIGxpbmVhciAkQXggPSBnJCBwYXJhIGRldGVybWluYXIgb3MgZXN0YWRvcyBkb3Mgc2Vuc29yZXMsIG9ic2VydmEtc2UgcXVlIG8gc2lzdGVtYSDDqSBjb25zaXN0ZW50ZS4gQ29uc2lkZXJhbmRvIGEgaW52ZXJzYSBkZSBtw61uaW1vcyBxdWFkcmFkb3MgJEFee2x9JCwgcXVhbCBkYXMgc2VndWludGVzIGFmaXJtYcOnw7VlcyBzb2JyZSBhIG1hdHJpeiAkQUFee2x9JCDDqSBjb3JyZXRhPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBtYXRyaXogJEFBXntsfSQgw6kgc2VtcHJlIGEgbWF0cml6IGlkZW50aWRhZGUgJElfezR9JC4iLCAiQiI6ICJBIG1hdHJpeiAkQUFee2x9JCDDqSBvIHByb2pldG9yIG9ydG9nb25hbCBzb2JyZSBvIGVzcGHDp28gY29sdW5hIGRhIG1hdHJpeiAkQSQsIHNlbmRvIMO6bmljYSBlIGludmFyaWFudGUsIGluZGVwZW5kZW50ZW1lbnRlIGRhIGVzY29saGEgZGUgJEFee2x9JC4iLCAiQyI6ICJBIG1hdHJpeiAkQUFee2x9JCBuw6NvIMOpIG5lY2Vzc2FyaWFtZW50ZSBcXHNpbcOpdHJpY2EsIHBvaXMgZGVwZW5kZSBkYSBlc2NvbGhhIGVzcGVjw61maWNhIGRhIGludmVyc2EgY29uZGljaW9uYWwgdXRpbGl6YWRhLiIsICJEIjogIk8gcHJvZHV0byAkQUFee2x9JCBkZXBlbmRlIGRvIHZldG9yICRnJCwgbG9nbyBzZXUgdmFsb3IgYWx0ZXJhLXNlIGNvbmZvcm1lIGEgZW50cmFkYSBkb3MgZGFkb3MgZG9zIHNlbnNvcmVzLiIsICJFIjogIkEgbWF0cml6ICRBQV57bH0kIMOpIGRlZmluaWRhIGFwZW5hcyBzZSAkQSQgZm9yIHVtYSBtYXRyaXogcXVhZHJhZGEgbsOjbyBzaW5ndWxhci4ifSwgImFsdGVybmF0aXZhX2NvcnJldGEiOiAiQiIsICJkaWNhIjogIkxlbWJyZS1zZSBkYSBwcm9wcmllZGFkZSBkbyBwcm9qZXRvciBhc3NvY2lhZGEgw6AgaW52ZXJzYSBkZSBtw61uaW1vcyBxdWFkcmFkb3MgZSBjb21vIGVsYSBhdHVhIHNvYnJlIG8gZXNwYcOnbyBjb2x1bmEgZGUgJEEkLiBBIHVuaWNpZGFkZSBkbyBwcm9qZXRvciDDqSB1bSByZXN1bHRhZG8gZnVuZGFtZW50YWwgZW0gbW9kZWxvcyBsaW5lYXJlcy4iLCAiZ2FiYXJpdG9fY29tZW50YWRvIjogIkEgbWF0cml6ICRBXntsfSQgw6kgdW1hIGludmVyc2EgZGUgbcOtbmltb3MgcXVhZHJhZG9zIHNlIHNhdGlzZmF6ICRBQV57bH1BID0gQSQgZSAkQUFee2x9ID0gKEFBXntsfSlee1x0b3B9JC4gUGFyYSBxdWFscXVlciBpbnZlcnNhIGRlIG3DrW5pbW9zIHF1YWRyYWRvcywgbyBwcm9kdXRvICRBQV57bH0kIGF0dWEgY29tbyBvIHByb2pldG9yIG9ydG9nb25hbCBzb2JyZSBvIGVzcGHDp28gY29sdW5hIGRlICRBJC4gVW1hIHByb3ByaWVkYWRlIGNlbnRyYWwgw6kgcXVlLCBlbWJvcmEgYSBpbnZlcnNhICRBXntsfSQgbsOjbyBzZWphIG5lY2Vzc2FyaWFtZW50ZSDDum5pY2EsIG8gcHJvZHV0byAkQUFee2x9JCDDqSDDum5pY28gZSBpbnZhcmlhbnRlIHBhcmEgcXVhbHF1ZXIgZXNjb2xoYSBkZSB1bWEgaW52ZXJzYSBjb25kaWNpb25hbCBxdWUgc2F0aXNmYcOnYSBhcyBjb25kacOnw7VlcyBkZSBtw61uaW1vcyBxdWFkcmFkb3MuIFBvcnRhbnRvLCBhIGFsdGVybmF0aXZhIEIgw6kgYSBjb3JyZXRhLiBBcyBvdXRyYXMgZXN0w6NvIGluY29ycmV0YXMgcG9pcyAkQUFee2x9JCBuw6NvIMOpIGEgaWRlbnRpZGFkZSAobyBwb3N0byDDqSAkcihBKSA8IDQkKSwgw6kgc2VtcHJlIFxcc2ltw6l0cmljYSwgbsOjbyBkZXBlbmRlIGRlICRnJCBlIGV4aXN0ZSBwYXJhIG1hdHJpemVzIG7Do28gcXVhZHJhZGFzLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTHVuYSwgSi4gRy4gJiBFc3RldmVzLCBFLiBNLiwgRXN0YXTDrXN0aWNhIELDoXNpY2EsIENhcCAxLCBwLiA0MCJ9LCB7ImVudW5jaWFkbyI6ICJTZWphICRBJCB1bWEgbWF0cml6ICRuIFx0aW1lcyBtJCBkZSBwb3N0byAkayQuIEEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlICRBXnsrfSQgw6kgYSDDum5pY2EgbWF0cml6IHF1ZSBzYXRpc2ZheiBxdWF0cm8gY29uZGnDp8O1ZXMgZnVuZGFtZW50YWlzLiBDb25zaWRlcmUgbyBjZW7DoXJpbyBvbmRlICRuID0gbSQgZSAkQSQgw6kgdW1hIG1hdHJpeiBpZGVtcG90ZW50ZSAoJEFeMiA9IEEkKS4gUXVhbCBkYXMgcHJvcHJpZWRhZGVzIGFiYWl4byDDqSB2ZXJkYWRlaXJhIHBhcmEgJEFeeyt9JCBuZXN0ZSBjYXNvIGVzcGVjw61maWNvPyIsICJhbHRlcm5hdGl2YXMiOiB7IkEiOiAiQSBtYXRyaXogJEFeeyt9JCDDqSBuZWNlc3NhcmlhbWVudGUgYSBpbnZlcnNhIGNsw6Fzc2ljYSAkQV57LTF9JC4iLCAiQiI6ICJBIG1hdHJpeiAkQV57K30kIMOpIGlndWFsIMOgIHByw7NwcmlhIG1hdHJpeiAkQSQuIiwgIkMiOiAiQSBtYXRyaXogJEFeeyt9JCDDqSBpZ3VhbCDDoCBtYXRyaXogdHJhbnNwb3N0YSAkQV57XHRvcH0kIGFwZW5hcyBzZSAkQSQgZm9yIFxcc2ltw6l0cmljYS4iLCAiRCI6ICJPIHBvc3RvIGRlICRBXnsrfSQgw6kgc2VtcHJlIG1haW9yIHF1ZSBvIHBvc3RvIGRlICRBJC4iLCAiRSI6ICJBIG1hdHJpeiAkQV57K30kIGRldmUgc2VyIG51bGEuIn0sICJhbHRlcm5hdGl2YV9jb3JyZXRhIjogIkIiLCAiZGljYSI6ICJDb25zdWx0ZSBvIFRlb3JlbWEgMyBkYXMgcHJvcHJpZWRhZGVzIGRhIGludmVyc2EgZGUgTW9vcmUtUGVucm9zZSBwYXJhIG1hdHJpemVzIFxcc2ltw6l0cmljYXMgb3UgY29uc2lkZXJlIGEgZGVmaW5pw6fDo28gZGUgaWRlbXBvdMOqbmNpYSBlIGEgdW5pY2lkYWRlIGRhIGludmVyc2EgZGUgTS1QLiIsICJnYWJhcml0b19jb21lbnRhZG8iOiAiRGUgYWNvcmRvIGNvbSBhcyBwcm9wcmllZGFkZXMgZGEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlIChUZW9yZW1hIDMsIHNsaWRlIDE0IGRhIEF1bGEgOSksIHNlIHVtYSBtYXRyaXogJEEkIMOpIGlkZW1wb3RlbnRlICgkQV4yID0gQSQpLCBlbnTDo28gc3VhIGludmVyc2EgZGUgTW9vcmUtUGVucm9zZSAkQV57K30kIMOpIGEgcHLDs3ByaWEgbWF0cml6ICRBJC4gSXNzbyBwb2RlIHNlciB2ZXJpZmljYWRvIGNoZWNhbmRvIGFzIHF1YXRybyBjb25kacOnw7VlcyBkZSBQZW5yb3NlOiAkQUFeeyt9QSA9IEFBQSA9IEFeMiA9IEEkOyAkQV57K31BQV57K30gPSBBQUEgPSBBXjIgPSBBID0gQV57K30kOyAkKEFeeyt9QSlee1x0b3B9ID0gKEFeMilee1x0b3B9ID0gQV57XHRvcH0kIGUgJChBQV57K30pXntcdG9wfSA9IChBXjIpXntcdG9wfSA9IEFee1x0b3B9JC4gQ29tbyAkQSQgw6kgaWRlbXBvdGVudGUgZSwgbmVzdGUgY29udGV4dG8sIHRyYXRhbW9zIGRlIHByb3ByaWVkYWRlcyBkZSBwcm9qZcOnw6NvLCBhIGlndWFsZGFkZSAkQV57K30gPSBBJCDDqSBzYXRpc2ZlaXRhLiIsICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTsOtdmVhIEJpc3BvLCBBdWxhIDk6IEludmVyc2EgR2VuZXJhbGl6YWRhIGRlIE1hdHJpemVzLCBzbGlkZSAxNCJ9XSwgInF1ZXN0b2VzX2Rpc2N1cnNpdmFzIjogW3siZW51bmNpYWRvIjogIkV4cGxpcXVlLCBzb2IgbyBwb250byBkZSB2aXN0YSBkYSDDgWxnZWJyYSBMaW5lYXIgYXBsaWNhZGEgYSBNb2RlbG9zIExpbmVhcmVzLCBwb3IgcXVlIGEgaW52ZXJzw6NvIGNsw6Fzc2ljYSBkZSBtYXRyaXplcyAkQV57LTF9JCBmYWxoYSBxdWFuZG8gYSBtYXRyaXogZGUgcGxhbmVqYW1lbnRvIHBvc3N1aSBwb3N0byBkZWZpY2llbnRlLiBFbSBzZWd1aWRhLCBkZXNjcmV2YSBjb21vIGEgaW52ZXJzYSBjb25kaWNpb25hbCAkQV57LX0kIHZpYWJpbGl6YSBhIHNvbHXDp8OjbyBkZSBzaXN0ZW1hcyBsaW5lYXJlcyBjb25zaXN0ZW50ZXMuIiwgImRpY2EiOiAiQ29uc2lkZXJlIGFzIHByb3ByaWVkYWRlcyBkZSBwb3N0byBkZSBtYXRyaXplcyAoJHIoQSkkKSBlIGEgcmVsYcOnw6NvIGVudHJlIG8gZGV0ZXJtaW5hbnRlIGUgYSBleGlzdMOqbmNpYSBkYSBpbnZlcnNhLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBBIGV4aXN0w6puY2lhIGRhIGludmVyc2EgY2zDoXNzaWNhICRBXnstMX0kIHJlcXVlciBxdWUgJEEkIHNlamEgcXVhZHJhZGEgKCRuPW0kKSBlIG7Do28gc2luZ3VsYXIsIG91IHNlamEsICRcXGRldChBKSBcXG5lcSAwJCwgbyBxdWUgaW1wbGljYSAkcihBKSA9IG4kLiIsICIyLiBFbSBtb2RlbG9zIGNvbSBtdWx0aWNvbGluZWFyaWRhZGUsICRyKEEpIDwgbSQsIGxvZ28gJFxcZGV0KEFee1xccHJpbWV9QSkgPSAwJCwgaW1wb3NzaWJpbGl0YW5kbyBhIGludmVyc8OjbyB0cmFkaWNpb25hbC4iLCAiMy4gQSBpbnZlcnNhIGNvbmRpY2lvbmFsICRBXnstfSQgw6kgZGVmaW5pZGEgcGVsYSBjb25kacOnw6NvICRBIEFeey19IEEgPSBBJC4iLCAiNC4gUGFyYSB1bSBzaXN0ZW1hIGNvbnNpc3RlbnRlICRBeD1nJCwgYW8gYXBsaWNhciAkeCA9IEFeey19ZyQsIHRlbW9zICRBeCA9IEEoQV57LX1nKSA9IChBQV57LX1BKXggPSBBeCA9IGckLiBBc3NpbSwgJEFeey19ZyQgZm9ybmVjZSB1bWEgc29sdcOnw6NvIHbDoWxpZGEgcGFyYSBvIHNpc3RlbWEsIG1lc21vIHF1ZSBhIG1hdHJpeiBzZWphIHNpbmd1bGFyLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEgJiBFc3RldmVzLCBJbnRyb2R1w6fDo28gYW9zIE1vZGVsb3MgTGluZWFyZXMsIENhcCAyLCBwLiAzNy00MCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJEYWRhIGEgbWF0cml6ICRBID0gXFxiZWdpbntwbWF0cml4fSAxICYgMSAmIDAgXFxcXCAxICYgMSAmIDAgXFxcXCAxICYgMCAmIDEgXFxcXCAxICYgMCAmIDEgXFxlbmR7cG1hdHJpeH0kIGUgdW1hIGNhbmRpZGF0YSBhIGludmVyc2EgY29uZGljaW9uYWwgJEFeey19ID0gXFxiZWdpbntwbWF0cml4fSAwICYgMCAmIDAgJiAwIFxcXFwgMCAmIDEgJiAwICYgMCBcXFxcIDAgJiAwICYgMSAmIDAgXFxlbmR7cG1hdHJpeH0kLCB2ZXJpZmlxdWUgc2UgZXN0YSBtYXRyaXogc2F0aXNmYXogYSBjb25kacOnw6NvIGZ1bmRhbWVudGFsICRBQV57LX1BID0gQSQuIiwgImRpY2EiOiAiUmVhbGl6ZSBhIG11bHRpcGxpY2HDp8OjbyBtYXRyaWNpYWwgcG9yIHBhcnRlczogcHJpbWVpcm8gJE0gPSBBQV57LX0kLCBkZXBvaXMgbyByZXN1bHRhZG8gdmV6ZXMgJEEkLiBWZXJpZmlxdWUgc2UgJE1BID0gQSQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIENhbGN1bGFuZG8gJEFBXnstfSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgJiAwIFxcXFwgMSAmIDEgJiAwIFxcXFwgMSAmIDAgJiAxIFxcXFwgMSAmIDAgJiAxIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMCAmIDAgJiAwICYgMCBcXFxcIDAgJiAxICYgMCAmIDAgXFxcXCAwICYgMCAmIDEgJiAwIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAwICYgMSAmIDAgJiAwIFxcXFwgMCAmIDEgJiAwICYgMCBcXFxcIDAgJiAwICYgMSAmIDAgXFxcXCAwICYgMCAmIDEgJiAwIFxcZW5ke3BtYXRyaXh9JC4iLCAiMi4gQ2FsY3VsYW5kbyAkKEFBXnstfSlBID0gXFxiZWdpbntwbWF0cml4fSAwICYgMSAmIDAgJiAwIFxcXFwgMCAmIDEgJiAwICYgMCBcXFxcIDAgJiAwICYgMSAmIDAgXFxcXCAwICYgMCAmIDEgJiAwIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgJiAwIFxcXFwgMSAmIDEgJiAwIFxcXFwgMSAmIDAgJiAxIFxcXFwgMSAmIDAgJiAxIFxcZW5ke3BtYXRyaXh9JC4iLCAiMy4gTyByZXN1bHRhZG8gZGEgbXVsdGlwbGljYcOnw6NvIMOpOiAkXFxiZWdpbntwbWF0cml4fSAxICYgMSAmIDAgXFxcXCAxICYgMSAmIDAgXFxcXCAxICYgMCAmIDEgXFxcXCAxICYgMCAmIDEgXFxlbmR7cG1hdHJpeH0gPSBBJC4iLCAiNC4gQ29tbyAkQUFeey19QSA9IEEkLCBhIG1hdHJpeiDDqSBjb25maXJtYWRhIGNvbW8gdW1hIGludmVyc2EgY29uZGljaW9uYWwgdsOhbGlkYS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzLCBDYXAgMiwgcC4gNDAiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGlzY29ycmEgc29icmUgYSBpbXBvcnTDom5jaWEgZGEgaW52ZXJzYSBjb25kaWNpb25hbCBlbSBtb2RlbG9zIGRlIHJlZ3Jlc3PDo28gbGluZWFyIGNvbSBkYWRvcyBkZXNiYWxhbmNlYWRvcyBvdSBzdXBlcnBhcmFtZXRyaXphZG9zLiBQb3IgcXVlIGEgdW5pY2lkYWRlIGRhIGludmVyc2EgbsOjbyDDqSB1bSByZXF1aXNpdG8gZXN0cml0byBuZXNzZXMgY2Fzb3MsIGVucXVhbnRvIGEgY29uZGnDp8OjbyAkQUFeey19QSA9IEEkIG8gw6k/IiwgImRpY2EiOiAiUGVuc2Ugbm8gcXVlIHJlYWxtZW50ZSBpbXBvcnRhIG5hIHByZWRpw6fDo28gJFxcaGF0e1l9ID0gWFxcaGF0e1xcdGhldGF9JCBlbSByZWxhw6fDo28gw6AgdmFyaWFiaWxpZGFkZSBleHBsaWNhZGEgcGVsbyBtb2RlbG8uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIEVtIG1vZGVsb3MgY29tIG11bHRpY29saW5lYXJpZGFkZSwgbyBzaXN0ZW1hIGRlIGVxdWHDp8O1ZXMgbm9ybWFpcyAkWF57XFxwcmltZX1YXFx0aGV0YSA9IFhee1xccHJpbWV9WSQgbsOjbyBwb3NzdWkgc29sdcOnw6NvIMO6bmljYS4iLCAiMi4gQSBpbnZlcnNhIGNvbmRpY2lvbmFsICRBXnstfSQgcGVybWl0ZSBvYnRlciB1bWEgc29sdcOnw6NvIHBhcnRpY3VsYXIgJFxcaGF0e1xcdGhldGF9ID0gQV57LX1YXntcXHByaW1lfVkkLiIsICIzLiBFbWJvcmEgJFxcaGF0e1xcdGhldGF9JCBuw6NvIHNlamEgw7puaWNvLCBvIHZhbG9yIHByZWRpdG8gJFxcaGF0e1l9ID0gWFxcaGF0e1xcdGhldGF9JCDDqSBpbnZhcmlhbnRlIGVtIHJlbGHDp8OjbyDDoCBlc2NvbGhhIGRhIGludmVyc2EgY29uZGljaW9uYWwsIGRlc2RlIHF1ZSBvIHNpc3RlbWEgc2VqYSBjb25zaXN0ZW50ZS4iLCAiNC4gQSBjb25kacOnw6NvICRBQV57LX1BID0gQSQgw6kgc3VmaWNpZW50ZSBwYXJhIGdhcmFudGlyIHF1ZSAkWFxcaGF0e1xcdGhldGF9JCBtaW5pbWl6ZSBhIHNvbWEgZGUgcXVhZHJhZG9zIGRvcyByZXPDrWR1b3MsIHF1ZSDDqSBvIG9iamV0aXZvIGNlbnRyYWwgZGEgcmVncmVzc8OjbywgbsOjbyBzZW5kbyBuZWNlc3PDoXJpYSBhIHVuaWNpZGFkZSBkYSBtYXRyaXogaW52ZXJzYSBwYXJhIGEgaW5mZXLDqm5jaWEgdsOhbGlkYS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzLCBDYXAgMiwgcC4gNDEtNDIiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiU2VqYSAkQSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFwgMCAmIDEgXFwgMCAmIDAgXFxlbmR7cG1hdHJpeH0kLiBWZXJpZmlxdWUgc2UgYSBtYXRyaXogJEFeeyt9ID0gXFxiZWdpbntwbWF0cml4fSAxICYgMCAmIDAgXFwgMCAmIDEgJiAwIFxcZW5ke3BtYXRyaXh9JCBzYXRpc2ZheiBhcyBxdWF0cm8gY29uZGnDp8O1ZXMgZGUgUGVucm9zZS4gRGVtb25zdHJlIG8gY8OhbGN1bG8gcGFyYSBjYWRhIGNvbmRpw6fDo28uIiwgImRpY2EiOiAiQ2FsY3VsZSAkQUFeeyt9JCBlICRBXnsrfUEkIHByaW1laXJvIGUgdmVyaWZpcXVlIGFzIHByb3ByaWVkYWRlcyBkZSBzaW1ldHJpYSBlIGlkZW1wb3TDqm5jaWEsIHNlZ3VpZGFzIGRhcyBjb25kacOnw7VlcyBkZSBpZ3VhbGRhZGUgZGEgaW52ZXJzYSBnZW5lcmFsaXphZGEuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IENhbGN1bGFyICRBQV57K30gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwIFxcIDAgJiAxIFxcIDAgJiAwIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgJiAwIFxcIDAgJiAxICYgMCBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgJiAwIFxcIDAgJiAxICYgMCBcXCAwICYgMCAmIDAgXFxlbmR7cG1hdHJpeH0kLiBOb3RlIHF1ZSDDqSBcXHNpbcOpdHJpY2EuIiwgIlBhc3NvIDI6IENhbGN1bGFyICRBXnsrfUEgPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwICYgMCBcXCAwICYgMSAmIDAgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSAxICYgMCBcXCAwICYgMSBcXCAwICYgMCBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFwgMCAmIDEgXFxlbmR7cG1hdHJpeH0gPSBJX3soMil9JC4gTm90ZSBxdWUgw6kgXFxzaW3DqXRyaWNhLiIsICJQYXNzbyAzOiBWZXJpZmljYXIgJEFBXnsrfUEgPSAoQUFeeyt9KUEgPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwICYgMCBcXCAwICYgMSAmIDAgXFwgMCAmIDAgJiAwIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFwgMCAmIDEgXFwgMCAmIDAgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwIFxcIDAgJiAxIFxcIDAgJiAwIFxcZW5ke3BtYXRyaXh9ID0gQSQuIiwgIlBhc3NvIDQ6IFZlcmlmaWNhciAkQV57K31BQV57K30gPSBBXnsrfShBQV57K30pID0gXFxiZWdpbntwbWF0cml4fSAxICYgMCAmIDAgXFwgMCAmIDEgJiAwIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgJiAwIFxcIDAgJiAxICYgMCBcXCAwICYgMCAmIDAgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwICYgMCBcXCAwICYgMSAmIDAgXFxlbmR7cG1hdHJpeH0gPSBBXnsrfSQuIiwgIkNvbmNsdXPDo286IENvbW8gYXMgcXVhdHJvIGNvbmRpw6fDtWVzIGZvcmFtIHZlcmlmaWNhZGFzLCBhIG1hdHJpeiAkQV57K30kIMOpIGEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlIGRlICRBJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6IG51bGwsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJFeHBsaXF1ZSwgc29iIGEgcGVyc3BlY3RpdmEgZGEgdGVvcmlhIGRlIHNpc3RlbWFzIGxpbmVhcmVzLCBwb3IgcXVlIGEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlIMOpIHByZWZlcsOtdmVsIMOgIGludmVyc2EgY29uZGljaW9uYWwgY29tdW0gKCRBXnstfSQpIHF1YW5kbyBidXNjYW1vcyB1bWEgc29sdcOnw6NvIMO6bmljYSBwYXJhIHVtIHNpc3RlbWEgaW5jb25zaXN0ZW50ZSAkQXg9ZyQuIiwgImRpY2EiOiAiQ29uc2lkZXJlIGEgcHJvcHJpZWRhZGUgZGUgdW5pY2lkYWRlIGRhIGludmVyc2EgZGUgTW9vcmUtUGVucm9zZSBlIG8gcGFwZWwgZG9zIHByb2pldG9yZXMgJEFBXnsrfSQgZSAkQV57K31BJCBuYSBtaW5pbWl6YcOnw6NvIGRhIG5vcm1hIGRvIGVycm8uIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIlBhc3NvIDE6IEEgaW52ZXJzYSBjb25kaWNpb25hbCBjb211bSAkQV57LX0kIHNhdGlzZmF6IGFwZW5hcyAkQUFeey19QT1BJCwgbsOjbyBzZW5kbywgZW0gZ2VyYWwsIMO6bmljYS4iLCAiUGFzc28gMjogQSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgJEFeeyt9JCDDqSDDum5pY2EsIGNvbmZvcm1lIGRlbW9uc3RyYWRvIHBlbG8gVGVvcmVtYSBkZSBQZW5yb3NlLiIsICJQYXNzbyAzOiBFbSBzaXN0ZW1hcyBpbmNvbnNpc3RlbnRlcywgYSBzb2x1w6fDo28gJHggPSBBXnsrfWckIGZvcm5lY2UgYSBzb2x1w6fDo28gZGUgbcOtbmltb3MgcXVhZHJhZG9zIGNvbSBhIG1lbm9yIG5vcm1hIGV1Y2xpZGlhbmEgZW50cmUgdG9kYXMgYXMgc29sdcOnw7VlcyBwb3Nzw612ZWlzLiIsICJQYXNzbyA0OiBJc3NvIG9jb3JyZSBkZXZpZG8gw6BzIHByb3ByaWVkYWRlcyBkZSBzaW1ldHJpYSBlIGlkZW1wb3TDqm5jaWEgZG9zIHByb2pldG9yZXMgJEFBXnsrfSQgZSAkQV57K31BJCwgcXVlIGdhcmFudGVtIHByb2plw6fDtWVzIG9ydG9nb25haXMgc29icmUgb3MgZXNwYcOnb3MgY29sdW5hcmVzIGRlICRBJC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJCaXNwbywgTi4sIEF1bGEgOTogSW52ZXJzYSBHZW5lcmFsaXphZGEgZGUgTWF0cml6ZXMsIHAuIDEwIiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSB1bWEgbWF0cml6ICRBJCAkKG4gXHRpbWVzIG0pJCBjb20gcG9zdG8gJHIoQSkgPSBrJC4gU2UgYSBkZWNvbXBvc2nDp8OjbyBlbSB2YWxvcmVzIHNpbmd1bGFyZXMgKERWUykgZGUgJEEkIMOpIGRhZGEgcG9yICRBID0gVSBcXExhbWJkYV57MS8yfSBWXntcXHRvcH0kLCBvbmRlICRVJCAkKG4gXHRpbWVzIG4pJCBlICRWJCAkKG0gXHRpbWVzIG0pJCBzw6NvIG9ydG9nb25haXMgZSAkXFxMYW1iZGFeezEvMn0kIGNvbnTDqW0gYXMgcmHDrXplcyBxdWFkcmFkYXMgZG9zIGF1dG92YWxvcmVzIG7Do28gbnVsb3MsIGRldGVybWluZSBhIGV4cHJlc3PDo28gZGEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlICRBXnsrfSQgZW0gdGVybW9zIGRhcyBtYXRyaXplcyBkYSBEVlMuIiwgImRpY2EiOiAiQ29uc2lkZXJlIGEgcmVsYcOnw6NvICRBXnsrfSA9IFYgXFxMYW1iZGFeeyt9IFVee1xcdG9wfSQsIG9uZGUgJFxcTGFtYmRhXnsrfSQgw6kgYSBwc2V1ZG9pbnZlcnNhIGRhIG1hdHJpeiBkaWFnb25hbC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogRGFkYSAkQSA9IFUgXFxMYW1iZGFeezEvMn0gVl57XFx0b3B9JCwgb25kZSAkXFxMYW1iZGFeezEvMn0kIMOpIGRpYWdvbmFsIGNvbSBlbnRyYWRhcyAkXFxzaWdtYV9pID0gXFxzcXJ0e1xcbGFtYmRhX2l9JCBwYXJhICRpPTEsIFxcZG90cywgayQuIiwgIlBhc3NvIDI6IEEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlIMOpIGRlZmluaWRhIHBvciAkQV57K30gPSBWIFxcTGFtYmRhXnsrfSBVXntcXHRvcH0kLiIsICJQYXNzbyAzOiBBIG1hdHJpeiAkXFxMYW1iZGFeeyt9JCDDqSB1bWEgbWF0cml6ICQobSBcdGltZXMgbikkIGRpYWdvbmFsIHRhbCBxdWUgJFxcbGFtYmRhXnsrfV97aWl9ID0gMS9cXHNpZ21hX2kkIHBhcmEgJGk9MSwgXFxkb3RzLCBrJCwgZSB6ZXJvIGNhc28gY29udHLDoXJpby4iLCAiUGFzc28gNDogRXN0YSBjb25zdHJ1w6fDo28gZ2FyYW50ZSBhIHNhdGlzZmHDp8OjbyBkYXMgcXVhdHJvIGNvbmRpw6fDtWVzIGRlIFBlbnJvc2UgcGVsYSBvcnRvZ29uYWxpZGFkZSBkZSAkVSQgZSAkViQgZSBwZWxhIGVzdHJ1dHVyYSBkZSBpbnZlcnPDo28gZGEgcGFydGUgZGlhZ29uYWwuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiQmlzcG8sIE4uLCBBdWxhIDk6IEludmVyc2EgR2VuZXJhbGl6YWRhIGRlIE1hdHJpemVzLCBwLiA5IiwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBhIG1hdHJpeiAkQSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgXFwgMSAmIDEgXFxlbmR7cG1hdHJpeH0kLiBFc3RhIG1hdHJpeiDDqSBzaW5ndWxhciAoJHIoQSkgPSAxJCkuIENhbGN1bGUgYSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgJEFeeyt9JCB1dGlsaXphbmRvIG8gY29uY2VpdG8gZGUgZGVjb21wb3Npw6fDo28gZGUgcG9zdG8gY29tcGxldG8gJEEgPSBCQyQuIFBhcmEgZXN0YSBtYXRyaXosIGVzY29saGEgJEIgPSBcXGJlZ2lue3BtYXRyaXh9IDEgXFxcXCAxIFxcZW5ke3BtYXRyaXh9JCBlICRDID0gXFxiZWdpbntwbWF0cml4fSAxICYgMSBcXGVuZHtwbWF0cml4fSQuIiwgImRpY2EiOiAiVXRpbGl6ZSBhIGbDs3JtdWxhICRBXnsrfSA9IENee1xcdG9wfShDQ157XFx0b3B9KV57LTF9KEJee1xcdG9wfUIpXnstMX1CXntcXHRvcH0kLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJQcmltZWlybywgY2FsY3VsYW1vcyAkQl57XFx0b3B9QiQ6ICRCXntcXHRvcH1CID0gXFxiZWdpbntwbWF0cml4fSAxICYgMSBcXGVuZHtwbWF0cml4fSBcXGJlZ2lue3BtYXRyaXh9IDEgXFxcXCAxIFxcZW5ke3BtYXRyaXh9ID0gKDIpJCwgbG9nbyAkKEJee1xcdG9wfUIpXnstMX0gPSAoMS8yKSQuIiwgIlNlZ3VuZG8sIGNhbGN1bGFtb3MgJENDXntcXHRvcH0kOiAkQ0Nee1xcdG9wfSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSAxIFxcXFwgMSBcXGVuZHtwbWF0cml4fSA9ICgyKSQsIGxvZ28gJChDQ157XFx0b3B9KV57LTF9ID0gKDEvMikkLiIsICJUZXJjZWlybywgbW9udGFtb3MgYSBleHByZXNzw6NvOiAkQV57K30gPSBDXntcXHRvcH0oQ0Nee1xcdG9wfSleey0xfShCXntcXHRvcH1CKV57LTF9Ql57XFx0b3B9ID0gXFxiZWdpbntwbWF0cml4fSAxIFxcXFwgMSBcXGVuZHtwbWF0cml4fSAoMS8yKSAoMS8yKSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxIFxcZW5ke3BtYXRyaXh9JC4iLCAiUG9yIGZpbSwgcmVhbGl6YW1vcyBhIG11bHRpcGxpY2HDp8OjbyBmaW5hbDogJEFeeyt9ID0gKDEvNCkgXFxiZWdpbntwbWF0cml4fSAxICYgMSBcXFxcIDEgJiAxIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAwLjI1ICYgMC4yNSBcXFxcIDAuMjUgJiAwLjI1IFxcZW5ke3BtYXRyaXh9JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzLCBDYXAgMSwgcC4gMzMiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRXhwbGlxdWUsIHNvYiBhIMOzdGljYSBkZSBzaXN0ZW1hcyBkZSBlcXVhw6fDtWVzIGxpbmVhcmVzLCBwb3IgcXVlIHJlY29ycmVtb3Mgw6AgaW52ZXJzYSBnZW5lcmFsaXphZGEgZGUgTW9vcmUtUGVucm9zZSBxdWFuZG8gbyBzaXN0ZW1hICRBeCA9IGckIMOpIGluY29uc2lzdGVudGUgb3UgcG9zc3VpIGluZmluaXRhcyBzb2x1w6fDtWVzLiBDb21vIGEgaW52ZXJzYSAkQV57K30kIG5vcyBhanVkYSBhIGVuY29udHJhciB1bWEgc29sdcOnw6NvIGRlIG3DrW5pbW9zIHF1YWRyYWRvcz8iLCAiZGljYSI6ICJQZW5zZSBubyBjb25jZWl0byBkZSBtaW5pbWl6YXIgYSBub3JtYSBkbyBlcnJvICR8fEF4IC0gZ3x8JCBlIG5vIHBhcGVsIGRhIGludmVyc2EgZ2VuZXJhbGl6YWRhIGNvbW8gdW0gb3BlcmFkb3IgcXVlIHByb2pldGEgbyB2ZXRvciAkZyQgbm8gZXNwYcOnbyBjb2x1bmEgZGUgJEEkLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJFbSBzaXN0ZW1hcyBpbmNvbnNpc3RlbnRlcywgbsOjbyBleGlzdGUgJHgkIHRhbCBxdWUgJEF4ID0gZyQuIEJ1c2NhbW9zIG1pbmltaXphciAkfHxBeCAtIGd8fF4yJC4iLCAiQSBzb2x1w6fDo28gZGUgbcOtbmltb3MgcXVhZHJhZG9zIMOpIGRhZGEgcG9yICR4ID0gQV57LX1nJC4iLCAiQSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgJEFeeyt9JCBwcm92w6ogdW1hIHNvbHXDp8OjbyBlc3BlY2lhbCBxdWUsIGFsw6ltIGRlIG1pbmltaXphciBvIGVycm8sIHRlbSBhIG1lbm9yIG5vcm1hICR8fHh8fCQgZW50cmUgdG9kYXMgYXMgc29sdcOnw7VlcyBwb3Nzw612ZWlzLiIsICJFbSBtb2RlbG9zIGxpbmVhcmVzLCBvIHVzbyBkZSAkQV57K30kIHBlcm1pdGUgb2J0ZXIgZXN0aW1hZG9yZXMgw7N0aW1vcyBtZXNtbyBlbSBkYWRvcyBkZXNiYWxhbmNlYWRvcyBvdSBxdWFuZG8gYSBtYXRyaXogZGUgZGVzZW5obyBwb3NzdWkgY29sdW5hcyBsaW5lYXJtZW50ZSBkZXBlbmRlbnRlcy4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hICYgRXN0ZXZlcywgSW50cm9kdcOnw6NvIGFvcyBNb2RlbG9zIExpbmVhcmVzLCBDYXAgMSwgcC4gNDEiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiRGFkYSBhIG1hdHJpeiBkaWFnb25hbCAkRCA9IFxcYmVnaW57cG1hdHJpeH0gNCAmIDAgXFxcXCAwICYgMCBcXGVuZHtwbWF0cml4fSQsIGRldGVybWluZSBhIHN1YSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2UgJEReeyt9JC4gVmVyaWZpcXVlIHNlIG8gcmVzdWx0YWRvIHNhdGlzZmF6IGEgY29uZGnDp8OjbyBkZSBzaW1ldHJpYSAkREReeyt9ID0gKEREXnsrfSlee1x0b3B9JC4iLCAiZGljYSI6ICJQYXJhIG1hdHJpemVzIGRpYWdvbmFpcywgYSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2Ugw6kgb2J0aWRhIGludmVydGVuZG8tc2UgYXBlbmFzIG9zIGVsZW1lbnRvcyBuw6NvIG51bG9zIGRhIGRpYWdvbmFsLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyJJZGVudGlmaWNhbW9zIG9zIGVsZW1lbnRvcyBkYSBkaWFnb25hbDogJGRfezExfSA9IDQkIGUgJGRfezIyfSA9IDAkLiIsICJDYWxjdWxhbW9zIGEgaW52ZXJzYSBnZW5lcmFsaXphZGEgJGRfezExfV57K30gPSAxLzQgPSAwLjI1JCBlICRkX3syMn1eeyt9ID0gMCQuIiwgIkNvbnN0cnXDrW1vcyBhIG1hdHJpeiAkRF57K30gPSBcXGJlZ2lue3BtYXRyaXh9IDAuMjUgJiAwIFxcXFwgMCAmIDAgXFxlbmR7cG1hdHJpeH0kLiIsICJDYWxjdWxhbW9zIG8gcHJvZHV0byAkREReeyt9ID0gXFxiZWdpbntwbWF0cml4fSA0ICYgMCBcXFxcIDAgJiAwIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMC4yNSAmIDAgXFxcXCAwICYgMCBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAwICYgMCBcXGVuZHtwbWF0cml4fSQuIiwgIkNvbW8gJFxcYmVnaW57cG1hdHJpeH0gMSAmIDAgXFxcXCAwICYgMCBcXGVuZHtwbWF0cml4fSQgw6kgdW1hIG1hdHJpeiBkaWFnb25hbCwgZWxhIMOpIFxcc2ltw6l0cmljYSwgcG9ydGFudG8gJChERF57K30pXntcdG9wfSA9IEREXnsrfSQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiAwLjI1fSwgeyJlbnVuY2lhZG8iOiAiU2VqYSAkWCA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgXFxcXCAxICYgMSBcXGVuZHtwbWF0cml4fSQgdW1hIG1hdHJpeiBkZSBkZXNpZ24gZGUgdW0gbW9kZWxvIGxpbmVhciAkWSA9IFhcXGJldGEgKyBcXHZhcmVwc2lsb24kLiBWZXJpZmlxdWUgc2UgJFgkIMOpIGRlIHBvc3RvIGNvbXBsZXRvLiBFbSBzZWd1aWRhLCBkZXRlcm1pbmUgdW1hIGludmVyc2EgZ2VuZXJhbGl6YWRhICRHJCBwYXJhICRYXntcXHRvcH1YJCBlIHV0aWxpemUtYSBwYXJhIGVuY29udHJhciB1bWEgc29sdcOnw6NvICRcXGhhdHtcYlxcZXRhfSQgZG8gc2lzdGVtYSBkZSBlcXVhw6fDtWVzIG5vcm1haXMgZGFkbyBxdWUgJFhee1xcdG9wfVkgPSBcXGJlZ2lue3BtYXRyaXh9IDQgXFxcXCA0IFxcZW5ke3BtYXRyaXh9JC4iLCAiZGljYSI6ICJWZXJpZmlxdWUgbyBkZXRlcm1pbmFudGUgZGUgJFhee1xcdG9wfVgkIG91IG9ic2VydmUgYSBkZXBlbmTDqm5jaWEgbGluZWFyIGVudHJlIGFzIGNvbHVuYXMgZGEgbWF0cml6ICRYJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiMS4gQ2FsY3VsYW1vcyAkWF57XFx0b3B9WCA9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgXFxcXCAxICYgMSBcXGVuZHtwbWF0cml4fSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxIFxcXFwgMSAmIDEgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDIgJiAyIFxcXFwgMiAmIDIgXFxlbmR7cG1hdHJpeH0kLiIsICIyLiBDb21vIGFzIGxpbmhhcyBkZSAkWF57XFx0b3B9WCQgc8OjbyBpZMOqbnRpY2FzLCAkXFx0ZXh0e3Bvc3RvfShYXntcXHRvcH1YKSA9IDEgPCAyJCwgbG9nbyBhIG1hdHJpeiDDqSBzaW5ndWxhci4iLCAiMy4gVW1hIGludmVyc2EgY29uZGljaW9uYWwgJEckIHNhdGlzZmF6ICRYXntcXHRvcH1YIEcgWF57XFx0b3B9WCA9IFhee1xcdG9wfVgkLiBVbWEgZXNjb2xoYSBzaW1wbGVzIHBhcmEgJEckIMOpICRcXGJlZ2lue3BtYXRyaXh9IDAuMjUgJiAwIFxcXFwgMCAmIDAgXFxlbmR7cG1hdHJpeH0kLiIsICI0LiBBIHNvbHXDp8OjbyDDqSAkXFxoYXR7XGJcXGV0YX0gPSBHIFhee1xcdG9wfVkgPSBcXGJlZ2lue3BtYXRyaXh9IDAuMjUgJiAwIFxcXFwgMCAmIDAgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSA0IFxcXFwgNCBcXGVuZHtwbWF0cml4fSA9IFxcYmVnaW57cG1hdHJpeH0gMSBcXFxcIDAgXFxlbmR7cG1hdHJpeH0kLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogbnVsbCwgInJlc3Bvc3RhX251bWVyaWNhX2VzcGVyYWRhIjogbnVsbH0sIHsiZW51bmNpYWRvIjogIkNvbnNpZGVyZSBvIHNpc3RlbWEgaW5jb25zaXN0ZW50ZSAkQXggPSBnJCBvbmRlICRBID0gXFxiZWdpbntwbWF0cml4fSAxICYgMSBcXFxcIDEgJiAtMSBcXFxcIC0yICYgMCBcXGVuZHtwbWF0cml4fSQgZSAkZyA9IFxcYmVnaW57cG1hdHJpeH0gMyBcXFxcIDEgXFxcXCAtNCBcXGVuZHtwbWF0cml4fSQuIEFwbGlxdWUgbyBjb25jZWl0byBkZSBlcXVhw6fDtWVzIG5vcm1haXMgcGFyYSBlbmNvbnRyYXIgdW1hIHNvbHXDp8OjbyBhcHJveGltYWRhIGRlIG3DrW5pbW9zIHF1YWRyYWRvcyAkXFxoYXR7eH0kLiIsICJkaWNhIjogIk8gc2lzdGVtYSBkZSBlcXVhw6fDtWVzIG5vcm1haXMgw6kgZGVmaW5pZG8gY29tbyAkQV57XFx0b3B9QVxcaGF0e3h9ID0gQV57XFx0b3B9ZyQuIiwgImdhYmFyaXRvX3Bhc3NvX2FfcGFzc28iOiBbIjEuIENhbGN1bGFtb3MgJEFee1xcdG9wfUEgPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxICYgLTIgXFxcXCAxICYgLTEgJiAwIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgXFxcXCAxICYgLTEgXFxcXCAtMiAmIDAgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDYgJiAwIFxcXFwgMCAmIDIgXFxlbmR7cG1hdHJpeH0kLiIsICIyLiBDYWxjdWxhbW9zICRBXntcXHRvcH1nID0gXFxiZWdpbntwbWF0cml4fSAxICYgMSAmIC0yIFxcXFwgMSAmIC0xICYgMCBcXGVuZHtwbWF0cml4fSBcXGJlZ2lue3BtYXRyaXh9IDMgXFxcXCAxIFxcXFwgLTQgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDMrMSs4IFxcXFwgMy0xKzAgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDEyIFxcXFwgMiBcXGVuZHtwbWF0cml4fSQuIiwgIjMuIFJlc29sdmVtb3MgbyBzaXN0ZW1hICRcXGJlZ2lue3BtYXRyaXh9IDYgJiAwIFxcXFwgMCAmIDIgXFxlbmR7cG1hdHJpeH0gXFxoYXR7eH0gPSBcXGJlZ2lue3BtYXRyaXh9IDEyIFxcXFwgMiBcXGVuZHtwbWF0cml4fSQuIiwgIjQuIFBvcnRhbnRvLCAkNlxcaGF0e3h9XzEgPSAxMiBcXFJpZ2h0YXJyb3cgXFxoYXR7eH1fMSA9IDIkIGUgJDJcXGhhdHt4fV8yID0gMiBcXFJpZ2h0YXJyb3cgXFxoYXR7eH1fMiA9IDEkLiBBIHNvbHXDp8OjbyDDqSAkXFxoYXR7eH0gPSBcXGJlZ2lue3BtYXRyaXh9IDIgXFxcXCAxIFxcZW5ke3BtYXRyaXh9JC4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hLCBKLiBHLiAmIEVzdGV2ZXMsIEUuIE0uLCBDYXAgMiwgRXhlcmPDrWNpbyAyLjIuNiIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJQcm92ZSBxdWUsIHNlICRQID0gWChYXntcXHRvcH1YKV57LX1YXntcXHRvcH0kIMOpIG8gcHJvamV0b3Igb3J0b2dvbmFsIHNvYnJlIG8gZXNwYcOnbyBjb2x1bmEgZGUgJFgkLCBlbnTDo28gbyB2ZXRvciBkZSBhcHJveGltYcOnw6NvIGRlIG3DrW5pbW9zIHF1YWRyYWRvcyAkXFxoYXR7eX0gPSBQIHkkIMOpIGludmFyaWFudGUgcGFyYSBxdWFscXVlciBzb2x1w6fDo28gJFxcaGF0e1xiXFxldGF9JCBkbyBzaXN0ZW1hIGRlIGVxdWHDp8O1ZXMgbm9ybWFpcy4iLCAiZGljYSI6ICJMZW1icmUtc2UgcXVlIHVtYSBzb2x1w6fDo28gJFxcaGF0e1xiXFxldGF9JCBkbyBzaXN0ZW1hICRYXntcXHRvcH1YXFxoYXR7XGJcXGV0YX0gPSBYXntcXHRvcH15JCBzYXRpc2ZheiAkWFxcaGF0e1xiXFxldGF9ID0gUHkkLiBVc2UgYXMgcHJvcHJpZWRhZGVzIGRhIGludmVyc2EgZ2VuZXJhbGl6YWRhLiIsICJnYWJhcml0b19wYXNzb19hX3Bhc3NvIjogWyIxLiBTZWphICRcXGhhdHtcYlxcZXRhfV8xJCBlICRcXGhhdHtcYlxcZXRhfV8yJCBkdWFzIHNvbHXDp8O1ZXMgZG8gc2lzdGVtYSAkWF57XFx0b3B9WFxcaGF0e1xiXFxldGF9ID0gWF57XFx0b3B9eSQuIiwgIjIuIFNhYmVtb3MgcXVlICRcXGhhdHt5fV8xID0gWFxcaGF0e1xiXFxldGF9XzEkIGUgJFxcaGF0e3l9XzIgPSBYXFxoYXR7XGJcXGV0YX1fMiQuIiwgIjMuIFBvciBkZWZpbmnDp8OjbywgJFhcXGhhdHtcYlxcZXRhfSA9IFgoWF57XFx0b3B9WCleey19WF57XFx0b3B9eSA9IFB5JC4iLCAiNC4gQ29tbyBhIG1hdHJpeiAkUCA9IFgoWF57XFx0b3B9WCleey19WF57XFx0b3B9JCDDqSDDum5pY2EgcGFyYSB1bWEgZGFkYSBtYXRyaXogJFgkLCBvIHByb2R1dG8gJFB5JCBuw6NvIGRlcGVuZGUgZGEgZXNjb2xoYSBkYSBpbnZlcnNhIGdlbmVyYWxpemFkYSAkKFhee1xcdG9wfVgpXnstfSQuIiwgIjUuIExvZ28sICRcXGhhdHt5fV8xID0gUHkkIGUgJFxcaGF0e3l9XzIgPSBQeSQsIGRlbW9uc3RyYW5kbyBxdWUgJFxcaGF0e3l9JCDDqSBpbnZhcmlhbnRlLiJdLCAiY29kaWdvX3Bsb3RseSI6IG51bGwsICJyZWZlcmVuY2lhX2xpdnJvIjogIkx1bmEsIEouIEcuICYgRXN0ZXZlcywgRS4gTS4sIENhcCAyLCBwLiA1NSIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJDb25zaWRlcmUgbyBzaXN0ZW1hIGRlIGVxdWHDp8O1ZXMgbGluZWFyZXMgJEF4ID0gZyQgY29tICRBID0gXFxiZWdpbntwbWF0cml4fSAxICYgMSBcXCAxICYgLTEgXFwgLTIgJiAwIFxcIFxcZW5ke3BtYXRyaXh9JCBlICRnID0gXFxiZWdpbntwbWF0cml4fSAzIFxcIDEgXFwgLTQgXFwgXFxlbmR7cG1hdHJpeH0kLiBWZXJpZmlxdWUgYSBjb25zaXN0w6puY2lhIGRvIHNpc3RlbWEgdXRpbGl6YW5kbyB1bWEgaW52ZXJzYSBnZW5lcmFsaXphZGEgJEFeey19JCBlIGRpc2N1dGEgbyBwYXBlbCBkZSAkQUFeey19ZyQgbmEgZGV0ZXJtaW5hw6fDo28gZGEgc29sdcOnw6NvLiIsICJkaWNhIjogIlVtIHNpc3RlbWEgJEF4ID0gZyQgw6kgY29uc2lzdGVudGUgc2UgZSBzb21lbnRlIHNlICRBQV57LX1nID0gZyQuIENhbGN1bGUgdW1hIGludmVyc2EgZ2VuZXJhbGl6YWRhIGUgdmVyaWZpcXVlIHNlIG8gcHJvZHV0byByZXN1bHRhIG5vIHZldG9yICRnJC4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogSWRlbnRpZmljYXIgbyBwb3N0byBkZSAkQSQuIENvbW8gYXMgY29sdW5hcyBuw6NvIHPDo28gbcO6bHRpcGxhcywgJHIoQSkgPSAyJC4iLCAiUGFzc28gMjogRW5jb250cmFyIHVtYSBpbnZlcnNhIGdlbmVyYWxpemFkYSAkQV57LX0kLiBVc2FuZG8gbyBhbGdvcml0bW8gZGUgU2VhcmxlLCBzZWxlY2lvbmFtb3MgYSBzdWJtYXRyaXogJE0gPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxIFxcIDEgJiAtMSBcXCBcXGVuZHtwbWF0cml4fSQsIGN1am8gZGV0ZXJtaW5hbnRlIMOpICQtMiQuIiwgIlBhc3NvIDM6IEEgaW52ZXJzYSDDqSAkTV57LTF9ID0gXFxmcmFjezF9ey0yfSBcXGJlZ2lue3BtYXRyaXh9IC0xICYgLTEgXFwgLTEgJiAxIFxcIFxcZW5ke3BtYXRyaXh9ID0gXFxiZWdpbntwbWF0cml4fSAwLjUgJiAwLjUgXFwgMC41ICYgLTAuNSBcXCBcXGVuZHtwbWF0cml4fSQuIiwgIlBhc3NvIDQ6IENvbnN0cnVpciAkQV57LX0gPSBcXGJlZ2lue3BtYXRyaXh9IDAuNSAmIDAuNSAmIDAgXFwgMC41ICYgLTAuNSAmIDAgXFwgXFxlbmR7cG1hdHJpeH0kIHBvciB0cmFuc3Bvc2nDp8Ojby4iLCAiUGFzc28gNTogVmVyaWZpY2FyIGEgY29uc2lzdMOqbmNpYTogJEFBXnstfWcgPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAxIFxcIDEgJiAtMSBcXCAtMiAmIDAgXFwgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSAwLjUgJiAwLjUgJiAwIFxcIDAuNSAmIC0wLjUgJiAwIFxcIFxcZW5ke3BtYXRyaXh9IFxcYmVnaW57cG1hdHJpeH0gMyBcXCAxIFxcIC00IFxcIFxcZW5ke3BtYXRyaXh9JC4iLCAiUGFzc28gNjogJEFBXnstfWcgPSBcXGJlZ2lue3BtYXRyaXh9IDEgJiAwICYgMCBcXCAwICYgMSAmIDAgXFwgLTEgJiAtMSAmIDAgXFwgXFxlbmR7cG1hdHJpeH0gXFxiZWdpbntwbWF0cml4fSAzIFxcIDEgXFwgLTQgXFwgXFxlbmR7cG1hdHJpeH0gPSBcXGJlZ2lue3BtYXRyaXh9IDMgXFwgMSBcXCAtNCBcXCBcXGVuZHtwbWF0cml4fSA9IGckLiBDb21vICRBQV57LX1nID0gZyQsIG8gc2lzdGVtYSDDqSBjb25zaXN0ZW50ZS4iXSwgImNvZGlnb19wbG90bHkiOiBudWxsLCAicmVmZXJlbmNpYV9saXZybyI6ICJMdW5hLCBKLiBHLiAmIEVzdGV2ZXMsIEUuIE0uLCBFeGVyY8OtY2lvIDIuMi42LCBwLiA1MCIsICJyZXNwb3N0YV9udW1lcmljYV9lc3BlcmFkYSI6IG51bGx9LCB7ImVudW5jaWFkbyI6ICJEYWRhIGEgbWF0cml6ICRBID0gXFxiZWdpbntwbWF0cml4fSA0ICYgMiAmIDIgXFwgMiAmIDIgJiAwIFxcIDIgJiAwICYgMiBcXCBcXGVuZHtwbWF0cml4fSQsIGRldGVybWluZSBzdWEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlICRBXnsrfSQuIEV4cGxpcXVlIGJyZXZlbWVudGUgY29tbyBhIGRlY29tcG9zacOnw6NvIGVzcGVjdHJhbCBhdXhpbGlhIG5lc3RlIGPDoWxjdWxvIHBhcmEgbWF0cml6ZXMgXFxzaW3DqXRyaWNhcy4iLCAiZGljYSI6ICJQYXJhIG1hdHJpemVzIFxcc2ltw6l0cmljYXMsICRBXnsrfSA9IFAgXFxMYW1iZGFeeyt9IFBee1xcdG9wfSQsIG9uZGUgJFxcTGFtYmRhXnsrfSQgY29udMOpbSBvcyByZWPDrXByb2NvcyBkb3MgYXV0b3ZhbG9yZXMgbsOjbyBudWxvcy4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogRW5jb250cmFyIG9zIGF1dG92YWxvcmVzIGRlICRBJC4gUmVzb2x2ZW5kbyAkXFxkZXQoQSAtIFxcbGFtYmRhIEkpID0gMCQsIGVuY29udHJhbW9zICRcXGxhbWJkYV8xID0gNiQgZSAkXFxsYW1iZGFfMiA9IDIkLiIsICJQYXNzbyAyOiBPYnRlciBvcyBhdXRvdmV0b3JlcyBub3JtYWxpemFkb3MgJHVfMSQgZSAkdV8yJCBjb3JyZXNwb25kZW50ZXMuIiwgIlBhc3NvIDM6IENvbnN0cnVpciBhIG1hdHJpeiBkZSBhdXRvdmV0b3JlcyAkUCQgZSBhIG1hdHJpeiBkaWFnb25hbCAkXFxMYW1iZGEkLiIsICJQYXNzbyA0OiBDYWxjdWxhciAkQV57K30gPSBQIFxcTGFtYmRhXnstMX0gUF57XFx0b3B9ID0gXFxmcmFjezF9ezZ9IFxcYmVnaW57cG1hdHJpeH0gMSAmIDEgJiAxIFxcIDIgJiAyICYgLTEgXFwgLTEgJiAtMSAmIDIgXFwgXFxlbmR7cG1hdHJpeH0gXFxkb3RzID0gXFxmcmFjezF9ezE4fSBcXGJlZ2lue3BtYXRyaXh9IDIgJiAxICYgMSBcXCAxICYgNSAmIC00IFxcIDEgJiAtNCAmIDUgXFwgXFxlbmR7cG1hdHJpeH0kLiIsICJQYXNzbyA1OiBBIGRlY29tcG9zacOnw6NvIGVzcGVjdHJhbCBwZXJtaXRlIHJlcHJlc2VudGFyIGEgbWF0cml6IGNvbW8gJEEgPSBcXHN1bSBcXGxhbWJkYV9pIHVfaSB1X2lee1xcdG9wfSQsIGUgYSBpbnZlcnNhIGRlIE1vb3JlLVBlbnJvc2Ugw6kgc2ltcGxlc21lbnRlICRBXnsrfSA9IFxcc3VtIFxcZnJhY3sxfXtcXGxhbWJkYV9pfSB1X2kgdV9pXntcXHRvcH0kIHBhcmEgJFxcbGFtYmRhX2kgXFxuZXEgMCQuIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiAiTHVuYSwgSi4gRy4gJiBFc3RldmVzLCBFLiBNLiwgcC4gMzctMzgiLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfSwgeyJlbnVuY2lhZG8iOiAiQ29uc2lkZXJlIHVtYSBtYXRyaXogJEEkIGRlIHBvc3RvIGNvbXBsZXRvIGNvbHVuYS4gUHJvdmUgcXVlIGEgaW52ZXJzYSBkZSBNb29yZS1QZW5yb3NlIHNhdGlzZmF6IGEgY29uZGnDp8OjbyBkZSByZWZsZXhpdmlkYWRlICRBXnsrfUFBXnsrfSA9IEFeeyt9JCBlIHF1ZSwgbmVzdGUgY2FzbywgJEFeeyt9QSA9IEkkLiIsICJkaWNhIjogIlVzZSBhIGZvcm1hICRBXnsrfSA9IChBXntcXHRvcH1BKV57LTF9QV57XFx0b3B9JCB2w6FsaWRhIHBhcmEgbWF0cml6ZXMgY29tIHBvc3RvIGNvbHVuYSBjb21wbGV0by4iLCAiZ2FiYXJpdG9fcGFzc29fYV9wYXNzbyI6IFsiUGFzc28gMTogRGVmaW5pw6fDo28gcGFyYSBwb3N0byBjb2x1bmEgY29tcGxldG86ICRBXnsrfSA9IChBXntcXHRvcH1BKV57LTF9QV57XFx0b3B9JC4iLCAiUGFzc28gMjogQ2FsY3VsYXIgJEFeeyt9QSA9IChBXntcXHRvcH1BKV57LTF9QV57XFx0b3B9QSA9IEkkLiIsICJQYXNzbyAzOiBQYXJhIGEgcmVmbGV4aXZpZGFkZSwgY2FsY3VsYW1vcyAkQV57K31BQV57K30gPSAoQV57K31BKUFeeyt9ID0gSSBcXGNkb3QgQV57K30gPSBBXnsrfSQuIiwgIlBhc3NvIDQ6IENvbmNsdcOtbW9zIHF1ZSBhIHByb3ByaWVkYWRlIGRlIHJlZmxleGl2aWRhZGUgw6kgc2F0aXNmZWl0YSBwZWxvIHByb2R1dG8gZGEgaW52ZXJzYSBjb20gYSBwcsOzcHJpYSBtYXRyaXouIl0sICJjb2RpZ29fcGxvdGx5IjogbnVsbCwgInJlZmVyZW5jaWFfbGl2cm8iOiBudWxsLCAicmVzcG9zdGFfbnVtZXJpY2FfZXNwZXJhZGEiOiBudWxsfV19').decode('utf-8'))


    # Inicialização do estado de progresso
    if "respostas_certas" not in st.session_state:
        st.session_state.respostas_certas = {}
    
    # Cálculo dinâmico do total de exercícios
    mcqs = dados_exercicios.get("questoes_multipla_escolha", [])
    discursivas = dados_exercicios.get("questoes_discursivas", [])
    total_exercicios = len(mcqs) + len(discursivas)
    acertos = sum(1 for k, v in st.session_state.respostas_certas.items() if v is True)
    
    # Exibição da barra de progresso
    if total_exercicios > 0:
        st.progress(acertos / total_exercicios)
        st.markdown(f"🏆 **Seu Progresso no Caderno:** {acertos} de {total_exercicios} desafios concluídos!")
    else:
        st.info("Nenhum exercício disponível para este tópico.")
    
    st.divider()
    
    # Renderização das questões de Múltipla Escolha
    if mcqs:
        st.subheader("📝 Questões de Múltipla Escolha")
        for i, questao in enumerate(mcqs):
            with st.container(border=True):
                st.markdown(f"**Questão {i+1}:** {questao.get('enunciado', '')}")
                
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
    
                # Execução de gráfico Plotly se existir
                codigo_plot = questao.get("codigo_plotly")
                if codigo_plot:
                    local_vars = {}
                    try:
                        exec(codigo_plot, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True)
                    except Exception as e:
                        st.error(f"Erro ao renderizar gráfico: {e}")
    
                # Alternativas
                opcoes = questao.get("alternativas", {})
                selecao = st.radio(
                    "Escolha uma alternativa:",
                    options=list(opcoes.keys()),
                    format_func=lambda x: f"{x}) {opcoes[x]}",
                    key=f"radio_mcq_{i}"
                )
    
                # Botão de Dica
                if st.button("💡 Dica", key=f"btn_dica_mcq_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
    
                # Verificação
                if st.button("✅ Verificar Resposta", key=f"btn_mcq_{i}"):
                    if selecao == questao.get("alternativa_correta"):
                        st.success("Correto! Muito bem.")
                        st.session_state.respostas_certas[f"mcq_{i}"] = True
                        st.rerun()
                    else:
                        st.error("Resposta incorreta. Tente novamente!")
                        st.session_state.respostas_certas[f"mcq_{i}"] = False
                
                with st.expander("✅ Ver Gabarito Comentado"):
                    st.write(questao.get("gabarito_comentado", "Gabarito indisponível"))
    
    st.divider()
    
    # Renderização das questões Discursivas
    if discursivas:
        st.subheader("✍️ Questões Discursivas")
        for i, questao in enumerate(discursivas):
            with st.container(border=True):
                st.markdown(f"**Desafio {i+1}:** {questao.get('enunciado', '')}")
                
                ref = questao.get("referencia_livro")
                if ref:
                    st.markdown(f"📖 *Referência: {ref}*")
                
                codigo_plot = questao.get("codigo_plotly")
                if codigo_plot:
                    local_vars = {}
                    try:
                        exec(codigo_plot, globals(), local_vars)
                        if "fig" in local_vars:
                            st.plotly_chart(local_vars["fig"], use_container_width=True)
                    except Exception as e:
                        st.error(f"Erro ao renderizar gráfico: {e}")
    
                st.text_area("Sua resposta (Prosa):", key=f"text_disc_{i}")
                
                # Verificação de resposta numérica ou checkbox de conclusão
                esperada = questao.get("resposta_numerica_esperada")
                if esperada is not None:
                    user_val = st.number_input("Digite o resultado numérico calculado para validação:", key=f"num_disc_{i}", value=0.0)
                    if st.button("Validar Cálculo", key=f"btn_val_disc_{i}"):
                        if abs(user_val - esperada) <= max(0.01, 0.01 * abs(esperada)):
                            st.success("Resposta Numérica Correta! Excelente trabalho de cálculo.")
                            st.session_state.respostas_certas[f"disc_{i}"] = True
                            st.rerun()
                        else:
                            st.error("O valor calculado difere do gabarito. Verifique seus cálculos.")
                            st.session_state.respostas_certas[f"disc_{i}"] = False
                else:
                    concluido = st.checkbox("Marque aqui após estudar e responder esta questão", key=f"check_disc_{i}")
                    if concluido:
                        st.session_state.respostas_certas[f"disc_{i}"] = True
                    else:
                        st.session_state.respostas_certas[f"disc_{i}"] = False
    
                if st.button("💡 Dica", key=f"btn_dica_disc_{i}"):
                    st.info(questao.get("dica", "Dica indisponível"))
                
                with st.expander("✅ Ver Resolução Detalhada"):
                    for passo in questao.get("gabarito_passo_a_passo", []):
                        st.write(f"- {passo}")
