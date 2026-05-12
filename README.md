# 📊 Relatório Automático de Mercado Financeiro com Python

Este projeto automatiza a coleta, análise e envio de relatórios de desempenho de ativos financeiros utilizando Python.

Ele coleta dados de mercado, gera gráficos e envia um relatório automatizado por e-mail com os resultados.

---

## 🚀 Funcionalidades

- Coleta de dados de ativos financeiros via yfinance
- Processamento de séries históricas de preços
- Cálculo de retornos diários
- Geração de gráficos automatizados
- Envio automático de relatório por e-mail com anexos

---

## 📈 Ativos analisados

- Ibovespa
- Dólar
- S&P 500
- Bitcoin

---

## 🛠️ Tecnologias utilizadas

- Python
- yfinance
- pandas
- matplotlib
- mplcyberpunk
- smtplib (envio de e-mail)

---

## 📊 Exemplo de saída

O sistema gera:
- Gráficos de performance dos ativos
- Percentual de retorno diário
- Relatório enviado automaticamente por e-mail

---

## ⚙️ Como executar

1. Instalar dependências:

```bash
pip install yfinance pandas matplotlib mplcyberpunk
```

⚠️ Observações
O uso do yfinance depende da disponibilidade do Yahoo Finance
Pode haver instabilidade em dados históricos
O envio de e-mail requer configuração de senha de app no Gmail
