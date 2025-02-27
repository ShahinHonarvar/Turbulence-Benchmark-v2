import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 67
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for b in range(i, rows):
                for a in range(j, cols):
                    submat = matrix[i:b + 1, j:a + 1]
                    if submat.shape[0] * submat.shape[1] == n:
                        count += 1
    return count