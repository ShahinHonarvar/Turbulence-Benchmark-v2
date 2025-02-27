import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            for size in range(1, n - max(i, j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == 154:
                    count += 1
    return count