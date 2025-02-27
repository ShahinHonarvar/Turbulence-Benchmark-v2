import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 16):
        for j in range(n - 16):
            if matrix[i:i + 17, j:j + 17].size == 176:
                count += 1
    return count