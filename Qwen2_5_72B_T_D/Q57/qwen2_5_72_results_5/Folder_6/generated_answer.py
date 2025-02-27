import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, current_sum, row, col, submatrix, result):
        if current_sum == target_sum:
            result.append(submatrix)
            return
        if row >= matrix.shape[0] or col >= matrix.shape[1] or current_sum > target_sum:
            return
        for next_row in range(row, matrix.shape[0]):
            for next_col in range(col, matrix.shape[1]):
                new_submatrix = matrix[row:next_row + 1, col:next_col + 1]
                find_submatrices(matrix, target_sum, current_sum + matrix[next_row, next_col], next_row, next_col + 1, new_submatrix, result)
                find_submatrices(matrix, target_sum, current_sum + matrix[next_row, next_col], next_row + 1, col, new_submatrix, result)
    result = []
    find_submatrices(matrix, 126, 0, 0, 0, np.array([]), result)
    return result