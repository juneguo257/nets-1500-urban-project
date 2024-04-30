import pickle
from igraph import Graph

# set to -1 to do all input data
MAX_NODES = -1

with open('final/combinedOUT.pkl', 'rb') as f:
    outEdgesDict = pickle.load(f)

with open('final/communitiesSCC.pkl', 'rb') as f:
    communities = pickle.load(f)

with open('final/communityColors.pkl', 'rb') as f:
    colors = pickle.load(f)

colorsTrans = []
for color in colors:
    colorsTrans.append((color[0], color[1], color[2], 0.9))

# get community sizes and determine where to end
commSizes = []
for i in range(len(communities)):
    commSizes.append(len(communities[i]))

# TOP 42 COMMUNITIES SIZES WILL BE USED
communitiesToUse = 42
# (after 42 it drops from 2416 nodes to 13 nodes)

listNames = []
communityNum = []
nameToCommunity = {}
count = 0
for i in range(communitiesToUse):
    for node in communities[i]:
        listNames.append(node)
        communityNum.append(i)
        nameToCommunity[node] = i
    count += 1

    if ((MAX_NODES != -1) and (count >= MAX_NODES)):
        break

print("Finished node collection.")

setNames = set(listNames)

dictNodeToNum = {}
count = 0
# init unique node # for each node
for i in range(len(listNames)):
    if (count % 10000 == 0):
        print("Dict translation finished: "+str(count))
    dictNodeToNum[listNames[i]] = i
    count += 1

print("-----------------------------------")

count = 0
edges = []
edgeColors = []
# init edges
for node in listNames:
    if ((MAX_NODES != -1) and count >= MAX_NODES):
        break
    if (count % 10000 == 0):
        print("Nodes finished: "+str(count))
    
    curCom = nameToCommunity[node]
    # some nodes don't actually exist in real graph >:(
    try:
        for dest in outEdgesDict[node]:
            if dest in setNames:
                edges.append([dictNodeToNum[node], dictNodeToNum[dest]])
                if (curCom == nameToCommunity[dest]):
                    edgeColors.append(colorsTrans[curCom])
                else:
                    edgeColors.append((0, 0, 0))
        count += 1
    except:
        pass

print("Finished edge addition with edges: " + str(count))

# g = Graph(n=len(listNames), edges=edges, directed=True)
g = Graph(n=len(listNames), edges=edges)

# init names
g.vs["name"] = listNames
g.vs["community"] = communityNum
g.es["color"] = edgeColors

print("Saving graph...")
g.write_pickle("final/undirectedFinishedGRAPH.net")
print("Outputted graph.")