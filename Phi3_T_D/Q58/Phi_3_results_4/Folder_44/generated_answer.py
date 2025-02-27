import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            n = 191
            while i + n <= matrix.shape[0] and j + n <= matrix.shape[1]:
                submatrix = matrix[i:i + n, j:j + n]
                if submatrix.size == n ** 2:
                    if np.all(submatrix == 1):
                        count += 1
                n += 1
    return count