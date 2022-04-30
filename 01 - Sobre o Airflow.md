## O que é o Airflow?

Airflow é uma plataforma onde é possível criar, agendar e monitorar seus workflows de forma programática.
Ou seja, é um orquestrador, onde é possível criar pipelines dinamicos e executar suas tarefas na ordem correta, de forma correta e no seu devido tempo.

## O que *não* é o Airflow?

O Airflow não é um framework para realizar procesamento de dados
Não use o Airflow como se estivesse usando o Spark. Para isso, chame um job do Spark no Airflow.

## Core Components

- Web Server
    - 
- Scheduler
- Metadata Database

2 componentes adicionais:

- Executor
- Worker

## Arquitetura:

Dados os componentes, é possível criar diversos tipos de arquiteturas usando o Airflow.

- Single Node

<img src="img/Single_Node.svg">

    - Neste caso, todos os recursos ficam disponíveis em uma unica máquina.
      - Não escala.
    - O Web Server é responsável por retornar os dados do banco de dados
    - O Scheduler se comunica com a base para verificar os horários de execução e realiza as chamadas para o Executor
    - O Executor faz o processamento (insere na fila - que faz parte do Executor, nesta arquitetura) e retorna as informações para o Banco.

- Multi Node cluster

<img src="img/Multi_Node.svg">

    - Neste modelo os recursos ficam disponíveis em "nós" e é possível escalar conforme a necessidade.
    - O WebServer é responsável por retornar os dados do banco de dados
    - O Scheduler se comunica com a base para verificar os horários de execução e realiza as chamadas para o Executor
    - O Executor coloca as informações na fila (desta vez, à parte do Executor) e os workers buscam os dados da fila para processar.
    - Com isso, caso seja necessário aumentar o paralelismo, basta adicionar novos workers no cluster.

## Conceitos

  - DAGs: é o conjunto de tarefas, possuindo um começo e um fim, sem passar novamente pelas etapas anteriores (Direct **Acyclic** Graph)
  
  <img src="img/Dag.svg">

  - Operadores: É uma das tarefas dentro da DAG.
    - Action Operator:
      - Responsável por executar algo dentro da DAG, por exemplo o PythonOperator, que executará um script em python desenvolvido, ou o BashOperator, que executará um comando bash.
    - Transfer Operator:
      - Permite transportar dados entre origens e destinos.
    - Sensor Operator:
      - Fica monitorando um status ocorrer antes de mover para a próxima task.
    
  - Task: 
    - Quando o Operator está vinculado à uma DAG (uma instância de um Operator).
  - Task Instance: 
    - É a execução de uma Task

  - Dependências
    - Determina os relacionamentos entre as Tasks
      - Podem ser utilizadas as funções set_upstream ou set_downstream, mas não é uma boa prática recomendada.
      - O ideal é usar os sinais "<<" ou ">>" para determinar as dependências entre as tasks

  - Workflow
    - Combinação de todos os tópicos citados acima.

Resumindo:

<img src="img/Workflow.svg">


## Ciclo de Vida de uma Tarefa

<img src="img/TaskLifecycle.svg">

## Extras and Providers

