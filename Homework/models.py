import numpy as np
from sympy import solve, Symbol, exp, simplify
from sympy.solvers import nsolve
import scipy
import scipy.optimize
 
 
''' 
#xxx update for arbitrary dimensions
def model1_v1(data, n, price1, price2):
    sample = float(data.shape[0])
    shares = np.histogram(data[:,1].astype('float32').view('int32'), bins=n)[0]/sample
    b = Symbol('b')
    eq = (shares[1]*price1 + shares[2]*price2 - (price1*exp(b*price1)+price2*exp(b*price2))/(1+exp(b*price1)+exp(b*price2)))
    #simpleEq = simplify(eq)
    sl = nsolve(eq, b, -0.2, rational=True, manual=True, implicit=True, simplify=True, numerical=True)
    #print(sl)
    V = np.array([0, sl*price1, sl*price2])
    return V 
'''


#xxx update for arbitrary dimensions
def model1(data, n, price1, price2):
    sample = float(data.shape[0])
    shares = np.histogram(data[:,1], bins=np.arange(1.0, n+2.0))[0]/sample
    def f(b):
        y = shares[1]*b*price1 + shares[2]*b*price2 - np.log(1 + np.exp(b*price1) + np.exp(b*price2))
        return y
    sl = scipy.optimize.fsolve(f, 0.0) # xxx    
    #print('prices: 0\t' + str(price1) + '\t' + str(price2))
    #print('shares: ' + str(shares[0]) + '\t' + str(shares[1])  + '\t' + str(shares[2]))
    #print('b = ' + str(sl[0]))
    V = np.array([0, sl*price1, sl*price2])
    return V, float(sl) 


# Same results with model2() but simpler implementation
def model2Simple(data, n, price1, price2):
    sample = float(data.shape[0])
    shares = np.histogram(data[:,1], bins=np.arange(1.0, n+2.0))[0]/sample
    V = np.array([0, np.log(shares[1]/(shares[1]+shares[2])), np.log(shares[2]/(shares[1]+shares[2]))])
    return V  


#xxx update for arbitrary dimensions
def model2(data, n, price1, price2):
    sample = float(data.shape[0])
    shares = np.histogram(data[:,1], bins=np.arange(1.0, n+2.0))[0]/sample
    x = Symbol('x')
    y = Symbol('y')
    eq1 = (shares[1]*price1 - (price1*x)/(1+x+y))
    eq2 = (shares[2]*price2 - (price2*y)/(1+x+y))
    sl = nsolve((eq1, eq2), (x, y), (0.5, 0.5), set=True, rational=True, manual=True, implicit=True, simplify=True, numerical=True)
    #print('prices: 0\t' + str(price1) + '\t' + str(price2))
    #print('shares: ' + str(shares[0]) + '\t' + str(shares[1])  + '\t' + str(shares[2]))
    #print('d = ' + str(sl[0]) + '\t' + str(sl[1]))
    V = np.array([0, sl[0], sl[1]])
    return V  
