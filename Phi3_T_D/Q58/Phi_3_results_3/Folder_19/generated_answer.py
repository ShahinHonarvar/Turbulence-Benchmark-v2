import numpy as np

def submatrix_with_n_numbers(matrix):
    if not matrix.shape[0] or not matrix.shape[1]:
        return 0
    count = 0
    rows, cols = matrix.shape
    for sr in range(rows):
        for sc in range(cols):
            for hr in range(sr, rows):
                for hc in range(sc, cols):
                    submatrix = matrix[sr:hr + 1, sc:hc + 1]
                    if submatrix.size == 17:
                        count += 1
    return count