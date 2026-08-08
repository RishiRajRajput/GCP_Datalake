from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def validate_transactions(df: DataFrame) -> dict:
    checks = {
        "row_count": df.count(),
        "null_transaction_id": df.filter(F.col("transaction_id").isNull()).count(),
        "duplicate_transaction_id": (
            df.groupBy("transaction_id").count()
              .filter(F.col("count") > 1).count()
        ),
        "negative_quantity": df.filter(F.col("quantity") < 0).count(),
        "negative_amount": df.filter(F.col("net_amount") < 0).count(),
    }

    failures = [
        k for k, v in checks.items()
        if k != "row_count" and v > 0
    ]
    checks["status"] = "FAILED" if failures else "PASSED"
    checks["failed_checks"] = failures
    return checks
