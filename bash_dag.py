from datetime import datetime

from airflow.decorators import task, dag
from airflow import DAG
from airflow.operators.bash import BashOperator

@dag(
    start_date=datetime(2024, 2, 29),
    schedule_interval='@daily',
    catchup=False
)
def docker_bash_dag():
    name_of_image = 'python_hello'
    name_of_container = 'test_name'
    
    command = f'docker run --name {name_of_container} {name_of_image}'
    command1 = f'docker logs {name_of_container}'
    command2 = f'docker rm {name_of_container}'
    task1 = BashOperator(
        task_id='docker_with_bash',
        bash_command=command
    )
    task2 = BashOperator(
        task_id='read_logs',
        bash_command=command1
    )
    task3 = BashOperator(
        task_id='delete_container',
        bash_command=command2
    )

    task1 >> task2 >> task3

dag = docker_bash_dag()