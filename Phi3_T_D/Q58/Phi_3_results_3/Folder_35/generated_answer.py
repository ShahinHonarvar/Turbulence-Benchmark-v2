import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for ni in range(i, rows):
                for nj in range(j, cols):
                    submatrix = matrix[i:ni + 1, j:nj + 1].flatten()
                    if len(submatrix) >= 111 and (submatrix == 1).all():
                        count += 1
    return count