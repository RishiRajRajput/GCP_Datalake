from google.cloud import storage, bigquery

def upload_to_gcs(local_file: str, bucket_name: str, blob_name: str) -> None:
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    bucket.blob(blob_name).upload_from_filename(local_file)

def load_csv_to_bigquery(
    uri: str,
    project_id: str,
    dataset_id: str,
    table_id: str,
) -> None:
    client = bigquery.Client(project=project_id)
    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
    )

    job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
    job.result()
    print(f"Loaded {uri} into {table_ref}")
