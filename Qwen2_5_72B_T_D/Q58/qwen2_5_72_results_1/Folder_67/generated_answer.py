import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target_size = 43
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            submatrix_size = 1
            while i + submatrix_size <= rows and j + submatrix_size <= cols:
                submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
                if submatrix.size == target_size:
                    count += 1
                submatrix_size += 1
    return count