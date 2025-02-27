import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 127
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + 11 < rows and j + 11 < cols:
                submatrix = matrix[i:i + 12, j:j + 12]
                if submatrix.size == n:
                    count += 1
    return count