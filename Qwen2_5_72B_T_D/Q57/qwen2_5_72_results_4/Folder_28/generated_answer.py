import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target):
        row, col = (len(mat), len(mat[0]))
        result = []
        for top_row in range(row):
            for left_col in range(col):
                for bottom_row in range(top_row, row):
                    for right_col in range(left_col, col):
                        if np.sum(mat[top_row:bottom_row + 1, left_col:right_col + 1]) == target:
                            result.append(mat[top_row:bottom_row + 1, left_col:right_col + 1].tolist())
        return result
    return submatrix_sum(matrix, 15)