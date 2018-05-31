# Benjamin Yi
# 925302651
# byi649

# To be accurate, this is more of a mashup of many different stack overflow answers than any original work of my own.

import numpy as np
from itertools import chain, combinations
import heapq

distances = np.loadtxt('distances.txt')
workable = []

for i, col in enumerate(distances):
	workable.append(col <= heapq.nsmallest(8, col)[-1])

# Turn booleans into list of index
index = [[i for i, x in enumerate(sub) if x] for sub in workable]

matrixindex = [list(chain.from_iterable(combinations(s, r) for r in range(3, 6))) for s in index]
matrixindex = list(dict.fromkeys(list(filter(None, [item for sublist in matrixindex for item in sublist]))))

matrix = [np.zeros(48) for x in range(len(matrixindex))]

for i, column in enumerate(matrix):
    for j in matrixindex[i]:
        column[j] = 1

matrix = np.transpose(matrix)

np.savetxt("matrix.txt", matrix, fmt="%d")