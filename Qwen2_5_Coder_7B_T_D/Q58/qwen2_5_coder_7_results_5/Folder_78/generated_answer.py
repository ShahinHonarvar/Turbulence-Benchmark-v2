import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 91 <= rows and j + 91 <= cols:
                submatrix = matrix[i:i + 91, j:j + 91]
                if submatrix.size == 91:
                    count += 1
    return count