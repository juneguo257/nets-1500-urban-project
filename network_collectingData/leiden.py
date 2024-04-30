import networkx as nx
import pickle
from cdlib import algorithms
import time

start_time = time.time()

# load graph
with open('graph.pkl', 'rb') as f:
    G = pickle.load(f)

loading_time = time.time()
print(f"graph loading time: {loading_time - start_time:.2f} seconds")

# do leiden algo from networkx
communities = algorithms.leiden(G)
leiden_time = time.time()
print(f"leiden algorithm time: {leiden_time - loading_time:.2f} seconds")

# make dictionary for community data
community_dict = {i: list(community) for i, community in enumerate(communities.communities)}

# save community dictionary as a pickle file
with open('communities.pkl', 'wb') as f:
    pickle.dump(community_dict, f, protocol=pickle.HIGHEST_PROTOCOL)

# print communities
for i, community in enumerate(communities.communities):
    print(f"community {i}: {list(community)}")

end_time = time.time()
print(f"total runtime: {end_time - start_time:.2f} seconds")
