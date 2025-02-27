import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_start in range(rows):
        for col_start in range(cols):
            for sub_rows in range(1, rows - row_start + 1):
                for sub_cols in range(1, cols - col_start + 1):
                    submatrix = matrix[row_start:row_start + sub_rows, col_start:col_start + sub_cols]
                    if np.sum(submatrix == 10) == submatrix.size:
                        count += 1
    return count