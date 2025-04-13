WITH source AS (
    SELECT
        code,
        codein,
        name,
        high,
        low,
        "varBid",
        "pctChange",
        bid,
        ask,
        timestamp,
        create_date
    FROM {{ source('dw_cotacaomoedas', 'cotacoes_moedas') }}
),

renamed AS (
    SELECT
        code AS moeda_origem,
        codein AS moeda_destino,
        name AS par_moeda,
        "varBid"::numeric AS preco_compra,
        ask::numeric AS preco_venda,
        "pctChange"::numeric AS porcent_variacao,
        high::numeric AS preco_maximo,
        low::numeric AS preco_minimo,
        CAST(create_date AS date) AS data_cotacao
    FROM source
)

SELECT * FROM renamed
