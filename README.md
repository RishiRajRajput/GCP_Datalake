# gcp_datalake
Enterprise Data Lake &amp; Data Warehouse on Google Cloud | PySpark + BigQuery + Airflow

# Enterprise Data Lake & Data Warehouse on Google Cloud

A portfolio-ready enterprise data engineering project demonstrating a Bronze/Silver/Gold
architecture using Python, PySpark, Google Cloud Storage, Dataproc, BigQuery and Airflow.

## Business scenario

A financial organization receives customer, product and transaction data from multiple
enterprise systems. The platform must ingest raw data, validate and transform it, and
publish analytics-ready datasets to BigQuery.

## Architecture

```text
SAP / Oracle / SQL Server / CSV
              |
              v
      Google Cloud Storage
          Bronze / RAW
              |
              v
        Apache Airflow
              |
              v
       Dataproc / PySpark
              |
              v
      GCS Silver / CURATED
              |
              v
          BigQuery
          Gold Layer
              |
              v
       BI / Analytics
```

See `architecture/architecture.mmd` for a Mermaid diagram.

## Pipeline

1. Generate or receive source files.
2. Land raw files in GCS Bronze.
3. Run PySpark transformations.
4. Apply data quality checks.
5. Write curated data to GCS Silver.
6. Load Gold tables into BigQuery.
7. Schedule the pipeline with Airflow.

## Gold model

- `dim_customer`
- `dim_product`
- `dim_date`
- `fact_sales`

## Scheduling

Airflow DAG: `dags/enterprise_data_lake_dag.py`

Default schedule: **02:00 UTC every day**

## Local demo

```bash
python scripts/generate_sample_data.py
python scripts/local_pipeline.py
```

The local pipeline writes the Bronze/Silver/Gold output under `data/output/`.

## GCP deployment

Install dependencies:

```bash
pip install -r requirements.txt
```

Set:

```bash
export GCP_PROJECT_ID="your-project"
export GCS_BUCKET="your-bucket"
export BQ_DATASET="enterprise_analytics"
```

Then adapt `src/gcp_pipeline.py` to your GCP environment and service account.

## Important

This repository contains synthetic data only. Do not upload IBM, SAP, customer,
financial, healthcare, or other confidential enterprise data.

