import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 43
    found_count = 0
    rows, cols = matrix.shape
    for r in range(rows - 1):
        for c in range(cols - 1):
            submatrix = matrix[r:r + 2, c:c + 2]
            if np.count_nonzero(submatrix == target_count) == 43:
                found_count += 1
    return found_count