import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for row_slice in range(rows):
        for col_slice in range(cols):
            for size in range(1, min(rows - row_slice, cols - col_slice) + 1):
                submat = matrix[row_slice:row_slice + size, col_slice:col_slice + size]
                if np.sum(submat) == -50:
                    submatrices.append(submat)
    return submatrices