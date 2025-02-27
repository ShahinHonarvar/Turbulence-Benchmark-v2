import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 85
    count = 0

    def count_submatrices(r, c):
        nonlocal count
        for i in range(r, rows + 1):
            for j in range(c, cols + 1):
                submatrix = matrix[r:i, c:j]
                if submatrix.size == n:
                    count += 1
    for i in range(rows):
        for j in range(cols):
            count_submatrices(i, j)
    return count