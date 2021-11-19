# spectral clustering
import networkx as nx
import time
from sklearn.cluster import SpectralClustering
import argparse

# Read input file path from terminal
parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True)
args = parser.parse_args()
start_time = time.time()

# Apply spectral clustering on the input graph
network_graph = nx.read_gml(args.path, label='id')
start_time = time.time()
print("___________________________________")
adj_mat = nx.to_numpy_matrix(network_graph)

spec_clust = SpectralClustering(3, affinity='precomputed', n_init=100)
spec_clust.fit(adj_mat)

print('Spectral Clustering')
print(spec_clust.labels_)
print("___________________________________")
print("time interval: {:.2f}s".format(time.time() - start_time))
