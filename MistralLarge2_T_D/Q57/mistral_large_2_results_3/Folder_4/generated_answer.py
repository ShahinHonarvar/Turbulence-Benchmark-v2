import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def find_submatrices(start_row, start_col, submatrix_sum):
        if submatrix_sum == 87:
            result.append(matrix[start_row:row, start_col:col])
            return
        if submatrix_sum > 87:
            return
        if row == rows and col == cols:
            return
        if col < cols:
            find_submatrices(start_row, start_col, submatrix_sum + matrix[row, col])
            col += 1
            find_submatrices(start_row, start_col, submatrix_sum)
        else:
            row += 1
            col = start_col
            find_submatrices(start_row, start_col, submatrix_sum)
    for row in range(rows):
        for col in range(cols):
            find_submatrices(row, col, matrix[row, col])
    return result