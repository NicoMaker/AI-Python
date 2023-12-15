# lettura dati file excel e crea il valore in base ai dati della tabella tasse da il valore con un logica  di AI

import numpy as Numpy
import pandas as Pandas

data = Pandas.read_excel("C:\Dati\entrate.xlsx" )
print(data)

class ReteNeurale():
    def __init__(self):
        # Inizializzazione dei pesi con valori casuali compresi tra -1 e 1
        Numpy.random.seed(1)
        self.pesi = 2 * Numpy.random.random((3, 1)) - 1

    def sigmoide(self, x):
        # Funzione di attivazione sigmoide
        return 1 / (1 + Numpy.exp(-x))

    def sigmoide_der(self, x):
        # Derivata della funzione sigmoide
        return x * (1 - x)

    def train(self, training_iNumpyuts, training_outputs, iterazioni):
        for iteration in range(iterazioni):
            # Calcolo dell'output a partire dall'iNumpyut
            output = self.calcola(training_iNumpyuts)
            # Calcolo del tasso di errore
            error = training_outputs - output
            # Calcolo delle correzioni secondo il tasso di errore
            adj = Numpy.dot(training_iNumpyuts.T, error * self.sigmoide_der(output))
            # Aggiornamento dei pesi
            self.pesi += adj

    def calcola(self, iNumpyuts):
        iNumpyuts = iNumpyuts.astype(float)
        # Applicazione della funzione sigmoide agli iNumpyut
        output = self.sigmoide(Numpy.dot(iNumpyuts, self.pesi))
        return output

if __name__ == "__main__":
    # Inizializzazione della rete neurale
    rete_neurale = ReteNeurale()
    
    # Definizione dei dati di addestramento
    training_iNumpyuts = Numpy.array([[0.5, 1, 0],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1]])
    training_outputs = Numpy.array([[0, 1, 1, 0]]).T
    
    # Addestramento della rete
    rete_neurale.train(training_iNumpyuts, training_outputs, 20000)
    
    # Inserimento di nuovi dati, senza l'output desiderato
    print("Nuovo iNumpyut: ", 1, 1, 0)
    
    # Calcolo dell'output per i nuovi dati
    print(rete_neurale.calcola(Numpy.array([1, 1, 0])))