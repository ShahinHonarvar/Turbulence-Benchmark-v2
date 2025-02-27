import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(mat):
        rows, cols = mat.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        yield mat[r1:r2 + 1, c1:c2 + 1]
    results = []
    for submat in submatrices(matrix):
        if submat.sum() == -6:
            results.append(submat)
    return results