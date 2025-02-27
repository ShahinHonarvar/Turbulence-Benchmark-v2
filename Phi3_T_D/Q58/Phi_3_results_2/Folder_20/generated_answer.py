import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.shape[1] < 7 or 49 not in matrix.diagonal().sum():
        return 0
    total_submatrices = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if j + 6 < matrix.shape[1]:
                total_submatrices += np.sum(matrix[i:i + 7, j:j + 7]) == 49
    return total_submatrices