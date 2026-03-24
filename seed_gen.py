import csv
import os
import random
from datetime import datetime, timedelta

random.seed(42)  

SEEDS_DIR = "seeds"
os.makedirs(SEEDS_DIR, exist_ok=True)


def write_csv(filename, headers, rows):
    path = os.path.join(SEEDS_DIR, filename)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"  {path} — {len(rows)} rows")


def random_datetime(start, end):
    delta = end - start
    rand_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=rand_seconds)


def fmt(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def fmt_date(dt):
    return dt.strftime("%Y-%m-%d")



FIRST_NAMES = [
    "Olena", "Dmytro", "Iryna", "Andriy", "Maryna",
    "Volodymyr", "Nataliia", "Serhii", "Oksana", "Yurii",
    "Tetiana", "Oleksandr", "Viktoriia", "Ivan", "Kateryna",
    "Pavlo", "Larysa", "Maksym", "Alina", "Roman",
    "Svitlana", "Bohdan", "Diana", "Artem", "Hanna",
]
LAST_NAMES = [
    "Kovalenko", "Shevchenko", "Bondarenko", "Melnyk", "Tkachenko",
    "Kravchenko", "Oliinyk", "Lysenko", "Moroz", "Polishchuk",
    "Savchenko", "Rudenko", "Marchenko", "Boyko", "Hrytsenko",
    "Kolomiiets", "Sydorenko", "Ponomarenko", "Vasylenko", "Cherniavskyi",
    "Zinchenko", "Tymoshenko", "Fedorenko", "Bilous", "Pryhodko",
]
CITIES = ["Kyiv", "Lviv", "Odesa", "Kharkiv", "Dnipro"]

print("Generating")

customers = []
for i in range(1, 26):
    reg_date = random_datetime(datetime(2023, 1, 1), datetime(2024, 2, 28))
    customers.append([
        i,
        FIRST_NAMES[i - 1],
        LAST_NAMES[i - 1],
        f"{FIRST_NAMES[i-1].lower()}.{LAST_NAMES[i-1][0].lower()}@gmail.com",
        f"+38050{random.randint(1000000, 9999999)}",
        random.choice(CITIES),
        fmt(reg_date),
        random.choice(["true", "true", "true", "true", "false"]),  
    ])

write_csv("customers.csv",
    ["customer_id", "first_name", "last_name", "email", "phone", "city", "registered_at", "is_active"],
    customers)



RESTAURANTS = [
    (1, "Puzata Hata", "ukrainian", "Kyiv", 4.5),
    (2, "Sushi Master", "japanese", "Kyiv", 4.2),
    (3, "Pizza Celentano", "italian", "Lviv", 4.0),
    (4, "Berliner Doner", "turkish", "Odesa", 3.8),
    (5, "Lviv Croissants", "bakery", "Lviv", 4.7),
    (6, "Tarantino Grill", "american", "Kyiv", 4.3),
    (7, "Saigon", "vietnamese", "Kharkiv", 4.1),
    (8, "Dim Sum House", "chinese", "Dnipro", 3.9),
    (9, "Kartopliana Khata", "ukrainian", "Kyiv", 4.4),
    (10, "Burger King", "american", "Odesa", 3.5),
    (11, "Bao Modern Asian", "asian", "Kyiv", 4.6),
    (12, "Napule Pizza", "italian", "Kharkiv", 4.2),
]

restaurants = []
for r_id, name, cuisine, city, rating in RESTAURANTS:
    created = random_datetime(datetime(2022, 6, 1), datetime(2023, 5, 1))
    is_active = "false" if r_id == 10 else "true"
    restaurants.append([r_id, name, cuisine, city, rating, is_active, fmt(created)])

write_csv("restaurants.csv",
    ["restaurant_id", "name", "cuisine_type", "city", "rating", "is_active", "created_at"],
    restaurants)



MENU = [
    (1, 1, "Borshch", "soup", 95), (2, 1, "Varenyky with potato", "main", 110),
    (3, 1, "Chicken Kyiv", "main", 165), (4, 2, "Philadelphia Roll", "sushi", 185),
    (5, 2, "Miso Soup", "soup", 75), (6, 2, "Salmon Sashimi", "sushi", 220),
    (7, 3, "Margherita Pizza", "pizza", 155), (8, 3, "Carbonara Pasta", "pasta", 140),
    (9, 3, "Tiramisu", "dessert", 95), (10, 4, "Doner Kebab", "main", 125),
    (11, 4, "Falafel Wrap", "main", 110), (12, 5, "Classic Croissant", "bakery", 55),
    (13, 5, "Almond Croissant", "bakery", 75), (14, 5, "Americano Coffee", "drink", 65),
    (15, 6, "BBQ Burger", "burger", 175), (16, 6, "Grilled Ribs", "main", 245),
    (17, 6, "Caesar Salad", "salad", 135), (18, 7, "Pho Bo", "soup", 145),
    (19, 7, "Spring Rolls", "appetizer", 95), (20, 7, "Pad Thai", "main", 155),
    (21, 8, "Dim Sum Set", "main", 185), (22, 8, "Kung Pao Chicken", "main", 165),
    (23, 8, "Wonton Soup", "soup", 85), (24, 9, "Deruny", "main", 95),
    (25, 9, "Holubtsi", "main", 120), (26, 9, "Salo Platter", "appetizer", 85),
    (27, 10, "Whopper", "burger", 145), (28, 10, "Chicken Nuggets", "appetizer", 95),
    (29, 11, "Bao Buns", "appetizer", 135), (30, 11, "Ramen Tonkotsu", "soup", 175),
    (31, 11, "Matcha Latte", "drink", 85), (32, 12, "Quattro Formaggi", "pizza", 180),
    (33, 12, "Pepperoni Pizza", "pizza", 165), (34, 12, "Panna Cotta", "dessert", 85),
]

menu_items = []
for item_id, rest_id, name, category, price in MENU:
    is_avail = "false" if rest_id == 10 else "true"
    menu_items.append([item_id, rest_id, name, category, f"{price:.2f}", is_avail])

write_csv("menu_items.csv",
    ["item_id", "restaurant_id", "name", "category", "price", "is_available"],
    menu_items)



COURIER_NAMES = [
    ("Taras", "Honcharenko"), ("Mykola", "Petrenko"), ("Oleg", "Ivanchuk"),
    ("Vasyl", "Karpenko"), ("Denys", "Zaitsev"), ("Kostiantyn", "Marchuk"),
    ("Yevhen", "Sokolov"), ("Ihor", "Tkach"),
]
VEHICLES = ["bicycle", "scooter", "car"]

couriers = []
for i, (fn, ln) in enumerate(COURIER_NAMES, 1):
    hired = random_datetime(datetime(2022, 6, 1), datetime(2023, 3, 1))
    is_active = "false" if i == 8 else "true"
    couriers.append([
        i, fn, ln,
        f"+38067{random.randint(1000000, 9999999)}",
        random.choice(VEHICLES),
        random.choice(CITIES),
        fmt(hired), is_active,
    ])

write_csv("couriers.csv",
    ["courier_id", "first_name", "last_name", "phone", "vehicle_type", "city", "hired_at", "is_active"],
    couriers)



promotions = [
    [1, "WELCOME10", "percentage", "10.00", "200.00", "2023-01-01", "2024-12-31", "true"],
    [2, "SUMMER20", "percentage", "20.00", "300.00", "2023-06-01", "2023-09-30", "false"],
    [3, "FLAT50", "fixed", "50.00", "250.00", "2023-04-01", "2024-06-30", "true"],
    [4, "NEWYEAR15", "percentage", "15.00", "150.00", "2023-12-20", "2024-01-31", "false"],
    [5, "FREESHIP", "fixed", "0.00", "100.00", "2023-01-01", "2024-12-31", "true"],
]

write_csv("promotions.csv",
    ["promo_id", "promo_code", "discount_type", "discount_value", "min_order_amount",
     "start_date", "end_date", "is_active"],
    promotions)


ACTIVE_RESTAURANTS = [r[0] for r in RESTAURANTS if r[0] != 10]
MENU_BY_RESTAURANT = {}
for item_id, rest_id, name, cat, price in MENU:
    if rest_id != 10:
        MENU_BY_RESTAURANT.setdefault(rest_id, []).append((item_id, price))

PROMO_IDS = [1, 2, 3]

orders = []
order_items_rows = []
order_item_id = 1

for order_id in range(1, 71):
    cust_id = random.randint(1, 25)
    rest_id = random.choice(ACTIVE_RESTAURANTS)
    order_date = random_datetime(datetime(2023, 3, 1), datetime(2024, 4, 10))

    rest_menu = MENU_BY_RESTAURANT[rest_id]
    num_items = random.choice([2, 2, 2, 3])
    chosen_items = random.sample(rest_menu, min(num_items, len(rest_menu)))

    subtotal = 0
    items_for_this_order = []
    for item_id, price in chosen_items:
        qty = random.choice([1, 1, 1, 2])
        line_total = price * qty
        subtotal += line_total
        items_for_this_order.append([order_item_id, order_id, item_id, qty, f"{price:.2f}", f"{line_total:.2f}"])
        order_item_id += 1

    if random.random() < 0.05:
        status = "cancelled"
        subtotal = 0
    else:
        status = "delivered"

    promo_id = random.choice(PROMO_IDS) if random.random() < 0.15 else ""

    updated_at = order_date + timedelta(minutes=random.randint(30, 90))

    orders.append([
        order_id, cust_id, rest_id, status,
        fmt(order_date), f"{subtotal:.2f}", promo_id, fmt(updated_at),
    ])
    order_items_rows.extend(items_for_this_order)

write_csv("orders.csv",
    ["order_id", "customer_id", "restaurant_id", "order_status", "order_date",
     "total_amount", "promo_id", "updated_at"],
    orders)

write_csv("order_items.csv",
    ["order_item_id", "order_id", "item_id", "quantity", "unit_price", "subtotal"],
    order_items_rows)



delivered_orders = [o for o in orders if o[3] == "delivered"]
active_couriers = [c[0] for c in couriers if c[7] == "true"]

deliveries = []
for did, order_row in enumerate(delivered_orders, 1):
    order_id = order_row[0]
    order_date = datetime.strptime(order_row[4], "%Y-%m-%d %H:%M:%S")
    courier_id = random.choice(active_couriers)

    estimated = random.choice([30, 35, 40, 45, 50])
    actual = estimated + random.choice([-5, -5, 0, 0, 0, 5, 5, 10])
    actual = max(15, actual)

    picked_up = order_date + timedelta(minutes=random.randint(5, 15))
    delivered_at = picked_up + timedelta(minutes=actual)

    deliveries.append([
        did, order_id, courier_id, "delivered",
        fmt(picked_up), fmt(delivered_at),
        estimated, actual, fmt(delivered_at),
    ])

write_csv("deliveries.csv",
    ["delivery_id", "order_id", "courier_id", "delivery_status",
     "picked_up_at", "delivered_at", "estimated_delivery_minutes",
     "actual_delivery_minutes", "updated_at"],
    deliveries)



payments = []
for pid, order_row in enumerate(orders, 1):
    order_id = order_row[0]
    order_date = datetime.strptime(order_row[4], "%Y-%m-%d %H:%M:%S")
    amount = float(order_row[5])
    method = random.choice(["card", "card", "card", "cash"])  

    if order_row[3] == "cancelled":
        status = "refunded"
    else:
        status = "completed"

    paid_at = order_date + timedelta(minutes=random.randint(0, 5))
    updated_at = paid_at if status == "completed" else paid_at + timedelta(minutes=10)

    payments.append([
        pid, order_id, method, f"{amount:.2f}",
        status, fmt(paid_at), fmt(updated_at),
    ])

write_csv("payments.csv",
    ["payment_id", "order_id", "payment_method", "amount",
     "payment_status", "paid_at", "updated_at"],
    payments)



reviews = []
review_id = 1
COMMENTS = [
    "Amazing food!", "Very tasty", "Good but slow delivery", "Best in the city",
    "Average experience", "Will order again", "Love this place", "Decent food",
    "Cold when arrived", "Perfect delivery time", "Great value", "Highly recommend",
    "Not bad", "Superb quality", "Portions are small",
]

for order_row in delivered_orders:
    if random.random() < 0.40:
        order_id = order_row[0]
        cust_id = order_row[1]
        rest_id = order_row[2]
        order_date = datetime.strptime(order_row[4], "%Y-%m-%d %H:%M:%S")
        review_date = order_date + timedelta(hours=random.randint(1, 48))
        rating = random.choice([3, 4, 4, 4, 5, 5, 5])

        reviews.append([
            review_id, order_id, cust_id, rest_id,
            rating, random.choice(COMMENTS), fmt(review_date),
        ])
        review_id += 1

write_csv("reviews.csv",
    ["review_id", "order_id", "customer_id", "restaurant_id",
     "rating", "comment", "created_at"],
    reviews)


print(f"Generated {len(os.listdir(SEEDS_DIR))} files in '{SEEDS_DIR}/'")
