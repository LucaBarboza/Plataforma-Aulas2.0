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
    temp_ementa_path = params.get("temp_ementa_path")
    temp_materials_dir = params.get("temp_materials_dir")
    diretrizes_texto = params.get("diretrizes_texto", "")
    nome_professor_clean = params.get("nome_professor_clean", "")
    codigo_disciplina_clean = params.get("codigo_disciplina_clean", "")
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

        # 2. Geração de Conteúdo da Aula
        set_status("Fase 1: Roteirista", f"Analisando a ementa e estruturando a trilha pedagógica para: {tema_solicitado}...")
        from gerador_conteudo import gerar_conteudo_aula
        
        payload_teoria = gerar_conteudo_aula(
            nome_professor=nome_professor,
            codigo_disciplina=codigo_disciplina,
            tema_solicitado=tema_solicitado,
            ementa_pdf_path=temp_ementa_path,
            diretrizes_texto=diretrizes_texto,
            status_callback=status_callback,
            memoria_pedagogica_acumulada=status_dict.get("memoria_pedagogica", "")
        )
        
        if not payload_teoria:
            raise Exception("Falha operacional ao gerar o conteúdo teórico com a ementa fornecida.")

        set_status("Fase 2: Escrita e Revisão", "Roteiro pedagógico estruturado e subtopicos validados pelo Revisor!")
        
        log_gerador = payload_teoria.get("log_gerador", {})
        exec_log["etapas"]["2_roteirista"] = {
            "descricao": "Agente 1: Roteirista (Alinhamento de Escopo e Trilha)",
            "status": "sucesso",
            "duracao_segundos": log_gerador.get("tempo_roteirista_segundos", 0.0)
        }
        exec_log["etapas"]["3_escrita_revisao"] = {
            "descricao": "Agente 2 + 2.5: Escritor & Revisor (Loop de Revisão Ativa)",
            "status": "sucesso",
            "duracao_segundos": log_gerador.get("tempo_escrita_revisao_segundos", 0.0),
            "subtopicos": log_gerador.get("subtopicos", [])
        }

        os.makedirs("cache", exist_ok=True)
        with open(os.path.join("cache", "payload_teoria.json"), "w", encoding="utf-8") as f:
            json.dump(payload_teoria, f, indent=4, ensure_ascii=False)

        # 3. Lapidação Editorial
        set_status("Fase 3: Editor-Chefe", "Unificando trilha acadêmica e alocando simuladores interativos...")
        from orquestrador_editorial import lapidar_conteudo_global, expandir_subtopico_para_prosa_livro
        
        t_start_editorial = time.time()
        resultado_editorial = lapidar_conteudo_global(os.path.join("cache", "payload_teoria.json"), diretrizes_texto)
        t_end_editorial = time.time()
        
        if not resultado_editorial:
            raise Exception("Falha crítica no processo editorial de unificação.")
        
        set_status("Fase 3: Editor-Chefe", "Coerência global estabelecida e referências consolidadas no rodapé!")
        exec_log["etapas"]["4_lapidacao_editorial"] = {
            "descricao": "Agente 3.5: Editor-Chefe (Unificação e Coerência Global)",
            "status": "sucesso",
            "duracao_segundos": round(t_end_editorial - t_start_editorial, 2)
        }

        # 4. Expansão de Prosa Exaustiva
        t_start_prosa = time.time()
        total_pags = len(resultado_editorial["paginas_conteudo"])
        for idx, pagina in enumerate(resultado_editorial["paginas_conteudo"]):
            set_status(
                f"Fase 4: Construtor de Prosa ({idx+1}/{total_pags})", 
                f"Redigindo com profundidade o subtópico: {pagina['titulo_subtopico']}"
            )
            dados_subtopico = {
                "titulo_subtopico": pagina["titulo_subtopico"],
                "discussao_teorica_prosa": pagina["discussao_teorica_prosa"],
                "formalismo_latex": pagina["formalismo_latex"]
            }
            try:
                prosa_longa = expandir_subtopico_para_prosa_livro(dados_subtopico, diretrizes_texto)
                pagina["prosa_longa_expandida"] = prosa_longa
            except Exception as e:
                set_status(
                    f"Fase 4: Construtor de Prosa ({idx+1}/{total_pags})",
                    f"⚠️ Falha de expansão no subtópico, utilizando prosa base. Erro: {e}"
                )
                pagina["prosa_longa_expandida"] = pagina["discussao_teorica_prosa"]
            time.sleep(1)
                
        t_end_prosa = time.time()
        exec_log["etapas"]["5_expansao_prosa"] = {
            "descricao": "Agente 3.75: Construtor de Prosa (Expansão Exaustiva de Livro)",
            "status": "sucesso",
            "duracao_segundos": round(t_end_prosa - t_start_prosa, 2)
        }

        with open(os.path.join("cache", "payload_teoria_gigante.json"), "w", encoding="utf-8") as f:
            json.dump(resultado_editorial, f, indent=4, ensure_ascii=False)

        # 5. Geração de Exercícios
        set_status("Fase 5: Caderno de Exercícios", "Projetando caderno de exercícios com múltipla escolha e discursivas...")
        from gerador_exercicios import gerar_caderno_exercicios
        
        t_start_exercicios = time.time()
        resultado_exercicios = gerar_caderno_exercicios(
            caminho_payload_teoria=os.path.join("cache", "payload_teoria.json"),
            nome_professor=nome_professor,
            codigo_disciplina=codigo_disciplina,
            diretrizes_texto=diretrizes_texto
        )
        t_end_exercicios = time.time()
        
        if not resultado_exercicios:
            raise Exception("Erro ao gerar o caderno de exercícios.")

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

        # Limpeza (Arquivo de ementa mantido no cache para reutilização no modo Lote/Batch)
        pass

        exec_log["status"] = "sucesso"
        exec_log["tempo_total_segundos"] = round(time.time() - t_inicio_geral_completo, 2)
        exec_log["timestamp_fim"] = time.strftime("%Y-%m-%d %H:%M:%S")
        
        from orquestrador_editorial import gerar_resumo_compacto_aula
        status_dict["resumo_aula"] = gerar_resumo_compacto_aula(resultado_editorial)

        with open(os.path.join("cache", "ultimo_log_execucao.json"), "w", encoding="utf-8") as f:
            json.dump(exec_log, f, indent=4, ensure_ascii=False)

        # CHECKPOINT DE SEGURANÇA EM LOTE
        try:
            os.makedirs("cache", exist_ok=True)
            checkpoint_path = os.path.join("cache", f"batch_checkpoint_{codigo_disciplina_clean}.json")
            cp_existente = {}
            if os.path.exists(checkpoint_path):
                try:
                    with open(checkpoint_path, "r", encoding="utf-8") as f_cp:
                        cp_existente = json.load(f_cp)
                except: pass
            
            temas_concluidos = cp_existente.get("temas_concluidos", [])
            if tema_solicitado not in temas_concluidos:
                temas_concluidos.append(tema_solicitado)
                
            batch_memoria = cp_existente.get("batch_memoria", "")
            if status_dict.get("resumo_aula"):
                batch_memoria += "\n\n" + status_dict["resumo_aula"]
                
            clean_params = {k: v for k, v in params.items() if k != "params"}
            checkpoint_data = {
                "codigo_disciplina": codigo_disciplina,
                "nome_professor": nome_professor,
                "ultimo_tema_concluido": tema_solicitado,
                "temas_concluidos": temas_concluidos,
                "batch_memoria": batch_memoria,
                "batch_total": params.get("batch_total", len(temas_concluidos)),
                "batch_queue": params.get("batch_queue", []),
                "params": clean_params,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            with open(checkpoint_path, "w", encoding="utf-8") as f:
                json.dump(checkpoint_data, f, indent=4, ensure_ascii=False)
        except Exception as e_cp:
            print(f"[CHECKPOINT] Aviso ao gravar checkpoint de lote: {e_cp}")

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

            # Git commit
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
                nome_arquivo_log = os.path.basename(caminho_log_especifico)
                caminho_repositorio_log = f"logdasaulasgeradas/{nome_arquivo_log}"
                commitar_arquivo_github(
                    caminho_local=caminho_log_especifico,
                    caminho_repositorio=caminho_repositorio_log,
                    mensagem_commit=f"feat: adiciona log json {caminho_repositorio_log}"
                )
                nome_arquivo_txt = os.path.basename(caminho_log_txt)
                caminho_repositorio_txt = f"logdasaulasgeradas/{nome_arquivo_txt}"
                commitar_arquivo_github(
                    caminho_local=caminho_log_txt,
                    caminho_repositorio=caminho_repositorio_txt,
                    mensagem_commit=f"feat: adiciona log descritivo txt {caminho_repositorio_txt}"
                )
            except: pass

        if sucesso_py:
            status_dict["mensagem_sucesso"] = "✨ A geração foi concluída perfeitamente! Os arquivos da aula e relatórios foram salvos no GitHub."
        else:
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
            if st.button("🪄 Criar Outra Aula", use_container_width=True):
                st.session_state.sucesso_geracao = False
                st.rerun()
        with col_b2:
            if st.button("📚 Atualizar Trilha & Concluir", type="primary", use_container_width=True):
                st.session_state.sucesso_geracao = False
                st.rerun()
        return
    elif st.session_state.erro_geracao:
        tempo_decorrido = time.time() - st.session_state.tempo_inicio
        minutos = int(tempo_decorrido // 60)
        segundos = int(tempo_decorrido % 60)
        st.error(f"❌ Geração abortada após {minutos:02d}:{segundos:02d} devido a uma falha crítica!")
        st.error(f"Detalhes do erro: {st.session_state.erro_geracao}")
        st.session_state.erro_geracao = None
        if st.button("Voltar ao Painel"):
            st.rerun()
        return
    # Bloco informativo premium
    st.info("""
        **🎓 Como funciona a geração de aulas Plataforma 2.0:**
        1. **Alinhamento de Escopo**: O Agente Roteirista analisará a ementa em PDF enviada para desenhar uma trilha perfeitamente alinhada.
        2. **Construção e Revisão Crítica**: Os Agentes Escritor e Revisor redigirão o conteúdo e auditarão as fórmulas matemáticas em LaTeX.
        3. **Refinamento Editorial e Expansão**: O Editor-Chefe removerá repetições e o Construtor de Prosa expandirá a explicação em prosa densa de livro.
        4. **Caderno de Exercícios & Compilação**: Serão criadas 5 questões fechadas e 3 abertas antes do compilador costurar o simulador interativo em Plotly.
    """)

    # Layout de Entradas Principais (Sem st.form para permitir interações dinâmicas fluidas)
    st.markdown("### 📝 Identificação & Tema")
    col1, col2 = st.columns(2)
    with col1:
        nome_professor = st.text_input("Nome do Professor", help="Nome do professor responsável pela disciplina.")

    # Seleção da disciplina
    disciplinas_options = list(DISCIPLINAS_PRECARREGADAS.keys()) + ["Outra (Upload Customizado)"]
    disciplina_selecionada = st.selectbox(
        "Selecione a Disciplina", 
        options=disciplinas_options,
        help="Escolha uma disciplina pré-carregada ou faça o upload manual de outra ementa."
    )
    
    is_custom = (disciplina_selecionada == "Outra (Upload Customizado)")
    
    if is_custom:
        with col2:
            codigo_disciplina = st.text_input("Código da Disciplina", help="Código identificador da disciplina (ex: MATD38).")
        tema_solicitado = st.text_input("Tema da Aula", help="Tópico estatístico/matemático principal que será abordado na aula.")
    else:
        codigo_disciplina = DISCIPLINAS_PRECARREGADAS[disciplina_selecionada]["codigo"]
        with col2:
            st.text_input("Código da Disciplina", value=codigo_disciplina, disabled=True, help="Código identificador da disciplina correspondente.")
        
        temas_possiveis = DISCIPLINAS_PRECARREGADAS[disciplina_selecionada]["temas"]
        tema_solicitado = st.selectbox(
            "Tema da Aula", 
            options=temas_possiveis, 
            help="Selecione um tópico específico extraído diretamente da ementa oficial."
        )

    st.markdown("---")
    st.markdown("### 📂 Documentos da Disciplina")
    
    if is_custom:
        ementa_file = st.file_uploader(
            "Ementa da Disciplina (PDF) - OBRIGATÓRIO",
            type=["pdf"],
            help="O PDF oficial da ementa que ditará o escopo do que deve ser ensinado."
        )
    else:
        st.info(f"📋 A ementa oficial para **{disciplina_selecionada}** já está pré-carregada no sistema.")
        ementa_file = None

    materiais_apoio = st.file_uploader(
        "Materiais de Apoio (PDFs/Imagens) - OPCIONAL",
        type=["pdf", "png", "jpg", "jpeg", "webp"],
        accept_multiple_files=True,
        help="Livros, artigos, imagens de referência ou notas de aula do professor para construir o RAG pessoal da disciplina."
    )

    # Seção opcional de customização de diretrizes
    st.markdown("---")
    
    notacoes_interface = {}
    
    with st.expander("📐 Customizar Diretrizes de Notação e Cores (Opcional)", expanded=False):
        st.markdown("##### 📥 Importar Diretrizes com IA")
        col_up, col_btn = st.columns([7, 3])
        with col_up:
            arquivo_diretrizes = st.file_uploader(
                "Faça o upload do arquivo de diretrizes do professor (PDF, Imagens, TXT ou MD):",
                type=["pdf", "png", "jpg", "jpeg", "webp", "txt", "md"],
                key="uploader_diretrizes",
                help="Selecione um arquivo onde o professor descreve suas convenções, notações, cores de preferência, imagens de referência ou estilo."
            )
        tem_arquivos_para_analise = bool(arquivo_diretrizes) or bool(materiais_apoio)

        with col_btn:
            st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
            processar_btn = st.button("Categorizar com IA", use_container_width=True, disabled=not tem_arquivos_para_analise)
            
        if processar_btn and tem_arquivos_para_analise:
            status_diretrizes = st.status("Processando arquivo(s) com IA...")
            caminhos_temporarios = []
            try:
                os.makedirs("cache", exist_ok=True)
                lista_info_arquivos = []
                
                # 1. Se houver arquivo específico de diretrizes
                if arquivo_diretrizes:
                    ext = os.path.splitext(arquivo_diretrizes.name)[1]
                    c_temp = os.path.join("cache", f"temp_diretriz_{int(time.time())}{ext}")
                    with open(c_temp, "wb") as f:
                        f.write(arquivo_diretrizes.getbuffer())
                    caminhos_temporarios.append(c_temp)
                    lista_info_arquivos.append((c_temp, arquivo_diretrizes.name))
                    
                # 2. Se houver materiais de apoio anexados
                if materiais_apoio:
                    for i, mat in enumerate(materiais_apoio):
                        ext = os.path.splitext(mat.name)[1]
                        c_temp = os.path.join("cache", f"temp_mat_{i}_{int(time.time())}{ext}")
                        with open(c_temp, "wb") as f:
                            f.write(mat.getbuffer())
                        caminhos_temporarios.append(c_temp)
                        lista_info_arquivos.append((c_temp, mat.name))

                status_diretrizes.update(label=f"Analisando {len(lista_info_arquivos)} arquivo(s) com Gemini...")
                
                # Executa o analisador de diretrizes
                from analisador_diretrizes import processar_arquivo_diretrizes_ia
                res_ia = processar_arquivo_diretrizes_ia(lista_info_arquivos)
                
                # Salva no session state
                st.session_state.diretrizes_ia_valores = res_ia
                
                # Se houver notações customizadas na resposta da IA, adiciona nas customizadas da página
                if "notacoes_customizadas" in res_ia and res_ia["notacoes_customizadas"]:
                    st.session_state.custom_notations = res_ia["notacoes_customizadas"]
                
                status_diretrizes.update(label=f"✅ Diretrizes extraídas com sucesso a partir de {len(lista_info_arquivos)} arquivo(s)!", state="complete")
                st.toast(f"Diretrizes importadas de {len(lista_info_arquivos)} arquivo(s)!")
                time.sleep(1)
                st.rerun()
            except Exception as ex:
                status_diretrizes.update(label=f"❌ Erro no processamento: {ex}", state="error")
                st.error(f"Erro detalhado: {ex}")
            finally:
                # Limpa arquivos temporários
                for path_temp in caminhos_temporarios:
                    if os.path.exists(path_temp):
                        try:
                            os.remove(path_temp)
                        except Exception:
                            pass

        # Se já foi importado, exibe um feedback visual e a opção de limpar
        if st.session_state.diretrizes_ia_valores:
            col_info, col_clear = st.columns([8, 2])
            with col_info:
                st.info("💡 **Diretrizes importadas ativas:** A parametrização abaixo foi pré-preenchida de acordo com o arquivo processado.")
            with col_clear:
                st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
                if st.button("Limpar Filtros", use_container_width=True, key="limpar_diretrizes_ia"):
                    st.session_state.diretrizes_ia_valores = {}
                    st.session_state.custom_notations = []
                    st.rerun()

        st.markdown("---")
        st.markdown("""
            Selecione as abas abaixo para alterar símbolos de notação matemática e cores do template.
            Opções não alteradas manterão os padrões rigorosos de livro didático da plataforma.
        """)
        
        tab_d1, tab_d2, tab_d3, tab_d4, tab_d5 = st.tabs([
            "📊 População & Amostra", 
            "🔬 Inferência & Hipóteses", 
            "📈 Regressão & Correlação", 
            "🎲 Distribuições & Funções", 
            "➕ Customizadas"
        ])
        
        with tab_d1:
            st.markdown("##### 📊 Elementos de Amostra e População")
            col_a1, col_a2, col_a3 = st.columns(3)
            with col_a1:
                notacoes_interface["tamanho_amostral"] = st.text_input("Tamanho Amostral", value=obter_valor_diretriz("tamanho_amostral", r"$n$"))
                notacoes_interface["tamanho_populacional"] = st.text_input("Tamanho Populacional", value=obter_valor_diretriz("tamanho_populacional", r"$N$"))
                notacoes_interface["media_populacional"] = st.text_input("Média Populacional", value=obter_valor_diretriz("media_populacional", r"$\mu$"))
                notacoes_interface["media_amostral"] = st.text_input("Média Amostral", value=obter_valor_diretriz("media_amostral", r"$\bar{X}$"))
            with col_a2:
                notacoes_interface["variancia_populacional"] = st.text_input("Variância Populacional", value=obter_valor_diretriz("variancia_populacional", r"$\sigma^2$"))
                notacoes_interface["variancia_amostral"] = st.text_input("Variância Amostral", value=obter_valor_diretriz("variancia_amostral", r"$S^2$"))
                notacoes_interface["desvio_padrao_populacional"] = st.text_input("Desvio Padrão Populacional", value=obter_valor_diretriz("desvio_padrao_populacional", r"$\sigma$"))
                notacoes_interface["desvio_padrao_amostral"] = st.text_input("Desvio Padrão Amostral", value=obter_valor_diretriz("desvio_padrao_amostral", r"$S$"))
            with col_a3:
                notacoes_interface["proporcao_populacional"] = st.text_input("Proporção Populacional", value=obter_valor_diretriz("proporcao_populacional", r"$p$"))
                notacoes_interface["proporcao_amostral"] = st.text_input("Proporção Amostral", value=obter_valor_diretriz("proporcao_amostral", r"$\hat{p}$"))
                notacoes_interface["margem_erro"] = st.text_input("Margem de Erro", value=obter_valor_diretriz("margem_erro", r"$E$"))
                notacoes_interface["intervalo_confianca"] = st.text_input("Intervalo de Confiança", value=obter_valor_diretriz("intervalo_confianca", r"$IC$"))
                notacoes_interface["erro_padrao_media"] = st.text_input("Erro Padrão da Média", value=obter_valor_diretriz("erro_padrao_media", r"$EP(\bar{X})$"))

        with tab_d2:
            st.markdown("##### 🔬 Inferência Estatística & Testes de Hipóteses")
            col_h1, col_h2, col_h3 = st.columns(3)
            with col_h1:
                notacoes_interface["hipotese_nula"] = st.text_input("Hipótese Nula", value=obter_valor_diretriz("hipotese_nula", r"$H_0$"))
                notacoes_interface["hipotese_alternativa"] = st.text_input("Hipótese Alternativa", value=obter_valor_diretriz("hipotese_alternativa", r"$H_1$"))
                notacoes_interface["nivel_significancia"] = st.text_input("Nível de Significância (Alfa)", value=obter_valor_diretriz("nivel_significancia", r"$\alpha$"))
                notacoes_interface["nivel_confianca"] = st.text_input("Nível de Confiança", value=obter_valor_diretriz("nivel_confianca", r"$1 - \alpha$"))
                notacoes_interface["erro_tipo_2"] = st.text_input("Erro Tipo II (Beta)", value=obter_valor_diretriz("erro_tipo_2", r"$\beta$"))
                notacoes_interface["poder_teste"] = st.text_input("Poder do Teste", value=obter_valor_diretriz("poder_teste", r"$1 - \beta$"))
            with col_h2:
                notacoes_interface["p_valor"] = st.text_input("P-Valor", value=obter_valor_diretriz("p_valor", r"$p\text{-valor}$"))
                notacoes_interface["regiao_rejeicao"] = st.text_input("Região Crítica (Rejeição)", value=obter_valor_diretriz("regiao_rejeicao", r"$RC$"))
                notacoes_interface["graus_liberdade"] = st.text_input("Graus de Liberdade", value=obter_valor_diretriz("graus_liberdade", r"$gl$"))
                notacoes_interface["graus_liberdade_num"] = st.text_input("Graus de Liberdade (Numerador)", value=obter_valor_diretriz("graus_liberdade_num", r"$gl_{\text{num}}$"))
                notacoes_interface["graus_liberdade_den"] = st.text_input("Graus de Liberdade (Denominador)", value=obter_valor_diretriz("graus_liberdade_den", r"$gl_{\text{den}}$"))
            with col_h3:
                notacoes_interface["estatistica_z_calc"] = st.text_input("Estatística Z Calculada", value=obter_valor_diretriz("estatistica_z_calc", r"$Z_{\text{calc}}$"))
                notacoes_interface["estatistica_t_calc"] = st.text_input("Estatística t Calculada", value=obter_valor_diretriz("estatistica_t_calc", r"$t_{\text{calc}}$"))
                notacoes_interface["estatistica_chi2_calc"] = st.text_input("Estatística Qui-Quadrado Calculada", value=obter_valor_diretriz("estatistica_chi2_calc", r"$\chi^2_{\text{calc}}$"))
                notacoes_interface["estatistica_f_calc"] = st.text_input("Estatística F Calculada", value=obter_valor_diretriz("estatistica_f_calc", r"$F_{\text{calc}}$"))
                notacoes_interface["valor_critico_z"] = st.text_input("Valor Crítico Z", value=obter_valor_diretriz("valor_critico_z", r"$Z_{\text{crit}}$"))
                notacoes_interface["valor_critico_t"] = st.text_input("Valor Crítico t", value=obter_valor_diretriz("valor_critico_t", r"$t_{\text{crit}}$"))
                notacoes_interface["valor_critico_chi2"] = st.text_input("Valor Crítico Qui-Quadrado", value=obter_valor_diretriz("valor_critico_chi2", r"$\chi^2_{\text{crit}}$"))
                notacoes_interface["valor_critico_f"] = st.text_input("Valor Crítico F", value=obter_valor_diretriz("valor_critico_f", r"$F_{\text{crit}}$"))

        with tab_d3:
            st.markdown("##### 📈 Correlação, Regressão Linear & Somas de Quadrados")
            col_r1, col_r2, col_r3 = st.columns(3)
            with col_r1:
                notacoes_interface["correlacao_populacional"] = st.text_input("Correlação Populacional (Rho)", value=obter_valor_diretriz("correlacao_populacional", r"$\rho$"))
                notacoes_interface["correlacao_amostral"] = st.text_input("Correlação Amostral (r)", value=obter_valor_diretriz("correlacao_amostral", r"$r$"))
                notacoes_interface["coeficiente_determinacao"] = st.text_input("Coeficiente de Determinação (R²)", value=obter_valor_diretriz("coeficiente_determinacao", r"$R^2$"))
                notacoes_interface["covariancia_populacional"] = st.text_input("Covariância Populacional", value=obter_valor_diretriz("covariancia_populacional", r"$\sigma_{XY}$"))
                notacoes_interface["covariancia_amostral"] = st.text_input("Covariância Amostral", value=obter_valor_diretriz("covariancia_amostral", r"$S_{XY}$"))
            with col_r2:
                notacoes_interface["intercepto_populacional"] = st.text_input("Intercepto Populacional (Beta 0)", value=obter_valor_diretriz("intercepto_populacional", r"$\beta_0$"))
                notacoes_interface["inclinacao_populacional"] = st.text_input("Inclinação Populacional (Beta 1)", value=obter_valor_diretriz("inclinacao_populacional", r"$\beta_1$"))
                notacoes_interface["intercepto_estimado"] = st.text_input("Intercepto Estimado (Beta 0 chapéu)", value=obter_valor_diretriz("intercepto_estimado", r"$\hat{\beta}_0$"))
                notacoes_interface["inclinacao_estimado"] = st.text_input("Inclinação Estimada (Beta 1 chapéu)", value=obter_valor_diretriz("inclinacao_estimado", r"$\hat{\beta}_1$"))
                notacoes_interface["residuo_amostral"] = st.text_input("Resíduo Amostral (Erro)", value=obter_valor_diretriz("residuo_amostral", r"$e_i$"))
            with col_r3:
                notacoes_interface["soma_quadrados_regressao"] = st.text_input("Soma de Quadrados da Regressão (SQR)", value=obter_valor_diretriz("soma_quadrados_regressao", r"$SQR$"))
                notacoes_interface["soma_quadrados_erro"] = st.text_input("Soma de Quadrados do Erro (SQE)", value=obter_valor_diretriz("soma_quadrados_erro", r"$SQE$"))
                notacoes_interface["soma_quadrados_total"] = st.text_input("Soma de Quadrados Total (SQT)", value=obter_valor_diretriz("soma_quadrados_total", r"$SQT$"))

        with tab_d4:
            st.markdown("##### 🎲 Distribuições Teóricas & Notação Matemática de Funções")
            col_f1, col_f2, col_f3 = st.columns(3)
            with col_f1:
                notacoes_interface["distribuicao_normal"] = st.text_input("Distribuição Normal", value=obter_valor_diretriz("distribuicao_normal", r"$N(\mu, \sigma^2)$"))
                notacoes_interface["distribuicao_normal_padrao"] = st.text_input("Distribuição Normal Padrão", value=obter_valor_diretriz("distribuicao_normal_padrao", r"$N(0, 1)$"))
                notacoes_interface["distribuicao_t"] = st.text_input("Distribuição t de Student", value=obter_valor_diretriz("distribuicao_t", r"$t(gl)$"))
                notacoes_interface["distribuicao_qui_quadrado"] = st.text_input("Distribuição Qui-Quadrado", value=obter_valor_diretriz("distribuicao_qui_quadrado", r"$\chi^2(gl)$"))
            with col_f2:
                notacoes_interface["distribuicao_f"] = st.text_input("Distribuição F de Snedecor", value=obter_valor_diretriz("distribuicao_f", r"$F(gl_{\text{num}}, gl_{\text{den}})$"))
                notacoes_interface["distribuicao_binomial"] = st.text_input("Distribuição Binomial", value=obter_valor_diretriz("distribuicao_binomial", r"$Bin(n, p)$"))
                notacoes_interface["distribuicao_poisson"] = st.text_input("Distribuição Poisson", value=obter_valor_diretriz("distribuicao_poisson", r"$Poi(\lambda)$"))
            with col_f3:
                notacoes_interface["funcao_densidade"] = st.text_input("Função de Densidade / Probabilidade", value=obter_valor_diretriz("funcao_densidade", r"$f(x)$"))
                notacoes_interface["funcao_acumulada"] = st.text_input("Função de Distribuição Acumulada", value=obter_valor_diretriz("funcao_acumulada", r"$F(x)$"))
                notacoes_interface["somatorio"] = st.text_input("Somatório", value=obter_valor_diretriz("somatorio", r"$\sum$"))
                notacoes_interface["productorio"] = st.text_input("Produtório", value=obter_valor_diretriz("productorio", r"$\prod$"))
                notacoes_interface["integral"] = st.text_input("Integral", value=obter_valor_diretriz("integral", r"$\int$"))

        with tab_d5:
            st.markdown("##### ➕ Adicionar Notações Personalizadas Dinâmicas")
            st.markdown("Adicione regras adicionais de notação matemática e símbolos livres para orientar a geração do professor:")
            
            # Renderiza as linhas de notações customizadas
            novas_remover = []
            for i, item in enumerate(st.session_state.custom_notations):
                col_k, col_v, col_del = st.columns([5, 5, 1])
                with col_k:
                    item["conceito"] = st.text_input(f"Nome do Conceito / Função {i+1}", value=item["conceito"], key=f"custom_k_{i}")
                with col_v:
                    item["simbolo"] = st.text_input(f"Símbolo em LaTeX {i+1}", value=item["simbolo"], key=f"custom_v_{i}")
                with col_del:
                    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
                    if st.button("🗑️", key=f"custom_del_{i}"):
                        novas_remover.append(i)
            
            # Remove elementos marcados
            if novas_remover:
                for idx in sorted(novas_remover, reverse=True):
                    st.session_state.custom_notations.pop(idx)
                st.rerun()

            # Botão para adicionar mais uma linha
            if st.button("➕ Adicionar Linha de Notação"):
                st.session_state.custom_notations.append({"conceito": "", "simbolo": ""})
                st.rerun()

        st.markdown("---")
        st.markdown("##### 🎨 Identidade Visual (Cores)")
        col_c1, col_c2, col_c3, col_c4 = st.columns(4)
        
        # Inicializa cores preferidas com fallback
        cores_ia = st.session_state.diretrizes_ia_valores.get("cores_preferidas") or {} if st.session_state.diretrizes_ia_valores else {}
        cor_principal_padrao = cores_ia.get("cor_primaria") or "#1E3A8A"
        cor_secundaria_padrao = cores_ia.get("cor_secundaria") or "#10B981"
        cor_alerta_padrao = cores_ia.get("cor_alerta") or "#F59E0B"
        cor_critica_padrao = cores_ia.get("cor_critica") or "#991B1B"
        
        with col_c1:
            cor_principal = st.color_picker("Cor Primária (Identidade)", value=cor_principal_padrao)
        with col_c2:
            cor_secundaria = st.color_picker("Cor Secundária (Gráficos/Sucesso)", value=cor_secundaria_padrao)
        with col_c3:
            cor_alerta = st.color_picker("Cor de Alerta (Aviso/Atenção)", value=cor_alerta_padrao)
        with col_c4:
            cor_critica = st.color_picker("Cor Crítica (Erro/Rejeição)", value=cor_critica_padrao)

        st.markdown("##### ✍️ Diretrizes de Estilo Livres")
        diretrizes_adicionais_padrao = st.session_state.diretrizes_ia_valores.get("diretrizes_estilo_livre") or "" if st.session_state.diretrizes_ia_valores else ""
        diretrizes_adicionais = st.text_area(
            "Diretrizes didáticas e regras de estilo adicionais (Texto Livre)",
            value=diretrizes_adicionais_padrao,
            placeholder="Ex: Evitar anglicismos, focar em exemplos voltados a ciências biológicas..."
        )

    # Verificação e Interface para Retomada de Lote Interrompido (Checkpoint Persistence)
    codigo_disciplina_clean = codigo_disciplina.lower().strip()
    checkpoint_file = os.path.join("cache", f"batch_checkpoint_{codigo_disciplina_clean}.json")
    if not os.path.exists(checkpoint_file):
        cand_fallback = os.path.join("cache", "batch_checkpoint.json")
        if os.path.exists(cand_fallback):
            checkpoint_file = cand_fallback

    if os.path.exists(checkpoint_file):
        try:
            with open(checkpoint_file, "r", encoding="utf-8") as f_cp:
                cp_data = json.load(f_cp)
            temas_concluidos = cp_data.get("temas_concluidos", [])
            temas_restantes = cp_data.get("batch_queue", [])
            
            if temas_restantes:
                st.warning(f"⏯️ **Processo em Lote Interrompido Encontrado para {codigo_disciplina.upper()}**:\n- **Aulas Concluídas com Sucesso**: {len(temas_concluidos)} ({', '.join([t[:30]+'...' for t in temas_concluidos[:2]])})\n- **Próxima Aula a Gerar**: {temas_restantes[0]}")
                
                col_res1, col_res2 = st.columns(2)
                with col_res1:
                    if st.button(f"⏯️ Retomar Lote da Aula {len(temas_concluidos)+1} ({len(temas_restantes)} pendentes)", type="primary", use_container_width=True):
                        st.session_state.is_batch_run = True
                        st.session_state.batch_total = cp_data.get("batch_total", len(temas_concluidos) + len(temas_restantes))
                        st.session_state.batch_index = len(temas_concluidos) + 1
                        st.session_state.batch_memoria = cp_data.get("batch_memoria", "")
                        
                        proximo_tema = temas_restantes.pop(0)
                        st.session_state.batch_queue = temas_restantes
                        
                        raw_params = cp_data.get("params", {})
                        saved_params = {k: v for k, v in raw_params.items() if k != "params"}
                        saved_params["tema_solicitado"] = proximo_tema
                        saved_params["tempo_inicio"] = time.time()
                        saved_params["batch_queue"] = temas_restantes
                        saved_params["batch_total"] = st.session_state.batch_total
                        
                        t_novo_inicio = time.time()
                        st.session_state.tempo_inicio = t_novo_inicio
                        novo_status = {
                            "etapa_atual": f"Retomando Tópico {st.session_state.batch_index}/{st.session_state.batch_total}...",
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
                            "params": saved_params
                        }
                        st.session_state.geracao_status = novo_status
                        st.session_state.gerando_aula = True
                        disparar_thread_geracao(novo_status, saved_params)
                        st.rerun()
                with col_res2:
                    if st.button("🗑️ Descartar Checkpoint e Reiniciar Lote do Zero", use_container_width=True):
                        try: os.remove(checkpoint_file)
                        except: pass
                        st.success("Checkpoint removido. Você pode iniciar do zero.")
                        st.rerun()
                st.markdown("---")
        except Exception as e_cp_read:
            print(f"[CHECKPOINT UI] Erro ao ler checkpoint: {e_cp_read}")

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        submit_btn = st.button("🚀 Gerar Aula Única", type="primary", use_container_width=True)
    with col_btn2:
        submit_batch_btn = st.button("⚡ Gerar Todas as Aulas da Ementa em Lote", type="secondary", use_container_width=True)

    # Lógica ao pressionar qualquer um dos botões de geração
    if submit_btn or submit_batch_btn:
        # Define se é lote
        st.session_state.is_batch_run = bool(submit_batch_btn)
        
        if submit_batch_btn:
            if not is_custom and disciplina_selecionada in DISCIPLINAS_PRECARREGADAS:
                temas_lote = list(DISCIPLINAS_PRECARREGADAS[disciplina_selecionada]["temas"])
            elif tema_solicitado.strip():
                temas_lote = [t.strip() for t in tema_solicitado.split(";") if t.strip()]
            else:
                st.error("Para gerar em lote uma disciplina customizada, preencha os temas separados por ponto e vírgula (;).")
                return
                
            if not temas_lote:
                st.error("Nenhum tema encontrado para a geração em lote.")
                return

            st.session_state.batch_total = len(temas_lote)
            st.session_state.batch_index = 1
            st.session_state.batch_memoria = ""
            tema_solicitado = temas_lote.pop(0)
            st.session_state.batch_queue = temas_lote

        t_inicio_geral_completo = time.time()
        
        # 1. Preparação física dos arquivos na thread principal (evita concorrência e perdas de buffers do Streamlit)
        nome_professor_clean = nome_professor.lower().strip()
        codigo_disciplina_clean = codigo_disciplina.lower().strip()
        
        os.makedirs("cache", exist_ok=True)
        temp_ementa_path = os.path.join("cache", f"ementa_{nome_professor_clean}_{codigo_disciplina_clean}.pdf")
        if is_custom:
            with open(temp_ementa_path, "wb") as f:
                f.write(ementa_file.getbuffer())
        else:
            orig_pdf_path = DISCIPLINAS_PRECARREGADAS[disciplina_selecionada]["pdf_path"]
            if not os.path.exists(orig_pdf_path):
                st.error(f"Arquivo de ementa original não encontrado em {orig_pdf_path}")
                return
            shutil.copy(orig_pdf_path, temp_ementa_path)
            
        temp_materials_dir = None
        if materiais_apoio:
            temp_materials_dir = f"temp_rag_{nome_professor_clean}_{codigo_disciplina_clean}"
            os.makedirs(temp_materials_dir, exist_ok=True)
            for uploaded_file in materiais_apoio:
                file_path = os.path.join(temp_materials_dir, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())

        # 2. Processamento das Diretrizes de Notação e Cores na thread principal
        diretrizes_texto = ""
        if os.path.exists("diretrizes_padrao.md"):
            with open("diretrizes_padrao.md", "r", encoding="utf-8") as f:
                diretrizes_texto = f.read()

            funcoes_adicionais = """
### 1.5 Notações Matemáticas e Funções Gerais
| Conceito | Símbolo Obrigatório (LaTeX) | Descrição |
| :--- | :--- | :--- |
| **Função de Densidade** | $f(x)$ | Função de densidade de probabilidade. |
| **Função de Distribuição Acumulada** | $F(x)$ | Função de probabilidade acumulada. |
| **Somatório** | $\\sum$ | Operador de somatório. |
| **Produtório** | $\\prod$ | Operador de produtório. |
| **Integral** | $\\int$ | Operador de integral. |
"""
            diretrizes_texto += funcoes_adicionais

            notacoes_mapeamento = {
                "tamanho_amostral": "Tamanho Amostral",
                "tamanho_populacional": "Tamanho Populacional",
                "media_populacional": "Média Populacional",
                "media_amostral": "Média Amostral",
                "variancia_populacional": "Variância Populacional",
                "variancia_amostral": "Variância Amostral",
                "desvio_padrao_populacional": "Desvio Padrão Populacional",
                "desvio_padrao_amostral": "Desvio Padrão Amostral",
                "proporcao_populacional": "Proporção Populacional",
                "proporcao_amostral": "Proporção Amostral",
                "margem_erro": "Margem de Erro",
                "intervalo_confianca": "Intervalo de Confiança",
                "erro_padrao_media": "Erro Padrão da Média",
                
                "hipotese_nula": "Hipótese Nula",
                "hipotese_alternativa": "Hipótese Alternativa",
                "nivel_significancia": "Nível de Significância",
                "nivel_confianca": "Nível de Confiança",
                "erro_tipo_2": "Probabilidade do Erro Tipo II",
                "poder_teste": "Poder do Teste",
                "p_valor": "P-Valor",
                "regiao_rejeicao": "Região de Rejeição",
                "graus_liberdade": "Graus de Liberdade",
                "graus_liberdade_num": "Graus de Liberdade (Numerador)",
                "graus_liberdade_den": "Graus de Liberdade (Denominador)",
                "estatistica_z_calc": "Estatística Z Calculada",
                "estatistica_t_calc": "Estatística t Calculada",
                "estatistica_chi2_calc": "Estatística Qui-Quadrado Calc.",
                "estatistica_f_calc": "Estatística F Calculada",
                "valor_critico_z": "Valor Crítico Z",
                "valor_critico_t": "Valor Crítico t",
                "valor_critico_chi2": "Valor Crítico Qui-Quadrado",
                "valor_critico_f": "Valor Crítico F",
                
                "distribuicao_normal": "Distribuição Normal",
                "distribuicao_normal_padrao": "Distribuição Normal Padrão",
                "distribuicao_t": "Distribuição t de Student",
                "distribuicao_qui_quadrado": "Distribuição Qui-Quadrado",
                "distribuicao_f": "Distribuição F de Snedecor",
                "distribuicao_binomial": "Distribuição Binomial",
                "distribuicao_poisson": "Distribuição Poisson",
                
                "correlacao_populacional": "Correlação Populacional",
                "correlacao_amostral": "Correlação Amostral",
                "coeficiente_determinacao": "Coeficiente de Determinação",
                "covariancia_populacional": "Covariância Populacional",
                "covariancia_amostral": "Covariância Amostral",
                "intercepto_populacional": "Intercepto Populacional",
                "inclinacao_populacional": "Inclinação Populacional",
                "intercepto_estimado": "Intercepto Estimado",
                "inclinacao_estimado": "Inclinação Estimada",
                "residuo_amostral": "Resíduo Amostral",
                "soma_quadrados_regressao": "Soma de Quadrados da Regressão",
                "soma_quadrados_erro": "Soma de Quadrados do Erro",
                "soma_quadrados_total": "Soma de Quadrados Total",

                "funcao_densidade": "Função de Densidade",
                "funcao_acumulada": "Função de Distribuição Acumulada",
                "somatorio": "Somatório",
                "productorio": "Produtório",
                "integral": "Integral"
            }

            for key, conceito in notacoes_mapeamento.items():
                val = notacoes_interface.get(key)
                if val:
                    diretrizes_texto = substituir_simbolo(diretrizes_texto, conceito, val)

            if cor_principal != "#1E3A8A":
                diretrizes_texto = diretrizes_texto.replace('"PRIMARY_BLUE": "#1E3A8A"', f'"PRIMARY_BLUE": "{cor_principal}"')
            if cor_secundaria != "#10B981":
                diretrizes_texto = diretrizes_texto.replace('"SECONDARY_GREEN": "#10B981"', f'"SECONDARY_GREEN": "{cor_secundaria}"')
            if cor_alerta != "#F59E0B":
                diretrizes_texto = diretrizes_texto.replace('"WARNING_AMBER": "#F59E0B"', f'"WARNING_AMBER": "{cor_alerta}"')
            if cor_critica != "#991B1B":
                diretrizes_texto = diretrizes_texto.replace('"CRITICAL_RED": "#991B1B"', f'"CRITICAL_RED": "{cor_critica}"')

            if diretrizes_adicionais.strip():
                diretrizes_texto += f"\n\n## ✍️ 3. Regras de Estilo e Diretrizes Customizadas Adicionais do Professor\n{diretrizes_adicionais.strip()}\n"

            if st.session_state.custom_notations:
                custom_table = "\n### 1.6 Notações Personalizadas Adicionais do Professor\n| Conceito | Símbolo Obrigatório (LaTeX) | Descrição |\n| :--- | :--- | :--- |\n"
                for item in st.session_state.custom_notations:
                    c_conceito = item.get("conceito", "").strip()
                    c_simbolo = item.get("simbolo", "").strip()
                    if c_conceito and c_simbolo:
                        custom_table += f"| **{c_conceito}** | {c_simbolo} | Definição personalizada adicionada dinamicamente pelo professor. |\n"
                diretrizes_texto += custom_table

        # Monta parâmetros de execução para a thread em background
        params = {
            "nome_professor": nome_professor,
            "codigo_disciplina": codigo_disciplina,
            "tema_solicitado": tema_solicitado,
            "temp_ementa_path": temp_ementa_path,
            "temp_materials_dir": temp_materials_dir,
            "diretrizes_texto": diretrizes_texto,
            "nome_professor_clean": nome_professor_clean,
            "codigo_disciplina_clean": codigo_disciplina_clean,
            "cor_principal": cor_principal,
            "cor_secundaria": cor_secundaria,
            "cor_alerta": cor_alerta,
            "cor_critica": cor_critica,
            "tempo_inicio": t_inicio_geral_completo
        }

        clean_params = {k: v for k, v in params.items() if k != "params"}

        # Configurando e iniciando a Thread em background
        st.session_state.tempo_inicio = t_inicio_geral_completo
        st.session_state.sucesso_geracao = False
        st.session_state.erro_geracao = None
        st.session_state.mensagem_sucesso = ""
        st.session_state.scroll_to_top_done = False
        st.session_state.geracao_status = {
            "etapa_atual": "Iniciando...",
            "subetapa_detalhe": "Disparando agentes de inteligência artificial...",
            "subtopicos": [],
            "status_subtopicos": {},
            "tentativas_subtopicos": {},
            "max_tentativas_subtopicos": {},
            "tempo_inicio": t_inicio_geral_completo,
            "ativo": True,
            "sucesso": False,
            "erro": None,
            "mensagem_sucesso": "",
            "memoria_pedagogica": st.session_state.get("batch_memoria", "") if st.session_state.get("is_batch_run") else "",
            "params": clean_params
        }
        st.session_state.gerando_aula = True

        disparar_thread_geracao(st.session_state.geracao_status, clean_params)
        st.rerun()

if __name__ == "__main__":
    run_page()
