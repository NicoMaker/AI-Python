tensorflow_version 2.x  # attiva esecuzione della versione 2.0
import tensorflow as tf
print(tf.__version__)

# crea un tensore
x = [[2.]]
m = tf.square(x)
print("Descrizione di m:", m)
print("Contenuto di m:", m.numpy())

# moltiplica due tensori
a = tf.constant([[2, 2], [3, 4]])
b = tf.constant([[2, 1],  # separare le righe aumenta leggibilità
                 [3, 2]])
ab = tf.matmul(a, b)
print('a * b = \n', ab.numpy())

@tf.function  # definisce operazione su tensore
def f(x): return tf.add(x, 1.)  # aggiunge 1 a tensore x

a = tf.constant("Benvenuto TensorFlow 2.0!")  # tensore con una stringa
print(a)
print(a.numpy())

scalar = tf.constant(1.0)  # tensore contiene una costante
vector = tf.constant([1.0, 1.0])  # tensore come array con 2 costanti

matrix = tf.constant([[3.0, 2.0], [6.0, 4.0]])  # tensore come matrice 2x2 con 4 costanti
print(f(scalar))
print(f(vector))
print(f(matrix))

# calcolo del grafo in Figura 18.1
a = tf.constant(5)
b = tf.constant(8)
c = tf.constant(2)
d = tf.constant(3)
e = tf.constant(6)
f = ((a + b + c) * d) / e
print(f)
print(f.numpy())

# crea un computational graph con i due approcci
import numpy as np
data = np.array([[1.764, 0.400],
                 [0.978, 2.240],
                 [1.867, -0.977],
                 [2.467, -0.107]])

input_layer = tf.keras.layers.InputLayer(input_shape=(2))  # input layer con 2 valori
hidden = tf.keras.layers.Dense(3, activation='relu')  # 1 hidden layer denso con 3 neuroni
output = tf.keras.layers.Dense(1, activation='sigmoid')  # output layer denso con 1 neurone

# crea modello con approccio di chiamata a funzione ed esecuzione dinamica
# i dati di input vanno nel primo livello, che è il primo nodo
# quando aggiunge il secondo nodo, l'output del primo nodo viene inserito nel secondo nodo
# e viene calcolato l'output del secondo nodo e così via
# consente di stampare stati intermedi del modello, ma rallenta molto i calcoli
def model_1(data):
    x = hidden(data)
    print('Dopo il primo layer:', x)
    out = output(x)
    print('Dopo il secondo layer:', out)
    return out

print('Output come tensore:', model_1(data))
print('Output come valori:\n', model_1(data).numpy())

@tf.function  # crea modello con approccio creazione grafo statico
# prima collega tutti i nodi facendo una grande operazione computazionale
# quindi segue il flusso del grafo per fare i calcoli, non mostra stati intermedi
# del modello né aggiunge nodi al volo, ma è più veloce dell'altro approccio
def model_2(data):
    x = input_layer(data)
    x = hidden(x)
    print('Dopo il primo layer:', x)
    out = output(x)
    print('Dopo il secondo layer:', out)
    return out

print('Output come tensore:', model_2(data))

for i, d in enumerate(data):
    print('batch ciclo esterno {} interno {}:'.format(i, j))
    model_1(d[np.newaxis, :])  # calcola loss con approccio eager

for i, d in enumerate(data):
    print('batch ciclo esterno {} interno {}:'.format(i, j))
    model_2(d[np.newaxis, :])  # calcola loss con approccio grafo statico
