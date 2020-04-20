import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def get_body_part_name(i):
    bodyparts = ["nose", ""]
    return bodyparts[i]

f = open("out3")
line = f.readline()
xs = []
ys = []
colors = []
viridis = cm.get_cmap('viridis', 256)
i = 0
while line:
    xyscore = line.split()
    if xyscore[2] < 0.4:
        line = f.readline()
        i+=1
        continue
    y = 1080 - float(xyscore[1])
    x = float(xyscore[0])
    color = viridis(float(i) / 700)
    part = i % 25
    if len(ys) <= part:
        xs.append([x])
        ys.append([y])
        colors.append([color])
    else:
        xs[part].append(x)
        ys[part].append(y)
        colors[part].append(color)
    line = f.readline()
    i+=1
f.close()

_, axes = plt.subplots(5,5)
for i in range(len(ys)):
    axes[i/5][i%5].scatter(xs[i], ys[i], color=colors[i])
    axes[i/5][i%5].set_title(i, loc='left')
plt.show()

