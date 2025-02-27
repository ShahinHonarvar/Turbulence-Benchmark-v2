import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(matrix, target_sum, current_sum, row, col, current_submatrix, result):
        if row >= matrix.shape[0] or col >= matrix.shape[1]:
            return
        current_sum += matrix[row][col]
        current_submatrix.append((row, col))
        if current_sum == target_sum:
            result.append([matrix[i][j] for i, j in current_submatrix])
        find_submatrices_with_sum(matrix, target_sum, current_sum, row + 1, col, current_submatrix, result)
        find_submatrices_with_sum(matrix, target_sum, current_sum, row, col + 1, current_submatrix, result)
        current_sum -= matrix[row][col]
        current_submatrix.pop()
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            find_submatrices_with_sum(matrix, 66, 0, i, j, [], result)
    return result