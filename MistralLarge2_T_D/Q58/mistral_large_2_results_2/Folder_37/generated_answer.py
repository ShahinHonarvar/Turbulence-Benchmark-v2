import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 64
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 7 < rows and j + 7 < cols:
                submatrix = matrix[i:i + 8, j:j + 8]
                if np.size(submatrix) == n:
                    count += 1
    return count