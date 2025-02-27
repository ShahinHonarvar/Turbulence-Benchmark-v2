import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        submatrices = []
        for i in range(rows):
            for j in range(cols):
                for r in range(i, rows):
                    for c in range(j, cols):
                        submatrix = matrix[i:r + 1, j:c + 1]
                        submatrices.append(submatrix)
        return submatrices
    result = []
    submatrices = get_submatrices(matrix)
    for submatrix in submatrices:
        if submatrix.sum() == -9:
            result.append(submatrix.tolist())
    return result