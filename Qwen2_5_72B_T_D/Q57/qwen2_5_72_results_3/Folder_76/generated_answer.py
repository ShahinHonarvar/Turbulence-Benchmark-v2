import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(m, start_row, start_col, end_row, end_col):
        sum_val = 0
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                sum_val += m[i][j]
        return sum_val
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    if sum_submatrix(matrix, i, j, k, l) == -255:
                        submatrices.append(matrix[i:k, j:l])
    return submatrices