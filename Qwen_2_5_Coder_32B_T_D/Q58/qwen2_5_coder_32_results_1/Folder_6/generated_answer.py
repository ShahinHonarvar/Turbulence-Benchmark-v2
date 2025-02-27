import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    submatrix_size = 11
    rows, cols = matrix.shape
    for i in range(rows - submatrix_size + 1):
        for j in range(cols - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if np.sum(submatrix == 122) == submatrix_size * submatrix_size:
                count += 1
    return count