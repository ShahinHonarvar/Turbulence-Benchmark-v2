import numpy as np

def submatrix_with_particular_sum(matrix):
    n_rows, n_cols = matrix.shape
    submatrices = []
    for row_start in range(n_rows):
        for row_end in range(row_start, n_rows):
            for col_start in range(n_cols):
                for col_end in range(col_start, n_cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if submatrix.sum() == 411:
                        submatrices.append(submatrix)
    return submatrices