import numpy as np
from numpy import array

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for a in range(i, rows):
                for b in range(j, cols):
                    submatrix = matrix[i:a + 1, j:b + 1]
                    if submatrix.sum() == 394:
                        result.append(submatrix)
    return result