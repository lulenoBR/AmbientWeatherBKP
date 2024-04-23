import requests
import csv
import urllib3
import os
from datetime import datetime, timedelta, timezone

# Desativar advertências de segurança
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_epoch_unix_for_yesterday():
    # Obter a data e hora atuais em UTC
    current_utc_time = datetime.now(timezone.utc)

    # Obter a data do dia anterior
    yesterday_utc = current_utc_time - timedelta(days=1)

    # Definir a hora para 00:00:00
    yesterday_start = datetime(yesterday_utc.year, yesterday_utc.month, yesterday_utc.day, 0, 0, 0, tzinfo=timezone.utc)

    # Definir a hora para 23:59:59
    yesterday_end = datetime(yesterday_utc.year, yesterday_utc.month, yesterday_utc.day, 23, 59, 59, 999999, tzinfo=timezone.utc)

    # Converter as datas para época Unix
    start_time = int(yesterday_start.timestamp()) * 1000
    end_time = int(yesterday_end.timestamp()) * 1000

    return start_time, end_time


def get_daily_data(mac_address, start_time, end_time):
    url = f'https://lightning.ambientweather.net/device-data?start={start_time}&end={end_time}&macAddress={mac_address}&res=1&limit=3600&dataKey=dataTableData'
    response = requests.get(url, verify=False)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Erro ao obter dados diários. Código de status:", response.status_code)
        return None

def save_to_csv(data, filename):
    if data is not None and 'data' in data:
        data_list = data['data']
        if isinstance(data_list, list) and len(data_list) > 0:
            first_item = data_list[0]
            if isinstance(first_item, dict):
                with open(filename, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=first_item.keys())
                    writer.writeheader()  # Escreve os cabeçalhos das colunas
                    for item in data_list:
                        # Convertendo os timestamps Unix para data e hora legíveis
                        item['dateutc'] = datetime.fromtimestamp(item['dateutc'] / 1000, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                        item['created_at'] = datetime.fromtimestamp(item['created_at'] / 1000, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                        item['dateutc5'] = datetime.fromtimestamp(item['dateutc5'] / 1000, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                        item['lastRain'] = datetime.fromtimestamp(item['lastRain'] / 1000, timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                        writer.writerow(item)
                print("Dados salvos em", filename)
                return
    print("Não há dados válidos para salvar.")

def main():
    # Defina o endereço MAC do dispositivo
    mac_address = '48:55:19:C3:17:68'

    # Obter época Unix para o dia anterior
    start_time, end_time = get_epoch_unix_for_yesterday()
    
    date_str = datetime.utcfromtimestamp(start_time / 1000).strftime('%d-%m-%Y')
    folder_name = 'AmbientWeather-bkp'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = os.path.join(folder_name, f'{date_str}_AmbientWeather.csv')

    # Obter os dados diários
    data = get_daily_data(mac_address, start_time, end_time)
    
    if data is not None:
        save_to_csv(data, filename)
    else:
        print("Não foi possível obter os dados diários.")

if __name__ == "__main__":
    main()
