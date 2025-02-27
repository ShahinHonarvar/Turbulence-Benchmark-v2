import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, current_sum, start_row, start_col, end_row, end_col, submatrices):
        if end_row > matrix.shape[0] or end_col > matrix.shape[1]:
            return
        current_sum += np.sum(matrix[start_row:end_row, start_col:end_col])
        if current_sum == target_sum:
            submatrices.append(matrix[start_row:end_row, start_col:end_col])
        find_submatrices(matrix, target_sum, current_sum - np.sum(matrix[start_row:end_row, start_col:end_col]), start_row, start_col + 1, end_row, end_col + 1, submatrices)
        find_submatrices(matrix, target_sum, 0, start_row, start_col + 1, start_row + 1, start_col + 2, submatrices)
        find_submatrices(matrix, target_sum, 0, start_row + 1, start_col, start_row + 2, start_col + 1, submatrices)
    submatrices = []
    find_submatrices(matrix, 901, 0, 0, 0, 1, 1, submatrices)
    return submatrices