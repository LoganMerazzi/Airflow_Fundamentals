## Operators

Um Operador é uma tarefa

        task1 = DummyOperator(
            task_id = 'task_1'
        )

Sempre utilizar um operador para cada tarefas, mesmo que seja do mesmo tipo.

        task1 = DummyOperator(
            task_id = 'task_1'
        )

        task2 = DummyOperator(
            task_id = 'task_2'
        )

Alguns parâmetros:

        task1 = DummyOperator(
            task_id = 'task_1',
            retry = 5,
            retry_delay=timedelta(minutes=5)
        )

E se eu precisar reaproveitar estes parâmetros para outras tarefas?
Usar o parâmetro *default_args* na DAG. 
(ver a dag [default_parameters.py](./dags/default_parameters.py))

