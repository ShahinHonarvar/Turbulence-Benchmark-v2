import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape

    def is_valid_submatrix(start_row, start_col, end_row, end_col):
        if end_row > rows or end_col > cols:
            return False
        return np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1]) == 84
    for size in range(1, min(rows, cols) + 1):
        for row in range(rows - size + 1):
            for col in range(cols - size + 1):
                if is_valid_submatrix(row, col, row + size - 1, col + size - 1):
                    submatrices.append(matrix[row:row + size, col:col + size])
    return submatrices