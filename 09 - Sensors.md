## Sensores

Sensores são utilizados para aguardar até uma ação ocorrer, antes de ir para a próxima tarefa.
Verificar o script [sensor.py](./dags/sensor.py) para ver como deve ser desenvolvido.

Notas
  1. Na interface, selecionar Admin -> Connections
     - Os dados são encriptados no banco, mas visualizados na interface.
  2. O campo *Connection id* deve ter o mesmo valor informado no script.
  3. No caso de arquivos de sistema, a *connection type* deve ser *File(path)*
  4. Extra: Espera um JSON. No caso do sistema de arquivos:

    {"path":"/tmp"}
   
  5. Por padrão, os sensores avaliam as conexões a cada 30 segundos, para alterar esse valor, deve-se usar o parâmetro *poke_interval*
