# python -m pip install pandas

import pandas as pd

data =  pd.read_csv("D:\\Corso ITS IIOT\\2 anno\AI Python\AI-Python\\4 lezione 13_12_2023\Codice\Macchine Learning\\Dati per es\\csv2.CSV")
print(data)  #stamppa dati

data.info()
for row in data:
    print(row)
data.to_csv("D:\\Corso ITS IIOT\\2 anno\AI Python\AI-Python\\4 lezione 13_12_2023\Codice\Macchine Learning\\IRIS\\Result IRIS\\outputfilecsv.csv" , index=None, header=True)    