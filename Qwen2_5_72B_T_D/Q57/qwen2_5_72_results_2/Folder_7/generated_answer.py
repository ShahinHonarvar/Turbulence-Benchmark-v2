import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum):
        row_count, col_count = matrix.shape
        submatrices = []
        for top_row in range(row_count):
            for left_col in range(col_count):
                for bottom_row in range(top_row + 1, row_count + 1):
                    for right_col in range(left_col + 1, col_count + 1):
                        submatrix = matrix[top_row:bottom_row, left_col:right_col]
                        if np.sum(submatrix) == target_sum:
                            submatrices.append(submatrix)
        return submatrices
    return find_submatrices(np.array(matrix), -128)