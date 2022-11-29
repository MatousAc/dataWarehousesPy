from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist  
import numpy as np
import matplotlib.pyplot as plt

# Creating the data
x1 = np.array([3, 1, 1, 2, 1, 6, 6, 6, 5, 6, 7, 8, 9, 8, 9, 9, 8])
x2 = np.array([5, 4, 5, 6, 5, 8, 6, 7, 6, 7, 1, 2, 1, 2, 3, 2, 3])
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
print(X)
  
# Visualizing the data
plt.plot()
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('Dataset')
plt.scatter(x1, x2)
plt.show()

distortions = []
inertias = []
mapping1 = {}
mapping2 = {}


for k in range(1, 10):
  km = KMeans(n_clusters=k).fit(X)
  km.fit(X)

  distortions.append(sum(np.min(cdist(X, km.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
  inertias.append(km.inertia_)

  mapping1[k] = sum(np.min(cdist(X, km.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0]
  mapping2[k] = km.inertia_

for key, val in mapping1.items():
  print(f'{key} : {val}')

plt.plot(K, distortions, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Distortion')
plt.title('The Elbow Method using Distortion')
plt.show()
