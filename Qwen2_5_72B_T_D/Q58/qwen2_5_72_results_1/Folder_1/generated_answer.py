import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_elements(submat, n=23):
        return sum((1 for item in submat.flatten() if item == n))
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for p in range(i + 1, m + 1):
                for q in range(j + 1, n + 1):
                    if count_elements(matrix[i:p, j:q]) == 23:
                        count += 1
    return count