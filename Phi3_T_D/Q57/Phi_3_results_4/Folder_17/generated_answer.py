import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_all_submatrices(matrix):
        rows, cols = matrix.shape
        submatrices = []
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        sub = matrix[r1:r2 + 1, c1:c2 + 1]
                        if np.sum(sub) == 398:
                            submatrices.append(sub)
        return submatrices
    return get_all_submatrices(matrix)