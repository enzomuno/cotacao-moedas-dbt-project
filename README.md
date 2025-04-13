# 💰 cotacao-moedas-dbt-project

Este projeto coleta diariamente as cotações de USD-BRL, EUR-BRL e BTC-BRL usando a AwesomeAPI, armazena em um banco de dados PostgreSQL (Neon) e transforma os dados com DBT.

## 🔧 Tecnologias

- Python
- DBT (Data Build Tool)
- PostgreSQL (Neon)
- GitHub Actions
- AwesomeAPI

## 📦 Funcionalidades

- Coleta automática de cotações via API
- Armazenamento no banco PostgreSQL
- Transformações SQL com DBT
- Automação com GitHub Actions

## ▶️ Como usar

1. Configure as variáveis de ambiente no `.env` ou nos GitHub Secrets:
   - `API_TOKEN`, `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`, `DB_PORT`, `DB_SSLMODE`

2. Execute o script de ETL:
```bash
cd src
python extract_load.py
```

3. Execute os modelos DBT:
```bash
cd dbt_cotacoes_moedas
dbt run
```

## ⏱️ Automação

- O script roda diariamente via GitHub Actions às 20h.
- Os modelos DBT também rodam automaticamente após a carga.