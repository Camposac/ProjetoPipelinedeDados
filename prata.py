import os
import json
import pandas as pd

bronze = "data_lake/bronze/carbonintensity/"
prata = "data_lake/prata/carbonintensity/"

#Garantindo uma lógica incremental
files = os.listdir(bronze)
files = [f.split(".")[0] for f in files]
recent = max(files)
#print(recent)
file_path = os.path.join(bronze, recent)

with open(file_path+".json", "r") as file:

    data = json.load(file)

    #print(data)
    #leitura e transformação do json em um dataset formato tabular, transformamos um dado bruto (json) em um dado mais analítico (csv) em na prata.
    df = pd.DataFrame(data)
    #print(df.head())

    file_name = prata+recent+".csv"
    df.to_csv(file_name, index=False)
