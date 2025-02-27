import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    target_number = 193
    total_numbers = rows * cols
    for i in range(rows):
        for j in range(cols):
            submatrix_count = 0
            for k in range(i, rows):
                for l in range(j, cols):
                    if matrix[k, l] == target_number:
                        submatrix_count += 1
            if submatrix_count == total_numbers:
                count += 1
    return count