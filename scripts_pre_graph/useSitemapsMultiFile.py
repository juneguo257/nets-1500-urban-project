import requests
from urllib.parse import quote
import re
import time
import pickle 
from igraph import Graph

startFile = 1
for curFile in range(startFile, 10):
    print("Starting file: " + str(curFile))

    with open("inputs/" + str(curFile) + ".txt", "r") as fin:
        links = fin.readlines()

    baseURL = "https://urbandictionary.com"

    # incoming edges
    urbanInDict = {}

    # outgoing edges
    urbanOutDict = {}

    startTime = time.time()

    curFinished = 0
    for link in links:
        if (curFinished % 1000 == 0):
            print("Now finished (URLs): " + str(curFinished))
        res = set()
        link = link.rstrip()
        resSingle = requests.get(link, stream=True)
        if resSingle.status_code == 200:
            curTitle = str.lower(re.search(r'\?term=(.*)', link).group(1))

            # step 1: get everything that actually matches keyword (urban shows others too)
            # regex: <div class="definition[^"z]+"[^<>]*>(.*?)Vote up
            while True:
                try:
                    definitions = re.findall(r'<div class="definition[^"]+"[^<>]*>(.*?)Vote up', resSingle.text)
                    break
                except:
                    pass

            # step 1.5: get titles
            # regex: <h\d class="flex-1"><a[^<>]*>(.*?)<\/a>
            for definition in definitions:
                try:
                    titleMatcher = re.search(r'<h\d class="flex-1"><a[^<>]*>(.*?)</a>', definition)
                except:
                    raise "Cannot find title of: "+link
                # regex to get link search term: \?term=(.*)
                if (quote(str.lower(titleMatcher.group(1))) == curTitle):
                    # step 2: get links
                    # regex: <a class="autolink" href="([^"<>]+)">
                    res.update(re.findall(r'<a class="autolink" href="([^"<>]+)">', definition))
            
            for resLink in res:
                # resLinkFormatted = urllib.request.urlopen(baseURL+resLink)
                
                # resLink[17:] is term itself
                lwCurTerm = str.lower(resLink[17:])
                lwCurTitle = str.lower(curTitle)

                if urbanInDict.__contains__(lwCurTerm):
                    urbanInDict[lwCurTerm].append(lwCurTitle)
                else:
                    urbanInDict[lwCurTerm] = [lwCurTitle]
                
                if urbanOutDict.__contains__(lwCurTitle):
                    urbanOutDict[lwCurTitle].append(lwCurTerm)
                else:
                    urbanOutDict[lwCurTitle] = [lwCurTerm]
        curFinished += 1

    print("Finished " + str(curFile) + " in (s): " + str(time.time()-startTime))

    with open('outputs/' + str(curFile) + 'IN.pkl', 'wb') as f:
        pickle.dump(urbanInDict, f)

    with open('outputs/' + str(curFile) + 'OUT.pkl', 'wb') as f:
        pickle.dump(urbanOutDict, f)