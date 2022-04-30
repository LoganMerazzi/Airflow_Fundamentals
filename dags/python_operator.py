from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from datetime import datetime, timedelta

default_args = {
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}

# Para buscar as informações disponíveis das DAGRuns:
#def _downloading_data(**kwargs):
#    print(kwargs)

# Para buscar uma informações específica disponíveis das DAGRuns:
#def _downloading_data(**kwargs):
#    print(kwargs[ds])

# Para buscar uma informações específica disponíveis das DAGRuns, usando o valor da variável diretamente:
# Em tempo: ds é a data de execução (execution_date)
def _downloading_data(ds):
    print(ds)


with DAG (
    dag_id = 'PythonOperator', 
    default_args = default_args,
    schedule_interval=timedelta(days=1), 
    start_date=days_ago(3),
    catchup=False
) as dag:
    
    downloading_data = PythonOperator(
        task_id = 'downloading_data',
        python_callable=_downloading_data
    )