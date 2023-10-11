#importando as bibliotecas necessárias no projeto
import json
import requests
from datetime import timedelta, date

#ENDPOINT
api_url = 'https://api.carbonintensity.org.uk/intensity/date/'

#Função que gera as datas
def generate_range_date (start_date, end_date):
    # (1) Lista de datas com a (2) data de hoje sendo a data de inicio 
    date_range = []
    current_date = start_date

    while current_date <= end_date:
        date_range.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)
    
    return date_range

#range de datas: ontem (start_date), hoje (today) e amanhã (end_date)
today = date.today()
start_date = today - timedelta(days=1)
end_date = today + timedelta(days=1)

#Aqui a função que gera as datas é chamada
dates = generate_range_date(start_date, end_date)
#lista vazia para receber as datas
dados = []

# (E) EXTRACT
#gerador de datas
for date in dates:
    r = requests.get(f'{api_url}{date}')
    #Significados 200: Ok; 400: Bad Request; 500: Internal Server Error 
    #print(r.status_code)
    r = r.json()

# (T) TRANSFORM

    intensity = r['data'][0]['intensity']
    forecast = intensity['forecast']
    actual = intensity['actual']
    index = intensity['index']

    dados.append({
        "Search_date":today.strftime("%Y-%m-%d"),
        "prevision_date": date,
        "index": index,
        "actual": actual,
        "forecast":forecast
    })  

    #print(dados)

# (L) LOAD

with open("bronze.json", "w") as arquivo:
    json.dump(dados,arquivo,indent=4)


