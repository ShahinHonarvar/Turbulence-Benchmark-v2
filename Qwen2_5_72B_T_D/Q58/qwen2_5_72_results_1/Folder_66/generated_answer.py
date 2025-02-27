import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target = 42
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target:
                if i + 1 < rows and j + 1 < cols:
                    if matrix[i, j + 1] == target and matrix[i + 1, j] == target and (matrix[i + 1, j + 1] == target):
                        count += 1
    return count