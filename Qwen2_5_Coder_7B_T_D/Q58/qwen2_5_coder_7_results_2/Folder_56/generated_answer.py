import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 68, rows + 1):
                for l in range(j + 68, cols + 1):
                    if np.sum(matrix[i:k, j:l]) == 68:
                        count += 1
    return count