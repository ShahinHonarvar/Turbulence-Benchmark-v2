import numpy as np

def submatrix_with_n_numbers(matrix, n=91):
    rows, cols = matrix.shape
    if rows * cols < n:
        return 0
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == n:
                        count += 1
    return count