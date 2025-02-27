import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 15
    submatrices = []
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            submatrices.append(submatrix)
    count = 0
    for submatrix in submatrices:
        if submatrix.shape == (n, n):
            count += 1
    return count