import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows = matrix.shape[0]
    num_cols = matrix.shape[1]
    count = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(submatrix) == 48:
                count += 1
    return count