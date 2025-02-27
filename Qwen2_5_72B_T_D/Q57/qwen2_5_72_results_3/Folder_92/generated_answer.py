import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, r, c, target):
        result = []
        for start_row in range(r):
            for start_col in range(c):
                for end_row in range(start_row, r):
                    for end_col in range(start_col, c):
                        sub = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(sub) == target:
                            result.append(sub)
        return result
    target = -3
    matrix = np.array(matrix)
    r, c = matrix.shape
    return submatrices(matrix, r, c, target)