import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    submatrix_size = 24
    num_submatrices = 0
    for i in range(num_rows - submatrix_size + 1):
        for j in range(num_cols - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if submatrix.size == submatrix_size:
                num_submatrices += 1
    return num_submatrices