import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    def check_submatrix(start_row, start_col, end_row, end_col):
        return np.count_nonzero(matrix[start_row:end_row + 1, start_col:end_col + 1] == 1) == 1
    for row in range(rows):
        for col in range(cols):
            if matrix[row, col] == 1:
                count += 1
                for i in range(row + 1, rows):
                    for j in range(col + 1, cols):
                        if check_submatrix(row, col, i, j):
                            count += 1
    return count