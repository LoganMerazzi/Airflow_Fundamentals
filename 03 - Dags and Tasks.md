DAGs iniciais:

- [simple_dag](./dags/simple_dag.py)
  - A DAG mais simples possível.

## DAG Scheduling

O agendamento de tarefas do airflow segue um fluxo um pouco diferente do usual, desta forma deve-se prestar muita atenção para esse ponto.

  - Parâmetros:
    - start_date:
      - Define a data que a DAG será agendada
    - schedule_interval:
      - Define a frequência que a DAG é disparada
    - execution_date:
      - Define a data que a DAG foi efetivamente executada.

> Importante: a DAG será realmente executada assim que o parâmetro *start_date* **+** o parâmetro *schedule_interval* forem atingidos (ver imagem para ficar mais claro)

<img src="img/Scheduling.svg">

Após a primeira execução da DAG, o parâmetro execution_date se torna o parâmetro start_date da próxima execução. Assim que o intevalo for atingido (start_date + schedule_interval), uma nova execução é iniciada. Neste momento, o parâmetro execution_date para esta execução é marcado.

Fica da seguinte forma:

Execução 1:
  - start_date: 15/10/2022 00:00
  - execution_date: 15/10/2022 06:00

Execução 2:
  - start_date: 15/10/2022 06:00
  - execution_date: 15/10/2022 12:00
  
Execução 3:
  - start_date: 15/10/2022 12:00
  - execution_date: 15/10/2022 18:00

E assim por diante.

