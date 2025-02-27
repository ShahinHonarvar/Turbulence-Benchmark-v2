import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 69
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            submatrix = matrix[i:, j:]
            if np.sum(submatrix == n) == 69:
                count += 1
    return count