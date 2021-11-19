# girvan newman clustering
import itertools
import time
import networkx as nx
import networkx.algorithms.community as nx_algo
from networkx.algorithms.community import greedy_modularity_communities
from networkx.algorithms.community.centrality import girvan_newman
from sklearn.cluster import SpectralClustering

start_time = time.time()
karate = nx.read_gml("C:\\Users\Kaushal\\Desktop\\karate.gml", label='id')
remove_edges = 7
comp = girvan_newman(karate)
count = 1
print("_____________________________________________")
print("Betweenness-based clustering using the Girvan-Newman")

#generating tuples by removing different edges 
for communities in itertools.islice(comp, remove_edges):
    print("Edge Removal no. {0}".format(count))
    if count == 3:
        modu = list(sorted(c) for c in communities)
    count = count + 1
    print(tuple(sorted(c) for c in communities))
    print(len(communities))

print("Modularity score is:{0}".format(nx_algo.modularity(karate, modu)))
print("_____________________________________________")
print("Modularity Based Clustering")

#implementing modularity for dolphin
community = list(greedy_modularity_communities(karate))
count = 0
for comm in community:
    print(sorted(comm))
print("Modularity score is:{0}".format(nx_algo.modularity(karate, community)))
print("___________________________________")

adj_mat = nx.to_numpy_matrix(karate)

#implementing spectral clustering for dolphin
spec_clust = SpectralClustering(5, affinity='precomputed', n_init=100)
spec_clust.fit(adj_mat)

print('Spectral Clustering')
print(spec_clust.labels_)
# print(modu)
print("___________________________________")
print("time elapsed: {:.2f}s".format(time.time() - start_time))