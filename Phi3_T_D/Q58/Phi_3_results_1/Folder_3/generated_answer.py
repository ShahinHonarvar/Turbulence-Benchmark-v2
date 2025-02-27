import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            if j + 4 < m and i + 4 < n:
                submatrix = matrix[i:i + 4, j:j + 4]
                if np.all(submatrix):
                    count += 1
    return count