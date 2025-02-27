import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n):
        for j in range(m):
            for Y in range(i + 1, n + 1):
                for X in range(j + 1, m + 1):
                    submatrix = matrix[i:Y, j:X]
                    if submatrix.size == 39:
                        count += 1
    return count