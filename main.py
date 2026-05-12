import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import mplcyberpunk
import os
import smtplib
from email.message import EmailMessage

# ticker = ["substitua_pelos_tickers_da_bolsa_e_separe_com_virgula"]
# dados_mercados = yf.download(tickers, period = 6mo, auto_adjust = False
# display(dados_mercado)

# Após ver a tabelona, separa por adj close para visualizar melhor a coluna
dados_mercado = dados_mercado["Adj Close"]
display(dados_mercado)

# Tirar o NaN da tabela
dados_mercado = dados_mercado.dropna()

# Renomear as colunas no lugar dos tickers, para melhor leitura
# dados_mercado.columns = ["Nome certo", "Separados por vírgula", "entre colchetes"]
display(dados_mercado) # Para ver a tabela com os nomes certos das cotações

plt.style.use("cyberpunk") # Para chamar a biblioteca do gráfico
plt.plot(dados_mercado["IBOV"]) # Faz o gráfico da [coluna]
plt.title(IBOVESPA) # Dá nome ao gráfico
plt.savefig("ibovespa.png") # Para salvar o gráfico
# Para criar e salvar os gráficos de cada ticker (dolar, bovespa, escambau) use as 3 últimas linhas de código
# Substituindo o nome do ticker pelo qual você quer fazer o gráfico

# Calcular retornos diários geral
retornos_diarios = dados_mercado.pct_change()
display(retornos_diarios)

# Calcular retornos diários especificamente
retorno_dolar = retornos_diarios["DOLAR"].iloc[-1] # para pegar sempre a última linha da "tabela", independente da quantidade de linhas
retorno_ibov = retornos_diarios["IBOV"].iloc[-1]
retorno_sp500 = retornos_diarios["S&P500"].iloc[-1]
retorno_btc = retornos_diarios["BTC"].iloc[-1]

retorno_dolar = str(round(retorno_dolar * 100, 2)) + "%" # Para transformar o resultado em porcentagem
retorno_ibov = str(round(retorno_ibov * 100, 2)) + "%"
retorno_sp500 = str(round(retorno_sp500 * 100, 2)) + "%"
retorno_btc = str(round(retorno_btc * 100, 2)) + "%


# Configurando o script para integrar ao GMAIL para enviar o email
email = "seu_email"
with open('senha.txt') as f: # Salva a senha na mesma raiz do script
    senha = f.readlines()
    f.close()

senha_do_email = senha[0]

msg = EmailMessage()
msg['Subject'] = "Relatório de Mercado"
msg['From'] = 'seu_email'
msg['To'] = "email de quem vai receber"
msg.set_content (f"""\
                 
        Prezado diretor, segue o relatório de mercado:

* O Ibovespa teve o retorno de {retorno_ibov}.
* O Dólar teve o retorno de {retorno_dolar}.
* O S&P500 teve o retorno de {retorno_sp500}.
* O BTC teve o retorno de {retorno_btc}.

Segue em anexo a performance dos ativos nos últimos 6 meses


At.te,

Ercilio Zamar
Junior Python Developer
                 """)

# Anexar os arquivos plotados

with open('dolar.png', 'rb') as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype='image', subtype='png', filename='dolar.png')

with open('ibovespa.png', 'rb') as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype='image', subtype='png', filename='ibovespa.png')

with open('sp500.png', 'rb') as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype='image', subtype='png', filename='sp500.png')

with open('btc.png', 'rb') as content_file:
    content = content_file.read()
    msg.add_attachment(content, maintype='image', subtype='png', filename='btc.png')

# Enviar email

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, senha_do_email)
    smtp.send_message(msg)
