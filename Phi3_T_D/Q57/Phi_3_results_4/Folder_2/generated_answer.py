import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    output = []
    for rowStart in range(rows):
        for colStart in range(cols):
            for rowSize in range(1, rows - rowStart + 1):
                for colSize in range(1, cols - colStart + 1):
                    submatrix = matrix[rowStart:rowStart + rowSize, colStart:colStart + colSize]
                    if submatrix.sum() == -863:
                        output.append(submatrix)
    return output