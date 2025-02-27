import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def find_submatrices(start_row, end_row, start_col, end_col):
        if end_row >= rows or end_col >= cols:
            return
        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
        if np.sum(submatrix) == -6:
            result.append(submatrix)
        find_submatrices(start_row, end_row, start_col, end_col + 1)
        find_submatrices(start_row, end_row + 1, start_col, end_col)
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, i, j, j)
    return result