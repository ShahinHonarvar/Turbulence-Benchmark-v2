import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(matrix, start_row, end_row, start_col, end_col):
        sum_val = 0
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                sum_val += matrix[i][j]
        return sum_val
    row_count, col_count = matrix.shape
    result = []
    for start_row in range(row_count):
        for end_row in range(start_row, row_count):
            for start_col in range(col_count):
                for end_col in range(start_col, col_count):
                    if sum_submatrix(matrix, start_row, end_row, start_col, end_col) == 88:
                        result.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
    return result