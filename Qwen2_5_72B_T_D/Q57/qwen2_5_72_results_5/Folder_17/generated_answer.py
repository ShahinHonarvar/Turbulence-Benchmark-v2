import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, current_sum, row, col, submatrix, result):
        if row >= mat.shape[0] or col >= mat.shape[1]:
            return
        current_sum += mat[row, col]
        submatrix.append(mat[row, col])
        if current_sum == target_sum:
            result.append(np.array(submatrix).reshape(-1, 1))
        find_submatrices_with_sum(mat, target_sum, current_sum, row + 1, col, submatrix, result)
        find_submatrices_with_sum(mat, target_sum, current_sum, row, col + 1, submatrix, result)
        submatrix.pop()
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            find_submatrices_with_sum(matrix, 398, 0, i, j, [], result)
    return result