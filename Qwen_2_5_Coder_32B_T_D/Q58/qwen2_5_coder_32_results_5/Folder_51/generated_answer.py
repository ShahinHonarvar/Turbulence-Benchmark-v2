import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 8):
        for j in range(cols - 8):
            if matrix[i:i + 9, j:j + 9].size == 95:
                count += 1
    return count