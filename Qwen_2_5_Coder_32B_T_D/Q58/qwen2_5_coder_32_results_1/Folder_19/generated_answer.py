import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 3):
        for j in range(cols - 5):
            if matrix[i:i + 4, j:j + 6].size == 17:
                count += 1
    return count