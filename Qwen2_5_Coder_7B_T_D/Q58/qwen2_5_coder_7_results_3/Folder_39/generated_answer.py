import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 58, rows):
                for l in range(j + 58, cols):
                    if np.sum(matrix[i:k + 1, j:l + 1]) == 59:
                        count += 1
    return count