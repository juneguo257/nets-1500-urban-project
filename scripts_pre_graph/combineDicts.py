import pickle

# file mins and maxes
MIN = 1
MAX = 45

finalDict = {}
for curFile in range(MIN, MAX + 1):
    with open('outputs/' + str(curFile) + 'OUT.pkl', 'rb') as f:
        outEdgesDict = pickle.load(f)
    finalDict = finalDict | outEdgesDict

with open("final/combinedOUT.pkl", "wb") as fout:
    pickle.dump(finalDict, fout)