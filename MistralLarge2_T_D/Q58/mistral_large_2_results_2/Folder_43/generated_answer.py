import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if np.count_nonzero(matrix[i:k + 1, j:l + 1]) == 85:
                        count += 1
    return count