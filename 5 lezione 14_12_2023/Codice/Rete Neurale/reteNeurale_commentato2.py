# Installazione delle dipendenze necessarie
# pip install numpy

import numpy as np

# Definizione della classe ReteNeurale
class ReteNeurale():
    def __init__(self):
        # Inizializzazione del generatore di numeri casuali per riproducibilità
        np.random.seed(1)
        # Inizializzazione dei pesi con valori casuali tra -1 e 1
        self.pesi = 2 * np.random.random((3, 1)) - 1

    def sigmoide(self, x):
        """
        Funzione di attivazione sigmoide.

        La funzione sigmoide è comunemente utilizzata nelle reti neurali per introdurre
        la non linearità. Questa funzione mappa i valori di input in un intervallo compreso
        tra 0 e 1, rendendola utile per modellare le probabilità o i pesi di attivazione.

        Argomenti:
        x (numpy.ndarray): Array contenente i valori di input.

        Ritorno:
        numpy.ndarray: Array contenente i risultati della funzione sigmoide applicata
                      agli elementi di x.
        """
        return 1 / (1 + np.exp(-x))

    def sigmoide_der(self, x):
        """
        Derivata della funzione sigmoide.

        La derivata della funzione sigmoide è utilizzata durante il processo di apprendimento
        per calcolare la correzione dei pesi. Aiuta a determinare quanto il modello deve
        aggiornare i suoi parametri in base all'errore commesso.

        Argomenti:
        x (numpy.ndarray): Array contenente i valori di input.

        Ritorno:
        numpy.ndarray: Array contenente i risultati della derivata della funzione sigmoide
                      applicata agli elementi di x.
        """
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, iterazioni):
        """
        Addestramento della rete neurale utilizzando l'algoritmo di retropropagazione.

        Argomenti:
        training_inputs (numpy.ndarray): Array contenente i dati di input di addestramento.
        training_outputs (numpy.ndarray): Array contenente gli output desiderati di addestramento.
        iterazioni (int): Numero di iterazioni per l'addestramento.
        """
        for iteration in range(iterazioni):
            # Calcolo dell'output a partire dall'input
            output = self.calcola(training_inputs)
            # Calcolo del tasso di errore
            error = training_outputs - output
            # Calcolo delle correzioni secondo il tasso di errore e la derivata della sigmoide
            adj = np.dot(training_inputs.T, error * self.sigmoide_der(output))
            # Aggiornamento dei pesi della rete neurale
            self.pesi += adj

    def calcola(self, inputs):
        """
        Calcolo dell'output della rete neurale per un dato insieme di input.

        Argomenti:
        inputs (numpy.ndarray): Array contenente i dati di input.

        Ritorno:
        numpy.ndarray: Array contenente l'output predetto dalla rete neurale.
        """
        # Conversione degli input in tipo float
        inputs = inputs.astype(float)
        # Applicazione della funzione sigmoide agli input per ottenere l'output della rete
        output = self.sigmoide(np.dot(inputs, self.pesi))
        return output

# Blocco principale del programma
if __name__ == "__main__":
    # Inizializzazione della rete neurale
    rete_neurale = ReteNeurale()

    # Definizione dei dati di addestramento
    training_inputs = np.array([[0, 0, 1],
                                [1, 1, 1],
                                [1, 0, 1],
                                [0, 1, 1]])
    training_outputs = np.array([[0, 1, 1, 0]]).T

    # Addestramento della rete per 20000 iterazioni
    rete_neurale.train(training_inputs, training_outputs, 20000)

    # Inserimento di nuovi dati di input senza specificare l'output desiderato
    print("Nuovo input: ", 1, 1, 0)
    print(rete_neurale.calcola(np.array([1, 1, 0])))
