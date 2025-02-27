import numpy as np

def get_submatrices(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i1 in range(rows):
        for j1 in range(cols):
            for i2 in range(i1, rows):
                for j2 in range(j1, cols):
                    submatrix = matrix[i1:i2 + 1, j1:j2 + 1]
                    submatrices.append(submatrix)
    return submatrices

def submatrix_with_particular_sum(matrix):
    target_sum = 432
    submatrices = get_submatrices(matrix)
    result = [np.array(submatrix) for submatrix in submatrices if np.sum(submatrix) == target_sum]
    return result