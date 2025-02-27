import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 91):
        for j in range(n - 91):
            if np.sum(matrix[i:i + 92, j:j + 92] == 92) == 92:
                count += 1
    return count