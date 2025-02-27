import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, row, col, rows, cols, current_sum, result, path):
        if current_sum == target_sum:
            result.append(path.copy())
            return
        if current_sum > target_sum or row >= rows or col >= cols:
            return
        path.append(matrix[row][col])
        find_submatrices(matrix, target_sum, row + 1, col, rows, cols, current_sum + matrix[row][col], result, path)
        find_submatrices(matrix, target_sum, row, col + 1, rows, cols, current_sum + matrix[row][col], result, path)
        path.pop()
    rows, cols = matrix.shape
    result = []
    for row in range(rows):
        for col in range(cols):
            find_submatrices(matrix, -64, row, col, rows, cols, 0, result, [])
    return [np.array(sub) for sub in result if np.sum(sub) == -64]