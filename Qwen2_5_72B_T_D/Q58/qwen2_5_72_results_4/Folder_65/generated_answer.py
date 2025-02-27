import numpy as np

def submatrix_with_n_numbers(matrix):
    total_rows, total_cols = matrix.shape
    count = 0
    for i in range(total_rows - 5):
        for j in range(total_cols - 6):
            if np.prod(matrix[i:i + 5, j:j + 7].shape) == 35:
                count += 1
    return count