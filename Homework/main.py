import math
import numpy as np
import random
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

from models import model1, model2
from plots import plotHistogram
from simulator import simulate



'''
Run simulator with random data
'''
print('part (a)')
n = 3
m1 = 10 
m2 = 5
sample = 100

a = np.random.rand(1, n) # intercepts
z = np.random.rand(n,m1) # variables with generic coefficients
w = np.random.rand(n,m2) # variables with alternative specific coefficients 
b = np.random.rand(1, m1) # generic coefficients
d = np.random.rand(n,m2) # alternative specific coefficients

results, prob, utilities = simulate(n, z, w, b, d, a, sample)

r = robjects.r
#mlogit = importr('mlogit')

'''
Run Homework 3 Problem 3 part (b)
'''
print('part (b)')
n = 2
sample = 1000

m1 = 1 
m2 = 0


a = np.zeros((1, n))
b = np.reshape(np.array([-1]), (1, m1))
z = np.array(([5], [6]))
w = np.zeros((n,m2))
d = np.zeros((n,m2))

results, prob, utilities = simulate(n, z, w, b, d, a, sample)
np.savetxt('data_frame.txt', results, delimiter='\t', fmt=['%i', '%i']+['%.8f']*(n*(m1+m2)))


# Repeat with b = -0.2
b = np.reshape(np.array([-0.2]), (1, m1))

results, prob, utilities = simulate(n, z, w, b, d, a, sample)
np.savetxt('data_frame2.txt', results, delimiter='\t', fmt=['%i', '%i']+['%.8f']*(n*(m1+m2)))


# Repeat with b = -0.2 and p_0 = 0
n=3
z = np.array(([0], [5], [6]))
a = np.zeros((1, n)) #xxx
w = np.zeros((n,m2)) #xxx
d = np.zeros((n,m2)) #xxx

results, prob, utilities = simulate(n, z, w, b, d, a, sample)
np.savetxt('data_frame3.txt', results, delimiter='\t', fmt=['%i', '%i']+['%.8f']*(n*(m1+m2)))


# Run r script to fit models
rscript = "F:\\Dropbox\\NYU\\2012 Fall\\Choice Models in Operations\\Homework\\Homework2\\problem2_3_b.R"
#results = r.source(rscript, **{'echo': True})

'''
Run Homework 3 Problem 3 part (c)
'''
print('part (c)')
n = 3

m1 = 0 
m2 = 1


a = np.reshape(np.array(([0, 3.584, 1.99])), (1, n))
b = np.zeros((1,m1))
z = np.zeros((n,m1))
w = np.array(([0], [-0.75], [-0.5]))
d = np.array(([0], [6], [5]))


results, prob, utilities = simulate(n, z, w, b, d, a, sample)
np.savetxt('data_frame4.txt', results, delimiter='\t', fmt=['%i', '%i']+['%.8f']*(n*(m1+m2)))


'''
Run Homework 3 Problem 3 part (d)
'''
print('part (d)')
n = 3
m1 = 0  # no variables with generic coefficients

a = np.reshape(np.array(([0, 3.584, 1.99])), (1, n)) # intercepts
b = np.zeros((1,m1))
z = np.zeros((n,m1))
w = np.array(([0], [-0.75], [-0.5])) # alternative specific variable coefficients

trainingSets = 100
errors = np.empty([trainingSets, 2]) 
for i in range(trainingSets):
    # sample each price independently and uniformly at random from the interval [0, 10]
    pblue = random.uniform(1, 10)
    pred = random.uniform(1, 10)
    d = np.array(([0], [pblue], [pred]))
    # ground truth model
    results, prob, utilities = simulate(n, z, w, b, d, a, sample)
    # fit model 1
    model1Estimate = model1(results, n, pblue, pred) #xxx
    # fit model 2
    model2Estimate = model2(results, n, pblue, pred) #xxx
    # compute sales
    trueShare = math.exp(utilities[0,1])/(1 + math.exp(utilities[0,1]))
    model1Share = math.exp(float(model1Estimate[1]))/(1 + math.exp(float(model1Estimate[1])))
    model2Share = math.exp(float(model2Estimate[1]))/(1 + math.exp(float(model2Estimate[1])))
    # compute errors
    errors.itemset((i, 0), math.fabs(trueShare-model1Share)/trueShare)
    errors.itemset((i, 1), math.fabs(trueShare-model2Share)/trueShare)

# plot histogram
plotHistogram(errors[:,0], errors[:,1], label1=r'Model 1: $V_j = \beta p_j$', label2=r'Model 2: $V_j = \delta_j p_j$', title='Histogram of relative errors', xlabel='Value', ylabel='Frequency')


print('Finished!')