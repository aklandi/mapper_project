# A Project in Topological Data Analysis: The Mapper Method

In this repository is a set of python programs used to imitate the mapper method described in *Topological Methods for the Analysis of High Dimensional Data Sets and 3D Object Recognition* by Singh, Memoli, and Carlsson in 2007.  The files in this repository are

* *mapper_project.py* = a file containing 3 examples of how to use *my_mapper.py*; outputs a graph in *examples_output.png*
* *my_mapper.py* = the implementation of the mapper method as described in the paper cited above
* *determine_covers.py* = finds the covers for a user selected data set; the covers are open intervals contained in [minimum_value_of_dataset, maximum_value_of_dataset]
* *determine_clusters.py* = clusters the data based on a pre-defined clustering method; these clusters become the vertices of the simplicial complex formed
* *determine_edges.py* = finds the edges between clusters based the overlapping of covers.
* *eccentric.py* = calculates the eccentricity as described in the paper cited above
* *density.py* = calculates the density as described in the paper cited above
* *mapper_test.png* = a result from a positive run of *mapper_project.py*.
* *my_singleLinkage.py* = a method that conducts clustering using single linkage.
