import numpy as np

def submatrix_with_n_numbers(matrix, n=54):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == n and (submatrix == 54).all():
                        count += 1
    return count