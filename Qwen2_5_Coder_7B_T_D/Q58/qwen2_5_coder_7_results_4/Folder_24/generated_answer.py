import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 51, rows + 1):
                for l in range(j + 51, cols + 1):
                    if np.sum(matrix[i:k, j:l]) == 51:
                        count += 1
    return count