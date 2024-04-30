import networkx as nx
import pickle
import time

start_time = time.time()

# load graph
with open('graph.pkl', 'rb') as f:
    G = pickle.load(f)

loading_time = time.time()

# find largest wcc and save it
largest_wcc = max(nx.weakly_connected_components(G), key=len)
largest_wcc_subgraph = G.subgraph(largest_wcc).copy()

# find largest scc and save it
largest_scc = max(nx.strongly_connected_components(G), key=len)
largest_scc_subgraph = G.subgraph(largest_scc).copy()

# find all isolated nodes
isolated_nodes = list(nx.isolates(G))

# printing
print("largest wcc:")
print("# nodes:", largest_wcc_subgraph.number_of_nodes())
print("# edges:", largest_wcc_subgraph.number_of_edges())

print("largest scc:")
print("# nodes:", largest_scc_subgraph.number_of_nodes())
print("# edges:", largest_scc_subgraph.number_of_edges())

print("# isolated nodes:", len(isolated_nodes))

# save components into pickle files
with open('largest_wcc.pkl', 'wb') as f:
    pickle.dump(nx.adjacency_data(largest_wcc_subgraph), f)

with open('largest_scc.pkl', 'wb') as f:
    pickle.dump(nx.adjacency_data(largest_scc_subgraph), f)

# save isolated nodes into file
with open('isolated_nodes.pkl', 'wb') as f:
    pickle.dump(isolated_nodes, f)

end_time = time.time()
print(f"runtime: {end_time - start_time:.2f} seconds")
