import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                count += 1
                for k in range(i + 1, rows):
                    if np.all(matrix[i:k + 1, j:j + 1] == 1):
                        count += 1
    return count