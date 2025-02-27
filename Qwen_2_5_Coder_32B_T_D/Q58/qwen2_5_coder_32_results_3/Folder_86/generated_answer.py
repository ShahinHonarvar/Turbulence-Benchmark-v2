import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 12 + 1):
        for j in range(cols - 12 + 1):
            if np.sum(matrix[i:i + 12, j:j + 12]) == 138:
                count += 1
    return count