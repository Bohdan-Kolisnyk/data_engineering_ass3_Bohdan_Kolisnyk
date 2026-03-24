select delivery_id, order_id, courier_id,
    delivery_status, picked_up_at, delivered_at, estimated_delivery_minutes,
    actual_delivery_minutes,
    actual_delivery_minutes - estimated_delivery_minutes as delay_minutes,
    case when actual_delivery_minutes > estimated_delivery_minutes then true else false end as is_delayed,
    updated_at
from {{ ref('raw_deliveries') }}