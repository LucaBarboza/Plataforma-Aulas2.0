import sys
import streamlit as st
import os
import shutil
import time
import json
import re

# Função auxiliar para garantir carregamento de chave
from gerador_conteudo import carregar_chave_api

DISCIPLINAS_PRECARREGADAS = {
    "MATD38 - Estatística Básica B": {
        "codigo": "MATD38",
        "pdf_path": os.path.join("Ementas", "matd38_-_estatistica_basica_b.pdf"),
        "temas": [
            "Unidade 1 - Tópico 1.1: Amostras aleatórias simples e amostras sistemáticas",
            "Unidade 1 - Tópico 1.2: Distribuição amostral da média e da proporção",
            "Unidade 2 - Tópico 2.1: Estimação pontual e intervalar",
            "Unidade 2 - Tópico 2.2.1: Intervalo de confiança para a média de populações Normais (Variância conhecida)",
            "Unidade 2 - Tópico 2.2.2: Intervalo de confiança para a média de populações Normais (Variância desconhecida: uso da distribuição t de Student)",
            "Unidade 2 - Tópico 2.3: Intervalo de confiança para média e proporção usando grandes amostras",
            "Unidade 2 - Tópico 2.4.1: Testes de hipóteses: As hipóteses estatísticas",
            "Unidade 2 - Tópico 2.4.2: Testes de hipóteses: Erros tipo I e tipo II",
            "Unidade 2 - Tópico 2.4.3: Testes de hipóteses: Região crítica e p-valor",
            "Unidade 2 - Tópico 2.5.1: Testes de hipóteses para a média de populações Normais (Variância conhecida)",
            "Unidade 2 - Tópico 2.5.2: Testes de hipóteses para a média de populações Normais (Variância desconhecida: teste t)",
            "Unidade 2 - Tópico 2.6: Testes de hipóteses para a média e para a proporção usando grandes amostras",
            "Unidade 2 - Tópico 2.7: Testes de hipóteses para a comparação das médias de duas populações Normais com variâncias desconhecidas",
            "Unidade 2 - Tópico 2.8: Teste para igualdade de variâncias",
            "Unidade 3 - Tópico 3.1: Teste de aderência para normalidade",
            "Unidade 3 - Tópico 3.2: Teste de associação",
            "Unidade 4 - Tópico 4.1: O modelo de regressão linear simples",
            "Unidade 4 - Tópico 4.2: O método de mínimos quadrados",
            "Unidade 4 - Tópico 4.3: Estimação dos coeficientes de regressão",
            "Unidade 4 - Tópico 4.4: Predição"
        ]
    },
    "MATD41 - Introdução aos Modelos Lineares": {
        "codigo": "MATD41",
        "pdf_path": os.path.join("Ementas", "matd41_introducao_aos_modelos_lineares.pdf"),
        "temas": [
            "Unidade 1 - Tópico 1.1: Formas especiais de vetores e matrizes, aplicações em Estatísticas: enfoque computacional",
            "Unidade 1 - Tópico 1.2: Matriz ortogonal, formas de HELMERT, matriz idempotente",
            "Unidade 1 - Tópico 1.3: Matrizes de covariâncias e correlação, autovalores e autovetores",
            "Unidade 1 - Tópico 1.4: Inversa generalizada de uma matriz",
            "Unidade 1 - Tópico 1.5: Formas quadráticas positivas definidas e semi positivas definidas",
            "Unidade 2 - Tópico 2.1: Consistência e soluções de sistemas de equações lineares",
            "Unidade 2 - Tópico 2.2: Soluções aproximadas e de mínimos quadrados",
            "Unidade 3 - Tópico 3.1: O problema fundamental das relações entre variáveis: Relações funcionais e estatísticas",
            "Unidade 3 - Tópico 3.2: Estimação por mínimos quadrados e o sistema de equações normais",
            "Unidade 3 - Tópico 3.3: Modelos de posto completo e incompleto. O modelo de regressão linear",
            "Unidade 4 - Tópico 4.1: Restrições e equações normais reduzidas",
            "Unidade 4 - Tópico 4.2: O uso de matriz inversa generalizada",
            "Unidade 4 - Tópico 4.3: Testes de hipóteses e o conceito de funções estimáveis em posto incompleto",
            "Unidade 5 - Tópico 5.1: O procedimento geral da análise de variância (ANOVA)",
            "Unidade 5 - Tópico 5.2: Análise de variância no modelo de regressão linear",
            "Unidade 5 - Tópico 5.3: Somas de quadrados e o coeficiente de determinação (R²)",
            "Unidade 6 - Tópico 6.1: Dados experimentais e observacionais",
            "Unidade 6 - Tópico 6.2: Delineamentos experimentais: Experimentos com um fator e com restrições na casualização (blocos casualizados e quadrados latinos)",
            "Unidade 6 - Tópico 6.3: Experimentos em blocos incompletos balanceados",
            "Unidade 7 - Tópico 7.1: Diagnóstico e bondade do ajuste: Análise de resíduos",
            "Unidade 7 - Tópico 7.2: Checagem de erros nas pressuposições dos modelos lineares",
            "Unidade 7 - Tópico 7.3: Identificação de observações não usuais (outliers, pontos de alavanca e de influência)"
        ]
    }
}


def substituir_simbolo(md_content, conceito, novo_simbolo):
    # Regex projetada para casar com: | **Conceito** | old_symbol |
    # e substituir old_symbol por novo_simbolo.
    padrao = rf"(\|\s*\*\*{re.escape(conceito)}\*\*\s*\|)[^|]+(\|)"
    novo_simbolo_escapado = novo_simbolo.replace("\\", "\\\\")
    md_content = re.sub(padrao, rf"\1 {novo_simbolo_escapado} \2", md_content)
    return md_content

def construir_relatorio_prosa_txt(exec_log, teoria_gigante_path, exercicios_path):
    """
    Constrói um relatório descritivo completo em formato TXT contendo todo o passo a passo,
    conteúdos intermediários, prosa expandida e exercícios da geração.
    """
    relatorio = []
    relatorio.append("======================================================================")
    relatorio.append("       RELATÓRIO DE AUDITORIA E HISTÓRICO COMPLETO DA AULA")
    relatorio.append("======================================================================")
    relatorio.append(f"Tema Global: {exec_log.get('tema', 'N/A')}")
    relatorio.append(f"Professor: {exec_log.get('professor', 'N/A')}")
    relatorio.append(f"Disciplina: {exec_log.get('disciplina', 'N/A')}")
    relatorio.append(f"Início da Geração: {exec_log.get('timestamp_inicio', 'N/A')}")
    relatorio.append(f"Fim da Geração: {exec_log.get('timestamp_fim', 'N/A')}")
    relatorio.append(f"Tempo Total: {exec_log.get('tempo_total_segundos', 0.0)} segundos")
    relatorio.append(f"Status Final: {exec_log.get('status', 'N/A').upper()}")
    relatorio.append("======================================================================\n")
    
    # 1. Roteiro e Cronograma
    relatorio.append("----------------------------------------------------------------------")
    relatorio.append("1. CRONOGRAMA E MÉTRICAS DAS ETAPAS DE DESENVOLVIMENTO")
    relatorio.append("----------------------------------------------------------------------")
    etapas = exec_log.get("etapas", {})
    for chave in sorted(etapas.keys()):
        et = etapas[chave]
        relatorio.append(f"- {et.get('descricao', 'Etapa')}:")
        relatorio.append(f"  * Status: {et.get('status', 'N/A')}")
        relatorio.append(f"  * Duração: {et.get('duracao_segundos', 0.0)} segundos")
    relatorio.append("\n")
    
    # 2. Conteúdo de Prosa por Subtópico
    if os.path.exists(teoria_gigante_path):
        try:
            with open(teoria_gigante_path, "r", encoding="utf-8") as f:
                teoria = json.load(f)
                
            relatorio.append("----------------------------------------------------------------------")
            relatorio.append("2. HISTÓRICO DE PRODUÇÃO DOS CONTEÚDOS E PROSA EXPANDIDA")
            relatorio.append("----------------------------------------------------------------------")
            
            subtopicos_log = etapas.get("3_escrita_revisao", {}).get("subtopicos", [])
            subtopicos_dict = {sub.get("titulo", ""): sub for sub in subtopicos_log}
            
            for idx, pagina in enumerate(teoria.get("paginas_conteudo", [])):
                titulo = pagina.get("titulo_subtopico", "Subtópico")
                relatorio.append(f"\n[Subtópico {idx+1}]: {titulo}")
                relatorio.append("-" * 40)
                
                # Exibe métricas de auditoria do revisor para este subtópico se existirem
                sub_info = subtopicos_dict.get(titulo)
                if sub_info:
                    relatorio.append(f"  * Auditoria do Revisor Científico:")
                    relatorio.append(f"    - Tentativas do Escritor: {sub_info.get('tentativas', 1)}")
                    relatorio.append(f"    - Reprovações do Revisor: {sub_info.get('reprovacoes', 0)}")
                    erros_api = sub_info.get("erros_api", {})
                    if erros_api:
                        total_sub_api = sum(erros_api.values())
                        relatorio.append(f"    - Retentativas de API de Rede: {total_sub_api} (429: {erros_api.get('429', 0)}, 503/Timeout: {erros_api.get('503', 0)}, Outros: {erros_api.get('outros', 0)})")
                    feedbacks = sub_info.get("feedbacks", [])
                    if feedbacks:
                        relatorio.append("    - Histórico de Feedbacks de Correção:")
                        for f_idx, fb in enumerate(feedbacks):
                            relatorio.append(f"      [Tentativa #{f_idx+1}] {fb}")
                
                relatorio.append("\n>>> A) PROSA BASE GERADA:")
                relatorio.append(pagina.get("discussao_teorica_prosa", "N/A"))
                relatorio.append("\n>>> B) FORMALISMO MATEMÁTICO (LaTeX):")
                relatorio.append(pagina.get("formalismo_latex", "N/A"))
                relatorio.append("\n>>> C) PROSA EXPANDIDA FINAL DE LIVRO DIDÁTICO:")
                relatorio.append(pagina.get("prosa_longa_expandida", "N/A"))
                relatorio.append("\n" + "=" * 40)
        except Exception as e:
            relatorio.append(f"[ERRO] Falha ao ler teoria para o relatório: {e}")
    else:
        relatorio.append("[AVISO] Arquivo de teoria não encontrado para detalhamento do conteúdo.")
        
    relatorio.append("\n")
    
    # 3. Exercícios Resolvidos
    if os.path.exists(exercicios_path):
        try:
            with open(exercicios_path, "r", encoding="utf-8") as f:
                exs = json.load(f)
                
            relatorio.append("----------------------------------------------------------------------")
            relatorio.append("3. CADERNO DE EXERCÍCIOS GERADO")
            relatorio.append("----------------------------------------------------------------------")
            
            relatorio.append("\n>>> A) QUESTÕES DE MÚLTIPLA ESCOLHA:")
            for q_idx, q in enumerate(exs.get("questoes_multipla_escolha", [])):
                relatorio.append(f"\nQuestão {q_idx+1}: {q.get('enunciado', 'N/A')}")
                for alt, texto in q.get("alternativas", {}).items():
                    relatorio.append(f"  {alt}) {texto}")
                relatorio.append(f"  * Dica: {q.get('dica', 'N/A')}")
                relatorio.append(f"  * Gabarito Correto: {q.get('alternativa_correta', 'N/A')}")
                relatorio.append(f"  * Justificativa: {q.get('gabarito_comentado', 'N/A')}")
                
            relatorio.append("\n>>> B) QUESTÕES DISCURSIVAS ABERTAS:")
            for q_idx, q in enumerate(exs.get("questoes_discursivas", [])):
                relatorio.append(f"\nQuestão {q_idx+1}: {q.get('enunciado', 'N/A')}")
                relatorio.append(f"  * Dica: {q.get('dica', 'N/A')}")
                relatorio.append("  * Resolução Passo a Passo:")
                for p_idx, passo in enumerate(q.get("gabarito_passo_a_passo", [])):
                    relatorio.append(f"    {p_idx+1}. {passo}")
        except Exception as e:
            relatorio.append(f"[ERRO] Falha ao ler exercícios para o relatório: {e}")
    else:
        relatorio.append("[AVISO] Arquivo de exercícios não encontrado para detalhamento.")
        
    relatorio.append("\n======================================================================")
    relatorio.append("                         FIM DO RELATÓRIO")
    relatorio.append("======================================================================")
    
    return "\n".join(relatorio)

def rodar_thread_completa(status_dict):
    """
    Executa o fluxo completo de geração de uma aula em background thread sem interagir diretamente com st.*
    Recebe os parâmetros necessários via status_dict['params'].
    """
    import traceback
    sys.setrecursionlimit(10000)
    params = status_dict.get("params", {})
    nome_professor = params.get("nome_professor", "")
    codigo_disciplina = params.get("codigo_disciplina", "")
    tema_solicitado = params.get("tema_solicitado", "")
    cor_principal = params.get("cor_principal", "#1E3A8A")
    cor_secundaria = params.get("cor_secundaria", "#10B981")
    cor_alerta = params.get("cor_alerta", "#F59E0B")
    cor_critica = params.get("cor_critica", "#991B1B")
    t_inicio_geral_completo = params.get("tempo_inicio", time.time())

    def set_status(etapa, detalhe):
        status_dict["etapa_atual"] = etapa
        status_dict["subetapa_detalhe"] = detalhe

    def status_callback(dados):
        if not status_dict.get("ativo", False):
            return
        status = status_dict
        etapa = dados.get("etapa")
        if etapa == "roteiro_concluido":
            status["subtopicos"] = dados.get("subtopicos", [])
            for sub in status["subtopicos"]:
                status["status_subtopicos"][sub] = "waiting"
                status["tentativas_subtopicos"][sub] = 1
            status["subetapa_detalhe"] = f"Roteiro estruturado! {len(status['subtopicos'])} subtópicos mapeados."
        elif etapa == "subtopico_iniciado":
            titulo = dados.get("titulo")
            status["status_subtopicos"][titulo] = "writing"
            status["etapa_atual"] = f"Fase 2: Escrita e Revisão ({dados.get('index', 0) + 1}/{dados.get('total', 1)})"
            status["subetapa_detalhe"] = f"Iniciando a redação do subtópico: {titulo}"
        elif etapa == "subtopico_tentativa":
            titulo = dados.get("titulo")
            status["status_subtopicos"][titulo] = "writing"
            status["tentativas_subtopicos"][titulo] = dados.get("tentativa", 1)
            if "max_tentativas_subtopicos" not in status:
                status["max_tentativas_subtopicos"] = {}
            status["max_tentativas_subtopicos"][titulo] = dados.get("max_tentativas", 5)
            status["subetapa_detalhe"] = f"Redigindo subtópico '{titulo}' (Tentativa {dados.get('tentativa', 1)}/{dados.get('max_tentativas', 5)})"
        elif etapa == "subtopico_aprovado":
            titulo = dados.get("titulo")
            status["status_subtopicos"][titulo] = "approved"
            status["subetapa_detalhe"] = f"✓ Subtópico '{titulo}' aprovado pelo revisor científico!"
            if "preview_subtopicos" not in status:
                status["preview_subtopicos"] = {}
            if dados.get("dados"):
                status["preview_subtopicos"][titulo] = dados.get("dados")
        elif etapa == "subtopico_reprovado":
            titulo = dados.get("titulo")
            status["status_subtopicos"][titulo] = "failed"
            status["subetapa_detalhe"] = f"⚠️ Subtópico '{titulo}' reprovado pelo revisor. Corrigindo..."
        elif etapa == "erro_api":
            titulo = dados.get("titulo")
            tipo = dados.get("tipo_erro", "outro")
            
            if "total_erros_api" not in status:
                status["total_erros_api"] = 0
            status["total_erros_api"] += 1
            
            if tipo == "429":
                status["subetapa_detalhe"] = f"⏳ Cota da API (429). Aguardando retentativa..."
            elif tipo == "503":
                status["subetapa_detalhe"] = f"⏳ Servidor do Gemini ocupado (503). Retentando em instantes..."
            else:
                status["subetapa_detalhe"] = f"⏳ Conexão temporária falhou. Retentando em instantes..."

    nome_professor_clean = nome_professor.lower().strip()
    codigo_disciplina_clean = codigo_disciplina.lower().strip()

    exec_log = {
        "status": "iniciado",
        "timestamp_inicio": time.strftime("%Y-%m-%d %H:%M:%S"),
        "tema": tema_solicitado,
        "professor": nome_professor,
        "disciplina": codigo_disciplina,
        "tempo_total_segundos": 0.0,
        "etapas": {}
    }

    try:
        # Preparação dos arquivos e diretrizes em background
        set_status("Iniciando...", "Preparando arquivos de ementa, materiais e diretrizes...")
        os.makedirs("cache", exist_ok=True)
        temp_ementa_path = os.path.join("cache", f"ementa_{nome_professor_clean}_{codigo_disciplina_clean}.pdf")
        is_custom = params.get("is_custom", False)
        ementa_bytes = params.get("ementa_bytes")
        disciplina_selecionada = params.get("disciplina_selecionada", "")

        if is_custom and ementa_bytes:
            with open(temp_ementa_path, "wb") as f:
                f.write(ementa_bytes)
        elif not is_custom and disciplina_selecionada in DISCIPLINAS_PRECARREGADAS:
            orig_pdf_path = DISCIPLINAS_PRECARREGADAS[disciplina_selecionada]["pdf_path"]
            if os.path.exists(orig_pdf_path):
                shutil.copy(orig_pdf_path, temp_ementa_path)

        temp_materials_dir = None
        materiais_buffers = params.get("materiais_buffers", [])
        if materiais_buffers:
            temp_materials_dir = f"temp_rag_{nome_professor_clean}_{codigo_disciplina_clean}"
            os.makedirs(temp_materials_dir, exist_ok=True)
            for arq_nome, arq_bytes in materiais_buffers:
                file_path = os.path.join(temp_materials_dir, arq_nome)
                with open(file_path, "wb") as f:
                    f.write(arq_bytes)

        diretrizes_texto = ""
        if os.path.exists("diretrizes_padrao.md"):
            with open("diretrizes_padrao.md", "r", encoding="utf-8") as f:
                diretrizes_texto = f.read()

        diretrizes_custom_buffers = params.get("diretrizes_custom_buffers", [])
        if diretrizes_custom_buffers:
            texto_custom_acumulado = []
            for arq_nome, arq_bytes in diretrizes_custom_buffers:
                ext = os.path.splitext(arq_nome)[1].lower()
                if ext in [".md", ".txt"]:
                    try:
                        conteudo_txt = arq_bytes.decode("utf-8", errors="ignore")
                        texto_custom_acumulado.append(f"### Arquivo Customizado ({arq_nome}):\n{conteudo_txt}")
                    except Exception as e_read: pass
                elif ext in [".pdf", ".png", ".jpg", ".jpeg", ".webp"]:
                    try:
                        c_temp = os.path.join("cache", f"temp_diretriz_{int(time.time())}_{arq_nome}")
                        with open(c_temp, "wb") as f_out:
                            f_out.write(arq_bytes)
                        from analisador_diretrizes import processar_arquivo_diretrizes_ia
                        res_ia = processar_arquivo_diretrizes_ia([(c_temp, arq_nome)])
                        if isinstance(res_ia, dict) and res_ia.get("diretrizes_estilo_livre"):
                            texto_custom_acumulado.append(f"### Diretrizes Extraídas da Mídia ({arq_nome}):\n{res_ia['diretrizes_estilo_livre']}")
                        try: os.remove(c_temp)
                        except: pass
                    except Exception as e_ia: pass

            if texto_custom_acumulado:
                diretrizes_texto += "\n\n## 📝 3. Diretrizes e Notações Customizadas do Professor\n" + "\n\n".join(texto_custom_acumulado)

        if cor_principal != "#1E3A8A":
            diretrizes_texto = diretrizes_texto.replace('"PRIMARY_BLUE": "#1E3A8A"', f'"PRIMARY_BLUE": "{cor_principal}"')
        if cor_secundaria != "#10B981":
            diretrizes_texto = diretrizes_texto.replace('"SECONDARY_GREEN": "#10B981"', f'"SECONDARY_GREEN": "{cor_secundaria}"')
        if cor_alerta != "#F59E0B":
            diretrizes_texto = diretrizes_texto.replace('"WARNING_AMBER": "#F59E0B"', f'"WARNING_AMBER": "{cor_alerta}"')
        if cor_critica != "#991B1B":
            diretrizes_texto = diretrizes_texto.replace('"CRITICAL_RED": "#991B1B"', f'"CRITICAL_RED": "{cor_critica}"')

        contexto_bloco = []
        foco_turma_sel = params.get("foco_turma_sel", "")
        foco_turma_custom = params.get("foco_turma_custom", "")
        diretrizes_adicionais = params.get("diretrizes_adicionais", "")
        if foco_turma_sel:
            area_final = foco_turma_custom.strip() if (foco_turma_sel == "✍️ Outra Área / Foco Personalizado" and foco_turma_custom.strip()) else foco_turma_sel
            contexto_bloco.append(f"- **Área / Foco da Turma**: {area_final}")
        contexto_bloco.append("- **Nível do Público-Alvo**: Estudantes de Graduação Universitária")
        if diretrizes_adicionais and diretrizes_adicionais.strip():
            contexto_bloco.append(f"- **Observações & Orientações Adicionais do Docente**: {diretrizes_adicionais.strip()}")

        if contexto_bloco:
            diretrizes_texto += "\n\n## 🎯 4. Perfil da Turma e Orientações Específicas da Aula\n" + "\n".join(contexto_bloco) + "\n"

        # 1. Processamento e Indexação do RAG Pessoal
        t_start_rag = time.time()
        if temp_materials_dir and os.path.exists(temp_materials_dir):
            set_status("Indexando base RAG...", "Indexando materiais de apoio fornecidos pelo professor...")
            from indexador_livros import inicializar_e_indexar
            inicializar_e_indexar(nome_professor_clean, codigo_disciplina_clean, temp_materials_dir)
            shutil.rmtree(temp_materials_dir, ignore_errors=True)
            set_status("Indexando base RAG...", "✓ RAG pessoal atualizado com sucesso no Google Cloud!")
        else:
            set_status("Carregando base...", "Utilizando base de livros globais da plataforma...")
        t_end_rag = time.time()
        
        exec_log["etapas"]["1_indexacao_rag"] = {
            "descricao": "Indexação dos Materiais de Apoio (RAG Pessoal)",
            "status": "sucesso" if temp_materials_dir else "pulado",
            "duracao_segundos": round(t_end_rag - t_start_rag, 2)
        }

        retomar = params.get("retomar_checkpoint", False)
        payload_teoria = None
        resultado_editorial = None
        resultado_prosa_gigante = None
        resultado_exercicios = None

        if retomar:
            set_status("Retomando...", "Buscando checkpoints salvas no cache...")
            if os.path.exists(os.path.join("cache", "payload_teoria.json")):
                try:
                    with open(os.path.join("cache", "payload_teoria.json"), "r", encoding="utf-8") as f_c:
                        payload_teoria = json.load(f_c)
                    set_status("Fase 2: Escrita e Revisão", "✓ Teoria bruta recuperada do cache!")
                except: pass

            if os.path.exists(os.path.join("cache", "payload_teoria_lapidada.json")):
                try:
                    with open(os.path.join("cache", "payload_teoria_lapidada.json"), "r", encoding="utf-8") as f_c:
                        resultado_editorial = json.load(f_c)
                    set_status("Fase 3: Lapidação Editorial", "✓ Editorial recuperado do cache!")
                except: pass

            if os.path.exists(os.path.join("cache", "payload_teoria_gigante.json")):
                try:
                    with open(os.path.join("cache", "payload_teoria_gigante.json"), "r", encoding="utf-8") as f_c:
                        resultado_prosa_gigante = json.load(f_c)
                    set_status("Fase 4: Expansão de Prosa", "✓ Prosa expandida recuperada do cache!")
                except: pass

            if os.path.exists(os.path.join("cache", "payload_exercicios.json")):
                try:
                    with open(os.path.join("cache", "payload_exercicios.json"), "r", encoding="utf-8") as f_c:
                        resultado_exercicios = json.load(f_c)
                    set_status("Fase 5: Caderno de Exercícios", "✓ Exercícios recuperados do cache!")
                except: pass

        # 2. Geração de Conteúdo da Aula
        if not payload_teoria:
            set_status("Fase 1: Roteirista", f"Analisando a ementa e estruturando a trilha pedagógica para: {tema_solicitado}...")
            from gerador_conteudo import gerar_conteudo_aula
            
            payload_teoria = gerar_conteudo_aula(
                nome_professor=nome_professor,
                codigo_disciplina=codigo_disciplina,
                tema_solicitado=tema_solicitado,
                ementa_pdf_path=temp_ementa_path,
                diretrizes_texto=diretrizes_texto,
                status_callback=status_callback
            )
            
            t_end_escrita = time.time()
            set_status("Fase 2: Escrita e Revisão", "✓ Todos os subtópicos foram redigidos e aprovados pelo revisor científico!")
            exec_log["etapas"]["3_escrita_revisao"] = {
                "descricao": "Agente 2 + 2.5: Escritor & Revisor (Loop de Revisão Ativa)",
                "status": "sucesso",
                "duracao_segundos": payload_teoria.get("log_gerador", {}).get("tempo_escrita_revisao_segundos", 0.0),
                "subtopicos": payload_teoria.get("log_gerador", {}).get("subtopicos", [])
            }

            with open(os.path.join("cache", "payload_teoria.json"), "w", encoding="utf-8") as f:
                json.dump(payload_teoria, f, indent=4, ensure_ascii=False)

        # 3. Lapidação Editorial (Orquestrador Editorial)
        if not resultado_editorial:
            set_status("Fase 3: Lapidação Editorial", "Unificando a prosa, eliminando repetições e formatando equações em KaTeX...")
            from orquestrador_editorial import lapidar_conteudo_global
            
            t_start_editorial = time.time()
            resultado_editorial = lapidar_conteudo_global(
                os.path.join("cache", "payload_teoria.json"),
                diretrizes_texto=diretrizes_texto
            )
            t_end_editorial = time.time()
            
            set_status("Fase 3: Lapidação Editorial", "✓ Capítulo unificado e formatado em padrão de livro universitário!")
            exec_log["etapas"]["4_lapidacao_editorial"] = {
                "descricao": "Agente 3.5: Editor-Chefe (Unificação e Coerência Global)",
                "status": "sucesso",
                "duracao_segundos": round(t_end_editorial - t_start_editorial, 2)
            }

            with open(os.path.join("cache", "payload_teoria_lapidada.json"), "w", encoding="utf-8") as f:
                json.dump(resultado_editorial, f, indent=4, ensure_ascii=False)

        # 4. Construtor de Prosa Longa
        if not resultado_prosa_gigante:
            set_status("Fase 4: Expansão de Prosa", "Expandindo explicações qualitativas e adicionando detalhes pedagógicos...")
            from orquestrador_editorial import construir_prosa_longa_capitulo
            
            t_start_prosa = time.time()
            resultado_prosa_gigante = construir_prosa_longa_capitulo(
                os.path.join("cache", "payload_teoria_lapidada.json"),
                diretrizes_texto=diretrizes_texto
            )
            t_end_prosa = time.time()
            
            set_status("Fase 4: Expansão de Prosa", "✓ Prosa acadêmica longa e profunda concluída!")
            exec_log["etapas"]["5_expansao_prosa"] = {
                "descricao": "Agente 3.75: Construtor de Prosa (Expansão Exaustiva de Livro)",
                "status": "sucesso",
                "duracao_segundos": round(t_end_prosa - t_start_prosa, 2)
            }

            with open(os.path.join("cache", "payload_teoria_gigante.json"), "w", encoding="utf-8") as f:
                json.dump(resultado_prosa_gigante, f, indent=4, ensure_ascii=False)

        # 5. Caderno de Exercícios
        if not resultado_exercicios:
            set_status("Fase 5: Caderno de Exercícios", "Gerando 5 exercícios de topo (fechados e abertos) com gabarito explicativo...")
            from gerador_exercicios import gerar_caderno_exercicios
            
            t_start_exercicios = time.time()
            resultado_exercicios = gerar_caderno_exercicios(
                caminho_payload_teoria=os.path.join("cache", "payload_teoria.json"),
                nome_professor=nome_professor,
                codigo_disciplina=codigo_disciplina,
                diretrizes_texto=diretrizes_texto
            )
            t_end_exercicios = time.time()
            
            with open(os.path.join("cache", "payload_exercicios.json"), "w", encoding="utf-8") as f:
                json.dump(resultado_exercicios, f, indent=4, ensure_ascii=False)
            
            set_status("Fase 5: Caderno de Exercícios", "✓ 5 Questões fechadas e 3 discursivas detalhadas com gabarito passo a passo geradas!")
            exec_log["etapas"]["6_caderno_exercicios"] = {
                "descricao": "Agente 3: Caderno de Exercícios (Questões Fechadas e Abertas)",
                "status": "sucesso",
                "duracao_segundos": round(t_end_exercicios - t_start_exercicios, 2)
            }

        # 6. Compilação da Interface
        set_status("Fase 6: Compilação de Interface", "Compilando e costurando o código Streamlit responsivo final...")
        from gerador_interface import compilar_aula_completa_por_fatias
        
        t_start_interface = time.time()
        caminho_script_gerado = compilar_aula_completa_por_fatias(
            os.path.join("cache", "payload_teoria_gigante.json"),
            os.path.join("cache", "payload_exercicios.json"),
            motor_grafico="plotly",
            cor_principal=cor_principal,
            cor_critica=cor_critica,
            cor_secundaria=cor_secundaria,
            cor_alerta=cor_alerta
        )
        t_end_interface = time.time()
        
        set_status("Fase 6: Compilação de Interface", "✓ Arquivo Python executável gerado fisicamente na pasta `/aulas`!")
        exec_log["etapas"]["7_compilacao_interface"] = {
            "descricao": "Fase 6: Compilação de Interface Streamlit",
            "status": "sucesso",
            "duracao_segundos": round(t_end_interface - t_start_interface, 2)
        }

        # Limpeza
        pass

        exec_log["status"] = "sucesso"
        exec_log["tempo_total_segundos"] = round(time.time() - t_inicio_geral_completo, 2)
        exec_log["timestamp_fim"] = time.strftime("%Y-%m-%d %H:%M:%S")
        
        from orquestrador_editorial import gerar_resumo_compacto_aula
        status_dict["resumo_aula"] = gerar_resumo_compacto_aula(resultado_editorial)

        with open(os.path.join("cache", "ultimo_log_execucao.json"), "w", encoding="utf-8") as f:
            json.dump(exec_log, f, indent=4, ensure_ascii=False)

        if caminho_script_gerado:
            nome_script = os.path.basename(caminho_script_gerado)
            os.makedirs("logdasaulasgeradas", exist_ok=True)
            caminho_log_especifico = os.path.join("logdasaulasgeradas", nome_script.replace(".py", ".log.json"))
            caminho_log_txt = os.path.join("logdasaulasgeradas", nome_script.replace(".py", ".log.txt"))
            
            try:
                with open(caminho_log_especifico, "w", encoding="utf-8") as f:
                    json.dump(exec_log, f, indent=4, ensure_ascii=False)
            except: pass
            
            try:
                teoria_gigante_path = os.path.join("cache", "payload_teoria_gigante.json")
                exercicios_path = os.path.join("cache", "payload_exercicios.json")
                relatorio_txt = construir_relatorio_prosa_txt(exec_log, teoria_gigante_path, exercicios_path)
                with open(caminho_log_txt, "w", encoding="utf-8") as f:
                    f.write(relatorio_txt)
            except: pass

            sucesso_py = False
            try:
                from git_integration import commitar_arquivo_github
                set_status("Fase 7: Salvamento no GitHub", "Enviando arquivos de aula e relatórios ao repositório do GitHub...")
                nome_arquivo_py = os.path.basename(caminho_script_gerado)
                caminho_repositorio_py = f"aulas/{nome_arquivo_py}"
                sucesso_py = commitar_arquivo_github(
                    caminho_local=caminho_script_gerado,
                    caminho_repositorio=caminho_repositorio_py,
                    mensagem_commit=f"feat: adiciona aula {caminho_repositorio_py}"
                )
            except: pass

        status_dict["mensagem_sucesso"] = "✨ A geração foi concluída localmente! Os arquivos foram gravados na pasta `/aulas`."
        status_dict["sucesso"] = True
        status_dict["ativo"] = False

    except Exception as ex:
        tb_str = traceback.format_exc()
        print(f"[ERRO CRÍTICO THREAD] {ex}\n{tb_str}")
        if temp_materials_dir and os.path.exists(temp_materials_dir):
            try: shutil.rmtree(temp_materials_dir, ignore_errors=True)
            except: pass
        
        exec_log["status"] = "erro"
        exec_log["erro_mensagem"] = f"{ex}\n{tb_str}"
        exec_log["tempo_total_segundos"] = round(time.time() - t_inicio_geral_completo, 2)
        exec_log["timestamp_fim"] = time.strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            with open(os.path.join("cache", "ultimo_log_execucao.json"), "w", encoding="utf-8") as f:
                json.dump(exec_log, f, indent=4, ensure_ascii=False)
        except: pass
        
        status_dict["erro"] = str(ex)
        status_dict["ativo"] = False

def disparar_thread_geracao(status_dict, params):
    """
    Associa os parâmetros de execução ao status_dict e dispara a thread de geração em background.
    """
    clean_params = {k: v for k, v in params.items() if k != "params"}
    status_dict["params"] = clean_params
    import threading
    import importlib
    
    add_script_run_ctx = None
    streamlit_paths = [
        ("streamlit.runtime.scriptrunner_utils.script_run_context", "add_script_run_ctx"),
        ("streamlit.runtime.scriptrunner", "add_script_run_ctx"),
        ("streamlit.runtime.scriptrunner.script_run_context", "add_script_run_ctx"),
        ("streamlit.scriptrunner", "add_script_run_ctx"),
        ("streamlit.report_thread", "add_report_ctx")
    ]

    for module_name, func_name in streamlit_paths:
        try:
            module = importlib.import_module(module_name)
            add_script_run_ctx = getattr(module, func_name)
            break
        except (ImportError, AttributeError):
            continue

    thread = threading.Thread(target=rodar_thread_completa, args=(status_dict,))
    if add_script_run_ctx:
        add_script_run_ctx(thread)
    thread.start()

def run_page():
    # Garante a carga da chave de API
    carregar_chave_api()

    # Inicializa estado para notações customizadas e diretrizes IA
    if "custom_notations" not in st.session_state:
        st.session_state.custom_notations = []
    if "diretrizes_ia_valores" not in st.session_state:
        st.session_state.diretrizes_ia_valores = {}

    def obter_valor_diretriz(chave: str, valor_padrao: str) -> str:
        if "diretrizes_ia_valores" in st.session_state and st.session_state.diretrizes_ia_valores:
            ia_val = st.session_state.diretrizes_ia_valores.get(chave)
            if ia_val is not None and str(ia_val).strip():
                return str(ia_val).strip()
        return valor_padrao

    # Injeção de Estilos CSS e Animações para a Tela de Carregamento Premium e Painel
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
            
            .gerador-title {
                font-size: 2.6rem;
                font-weight: 800;
                background: linear-gradient(135deg, #1E3A8A 0%, #3B82F6 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0.2rem;
                text-align: center;
            }
            .gerador-subtitle {
                font-size: 1.15rem;
                color: #64748B;
                margin-bottom: 2rem;
                text-align: center;
                font-style: italic;
            }
            
            /* Efeitos premium para os uploads de arquivos */
            div[data-testid="stFileUploader"] {
                background-color: #F8FAFC !important;
                border: 2px dashed #CBD5E1 !important;
                border-radius: 12px !important;
                padding: 1rem !important;
                transition: all 0.3s ease !important;
            }
            div[data-testid="stFileUploader"]:hover {
                border-color: #3B82F6 !important;
                background-color: #F1F5F9 !important;
            }
            
            /* Estilo dos Expanders */
            div[data-testid="stExpander"] {
                border-radius: 12px !important;
                border: 1px solid #E2E8F0 !important;
                background-color: #FFFFFF !important;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.02) !important;
            }
            
            /* ANIMAÇÃO DE SPINNING PREMIUM PARA O CARREGADOR */
            @keyframes spin-gradient {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
            @keyframes pulse-opacity {
                0%, 100% { opacity: 0.6; }
                50% { opacity: 1; }
            }
            
            .loader-container {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                padding: 3rem;
                background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
                border-radius: 20px;
                color: #F8FAFC;
                box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3), 0 10px 10px -5px rgba(0, 0, 0, 0.3);
                border: 1px solid #334155;
                margin-bottom: 2rem;
            }
            
            .loader-ring {
                position: relative;
                width: 120px;
                height: 120px;
                display: flex;
                align-items: center;
                justify-content: center;
                margin-bottom: 2rem;
            }
            .loader-ring::before {
                content: "";
                position: absolute;
                width: 100%;
                height: 100%;
                border-radius: 50%;
                border: 8px solid transparent;
                border-top-color: #38BDF8;
                border-bottom-color: #6366F1;
                animation: spin-gradient 1.5s linear infinite;
            }
            .loader-ring::after {
                content: "🎓";
                font-size: 3rem;
                animation: pulse-opacity 2s ease-in-out infinite;
            }
            
            .loader-timer {
                font-size: 1.8rem;
                font-weight: 800;
                color: #38BDF8;
                font-family: monospace;
                margin-bottom: 1rem;
                text-shadow: 0 0 10px rgba(56, 189, 248, 0.3);
            }
            
            .loader-status {
                font-size: 1.25rem;
                font-weight: 600;
                margin-bottom: 0.5rem;
                color: #F1F5F9;
                text-align: center;
            }
            .loader-substatus {
                font-size: 0.95rem;
                color: #94A3B8;
                margin-bottom: 1.5rem;
                text-align: center;
                font-style: italic;
            }
            
            /* Lista de Subtópicos Gerados na Tela */
            .subtopicos-list {
                width: 100%;
                max-width: 600px;
                background: rgba(15, 23, 42, 0.6);
                border-radius: 12px;
                padding: 1.25rem;
                border: 1px solid #334155;
                margin-top: 1rem;
            }
            .subtopico-item {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0.6rem 0.8rem;
                margin-bottom: 0.5rem;
                border-radius: 8px;
                background-color: rgba(30, 41, 59, 0.8);
                border-left: 4px solid #475569;
                font-size: 0.9rem;
            }
            .subtopico-item.active {
                border-left-color: #38BDF8;
                background-color: rgba(56, 189, 248, 0.1);
                font-weight: 600;
            }
            .subtopico-item.done {
                border-left-color: #10B981;
                background-color: rgba(16, 185, 129, 0.1);
            }
            .subtopico-item.reprovado {
                border-left-color: #EF4444;
                background-color: rgba(239, 68, 68, 0.1);
            }
        </style>
    """, unsafe_allow_html=True)

    # Funções de suporte para a Tela de Carregamento Premium
    def renderizar_tela_carregamento(placeholder, status_info, tempo_decorrido):
        minutos = int(tempo_decorrido // 60)
        segundos = int(tempo_decorrido % 60)
        tempo_str = f"{minutos:02d}:{segundos:02d}"
        
        etapa_atual = status_info.get("etapa_atual", "")
        fase_pos_escrita = any(f in etapa_atual for f in ["Fase 3", "Fase 4", "Fase 5", "Fase 6", "Fase 7"])

        subtopicos_html = ""
        if status_info.get("subtopicos"):
            subtopicos_html += '<div class="subtopicos-list">'
            for idx, titulo in enumerate(status_info["subtopicos"]):
                status = status_info["status_subtopicos"].get(titulo, "waiting")
                tentativas = status_info["tentativas_subtopicos"].get(titulo, 1)
                max_tentativas = status_info.get("max_tentativas_subtopicos", {}).get(titulo, 3)
                
                classe_status = "waiting"
                badge = "📥 Fila"
                if status == "writing" and not fase_pos_escrita:
                    classe_status = "active"
                    badge = f"⏳ Gerando (Tentativa {tentativas}/{max_tentativas})"
                elif status == "approved" or fase_pos_escrita:
                    classe_status = "done"
                    badge = "✅ Concluído"
                elif status == "failed" and not fase_pos_escrita:
                    classe_status = "reprovado"
                    badge = "⚠️ Corrigindo"
                    
                subtopicos_html += f"""
                    <div class="subtopico-item {classe_status}">
                        <span>📖 Subtópico {idx+1}: {titulo}</span>
                        <span style="font-weight: 600;">{badge}</span>
                    </div>
                """
            subtopicos_html += '</div>'
            
        batch_badge_html = ""
        if st.session_state.get("is_batch_run"):
            b_idx = st.session_state.get("batch_index", 1)
            b_tot = st.session_state.get("batch_total", 1)
            batch_badge_html = f"""
                <div style="background: rgba(56, 189, 248, 0.15); color: #38BDF8; padding: 0.5rem 1.2rem; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.3); font-weight: 700; margin-bottom: 1rem; text-align: center; font-size: 1.1rem;">
                    ⚡ Modo Lote (Batch) Ativo: Tópico {b_idx} de {b_tot}
                </div>
            """

        tempo_inicio_ms = int(st.session_state.get("tempo_inicio", time.time()) * 1000)

        loader_html = f"""
            <div class="loader-container">
                {batch_badge_html}
                <div class="loader-ring"></div>
                <div class="loader-timer" id="live-timer-el" data-start-ms="{tempo_inicio_ms}">{tempo_str}</div>
                <div class="loader-status">{status_info.get("etapa_atual", "Processando")}</div>
                <div class="loader-substatus">{status_info.get("subetapa_detalhe", "")}</div>
                {subtopicos_html}
            </div>
            <script>
                (function() {{
                    function tick() {{
                        const el = document.getElementById("live-timer-el");
                        if (!el) return;
                        const startMs = parseInt(el.getAttribute("data-start-ms") || "0", 10);
                        if (!startMs) return;
                        const diffSec = Math.max(0, Math.floor((Date.now() - startMs) / 1000));
                        const m = Math.floor(diffSec / 60);
                        const s = diffSec % 60;
                        const str = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
                        el.textContent = str;
                    }}
                    tick();
                    if (!window.__liveTimerInt) {{
                        window.__liveTimerInt = setInterval(tick, 500);
                    }}
                }})();
            </script>
        """
        placeholder.html(loader_html)

    # Título premium estilizado
    st.markdown("""
        <div>
            <h1 class="gerador-title">🪄 Painel de Criação de Aulas Acadêmicas</h1>
            <p class="gerador-subtitle">
                Gere trilhas de aprendizagem completas de nível universitário premium com RAG pessoal e inteligência artificial
            </p>
        </div>
    """, unsafe_allow_html=True)
    # Inicializa variáveis de controle no session state se não existirem
    if "gerando_aula" not in st.session_state:
        st.session_state.gerando_aula = False
    if "sucesso_geracao" not in st.session_state:
        st.session_state.sucesso_geracao = False
    if "erro_geracao" not in st.session_state:
        st.session_state.erro_geracao = None
    if "mensagem_sucesso" not in st.session_state:
        st.session_state.mensagem_sucesso = ""
    if "geracao_status" not in st.session_state:
        st.session_state.geracao_status = {}

    if st.session_state.gerando_aula:
        # Define placeholders persistentes de ordem idêntica para evitar duplicações no rerun do Streamlit
        loader_placeholder = st.empty()
        scroll_placeholder = st.empty()

        # Rola a página automaticamente para o topo na primeira renderização do carregamento
        if not st.session_state.get("scroll_to_top_done", False):
            import streamlit.components.v1 as components
            with scroll_placeholder:
                components.html(
                    """
                    <script>
                        setTimeout(() => {
                            try {
                                window.parent.scrollTo({top: 0, behavior: 'smooth'});
                                
                                const selectors = [
                                    '.main',
                                    '.stMain',
                                    '.stApp',
                                    '[data-testid="stAppViewContainer"]',
                                    '[data-testid="stAppViewBlockContainer"]',
                                    '#root'
                                ];
                                
                                selectors.forEach(selector => {
                                    try {
                                        const el = window.parent.document.querySelector(selector);
                                        if (el) {
                                            el.scrollTo({top: 0, behavior: 'smooth'});
                                            el.scrollTop = 0;
                                        }
                                    } catch(err) {}
                                });
                            } catch (e) {
                                console.error("Scroll error:", e);
                            }
                        }, 100);
                    </script>
                    """,
                    height=0,
                    width=0
                )
            st.session_state.scroll_to_top_done = True
        else:
            scroll_placeholder.empty()

        # Monitora a thread a partir do dicionário de status compartilhado
        status_dict = st.session_state.geracao_status
        
        if status_dict.get("sucesso"):
            if st.session_state.get("is_batch_run") and st.session_state.get("batch_queue"):
                resumo_aula = status_dict.get("resumo_aula", "")
                st.session_state.batch_memoria = st.session_state.get("batch_memoria", "") + "\n\n" + resumo_aula
                
                proximo_tema = st.session_state.batch_queue.pop(0)
                st.session_state.batch_index = st.session_state.get("batch_index", 1) + 1
                
                t_novo_inicio = time.time()
                st.session_state.tempo_inicio = t_novo_inicio
                
                novos_params = {k: v for k, v in status_dict.get("params", {}).items() if k != "params"}
                novos_params["tema_solicitado"] = proximo_tema
                novos_params["tempo_inicio"] = t_novo_inicio
                
                novo_status = {
                    "etapa_atual": f"Iniciando Tópico {st.session_state.batch_index}...",
                    "subetapa_detalhe": f"Iniciando geração para: {proximo_tema}",
                    "subtopicos": [],
                    "status_subtopicos": {},
                    "tentativas_subtopicos": {},
                    "max_tentativas_subtopicos": {},
                    "tempo_inicio": t_novo_inicio,
                    "ativo": True,
                    "sucesso": False,
                    "erro": None,
                    "mensagem_sucesso": "",
                    "memoria_pedagogica": st.session_state.batch_memoria,
                    "params": novos_params
                }
                st.session_state.geracao_status = novo_status
                disparar_thread_geracao(novo_status, novos_params)
                st.rerun()
            else:
                st.session_state.sucesso_geracao = True
                if st.session_state.get("is_batch_run"):
                    st.session_state.mensagem_sucesso = f"✨ Todas as {st.session_state.get('batch_total', 1)} aulas da ementa foram geradas e compiladas em Lote com Sucesso no GitHub!"
                    # Remove o checkpoint pois o lote foi 100% concluído
                    codigo_clean = str(status_dict.get("params", {}).get("codigo_disciplina_clean", "")).lower().strip()
                    if codigo_clean:
                        cp_file = os.path.join("cache", f"batch_checkpoint_{codigo_clean}.json")
                        if os.path.exists(cp_file):
                            try: os.remove(cp_file)
                            except: pass
                else:
                    st.session_state.mensagem_sucesso = status_dict.get("mensagem_sucesso", "")
                st.session_state.tempo_decorrido_final = time.time() - st.session_state.tempo_inicio
                st.session_state.gerando_aula = False
                st.rerun()
        elif status_dict.get("erro"):
            st.session_state.erro_geracao = status_dict.get("erro")
            st.session_state.tempo_decorrido_final = time.time() - st.session_state.tempo_inicio
            st.session_state.gerando_aula = False
            st.rerun()
        elif not status_dict.get("ativo", False):
            st.session_state.erro_geracao = "A thread de geração foi encerrada inesperadamente."
            st.session_state.tempo_decorrido_final = time.time() - st.session_state.tempo_inicio
            st.session_state.gerando_aula = False
            st.rerun()

        # Se a geração estiver ativa, renderiza a tela de carregamento e força o rerun
        tempo_decorrido = time.time() - st.session_state.tempo_inicio
        renderizar_tela_carregamento(loader_placeholder, status_dict, tempo_decorrido)
        
        # Componente de Live Preview do Conteúdo em Tempo Real
        with st.expander("👁️ Visualizar Prévia em Tempo Real (Live Stream dos Agentes)", expanded=True):
            tab_teoria, tab_exercicios, tab_log = st.tabs(["📖 Teoria & Notações (Live Draft)", "✏️ Exercícios & Gabarito", "⚙️ Log dos Agentes"])
            
            with tab_teoria:
                preview_subs = status_dict.get("preview_subtopicos", {})
                payload_teoria_path = os.path.join("cache", "payload_teoria.json")
                payload_gigante_path = os.path.join("cache", "payload_teoria_gigante.json")
                
                path_usar = payload_gigante_path if os.path.exists(payload_gigante_path) else payload_teoria_path
                dados_arquivo = None
                if os.path.exists(path_usar):
                    try:
                        with open(path_usar, "r", encoding="utf-8") as f_p:
                            dados_arquivo = json.load(f_p)
                    except: pass
                
                if dados_arquivo and (dados_arquivo.get("conteudo_paginas") or dados_arquivo.get("paginas_conteudo")):
                    paginas = dados_arquivo.get("conteudo_paginas", []) or dados_arquivo.get("paginas_conteudo", [])
                    st.success(f"📚 **Capítulo de Aula em Construção**: {len(paginas)} subtópico(s) consolidados")
                    
                    for sub_i, pag in enumerate(paginas):
                        sub_tit = pag.get("titulo_subtopico", f"Subtópico {sub_i+1}")
                        conteudo_obj = pag.get("conteudo", {})
                        
                        st.markdown(f"#### 📖 {sub_i+1}. {sub_tit}")
                        
                        intuitivo = conteudo_obj.get("conceito_intuitivo") or pag.get("discussao_teorica_prosa") or pag.get("prosa_longa_expandida")
                        if intuitivo:
                            st.markdown("**💡 Explicação Didática:**")
                            st.write(str(intuitivo)[:600] + ("..." if len(str(intuitivo)) > 600 else ""))
                        
                        formal = conteudo_obj.get("conceito_formal") or pag.get("formalismo_latex")
                        if formal:
                            st.markdown("**📐 Equação / Enunciado Matemático:**")
                            st.latex(str(formal).replace("$", "").strip())
                            
                        exemplo_obj = conteudo_obj.get("exemplo_canonico")
                        if exemplo_obj and isinstance(exemplo_obj, dict):
                            st.markdown(f"**🎯 Exemplo Prático:** {exemplo_obj.get('enunciado', '')[:250]}...")
                            
                        st.markdown("---")
                elif preview_subs:
                    st.info(f"✨ **{len(preview_subs)} subtópico(s) aprovado(s) pelo revisor em tempo real:**")
                    for sub_tit, sub_d in preview_subs.items():
                        c_dict = sub_d.get("conteudo", {})
                        st.markdown(f"#### 📖 {sub_tit}")
                        if c_dict.get("conceito_intuitivo"):
                            st.write(str(c_dict["conceito_intuitivo"])[:400] + "...")
                        if c_dict.get("conceito_formal"):
                            st.latex(str(c_dict["conceito_formal"]).replace("$", "").strip())
                        st.markdown("---")
                else:
                    st.info("⏳ O Roteirista e o Escritor estão alinhando a didática e notações. A prévia ao vivo surgirá aqui assim que o primeiro bloco for aprovado...")

            with tab_exercicios:
                payload_ex_path = os.path.join("cache", "payload_exercicios.json")
                if os.path.exists(payload_ex_path):
                    try:
                        with open(payload_ex_path, "r", encoding="utf-8") as f_ex:
                            dados_ex = json.load(f_ex)
                        
                        fechadas = dados_ex.get("questoes_multipla_escolha", [])
                        abertas = dados_ex.get("questoes_discursivas", [])
                        
                        st.success(f"✓ Caderno gerado com {len(fechadas)} Questões Objetivas e {len(abertas)} Discursivas!")
                        if fechadas:
                            st.markdown(f"**Prévia Q1 (Múltipla Escolha):** {fechadas[0].get('enunciado', '')[:300]}...")
                    except: pass
                else:
                    st.info("⏳ O Agente de Exercícios iniciará a elaboração das questões no Passo 5...")

            with tab_log:
                st.markdown("##### 📜 Atualizações dos Agentes:")
                if status_dict.get("subetapa_detalhe"):
                    st.info(f"[{status_dict.get('etapa_atual', '')}] {status_dict['subetapa_detalhe']}")
                log_path = os.path.join("cache", "ultimo_log_execucao.json")
                if os.path.exists(log_path):
                    try:
                        with open(log_path, "r", encoding="utf-8") as f_l:
                            st.json(json.load(f_l).get("etapas", {}))
                    except: pass

        # Atualização contínua segundo a segundo
        time.sleep(1.0)
        st.rerun()

    # Quando a thread terminar:
    if st.session_state.sucesso_geracao:
        st.balloons()
        tempo_total_seg = st.session_state.get("tempo_decorrido_final", 0)
        m = int(tempo_total_seg // 60)
        s = int(tempo_total_seg % 60)
        tempo_fmt = f"{m:02d}:{s:02d}"

        st.markdown(f"""
            <div style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); border-radius: 16px; padding: 2rem; border: 1px solid #10B981; color: white; text-align: center; margin-bottom: 1.5rem; box-shadow: 0 10px 25px rgba(0,0,0,0.2);">
                <div style="font-size: 3.5rem; margin-bottom: 0.5rem;">🎓✨</div>
                <h2 style="color: #38BDF8; font-weight: 800; margin-bottom: 0.5rem;">Aula Acadêmica Gerada com Sucesso!</h2>
                <p style="font-size: 1.1rem; color: #94A3B8; margin-bottom: 1rem;">O cronômetro foi finalizado e a aula foi compilada na pasta <code style="color: #34D399;">/aulas</code>.</p>
                <div style="background: rgba(56, 189, 248, 0.1); display: inline-block; padding: 0.6rem 1.8rem; border-radius: 30px; font-weight: 700; color: #38BDF8; font-size: 1.2rem; border: 1px solid rgba(56, 189, 248, 0.3);">
                    ⏱️ Tempo Total Concluído: {tempo_fmt}
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.success(st.session_state.mensagem_sucesso)

        col_b1, col_b2 = st.columns([1, 1])
        with col_b1:
            if st.button("🪄 Criar Outra Aula", key="btn_criar_outra_aula", use_container_width=True):
                st.session_state.sucesso_geracao = False
                st.rerun()
        with col_b2:
            if st.button("📚 Atualizar Trilha & Concluir", key="btn_atualizar_trilha_concluir", type="primary", use_container_width=True):
                st.session_state.sucesso_geracao = False
                st.rerun()
        return
    elif st.session_state.erro_geracao:
        tempo_decorrido = time.time() - st.session_state.tempo_inicio
        minutos = int(tempo_decorrido // 60)
        segundos = int(tempo_decorrido % 60)
        st.error(f"❌ Geração interrompida após {minutos:02d}:{segundos:02d} devido a uma oscilação ou falha pontual!")
        st.error(f"Detalhes do erro: {st.session_state.erro_geracao}")
        
        st.info("💡 **Dica de Recuperação**: Você pode clicar em **Tentar Novamente (Retomar de onde parou)** abaixo. O sistema reaproveitará os subtópicos e fases já salvas em cache, continuando exatamente a partir da etapa que falhou!")

        col_ret1, col_ret2 = st.columns([1.2, 1])
        with col_ret1:
            if st.button("🔄 Tentar Novamente (Retomar de Onde Parou)", key="btn_retomar_checkpoint_main", type="primary", use_container_width=True):
                old_params = dict(st.session_state.get("geracao_status", {}).get("params", {}))
                old_params["retomar_checkpoint"] = True
                t_novo = time.time()
                old_params["tempo_inicio"] = t_novo
                st.session_state.tempo_inicio = t_novo
                st.session_state.erro_geracao = None
                st.session_state.sucesso_geracao = False
                
                novo_status = {
                    "etapa_atual": "Retomando...",
                    "subetapa_detalhe": "Buscando checkpoints salvas no cache e retomando agentes...",
                    "subtopicos": [],
                    "status_subtopicos": {},
                    "tentativas_subtopicos": {},
                    "max_tentativas_subtopicos": {},
                    "tempo_inicio": t_novo,
                    "ativo": True,
                    "sucesso": False,
                    "erro": None,
                    "mensagem_sucesso": "",
                    "params": old_params
                }
                st.session_state.geracao_status = novo_status
                st.session_state.gerando_aula = True
                disparar_thread_geracao(novo_status, old_params)
                st.rerun()
                
        with col_ret2:
            if st.button("↩️ Voltar ao Painel", key="btn_voltar_painel_erro", use_container_width=True):
                st.session_state.erro_geracao = None
                st.rerun()
        return
    # Bloco informativo didático premium
    st.markdown("""
        <div style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%); border-radius: 16px; padding: 1.8rem; border: 1px solid #334155; color: #F8FAFC; margin-bottom: 2rem; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.2);">
            <h3 style="color: #38BDF8; font-weight: 800; margin-top: 0; margin-bottom: 0.8rem; font-size: 1.4rem;">
                🎓 Como os Agentes de IA trabalham para criar a sua aula:
            </h3>
            <p style="color: #94A3B8; font-size: 0.95rem; margin-bottom: 1.2rem; line-height: 1.5;">
                Esta plataforma não gera resumos simples. Ela utiliza uma equipe de <strong>agentes especializados</strong> operando em cadeia para produzir um capítulo completo de livro didático universitário premium com simuladores reativos e caderno de exercícios:
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem;">
                <div style="background: rgba(30, 41, 59, 0.7); padding: 1rem; border-radius: 10px; border-left: 4px solid #38BDF8;">
                    <div style="font-weight: 700; color: #38BDF8; margin-bottom: 0.3rem;">🎯 1. Agente Roteirista</div>
                    <div style="font-size: 0.85rem; color: #CBD5E1;">Lê a sua ementa e trava o escopo. Impede a IA de inventar assuntos fora da disciplina ou invadir outras matérias.</div>
                </div>
                <div style="background: rgba(30, 41, 59, 0.7); padding: 1rem; border-radius: 10px; border-left: 4px solid #6366F1;">
                    <div style="font-weight: 700; color: #818CF8; margin-bottom: 0.3rem;">📚 2. Escritor & Revisor</div>
                    <div style="font-size: 0.85rem; color: #CBD5E1;">Busca os seus materiais (RAG) e faz uma auditoria rigorosa de notação e fórmulas em LaTeX com tolerância zero para erros.</div>
                </div>
                <div style="background: rgba(30, 41, 59, 0.7); padding: 1rem; border-radius: 10px; border-left: 4px solid #10B981;">
                    <div style="font-weight: 700; color: #34D399; margin-bottom: 0.3rem;">✍️ 3. Editor & Prosa</div>
                    <div style="font-size: 0.85rem; color: #CBD5E1;">Unifica a leitura sem repetições e expande as explicações em uma prosa acadêmica denso e fluida de livro.</div>
                </div>
                <div style="background: rgba(30, 41, 59, 0.7); padding: 1rem; border-radius: 10px; border-left: 4px solid #F59E0B;">
                    <div style="font-weight: 700; color: #FBBF24; margin-bottom: 0.3rem;">📊 4. Exercícios & UI</div>
                    <div style="font-size: 0.85rem; color: #CBD5E1;">Cria 5 questões (fechadas e abertas com gabarito) e programa o código reativo em Streamlit com gráficos Plotly.</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Layout de Entradas Principais
    st.markdown("### 📝 1. Identificação & Escopo da Disciplina")
    st.info("💡 **Por que preencher?** O nome do professor e o código da disciplina identificam o seu acervo no banco de memória (RAG). A IA lembrará do seu estilo e convenções usadas em aulas passadas.")

    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            nome_professor = st.text_input(
                "👤 Nome do Professor", 
                help="Digite seu nome completo ou como deseja ser identificado nos relatórios acadêmicos e acervo RAG."
            )

        # Seleção da disciplina
        disciplinas_options = list(DISCIPLINAS_PRECARREGADAS.keys()) + ["Outra (Upload Customizado)"]
        disciplina_selecionada = st.selectbox(
            "📚 Selecione a Disciplina Acadêmica", 
            options=disciplinas_options,
            help="Escolha uma disciplina pré-carregada para usar a ementa oficial já cadastrada, ou escolha 'Outra' para enviar um PDF customizado."
        )
        
        is_custom = (disciplina_selecionada == "Outra (Upload Customizado)")
        
        if is_custom:
            with col2:
                codigo_disciplina = st.text_input(
                    "🏷️ Código da Disciplina", 
                    help="Código identificador da disciplina (ex: MATD38, EST001)."
                )
            tema_solicitado = st.text_input(
                "🎯 Tema da Aula", 
                help="Tópico estatístico/matemático principal que será abordado nesta aula."
            )
        else:
            codigo_disciplina = DISCIPLINAS_PRECARREGADAS[disciplina_selecionada]["codigo"]
            with col2:
                st.text_input(
                    "🏷️ Código da Disciplina", 
                    value=codigo_disciplina, 
                    disabled=True, 
                    help="Código identificador oficial correspondente à disciplina selecionada."
                )
            
            temas_possiveis = DISCIPLINAS_PRECARREGADAS[disciplina_selecionada]["temas"]
            tema_solicitado = st.selectbox(
                "🎯 Tema da Aula (Extraído da Ementa Oficial)", 
                options=temas_possiveis, 
                help="Selecione um tópico específico extraído diretamente da ementa oficial da disciplina."
            )

    st.markdown("---")
    st.markdown("### 📂 2. Documentos da Disciplina (Ementa & RAG do Professor)")
    
    with st.container(border=True):
        if is_custom:
            st.info("💡 **Guia de Referência da Ementa (Opcional):** Se anexada, a ementa servirá como bússola de referência didática para o Agente Roteirista, auxiliando a alinhar os tópicos com o programa do curso.")
            ementa_file = st.file_uploader(
                "📄 Ementa da Disciplina (PDF) - OPCIONAL",
                type=["pdf"],
                help="O PDF oficial da ementa para ser usado como guia de referência do programa do curso."
            )
        else:
            st.success(f"📋 **Ementa de Referência Ativa:** A ementa oficial para **{disciplina_selecionada}** está pré-carregada como guia de referência.")
            ementa_file = None

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        st.info("💡 **Dica Didática para Materiais de Apoio:** Quanto mais notas de aula, slides, apostilas ou provas antigas você anexar, mais fiel será o tom de voz da IA. O agente aprenderá a sua notação, terminologias e os seus exemplos favoritos.")
        materiais_apoio = st.file_uploader(
            "📚 Materiais de Apoio do Professor (Anexe múltiplos PDFs, Slides, Imagens, Apostilas, Notas em TXT ou MD)",
            type=["pdf", "png", "jpg", "jpeg", "webp", "txt", "md"],
            accept_multiple_files=True,
            help="Selecione e anexe múltiplos arquivos juntos. Todos os documentos serão processados pelo RAG para que a IA aprenda a linguagem do professor."
        )

    # Seção de customização de diretrizes
    st.markdown("---")
    st.markdown("### 📐 3. Diretrizes de Notação e Identidade Visual (Opcional)")
    
    with st.container(border=True):
        st.info("""
            💡 **Como funcionam as diretrizes de notação?**
            Para garantir **zero erro** de renderização em fórmulas matemáticas (KaTeX), a plataforma utiliza como base o documento oficial `diretrizes_padrao.md`. 
            Você pode **baixar este documento em Markdown**, visualizá-lo ou editá-lo offline, e anexar uma versão customizada abaixo caso queira convenções específicas da sua instituição.
        """)
        
        col_dl, col_up = st.columns([1, 1])
        
        with col_dl:
            st.markdown("##### 📄 Documento de Diretrizes Padrão")
            conteudo_diretrizes_padrao = ""
            if os.path.exists("diretrizes_padrao.md"):
                with open("diretrizes_padrao.md", "r", encoding="utf-8") as f_dir:
                    conteudo_diretrizes_padrao = f_dir.read()
            
            st.download_button(
                label="📥 Baixar Diretrizes Padrão (.md)",
                data=conteudo_diretrizes_padrao,
                file_name="diretrizes_padrao.md",
                mime="text/markdown",
                use_container_width=True,
                help="Clique para baixar o arquivo de diretrizes oficiais em formato Markdown (.md) para visualizar ou modificar offline."
            )
            
        with col_up:
            st.markdown("##### 📤 Anexar Diretrizes Customizadas")
            arquivo_diretrizes_custom = st.file_uploader(
                "Upload de Arquivos de Diretrizes (.md, .txt, .pdf):",
                type=["md", "txt", "pdf", "png", "jpg", "jpeg", "webp"],
                accept_multiple_files=True,
                key="uploader_diretrizes_custom",
                help="Envie um ou mais arquivos de diretrizes customizados para complementar ou substituir as regras padrão do professor."
            )
            
        st.markdown("---")
        st.markdown("##### 🎨 Identidade Visual (Paleta de Cores Harmônica em Gradação de Tons)")
        st.caption("Escolha a paleta temática de cores para a sua aula. A plataforma aplicará os tons nos cartões de exemplo, tabelas e curvas dos simuladores Plotly.")
        
        paletas_predefinidas = {
            "🔵 Tons de Azul Institucional (Padrão Acadêmico)": {
                "principal": "#1E3A8A", # Azul Marinho Escuro
                "secundaria": "#2563EB", # Azul Real
                "alerta": "#3B82F6",    # Azul Claro
                "critica": "#991B1B",   # Vermelho Crítico
                "tons": ["#0F172A", "#1E3A8A", "#2563EB", "#3B82F6", "#60A5FA"]
            },
            "🟢 Tons de Verde Esmeralda (Saúde, Biologia & Vida)": {
                "principal": "#064E3B", # Verde Floresta
                "secundaria": "#10B981", # Verde Esmeralda
                "alerta": "#34D399",    # Verde Menta
                "critica": "#991B1B",   # Vermelho Crítico
                "tons": ["#022C22", "#064E3B", "#10B981", "#34D399", "#6EE7B7"]
            },
            "🟣 Tons de Roxo Imperial & Violeta": {
                "principal": "#4C1D95", # Roxo Escuro
                "secundaria": "#7C3AED", # Violeta
                "alerta": "#A78BFA",    # Lavanda
                "critica": "#991B1B",   # Vermelho Crítico
                "tons": ["#2E1065", "#4C1D95", "#7C3AED", "#A78BFA", "#C4B5FD"]
            },
            "🟧 Tons Quentes de Âmbar & Laranja (Mercado & Negócios)": {
                "principal": "#78350F", # Marrom/Âmbar Escuro
                "secundaria": "#D97706", # Laranja Âmbar
                "alerta": "#F59E0B",    # Amarelo Ouro
                "critica": "#991B1B",   # Vermelho Crítico
                "tons": ["#451A03", "#78350F", "#D97706", "#F59E0B", "#FBBF24"]
            },
            "🌑 Tons de Cinza Slate / Dark Tech": {
                "principal": "#0F172A", # Grafite Escuro
                "secundaria": "#334155", # Cinza Slate
                "alerta": "#64748B",    # Cinza Médio
                "critica": "#991B1B",   # Vermelho Crítico
                "tons": ["#020617", "#0F172A", "#334155", "#64748B", "#CBD5E1"]
            },
            "🎨 Personalizada (Escolha manual de cada cor)": None
        }
        
        col_pal1, col_pal2 = st.columns([2, 1])
        with col_pal1:
            paleta_selecionada_nome = st.selectbox(
                "Selecione a Paleta de Cores da Aula",
                options=list(paletas_predefinidas.keys()),
                help="Escolha uma paleta de cores temática pré-configurada em gradação de tons ou selecione a opção personalizada."
            )
            
        dados_paleta = paletas_predefinidas[paleta_selecionada_nome]
        
        if dados_paleta is not None:
            cor_principal = dados_paleta["principal"]
            cor_secundaria = dados_paleta["secundaria"]
            cor_alerta = dados_paleta["alerta"]
            cor_critica_padrao = dados_paleta["critica"]
            
            with col_pal2:
                cor_critica = st.color_picker("Cor Crítica (Região de Rejeição/Erro)", value=cor_critica_padrao, help="Cor destacada para indicar erros, alertas críticos ou regiões de rejeição nos testes.")
            
            # Barra visual de pré-visualização dos 5 tons da paleta selecionada
            tons_html = "".join([f"<div style='flex: 1; height: 28px; background-color: {c}; border-radius: 4px;' title='Tom {c}'></div>" for c in dados_paleta["tons"]])
            st.markdown(f"""
                <div style="margin-top: 0.5rem; margin-bottom: 1rem;">
                    <div style="font-size: 0.82rem; font-weight: 600; color: #64748B; margin-bottom: 0.3rem;">Visualização da Gradação de Tons da Paleta Selecionada:</div>
                    <div style="display: flex; gap: 6px; background: #F8FAFC; padding: 6px; border-radius: 8px; border: 1px solid #E2E8F0;">
                        {tons_html}
                    </div>
                </div>
            """, unsafe_allow_html=True)
        else:
            col_c1, col_c2, col_c3, col_c4 = st.columns(4)
            with col_c1:
                cor_principal = st.color_picker("Cor Primária", value="#1E3A8A")
            with col_c2:
                cor_secundaria = st.color_picker("Cor Secundária", value="#10B981")
            with col_c3:
                cor_alerta = st.color_picker("Cor de Alerta", value="#F59E0B")
            with col_c4:
                cor_critica = st.color_picker("Cor Crítica", value="#991B1B")

    st.markdown("---")
    st.markdown("### 🎯 4. Perfil da Turma & Informações Adicionais")
    st.info("💡 **Como funciona?** Selecione a área da sua turma. A inteligência artificial adaptará os exemplos práticos, os problemas resolvidos e a narrativa para o universo dos seus alunos (mantendo o rigor da graduação).")
    
    with st.container(border=True):
        foco_turma_opcoes = [
            "📊 Estatística & Matemática (Geral, Conceitual e Aprofundamento Teórico)",
            "🏥 Ciências da Saúde (Nutrição, Psicologia, Medicina, Biologia, Enfermagem)",
            "📈 Economia, Negócios & Finanças (Administração, Mercado Financeiro, Gestão)",
            "⚙️ Engenharia & Computação (Ciência de Dados, Algoritmos, Física)",
            "✍️ Outra Área / Foco Personalizado"
        ]
        
        foco_turma_sel = st.selectbox(
            "🎯 Área de Aplicação Principal da Turma",
            options=foco_turma_opcoes,
            help="Selecione o curso/área da turma para a IA direcionar os problemas e estudos de caso da aula."
        )
        
        if foco_turma_sel == "✍️ Outra Área / Foco Personalizado":
            foco_turma_custom = st.text_input(
                "Especifique a área ou curso da turma:",
                help="Ex: Agronomia, Arquitetura, Direito, etc."
            )
            
        st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
        diretrizes_adicionais = st.text_area(
            "✍️ Observações ou Orientações Extras da Aula (Opcional):",
            value="",
            height=100,
            help="Campo livre para acrescentar qualquer instrução adicional (ex: termos que prefere usar, tom de voz, etc.)."
        )

    st.markdown("---")
    st.markdown("### 🚀 5. Execução & Geração da Aula")
    st.info("💡 **Pronto para gerar?** Clique no botão abaixo para disparar a cadeia de Agentes de Inteligência Artificial (Roteirista, Escritor, Revisor, Editor e Exercícios) e produzir o capítulo de aula completo.")

    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
    submit_btn = st.button("🚀 Gerar Aula Acadêmica", key="btn_gerar_aula_unica_main", type="primary", use_container_width=True)
    submit_batch_btn = False

    # Lógica ao pressionar o botão de geração
    if submit_btn:
        st.session_state.is_batch_run = False
        t_inicio_geral_completo = time.time()

        ementa_bytes = ementa_file.getvalue() if (is_custom and 'ementa_file' in locals() and ementa_file) else None
        materiais_buffers = [(f.name, f.getvalue()) for f in materiais_apoio] if ('materiais_apoio' in locals() and materiais_apoio) else []
        diretrizes_custom_buffers = [(f.name, f.getvalue()) for f in arquivo_diretrizes_custom] if ('arquivo_diretrizes_custom' in locals() and arquivo_diretrizes_custom) else []

        params = {
            "nome_professor": nome_professor,
            "codigo_disciplina": codigo_disciplina,
            "tema_solicitado": tema_solicitado,
            "is_custom": is_custom,
            "ementa_bytes": ementa_bytes,
            "disciplina_selecionada": disciplina_selecionada,
            "materiais_buffers": materiais_buffers,
            "diretrizes_custom_buffers": diretrizes_custom_buffers,
            "cor_principal": cor_principal,
            "cor_secundaria": cor_secundaria,
            "cor_alerta": cor_alerta,
            "cor_critica": cor_critica,
            "foco_turma_sel": foco_turma_sel if 'foco_turma_sel' in locals() else "",
            "foco_turma_custom": foco_turma_custom if 'foco_turma_custom' in locals() else "",
            "diretrizes_adicionais": diretrizes_adicionais if 'diretrizes_adicionais' in locals() else "",
            "tempo_inicio": t_inicio_geral_completo
        }

        st.session_state.tempo_inicio = t_inicio_geral_completo
        st.session_state.sucesso_geracao = False
        st.session_state.erro_geracao = None
        st.session_state.mensagem_sucesso = ""
        st.session_state.scroll_to_top_done = False
        st.session_state.geracao_status = {
            "etapa_atual": "Iniciando...",
            "subetapa_detalhe": "Preparando arquivos e disparando agentes de inteligência artificial...",
            "subtopicos": [],
            "status_subtopicos": {},
            "tentativas_subtopicos": {},
            "max_tentativas_subtopicos": {},
            "tempo_inicio": t_inicio_geral_completo,
            "ativo": True,
            "sucesso": False,
            "erro": None,
            "mensagem_sucesso": "",
            "memoria_pedagogica": "",
            "params": params
        }
        st.session_state.gerando_aula = True

        disparar_thread_geracao(st.session_state.geracao_status, params)
        st.rerun()

if __name__ == "__main__":
    run_page()
