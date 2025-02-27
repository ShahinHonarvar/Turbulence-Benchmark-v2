import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix, target_sum):
        rows, cols = matrix.shape
        submatrices = []
        for start_r in range(rows):
            for start_c in range(cols):
                for end_r in range(start_r, rows):
                    for end_c in range(start_c, cols):
                        submatrix = matrix[start_r:end_r + 1, start_c:end_c + 1]
                        if np.sum(submatrix) == target_sum:
                            submatrices.append(submatrix)
        return submatrices
    return get_submatrices(matrix, 398)