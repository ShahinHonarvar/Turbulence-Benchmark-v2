import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    rows, cols = matrix.shape
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    if np.sum(matrix[r1:r2 + 1, c1:c2 + 1]) == 830:
                        results.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return results