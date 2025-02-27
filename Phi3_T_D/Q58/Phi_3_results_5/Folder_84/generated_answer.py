import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for n in range(1, min(rows, cols) + 1):
        for i in range(rows - n + 1):
            for j in range(cols - n + 1):
                if (matrix[i:i + n, j:j + n] == 127).all():
                    count += 1
    return count