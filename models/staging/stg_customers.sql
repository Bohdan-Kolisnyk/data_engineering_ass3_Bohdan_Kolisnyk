select customer_id,
    {{ standardize_text('first_name') }} as first_name,
    {{ standardize_text('last_name') }} as last_name,
    first_name || ' ' || last_name as full_name,
    email,
    phone,
    {{ standardize_text('city') }} as city,
    registered_at,
    is_active
from {{ ref('raw_customers') }}