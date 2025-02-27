import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, current_row, current_col, current_sum, current_submatrix, result):
        if current_row >= mat.shape[0] or current_col >= mat.shape[1]:
            return
        current_sum += mat[current_row, current_col]
        if current_sum == target_sum:
            result.append(current_submatrix + [(current_row, current_col)])
        find_submatrices_with_sum(mat, target_sum, current_row + 1, current_col, current_sum, current_submatrix + [(current_row, current_col)], result)
        find_submatrices_with_sum(mat, target_sum, current_row, current_col + 1, current_sum, current_submatrix + [(current_row, current_col)], result)
        if current_sum - mat[current_row, current_col] < target_sum:
            find_submatrices_with_sum(mat, target_sum, current_row + 1, current_col, current_sum - mat[current_row, current_col], current_submatrix, result)
            find_submatrices_with_sum(mat, target_sum, current_row, current_col + 1, current_sum - mat[current_row, current_col], current_submatrix, result)

    def convert_to_submatrix(matrix, positions):
        min_row = min((pos[0] for pos in positions))
        max_row = max((pos[0] for pos in positions))
        min_col = min((pos[1] for pos in positions))
        max_col = max((pos[1] for pos in positions))
        return matrix[min_row:max_row + 1, min_col:max_col + 1]
    mat = np.array(matrix)
    target_sum = -42
    result_positions = []
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            find_submatrices_with_sum(mat, target_sum, i, j, 0, [], result_positions)
    result_matrices = [convert_to_submatrix(mat, pos) for pos in result_positions]
    return result_matrices