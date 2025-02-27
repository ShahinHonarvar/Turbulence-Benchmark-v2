import numpy as np

def submatrix_with_particular_sum(matrix):

    def contains_sum(matrix, target_sum):
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        submatrix = matrix[i:k, j:l]
                        if np.sum(submatrix) == target_sum:
                            return submatrix.tolist()
        return []
    return contains_sum(matrix, 77)