import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, result):
        for size in range(1, min(matrix.shape) + 1):
            for i in range(matrix.shape[0] - size + 1):
                for j in range(matrix.shape[1] - size + 1):
                    submatrix = matrix[i:i + size, j:j + size]
                    if np.sum(submatrix) == target_sum:
                        result.append(submatrix)
    result = []
    find_submatrices(np.array(matrix), 1, result)
    return result