AmbientWeather Data Backup

Este script Python permite fazer backup dos dados diários de um dispositivo AmbientWeather para um arquivo CSV. Ele obtém os dados do dia anterior e os salva em um arquivo CSV para fins de registro ou análise posterior.

Requisitos
Python 3.x
Bibliotecas Python: requests, csv, urllib3
Um dispositivo AmbientWeather com um endereço MAC válido

Configuração
Antes de executar o script, é necessário configurar o endereço MAC do dispositivo AmbientWeather que deseja fazer backup. O endereço MAC deve ser atribuído à variável mac_address na função main().

Funcionalidades
Obtenção de Dados Diários: O script calcula o intervalo de tempo correspondente ao dia anterior em UTC e obtém os dados diários do dispositivo AmbientWeather para esse período.
Salvamento em Arquivo CSV: Os dados obtidos são salvos em um arquivo CSV com cabeçalhos de coluna correspondentes aos nomes dos campos de dados. Os timestamps Unix são convertidos em formatos legíveis de data e hora para facilitar a interpretação.
Gestão de Erros: O script lida com possíveis erros, como falha na obtenção de dados ou falta de dados válidos para salvar.

Execução
Para executar o script, basta chamar a função main().

python ambientweather_backup.py

Notas
Este script foi desenvolvido para fazer backup de dados diários de um dispositivo AmbientWeather específico. Modificações podem ser necessárias para adaptá-lo a outros dispositivos ou requisitos específicos.
É importante observar que este script faz uso da biblioteca requests para realizar solicitações HTTP. Certifique-se de que o ambiente em que o script é executado tenha acesso à internet e permissões adequadas para acessar o serviço AmbientWeather.
Este script foi desenvolvido para ser executado em um ambiente local. Se desejar automatizar o processo de backup, considere agendar a execução do script em um servidor ou sistema com tarefas agendadas.

Autor
Este script foi desenvolvido por Leonardo Ramos.