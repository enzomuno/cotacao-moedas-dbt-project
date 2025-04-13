import requests
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Carregar as variáveis do .env
load_dotenv()

# ===== VARIÁVEIS DE CONEXÃO AO BANCO =====
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST', '5432')
DB_PORT = os.getenv('DB_PORT')
DB_SSLMODE = os.getenv('DB_SSLMODE')
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode={DB_SSLMODE}"

# ===== VARIÁVEIS DE CONEXÃO DA API =====
API_TOKEN = os.getenv('API_TOKEN').strip()
url_base = "https://economia.awesomeapi.com.br/json/"
moedas_consultar_cotacao = 'USD-BRL,EUR-BRL,BTC-BRL'

# ===== FUNÇÃO DE CONSULTA À API =====
def endpoint_cotacao(moedas_cotacao):
    headers = {'x-api-key': API_TOKEN}  # Corrigido: hífen no nome do header
    url_endpoint = f"{url_base}last/{moedas_cotacao}"
    response = requests.get(url=url_endpoint, headers=headers)
    return response.json()

# ===== FUNÇÃO PARA INSERIR NO BANCO =====
def ingetar_dados_db(data_json):
    df = pd.DataFrame(data_json).T  # Transpor para formatar linhas por moeda
    engine = create_engine(DB_URL)
    df.to_sql('cotacoes_moedas', engine, if_exists='append', index=False)

if __name__ == "__main__":
    dados = endpoint_cotacao(moedas_cotacao=moedas_consultar_cotacao)
    ingetar_dados_db(data_json=dados)
