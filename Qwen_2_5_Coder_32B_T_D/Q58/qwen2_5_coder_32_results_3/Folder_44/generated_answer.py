import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 191
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            total = matrix[r, c]
            if total == target_count:
                count += 1
            for sub_r in range(r + 1, rows):
                for sub_c in range(c + 1, cols):
                    total += matrix[sub_r, sub_c]
                    if total == target_count:
                        count += 1
    return count