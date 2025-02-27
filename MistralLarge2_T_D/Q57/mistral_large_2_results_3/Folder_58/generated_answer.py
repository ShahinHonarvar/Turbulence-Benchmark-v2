import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(start_row, start_col, end_row, end_col):
        return prefix_sum[end_row + 1, end_col + 1] - prefix_sum[start_row, end_col + 1] - prefix_sum[end_row + 1, start_col] + prefix_sum[start_row, start_col]
    rows, cols = matrix.shape
    prefix_sum = np.zeros((rows + 1, cols + 1), dtype=int)
    for i in range(rows):
        for j in range(cols):
            prefix_sum[i + 1, j + 1] = matrix[i, j] + prefix_sum[i, j + 1] + prefix_sum[i + 1, j] - prefix_sum[i, j]
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):
                    if submatrix_sum(start_row, start_col, end_row, end_col) == -137:
                        result.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
    return result