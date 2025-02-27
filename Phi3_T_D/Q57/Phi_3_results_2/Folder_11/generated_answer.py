import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy array')
    rows, cols = matrix.shape
    result = []

    def check_sum(sub):
        return np.sum(sub) == 38

    def add_submatrix(row_start, row_end, col_start, col_end):
        if row_start < 0 or row_end > rows or col_start < 0 or (col_end > cols):
            return
        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
        if check_sum(submatrix):
            result.append(submatrix)
            for new_row in range(row_start, row_end):
                add_submatrix(new_row, row_end, col_start, col_end)
    for row in range(rows):
        for col in range(cols):
            add_submatrix(row, rows - 1, col, cols - 1)
    return result