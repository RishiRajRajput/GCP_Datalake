from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def generate_data():
    import subprocess
    subprocess.run(
        ["python", "/opt/airflow/project/scripts/generate_sample_data.py"],
        check=True,
    )

def run_spark_pipeline():
    import subprocess
    subprocess.run(
        ["python", "/opt/airflow/project/src/local_pipeline.py"],
        check=True,
    )
    
def load_spark_pipeline():
    import subprocess
    subprocess.run(
        ["python", "/opt/airflow/project/src/gcp_pipeline.py"],
        check=True,
    )

with DAG(
    dag_id="enterprise_gcp_data_lake",
    start_date=datetime(2026, 1, 1),
    schedule="0 2 * * *",
    catchup=False,
    default_args={
        "owner": "data-engineering",
        "retries": 2,
        "retry_delay": timedelta(minutes=10),
    },
    tags=["gcp", "bigquery", "pyspark", "etl"],
) as dag:

    '''generate = PythonOperator(
        task_id="generate_source_data",
        python_callable=generate_data,
    )'''

    transform = PythonOperator(
        task_id="pyspark_transform_and_quality",
        python_callable=run_spark_pipeline,
    )

    #generate >> transform
    transform >> load_spark_pipeline
