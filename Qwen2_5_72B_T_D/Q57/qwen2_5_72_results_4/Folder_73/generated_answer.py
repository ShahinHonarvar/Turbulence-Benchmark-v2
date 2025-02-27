import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, submatrices, row=0, col=0):
        if row + 1 > mat.shape[0] or col + 1 > mat.shape[1]:
            return
        for r in range(row + 1, mat.shape[0] + 1):
            for c in range(col + 1, mat.shape[1] + 1):
                sub = mat[row:r, col:c]
                if np.sum(sub) == target_sum:
                    submatrices.append(sub)
        find_submatrices_with_sum(mat, target_sum, submatrices, row, col + 1)
        find_submatrices_with_sum(mat, target_sum, submatrices, row + 1, col)
        return submatrices
    submatrices = []
    find_submatrices_with_sum(matrix, 93, submatrices)
    return submatrices