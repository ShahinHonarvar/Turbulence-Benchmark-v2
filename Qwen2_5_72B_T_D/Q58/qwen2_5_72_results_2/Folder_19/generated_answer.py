import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 17
    found_submatrices = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i:i + 4, j:j + 4].size == target_count:
                found_submatrices += 1
    return found_submatrices if found_submatrices > 0 else 0