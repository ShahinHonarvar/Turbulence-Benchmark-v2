import numpy as np

def submatrix_with_n_numbers(matrix):
    shape = matrix.shape
    count = 0
    n = 122
    for x1 in range(shape[0]):
        for y1 in range(shape[1]):
            for x2 in range(x1, shape[0]):
                for y2 in range(y1, shape[1]):
                    submat = matrix[x1:x2 + 1, y1:y2 + 1]
                    if submat.size == n:
                        count += 1
    return count