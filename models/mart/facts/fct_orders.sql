{{
    config(
        materialized='incremental',
        unique_key='order_id'
    )
}}

select o.order_id, o.customer_id, o.restaurant_id,
    o.order_status, o.order_date, o.order_month,
    o.total_amount, o.promo_id, o.updated_at
from {{ ref('stg_orders') }} o

{% if is_incremental() %}
    where o.updated_at > (select max(updated_at) from {{ this }})
{% endif %}