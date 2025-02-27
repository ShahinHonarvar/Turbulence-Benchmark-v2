import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):
    results = []
    n, m = matrix.shape
    target_sum = 245
    for size in range(1, min(n, m) + 1):
        for i in range(n - size + 1):
            for j in range(m - size + 1):
                sub_matrix_sum = np.sum(matrix[i:i + size, j:j + size])
                if sub_matrix_sum == target_sum:
                    results.append(matrix[i:i + size, j:j + size])
    return results