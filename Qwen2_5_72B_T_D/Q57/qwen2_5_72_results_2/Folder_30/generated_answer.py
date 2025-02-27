import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, result, row, col, current, sum_val):
        if row > matrix.shape[0] or col > matrix.shape[1]:
            return
        if sum_val == target_sum:
            result.append(current)
            return
        if row == matrix.shape[0] or col == matrix.shape[1]:
            return
        for i in range(row, matrix.shape[0]):
            for j in range(col, matrix.shape[1]):
                new_sum = sum_val + matrix[i, j]
                if new_sum > target_sum:
                    continue
                find_submatrices(matrix, target_sum, result, i, j + 1, current + [matrix[i, j]], new_sum)
                find_submatrices(matrix, target_sum, result, i + 1, col, current + [matrix[i, j]], new_sum)
    result = []
    find_submatrices(np.array(matrix), 21, result, 0, 0, [], 0)
    return [np.array(sub).reshape((-1, 1)) for sub in result if np.sqrt(len(sub)) == int(np.sqrt(len(sub)))]