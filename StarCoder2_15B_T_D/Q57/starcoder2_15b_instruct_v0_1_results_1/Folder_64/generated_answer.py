import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n_rows, n_cols = matrix.shape
    for row_start in range(n_rows):
        for row_end in range(row_start + 1, n_rows + 1):
            for col_start in range(n_cols):
                for col_end in range(col_start + 1, n_cols + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.sum() == -4:
                        submatrices.append(submatrix)
    return submatrices