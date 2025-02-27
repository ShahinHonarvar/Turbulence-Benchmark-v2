import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for x in range(rows):
        for y in range(cols):
            for subrows in range(1, rows - x + 1):
                if y + subrows <= cols:
                    submatrix = matrix[x:x + subrows, y:y + subrows]
                    if submatrix.size == 37:
                        count += 1
    return count