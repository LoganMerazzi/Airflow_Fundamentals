from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.models.baseoperator import chain, cross_downstream

from datetime import datetime, timedelta

default_args = {
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}

def _downloading_data(ti, **kwargs):
  with open('/d/tmp/teste.txt','w') as f:
      f.write('my_data')
  ti.xcom_push(key="chave_personalizada", value="Novo valor")

def _check_data(ti):
    my_xcom = ti.xcom_pull(key='chave_personalizada', task_ids=['downloading_data'])
    print(my_xcom)
    
with DAG (
    dag_id = 'Xcoms', 
    default_args = default_args,
    schedule_interval=timedelta(days=1), 
    start_date=days_ago(3),
    catchup=False
) as dag: 
    
    downloading_data = PythonOperator(
        task_id = 'downloading_data',
        python_callable=_downloading_data
    )

    check_data = PythonOperator(
        task_id = 'check_data',
        python_callable=_check_data
    )

    waiting_for_data = FileSensor(
        task_id = 'waiting_for_data',
        fs_conn_id = 'fs_default', # fs_default é conexão que deve ser realizada para o sensor monitorar o local e identificar a ação. Deve ser criado na UI.
        filepath='teste.txt'#,
        #poke_interval=15
    )

    processing_data = BashOperator(
        task_id = 'processing_data',
        bash_command = 'exit 0'
    )

    chain(downloading_data, check_data, waiting_for_data , processing_data)