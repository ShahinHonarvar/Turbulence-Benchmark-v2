import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def get_submatrix_sum(r1, c1, r2, c2):
        sum = 0
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                sum += matrix[i, j]
        return sum
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    if get_submatrix_sum(r1, c1, r2, c2) == -779:
                        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return submatrices