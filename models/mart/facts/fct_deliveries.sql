{{
    config(
        materialized='incremental',
        unique_key='delivery_id'
    )
}}

select d.delivery_id, d.order_id, d.courier_id, d.delivery_status,
    d.picked_up_at, d.delivered_at, d.estimated_delivery_minutes,
    d.actual_delivery_minutes, d.delay_minutes, d.is_delayed, d.updated_at
from {{ ref('stg_deliveries') }} d

{% if is_incremental() %}
    where d.updated_at > (select max(updated_at) from {{ this }})
{% endif %}