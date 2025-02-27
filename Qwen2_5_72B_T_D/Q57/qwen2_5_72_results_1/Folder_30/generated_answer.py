import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, current_sum, row, col, rows, cols, submatrix, result):
        if current_sum == target_sum:
            result.append(submatrix)
            return
        if current_sum > target_sum or row >= rows or col >= cols:
            return
        find_submatrices(matrix, target_sum, current_sum, row + 1, col, rows, cols, submatrix, result)
        find_submatrices(matrix, target_sum, current_sum, row, col + 1, rows, cols, submatrix, result)
        new_submatrix = matrix[row:row + len(submatrix) + 1, col:col + len(submatrix[0]) + 1]
        if new_submatrix.size > 0 and new_submatrix.shape[0] == submatrix.shape[0] + 1 and (new_submatrix.shape[1] == submatrix.shape[1] + 1):
            find_submatrices(matrix, target_sum, current_sum + new_submatrix[-1, -1], row, col, rows, cols, new_submatrix, result)
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            find_submatrices(matrix, 21, matrix[i, j], i, j, rows, cols, matrix[i, j].reshape(1, 1), result)
    return [r.tolist() for r in result]