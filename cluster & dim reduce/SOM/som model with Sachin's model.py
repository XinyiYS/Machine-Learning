import Sachin_som_with_TF as som
import matplotlib
import matplotlib.pylab as plt
import numpy as np
from SOM import DPP
from mpl_toolkits.axes_grid.anchored_artists import AnchoredText

dpp = DPP.DPP(data_dir='dataOut.csv')
data, chosen_attributes = dpp.get_data()

n_features = sum(len(v) for v in chosen_attributes.values())
print('no features is :', n_features)

# initialize the som with size, n_features, and n_itearations
som = som.SOM(15, 15, n_features,  100)
som.train(data)
print('training is done')

# Map colours to their closest neurons
mapped = np.array(som.map_vects(data))

# Cluster the points accordingly
centroids, labels = som.cluster(mapped, n_clusters=7) #n_cluster = 5 by default

# Plotting the clusters
plt.suptitle("Driving data Numbered clusters SOM",)
x = mapped[:, 0]
y = mapped[:, 1]
ax = plt.subplot(111)
colors = list(matplotlib.colors.cnames.values())
for i, label in enumerate(labels):
    plt.scatter(x[i],y[i],alpha=0.7, c=colors[labels[i]])
    plt.annotate(labels[i], (x[i], y[i]), color='k')

# include the chosen attributes in the graph
textBoxHeight = 1.0+0.1*(len(chosen_attributes.keys())-1)
# label = "Chosen attributes are: "
for i, key in enumerate(chosen_attributes.keys()):
    attributes = " ".join(list(chosen_attributes[key]))
    text = key + ":" + attributes
    ax = plt.subplot(111)
    ann = AnchoredText(text,
                       loc=1, prop=dict(size=8), frameon=True,
                       bbox_to_anchor=(1.85,1.0-i*0.1),
                       bbox_transform=ax.transAxes
                       )
    ann.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(ann)

# display the labeled centroids
centroids = np.array(centroids)
plt.scatter(centroids[:,0],centroids[:,1],c='r',s=20)

# annotate the centroids if neended
# for centroid in centroids:
#     plt.annotate("centroid", (centroid[0],centroid[1]))
plt.show()

def show_plot(centroids,show_attributes=False,show_centroids=True,color_dist=False,size_dist=False):
    if show_attributes:
        # include the chosen attributes in the graph
        attributes = " ".join(chosen_attributes)
        ax = plt.subplot(111)
        ann = AnchoredText("Chosen attributes are: " + attributes,
                           loc=3, prop=dict(size=8), frameon=True,
                           bbox_to_anchor=(0., 1.),
                           bbox_transform=ax.transAxes
                           )
        ann.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
        ax.add_artist(ann)

    if show_centroids:
        centroids = np.array(centroids)
        x = centroids[:, 0]
        y = centroids[:, 1]
        plt.scatter(x, y)
        for i, centroid in centroids:
            plt.annotate("centroid", centroid)
        pass

    if color_dist:
        pass

    if size_dist:
        pass

    plt.show()
print('plot is shown')
plt.show()


