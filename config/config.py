import os

PROJECT_ID = os.getenv("GCP_PROJECT_ID", "gcpdatalake-504916")
GCS_BUCKET = os.getenv("GCS_BUCKET", "gcp_datalake_csv")
BQ_DATASET = os.getenv("BQ_DATASET", "dev_bronze")

BRONZE_PREFIX = "bronze"
SILVER_PREFIX = "silver"
GOLD_PREFIX = "gold"
