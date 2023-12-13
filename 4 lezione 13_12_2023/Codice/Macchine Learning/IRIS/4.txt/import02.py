import pandas as pd
import openpyxl

data = pd.read_csv('C:\dati\csv2.csv', sep=';')
print(data) #visualizza i dati
data.info() #visualizza struttura dataframe e nomi di colonne
for row in data: #visualizza nomi di colonne
    print(row)
data.to_csv (r'C:\dati\lezione-iiot.csv', index = None, header=True) #salva in file dataframe.csv il dataframe con nome data
#data.to_excel(r'C:\dati\exportexcel.xlsx', index=False)