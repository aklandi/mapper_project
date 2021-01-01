'''
The clusters are considered the vertices of the simplicial complex being built.
This function will connect vertices with an edge if they are under the same cover.

param: clusters, a list of clusters from each cover
result: a list of edges, each element contains an id [num cover, num cluster] so we
            have an idea of where the similarities are located
'''
def determine_edges(clusters):
    
    edges = []
    vertices = []
    # since clusters is first divided by covers,
    # this will give the number of covers
    length = len(clusters)
    
    # for each cover
    for l in range(length):
        
        current = clusters[l]
        
        # we'll compare to the other covers
        for i in range(l+1,length):
            
            next = clusters[i]
            
            # len(current) is how many clusters are within the current cover
            for j in range(len(current)):
                
                # x is the current cluster within the current cover
                x = current[j]
                vertices.append([l,j])
                
                #len(next) is how many clusters are within the following covers
                for k in range(len(next)):
                    
                    # y is the current cluster within the following cover
                    y = next[k]
                    vertices.append([i,k])
                    # resets for each cluster we explore
                    count = 0
                    
                    # for the points in x
                    for pt in x:
                        
                        # if the point is also in y
                        if pt in y:
                            
                            # increase the coutn
                            count += 1
                            
                    # if there is at least one point in both x and y
                    if count > 0:
                        
                        # append the edge [cover l, cluster j] to [cover i, cluster k]
                        edges.append([[l,j],[i,k]])

    return edges
    