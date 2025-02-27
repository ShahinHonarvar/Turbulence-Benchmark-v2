import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, row, col, rows, cols, current_sum, start_row, start_col, result):
        if start_row < 0 or start_col < 0 or row >= rows or (col >= cols):
            return
        current_sum += matrix[row][col]
        if current_sum == target_sum:
            submatrix = matrix[start_row:row + 1, start_col:col + 1]
            result.append(submatrix)
        if current_sum < target_sum:
            find_submatrices(matrix, target_sum, row, col + 1, rows, cols, current_sum, start_row, start_col, result)
            find_submatrices(matrix, target_sum, row + 1, col, rows, cols, current_sum, start_row, start_col, result)
            find_submatrices(matrix, target_sum, row + 1, col + 1, rows, cols, current_sum, start_row, start_col, result)
    result = []
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            find_submatrices(matrix, 66, start_row, start_col, rows, cols, 0, start_row, start_col, result)
    return result