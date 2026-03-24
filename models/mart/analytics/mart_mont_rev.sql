select order_month, count(*) as total_orders,
    sum(total_amount) as monthly_revenue,
    sum(sum(total_amount)) over (order by order_month) as cumulative_revenue,
    sum(total_amount) - lag(sum(total_amount)) over (order by order_month) as mom_change
from {{ ref('stg_orders') }}
where order_status = 'delivered'
group by order_month
order by order_month