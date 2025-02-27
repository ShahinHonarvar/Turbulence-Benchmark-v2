import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, current_sum, row, col, submatrix, result):
        if row >= mat.shape[0] or col >= mat.shape[1]:
            return
        current_sum += mat[row][col]
        submatrix.append(mat[row][col])
        if current_sum == target_sum:
            result.append(np.array(submatrix).reshape(-1, 1))
        elif current_sum < target_sum:
            find_submatrices_with_sum(mat, target_sum, current_sum, row + 1, col, submatrix.copy(), result)
            find_submatrices_with_sum(mat, target_sum, current_sum, row, col + 1, submatrix.copy(), result)

    def get_all_submatrices(matrix):
        rows, cols = matrix.shape
        submatrices = []
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row + 1, rows + 1):
                    for end_col in range(start_col + 1, cols + 1):
                        submatrices.append(matrix[start_row:end_row, start_col:end_col])
        return submatrices
    target_sum = 245
    all_submatrices = get_all_submatrices(matrix)
    valid_submatrices = [submat for submat in all_submatrices if np.sum(submat) == target_sum]
    return valid_submatrices