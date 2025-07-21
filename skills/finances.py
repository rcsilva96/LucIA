import requests
import re

def can_handle(comando):
    padrao = re.compile(r"(cotação|valor|preço).*(dólar|dollar|usd)", re.IGNORECASE)
    return bool(padrao.search(comando))

def execute(comando):
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.get(url)
        dados = response.json()
        cotacao = float(dados['USDBRL']['bid'])
        variacao = float(dados['USDBRL']['varBid'])
        return f"A cotação atual do dólar é R$ {cotacao:.2f}. Variação de {variacao:.2f}%."
    except Exception as e:
        return "Não consegui obter a cotação agora."
