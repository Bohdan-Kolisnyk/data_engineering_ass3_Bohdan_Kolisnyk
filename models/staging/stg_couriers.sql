select courier_id,
    {{ standardize_text('first_name') }} as first_name,
    {{ standardize_text('last_name') }} as last_name,
    first_name || ' ' || last_name as full_name,
    phone, vehicle_type,
    {{ standardize_text('city') }} as city,
    hired_at, is_active
from {{ ref('raw_couriers') }}