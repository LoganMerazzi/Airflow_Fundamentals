## Backfilling

Referência: Script [default_parameters.py](./dags/default_parameters.py)

Backfilling é a possibilidade do Airflow executar processos que ainda não rodaram no passado (por exemplo, durante uma manutenção na DAG que ocorreu e "pulou" alguma execução). Ao habilitar o ajuste, automaticamente todas as DAGs anteriores não executadas serão executadas automaticamente.

Parâmetro *catchup=True/False* na definição da DAG.

Cuidar com esse parâmetro, pois você pode esgotar os recursos da máquina, supondo que seja especificado uma data de início como algo a um ano no passar e um intervalo de execução por hora. Ao ativar a DAG, o scheduler irá disparar mais de 8500 processos (24 execuções por dia, por 365 dias).

O parâmetro *max_active_runs* na definição da DAG faz com que você consiga limitar o máximo de execuções concorrentes que aquela DAG possuirá.

Melhores práticas:
  - Quando precisar usar o backfilling, o ideal é deixar o parâmetro catchup como False e executar o processo de backfilling via CLI.