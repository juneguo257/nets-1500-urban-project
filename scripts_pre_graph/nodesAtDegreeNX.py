import time
import pickle
import numpy as np
import networkx as nx
import random
from igraph import Graph, plot, load

start = time.time()

# ---------------------------------------------------------- part 1
# g = Graph.Read_Pickle('final/directedFinishedGRAPH.net')
# print("Loaded graph! Transferring to networkX...")

# G = g.to_networkx()
# with open("nxGraph.nx", "wb") as fout:
#     pickle.dump(G, fout)

# print("Imported into networkX...")

# ---------------------------------------------------------- end part 1

with open("directedNXGraph.nx", "rb") as fin:
    G = pickle.load(fin)

print("Imported from networkX...")

# with open("dumpSrcPathLengths.pkl", "wb") as fout:
#     pickle.dump(source_path_lengths, fout)

# with open("dumpSrcPathLengths.pkl", "rb") as fin:
#     source_path_lengths = pickle.load(fin)

for i in range(100):
    curStart = random.randint(0, G.number_of_nodes())
    source_path_lengths = nx.single_source_dijkstra_path_length(G, curStart) # random number

    print("Attempting to dump data for iter: " + str(i))

    res = {}
    for key in source_path_lengths:
        if source_path_lengths[key] not in res:
            res[source_path_lengths[key]] = 1
        else:
            res[source_path_lengths[key]] = res[source_path_lengths[key]] + 1

    with open("results/resDegree.txt", "a") as fout:
        for key in res:
            print(str(key) + "," +  str(res[key]), file=fout)
        print("----------------------", file=fout)

    print("Finished in (seconds): " + str(time.time() - start))