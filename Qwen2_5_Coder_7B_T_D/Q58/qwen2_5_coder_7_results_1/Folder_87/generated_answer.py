import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == 96:
                count += 1
    return count