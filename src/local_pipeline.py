from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from data_quality import validate_transactions

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "input"
OUTPUT = ROOT / "data" / "output"

spark = (
    SparkSession.builder
    .appName("EnterpriseDataLakeLocal")
    .master("local[*]")
    .getOrCreate()
)

customers = spark.read.option("header", True).option("inferSchema", True).csv(
    str(INPUT / "customers.csv")
)
products = spark.read.option("header", True).option("inferSchema", True).csv(
    str(INPUT / "products.csv")
)
transactions = spark.read.option("header", True).option("inferSchema", True).csv(
    str(INPUT / "transactions.csv")
)

quality = validate_transactions(transactions)
print("Data quality:", quality)

if quality["status"] != "PASSED":
    raise ValueError(f"Quality checks failed: {quality}")

silver = (
    transactions
    .join(customers, "customer_id", "left")
    .join(products, "product_id", "left")
    .withColumn("order_date", F.to_date("order_date"))
    .withColumn("load_timestamp", F.current_timestamp())
    .dropDuplicates(["transaction_id"])
)

gold_fact = silver.select(
    "transaction_id", "customer_id", "product_id", "order_date",
    "quantity", "net_amount", "currency", "load_timestamp"
)

gold_customer = customers
gold_product = products

for name, df in [
    ("silver_sales", silver),
    ("fact_sales", gold_fact),
    ("dim_customer", gold_customer),
    ("dim_product", gold_product),
]:
    target = OUTPUT / name
    df.coalesce(1).write.mode("overwrite").option("header", True).csv(str(target))
    print(f"Wrote {target}")

spark.stop()
