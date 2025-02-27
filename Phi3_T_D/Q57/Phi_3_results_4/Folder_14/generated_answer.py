import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size in range(1, rows - i + 1):
                for bottom in range(i + size, rows + 1):
                    for right in range(j + size, cols + 1):
                        submatrix = matrix[i:bottom, j:right]
                        if np.sum(submatrix) == -93:
                            submatrices.append(submatrix)
    return submatrices