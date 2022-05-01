## Parâmetro schedule_interval

Ver o uso do parâmetro no script [simple_dag_03](./dags/simple_dag_03.py)

Valor default: 24 horas
O parametro pode ser:
  - uma expressão *cron* (crontab)
    - usar o site http://crontab.guru para facilitar a criação da string.
  - um objeto do tipo *timedelta*
  - ser do tipo None. Neste caso, o scheduler nunca irá disparar a DAG. As execuções precisarão ocorrer de forma manual ou externamente.


