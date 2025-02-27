import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 175
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - target_count + 1):
        for j in range(cols - target_count + 1):
            submatrix = matrix[i:i + target_count, j:j + target_count]
            if submatrix.size == target_count:
                count += 1
    return count