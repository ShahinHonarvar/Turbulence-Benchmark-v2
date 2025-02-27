import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            for p in range(i, n):
                for q in range(j, m):
                    submatrix_sum = np.sum(matrix[i:p + 1, j:q + 1])
                    if submatrix_sum == 17:
                        result.append(matrix[i:p + 1, j:q + 1])
    return result