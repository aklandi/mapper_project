import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

from my_mapper import my_mapper

# read in the data from csv as pandas data frame
data = pd.read_csv("./steam-200k.csv")
# separate the data into purchased and play since the same user can be listed twice for the same game
# once for the purchase and again for the play time
D1 = data[data['behavior-name'] == "purchase"]
D2 = data[data['behavior-name'] == "play"]
# I decided to merge the two data frames so that a user has its own row per game
D = pd.merge(D1, D2, how = "outer", on = ["user-id", "game-title"])
D["value_y"].fillna(0, inplace = True)
# Now we groupby game in order to tally up the average play time per game.
grouped_by_game = pd.DataFrame({"mean_play_time": D.groupby(by = "game-title")["value_y"].mean()}).reset_index()
# change the data to a numpy array so that the mapper method will accept the data
X = np.array([grouped_by_game['mean_play_time']]).T

fig, axs = plt.subplots(1,2)
axs[0].scatter(np.arange(np.shape(X)[0]), X[:,0], marker = "x")
axs[0].set_title("Original Data")

# # we want to now apply the mapper method to the mean_play_time and find the simplicial complex of the games.
edges = my_mapper(X, function = "default", length = 0.75, percent = 0.5, cluster_method = ["dbscan", 0.001, 20])
print(edges)

for e in edges:
        
    # plot a node for the first vertex
    axs[1].plot([e[0][0]],[e[0][1]],marker = "o", markersize = 20, c = "blue")
    # plot a node for the second vertex
    axs[1].plot([e[1][0]],[e[1][1]],marker="o", markersize = 20, c = "blue")
    # plot a line connecting these two nodes
    axs[1].plot([e[0][0],e[1][0]],[e[0][1],e[1][1]], linestyle = "-", c = "lightgray")
            
axs[1].set_xlim(-1,5)
axs[1].set_title("The Simplicial Complex")
plt.savefig("blah.png")