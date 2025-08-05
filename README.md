# 📊 Desafio Técnico – Analista de Dados Jr

Este projeto foi desenvolvido como parte de um desafio técnico para a vaga de **Analista de Dados Júnior**. O objetivo é diagnosticar a alta taxa de inadimplência de uma empresa de assinaturas mensais com base em uma base fictícia de clientes.

---

> 🔗 [Clique aqui para visualizar o dashboard](https://lookerstudio.google.com/s/t4P213IoPzc)


## ✅ Etapas do Projeto

### 1. **ETL (Limpeza e Tratamento dos Dados)**
- Carregamento do arquivo `base_dados_desafio.csv`
- Remoção de duplicatas e valores ausentes
- Conversão de colunas de data
- Cálculo da idade dos clientes
- Criação de colunas derivadas:
  - `idade`
  - `faixa_etaria`
  - `faixa_valor` (categorias de valor de mensalidade)
  - `inadimplente` (variável binária)

> Resultado salvo em: `clientes_tratado.csv`

---

### 2. **Análise Exploratória (EDA)**
Foram exploradas métricas como:

- Taxa geral de inadimplência
- Inadimplência por:
  - Faixa etária
  - Estado
  - Faixa de valor da mensalidade
- Distribuição de clientes por idade
- Comparativo entre adimplentes e inadimplentes

Gráficos gerados com `matplotlib` e organizados em uma única janela (`subplots`).

> Código disponível em: `ETL+Analise Exploratoria (Arquivo Python).py`

---

### 3. **Relatório Executivo (PDF)**
Documento com linguagem acessível apresentando:

- Principais descobertas da análise
- Padrões de comportamento e alertas
- Plano estratégico sugerido para redução da inadimplência

> Arquivo: `relatorio_final.pdf`

---

### 4. **Dashboard Interativo (Looker Studio)**
Dashboard construído no Looker Studio com:

- Taxa geral de inadimplência
- Filtro por Estado
- Filtro por Faixa Etária
- Gráfico de distribuição da base
- Gráficos adicionais com métricas relevantes

> 🔗 [Clique aqui para visualizar o dashboard](https://lookerstudio.google.com/s/t4P213IoPzc)



