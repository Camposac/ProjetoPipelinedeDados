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
    df = pd.read_csv(file_path)

    return df

def escrita_dados(df, path, dados):
    
    file_name = f"{path}{dados['search_date'][0]}.csv"
    df.to_csv(file_name, Index=False)
    

today = date.today()
today_pd = pd.to_datetime(today)


ontem = today - timedelta(days=1)
amanha = today + timedelta(days=1)

ontem_pd = pd.to_datetime(ontem)
amanha_pd = pd.to_datetime(amanha)

#ouro = leitura_dados(ouro)

prata = leitura_dados(prata)

prata['prevision_data'] = pd.to_datetime(prata['prevision_data'])


