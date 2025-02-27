import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        submatrices = []
        for r1 in range(rows):
            for c1 in range(cols):
                for r2 in range(r1 + 1, rows + 1):
                    for c2 in range(c1 + 1, cols + 1):
                        submatrix = mat[r1:r2, c1:c2]
                        submatrices.append(submatrix)
        return submatrices
    target_sum = 59
    result = []
    submatrices = get_submatrices(matrix)
    for submatrix in submatrices:
        if submatrix.sum() == target_sum:
            result.append(submatrix)
    return result