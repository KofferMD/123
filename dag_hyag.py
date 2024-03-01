from datetime import datetime

from airflow.decorators import task, dag
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.providers.ssh.hooks.ssh import SSHHook


@dag(
    dag_id='nsi_ssh_dag',
    start_date=datetime(2024, 2, 29),
    schedule_interval='@daily',
    catchup=False
)
def ssh_dag():
    ...
    