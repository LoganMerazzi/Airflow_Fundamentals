## Parâmetro start_date

Observações:

    É um parâmetro obrigatório nas DAGs.

    Importar a lib datetime

    As datas estão sempre em UTC.

    Especificando uma data no passado, todas as DAG Runs que teriam sido executadas, serão disparadas automaticamente, ao mesmo tempo.

    Nunca utilizar uma data dinâmica, por exemplo datime.now(). Se isso ocorrer, a DAG nunca será executada, pois nunca chegará na trigger.