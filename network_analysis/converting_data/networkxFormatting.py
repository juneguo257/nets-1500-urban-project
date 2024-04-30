import networkx as nx
import pickle
import time

start_time = time.time()

# load collected data
try:
    with open('combinedOUT.pkl', 'rb') as file:
        adjacency_list = pickle.load(file)

G = nx.DiGraph()

# add edges into networkx graph
for source, targets in adjacency_list.items():
    for target in targets:
        G.add_edge(source, target)

loading_time = time.time()
print(f"graph loading time: {loading_time - start_time:.2f} seconds")

# save graph into pickle file
with open('graph.pkl', 'wb') as f:
    pickle.dump(G, f, pickle.HIGHEST_PROTOCOL)

end_time = time.time()
print(f"total runtime: {end_time - start_time:.2f} seconds")
