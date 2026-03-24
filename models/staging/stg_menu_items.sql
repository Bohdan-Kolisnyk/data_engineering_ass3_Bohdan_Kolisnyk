select item_id,
    restaurant_id,
    {{ standardize_text('name') }} as item_name,
    category,
    price,
    is_available
from {{ ref('raw_menu_items') }}