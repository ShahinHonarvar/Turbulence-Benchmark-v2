import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_2_integers_submatrix(start_row, start_col, rows, cols):
        return (rows < matrix.shape[0] and cols < matrix.shape[1]) and np.count_nonzero(mat[start_row:start_row + rows, start_col:start_col + cols]) == 2
    rows, cols = matrix.shape
    count = 0
    for row in range(0, rows):
        for col in range(0, cols):
            for h_size in range(1, rows - row + 1):
                for w_size in range(1, cols - col + 1):
                    if count_2_integers_submatrix(row, col, h_size, w_size):
                        count += 1
    return count