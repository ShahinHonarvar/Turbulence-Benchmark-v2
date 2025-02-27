import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            sum_submatrix = 0
            for k in range(i, rows):
                for l in range(j, cols):
                    sum_submatrix += matrix[k, l]
                    if sum_submatrix == 127:
                        count += 1
    return count