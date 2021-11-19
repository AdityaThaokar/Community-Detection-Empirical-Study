# girvan newman clustering
import itertools
import time
import networkx as nx
import networkx.algorithms.community as nx_algo
from networkx.algorithms.community.centrality import girvan_newman
import argparse

# Read input file path from terminal
parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, required=True)
args = parser.parse_args()
start_time = time.time()

# Apply girvan newman on the input graph
network_graph = nx.read_gml(args.path, label='id')
remove_edges = 7
commu = girvan_newman(network_graph)
count = 1
print("_____________________________________________")
print("Betweeness-based clustering using the Girvan-Newman")
for communities in itertools.islice(commu, remove_edges):
    print("_____________________________________________")
    print("Edge Removal no. {0}".format(count))
    if count == 5:
        modu = list(sorted(c) for c in communities)
    count = count + 1
    print(tuple(sorted(commu) for commu in communities))
    print("Total Clusters:{0}".format(len(communities)))

# print Modularity score and time interval
print("Modularity score is:{0}".format(nx_algo.modularity(network_graph, modu)))
print("_____________________________________________")
print("time interval: {:.2f}s".format(time.time() - start_time))

