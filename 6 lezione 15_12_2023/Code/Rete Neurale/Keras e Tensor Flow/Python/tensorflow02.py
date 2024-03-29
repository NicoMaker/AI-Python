import tensorflow_datasets as tfds
print("Elenco data set in TensorFlow 2.0", tfds.list_builders())
data, info = tfds.load(name='fashion_mnist', as_supervised=True, split=None, with_info=True)
print("Descrizione data set MNIST",info)