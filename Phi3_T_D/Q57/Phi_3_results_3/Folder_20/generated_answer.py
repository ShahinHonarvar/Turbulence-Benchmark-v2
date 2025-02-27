import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for rows in range(1, m + 1):
        for cols in range(1, n + 1):
            for i, j, k, l in product(range(m - rows + 1), range(n - cols + 1), range(rows), range(cols)):
                submat = matrix[i:i + rows, j:j + cols]
                if submat.sum() == -57:
                    result.append(submat)
    return result