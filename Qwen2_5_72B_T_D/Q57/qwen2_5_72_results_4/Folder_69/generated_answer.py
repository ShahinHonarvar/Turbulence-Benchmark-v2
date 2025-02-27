import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, current_sum, row, col, current_submatrix, result):
        rows, cols = mat.shape
        if row > rows - 1 or col > cols - 1:
            return
        current_value = mat[row][col]
        current_sum += current_value
        current_submatrix.append(current_value)
        if current_sum == target_sum:
            result.append(np.array(current_submatrix))
        elif current_sum < target_sum:
            find_submatrices_with_sum(mat, target_sum, current_sum, row + 1, col, current_submatrix, result)
            find_submatrices_with_sum(mat, target_sum, current_sum, row, col + 1, current_submatrix, result)
        current_submatrix.pop()
    result = []
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            find_submatrices_with_sum(matrix, 752, 0, start_row, start_col, [], result)
    return result