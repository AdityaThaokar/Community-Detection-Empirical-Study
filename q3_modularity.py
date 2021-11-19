# Modularity based clustering
import itertools
import time
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
import networkx.algorithms.community as nx_algo
import argparse


# Read input file path from terminal
parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True)
args = parser.parse_args()
start_time = time.time()

# Apply modularity-based clustering (modularity maximization) on the input graph
network_graph = nx.read_gml(args.path, label='id')
community = list(greedy_modularity_communities(network_graph))
print("_____________________________________________")
print("Modularity Based Clustering")
for cluster in community:
    print(sorted(cluster))

# print Modularity score and time interval
print("Modularity score is:{0}".format(nx_algo.modularity(network_graph, community)))
print("___________________________________")
print("time interval: {:.2f}s".format(time.time() - start_time))


