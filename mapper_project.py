'''
In this script, the mapper method from my_mapper.py is used on three common data sets.  
The script will produce graphs, in examples_output.png
'''

import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_circles
from sklearn.datasets.samples_generator import make_blobs

from my_mapper import my_mapper

# moons example, works best with eps = 0.2, r = 5
X1,y = make_moons(n_samples = 400, noise = 0.05, random_state = 5)

fig = plt.figure()

plot1 = fig.add_subplot(3,2,1)
plot1.scatter(X1[:,0], X1[:,1], marker = "o")
plot1.set_title("Original Data")

e1 = my_mapper(X1, function = "default", length = 0.75, percent = 0.5, cluster_method = ["dbscan", 0.2, 5])


plot2 = fig.add_subplot(3,2,2)
# for each element in our list of edges
for e in e1:
    
    # plot a node for the first vertex
    plot2.plot([e[0][0]],[e[0][1]],marker = "o", markersize = 20, c = "blue")
    # plot a node for the second vertex
    plot2.plot([e[1][0]],[e[1][1]],marker="o", markersize = 20, c = "blue")
    # plot a line connecting these two nodes
    plot2.plot([e[0][0],e[1][0]],[e[0][1],e[1][1]], linestyle = "-", c = "lightgray")
            
plot2.set_ylim([-1,2])
plot2.set_xlim([-1,8])

# blobs example, works best with eps = 0.3, r = 10
centers = [[1,1],[-1,-1],[1,-1]]
X2, labels_true = make_blobs(n_samples = 750, centers = centers, cluster_std = 0.4, random_state = 0)

plot3 = fig.add_subplot(3,2,3)
plot3.scatter(X2[:,0], X2[:,1], marker = "o")

e2 = my_mapper(X2, function = "eccentric", length = 0.75, percent = 0.25, cluster_method = ["dbscan", 0.3, 10])

#plot the data
plot4 = fig.add_subplot(3,2,4)
# for each element in our list of edges
for e in e2:
    
    # plot a node for the first vertex
    plot4.plot([e[0][0]],[e[0][1]],marker = "o", markersize = 20, c = "blue")
    # plot a node for the second vertex
    plot4.plot([e[1][0]],[e[1][1]],marker="o", markersize = 20, c = "blue")
    # plot a line connecting these two nodes
    plot4.plot([e[0][0],e[1][0]],[e[0][1],e[1][1]], linestyle = "-", c = "lightgray")

plot4.set_ylim([-5,5])
plot4.set_xlim([-5,5])

# enclosed circles example, works best with eps = 0.2, r = 5
X3, y = make_circles(n_samples = 750, noise = 0.05, factor = 0.5)

plot5 = fig.add_subplot(3,2,5)
plot5.scatter(X3[:,0], X3[:,1], marker = "o")

e3 = my_mapper(X3, function = "default", length = 0.75, percent = 0.5, cluster_method = ["dbscan", 0.2, 5])
#plot the data
plot6 = fig.add_subplot(3,2,6)
# for each element in our list of edges
for e in e3:
    
    # plot a node for the first vertex
    plot6.plot([e[0][0]],[e[0][1]],marker = "o", markersize = 20, c = "blue")
    # plot a node for the second vertex
    plot6.plot([e[1][0]],[e[1][1]],marker="o", markersize = 20, c = "blue")
    # plot a line connecting these two nodes
    plot6.plot([e[0][0],e[1][0]],[e[0][1],e[1][1]], linestyle = "-", c = "lightgray")
    
plot6.set_ylim([-2,2])
plot6.set_xlim([-2,2])

fig.savefig("examples_output.png")

