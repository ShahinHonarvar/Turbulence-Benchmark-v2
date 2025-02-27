import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                count += 1
                k = 1
                while i + k < rows and j + k < cols and np.all(matrix[i:i + k + 1, j:j + k + 1] == 1):
                    count += 1
                    k += 1
    return count