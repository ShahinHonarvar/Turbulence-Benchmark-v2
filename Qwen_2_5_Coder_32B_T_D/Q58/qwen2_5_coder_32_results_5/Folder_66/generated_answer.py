import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    if np.sum(matrix[i:m + 1, j:n + 1]) == 42:
                        count += 1
    return count