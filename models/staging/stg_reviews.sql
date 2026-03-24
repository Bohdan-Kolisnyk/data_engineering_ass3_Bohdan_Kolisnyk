select review_id, order_id, customer_id, restaurant_id, rating, comment, created_at
from {{ ref('raw_reviews') }}