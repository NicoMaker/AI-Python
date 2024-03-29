# python -m pip install scikit-learn

from sklearn.datasets import load_iris
iris = load_iris()

x = iris.data
y = iris.target

print(x.shape, y.shape)
print(iris.feature_names, iris.target_names)