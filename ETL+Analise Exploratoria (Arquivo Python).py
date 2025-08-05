#Olá! Vou comentar o código que elaborei para o ETL dos dados:
#Importando bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

#Carregar o CSV
df = pd.read_csv("base_dados_desafio.csv")

#Visualizar as primeiras linhas
print(df.head())

#Verificar os tipos de dados e valores nulos
print(df.info())
print(df.isnull().sum())

#Remover duplicatas
df = df.drop_duplicates()

#Exibir quantidade de dados ausentes por coluna
print(df.isnull().sum())

#Remover linhas com qualquer dado ausente
df = df.dropna()

#Converter colunas de data
df['data_nascimento'] = pd.to_datetime(df['data_nascimento'], errors='coerce')
df['data_inicio'] = pd.to_datetime(df['data_inicio'], errors='coerce')

#Conferir novamente os tipos
print(df.dtypes)

#Calcular idade em 2025
df['idade'] = 2025 - df['data_nascimento'].dt.year

#Categorizar idade
df['faixa_etaria'] = pd.cut(df['idade'],
                            bins=[0, 18, 30, 45, 60, 100],
                            labels=['0-18', '19-30', '31-45', '46-60', '60+'])

#Remover espaços e converter para minúsculo
df['email'] = df['email'].str.strip().str.lower()

#Converter para valor binário
df['inadimplente'] = df['status'].apply(lambda x: 1 if x.strip().lower() == 'inadimplente' else 0)

#Garantir que os valores estão numéricos
df['valor_mensal'] = pd.to_numeric(df['valor_mensal'], errors='coerce')

#Criar faixa_valor (para categorizar mensalidade)
df['faixa_valor'] = pd.cut(df['valor_mensal'],
                           bins=[0, 80, 120, 160, 200],
                           labels=['0-80', '81-120', '121-160', '161-200'])

#Salvar o CSV tratado com todas as transformações aplicadas
df.to_csv("clientes_tratado.csv", index=False)

#Agora vamos para a ETAPA 2: "Analise Exploratoria"
#Vou usar a base tratada para extrair as principais métricas e exibir dados que vão servir como base para a elaboração da visão no Looker Studio

#Carregando a base tratada
df_tratado = pd.read_csv("clientes_tratado.csv") 
df_tratado.describe()

#Quantidade de inadimplentes
inadimplencia_geral = df_tratado['inadimplente'].mean() * 100
print(f"Taxa geral de inadimplência: {inadimplencia_geral:.2f}%")

#Por faixa etária
df_tratado.groupby("faixa_etaria")["inadimplente"].mean() * 100

#Por Estado
df_tratado.groupby("estado")["inadimplente"].mean().sort_values(ascending=False) * 100

#Por mensalidade (faixa_valor já foi criada na etapa anterior)

df_tratado.groupby("faixa_valor")["inadimplente"].mean() * 100

df_tratado['idade'].hist(bins=20)
plt.title('Distribuição das Idades')
plt.xlabel('Idade')
plt.ylabel('Quantidade de Clientes')

df_tratado['inadimplente'].value_counts(normalize=True) * 100
 
#Cálculos para os gráficos
inadimplencia_faixa_etaria = df_tratado.groupby("faixa_etaria")["inadimplente"].mean() * 100
inadimplencia_estado = df_tratado.groupby("estado")["inadimplente"].mean().sort_values(ascending=False) * 100
inadimplencia_valor = df_tratado.groupby("faixa_valor")["inadimplente"].mean() * 100
distribuicao_inadimplentes = df_tratado['inadimplente'].value_counts()

#Usar estilo ggplot do matplotlib (estilo padrão para organizar os gráficos)
plt.style.use('ggplot')
plt.rcParams.update({'axes.titlesize': 14, 'axes.titleweight': 'bold', 'axes.labelsize': 12})

#Criar figura e eixos para subplots (layout da página dos gráficos; subplosts="janela única com vários gráficos")
fig, axs = plt.subplots(3, 2, figsize=(16, 16))
fig.suptitle('Análise Exploratória - Gráficos Consolidados', fontsize=18, weight='bold')

#Agora vamos definir e organizar os principais gráficos
#1. Histograma das idades
axs[0, 0].hist(df_tratado['idade'], bins=20, color='#6495ED', edgecolor='black')
axs[0, 0].set_title('Distribuição das Idades', loc='center')
axs[0, 0].set_xlabel('Idade')
axs[0, 0].set_ylabel('Quantidade de Clientes')

#2. Pizza inadimplentes x adimplentes
colors = ['#1f77b4', '#ff7f0e']
labels = ['Adimplente', 'Inadimplente']
axs[0, 1].pie(distribuicao_inadimplentes, labels=labels, autopct='%.1f%%', startangle=90, colors=colors,
              textprops={'fontsize': 12})
axs[0, 1].set_title('Distribuição de Clientes', loc='center')

#3. Barra inadimplência por faixa etária
inadimplencia_faixa_etaria.plot(kind='bar', color='#ff6f61', edgecolor='black', ax=axs[1, 0])
axs[1, 0].set_title('Inadimplência por Faixa Etária (%)', loc='center')
axs[1, 0].set_xlabel('Faixa Etária')
axs[1, 0].set_ylabel('Inadimplência (%)')
axs[1, 0].set_ylim(0, 100)
axs[1, 0].grid(axis='y', linestyle='--', alpha=0.7)

#4. Barra inadimplência por estado
inadimplencia_estado.plot(kind='bar', color='#2ca02c', edgecolor='black', ax=axs[1, 1])
axs[1, 1].set_title('Inadimplência por Estado (%)', loc='center')
axs[1, 1].set_xlabel('Estado')
axs[1, 1].set_ylabel('Inadimplência (%)')
axs[1, 1].set_ylim(0, 100)
axs[1, 1].grid(axis='y', linestyle='--', alpha=0.7)

#5. Barra inadimplência por faixa valor mensalidade
inadimplencia_valor.plot(kind='bar', color='#ffa500', edgecolor='black', ax=axs[2, 0])
axs[2, 0].set_title('Inadimplência por Faixa Valor Mensalidade (%)', loc='center')
axs[2, 0].set_xlabel('Faixa de Valor (R$)')
axs[2, 0].set_ylabel('Inadimplência (%)')
axs[2, 0].set_ylim(0, 100)
axs[2, 0].grid(axis='y', linestyle='--', alpha=0.7)

#Espaço vazio (3ª linha, 2ª coluna)
axs[2, 1].axis('off')

#6 gráficos organizados em subplots
plt.tight_layout(rect=[0, 0, 1, 0.96])

#Mostra os gráficos ao final
plt.show()