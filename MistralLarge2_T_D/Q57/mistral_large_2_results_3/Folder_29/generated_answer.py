import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum):
        result = []
        rows, cols = matrix.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix)
        return result
    return find_submatrices(matrix, 84)