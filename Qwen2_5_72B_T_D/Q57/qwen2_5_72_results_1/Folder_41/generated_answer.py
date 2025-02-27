import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        R, C = mat.shape
        for top in range(R):
            for bottom in range(top, R):
                for left in range(C):
                    for right in range(left, C):
                        yield mat[top:bottom + 1, left:right + 1]
    target_sum_submatrices = []
    for submat in get_submatrices(matrix):
        if np.sum(submat) == -26:
            target_sum_submatrices.append(submat)
    return target_sum_submatrices