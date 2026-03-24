{{
    config(
        materialized='incremental',
        unique_key='payment_id'
    )
}}

select p.payment_id, p.order_id, p.payment_method,
    p.amount, p.payment_status, p.paid_at, p.updated_at
from {{ ref('stg_payments') }} p

{% if is_incremental() %}
    where p.updated_at > (select max(updated_at) from {{ this }})
{% endif %}