import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size < 91:
        return 0
    count = 0
    rows, cols = matrix.shape
    for r in range(rows - 8):
        for c in range(cols - 8):
            if matrix[r:r + 9, c:c + 9].size == 91:
                count += 1
    return count