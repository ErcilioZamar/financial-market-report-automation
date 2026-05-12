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

## 📌 Instalação completa

```bash
git clone URL_DO_REPO
cd repo
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python main.py
```

⚠️ Observações
O uso do yfinance depende da disponibilidade do Yahoo Finance
Pode haver instabilidade em dados históricos
O envio de e-mail requer configuração de senha de app no Gmail

👨‍💻 Autor
Desenvolvido por Ercilio Zamar
Estudante de Análise e Desenvolvimento de Sistemas com foco em automação, dados e desenvolvimento Python.
