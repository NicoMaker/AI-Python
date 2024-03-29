from sklearn.datasets import load_iris
iris = load_iris()

#L’oggetto iris è un tipo di dato particolare.
#  Per ricavare le feature e le etichette delle classi:

X = iris.data
y = iris.target

#Si ottengono due strutture numpy.ndarray, per conoscere le dimensioni:
print(X.shape, y.shape)
print(iris.feature_names, iris.target_names)