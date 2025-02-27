import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix, sum_target):
        nrows, ncols = matrix.shape
        submatrices = []
        for top in range(nrows):
            for left in range(ncols):
                for bottom in range(top, nrows):
                    for right in range(left, ncols):
                        submatrix = matrix[top:bottom + 1, left:right + 1]
                        if np.sum(submatrix) == -4:
                            submatrices.append(submatrix)
        return submatrices
    return all_submatrices(matrix, -4)