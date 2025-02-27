import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for row_start, row_end in product(range(rows), repeat=2):
        for col_start, col_end in product(range(cols), repeat=2):
            submatrix = matrix[row_start:row_end, col_start:col_end]
            if np.sum(submatrix) == 59:
                result.append(submatrix)
    return result