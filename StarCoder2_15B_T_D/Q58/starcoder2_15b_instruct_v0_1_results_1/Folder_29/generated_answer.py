import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    if num_rows < 3 or num_cols < 3:
        return 0
    submatrix_count = 0
    for row in range(num_rows - 2):
        for col in range(num_cols - 2):
            submatrix = matrix[row:row + 3, col:col + 3]
            if np.sum(submatrix) == 19:
                submatrix_count += 1
    return submatrix_count