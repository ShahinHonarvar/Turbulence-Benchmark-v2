import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 99
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 2):
        for j in range(cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if (submatrix == target).sum() == 99:
                count += 1
    return count