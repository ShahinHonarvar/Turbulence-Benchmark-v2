import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, curr_sum, row, col, curr_matrix, result):
        if row >= matrix.shape[0] or col >= matrix.shape[1] or curr_sum > target_sum:
            return
        curr_matrix[row][col] = matrix[row, col]
        curr_sum += matrix[row][col]
        if curr_sum == target_sum:
            result.append(np.array(curr_matrix, dtype=np.int32))
        find_submatrices(matrix, target_sum, curr_sum, row + 1, col, curr_matrix + np.zeros_like(curr_matrix, dtype=np.int32), result)
        find_submatrices(matrix, target_sum, curr_sum, row, col + 1, curr_matrix + np.zeros_like(curr_matrix, dtype=np.int32), result)
    target_sum = -3
    result = []
    for start_row in range(matrix.shape[0]):
        for start_col in range(matrix.shape[1]):
            find_submatrices(matrix, target_sum, 0, start_row, start_col, np.zeros_like(matrix, dtype=np.int32), result)
    return result