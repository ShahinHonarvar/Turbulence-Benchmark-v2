import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, column_count = matrix.shape
    for row_start in range(row_count - 2):
        for column_start in range(column_count - 2):
            submatrix = matrix[row_start:row_start + 3, column_start:column_start + 3]
            if np.sum(submatrix) == 95:
                return 1
    return 0