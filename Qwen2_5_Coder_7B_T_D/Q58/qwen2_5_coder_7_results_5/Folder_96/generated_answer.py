import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 20
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    if np.sum(matrix[i:k, j:l]) == n:
                        count += 1
    return count