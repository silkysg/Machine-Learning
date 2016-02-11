import pandas as pd 
#import ggplot as gp 
from matplotlib import pyplot as plt
import math as mt
import numpy as np
#import scipy as sc
from scipy.optimize import minimize

def sigmoid(z):
	output = []
	for i in range(len(z)):
		denominator = 1 + mt.exp(-1*(z[i]))
		output.append(1/denominator)
	return output			

def computeCost(theta, x, y):
	h_theta = sigmoid(np.transpose(np.dot(theta,np.transpose(x))))
	cost = 0
	m = len(h_theta)
	for i in range(len(h_theta)):	
		cost = cost + (-1*y[i]*mt.log(h_theta[i]))+(-1*(1-y[i])*mt.log(1-h_theta[i]))
	cost = cost/m
	return cost

def computeGradient(x,y,theta):
	h_theta = sigmoid(np.transpose(np.dot(theta,np.transpose(x))))
	gradient = []
	m = len(h_theta)
	for i in range(len(theta)):
			g = np.dot(h_theta-y,x)/m
			gradient.append(g)
	return gradient		

def gradientDescent(x,y,theta, alpha, iterations):
	for i in range(iterations):
		h_theta = sigmoid(np.transpose(np.dot(theta,np.transpose(x))))
		cost = computeCost(x,y,theta)
		step = computeGradient(x,y,theta)
		theta = theta - step
	return theta

data = pd.read_csv("Machine_Learning/machine-learning-ex2/ex2/ex2data1.txt")

pos_data = data.loc[data.Admission == 1]
neg_data = data.loc[data.Admission == 0]

'''
plt.plot(pos_data['Exam1'], pos_data['Exam2'], '+')
plt.plot(neg_data['Exam1'], neg_data['Exam2'], 'o')
plt.xlabel('Exam1 Score')
plt.ylabel('Exam2 Score')
plt.show()
'''

x  = np.c_[np.ones(len(data['Exam1'])),data.as_matrix(['Exam1', 'Exam2'])]
y = data['Admission']
alpha = 0.01
iterations = 2
theta = np.zeros((1,3))
#print(computeCost(x,y,theta))
#print(computeGradient(x,y,theta))

#res = sc.fmin(computeCost(theta, x, y), theta)
res = minimize(computeCost(theta, x, y), theta, method='nelder-mead', options={'xtol': 1e-8, 'disp': True})
print(res)
#print(x)
#print(sigmoid(np.array([1,0])))

#print(pos_data['Exam1'])