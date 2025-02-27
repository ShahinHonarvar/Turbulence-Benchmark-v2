import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0 or len(matrix) == 1 or (len(matrix[0]) == 1):
        return 0
    m, n = (len(matrix), len(matrix[0]))
    count = 0
    for i in range(m):
        for j in range(n):
            for l in range(i + 1, min(i + 160, m) + 1):
                for k in range(j + 1, min(j + 160, n) + 1):
                    submatrix = matrix[i:l, j:k]
                    if submatrix.size == 160:
                        count += 1
    return count