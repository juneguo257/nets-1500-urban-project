import networkx as nx
import pickle
import time

start_time = time.time()

# load the graph
with open('graph.pkl', 'rb') as f:
    G = pickle.load(f)

loading_time = time.time()
print(f"graph loading time: {loading_time - start_time:.2f} seconds")

# in-degree for all nodes
in_degrees = G.in_degree()

# make sorted dictionary of nodes and indegrees
node_indegree_dict = {node: degree for node, degree in sorted(in_degrees, key=lambda x: x[1], reverse=True)}

# save dictionary into pickle
with open('node_indegrees.pkl', 'wb') as f:
    pickle.dump(node_indegree_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

end_time = time.time()
print(f"Total runtime: {end_time - start_time:.2f} seconds")
