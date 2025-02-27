import numpy as np

def submatrix_with_n_numbers(matrix, n=33):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 5 < rows and j + 5 < cols:
                submatrix = matrix[i:i + 6, j:j + 6]
                if np.sum(submatrix) == n * 6:
                    count += 1
    return count