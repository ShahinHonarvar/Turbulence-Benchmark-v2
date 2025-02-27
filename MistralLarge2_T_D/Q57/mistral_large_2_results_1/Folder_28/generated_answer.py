import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        rows, cols = matrix.shape
        submatrices = []
        for r1 in range(rows):
            for c1 in range(cols):
                for r2 in range(r1 + 1, rows + 1):
                    for c2 in range(c1 + 1, cols + 1):
                        submatrices.append(matrix[r1:r2, c1:c2])
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == 15]
    return result