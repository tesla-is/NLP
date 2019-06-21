import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv('dataset/StudentsPerformance.csv')
dataset.columns = ['gender',
                   'race',
                   'ped',
                   'lunch',
                   'test',
                   'math',
                   'reading',
                   'writing']

dataset.info()
dataset.describe()
pd.scatter_matrix(dataset)
sns.pairplot(dataset)

dataset['gender'].value_counts()

sns.barplot(dataset['gender'].value_counts().index,
            dataset['gender'].value_counts())

sns.barplot(dataset['gender'], dataset['math'],
            hue = dataset['gender'])

sns.barplot(dataset['gender'], dataset['reading'],
            hue = dataset['gender'])

sns.barplot(dataset['gender'], dataset['writing'],
            hue = dataset['gender'])

sns.barplot(dataset['race'], dataset['math'],
            hue = dataset['gender'])

sns.barplot(dataset['ped'], dataset['reading'],
            hue = dataset['gender'])

sns.barplot(dataset['lunch'], dataset['reading'],
            hue = dataset['gender'])

sns.barplot(dataset['test'], dataset['reading'],
            hue = dataset['gender'])

plt.hist(dataset['math'], bins = 100)
sns.boxplot(dataset['math'])
sns.boxplot(dataset['reading'])
sns.boxplot(dataset['writing'])

sns.boxplot(dataset['gender'], dataset['math'])
sns.boxplot(dataset['gender'], dataset['reading'])
sns.boxplot(dataset['gender'], dataset['writing'])




































