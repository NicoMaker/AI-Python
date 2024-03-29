import numpy as np

class ReteNeurale():
    def __init__(self):
        # Inizializzazione dei pesi con valori casuali compresi tra -1 e 1
        np.random.seed(1)
        self.pesi = 2 * np.random.random((3, 1)) - 1

    def sigmoide(self, x):
        # Funzione di attivazione sigmoide
        return 1 / (1 + np.exp(-x))

    def sigmoide_der(self, x):
        # Derivata della funzione sigmoide
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, iterazioni):
        for iteration in range(iterazioni):
            # Calcolo dell'output a partire dall'input
            output = self.calcola(training_inputs)
            # Calcolo del tasso di errore
            error = training_outputs - output
            # Calcolo delle correzioni secondo il tasso di errore
            adj = np.dot(training_inputs.T, error * self.sigmoide_der(output))
            # Aggiornamento dei pesi
            self.pesi += adj

    def calcola(self, inputs):
        inputs = inputs.astype(float)
        # Applicazione della funzione sigmoide agli input
        output = self.sigmoide(np.dot(inputs, self.pesi))
        return output

if __name__ == "__main__":
    # Inizializzazione della rete neurale
    rete_neurale = ReteNeurale()
    
    # Definizione dei dati di addestramento
    training_inputs = np.array([[0.5, 1, 0],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1]])
    training_outputs = np.array([[0, 1, 1, 0]]).T
    
    # Addestramento della rete
    rete_neurale.train(training_inputs, training_outputs, 20000)
    
    # Inserimento di nuovi dati, senza l'output desiderato
    print("Nuovo input: ", 1, 1, 0)
    
    # Calcolo dell'output per i nuovi dati
    print(rete_neurale.calcola(np.array([1, 1, 0])))
