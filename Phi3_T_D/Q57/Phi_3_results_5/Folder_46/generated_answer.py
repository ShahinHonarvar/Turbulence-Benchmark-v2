import numpy as np

def submatrix_with_particular_sum(matrix):
    valid_submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size in range(min(rows - i, cols - j), 0, -1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.sum(submatrix) == 416:
                    valid_submatrices.append(submatrix.tolist())
    return valid_submatrices