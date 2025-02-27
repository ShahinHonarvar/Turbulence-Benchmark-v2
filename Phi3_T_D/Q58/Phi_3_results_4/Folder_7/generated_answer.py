import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    n = 121
    count = 0
    for i, j in product(range(len(matrix)), repeat=2):
        for k in range(i + 1, len(matrix) + 1):
            for l in range(j + 1, len(matrix[0]) + 1):
                submatrix = matrix[i:k, j:l]
                if submatrix.size == n:
                    count += 1
    return count