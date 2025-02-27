import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 7):
        for j in range(n - 7):
            if np.sum(matrix[i:i + 7, j:j + 7] == 84) == 84:
                count += 1
    return count