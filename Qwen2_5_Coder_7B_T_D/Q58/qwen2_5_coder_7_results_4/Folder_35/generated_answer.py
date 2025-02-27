import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 2, rows):
                for l in range(j + 2, cols):
                    if np.all(matrix[i:k, j:l] == 111):
                        count += 1
    return count