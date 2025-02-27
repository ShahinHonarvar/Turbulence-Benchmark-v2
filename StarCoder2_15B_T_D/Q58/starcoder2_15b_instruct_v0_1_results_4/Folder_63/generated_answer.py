import numpy as np
import itertools

def submatrix_with_n_numbers(matrix):
    n = 57
    rows, cols = matrix.shape
    submatrix_counts = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == n:
                        submatrix_counts += 1
    return submatrix_counts