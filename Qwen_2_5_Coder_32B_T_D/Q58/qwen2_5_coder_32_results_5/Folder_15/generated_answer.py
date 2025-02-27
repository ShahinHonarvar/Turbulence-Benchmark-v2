import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols - 1):
            count += 1
        for j in range(rows - 1):
            count += 1
    return count