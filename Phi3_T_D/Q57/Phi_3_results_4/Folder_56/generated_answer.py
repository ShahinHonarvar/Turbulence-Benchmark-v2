import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for size in range(1, rows + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix_sum = np.sum(matrix[i:i + size, j:j + size])
                if submatrix_sum == -50:
                    submatrices.append(matrix[i:i + size, j:j + size])
    return submatrices