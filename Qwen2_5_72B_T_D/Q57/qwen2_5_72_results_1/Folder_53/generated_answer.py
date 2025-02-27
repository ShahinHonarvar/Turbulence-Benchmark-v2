import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        rows, cols = mat.shape
        result = []
        for top_row in range(rows):
            for left_col in range(cols):
                for bottom_row in range(top_row, rows):
                    for right_col in range(left_col, cols):
                        submatrix = mat[top_row:bottom_row + 1, left_col:right_col + 1]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix)
        return result
    return find_submatrices_with_sum(matrix, -37)