{{
    config(
        materialized='incremental',
        unique_key=['restaurant_id', 'order_month'],
        incremental_predicates=[
            "DBT_INCREMENTAL_TARGET.order_month >= (select max(order_month) - interval '2 months' from " ~ this ~ ")"
        ]
    )
}}

select restaurant_id, order_month,
    count(*) as total_orders,
    sum(total_amount) as monthly_revenue,
    avg(total_amount) as avg_order_value
from {{ ref('stg_orders') }}
where order_status = 'delivered'

{% if is_incremental() %}
    and order_month >= (select max(order_month) - interval '2 months' from {{ this }})
{% endif %}

group by restaurant_id, order_month