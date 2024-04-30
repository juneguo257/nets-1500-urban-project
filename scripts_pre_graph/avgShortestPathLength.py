import pickle
import random
import sys

outputFile = sys.argv[1]

with open('final/combinedOUT.pkl', 'rb') as f:
    outEdgesDict = pickle.load(f)

def bfsShortestPathLength(start, end): 
    # Mark all the vertices as not visited
    visited = set()
 
    # Create a queue for BFS
    queue = []
 
    # Mark the source node as
    # visited and enqueue it
    queue.append([start, 0])
    visited.add(start)
 
    while queue:
        # Dequeue a vertex from
        # queue and print it
        s = queue.pop(0)
        curStr = s[0]
        curLen = s[1]

        # Get all adjacent vertices of the
        # dequeued vertex s.
        # If an adjacent has not been visited,
        # then mark it visited and enqueue it

        if curStr in outEdgesDict: # should ALMOST ALWAYS BE IN DICT
            for neighbor in outEdgesDict[curStr]:
                if (neighbor == end):
                    print("Found ending!")
                    return curLen + 1
                
                if neighbor not in visited:
                    queue.append([neighbor, curLen + 1])
                    visited.add(curStr)
    
    return -1

print("Loaded dictionary!")
allKeys = list(outEdgesDict.keys())
itersDone = 0
for i in range(2):
    start = random.choice(allKeys)
    goal = random.choice(allKeys)
    print(start)
    print(goal)
    res = bfsShortestPathLength(start, goal)
    print(res)

    with open("final/spl" + outputFile + ".txt", "a") as fout:
        print(res, file=fout)
    
    print("--------------------------")