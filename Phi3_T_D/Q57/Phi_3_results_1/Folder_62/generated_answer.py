import numpy as np

def get_submatrices(n, rows, cols):
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    yield n[i:k, j:l]

def submatrix_with_particular_sum(matrix):
    result = []
    for submatrix in get_submatrices(matrix, matrix.shape[0], matrix.shape[1]):
        if np.sum(submatrix) == 394:
            result.append(submatrix.tolist())
    return result