import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows - 5):
        for c in range(cols - 5):
            if np.count_nonzero(matrix[r:r + 5, c:c + 5].flatten() == 34) == 34:
                count += 1
    return count