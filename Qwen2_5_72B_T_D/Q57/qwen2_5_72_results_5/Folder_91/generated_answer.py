import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(row, col, target_sum, current_sum, path, result):
        if row > len(matrix) or col > len(matrix[0]):
            return
        current_sum += matrix[row][col]
        path.append((row, col))
        if current_sum == target_sum:
            result.append([matrix[i][j] for i, j in path])
        if row < len(matrix) - 1:
            find_submatrices(row + 1, col, target_sum, current_sum, path, result)
        if col < len(matrix[0]) - 1:
            find_submatrices(row, col + 1, target_sum, current_sum, path, result)
        path.pop()
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            find_submatrices(i, j, -6, 0, [], result)
    return result