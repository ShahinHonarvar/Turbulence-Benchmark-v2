import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 34
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == n:
                        count += 1
    return count