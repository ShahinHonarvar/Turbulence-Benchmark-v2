import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for r_begin, r_end in product(range(rows), range(r_begin + 1, rows + 1)):
        for c_begin, c_end in product(range(cols), range(c_begin + 1, cols + 1)):
            submatrix = matrix[r_begin:r_end, c_begin:c_end]
            if submatrix.sum() == -87:
                submatrices.append(submatrix)
    return submatrices