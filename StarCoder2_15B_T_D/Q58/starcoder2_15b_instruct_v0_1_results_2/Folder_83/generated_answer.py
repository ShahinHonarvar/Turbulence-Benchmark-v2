import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for row in range(num_rows - 1):
        for col in range(num_cols - 1):
            submatrix = matrix[row:row + 2, col:col + 2]
            if np.sum(submatrix) == 47:
                count += 1
    return count