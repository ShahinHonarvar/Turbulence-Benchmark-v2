import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(m):
        submatrices = []
        rows, cols = m.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        submatrices.append(m[r1:r2 + 1, c1:c2 + 1])
        return submatrices

    def sum_equals_100(submatrix):
        return np.sum(submatrix) == 100
    all_subs = all_submatrices(matrix)
    result = [sub for sub in all_subs if sum_equals_100(sub)]
    return result