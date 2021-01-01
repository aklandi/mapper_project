import numpy as np
from sklearn.cluster import DBSCAN, KMeans
from my_singleLinkage import my_singleLinkage

'''
This function determines the clusters of data points 

param: data, a data array of the points in topological space X
param: covers, a list of the covers, and each element contains a list of
            the points from data under each cover
param: cluster_method, a string indicating which clustering method is preferred
            with a choice of dbscan, kmeans, and single linkage.
returns: clusters, a list of the clusters under each cover
'''
def determine_clusters(data, covers, cluster_method):
    
    # create an empty list to contain the clusters within each cover
    clusters = []
    
    if cluster_method[0] == "dbscan":
        
        # for each of the covers
        for cover in covers:
            
            # turn it into an array since the method assumes array
            cover = np.array(cover)
            
            # create a list for clusters of this particular cover
            c = []
            # get the assignments for each data point
            db = DBSCAN(eps = cluster_method[1], min_samples = cluster_method[2]).fit(cover)
            # find the number of clusters
            num = len(np.unique(db.labels_))
            
            # then, separate the data of this cover into their clusters
            for i in range(num):
                
                c.append(cover[db.labels_ == i,:])
                
            clusters.append(c)
            
    elif cluster_method[0] == "kmeans":
        
        # for each of the covers
        for cover in covers:
            
            # turn it into an array since the method assumes array
            cover = np.array(cover)
            
            # create a list for clusters of this particular cover
            c = []
            # get the assignments for each data point
            km = KMeans(n_clusters = cluster_method[1]).fit(cover) 
            # find the number of clusters
            num = len(np.unique(km))
            
            # then, separate the data of this cover into their clusters
            for i in range(num):
                
                c.append(cover[km == i,:])
                
            clusters.append(c)
        
    else:
        
        # for each of the covers
        for cover in covers:
            
            # turn it into a narray since the method assumes array
            cover = np.array(cover)
            
            # create a list for clusters of this particular cover
            c = []
            # get the assignments for each data point
            c_assign = my_singleLinkage(cover)
            # find the number of clusters
            num = len(np.unique(c_assign))
            
            # then, separate the data of this cover into their clusters
            for i in range(num):
                
                c.append(cover[c_assign == i, :])
                
            clusters.append(c)
        
    return clusters