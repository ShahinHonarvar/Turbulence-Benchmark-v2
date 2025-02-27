import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, current_sum, start_row, start_col, end_row, end_col, result):
        if current_sum == target_sum:
            submatrix = matrix[start_row:end_row, start_col:end_col].copy()
            result.append(submatrix)
            return
        if current_sum > target_sum or end_row > matrix.shape[0] or end_col > matrix.shape[1]:
            return
        find_submatrices(matrix, target_sum, current_sum + matrix[end_row, start_col], start_row, start_col, end_row + 1, end_col, result)
        find_submatrices(matrix, target_sum, current_sum + matrix[start_row, end_col], start_row, start_col, end_row, end_col + 1, result)
    result = []
    for start_row in range(matrix.shape[0]):
        for start_col in range(matrix.shape[1]):
            find_submatrices(matrix, 126, 0, start_row, start_col, start_row, start_col, result)
    return result