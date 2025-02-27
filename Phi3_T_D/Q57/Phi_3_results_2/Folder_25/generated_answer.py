import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    rows, cols = matrix.shape

    def helper(row_start, row_end, col_start, col_end):
        if row_end <= row_start or col_end <= col_start:
            return
        submatrix = matrix[row_start:row_end, col_start:col_end]
        if np.sum(submatrix) == -20:
            results.append(submatrix)
        helper(row_start + 1, row_end, col_start, col_end)
        helper(row_start, row_end - 1, col_start, col_end)
        helper(row_start, row_end, col_start + 1, col_end)
        helper(row_start, row_end, col_start, col_end - 1)
        helper(row_start + 1, row_end - 1, col_start + 1, col_end - 1)
    helper(0, rows, 0, cols)
    return results