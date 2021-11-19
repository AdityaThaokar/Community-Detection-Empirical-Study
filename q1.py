import networkx as nx

print("-----------Dolphins Statistics -----------")
#reading the dolphin gml
dolphin = nx.read_gml("C:\\Users\Aditya\\Desktop\\dolphins.gml")

#getting the info about no. of nodes and edges
print(nx.info(dolphin))
print("Avg path length : ", nx.average_shortest_path_length(dolphin))
average = nx.average_clustering(dolphin)
print("Avg clustering coefficient : ", average)
print("-----------------------------------------")



print("-----------Karate Club Statistics -----------")
#reading the karate gml
karate = nx.read_gml("C:\\Users\Aditya\\Desktop\\karate.gml", label='id')

#getting the info about no. of nodes and edges
print(nx.info(karate))
print("Avg path length : ", nx.average_shortest_path_length(karate))
average = nx.average_clustering(karate)
print("Avg clustering coefficient : ", average)
print("-----------------------------------------")



print("-----------Jazz Statistics -----------")
#reading the Jazz gml
jazz = nx.read_weighted_edgelist("C:\\Users\Aditya\\Desktop\\jazz.net")

#getting the info about no. of nodes and edges
print(nx.info(jazz))
print("Avg path length : ", nx.average_shortest_path_length(jazz))
average = nx.average_clustering(jazz)
print("Avg clustering coefficient : ", average)
print("-----------------------------------------")
