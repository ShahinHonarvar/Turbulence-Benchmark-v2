import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 76
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for r_size in range(1, rows - i + 1):
                for c_size in range(1, cols - j + 1):
                    if r_size * c_size == target_count:
                        submatrix = matrix[i:i + r_size, j:j + c_size]
                        count += 1
    return count