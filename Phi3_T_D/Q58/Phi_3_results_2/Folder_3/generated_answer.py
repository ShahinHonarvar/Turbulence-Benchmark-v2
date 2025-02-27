import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r_idx in range(rows):
        for c_idx in range(cols):
            for subrows in range(1, rows - r_idx + 1):
                for subcols in range(1, cols - c_idx + 1):
                    submatrix = matrix[r_idx:r_idx + subrows, c_idx:c_idx + subcols]
                    if submatrix.size == 54:
                        count += 1
    return count