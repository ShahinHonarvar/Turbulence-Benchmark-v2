import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(matrix, start_row, end_row, start_col, end_col):
        sum_val = 0
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                sum_val += matrix[i][j]
        return sum_val
    rows, cols = matrix.shape
    submatrices = []
    for start_row in range(rows):
        for end_row in range(start_row + 1, rows + 1):
            for start_col in range(cols):
                for end_col in range(start_col + 1, cols + 1):
                    if sum_submatrix(matrix, start_row, end_row, start_col, end_col) == 94:
                        submatrices.append(matrix[start_row:end_row, start_col:end_col])
    return submatrices