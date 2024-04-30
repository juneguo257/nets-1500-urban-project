import pickle
import random
import sys

with open('final/combinedOUT.pkl', 'rb') as f:
    outEdgesDict = pickle.load(f)

def bfsNumNodes(start): 
    # Mark all the vertices as not visited
    visited = set()
 
    # Create a queue for BFS
    queue = []
 
    # Mark the source node as
    # visited and enqueue it
    queue.append([start, 0])
    visited.add(start)
    prevDeg = 0
 
    while queue:
        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        curStr = s[0]
        curLen = s[1]

        if (prevDeg < curLen):
            with open("final/nodesAtDegree.txt", "a") as fout:
                print(str(prevDeg) + "," + str(len(visited)))
                print(str(prevDeg) + "," + str(len(visited)), file=fout)
            prevDeg = curLen
            
        # Get all adjacent vertices of the
        # dequeued vertex s.
        # If an adjacent has not been visited,
        # then mark it visited and enqueue it

        if curStr in outEdgesDict: # should ALMOST ALWAYS BE IN DICT
            for neighbor in outEdgesDict[curStr]:
                if neighbor not in visited:
                    queue.append([neighbor, curLen + 1])
                    visited.add(curStr)
    
print("Loaded dictionary!")
allKeys = list(outEdgesDict.keys())
itersDone = 0
start = "rizz"

print("Starting from:" + start)
bfsNumNodes(start)