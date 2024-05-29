import numpy as np
import pandas as pd
from sklearn import datasets #riferimento ai dati di esempio
from sklearn.model_selection import train_test_split #organizza dati learning
from sklearn.linear_model import Perceptron #modello di predizione scelto
from sklearn.metrics import accuracy_score #calcolo dell'accuratezza

csv = pd.read_csv("supermarket_sales.csv")

elemments = [
    'Unit price', 'Quantity','Tax 5%','Total',
        'cogs','gross margin percentage','gross income','Rating'
]

# Variabile con i valori dei vettori
Data = csv[elemments]
target = csv['City']

# Gestire il formato della variabile target
target_temp = target.squeeze()
nome_temp = pd.unique(target_temp)

x_train,x_text,y_train,y_text = train_test_split(Data,target, test_size = 0.2, random_state=0)

precetrom = Perceptron(max_iter=1000,tol=0.001,eta0 = 0.01,random_state = 1, verbose=10)
precetrom.fit(x_train,y_train)

y_pred = precetrom.predict(x_text)
accuraty = accuracy_score(y_text,y_pred)
print("Accuratezza: ",accuraty)

nuovo_esempio = np.array([[
    58.15,4,11.63,244.23,232.6,4.761904762,11.63,8.4
]])

classe_predetta = precetrom.predict(nuovo_esempio)

print("Classe Predetta: ",classe_predetta)