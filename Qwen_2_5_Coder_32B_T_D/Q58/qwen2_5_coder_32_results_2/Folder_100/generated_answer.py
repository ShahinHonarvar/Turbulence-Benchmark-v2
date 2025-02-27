import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    n = 10
    for i in range(m - int(np.sqrt(n)) + 1):
        for j in range(n - int(np.sqrt(n)) + 1):
            submatrix = matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))]
            if submatrix.size == n:
                count += 1
    return count