import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + 7 < rows and j + 7 < cols:
                submatrix = matrix[i:i + 8, j:j + 8]
                if submatrix.size == 8 * 8:
                    count += 1
    return count