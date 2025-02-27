import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(r, c, size):
        return np.sum(matrix[r:r + size, c:c + size])
    row, col = matrix.shape
    result = []
    for size in range(1, min(row, col) + 1):
        for r in range(row - size + 1):
            for c in range(col - size + 1):
                if submatrix_sum(r, c, size) == 3:
                    result.append(matrix[r:r + size, c:c + size])
    return result