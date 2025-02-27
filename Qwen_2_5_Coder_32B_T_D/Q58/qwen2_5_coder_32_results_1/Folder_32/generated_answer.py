import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 9):
        for j in range(n - 9):
            if np.count_nonzero(matrix[i:i + 10, j:j + 10] == 103) == 100:
                count += 1
    return count