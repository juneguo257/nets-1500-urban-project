import pickle
import time
import matplotlib.pyplot as plt
from igraph import Graph, plot, load

start = time.time()
# init colors
with open('final/communityColors.pkl', 'rb') as f:
    colors = pickle.load(f)

g = Graph.Read_Pickle('final/sampleCleanedGRAPH.net')
print("Loaded graph! Getting colors...")

# visual style for ending
visual_style = {}
visual_style["target"] = "graph32kmiddle.png"
visual_style["vertex_size"] = 12
visual_style["vertex_color"] = [colors[community] for community in g.vs["community"]]
visual_style["edge_width"] = 5
visual_style["edge_color"] = g.es["color"]
visual_style["bbox"] = (30720, 17280)
visual_style["margin"] = 100
print("Finished getting colors & init settings! Getting layout...")

visual_style["layout"] = g.layout("drl")

print("Finished layout! Plotting graph...")


plot(g, background=(0, 0, 0), **visual_style)
print("Outputted graph! Finished in: " + str(time.time() - start) + " seconds.")