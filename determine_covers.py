from eccentric import eccentric
from density import density

'''
param: data, a numpy array of data points in topological space X
param: function, a string that indicates filter wanted
param: length, a real number indicating the length of each cover for the range
                of the filter
param: percent, a real number between 0 and 1 indicating the amount of
                overlap between each cover.
returns: a list of inverse covers in X; these covers consist of the points in X
        which map by the filter to covers in the reals
'''
def determine_covers(data, function, length, percent):
    
    if function == "eccentric":
        
        image = eccentric(data)
        
    elif function == "density":
    
        image = density(data)
    
    # if not indicated, we default to projecting the data
    # to its x-coordinate    
    else:
        
        image = data[:,0]
        
    # determine the range of the filter function from points in X
    I = [min(image), max(image)]
    # determine the overlap
    overlap = length*percent
    # intialize the subintervals with the first cover starting at the first point
    sub_interval = [[I[0], I[0] + length]]
    # initialize a list called last which will help determine the stopping point of the while loop
    last = [I[0], I[0]]
    
    # while our last cover does not cover the whole range
    while last[1] < I[1]:
        
        # s will begin within the previous cover
        s = [sub_interval[-1][1] - overlap, sub_interval[-1][1] - overlap + length]
        # append this cover to our list of covers
        sub_interval.append(s)
        
        # update last to be the most recent cover
        last = sub_interval[-1]

    cover = []
    # since we have the covers in the range, we can create the covers in X
    for sub in sub_interval:
        # for each cover in reals, we create a cover in X
        g = []
        ind = 0
        # we go down the vector of values in reals
        for pt in image:
            
            # if the point is contained within a sub interval
            if pt >= sub[0] and pt <= sub[1]:
                
                # then append the original data point to the current cover
                g.append(data[ind, :])
            # increase the index for each point we pass over so 
            # we know the corresponding data point in the original
            # data vector
            ind += 1
            
        # once we've found all points in this cover, we append its corresponding
        # cover in X to a bigger list, unless g is empty, then we do not append
        if g: 
            
            cover.append(g)
        
    return cover