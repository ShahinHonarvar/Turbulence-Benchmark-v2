import numpy as np

def submatrix_with_n_numbers(matrix):
    size = 93
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + size <= rows and j + size <= cols:
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == size * size:
                    count += 1
    return count