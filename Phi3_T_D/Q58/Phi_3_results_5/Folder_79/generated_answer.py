import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 60
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if submatrix.size == n:
                        count += 1
    return count