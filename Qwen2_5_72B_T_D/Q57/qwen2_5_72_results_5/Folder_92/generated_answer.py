import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        row, col = mat.shape
        result = []
        for top_row in range(row):
            for left_col in range(col):
                for bottom_row in range(top_row + 1, row + 1):
                    for right_col in range(left_col + 1, col + 1):
                        if np.sum(mat[top_row:bottom_row, left_col:right_col]) == target_sum:
                            result.append(mat[top_row:bottom_row, left_col:right_col])
        return result
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return []
    return find_submatrices_with_sum(matrix, -3)