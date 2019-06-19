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

sns.barplot(dataset['gender'].value_counts().index,
            dataset['gender'].value_counts(),
            hue = ['female', 'male'])


















