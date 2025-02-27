import numpy as np

def get_submatrices(matrix):
    m, n = matrix.shape
    submatrices = []
    for size in range(1, m + 1):
        for row in range(m - size + 1):
            for col in range(n - size + 1):
                yield matrix[row:row + size, col:col + size]

def submatrix_with_particular_sum(matrix):
    target_sum = -137
    for submat in get_submatrices(matrix):
        if np.sum(submat) == target_sum:
            submatrices.append(submat.tolist())
    return submatrices