import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def sum_submatrix(top_left, bottom_right):
        return np.sum(matrix[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1])
    for top_left_row in range(rows):
        for top_left_col in range(cols):
            for bottom_right_row in range(top_left_row, rows):
                for bottom_right_col in range(top_left_col, cols):
                    if sum_submatrix((top_left_row, top_left_col), (bottom_right_row, bottom_right_col)) == -77:
                        result.append(matrix[top_left_row:bottom_right_row + 1, top_left_col:bottom_right_col + 1].tolist())
    return result