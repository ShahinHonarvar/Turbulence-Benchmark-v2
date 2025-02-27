import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for sr in range(rows):
        for sc in range(cols):
            for tr in range(sr, rows):
                for tc in range(sc, cols):
                    submatrix = matrix[sr:tr + 1, sc:tc + 1]
                    if np.sum(submatrix) == -936:
                        result.append(submatrix)
    return result