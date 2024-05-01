import time
import pickle
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random

start = time.time()

# with open("nxGraph.nx", "rb") as fin:
#     G = pickle.load(fin)

# print("Imported from networkX...")

# for i in range(99000):
#     curStart = random.randint(0, G.number_of_nodes())
#     curEnd = random.randint(0, G.number_of_nodes())

#     print("Starting from: " + str(curStart))
#     print("Starting from: " + str(curEnd))

#     res = nx.shortest_path_length(G, source=curStart, target=curEnd)

#     with open("shortestPathLengths.txt", "a") as fout:
#         print(res)
#         print(res, file=fout)
#     print("----------------------------")

with open("shortestPathLengths.txt", "r") as fin:
    res = fin.readlines()

resCount = {}
avg = 0.0
count = 0
for num in res:
    avg += int(num.strip())
    if int(num.strip()) not in resCount:
        resCount[int(num.strip())] = 1
    else:
        resCount[int(num.strip())] = resCount[int(num.strip())] + 1
    count += 1

print(resCount)
fig, ax = plt.subplots()
ax.set_xlabel('Shortest Path Length')
ax.set_ylabel('# Of Occurences')

plt.bar(list(resCount.keys()), resCount.values(), color='b')

plt.show()

print("Average shortest path length: " + str(avg / count))

print("Finished in (seconds): " + str(time.time() - start))