from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
import os


with DAG (
    "init_dag",
    description="DAG FOR (CREATE AND INSERT DATA)",
    start_date=datetime(2025,2,12,14,40),
    schedule_interval="*/5 * * * *",
    catchup=False,
    dagrun_timeout=timedelta(minutes=45),
    tags=["football"]
) as dag :
    create_table_task = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres",  # Connection ID configured in Airflow
        sql= "./sql/create_table.sql"
    )

    insert_data_task = PostgresOperator(
        task_id="insert_data",
        postgres_conn_id="postgres",
        sql="./sql/insert_data.sql"
    )

    create_table_task >> insert_data_task
