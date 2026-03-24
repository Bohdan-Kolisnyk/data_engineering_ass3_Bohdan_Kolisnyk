select order_id, customer_id, restaurant_id,
    order_status, order_date, date_trunc('month', order_date)::date as order_month, total_amount, 
    promo_id, updated_at
from {{ ref('raw_orders') }}