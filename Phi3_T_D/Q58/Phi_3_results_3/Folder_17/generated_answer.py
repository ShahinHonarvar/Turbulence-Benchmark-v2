import numpy as np

def submatrix_with_n_numbers(matrix):
    n = matrix.shape[0] * matrix.shape[1]
    count = 0
    if n < 166:
        return 0
    while matrix.shape[0] >= 166 or matrix.shape[1] >= 166:
        min_size = min(matrix.shape)
        for top in range(0, matrix.shape[0] - min_size + 1):
            for left in range(0, matrix.shape[1] - min_size + 1):
                sub_matrix = matrix[top:top + min_size, left:left + min_size]
                if sub_matrix.size == 166:
                    count += 1
        min_size -= 1
    return count