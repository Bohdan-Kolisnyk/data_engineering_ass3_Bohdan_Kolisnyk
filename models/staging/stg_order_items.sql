select order_item_id, order_id, item_id, quantity, unit_price, subtotal
from {{ ref('raw_order_items') }}