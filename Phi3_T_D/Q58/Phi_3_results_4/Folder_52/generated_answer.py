import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for x in range(rows):
        for y in range(cols):
            for i in range(x, rows):
                for j in range(y, cols):
                    submatrix = matrix[x:i + 1, y:j + 1]
                    if submatrix.size == 147:
                        count += 1
    return count