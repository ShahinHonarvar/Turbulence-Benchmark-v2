import numpy as np

def submatrix_with_n_numbers(matrix):
    count, n = (0, 131)
    rows, cols = matrix.shape
    for rowStart in range(rows):
        for colStart in range(cols):
            for rowEnd in range(rowStart, rows):
                for colEnd in range(colStart, cols):
                    submatrix = matrix[rowStart:rowEnd + 1, colStart:colEnd + 1]
                    if submatrix.size == n:
                        count += 1
    return count