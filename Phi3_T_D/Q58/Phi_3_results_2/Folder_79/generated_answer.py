import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for rowStart in range(rows):
        for colStart in range(cols):
            for rowLen in range(1, rows - rowStart + 1):
                for colLen in range(1, cols - colStart + 1):
                    submatrix = matrix[rowStart:rowStart + rowLen, colStart:colStart + colLen]
                    if np.count_nonzero(submatrix == 60) == submatrix.size:
                        count += 1
    return count