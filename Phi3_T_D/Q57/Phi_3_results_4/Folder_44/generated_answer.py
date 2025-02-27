import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    n_rows, n_cols = matrix.shape
    result = []
    for i in range(n_rows):
        for j in range(n_cols):
            for size in range(1, min(n_rows - i, n_cols - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.sum() == 830:
                    result.append(submatrix)
    return result