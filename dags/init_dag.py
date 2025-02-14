from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.models import Variable
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import requests
import logging

# Constants
TRELLO_API_URL = "https://api.trello.com/1"
CREATE_CARD_URL = f"{TRELLO_API_URL}/cards"


# Retrieve Trello credentials from Airflow Variables
TRELLO_API_KEY = Variable.get("TRELLO_API_KEY")
TRELLO_TOKEN = Variable.get("TRELLO_TOKEN")
BOARD_ID = Variable.get("BOARD_ID")
LIST_ID = Variable.get("LIST_ID")


def create_trello_card(card_name: str, card_desc: str) -> None:
    headers = {"Accept": "application/json"}
    query = {
        "key": TRELLO_API_KEY,
        "token": TRELLO_TOKEN,
        "idList": LIST_ID,
        "name": card_name,
        "desc": card_desc,
    }

    response = requests.post(CREATE_CARD_URL, headers=headers, params=query)
    if response.status_code == 200:
        logging.info(f"Card '{card_name}' created successfully!")
    else:
        logging.error(f"Failed to create card: {response.text}")


def on_failure_callback(context):
    task_instance = context["task_instance"]
    task_id = task_instance.task_id
    exception = context["exception"]
    card_name = f"Failed Task: {task_id}"
    card_desc = f"Task {task_id} failed with exception: {exception}"
    create_trello_card(card_name, card_desc)


default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),  
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "on_failure_callback": on_failure_callback,  
}

with DAG(
    "init_dag",
    description="DAG for creating a table and inserting data into PostgreSQL, with Trello integration",
    default_args=default_args,
    schedule_interval="*/5 * * * *",  
    catchup=False,
    dagrun_timeout=timedelta(minutes=45),
    tags=["football"],
) as dag:
    
    create_table_task = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres",
        sql="./sql/create_table.sql",  
    )

    insert_data_task = PostgresOperator(
        task_id="insert_data",
        postgres_conn_id="postgres",
        sql="./sql/insert_data.sql",  
    )

    create_table_task >> insert_data_task