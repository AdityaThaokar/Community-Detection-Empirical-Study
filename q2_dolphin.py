import itertools
import time
import networkx.algorithms.community as nx_algo
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities
from networkx.algorithms.community.centrality import girvan_newman
from sklearn.cluster import SpectralClustering

start_time = time.time()
dolphin = nx.read_gml("C:\\Users\Kaushal\\Desktop\\dolphins.gml", label='id')
remove_edges = 7
comp = girvan_newman(dolphin)
count = 1
print("_____________________________________________")
print("Betweenness-based clustering using the Girvan-Newman")
for communities in itertools.islice(comp, remove_edges):
    print("Edge Removal no. {0}".format(count))
    if count == 3:
        modu = list(sorted(c) for c in communities)
    count = count + 1
    print(tuple(sorted(c) for c in communities))
    print(len(communities))

print("Modularity score is:{0}".format(nx_algo.modularity(dolphin, modu)))
print("_____________________________________________")
print("Modularity Based Clustering")
community = list(greedy_modularity_communities(dolphin))
count = 0
for comm in community:
    print(sorted(comm))
print("Modularity score is:{0}".format(nx_algo.modularity(dolphin, community)))
print("___________________________________")

adj_mat = nx.to_numpy_matrix(dolphin)

spec_clust = SpectralClustering(5, affinity='precomputed', n_init=100)
spec_clust.fit(adj_mat)

print('Spectral Clustering')
print(spec_clust.labels_)
# print(modu)
print("___________________________________")
print("time elapsed: {:.2f}s".format(time.time() - start_time))