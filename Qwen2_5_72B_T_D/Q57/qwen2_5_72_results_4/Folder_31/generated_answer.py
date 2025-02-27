import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(matrix, top_left, bottom_right):
        sub = matrix[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1]
        return (np.sum(sub), sub)
    rows, cols = matrix.shape
    result = []
    for tl_row in range(rows):
        for tl_col in range(cols):
            for br_row in range(tl_row, rows):
                for br_col in range(tl_col, cols):
                    total_sum, sub = sum_submatrix(matrix, (tl_row, tl_col), (br_row, br_col))
                    if total_sum == -44:
                        result.append(sub)
    return result