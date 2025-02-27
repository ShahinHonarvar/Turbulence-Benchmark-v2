import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    submatrix_size = 51
    for i in range(num_rows - submatrix_size + 1):
        for j in range(num_cols - submatrix_size + 1):
            submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
            if np.sum(submatrix) == 51:
                return 1
    return 0