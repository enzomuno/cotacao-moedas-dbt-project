WITH source AS (
    SELECT * FROM {{ ref('stg_cotacoes') }}
),

agregado AS (
    SELECT
        data_cotacao,
        moeda_origem,
        moeda_destino,
        AVG(preco_compra) AS media_preco_compra,
        AVG(preco_venda) AS media_preco_venda,
        MAX(preco_maximo) AS preco_maximo_dia,
        MIN(preco_minimo) AS preco_minimo_dia,
        AVG(porcent_variacao) AS variacao_media
    FROM source
    GROUP BY 1, 2, 3
)

SELECT * FROM agregado
