import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, submatrices):
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                for r in range(i + 1, rows + 1):
                    for c in range(j + 1, cols + 1):
                        submatrix = mat[i:r, j:c]
                        if np.sum(submatrix) == target_sum:
                            submatrices.append(submatrix)
    submatrices = []
    find_submatrices_with_sum(matrix, 69, submatrices)
    return submatrices