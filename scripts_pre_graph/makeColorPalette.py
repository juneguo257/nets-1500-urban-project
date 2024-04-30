import distinctipy
import pickle

with open('final/communityColors.pkl', 'rb') as f:
    colors = pickle.load(f)
# colors = distinctipy.get_colors(43, pastel_factor=0.9)

def swap(ele1, ele2):
    tmp = colors[ele1]
    colors[ele1] = colors[ele2]
    colors[ele2] = tmp

swap(0, 7)

distinctipy.color_swatch(colors)

with open("final/communityColors.pkl", 'wb') as f:
    pickle.dump(colors, f)