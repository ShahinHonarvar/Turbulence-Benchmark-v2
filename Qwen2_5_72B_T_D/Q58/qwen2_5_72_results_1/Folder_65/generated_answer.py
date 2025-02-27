import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 35
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (i + 1) * (j + 1) == n:
                if i <= rows and j <= cols:
                    count += 1
    return count if count > 0 else 0