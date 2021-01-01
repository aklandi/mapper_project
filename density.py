import numpy as np

'''
The function calculates the density for a data set.

param: data, a numpy array of input values we want to find the density 
param: epsilon, a number, default 0.2, which controls "smoothness"

returns: an array of real values for density(x)
'''
def density(data, eps = 0.2):
    
    n,_ = np.shape(data)
    
    s = np.array([0.0 for i in range(n)])
    
    for i in range(n):
        
        # we look at each data point in order to calculate its value
        current = data[i,:]
        
        temp = 0
        # calculate the distance of the current point to each other point, 
        # even itself since that is only 0
        for j in range(n):
            
            temp += np.exp(( -( np.linalg.norm(current - data[j,:], ord = 2)) ** 2)/eps)
        
        s[i] = temp    
    
    # then calculate the area under the "curve" so that
    # the output values result in area under "curve" as 1        
    area = np.trapz(s)

    return s/area        
    