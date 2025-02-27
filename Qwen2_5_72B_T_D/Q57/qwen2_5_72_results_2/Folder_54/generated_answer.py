import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, row, col, rows, cols, current_sum, submatrix, result):
        if row > rows or col > cols:
            return
        current_sum += mat[row][col]
        submatrix.append(mat[row][col])
        if current_sum == target_sum:
            result.append(np.array(submatrix))
        find_submatrices_with_sum(mat, target_sum, row + 1, col, rows, cols, current_sum, submatrix.copy(), result)
        find_submatrices_with_sum(mat, target_sum, row, col + 1, rows, cols, current_sum, submatrix.copy(), result)
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return []
    rows, cols = matrix.shape
    all_submatrices = []
    for i in range(rows):
        for j in range(cols):
            find_submatrices_with_sum(matrix, -59, i, j, rows - 1, cols - 1, 0, [], all_submatrices)
    return all_submatrices