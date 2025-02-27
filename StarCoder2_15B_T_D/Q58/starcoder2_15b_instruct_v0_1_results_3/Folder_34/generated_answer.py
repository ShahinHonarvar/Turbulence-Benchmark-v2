import numpy as np
from itertools import submatrices

def submatrix_with_n_numbers(matrix):
    count = 0
    for sub_matrix in submatrices(matrix, 83):
        count += 1
    return count