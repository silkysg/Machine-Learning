import pandas as pd 
from matplotlib import pyplot as plt
import math as mt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

#Reading data from csv and saving it into a dataframe
data = pd.read_csv("Python_Scripts/knn_data.csv")

#Extracting feature matrix into X and target class values into y
X = data.as_matrix(['Device', 'Attempts'])
y = data.as_matrix(['Genuine'])

#Creating separate dataframes for 1 and 0 classes
pos_data = data.loc[data.Genuine == 1]
neg_data = data.loc[data.Genuine == 0]

#Plotting the data to visualize classes
plt.plot(pos_data['Device'], pos_data['Attempts'], '+')
plt.plot(neg_data['Device'], neg_data['Attempts'], 'o')
plt.axis([0,10,0,10])
plt.xlabel('Number of devices')
plt.ylabel('Number of attempts to log in')
plt.show()

#Creating an instance of KNN classifier and fitting it on data
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

devices = 3
attempts = 5
print(neigh.predict([[devices,attempts]]))