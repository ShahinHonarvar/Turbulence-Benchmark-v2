import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for sr in range(rows):
        for sc in range(cols):
            for dr in range(sr, rows):
                for dc in range(sc, cols):
                    submat = matrix[sr:dr + 1, sc:dc + 1]
                    if submat.sum() == -15:
                        result.append(submat)
    return result