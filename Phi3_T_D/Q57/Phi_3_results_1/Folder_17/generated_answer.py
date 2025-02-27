import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        m, n = mat.shape
        subs = []
        for i1 in range(m):
            for j1 in range(n):
                for i2 in range(i1, m):
                    for j2 in range(j1, n):
                        subs.append(mat[i1:i2 + 1, j1:j2 + 1])
        return subs
    target_sum = 398
    matrix = np.array(matrix)
    all_subs = get_submatrices(matrix)
    result = [sub for sub in all_subs if sub.sum() == target_sum]
    return result