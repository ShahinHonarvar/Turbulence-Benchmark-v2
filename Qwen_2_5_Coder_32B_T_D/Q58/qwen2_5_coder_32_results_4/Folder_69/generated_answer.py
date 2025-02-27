import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 11):
        for j in range(n - 11):
            if np.sum(matrix[i:i + 11, j:j + 11]) == 126:
                count += 1
    return count