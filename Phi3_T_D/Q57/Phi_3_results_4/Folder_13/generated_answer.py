import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i, j in product(range(rows), range(cols)):
        for m in range(i, rows):
            for n in range(j, cols):
                submatrix = matrix[i:m + 1, j:n + 1]
                if submatrix.sum() == 382:
                    result.append(submatrix)
    return result