import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 111
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == n:
                for r in range(i + 1, rows + 1):
                    for c in range(j + 1, cols + 1):
                        if np.all(matrix[i:r, j:c] == n):
                            count += 1
    return count