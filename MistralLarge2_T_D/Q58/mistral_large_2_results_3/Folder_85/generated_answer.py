import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    def is_valid_submatrix(start_row, start_col, size):
        if start_row + size > rows or start_col + size > cols:
            return False
        return True
    for size in range(1, min(rows, cols) + 1):
        if size * size == 13:
            for i in range(rows - size + 1):
                for j in range(cols - size + 1):
                    if is_valid_submatrix(i, j, size):
                        count += 1
    return count