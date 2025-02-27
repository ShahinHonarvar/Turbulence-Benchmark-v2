import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(matrix, target_sum, row, col, rows, cols, current_sum, path, result):
        if row > rows or col > cols:
            return
        current_sum += matrix[row, col]
        path.append((row, col))
        if current_sum == target_sum:
            submatrix = matrix[np.ix_(*zip(*path))]
            result.append(submatrix)
        if row < rows:
            find_submatrices_with_sum(matrix, target_sum, row + 1, col, rows, cols, current_sum, path, result)
        if col < cols:
            find_submatrices_with_sum(matrix, target_sum, row, col + 1, rows, cols, current_sum, path, result)
        path.pop()
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            find_submatrices_with_sum(matrix, -863, i, j, rows, cols, 0, [], result)
    return result