from pathlib import Path
import pandas as pd

fileName = "ipca.xlsx"
months = 12

def doing (fileName,months):
    xlsx = pd.ExcelFile(Path("docs",fileName))
    df = pd.read_excel(xlsx)
    df = pd.DataFrame(df)
    #formata a data para o padrão de dataframe
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%y')
    #pega os ultimos 12 meses pela data
    newDf = df[df['data'] >= pd.to_datetime(df['data'].iloc[-1]).date() - pd.DateOffset(months=months-1)]
    #soma todos os meses
    total = newDf['valor'].sum(axis = 0)
    return total.round(3)
print(doing("ipca.xlsx",12))