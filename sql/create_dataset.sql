CREATE SCHEMA IF NOT EXISTS `gcpdatalake-504916.dev_bronze`;

CREATE TABLE IF NOT EXISTS `gcpdatalake-504916.dev_bronze.fact_sales`
(
  transaction_id INT64,
  customer_id INT64,
  product_id INT64,
  order_date DATE,
  quantity INT64,
  net_amount NUMERIC,
  currency STRING,
  load_timestamp TIMESTAMP
)
PARTITION BY order_date
CLUSTER BY customer_id, product_id;
