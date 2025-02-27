import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    num_submatrices = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i, j] == 173:
                num_submatrices += 1
    return num_submatrices