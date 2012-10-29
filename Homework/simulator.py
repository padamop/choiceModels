import numpy as np 


def random_pick(choices, probs):
    '''
    >>> a = ['Hit', 'Out']
    >>> b = [.3, .7]
    >>> random_pick(a,b)
    '''
    cutoffs = np.cumsum(probs)
    idx = cutoffs.searchsorted(np.random.uniform(0, cutoffs[-1]))
    return choices[idx]

def choiceProbabilities(utilities):
    probabilities = np.exp(utilities)/np.sum(np.exp(utilities))
    return probabilities


def simulate(NumberOfAlternatives, variablesWithGenericCoefficients, variablesWithAlternativeSpecific, genericCoefficients, alternativeSpecificCoefficients, intercepts, sample):
    n = NumberOfAlternatives
    a = intercepts # 1 x n
    z = variablesWithGenericCoefficients # n x m1
    w = variablesWithAlternativeSpecific # n x m2
    b = genericCoefficients # 1 x m1
    d = alternativeSpecificCoefficients # n x m2
    sample = sample
    
    '''
    Check dimensions of arrays
    '''
    if ((n != a.shape[1]) or (n != z.shape[0]) or (n != w.shape[0]) or (n != z.shape[0]) or (n != d.shape[0])):
        print('Check input data (n dimension)')
        
    if (z.shape[1] != b.shape[1]):
        print('Check input data (m1 dimension)')
        
    if (w.shape[1] != d.shape[1]):
        print('Check input data (m2 dimension)')
    
    #Set variables    
    m1 = z.shape[1]
    m2 = w.shape[1]
    choices = np.arange(1,n+1)
    
    # Compute utilities
    V = a + np.dot(b, z.T) + np.sum(np.multiply(d, w), axis=1)
    # Compute probabilities 
    probs = choiceProbabilities(V) 
    
    results = np.empty([sample, 2+n*(m1+m2)])        
    attributes = np.ravel(np.hstack((z,w))) # n(m1+m2) elements
    
    
    for i in range(sample):
        choice = random_pick(choices, probs) 
        results[i, :] = np.concatenate(([int(i+1), int(choice)], attributes), axis=1)
    
    return results, probs, V

