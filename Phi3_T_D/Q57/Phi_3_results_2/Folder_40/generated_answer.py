import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def get_all_submatrices(r1, c1, size):
        for r in range(r1, rows - size + 1):
            for c in range(c1, cols - size + 1):
                submatrix = matrix[r:r + size, c:c + size]
                if submatrix.sum() == -10:
                    result.append(submatrix.tolist())
    for size in range(1, min(rows, cols) + 1):
        get_all_submatrices(0, 0, size)
    return result