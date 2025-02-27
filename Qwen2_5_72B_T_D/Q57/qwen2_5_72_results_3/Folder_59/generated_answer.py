import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target):
        rows, cols = matrix.shape
        submatrices = []
        for top_row in range(rows):
            for left_col in range(cols):
                for bottom_row in range(top_row, rows):
                    for right_col in range(left_col, cols):
                        submat = matrix[top_row:bottom_row + 1, left_col:right_col + 1]
                        if np.sum(submat) == target:
                            submatrices.append(submat)
        return submatrices
    return find_submatrices(matrix, 2)