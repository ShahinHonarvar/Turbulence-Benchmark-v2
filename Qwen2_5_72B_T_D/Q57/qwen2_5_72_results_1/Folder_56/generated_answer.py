import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum_helper(arr, target):
        result = []
        rows, cols = arr.shape
        for top_row in range(rows):
            for left_col in range(cols):
                for bottom_row in range(top_row + 1, rows + 1):
                    for right_col in range(left_col + 1, cols + 1):
                        if np.sum(arr[top_row:bottom_row, left_col:right_col]) == target:
                            result.append(arr[top_row:bottom_row, left_col:right_col].tolist())
        return result
    return submatrix_sum_helper(matrix, -50)