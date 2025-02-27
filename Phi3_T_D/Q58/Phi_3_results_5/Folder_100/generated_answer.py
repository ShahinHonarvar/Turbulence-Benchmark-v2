import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for sr in range(rows):
        for sc in range(cols):
            for dr in range(sr, rows):
                for dc in range(sc, cols):
                    submatrix = matrix[sr:dr + 1, sc:dc + 1]
                    if submatrix.size == 10:
                        count += 1
    return count