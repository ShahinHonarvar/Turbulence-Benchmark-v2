import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix.shape) != 2:
        return 0
    count = 0
    rows, cols = matrix.shape
    for sr in range(rows):
        for sc in range(cols):
            for hr in range(sr, rows):
                for hc in range(sc, cols):
                    submatrix = matrix[sr:hr + 1, sc:hc + 1]
                    if np.size(submatrix) == 67:
                        count += 1
    return count