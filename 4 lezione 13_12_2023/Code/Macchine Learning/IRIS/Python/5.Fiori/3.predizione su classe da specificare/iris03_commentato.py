# Installazione delle librerie necessarie
# Puoi eseguire questi comandi nel tuo ambiente virtuale o nel tuo terminale prima di eseguire lo script
# pip install numpy scikit-learn

# Importazione delle librerie necessarie
import numpy as np
from sklearn import datasets  # Riferimento ai dati di esempio
from sklearn.model_selection import train_test_split  # Organizza dati di apprendimento
from sklearn.linear_model import Perceptron  # Modello di predizione scelto
from sklearn.metrics import accuracy_score  # Calcolo dell'accuratezza

# Caricamento dei dati specifici Iris
iris = datasets.load_iris()
X = iris.data  # Input
y = iris.target  # Output

# Divisione in insiemi di training (80%) e test (20%) senza scelta casuale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Impostazione dei parametri del modello Perceptron
ppn = Perceptron(max_iter=40, tol=0.001, eta0=0.01, random_state=0, verbose=10)
# Supervised learning del modello scelto
ppn.fit(X_train, y_train)

# Predizione sul test set
y_pred = ppn.predict(X_test)

# Verifica dell'errore sul test set
print('Accuratezza della predizione:', accuracy_score(y_test, y_pred))

# Messa in esercizio su nuovi dati da classificare
print("Classe predetta:", ppn.predict([[1.3, 1.2, 4.1, 2.4]]))
print("Classe predetta:", ppn.predict([[4, 11, 3, 3]]))
