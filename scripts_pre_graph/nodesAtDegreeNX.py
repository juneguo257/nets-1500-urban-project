import time
import pickle
import numpy as np
import networkx as nx
from igraph import Graph, plot, load

start = time.time()

# ---------------------------------------------------------- part 1
# g = Graph.Read_Pickle('final/undirectedFinishedGRAPH.net')
# print("Loaded graph! Transferring to networkX...")

# G = g.to_networkx()
# with open("nxGraph.nx", "wb") as fout:
#     pickle.dump(G, fout)

# print("Imported into networkX...")

# ---------------------------------------------------------- end part 1

with open("nxGraph.nx", "rb") as fin:
    G = pickle.load(fin)

print("Imported from networkX...")

source_path_lengths = nx.single_source_dijkstra_path_length(G, 370124) # random number

# with open("dumpSrcPathLengths.pkl", "wb") as fout:
#     pickle.dump(source_path_lengths, fout)

# with open("dumpSrcPathLengths.pkl", "rb") as fin:
#     source_path_lengths = pickle.load(fin)

print("Attempting to dump data:")

res = {}
for key in source_path_lengths:
    if source_path_lengths[key] not in res:
        res[source_path_lengths[key]] = 1
    else:
        res[source_path_lengths[key]] = res[source_path_lengths[key]] + 1

with open("resDegree5.txt", "w") as fout:
    for key in res:
        print("degree away: " + str(key), file=fout)
        print(res[key], file=fout)
        print("----------------------------", file=fout)

print("Finished in (seconds): " + str(time.time() - start))