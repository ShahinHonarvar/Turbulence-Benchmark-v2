import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 16
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 0:
                continue
            size = 1
            while i + size <= rows and j + size <= cols:
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == n:
                    count += 1
                size += 1
    return count