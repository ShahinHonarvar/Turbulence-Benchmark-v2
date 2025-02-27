import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(matrix, row_start, row_end, col_start, col_end):
        sum_val = 0
        for i in range(row_start, row_end + 1):
            for j in range(col_start, col_end + 1):
                sum_val += matrix[i][j]
        return sum_val
    rows, cols = matrix.shape
    result = []
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    if sum_submatrix(matrix, row_start, row_end, col_start, col_end) == -93:
                        result.append(matrix[row_start:row_end + 1, col_start:col_end + 1])
    return result