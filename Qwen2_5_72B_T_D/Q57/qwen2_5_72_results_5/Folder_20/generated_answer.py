import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(mat):
        rows, cols = mat.shape
        for top_row in range(rows):
            for bottom_row in range(top_row, rows):
                for left_col in range(cols):
                    for right_col in range(left_col, cols):
                        yield mat[top_row:bottom_row + 1, left_col:right_col + 1]
    result = [submatrix for submatrix in all_submatrices(matrix) if np.sum(submatrix) == -57]
    return result