import tsne as TSNE
import numpy as np
import matplotlib.pyplot as plt 

X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])

labels = np.array([1,2,3,4])
Y = TSNE.tsne(X, 2, 50, 20.0)
plt.scatter(Y[:,0], Y[:,1], 20, labels)
plt.show()

