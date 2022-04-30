## Como chamar uma função em python:

    def _funcao_criada():
        print('saída da função')

    ... definição da DAG

    task_1 = PythonOperator(
        task_id = 'task_1',
        python_callable=_funcao_criada
    )

Para obter as informações das execuções (do contexto)

    def _funcao_criada(**kwargs):
        print(kwargs)

Para buscar uma informações específica disponíveis das DAGRuns:

def _downloading_data(**kwargs):
        print(kwargs[ds])

Para buscar uma informações específica disponíveis das DAGRuns, usando o valor da variável diretamente:
Em tempo: ds é a data de execução (execution_date)

    def _downloading_data(ds):
        print(ds)

Para adicionar os seus próprios parâmetros:

    def _downloading_data(my_param, ds):
        print(my_param)
        print(ds)

    task_1 = PythonOperator(
        task_id = 'task_1',
        python_callable=_funcao_criada,
        op_kwargs={'my_param': '42'}
    )