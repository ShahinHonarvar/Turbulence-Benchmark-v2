import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    results = []
    for start_i in range(n):
        for end_i in range(start_i, n):
            for start_j in range(m):
                for end_j in range(start_j, m):
                    submatrix = matrix[start_i:end_i + 1, start_j:end_j + 1]
                    if submatrix.sum() == -452:
                        results.append(submatrix)
    return results