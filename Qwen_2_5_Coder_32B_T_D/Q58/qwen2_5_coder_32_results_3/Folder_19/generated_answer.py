import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    h, w = matrix.shape
    for i in range(h - 3):
        for j in range(w - 5):
            submatrix = matrix[i:i + 4, j:j + 5]
            if submatrix.size == 17:
                count += 1
    return count