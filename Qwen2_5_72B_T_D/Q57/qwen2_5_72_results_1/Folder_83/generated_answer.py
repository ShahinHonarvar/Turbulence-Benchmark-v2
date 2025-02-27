import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrix_sum(mat, target_sum):
        row, col = mat.shape
        result = []
        for top_row in range(row):
            for left_col in range(col):
                for bottom_row in range(top_row + 1, row + 1):
                    for right_col in range(left_col + 1, col + 1):
                        submatrix = mat[top_row:bottom_row, left_col:right_col]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix)
        return result
    return find_submatrix_sum(matrix, -15)