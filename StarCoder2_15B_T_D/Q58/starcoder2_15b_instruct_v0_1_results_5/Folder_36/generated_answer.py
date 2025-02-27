import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    num_submatrices = 0
    submatrix_size = 131
    for row in range(num_rows - submatrix_size + 1):
        for col in range(num_cols - submatrix_size + 1):
            submatrix = matrix[row:row + submatrix_size, col:col + submatrix_size]
            if submatrix.size == submatrix_size:
                num_submatrices += 1
    return num_submatrices