import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        n, m = mat.shape
        for top_row in range(n):
            for bottom_row in range(top_row, n):
                for left_col in range(m):
                    for right_col in range(left_col, m):
                        yield mat[top_row:bottom_row + 1, left_col:right_col + 1]
    result = [submat for submat in get_submatrices(matrix) if np.sum(submat) == 15]
    return result