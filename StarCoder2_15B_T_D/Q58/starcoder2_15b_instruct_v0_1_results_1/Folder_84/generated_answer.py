import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    total_submatrices = (row_count - 2) * (col_count - 2)
    submatrices_with_127_numbers = 0
    for i in range(row_count - 2):
        for j in range(col_count - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if np.sum(sub_matrix) == 127:
                submatrices_with_127_numbers += 1
    return submatrices_with_127_numbers