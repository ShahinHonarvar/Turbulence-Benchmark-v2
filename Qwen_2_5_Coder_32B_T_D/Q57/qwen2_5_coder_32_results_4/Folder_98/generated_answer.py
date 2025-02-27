import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_zero_submatrices(top, left, bottom, right):
        if top > bottom or left > right:
            return []
        submatrices = []
        for t in range(top, bottom + 1):
            for l in range(left, right + 1):
                for b in range(t, bottom + 1):
                    for r in range(l, right + 1):
                        submatrix = matrix[t:b + 1, l:r + 1]
                        if np.sum(submatrix) == 0:
                            submatrices.append(submatrix)
        return submatrices
    height, width = matrix.shape
    return sum_zero_submatrices(0, 0, height - 1, width - 1)