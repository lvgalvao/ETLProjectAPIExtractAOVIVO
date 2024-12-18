import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import time

# 1) st.title - Título principal
st.title("🚀 Quick Starter Streamlit - Jornada de dados")

# 2) st.header - Seção
st.header("1. Contexto de Data Engineering")

# 3) st.write - Texto simples
st.write(
    """
    Esse dashboard simula alguns elementos que você usaria em um projeto de Engenharia de Dados:
    - Coleta/Extração de dados
    - Transformação e limpeza
    - Visualização de métricas
    - Monitoramento de pipelines
    """
)

# 4) st.markdown - Texto em formato Markdown
st.markdown("""
### Tópicos Abordados:
- **Criação de widgets** para coleta de parâmetros
- **Exibição de DataFrames** (parte de "Transform")
- **Gráficos** para monitorar performance e throughput
- **Métricas** representando KPIs de pipelines ETL
""")

st.header("2. Parâmetros para Pipelines")

# 5) st.text_input - Parâmetro textual
nome_pipeline = st.text_input("Nome da Pipeline de Dados", value="Pipeline_Ingestao_Bitcoin")

# 6) st.number_input - Parâmetro numérico
batch_size = st.number_input("Batch size (linhas por ingestão):", min_value=100, max_value=100000, value=1000, step=100)

# 7) st.slider - Seletor contínuo
latencia_maxima = st.slider("Latência Máxima Aceitável (segundos):", min_value=1, max_value=30, value=5)

# 8) st.selectbox - Escolha de um pipeline
tipo_pipeline = st.selectbox("Tipo de Pipeline:", ["Batch", "Streaming", "Lambda", "Kappa"])

# 9) st.multiselect - Escolha múltipla de camadas de processamento
camadas = st.multiselect(
    "Quais camadas envolvidas no pipeline?",
    ["Raw", "Staging", "Trusted", "Analytics", "Sandbox", "Dimensão", "Fato"],
    default=["Raw", "Staging"]
)

# 10) st.checkbox - Check para simular ativação de logs
ativar_logs = st.checkbox("Ativar Logs de Execução")

st.header("3. Exibição de Dados (Transform)")

# 11) Criar um dataset fictício sobre "execuções" de pipeline
dados_execucoes = {
    "data_execucao": pd.date_range(end=datetime.now(), periods=5, freq="H"),
    "status": ["Sucesso", "Sucesso", "Falha", "Sucesso", "Sucesso"],
    "linhas_processadas": [1000, 1200, 900, 1500, 1300],
    "tempo_execucao_seg": [4.2, 5.1, 7.8, 3.9, 4.5]
}
df_execucoes = pd.DataFrame(dados_execucoes)

# 12) st.dataframe - Tabela interativa
st.subheader("Executões Recentes da Pipeline")
st.dataframe(df_execucoes)

# 13) st.table - Tabela estática
st.subheader("Tabela Estática - Últimas Execuções")
st.table(df_execucoes)

# 14) st.metric - Exibir métricas de KPIs
st.subheader("Indicadores de Performance (KPIs)")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Linhas Processadas", f"{df_execucoes['linhas_processadas'].sum():,}")
col2.metric("Execuções com Sucesso", str(df_execucoes['status'].value_counts().get("Sucesso", 0)))
col3.metric("Execuções com Falha", str(df_execucoes['status'].value_counts().get("Falha", 0)))

st.header("4. Visualização de Gráficos (Monitor)")

# 15) st.line_chart - Gráfico de linha com métricas
st.subheader("Linhas Processadas por Execução (Line Chart)")
df_execucoes_ordenado = df_execucoes.sort_values(by="data_execucao")
st.line_chart(data=df_execucoes_ordenado, x="data_execucao", y="linhas_processadas")

# 16) st.bar_chart - Gráfico de barras
st.subheader("Tempo de Execução por Data (Bar Chart)")
st.bar_chart(data=df_execucoes_ordenado, x="data_execucao", y="tempo_execucao_seg")

st.header("5. Outros Recursos Úteis")

# 17) st.date_input - Seletor de data
data_planejada = st.date_input("Data de início para nova pipeline", datetime.now())

# 18) st.progress - Barra de progresso (simulação)
st.write("Carregando dados de log...")
progress_bar = st.progress(0)
for i in range(101):
    time.sleep(0.01)
    progress_bar.progress(i)

# 19) Mensagens de sucesso/erro
if ativar_logs:
    st.success("Logs de execução estão ativos.")
else:
    st.warning("Logs de execução estão desativados.")

# 20) st.button - Botão para simular disparo de pipeline
if st.button("Disparar Nova Execução"):
    st.info(f"Pipeline '{nome_pipeline}' disparada em modo {tipo_pipeline}.")
    st.write(f"Batch size configurado para {batch_size} linhas. Latência Máxima: {latencia_maxima}s")
    st.write(f"Camadas selecionadas: {', '.join(camadas)}")

st.markdown("___")
st.caption("Quick Starter de Streamlit aplicado à Engenharia de Dados. © 2024")

