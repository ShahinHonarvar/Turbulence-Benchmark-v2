import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 40
    for i in range(rows):
        for j in range(cols):
            k = 0
            submatrix_sum = 0
            for di in range(rows - i):
                for dj in range(cols - j):
                    submatrix_sum += 1
                    k += 1
                    if k == n:
                        count += 1
    return count