import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(top, left, bottom, right):
        return (bottom - top + 1) * (right - left + 1)
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if count_submatrices(i, j, k, l) == 180:
                        count += 1
    return count