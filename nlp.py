import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
import re

dataset = pd.read_csv('train.csv')
dataset['tweet'][0]

processed_list = []

for i in range(31962):
    tweet = re.sub('[^a-zA-Z]', ' ', dataset['tweet'][i])
    tweet = tweet.lower()
    tweet = tweet.split()
    tweet = [ps.stem(token) for token in tweet if not token in set(stopwords.words('english'))]
    tweet = ' '.join(tweet)
    processed_list.append(tweet)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 3000)
X = cv.fit_transform(processed_list)
X =  X.toarray()
y = dataset.iloc[:, 1].values
print(cv.get_feature_names())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

from sklearn.tree import DecisionTreeClassifier
dtf = DecisionTreeClassifier(max_depth = 5)
dtf.fit(X_train, y_train)


from sklearn.svm import SVC
svm = SVC()
svm.fit(X_train, y_train)


from sklearn.naive_bayes import GaussianNB
n_b = GaussianNB()
n_b.fit(X_train, y_train)


log_reg.score(X_train, y_train)
log_reg.score(X_test, y_test)
log_reg.score(X, y)

knn.score(X_train, y_train)
knn.score(X_test, y_test)
knn.score(X, y)

dtf.score(X_train, y_train)
dtf.score(X_test, y_test)
dtf.score(X, y)

svm.score(X_train, y_train)
svm.score(X_test, y_test)
svm.score(X, y)

n_b.score(X_train, y_train)
n_b.score(X_test, y_test)
n_b.score(X, y)























