import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        submatrices = []
        rows, cols = mat.shape
        for top_row in range(rows):
            for left_col in range(cols):
                for bottom_row in range(top_row + 1, rows + 1):
                    for right_col in range(left_col + 1, cols + 1):
                        submatrices.append(mat[top_row:bottom_row, left_col:right_col])
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submat for submat in submatrices if np.sum(submat) == -83]
    return result