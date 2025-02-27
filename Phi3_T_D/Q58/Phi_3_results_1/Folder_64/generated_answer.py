import numpy as np

def submatrix_with_n_numbers(matrix, n=7):
    count = 0
    rows, cols = matrix.shape
    submatrices = [matrix[row:row + i, col:col + j] for row in range(rows) for col in range(cols) for i in range(1, rows - row + 1) for j in range(1, cols - col + 1)]
    for submatrix in submatrices:
        if submatrix.size == n:
            count += 1
    return count