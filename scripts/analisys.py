import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados
# O k6 exporta o tempo em segundos desde o início do teste na coluna 'timestamp'
df = pd.read_csv('results/microservice/results_round_1.csv')

# Filtrar apenas as métricas de interesse
latency = df[df['metric_name'] == 'http_req_duration']
rps = df[df['metric_name'] == 'http_reqs']

# Converter timestamp para segundos relativos (começando em 0)
latency['time_sec'] = latency['timestamp'] - latency['timestamp'].min()
rps['time_sec'] = rps['timestamp'] - rps['timestamp'].min()

# Agrupar por segundo para calcular a média de latência e soma de requisições
latency_aggr = latency.groupby('time_sec')['metric_value'].mean()
rps_aggr = rps.groupby('time_sec')['metric_value'].count()

# 2. Configurar o estilo do gráfico
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax1 = plt.subplots(figsize=(10, 6))

# Configurações do Eixo Y1: Latency
ax1.set_xlabel('Elapsed Time (seconds)', fontsize=12)
ax1.set_ylabel('Latency (ms)', color='tab:blue', fontsize=12)
ax1.plot(latency_aggr.index, latency_aggr.values, color='tab:blue', label='Average Latency', linewidth=2)
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Configurações do Eixo Y2: Throughput (RPS)
ax2 = ax1.twinx()
ax2.set_ylabel('Throughput (Requests per Second)', color='tab:red', fontsize=12)
ax2.plot(rps_aggr.index, rps_aggr.values, color='tab:red', linestyle='--', label='RPS', linewidth=2)
ax2.tick_params(axis='y', labelcolor='tab:red')

# Título e Legendas
plt.title('Performance Analysis: Matrix Multiplication API', fontsize=14, pad=20)
fig.tight_layout()

# Salvar para o artigo em alta resolução (PDF ou PNG 300 DPI)
plt.savefig('results/microservice/performance_analysis_1.pdf', format='pdf')
plt.show()