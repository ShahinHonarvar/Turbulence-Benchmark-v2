import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, result):
        rows, cols = mat.shape
        for top_row in range(rows):
            for left_col in range(cols):
                for bottom_row in range(top_row + 1, rows + 1):
                    for right_col in range(left_col + 1, cols + 1):
                        submat_sum = np.sum(mat[top_row:bottom_row, left_col:right_col])
                        if submat_sum == target_sum:
                            result.append(mat[top_row:bottom_row, left_col:right_col])
    result = []
    find_submatrices_with_sum(matrix, 382, result)
    return result