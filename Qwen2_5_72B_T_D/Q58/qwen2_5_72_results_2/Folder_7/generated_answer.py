import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_size = 121
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 10):
        for j in range(cols - 10):
            submatrix = matrix[i:i + 11, j:j + 11]
            if submatrix.size == submatrix_size:
                count += 1
    return count