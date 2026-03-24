select order_id, total_amount
from {{ ref('fct_orders') }}
where order_status = 'delivered' and total_amount <= 0