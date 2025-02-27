import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 99
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                if i + 9 < rows and j + 9 < cols:
                    if np.all(matrix[i:i + 10, j:j + 10] == target):
                        count += 1
    return count