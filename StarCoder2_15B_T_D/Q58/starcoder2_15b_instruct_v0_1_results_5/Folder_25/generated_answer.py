import numpy as np

def submatrix_with_n_numbers(matrix):
    num_submatrices = 0
    num_rows, num_cols = matrix.shape
    for i in range(num_rows - 1):
        for j in range(num_cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.count_nonzero(submatrix) == 66:
                num_submatrices += 1
    return num_submatrices