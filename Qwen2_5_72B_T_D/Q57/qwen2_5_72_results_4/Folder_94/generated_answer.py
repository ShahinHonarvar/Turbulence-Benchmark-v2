import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, current_sum, row, col, path, result):
        if current_sum == target_sum:
            result.append(path)
            return
        if current_sum > target_sum or row >= len(matrix) or col >= len(matrix[0]):
            return
        for i in range(row, len(matrix)):
            for j in range(col, len(matrix[0])):
                find_submatrices(matrix, target_sum, current_sum + matrix[i][j], i, j + 1, path + [matrix[i][j]], result)
    result = []
    find_submatrices(matrix, 92, 0, 0, 0, [], result)
    return [np.array(submat) for submat in result]