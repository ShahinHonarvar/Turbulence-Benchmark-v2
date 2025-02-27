import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        row_count, col_count = mat.shape
        submatrices = []
        for top_row in range(row_count):
            for left_col in range(col_count):
                for bottom_row in range(top_row + 1, row_count + 1):
                    for right_col in range(left_col + 1, col_count + 1):
                        submatrix_sum = np.sum(mat[top_row:bottom_row, left_col:right_col])
                        if submatrix_sum == target_sum:
                            submatrices.append(mat[top_row:bottom_row, left_col:right_col])
        return submatrices
    return find_submatrices_with_sum(matrix, -90)