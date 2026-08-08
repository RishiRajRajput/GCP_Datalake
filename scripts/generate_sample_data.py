from pathlib import Path
import csv
import random
from datetime import date, timedelta

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "input"
OUT.mkdir(parents=True, exist_ok=True)

random.seed(42)

customers = [
    [1, "Acme Finance", "IN", "Enterprise"],
    [2, "Northwind Bank", "US", "Enterprise"],
    [3, "BlueSky Retail", "UK", "SMB"],
    [4, "Metro Services", "IN", "SMB"],
    [5, "Global Trade", "SG", "Enterprise"],
]

products = [
    [101, "Cloud Storage", "Cloud", 120.00],
    [102, "Data Platform", "Analytics", 250.00],
    [103, "Security Suite", "Security", 180.00],
    [104, "AI Analytics", "AI", 320.00],
]

start = date(2026, 1, 1)
transactions = []
for i in range(1, 51):
    customer = random.choice(customers)
    product = random.choice(products)
    order_date = start + timedelta(days=random.randint(0, 90))
    qty = random.randint(1, 10)
    transactions.append([
        i, customer[0], product[0], order_date.isoformat(), qty,
        round(qty * product[3], 2), "USD"
    ])

def save(name, header, rows):
    with open(OUT / name, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

save("customers.csv",
     ["customer_id", "customer_name", "country", "customer_type"], customers)

save("products.csv",
     ["product_id", "product_name", "category", "unit_price"], products)

save("transactions.csv",
     ["transaction_id", "customer_id", "product_id", "order_date",
      "quantity", "net_amount", "currency"], transactions)

print(f"Generated synthetic data in {OUT}")
