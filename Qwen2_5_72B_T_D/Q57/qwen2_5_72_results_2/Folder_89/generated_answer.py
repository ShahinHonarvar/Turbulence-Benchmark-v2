import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(m, target_sum, result, row, col, height, width):
        if row + height > m.shape[0] or col + width > m.shape[1]:
            return
        if sum((sum((m[i][j] for j in range(col, col + width))) for i in range(row, row + height))) == target_sum:
            result.append(m[row:row + height, col:col + width].tolist())
        if row + height < m.shape[0]:
            submatrix_sum(m, target_sum, result, row + 1, col, height, width)
        if col + width < m.shape[1]:
            submatrix_sum(m, target_sum, result, row, col + 1, height, width)
        if height < m.shape[0]:
            submatrix_sum(m, target_sum, result, row, col, height + 1, width)
        if width < m.shape[1]:
            submatrix_sum(m, target_sum, result, row, col, height, width + 1)
    target_sum = 80
    result = []
    submatrix_sum(matrix, target_sum, result, 0, 0, 1, 1)
    return result