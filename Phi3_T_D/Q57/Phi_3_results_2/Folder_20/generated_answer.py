import numpy as np
import itertools

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i, j, k, l in itertools.product(range(rows), range(cols), range(rows), range(cols)):
        submatrix = matrix[i:k, j:l]
        if submatrix.size > 0 and submatrix.sum() == -57:
            submatrices.append(np.array(submatrix))
    return submatrices