import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    def count_submatrices(start_row, start_col, size):
        if start_row + size > rows or start_col + size > cols:
            return 0
        submatrix = matrix[start_row:start_row + size, start_col:start_col + size]
        if np.count_nonzero(submatrix) == 39:
            return 1
        return 0
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                count += count_submatrices(i, j, size)
    return count