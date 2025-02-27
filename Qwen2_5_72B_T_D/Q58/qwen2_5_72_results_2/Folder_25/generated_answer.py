import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    target_size = 66
    for i in range(m):
        for j in range(n):
            if i + 10 <= m and j + 6 <= n and (np.prod(matrix[i:i + 10, j:j + 6].shape) == target_size):
                count += 1
    return count