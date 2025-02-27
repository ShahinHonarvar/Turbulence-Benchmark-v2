import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 9):
        for j in range(n - 9):
            submatrix = matrix[i:i + 10, j:j + 10]
            if np.prod(submatrix.shape) == 96:
                count += 1
    return count