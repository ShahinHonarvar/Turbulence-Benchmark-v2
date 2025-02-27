import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 99
    for i in range(rows):
        for j in range(cols):
            for k in range(1, rows - i + 1):
                for l in range(1, cols - j + 1):
                    if np.all(matrix[i:i + k, j:j + l] == n):
                        count += 1
    return count