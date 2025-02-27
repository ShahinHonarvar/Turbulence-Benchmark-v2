import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, current_sum, start_row, start_col, end_row, end_col, result):
        if current_sum == target_sum:
            result.append(matrix[start_row:end_row, start_col:end_col].copy())
        if current_sum >= target_sum or end_row > matrix.shape[0] or end_col > matrix.shape[1]:
            return
        if end_row <= matrix.shape[0]:
            find_submatrices(matrix, target_sum, current_sum + sum(matrix[end_row - 1, start_col:end_col]), start_row, start_col, end_row + 1, end_col, result)
        if end_col <= matrix.shape[1]:
            find_submatrices(matrix, target_sum, current_sum + sum(matrix[start_row:end_row, end_col - 1]), start_row, start_col, end_row, end_col + 1, result)
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            find_submatrices(matrix, 616, 0, i, j, i + 1, j + 1, result)
    return result