import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    count = 0
    for i in range(n):
        for j in range(n):
            for size in range(1, n - max(i, j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.all(submatrix == 37):
                    count += 1
    return count