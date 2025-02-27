import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def find_submatrices(start_row, start_col, current_sum, current_submatrix):
        if current_sum == 56:
            result.append(current_submatrix)
            return
        if current_sum > 56 or start_row >= rows or start_col >= cols:
            return
        for i in range(start_row, rows):
            for j in range(start_col, cols):
                new_submatrix = current_submatrix + [(i, j)]
                find_submatrices(i, j + 1, current_sum + matrix[i, j], new_submatrix)
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, j, 0, [])
    return result