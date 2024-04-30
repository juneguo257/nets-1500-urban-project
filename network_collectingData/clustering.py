import networkx as nx
import pickle
from cdlib import algorithms
import time

start_time = time.time()

# load  graph uncomment for scc
# with open('largest_scc.pkl', 'rb') as f:
#     adjacency_data = pickle.load(f)
# 
# G =  nx.adjacency_graph(adjacency_data)

# load entire graph
with open('graph.pkl', 'rb') as f:
    G = pickle.load(f)


loading_time = time.time()
print(f"Graph loading time: {loading_time - start_time:.2f} seconds")

# calc clustering coefficients for each node
clustering_coeffs = nx.clustering(G)

# make sorted dictionary
clustering_dict = {node: coeff for node, coeff in sorted(clustering_coeffs.items(), key=lambda x: x[1], reverse=True)}

# save dictionary into pickle file
with open('node_clustering_coeffs.pkl', 'wb') as f:
    pickle.dump(clustering_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

# print top 50 nodes
print("top 50 nodes by clustering coefficient:")
for i, (node, coeff) in enumerate(clustering_dict.items()):
    if i < 50:
        print(f"node {node} has a clustering coefficient of {coeff}")

end_time = time.time()
print(f"total runtime: {end_time - start_time:.2f} seconds")
