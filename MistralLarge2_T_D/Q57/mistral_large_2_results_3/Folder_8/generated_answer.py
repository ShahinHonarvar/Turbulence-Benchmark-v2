import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    target_sum = -61
    result = []

    def get_submatrices(start_row, start_col, end_row, end_col):
        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
        if submatrix.sum() == target_sum:
            result.append(submatrix.tolist())
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    get_submatrices(i, j, k, l)
    return result