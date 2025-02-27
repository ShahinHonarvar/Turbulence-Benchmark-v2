import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 35
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if np.prod(matrix[i:i + n, j:j + n].shape) == n:
                count += 1
    return count