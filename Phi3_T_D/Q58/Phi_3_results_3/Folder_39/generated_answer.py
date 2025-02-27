import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for n in range(59, rows - i + 1):
                for m in range(59, cols - j + 1):
                    submatrix = matrix[i:i + n, j:j + m]
                    if submatrix.size == 59:
                        count += 1
    return count