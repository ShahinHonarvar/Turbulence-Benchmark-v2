import numpy as np

def submatrix_with_particular_sum(matrix):
    sum_target = 59
    result = []

    def find_submatrices_rec(i, j, path=[]):
        if i < 0 or j < 0:
            return
        if i == matrix.shape[0]:
            return
        if j == matrix.shape[1]:
            i += 1
            j = 0
        if sum((np.sum(matrix[x, j:j + k]) for x, k in enumerate(path + [len(path) + 1]))) == sum_target:
            result.append(matrix[len(path):i, j:j + len(path) + 1])
        find_submatrices_rec(i, j + 1, path + [i - len(path)])
        find_submatrices_rec(i + 1, j, path)
    find_submatrices_rec(1, 0)
    return result