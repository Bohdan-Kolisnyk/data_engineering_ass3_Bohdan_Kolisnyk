select restaurant_id,
    {{ standardize_text('name') }} as restaurant_name,
    {{ standardize_text('cuisine_type') }} as cuisine_type,
    city,
    rating,
    is_active,
    created_at
from {{ ref('raw_restaurants') }}