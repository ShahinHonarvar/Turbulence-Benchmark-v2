import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(start_row, start_col, end_row, end_col, target_sum):
        if start_row > end_row or start_col > end_col:
            return []
        current_sum = np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1])
        if current_sum == target_sum:
            return [matrix[start_row:end_row + 1, start_col:end_col + 1]]
        submatrices = []
        if end_row < matrix.shape[0] - 1:
            submatrices += find_submatrices(start_row, start_col, end_row + 1, end_col, target_sum)
        if end_col < matrix.shape[1] - 1:
            submatrices += find_submatrices(start_row, start_col, end_row, end_col + 1, target_sum)
        return submatrices
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            submatrices += find_submatrices(i, j, i, j, -87)
    return submatrices