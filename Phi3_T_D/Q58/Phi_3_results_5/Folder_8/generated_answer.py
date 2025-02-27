import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.ndim != 2:
        raise ValueError('Matrix must be two-dimensional')
    rows, cols = matrix.shape
    count = 0
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == size ** 2 == 29:
                    count += 1
    return count