import numpy as np

def submatrix_with_n_numbers(matrix, n=179):
    count = 0
    rows, cols = matrix.shape
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == n:
                    count += 1
    return count