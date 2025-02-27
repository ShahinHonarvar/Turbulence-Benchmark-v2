import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 2, rows):
                for l in range(j + 2, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 33:
                        count += 1
    return count