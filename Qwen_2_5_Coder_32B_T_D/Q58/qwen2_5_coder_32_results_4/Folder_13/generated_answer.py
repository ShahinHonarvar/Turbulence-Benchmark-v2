import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 164):
        for j in range(cols - 164):
            if matrix[i:i + 15, j:j + 15].size == 175:
                count += 1
    return count