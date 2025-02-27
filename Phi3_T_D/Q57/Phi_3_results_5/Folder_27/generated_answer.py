import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    valid_submatrices = []
    for i, j in product(range(matrix.shape[0]), range(matrix.shape[1])):
        for k, l in product(range(i + 1, matrix.shape[0] + 1), range(j + 1, matrix.shape[1] + 1)):
            submatrix = matrix[i:k, j:l]
            if submatrix.sum() == 77:
                valid_submatrices.append(submatrix)
    return valid_submatrices