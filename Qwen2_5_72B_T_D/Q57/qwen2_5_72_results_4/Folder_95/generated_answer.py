import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(arr, target_sum, start_row, start_col, rows, cols, result):
        for end_row in range(start_row, rows):
            for end_col in range(start_col, cols):
                current_sum = np.sum(arr[start_row:end_row + 1, start_col:end_col + 1])
                if current_sum == target_sum:
                    result.append(arr[start_row:end_row + 1, start_col:end_col + 1])
    result = []
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            find_submatrices_with_sum(matrix, 19, start_row, start_col, rows, cols, result)
    return result