# Per installare le librerie necessarie, esegui i seguenti comandi:

# pip install keras
# pip install scikit-learn
# pip install matplotlib

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import CuDNNLSTM, Dense, Dropout, LSTM
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Importa i dati e crea training e test, dal training ricava il validation set
(X_train_val, y_train_val), (X_test, y_test) = mnist.load_data()
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.15)

# Normalizza i valori dei pixel rispetto valore massimo 255
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0
X_val = X_val.astype('float32') / 255.0

# Inizializza il modello
lstm = Sequential()

# Aggiunge il livello input a LSTM
lstm.add(CuDNNLSTM(128, input_shape=(X_train.shape[1:]), return_sequences=True))
lstm.add(Dropout(0.2))

# Aggiunge un altro livello
lstm.add(CuDNNLSTM(128))

# Aggiunge il dense hidden layer con attivazione relu
lstm.add(Dense(64, activation='relu'))
lstm.add(Dropout(0.2))

# Aggiunge livello output
lstm.add(Dense(10, activation='softmax'))

# Compila il modello con i parametri per training e misura metrica
lstm.compile(loss='sparse_categorical_crossentropy', optimizer=Adam(lr=0.001, decay=1e-6), metrics=['accuracy'])

# Fit del modello con i dati per fare training
history = lstm.fit(X_train, y_train, epochs=3, validation_data=(X_val, y_val))

# Raccoglie i dati per descrivere il training eseguito
print(history.history.keys())

# Crea i grafici per mostrare andamento del training eseguito
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Andamento loss durante il training')
plt.ylabel('Loss')
plt.xlabel('Epoca')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

# Valuta i dati sul test set e misura delle metriche
test_loss, test_acc = lstm.evaluate(X_test, y_test)
print('Test Loss: {}'.format(test_loss))
print('Test Accuracy: {}'.format(test_acc))
