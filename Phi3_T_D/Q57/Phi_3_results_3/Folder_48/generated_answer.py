import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i, j in product(range(rows), range(cols)):
        for m in range(i + 1, rows + 1):
            for n in range(j + 1, cols + 1):
                submat = matrix[i:m, j:n]
                if submat.sum() == -261:
                    result.append(submat)
    return result