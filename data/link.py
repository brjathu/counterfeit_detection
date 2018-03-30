import numpy as np
from numpy import loadtxt


icon_list = np.load("icon_list.npy")
top_list = np.loadtxt("top10000.txt", comments="#", delimiter="\n", unpack=False, dtype=object)


top_path = np.ndarray((10000), dtype=object)

c = 0
x = 0
for t in top_list:
    for i in icon_list:
        a = i.split("/")[-1][0:-4]
        if (a == t):
            c += 1
            top_path[x] = i
            print(i, a, t, c)
    x += 1

np.save("top10000.npy", top_path)
print(x)
print(c)
