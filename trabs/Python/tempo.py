import matplotlib.pyplot as plt
import numpy as np

vetor = [6, 8, 0, 7, 9, 1, 3, 4, 2, 5]

avlTime = []
with open("./avl_time", "r") as f:
    content = f.readlines()
    for line in content:
        avlTime.append(line[:-1])
f.close

rbTime = []
with open("./rb_time", "r") as f:
    content = f.readlines()
    for line in content:
        rbTime.append(line[:-1])
f.close

width = 0.3
x = np.arange(len(vetor))

plt.bar(x, avlTime, width, color="blue", align="center")
plt.bar(x-width, rbTime, width, color="red", align="center")

plt.xticks(x-width/2, vetor)

plt.show()