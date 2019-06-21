import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import load_iris
dataset = load_iris()

X = dataset.data
y = dataset.target

plt.scatter(X[y == 0, 0] , X[y == 0, 1], c = "r", label = "Setosa")
plt.scatter(X[y == 1, 0] , X[y == 1, 1], c = "g", label = "Versicolor")
plt.scatter(X[y == 2, 0] , X[y == 2, 1], c = "b", label = "Verginica")
plt.legend()
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Analysis on the Iris dataset')
plt.show()


plt.scatter(X[y == 0, 2] , X[y == 0, 3], c = "r", label = "Setosa")
plt.scatter(X[y == 1, 2] , X[y == 1, 3], c = "g", label = "Versicolor")
plt.scatter(X[y == 2, 2] , X[y == 2, 3], c = "b", label = "Verginica")
plt.legend()
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Analysis on the Iris dataset')
plt.show()








