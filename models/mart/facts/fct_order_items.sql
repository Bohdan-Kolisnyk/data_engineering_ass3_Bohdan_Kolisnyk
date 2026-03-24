{{
    config(
        materialized='incremental',
        unique_key='order_item_id'
    )
}}

select oi.order_item_id, oi.order_id, oi.item_id,
    oi.quantity, oi.unit_price, oi.subtotal
from {{ ref('stg_order_items') }} oi

{% if is_incremental() %}
    where oi.order_id > (select max(order_id) from {{ this }})
{% endif %}