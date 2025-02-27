import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 73
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if submatrix.size == n:
                count += 1
    return count