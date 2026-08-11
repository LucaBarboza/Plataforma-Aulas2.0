import sys
import os
import re

# Aumenta o limite de recursão para suportar schemas Pydantic e árvores JSON profundas
sys.setrecursionlimit(5000)

# Removido SafeStreamWrapper pois o Streamlit recarrega o stdout a cada rerun, causando RecursionError

import streamlit as st

# 1. Configuração global da página - Executada antes de qualquer elemento UI
st.set_page_config(
    page_title="Plataforma de Aulas Premium 2.0",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS premium global e na sidebar para identidade visual de luxo
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        html, body, [class*="css"], .stApp {
            font-family: 'Outfit', 'Segoe UI', sans-serif;
        }
        
        /* Estilização da Sidebar */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
            border-right: 1px solid #334155;
        }
        [data-testid="stSidebar"] * {
            color: #E2E8F0 !important;
        }
        [data-testid="stSidebar"] svg {
            fill: #38BDF8 !important;
        }
        
        /* Cartão de Boas-vindas */
        .welcome-card {
            background-color: #F8FAFC;
            border-left: 5px solid #2563EB;
            padding: 1.5rem;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
        }
        
        /* Botões do Streamlit */
        div.stButton > button {
            background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
            color: white !important;
            font-weight: 600 !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 0.5rem 1.5rem !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2), 0 2px 4px -2px rgba(37, 99, 235, 0.2) !important;
        }
        div.stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3), 0 4px 6px -4px rgba(37, 99, 235, 0.3) !important;
            background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%) !important;
        }
        
        /* Inputs do Streamlit */
        div.stTextInput input, div.stSelectbox [data-baseweb="select"] {
            border-radius: 8px !important;
            border: 1px solid #CBD5E1 !important;
            background-color: #FFFFFF !important;
            transition: border-color 0.2s ease !important;
        }
        div.stTextInput input:focus, div.stSelectbox [data-baseweb="select"]:focus-within {
            border-color: #2563EB !important;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
        }
    </style>
""", unsafe_allow_html=True)

pasta_aulas = "aulas"
paginas_aulas = []

# Varredura dinâmica das aulas na pasta /aulas
if os.path.exists(pasta_aulas):
    arquivos = sorted(os.listdir(pasta_aulas))
    for arquivo in arquivos:
        if arquivo.startswith("aula") and arquivo.endswith(".py"):
            caminho_completo = os.path.join(pasta_aulas, arquivo)
            
            # Limpa o nome do arquivo "aula1_teste_t.py" -> "Aula 01: Teste T"
            match = re.match(r'^aula(\d+)_?(.*)', arquivo, flags=re.IGNORECASE)
            if match:
                num_aula = int(match.group(1))
                nome_resto = match.group(2).replace(".py", "").replace("_", " ").strip().title()
                titulo_bonito = f"Aula {num_aula:02d}: {nome_resto}"
            else:
                titulo_bonito = arquivo.replace(".py", "").replace("_", " ").title()
            
            try:
                paginas_aulas.append(st.Page(caminho_completo, title=titulo_bonito, icon="📐"))
            except Exception as e_page:
                print(f"[ERRO] Erro ao registrar aula {arquivo}: {e_page}")

# Importação da página do gerador de aulas e relatórios
import gerador_page
import relatorios_page

# Página fixa de administração/geração
pagina_gerador = st.Page(gerador_page.run_page, title="Criar Nova Aula", icon="🪄", url_path="criar_aula", default=True)
pagina_relatorios = st.Page(relatorios_page.run_page, title="Relatórios de Auditoria", icon="📊", url_path="relatorios")

# Configuração da navegação dinâmica (Geração de Aulas no topo)
secoes = {}
secoes["🪄 Geração de Aulas"] = [pagina_gerador]
if paginas_aulas:
    secoes["📚 Trilha de Aprendizagem"] = paginas_aulas
secoes["📊 Relatórios & Auditoria"] = [pagina_relatorios]

try:
    pg = st.navigation(secoes)
    pg.run()
except Exception as ex_nav:
    st.error(f"⚠️ Erro ao carregar a página selecionada: {ex_nav}")
    st.info("Caso uma aula recém-gerada contenha dependências ausentes, selecione outra página no menu lateral para continuar.")
