import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        rows, cols = matrix.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        yield matrix[r1:r2 + 1, c1:c2 + 1]

    def has_sum(submatrix, target=-27):
        return np.sum(submatrix) == target
    return [submat for submat in all_submatrices(matrix) if has_sum(submat)]