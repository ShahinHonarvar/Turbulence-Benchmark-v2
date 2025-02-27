import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 45
    for i in range(rows):
        for j in range(cols):
            for size in range(1, n):
                if i + size <= rows and j + size <= cols:
                    submatrix = matrix[i:i + size, j:j + size]
                    if submatrix.size == n:
                        count += 1
    return count