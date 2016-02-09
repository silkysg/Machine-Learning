import numpy as np 
from matplotlib import pyplot as py 

def GradientDescent(x, y, theta, alpha, iterations):
	m = len(y)
	for i in range(iterations):
		h_theta = np.dot(theta,np.transpose(x)) #Hypothesis
		cost_theta = sum(np.transpose(np.square(h_theta-np.transpose(y))))/(2*m) #Cost after each iteration
		step = np.dot(h_theta-np.transpose(y),x) #Step at each iteration which gets multiplied by learning rate alpha
		theta = theta - ((alpha*step)/m) #Updating paramters    

	return theta, h_theta, cost_theta



#Txt file contains data for profits and populations from various cities of a food truck
print('Reading data from txt..')
data = np.loadtxt("Machine_Learning/machine-learning-ex1/ex1/ex1data1.txt", delimiter=",", unpack=False)
print('done..')

x = data[:,0] #Population
y = data[:,1] #Profit

#Plotting data 
py.plot(x,y,'.')
py.xlabel('Population of City in 10,000s')
py.ylabel('Profit in $10,000s')
py.show()


#Initializing parameters to be zeros
theta = np.zeros((1,2))

#Learning rate
alpha = 0.01

#Number of iterations for optimization
iterations = 1500

#Adding a column of ones to take into account the intercept
x = np.c_[np.ones(len(x)),np.array(x)]
y = np.array(y)

result = GradientDescent(x, y, theta, alpha, iterations)
print('Final parameters : ', result[0])
print('Final cost: ', result[2])




