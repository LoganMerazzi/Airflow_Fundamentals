## Parâmetro schedule_interval

Valor default: 24 horas
O parametro pode ser:
  - uma expressão *cron* (crontab)
    - usar o site http://crontab.guru para facilitar a criação da string.
  - um objeto do tipo *timedelta*
  - ser do tipo None. Neste caso, o scheduler nunca irá disparar a DAG. As execuções precisarão ocorrer de forma manual ou externamente.


