#importazione librerie necessarie

import numpy as np
from sklearn import datasets #riferimento ai dati di esempio
from sklearn.model_selection import train_test_split #organizza dati learning
from sklearn.linear_model import Perceptron #modello di predizione scelto
from sklearn.metrics import accuracy_score #calcolo dell'accuratezza

#carica gli specifici dati Iris
iris = datasets.load_iris()
X = iris.data #input
y = iris.target #output
#divide in insiemi di training 80% e test 20% senza scelta casuale  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#impostazione parametri del modello neural network Perceptron
ppn = Perceptron(max_iter=40, tol=0.001, eta0=0.01, random_state=0)
#supervised learning del modello scelto
ppn.fit(X_train, y_train)

#predizione sul test set
y_pred = ppn.predict(X_test)
#verifica errore sul test set
accuracy_score(y_test, y_pred)

#messa in esercizio su nuovi dati di un oggetto da classificare
print ("classe predetta",ppn.predict([[7, 5, 2, 1, 0]]))