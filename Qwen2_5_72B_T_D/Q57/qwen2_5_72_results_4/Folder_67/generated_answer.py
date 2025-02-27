import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(r, c, target_sum):
        result = []
        for rr in range(r + 1):
            for cc in range(c + 1):
                for i in range(r - rr + 1):
                    for j in range(c - cc + 1):
                        sub = matrix[i:i + rr, j:j + cc]
                        if np.sum(sub) == target_sum:
                            result.append(sub)
        return result
    r, c = matrix.shape
    return find_submatrices(r, c, 40)