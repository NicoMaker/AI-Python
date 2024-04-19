# pulire dataset
# addestrare una rete neurale che in base all'importo capisce a che categoria di entrate 
#appartiene

# Importa librerie necessarie
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# Carica il dataset load entrate()
dati_pagamenti = pd.read_excel('c:\dati\entrate.xlsx')

# Seleziona colonne da verificare per la pulizia del dataset
cols_to_check = ['Accertamenti 2^ Esercizio antecedente', 'Previsione definitiva Esercizio Precedente', 'Previsioni Iniziali Competenza', 'Previsioni Definitive Competenza', 'Accertamenti', 'Riscossioni', 'Residui']

# Rimuovi le righe in cui tutte le colonne selezionate hanno valore zero
dati_pagamenti = dati_pagamenti.loc[~(dati_pagamenti[cols_to_check] == 0).all(axis=1)]

# Seleziona le colonne di input e output
data = dati_pagamenti[["Accertamenti 2^ Esercizio antecedente","Previsione definitiva Esercizio Precedente","Previsioni Iniziali Competenza","Previsioni Definitive Competenza","Accertamenti","Riscossioni","Residui"]]
target = dati_pagamenti[["Titolo"]]

# Gestisci il formato della variabile target
temp_target = target.squeeze()
target_names = pd.unique(temp_target)

print("Target Names:", target_names)

# Suddividi il dataset in set di addestramento e test
data_train, data_test, target_train, target_test = train_test_split(data, target, test_size=0.2, random_state=0)

# Crea e addestra il classificatore Perceptron
ppn = Perceptron(max_iter=40, tol=0.001, eta0=0.01, random_state=0)
ppn.fit(data_train, target_train)

# Calcola l'accuratezza del modello
target_pred = ppn.predict(data_test)
accuracy = accuracy_score(target_test, target_pred)
print("Accuratezza del modello:", accuracy)

# Esegui una predizione su un nuovo esempio
new_example = np.array([[6541,651,178096,32,189,1234,0]])  # valori di esempio
predicted_class = ppn.predict(new_example)
print("Classe predetta:", predicted_class)
