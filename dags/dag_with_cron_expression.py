from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "nikki",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="dag_with_cron_expression_v01",
    default_args=default_args,
    start_date=datetime(2023, 8, 1),
    schedule="0 3 * * Tue-Fri",
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo This is a simple bash command!",
    )
    task1
