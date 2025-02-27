import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for sr in range(0, rows):
        for sc in range(0, cols):
            for dr in range(sr, rows):
                for dc in range(sc, cols):
                    submatrix = matrix[sr:dr + 1, sc:dc + 1]
                    if submatrix.sum() == 19:
                        submatrices.append(submatrix)
    return submatrices