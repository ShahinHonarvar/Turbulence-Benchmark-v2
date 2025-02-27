import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(m):
        h, w = m.shape
        return [m[i:i + h2, j:j + w2] for h2 in range(1, h + 1) for w2 in range(1, w + 1) for i in range(h + 1 - h2) for j in range(w + 1 - w2)]

    def check_sum(sub):
        return np.sum(sub) == -61
    return [sub for sub in all_submatrices(matrix) if check_sum(sub) and sub.size > 0]