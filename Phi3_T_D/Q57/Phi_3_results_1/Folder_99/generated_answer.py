import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r_start, r_end in product(range(rows), range(r_start + 1, rows + 1)):
        for c_start, c_end in product(range(cols), range(c_start + 1, cols + 1)):
            submatrix = matrix[r_start:r_end, c_start:c_end]
            if submatrix.sum() == -185:
                result.append(submatrix)
    return result