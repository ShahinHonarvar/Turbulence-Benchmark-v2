import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for size_i in range(i + 1, rows + 1):
                for size_j in range(j + 1, cols + 1):
                    submatrix = matrix[i:size_i, j:size_j]
                    if submatrix.sum() == 862:
                        result.append(submatrix.tolist())
    return result