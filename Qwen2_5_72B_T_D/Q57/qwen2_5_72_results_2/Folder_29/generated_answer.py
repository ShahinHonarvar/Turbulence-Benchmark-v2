import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(matrix, target_sum):
        row_count, col_count = matrix.shape
        result = []
        for top_row in range(row_count):
            for left_col in range(col_count):
                for bottom_row in range(top_row, row_count):
                    for right_col in range(left_col, col_count):
                        submatrix = matrix[top_row:bottom_row + 1, left_col:right_col + 1]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix)
        return result
    return find_submatrices_with_sum(matrix, 84)