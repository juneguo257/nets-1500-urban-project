import pickle
import time
import networkx as nx
from igraph import Graph, plot, load

g = Graph.Read_Pickle('final/sampleFinishedGRAPH.net')
print("Loaded graph! Transferring to networkX...")

G = g.to_networkx()

print("Imported into networkX...")

delNodes = [c for c in sorted(nx.connected_components(G), key=len, reverse=True)]
removeVerts = []

print("Num verticies in 1st component: " + str(len(delNodes[0])))

# index to start deleting from
startDelete = 1
for i in range(startDelete, len(delNodes)):
    removeVerts.extend(delNodes[i])

g.delete_vertices(removeVerts)

g.write_pickle("final/sampleCleanedGRAPH.net")