import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + 7 < rows and j + 7 < cols:
                submatrix_size = 8
                submatrix = matrix[i:i + submatrix_size, j:j + submatrix_size]
                if submatrix.size == 84:
                    count += 1
    return count