import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 96
    count = 0
    for i in range(rows):
        for j in range(cols):
            for m in range(i + 1, rows + 1):
                for n in range(j + 1, cols + 1):
                    submatrix = matrix[i:m, j:n]
                    if np.prod(submatrix.shape) == n:
                        count += 1
    return count