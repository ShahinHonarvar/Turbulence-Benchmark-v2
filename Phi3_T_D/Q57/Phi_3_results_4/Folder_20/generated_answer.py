import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            for x in range(i + 1, n + 1):
                for y in range(j + 1, m + 1):
                    submatrix = matrix[i:x, j:y]
                    if submatrix.sum() == -57:
                        result.append(submatrix.tolist())
    return result