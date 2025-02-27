import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_valid_submatrix(submat):
        return np.sum(submat) == 901
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    submat = matrix[i:x + 1, j:y + 1]
                    if is_valid_submatrix(submat):
                        result.append(submat)
    return result