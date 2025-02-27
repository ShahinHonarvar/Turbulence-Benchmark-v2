import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    if rows * cols < 120:
        return 0
    for i in range(rows - 11):
        for j in range(cols - 11):
            if np.size(matrix[i:i + 10, j:j + 12]) == 120:
                count += 1
    return count