import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(m, start_row, start_col, end_row, end_col):
        total = 0
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                total += m[i][j]
        return total
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if sum_submatrix(matrix, i, j, k, l) == 901:
                        result.append(matrix[i:k + 1, j:l + 1])
    return result