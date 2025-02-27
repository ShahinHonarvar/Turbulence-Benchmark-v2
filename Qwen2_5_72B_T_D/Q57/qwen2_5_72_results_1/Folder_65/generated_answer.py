import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_sum_78(submat):
        return np.sum(submat) == 78
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for width in range(1, cols - j + 1):
                for height in range(1, rows - i + 1):
                    submat = matrix[i:i + height, j:j + width]
                    if is_sum_78(submat):
                        result.append(submat)
    return result