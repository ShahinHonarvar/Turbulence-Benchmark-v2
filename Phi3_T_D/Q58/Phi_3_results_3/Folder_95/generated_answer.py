import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 87
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for p in range(i, rows):
                for q in range(j, cols):
                    submatrix = matrix[i:p + 1, j:q + 1]
                    if np.sum(submatrix == n) == (p - i + 1) * (q - j + 1):
                        count += 1
    return count