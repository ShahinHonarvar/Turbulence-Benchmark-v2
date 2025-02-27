import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target_sum):
        rows, cols = mat.shape
        result = []
        for top_row in range(rows):
            for left_col in range(cols):
                for bottom_row in range(top_row + 1, rows + 1):
                    for right_col in range(left_col + 1, cols + 1):
                        submat = mat[top_row:bottom_row, left_col:right_col]
                        if np.sum(submat) == target_sum:
                            result.append(submat)
        return result
    return submatrix_sum(matrix, 38)