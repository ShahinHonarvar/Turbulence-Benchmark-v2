import numpy as np

def submatrix_with_n_numbers(matrix):
    counter = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submat = matrix[i:k + 1, j:l + 1]
                    if submat.size == 139:
                        counter += 1
    return counter