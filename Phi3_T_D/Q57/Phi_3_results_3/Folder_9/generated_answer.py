import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for a in range(m + 1):
        for b in range(a, m + 1):
            for c in range(n + 1):
                for d in range(c, n + 1):
                    submatrix = matrix[a:b, c:d]
                    if submatrix.size and np.sum(submatrix) == -86:
                        result.append(submatrix)
    return result