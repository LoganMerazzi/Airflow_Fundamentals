from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta

default_args = {
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG (
    dag_id = 'simple_dag_default_parameters', 
    default_args = default_args,
    schedule_interval=timedelta(days=1), 
    start_date=days_ago(3),
    catchup=False
) as dag:
    
    task_1 = DummyOperator(
        task_id='task_1'
    )
    task_2 = DummyOperator(
        task_id='task_2',
        retry=3 # Terá a prioridade sobre o parametro default
    )
    task_3 = DummyOperator(
        task_id='task_3'
    )