from scipy.cluster.hierarchy import linkage, fcluster

'''
This function clusters data according to the single linkage method

param: data, a numpy array which contains the data we want to cluster
returns: a cluster assignment using the single linkage clustering method
'''
def my_singleLinkage(data):
    
    # creates the linkage matrix -- contains the clustering at each level 
    # uses the single linkage method
    # default metric is Euclidean
    Z = linkage(data, method = "single")
    
    # finds the cluster assignments based on the linkage matrix,
    # I give 2 clusters as default, and uses the max cluster criterion
    assignment = fcluster(Z, 2, criterion = "maxclust")
    
    # dendrogram(Z, truncate_mode = "lastp", p = 12, leaf_rotation = 90, leaf_font_size = 12, show_contracted = True)
    
    
    return assignment