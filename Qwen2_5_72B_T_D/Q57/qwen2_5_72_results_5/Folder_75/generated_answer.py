import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submat, target):
        return np.sum(submat) == target
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for width in range(1, cols - j + 1):
                for height in range(1, rows - i + 1):
                    submat = matrix[i:i + height, j:j + width]
                    if submatrix_sum(submat, 16):
                        result.append(submat)
    return result