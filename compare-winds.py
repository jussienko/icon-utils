import numpy as np
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

vn1, w1 = [], []
with open(file1, 'r') as f:
    for line in f:
        if 'MAXABS' in line:
            line = line.split()
            vn1.append(float(line[6]))
            w1.append(float(line[10]))
vn1 = np.array(vn1)
w1 = np.array(w1)

vn2, w2 = [], []
with open(file2, 'r') as f:
    for line in f:
        if 'MAXABS' in line:
            line = line.split()
            vn2.append(float(line[6]))
            w2.append(float(line[10]))
vn2 = np.array(vn2)
w2 = np.array(w2)
print(vn1.shape)
print(w1.shape)

try:
    n = int(sys.argv[3])
    print("Difference in {} time step for vn".format(n))
    print(vn1[(n-1)*5:n*5] - vn2[(n-1)*5:n*5])
    print("Difference in {} time step for w".format(n))
    print(w1[(n-1)*5:n*5] - w2[(n-1)*5:n*5])
except IndexError:
    print("Difference in first time step for vn")
    print(vn1[:5] - vn2[:5])
    print("Difference in first time step for w")
    print(w1[:5] - w2[:5])
    print("Difference in last time step for vn")
    print(vn1[-5:] - vn2[-5:])
    print("Difference in last time step for w")
    print(w1[-5:] - w2[-5:])
