import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    if matrix.size < 51:
        return 0
    for i in range(matrix.shape[0] - 7):
        for j in range(matrix.shape[1] - 7):
            if np.size(matrix[i:i + 7, j:j + 7]) == 51:
                submatrix_count += 1
    return submatrix_count