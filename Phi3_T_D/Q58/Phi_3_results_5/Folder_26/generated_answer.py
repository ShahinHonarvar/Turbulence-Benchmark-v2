import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for x in range(rows):
        for y in range(cols):
            for size in range(1, min(rows - x, cols - y) + 1):
                submatrix = matrix[x:x + size, y:y + size]
                if submatrix.size == 115:
                    count += 1
    return count