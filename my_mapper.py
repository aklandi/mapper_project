'''
The Mapper method based on descriptions in Topological Methods for the Analysis of High Dimensional Data Sets and 3D Object Recognition
by Singh, Memoli, and Carlsson, 2007

The mapper method outputs a simplicial complex determined by clusters, covers, and filter functions.
If chosen, the mapper method will display a graph for the simplicial complex.
'''

from determine_covers import determine_covers
from determine_clusters import determine_clusters
from determine_edges import determine_edges
    
def my_mapper(data, function, length, percent, cluster_method):

    covers = determine_covers(data, function, length, percent)
    clusters = determine_clusters(data, covers, cluster_method)
    edge = determine_edges(clusters)

    return edge