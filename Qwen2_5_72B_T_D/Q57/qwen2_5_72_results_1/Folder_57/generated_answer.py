import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(matrix, target):
        rows, cols = matrix.shape
        submatrices = []
        for top_row in range(rows):
            for left_col in range(cols):
                for bottom_row in range(top_row + 1, rows + 1):
                    for right_col in range(left_col + 1, cols + 1):
                        submatrix = matrix[top_row:bottom_row, left_col:right_col]
                        if np.sum(submatrix) == target:
                            submatrices.append(submatrix)
        return submatrices
    return find_submatrices_with_sum(matrix, 13)