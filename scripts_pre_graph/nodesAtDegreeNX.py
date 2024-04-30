import time
import pickle
import numpy as np
import networkx as nx
from igraph import Graph, plot, load

start = time.time()
# g = Graph.Read_Pickle('final/undirectedFinishedGRAPH.net')
# print("Loaded graph! Transferring to networkX...")

# G = g.to_networkx()
# with open("nxGraph.nx", "wb") as fout:
#     pickle.dump(G, fout)

# print("Imported into networkX...")

with open("nxGraph.nx", "rb") as fin:
    G = pickle.load(fin)

print("Imported from networkX...")

source_path_lengths = nx.single_source_dijkstra_path_length(G, 481) # random number

print(source_path_lengths)

with open("resDegree.txt", "w") as fout:
    for key in source_path_lengths:
        print("iter: " + str(key), file=fout)
        print(len(source_path_lengths[key]), file=fout)
        print("----------------------------", file=fout)

print("Finished in (seconds): " + str(time.time() - start))