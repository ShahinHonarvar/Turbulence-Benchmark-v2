import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    submatrices = []
    for i in range(n):
        for j in range(m):
            for x in range(i, n):
                for y in range(j, m):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if np.sum(submatrix) == -20:
                        submatrices.append(submatrix.tolist())
    return submatrices