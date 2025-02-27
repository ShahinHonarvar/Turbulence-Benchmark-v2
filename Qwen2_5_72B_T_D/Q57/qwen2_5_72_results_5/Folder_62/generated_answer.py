import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target):
        result = []
        rows, cols = mat.shape
        for top_row in range(rows):
            for left_col in range(cols):
                for bottom_row in range(top_row, rows):
                    for right_col in range(left_col, cols):
                        if np.sum(mat[top_row:bottom_row + 1, left_col:right_col + 1]) == target:
                            result.append(mat[top_row:bottom_row + 1, left_col:right_col + 1])
        return result
    return submatrix_sum(matrix, 394)