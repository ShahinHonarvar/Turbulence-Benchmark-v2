import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 120
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                if size * size == target_count:
                    submatrix_count += 1
    return submatrix_count