import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def check_sum(row_start, col_start, row_end, col_end):
        return np.sum(matrix[row_start:row_end, col_start:col_end]) == -82
    for rows_start in range(rows):
        for cols_start in range(cols):
            for rows_end in range(rows_start + 1, rows + 1):
                for cols_end in range(cols_start + 1, cols + 1):
                    if check_sum(rows_start, cols_start, rows_end, cols_end):
                        result.append(matrix[rows_start:rows_end, cols_start:cols_end])
    return result