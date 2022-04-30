from airflow import DAG
from datetime import datetime

from airflow.operators.dummy import DummyOperator

with DAG (dag_id = 'simple_dag_02', start_date=datetime(2022,4,29)) as dag:
    
    task_1 = DummyOperator(
        task_id='task_1'
    )
