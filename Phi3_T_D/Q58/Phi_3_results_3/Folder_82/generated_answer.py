import numpy as np

def submatrix_with_n_numbers(matrix, n=99):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for size in range(min(rows - i, cols - j)):
                submatrix = matrix[i:i + size + 1, j:j + size + 1]
                if submatrix.size == n:
                    count += 1
    return count