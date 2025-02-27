import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_sum_correct(submatrix, target_sum=416):
        return np.sum(submatrix) == target_sum
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for width in range(1, cols - j + 1):
                for height in range(1, rows - i + 1):
                    submatrix = matrix[i:i + height, j:j + width]
                    if is_sum_correct(submatrix):
                        submatrices.append(submatrix)
    return submatrices