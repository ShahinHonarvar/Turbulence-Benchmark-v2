import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 3, rows):
                for l in range(j + 3, cols):
                    if np.sum(matrix[i:k, j:l]) == 16:
                        count += 1
    return count