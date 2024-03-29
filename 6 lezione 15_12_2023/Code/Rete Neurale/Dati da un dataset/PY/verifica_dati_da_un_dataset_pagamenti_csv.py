#versione Eduardo Pazitto
#convertito l'excel in un csv

import pandas as pd 
from sklearn.model_selection import train_test_split #organizza dati learning
from sklearn.linear_model import Perceptron #modello di predizione scelto
from sklearn.metrics import accuracy_score #calcolo dell'accuratezza

data = pd.read_csv('./entrate.csv', sep=',')

data.info()
data = data.dropna()

columnsToStudy = [
    'Accertamenti 2^ Esercizio antecedente', 
    'Previsione definitiva Esercizio Precedente',
    'Previsioni Iniziali Competenza',
    'Previsioni Definitive Competenza',
    'Accertamenti',
    'Riscossioni',
    'Residui',
]

targetColumn = 'Titolo Codice'

data = data.loc[~(data[columnsToStudy] == 0).all(axis=1)]

# Estrai i dati di addestramento e test
X_train, X_test, y_train, y_test = train_test_split(
    data[columnsToStudy], 
    data[targetColumn], 
    test_size=0.2, 
    random_state=0
)

# impostazione parametri del modello neural network Perceptron
ppn = Perceptron(max_iter=40, tol=0.001, eta0=0.01, random_state=0,verbose=10)

# supervised learning del modello scelto
ppn.fit(X_train, y_train)

# Effettua previsioni sui dati di test
predictions = ppn.predict(X_test)

# Calcola e stampa l'accuratezza del modello
accuracy = accuracy_score(y_test, predictions)

print(f'Accuratezza: {accuracy}')
print(f'Predictions: {predictions}')

# Dati di input per la previsione
predictionDataTest = {
    'Accertamenti 2^ Esercizio antecedente': 80979873,
    'Previsione definitiva Esercizio Precedente': 870000,
    'Previsioni Iniziali Competenza': 900000,
    'Previsioni Definitive Competenza': 900000,
    'Accertamenti': 88279161,
    'Riscossioni': 88207095,
    'Residui': 72066,
}


# Creazione di un DataFrame dai nuovi dati
predictionDataTestDf = pd.DataFrame([predictionDataTest])

# Effettua la previsione utilizzando il modello addestrato
previsione = ppn.predict(predictionDataTestDf)

# Stampa la previsione
print(f"La previsione del Titolo Codice per i nuovi dati è: {previsione}")