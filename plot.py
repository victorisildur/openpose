import matplotlib.pyplot as plt
import numpy as np

def get_body_part_name(i):
    bodyparts = ["nose", ""]
    return bodyparts[i]

f = open("me")
line = f.readline()
x = []
ys = []
xys = []
i = 0
while line:
    part = i % 25
    xyscore = line.split()
    xyscore[0] = float(xyscore[0])
    xyscore[1] = float(xyscore[1])
    xyscore[2] = float(xyscore[2])
    if part == 0:
        x.append(i)
    y = 1080 - float(xyscore[1])
    if len(ys) <= part:
        ys.append([y])
        xys.append([xyscore])
    else:
        ys[part].append(y)
        xys[part].append(xyscore)
    line = f.readline()
    i+=1
f.close()

## python list -> np.array
xy1s = np.array(xys[1])
print(xys[1])
print(xy1s)
xy8s = np.array(xys[8])
xy10s = np.array(xys[10])
ma_x = xy1s[...,0] - xy8s[...,0]
ma_y = xy1s[...,1] - xy8s[...,1]
mb_x = xy8s[...,0] - xy10s[...,0]
mb_y = xy8s[...,1] - xy10s[...,1]
ab_x = xy10s[...,0] - xy1s[...,0]
ab_y = xy10s[...,1] - xy1s[...,1]
ab_val2 = ab_x * ab_x + ab_y * ab_y
ma_val2 = ma_x * ma_x + ma_y * ma_y
mb_val2 = mb_x * mb_x + mb_y * mb_y
cos_M = (ma_val2+mb_val2-ab_val2) / (2 * np.sqrt(ma_val2)*np.sqrt(mb_val2))
angleAMB = np.arccos(cos_M)/np.pi * 180
plt.scatter(np.array(x),angleAMB)
plt.show()
