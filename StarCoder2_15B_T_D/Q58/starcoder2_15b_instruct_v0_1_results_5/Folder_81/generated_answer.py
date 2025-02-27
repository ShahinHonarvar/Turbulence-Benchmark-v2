import numpy as np

def submatrix_with_n_numbers(matrix):
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 2):
        for j in range(n_cols - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if np.sum(sub_matrix) == 97:
                count += 1
    return count