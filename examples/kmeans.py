import numpy as np
from sklearn.datasets import make_blobs
import os

from mla.kmeans import KMeans


def kmeans_example(plot=False):
    X, y = make_blobs(centers=4, n_samples=500, n_features=2, shuffle=True, random_state=42)
    clusters = len(np.unique(y))
    k = KMeans(K=clusters, max_iters=150, init="++")
    k.fit(X)
    k.predict()

    if plot:
        save_dir = '/var/app/'
        save_path = os.path.join(save_dir, 'kmeans.PNG')
        k.plot(save_path=save_path)

if __name__ == "__main__":
    kmeans_example(plot=True)

