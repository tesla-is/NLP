import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_excel('blood.xlsx')
X = dataset.iloc[:, 1].values
X = X.reshape(-1, 1)
y = dataset.iloc[:, -1].values

plt.scatter(X, y)
plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)


lin_reg.score(X, y)
lin_reg.score(X_train, y_train)
lin_reg.score(X_test, y_test)

plt.scatter(X_train, y_train)
plt.plot(X_train, lin_reg.predict(X_train), c = "r")
plt.show()

plt.scatter(X_test, y_test)
plt.plot(X_test, lin_reg.predict(X_test), c = "r")
plt.show()

plt.scatter(X, y)
plt.plot(X, lin_reg.predict(X), c = "r")
plt.show()

y_pred = lin_reg.predict(X_test)

lin_reg.predict([[20]])
lin_reg.predict([[26]])
lin_reg.coef_
lin_reg.intercept_































