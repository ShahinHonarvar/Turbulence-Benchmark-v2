import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for top_left in product(range(rows), repeat=2):
        for bottom_right in product(range(top_left[0] + 1, rows + 1), range(top_left[1] + 1, cols + 1)):
            submatrix = matrix[top_left[0]:bottom_right[0], top_left[1]:bottom_right[1]]
            if submatrix.sum() == -4:
                submatrices.append(submatrix)
    return submatrices