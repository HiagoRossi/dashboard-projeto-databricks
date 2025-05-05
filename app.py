import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_parquet("logs_processados.parquet")
df['data_execucao'] = pd.to_datetime(df['data_execucao'])

st.set_page_config(layout="wide")
st.title("📊 Monitoramento de Jobs no Databricks")

min_data = df['data_execucao'].min()
max_data = df['data_execucao'].max()
data_ini, data_fim = st.date_input("📅 Selecione o intervalo", [min_data, max_data])

df_filt = df[(df['data_execucao'] >= pd.to_datetime(data_ini)) & (df['data_execucao'] <= pd.to_datetime(data_fim))]

fig1 = px.bar(df_filt.groupby('job_id')['duration_minutes'].mean().reset_index(),
              x='job_id', y='duration_minutes', title='Duração Média por Job ID')
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.histogram(df_filt, x='data_execucao', color='result_state',
                    title='Execuções por Dia e Resultado', nbins=15)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("### 📌 Métricas")
st.write(f"Média de duração: {df_filt['duration_minutes'].mean():.2f} minutos")
st.write(f"Total de jobs: {len(df_filt)}")
st.write(f"Jobs com falha: {(df_filt['result_state'] != 'SUCCESS').sum()}")

if not df_filt[df_filt['result_state'] == 'FAILED'].empty:
    st.error("⚠️ Há falhas nos jobs nesse período!")
    st.dataframe(df_filt[df_filt['result_state'] == 'FAILED'][['job_id', 'run_id', 'data_execucao', 'duration_minutes']])
else:
    st.success("✅ Nenhuma falha no período selecionado.")
