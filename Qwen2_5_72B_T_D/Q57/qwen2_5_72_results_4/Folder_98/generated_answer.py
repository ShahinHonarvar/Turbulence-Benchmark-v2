import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        row, col = mat.shape
        submatrices = []
        for top in range(row):
            for bottom in range(top, row):
                for left in range(col):
                    for right in range(left, col):
                        if np.sum(mat[top:bottom + 1, left:right + 1]) == target_sum:
                            submatrices.append(mat[top:bottom + 1, left:right + 1])
        return submatrices
    return find_submatrices_with_sum(np.array(matrix), 0)