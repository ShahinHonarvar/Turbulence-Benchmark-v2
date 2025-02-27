import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    num_submatrices = 0
    for i in range(num_rows - 174):
        for j in range(num_cols - 174):
            submatrix = matrix[i:i + 175, j:j + 175]
            if submatrix.size == 175:
                num_submatrices += 1
    return num_submatrices