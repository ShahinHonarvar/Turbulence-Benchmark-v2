import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    size = 7
    for i in range(rows - size + 1):
        for j in range(cols - size + 1):
            count += 1
    return count if count > 0 else 0