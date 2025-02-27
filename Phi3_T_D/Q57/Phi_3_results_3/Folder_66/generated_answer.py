import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                submat = matrix[i:i + size, j:j + size]
                if submat.sum() == 99:
                    result.append(submat)
    return result