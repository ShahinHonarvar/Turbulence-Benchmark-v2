import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(m):
        submatrices = []
        for start_row in range(m.shape[0]):
            for start_col in range(m.shape[1]):
                for end_row in range(start_row + 1, m.shape[0] + 1):
                    for end_col in range(start_col + 1, m.shape[1] + 1):
                        sub = m[start_row:end_row, start_col:end_col]
                        submatrices.append(sub)
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [sub.tolist() for sub in submatrices if np.sum(sub) == -59]
    return result