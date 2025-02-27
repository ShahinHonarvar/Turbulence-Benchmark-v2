import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix.shape) != 2:
        return 0
    n_rows, n_cols = matrix.shape
    count = 0
    for rows in range(n_rows):
        for cols in range(n_cols):
            for sub_rows in range(rows, n_rows):
                for sub_cols in range(cols, n_cols):
                    submatrix = matrix[rows:sub_rows + 1, cols:sub_cols + 1]
                    if submatrix.size == 5:
                        count += 1
    return count