import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(arr, target_sum, result, current_matrix, start_row, start_col):
        rows, cols = arr.shape
        for end_row in range(start_row, rows):
            for end_col in range(start_col, cols):
                submatrix = arr[start_row:end_row + 1, start_col:end_col + 1]
                if np.sum(submatrix) == target_sum:
                    result.append(submatrix)
        return result
    result = []
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            result = find_submatrices_with_sum(matrix, -9, result, [], start_row, start_col)
    return result