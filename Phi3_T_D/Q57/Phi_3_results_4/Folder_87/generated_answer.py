import numpy as np

def get_submatrices(matrix, rows, cols, numRows, numCols):
    for i in range(rows - numRows + 1):
        for j in range(cols - numCols + 1):
            yield matrix[i:i + numRows, j:j + numCols]

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for numRows in range(1, rows + 1):
        for numCols in range(1, cols + 1):
            for submatrix in get_submatrices(matrix, rows, cols, numRows, numCols):
                if submatrix.sum() == 35:
                    result.append(submatrix)
    return result