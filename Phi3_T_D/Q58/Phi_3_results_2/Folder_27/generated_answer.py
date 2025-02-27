import numpy as np

def submatrix_with_n_numbers(matrix, n=77):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for k in range(min(r + 1, n), min(r + 1, rows) + 1):
                for l in range(min(c + 1, n), min(c + 1, cols) + 1):
                    if (matrix[r:r + k, c:c + l] == matrix[r:r + k, c:c + l]).all():
                        count += 1
    return count