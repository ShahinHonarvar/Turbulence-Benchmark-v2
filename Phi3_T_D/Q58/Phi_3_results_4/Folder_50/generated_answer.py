import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 40
    m, k = matrix.shape
    count = 0
    for i in range(m):
        for j in range(k):
            for x in range(i, m):
                for y in range(j, k):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if submatrix.size == n:
                        count += 1
    return count