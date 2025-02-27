import numpy as np

def all_submatrices(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for m in range(i + 1, rows + 1):
                for n in range(j + 1, cols + 1):
                    submatrices.append(matrix[i:m, j:n])
    return submatrices

def submatrix_with_particular_sum(matrix):
    target_sum = -936
    all_subs = all_submatrices(matrix)
    results = [sub for sub in all_subs if sub.sum() == target_sum]
    return results