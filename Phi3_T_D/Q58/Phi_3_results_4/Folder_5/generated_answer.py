import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for x in range(rows):
        for y in range(cols):
            for h in range(1, rows - x + 1):
                for w in range(1, cols - y + 1):
                    if sum(matrix[x:x + h, y:y + w].flatten()) == 63:
                        count += 1
    return count