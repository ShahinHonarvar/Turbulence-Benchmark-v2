import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(m, target_sum, current_sum, row, col, submatrix, result):
        if row >= m.shape[0] or col >= m.shape[1]:
            return
        current_sum += m[row][col]
        submatrix.append(m[row][col])
        if current_sum == target_sum:
            result.append(submatrix.copy())
        find_submatrices_with_sum(m, target_sum, current_sum, row + 1, col, submatrix, result)
        find_submatrices_with_sum(m, target_sum, current_sum, row, col + 1, submatrix, result)
        submatrix.pop()
    target_sum = -82
    all_submatrices = []
    for start_row in range(matrix.shape[0]):
        for start_col in range(matrix.shape[1]):
            find_submatrices_with_sum(matrix, target_sum, 0, start_row, start_col, [], all_submatrices)
    return all_submatrices