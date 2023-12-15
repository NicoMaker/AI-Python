import numpy as np
import pandas as pd
from sklearn import datasets #riferimento ai dati di esempio
from sklearn.model_selection import train_test_split #organizza dati learning
from sklearn.linear_model import Perceptron #modello di predizione scelto
from sklearn.metrics import accuracy_score #calcolo dell'accuratezza

excelFile = pd.read_excel('C:\Dati\entrate.xlsx')
X = np.array([excelFile["Esercizio"],
             #excelFile.Accertamenti.values,
             #excelFile.Riscossioni.values,
             excelFile["Residui"]]).T #input
y = excelFile["Esercizio"] #output

print(X)
print(X.shape)
print(y.shape)
#divide in insiemi di training 80% e test 20% e senza scelta casuale  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#impostazione parametri del modello neural network Perceptron
ppn = Perceptron(max_iter=40, tol=0.001, eta0=0.01, random_state=0)
#supervised learning del modello scelto
ppn.fit(X_train, y_train)

#predizione sul test set
y_pred = ppn.predict(X_test)

#verifica errore sul test set
print('accuratezza della predizione',accuracy_score(y_test, y_pred))

#messa in esercizio su nuovi dati di un oggetto da classificare
print ("classe predetta",ppn.predict([[1.3, 1.2]]))
print ("classe predetta",ppn.predict([[4,11]]))