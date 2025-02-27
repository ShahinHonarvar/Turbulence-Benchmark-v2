import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_all_submatrices(matrix):
        submatrices = []
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                for i_end in range(i + 1, matrix.shape[0] + 1):
                    for j_end in range(j + 1, matrix.shape[1] + 1):
                        submatrices.append(matrix[i:i_end, j:j_end])
        return submatrices
    submatrices = get_all_submatrices(matrix)
    result = [sub for sub in submatrices if np.sum(sub) == -83]
    return result