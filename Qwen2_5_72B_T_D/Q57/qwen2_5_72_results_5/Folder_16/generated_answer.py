import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrix_sum(submatrix):
        return np.sum(submatrix)
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, cols + 1):
                    submatrix = matrix[i:x, j:y]
                    if find_submatrix_sum(submatrix) == -157:
                        result.append(submatrix)
    return result