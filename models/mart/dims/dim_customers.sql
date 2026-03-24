with customers as (
    select * from {{ ref('stg_customers') }}
),

order_stats as (
    select customer_id, count(*) as total_orders,
        sum(total_amount) as lifetime_revenue,
        min(order_date) as first_order_date,
        max(order_date) as last_order_date
    from {{ ref('stg_orders') }}
    where order_status = 'delivered'
    group by customer_id
)

select c.customer_id, c.full_name, c.city, c.is_active,
    coalesce(os.total_orders, 0) as total_orders,
    coalesce(os.lifetime_revenue, 0) as lifetime_revenue,
    os.first_order_date, os.last_order_date,
    row_number() over (order by coalesce(os.lifetime_revenue, 0) desc) as revenue_rank
from customers c
left join order_stats os on c.customer_id = os.customer_id