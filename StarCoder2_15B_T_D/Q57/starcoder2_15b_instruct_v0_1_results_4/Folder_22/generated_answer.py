import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(1, matrix.shape[0] - 1):
        for j in range(1, matrix.shape[1] - 1):
            submatrix_sum = np.sum(matrix[i - 1:i + 2, j - 1:j + 2])
            if submatrix_sum == -38:
                submatrices.append(matrix[i - 1:i + 2, j - 1:j + 2])
    return submatrices