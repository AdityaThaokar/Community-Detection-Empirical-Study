import networkx as nx
dolphin = nx.read_gml("C:\\Users\Kaushal\\Desktop\\dolphins.gml")
print("-----------Dolphins Statistics -----------")
print(nx.info(dolphin))
print("Avg path length : ", nx.average_shortest_path_length(dolphin))
average = nx.average_clustering(dolphin)
print("Avg clustering coefficient : ", average)
print("-----------------------------------------")



print("-----------Karate Club Statistics -----------")
karate = nx.read_gml("C:\\Users\Kaushal\\Desktop\\karate.gml", label='id')
print(nx.info(karate))
print("Avg path length : ", nx.average_shortest_path_length(karate))
average = nx.average_clustering(karate)
print("Avg clustering coefficient : ", average)
print("-----------------------------------------")


print("-----------Jazz Statistics -----------")
"""
f = open("C:\\Users\Kaushal\\Desktop\\jazz.net","r")
lines = f.readlines()
f.close()
nf = open("C:\\Users\Kaushal\\Desktop\\jazz.net","w")
for i in lines:
    if i != lines[0] and i != lines[1] and i != lines[2]:
        nf.write(i)
nf.close()
"""
jazz = nx.read_weighted_edgelist("C:\\Users\Kaushal\\Desktop\\jazz.net")
print(nx.info(jazz))
print("Avg path length : ", nx.average_shortest_path_length(jazz))
average = nx.average_clustering(jazz)
print("Avg clustering coefficient : ", average)
print("-----------------------------------------")
