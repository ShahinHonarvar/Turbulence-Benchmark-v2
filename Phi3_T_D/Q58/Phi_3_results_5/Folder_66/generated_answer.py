import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    def count_submatrix(i_start, j_start, size):
        return 1 if np.all(matrix[i_start:i_start + size, j_start:j_start + size] == 42) else 0
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                count += count_submatrix(i, j, size)
    return count