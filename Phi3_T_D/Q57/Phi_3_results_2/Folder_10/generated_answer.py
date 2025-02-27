import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    m, n = matrix.shape
    for x in range(m):
        for y in range(n):
            for dx in range(x, m):
                for dy in range(y, n):
                    submat = matrix[x:dx + 1, y:dy + 1]
                    if np.sum(submat) == 56:
                        result.append(submat)
    return result