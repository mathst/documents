from pathlib import Path
import pandas as pd
import requests
import json

def check(file):
    try:
        xlsx = pd.ExcelFile(Path("docs",file))
        df = pd.read_excel(xlsx)
        df = pd.DataFrame(df)
    except:
        df = file
    return df

def doing (file,months):
    months = int(months)
    # if para ver se é um xlsx ou um json 
    dfN = check(file)
    #formata a data para o padrão de dataframe
    dfN['data'] = pd.to_datetime(dfN['data'],dayfirst=True)
    #pega os ultimos 12 meses pela data
    newdfN = dfN[dfN['data'] >= pd.to_datetime(dfN['data'].iloc[-1]).date() - pd.DateOffset(months=months-1)]
    #soma todos os meses
    total =pd.to_numeric(newdfN['valor']).sum(axis = 0)

    return total.round(3)
    
    

def resquestBank():
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json&dataInicial=01/01/2000&dataFinal=31/12/2100"

    payload={}
    headers = {
    'Cookie': 'TS01799025=0198c2d644f13cfdef27b53fb25bc65b118a0740692bec41dbe45d475d7a2170c1fa95b97b51f1450671360e491fffc128110b374b; cookie_p=!nOx5QBw5Y6Skqlyk8M1gyyMHr0m/UwJSD7hWYaaTlYqZPXQx3bPhZq2NLuVPEZrUMXZP8UYkfaGE0/I='
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    
    
    data = json.loads(response.text)
    dfItem = pd.DataFrame.from_records(data)
    # saida de um df
    return dfItem
