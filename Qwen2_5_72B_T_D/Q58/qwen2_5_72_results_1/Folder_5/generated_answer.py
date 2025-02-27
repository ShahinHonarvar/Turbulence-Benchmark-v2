import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 63
    count = 0
    rows, cols = matrix.shape
    if rows * cols < n:
        return 0
    for i in range(rows - n // cols + 1):
        for j in range(cols - n // (rows - i) + 1):
            if i + n // cols <= rows and j + n // (rows - i) <= cols:
                count += 1
    return count