import numpy as np

def submatrix_with_n_numbers(matrix):
    if not matrix.size or len(matrix.shape) != 2:
        return 0
    n = 8
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if j + n <= cols and i + n <= rows:
                submatrix_elements = np.prod(matrix[i:i + n, j:j + n])
                if submatrix_elements == n ** n:
                    count += 1
    return count