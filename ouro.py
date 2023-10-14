import os
import pandas as pd
from datetime import timedelta, date


prata = "data_lake/prata/carbonintensity/"
ouro = "data_lake/ouro/carbonintensity/"

def leitura_dados(path):

    files = os.listdir(path)
    files = [f.split(".")[0] for f in files]
    recent = max(files)
    file_path = os.path.join(path, recent)
    df = pd.read_csv(file_path+".csv")

    return df

def escrita_dados(df, path, dados):
    
    file_name = f"{path}{dados['search_date'][0]}.csv"
    df.to_csv(file_name, index=False)
    

today = date.today()
today_pd = pd.to_datetime(today)


ontem = today - timedelta(days=1)
amanha = today + timedelta(days=1)

ontem_pd = pd.to_datetime(ontem)
amanha_pd = pd.to_datetime(amanha)

#ouro = leitura_dados(ouro)

prata = leitura_dados(prata)

prata['prevision_date'] = pd.to_datetime(prata['prevision_date'])

df_filtrado = prata.query('@ontem_pd <= prevision_date <= @today_pd')


dados = {

    "search_date": [today],
    "avg_start_date": [ontem],
    "avg_end_date": [today],
    "actual_average": [df_filtrado['actual'].mean()],
    "today_actual": prata.query("prevision_date == @today_pd")['actual'].values,
    "yesterday_actual": prata.loc[prata['prevision_date'] == ontem.strftime("%Y-%m-%d"), 'actual'].values,
    "tomorrow_forecast": prata.loc[prata['prevision_date'] == amanha.strftime("%Y-%m-%d"), 'forecast'].values,
    "today_index": prata.loc[prata['prevision_date'] == today.strftime("%Y-%m-%d"), 'index'].values,
    "yesterday_index": prata.loc[prata['prevision_date'] == ontem.strftime("%Y-%m-%d"), 'index'].values,
    "tomorrow_index": prata.loc[prata['prevision_date'] == amanha.strftime("%Y-%m-%d"), 'index'].values  
}


new_df =pd.DataFrame(dados)

escrita_dados(new_df, ouro ,dados)
