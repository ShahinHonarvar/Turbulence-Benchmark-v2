import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, current_sum, row, col, submatrix, result):
        if row >= mat.shape[0] or col >= mat.shape[1]:
            return
        current_sum += mat[row][col]
        submatrix.append(mat[row][col])
        if current_sum == target_sum:
            result.append(np.array(submatrix))
        elif current_sum < target_sum:
            find_submatrices_with_sum(mat, target_sum, current_sum, row + 1, col, submatrix.copy(), result)
            find_submatrices_with_sum(mat, target_sum, current_sum, row, col + 1, submatrix.copy(), result)
    target_sum = 80
    result = []
    for start_row in range(matrix.shape[0]):
        for start_col in range(matrix.shape[1]):
            find_submatrices_with_sum(matrix, target_sum, 0, start_row, start_col, [], result)
    return result