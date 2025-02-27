import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + 2 < rows and j + 2 < cols:
                sub = matrix[i:i + 3, j:j + 3]
                count += np.all(sub == 10)
    return count