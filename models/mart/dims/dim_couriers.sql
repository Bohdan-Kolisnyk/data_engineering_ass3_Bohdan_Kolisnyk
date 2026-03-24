select c.courier_id, c.full_name, c.vehicle_type, c.city, c.is_active,
    count(d.delivery_id) as total_deliveries,
    round(avg(d.actual_delivery_minutes), 1) as avg_delivery_minutes,
    sum(case when d.is_delayed then 1 else 0 end) as delayed_deliveries,
    rank() over (order by avg(d.actual_delivery_minutes)) as speed_rank
from {{ ref('stg_couriers') }} c
left join {{ ref('stg_deliveries') }} d on c.courier_id = d.courier_id
group by c.courier_id, c.full_name, c.vehicle_type, c.city, c.is_active