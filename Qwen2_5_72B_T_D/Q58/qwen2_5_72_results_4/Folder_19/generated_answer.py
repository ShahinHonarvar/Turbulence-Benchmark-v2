import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 17
    count = 0
    rows, cols = matrix.shape
    for row_start in range(rows - 3):
        for col_start in range(cols - 3):
            submatrix = matrix[row_start:row_start + 4, col_start:col_start + 4]
            if np.sum(submatrix == target) == 17:
                count += 1
    return count