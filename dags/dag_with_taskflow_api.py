from datetime import datetime, timedelta

from airflow.decorators import dag, task

default_args = {
    "owner": "nikki",
    "retries": 5,
    "retry_delay": timedelta(minutes=5),
}


@dag(
    dag_id="dag_with_taskflow_api_v01",
    default_args=default_args,
    start_date=datetime(2023, 8, 7),
    schedule="@daily",
)
def hello_world_etl():
    @task(multiple_outputs=True)
    def get_name():
        return {
            "first_name": "Jerry",
            "last_name": "Fridman",
        }

    @task()
    def get_age():
        return 19

    @task()
    def greet(first_name, last_name, age):
        print(
            f"Hello World! My name is {first_name} {last_name} and I am {age} years old!"
        )

    name_dict = get_name()
    age = get_age()
    greet = greet(name_dict["first_name"], name_dict["last_name"], age)


greet_dag = hello_world_etl()
