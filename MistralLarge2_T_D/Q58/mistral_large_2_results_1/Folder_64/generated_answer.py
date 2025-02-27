import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    def is_valid_submatrix(start_row, start_col, size):
        if start_row + size > rows or start_col + size > cols:
            return False
        submatrix = matrix[start_row:start_row + size, start_col:start_col + size]
        return np.count_nonzero(submatrix) == 7
    for size in range(1, max(rows, cols) + 1):
        for start_row in range(rows):
            for start_col in range(cols):
                if is_valid_submatrix(start_row, start_col, size):
                    count += 1
    return count