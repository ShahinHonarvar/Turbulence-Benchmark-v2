import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target_sum):
        rows, cols = (len(mat), len(mat[0]))
        submatrices = []
        for top_row in range(rows):
            for left_col in range(cols):
                for bottom_row in range(top_row, rows):
                    for right_col in range(left_col, cols):
                        current_sum = np.sum(mat[top_row:bottom_row + 1, left_col:right_col + 1])
                        if current_sum == target_sum:
                            submatrices.append(mat[top_row:bottom_row + 1, left_col:right_col + 1])
        return submatrices
    return submatrix_sum(matrix, -61)