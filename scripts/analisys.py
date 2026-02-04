import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados
file_path = 'results/microservice/results_round_1 (1).csv'
df = pd.read_csv(file_path)

# --- MELHORIA: Filtragem de Sucesso ---
# Filtramos apenas onde o status é 200 (OK) e a métrica é de uma requisição HTTP
# Usamos .copy() para evitar o SettingWithCopyWarning do Pandas
df_success = df[(df['status'] >= 200) & (df['status'] < 300)].copy()

# 2. Filtrar métricas de interesse a partir apenas dos sucessos
latency = df_success[df_success['metric_name'] == 'http_req_duration'].copy()
rps = df_success[df_success['metric_name'] == 'http_reqs'].copy()

# 3. Converter timestamp para segundos relativos
# Garantimos que o cálculo use o início do teste global, não apenas o primeiro sucesso
start_time = df['timestamp'].min()
latency['time_sec'] = (latency['timestamp'] - start_time).astype(int)
rps['time_sec'] = (rps['timestamp'] - start_time).astype(int)

# 4. Agrupar por segundo
latency_aggr = latency.groupby('time_sec')['metric_value'].mean()
rps_aggr = rps.groupby('time_sec')['metric_value'].count()

# 5. Configurar o estilo do gráfico
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax1 = plt.subplots(figsize=(12, 6))

# Eixo Y1: Latência (Média)
ax1.set_xlabel('Tempo Decorrido (segundos)', fontsize=12)
ax1.set_ylabel('Latência Média (ms)', color='tab:blue', fontsize=12)
ax1.plot(latency_aggr.index, latency_aggr.values, color='tab:blue', label='Latência (Sucesso)', linewidth=2)
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Eixo Y2: Throughput (RPS)
ax2 = ax1.twinx()
ax2.set_ylabel('Requisições por Segundo (Sucesso)', color='tab:red', fontsize=12)
ax2.plot(rps_aggr.index, rps_aggr.values, color='tab:red', linestyle='--', label='RPS (Sucesso)', linewidth=2)
ax2.tick_params(axis='y', labelcolor='tab:red')

# Título e Ajustes Finais
plt.title('Análise de Performance: Apenas Requisições Bem-sucedidas (HTTP 2xx)', fontsize=14, pad=20)
fig.tight_layout()

# 6. Salvar e Mostrar
plt.savefig('results/microservice/performance_analysis_success_only.pdf (1)', format='pdf')
plt.show()