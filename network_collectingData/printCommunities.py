import pickle
import matplotlib.pyplot as plt

# file containing the data
filename = 'communitiesSCC.pkl' #can be communitiesSCC.pkl or communities.pkl

# loading file data
def load_communities(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

#save file data to communities
communities = load_communities(filename)

print("communities loaded")
print(f"#communities: {len(communities)}") #print num communities

#sort
sorted_communities = sorted(communities.items(), key=lambda item: len(item[1]), reverse=True)
top_40_communities = sorted_communities[:40]

# match color to slides
r = 19 / 255
g = 79 / 255
b = 230 / 255
color = (r, g, b)

#visualizing
if top_40_communities:
    community_ids = [comm[0] for comm in top_40_communities]
    sizes = [len(comm[1]) for comm in top_40_communities]
    plt.figure(figsize=(10, 8))
    plt.bar(community_ids, sizes, color=color)
    plt.xlabel('Community ID')
    plt.ylabel('Number of Nodes')
    plt.title('Top 40 Largest Communities by Node Count')
    plt.xticks(rotation=90)
    plt.show()