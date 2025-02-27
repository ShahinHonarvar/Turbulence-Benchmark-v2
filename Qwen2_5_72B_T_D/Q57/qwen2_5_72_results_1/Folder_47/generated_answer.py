import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(m, target):
        R, C = m.shape
        submatrices = []
        for start_row in range(R):
            for start_col in range(C):
                for end_row in range(start_row + 1, R + 1):
                    for end_col in range(start_col + 1, C + 1):
                        if np.sum(m[start_row:end_row, start_col:end_col]) == target:
                            submatrices.append(m[start_row:end_row, start_col:end_col].tolist())
        return submatrices
    return submatrix_sum(matrix, 27)