import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for layer in range(min(rows, cols) // 2):
        for row_top in range(layer, rows - layer):
            for col_left in range(layer, cols - layer):
                if np.all(matrix[row_top - layer:row_top + layer + 1, col_left - layer:col_left + layer + 1]):
                    count += 1
    return count