import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 93
    rows, cols = matrix.shape
    if rows * cols < target_count:
        return 0
    valid_submatrices = 0
    for i in range(rows):
        for j in range(cols):
            if (i + 1) * (j + 1) == target_count:
                valid_submatrices += 1
            if (rows - i) * (j + 1) == target_count:
                valid_submatrices += 1
            if (i + 1) * (cols - j) == target_count:
                valid_submatrices += 1
            if (rows - i) * (cols - j) == target_count:
                valid_submatrices += 1
    return valid_submatrices