# 📊 databricks-job-monitoring

Projeto de dashboard interativo para **monitoramento de performance de jobs no Databricks**, com foco na identificação de falhas e análise de duração das execuções. Desenvolvido com Python e Streamlit.

---

## 🚀 Objetivo

Coletar, processar e visualizar logs de execução de jobs do Databricks, com o intuito de:

- Analisar a performance (tempo de execução)
- Detectar falhas automaticamente
- Facilitar a tomada de decisões e identificação de gargalos

---

## 🛠 Tecnologias Utilizadas

- **Python** → Linguagem principal do projeto
- **Streamlit** → Interface do dashboard
- **Pandas** → Manipulação de dados
- **Plotly** → Gráficos interativos
- **PyArrow** → Leitura/escrita de arquivos `.parquet`

---

## 📂 Estrutura do Projeto



---

## 📈 Funcionalidades

- Filtro de data para visualização dos logs por período
- Gráfico de **duração média por `job_id`**
- Gráfico de **execuções por dia**, segmentadas por status (`SUCCESS`, `FAILED`)
- Métricas gerais:
  - Média de duração
  - Total de execuções
  - Quantidade de falhas
- **Sistema de alerta automático** se houver falhas nos jobs

---

## ⚠️ Sistema de Alerta

O dashboard analisa o campo `result_state` dos logs.  
Se houver qualquer execução com o valor `"FAILED"` dentro do período selecionado, um alerta visual é exibido:






Isso permite a identificação rápida de execuções que falharam e precisam ser reprocessadas ou analisadas.

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/databricks-job-monitoring.git
cd databricks-job-monitoring

