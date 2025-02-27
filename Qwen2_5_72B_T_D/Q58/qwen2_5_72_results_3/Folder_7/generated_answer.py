import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_size = 121
    matrix_height, matrix_width = matrix.shape
    count = 0
    for i in range(matrix_height - 10 + 1):
        for j in range(matrix_width - 10 + 1):
            if np.size(matrix[i:i + 10, j:j + 10]) == submatrix_size:
                count += 1
    return count