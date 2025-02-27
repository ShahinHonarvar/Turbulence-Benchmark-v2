import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_generator(matrix, row, col, size):
        for i in range(row + 1):
            for j in range(col + 1):
                for r in range(i + 1, row + 1):
                    for c in range(j + 1, col + 1):
                        yield matrix[i:r, j:c]
    row, col = matrix.shape
    result = []
    for submatrix in submatrix_generator(matrix, row, col, 3):
        if np.sum(submatrix) == 3:
            result.append(submatrix)
    return result