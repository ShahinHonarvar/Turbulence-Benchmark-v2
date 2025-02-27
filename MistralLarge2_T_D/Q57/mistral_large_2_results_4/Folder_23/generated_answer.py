import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def find_submatrices(start_row, end_row, start_col, end_col):
        if start_row > end_row or start_col > end_col:
            return
        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
        if submatrix.sum() == 59:
            result.append(submatrix)
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                find_submatrices(i, end_row, j, end_col)
                find_submatrices(start_row, i, j, end_col)
                find_submatrices(start_row, end_row, j, start_col)
                find_submatrices(start_row, i, j, start_col)
    find_submatrices(0, rows - 1, 0, cols - 1)
    return result