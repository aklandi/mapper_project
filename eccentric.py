import sys
import numpy as np

'''
This function calculates the eccentricity of a data set.

param: X, a numpy array of our data points
param: p, a number between 1 and infinity.  
        we use 0 to represent positive infinity, default is 1
returns: a vector of results for eccentric(x)
'''
def eccentric(X, p = 1):
    
    # here we check whether the p given is correct
    # if not, exit function and throw error message
    if p < 1 and p != 0:
        
        sys.exit("choose eccentricity p between 1 and +infty")
        
    n,_ = np.shape(X)
    
    # p = 0 represents the positive infinity
    # this is the max norm
    if p == 0:
        
        # for max comparison, always use smallest number possible 
        # for initialization
        max = np.array([-2e-16 for i in range(n)])
        
        for i in range(n):
            
            current = X[i,:]
            
            for j in range(n):
                
                # if the distance between current point and another point
                # is greater than the current max, make this distance the max
                if np.linalg.norm(current - X[j,:], ord = 2) > max[i]:
                    
                    max[i] = np.linalg.norm(current - X[j,:], ord = 2)
        
        # return this value since we're done
        return max
    
    # for other values of p, do this
    else: 
    
        s = np.array([0 for i in range(n)])
    
        for i in range(n):
            
            current = X[i,:]
            
            for j in range(n):
                
                s[i] += np.linalg.norm(current - X[j,:], ord = 2) ** p
        
        return (s/n) ** (1/p)