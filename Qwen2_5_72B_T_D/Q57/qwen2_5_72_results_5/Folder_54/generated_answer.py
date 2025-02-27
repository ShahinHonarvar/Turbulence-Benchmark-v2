import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        m, n = mat.shape
        for top_row in range(m):
            for bottom_row in range(top_row, m):
                for left_col in range(n):
                    for right_col in range(left_col, n):
                        yield mat[top_row:bottom_row + 1, left_col:right_col + 1]
    result = []
    for submat in get_submatrices(matrix):
        if np.sum(submat) == -59:
            result.append(submat)
    return result