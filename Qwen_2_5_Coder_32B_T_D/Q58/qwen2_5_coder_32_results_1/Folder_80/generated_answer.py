import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 17):
        for j in range(cols - 17):
            if matrix[i:i + 18, j:j + 18].size == 180:
                count += 1
    return count