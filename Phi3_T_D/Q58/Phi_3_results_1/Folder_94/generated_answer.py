import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 93
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub = matrix[i:k + 1, j:l + 1]
                    if sub.size == n:
                        count += 1
    return count