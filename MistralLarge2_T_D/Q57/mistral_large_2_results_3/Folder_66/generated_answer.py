import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def find_submatrices(start_row, start_col, current_sum, current_submatrix):
        if current_sum == 99:
            result.append(current_submatrix)
            return
        if current_sum > 99 or start_row >= rows or start_col >= cols:
            return
        for r in range(start_row, rows):
            for c in range(start_col, cols):
                find_submatrices(r, c + 1, current_sum + matrix[r, c], current_submatrix + [[r, c]])
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, j, 0, [])
    return result