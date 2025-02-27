import numpy as np

def find_submatrix_with_sum(matrix, target_sum):
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == target_sum:
                        return submatrix
    return None