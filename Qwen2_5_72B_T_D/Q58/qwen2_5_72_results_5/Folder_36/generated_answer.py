import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_size = 131
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (rows - i) * (cols - j) == target_size:
                count += 1
    return count