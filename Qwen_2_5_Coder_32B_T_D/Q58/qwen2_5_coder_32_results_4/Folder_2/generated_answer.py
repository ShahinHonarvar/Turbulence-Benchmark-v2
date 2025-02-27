import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 107
    if matrix.size < n:
        return 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    if (r - i + 1) * (c - j + 1) == n:
                        if matrix[i:r + 1, j:c + 1].size == n:
                            count += 1
    return count