import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(i, j, rows, cols, target, current, result):
        if target == 0:
            result.append(current)
            return
        if target < 0 or i >= rows or j >= cols:
            return
        current_size = len(current)
        current.append(matrix[i][j])
        find_submatrices(i + 1, j, rows, cols, target - matrix[i][j], current, result)
        find_submatrices(i, j + 1, rows, cols, target - matrix[i][j], current, result)
        current.pop()
        if current_size != len(current):
            return
        find_submatrices(i + 1, j, rows, cols, target, current, result)
        find_submatrices(i, j + 1, rows, cols, target, current, result)
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, j, rows, cols, -81, [], result)
    return [np.array(sub) for sub in result]