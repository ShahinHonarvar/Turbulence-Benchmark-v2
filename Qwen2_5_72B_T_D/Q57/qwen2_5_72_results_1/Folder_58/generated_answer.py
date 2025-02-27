import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                for x in range(i + 1, mat.shape[0] + 1):
                    for y in range(j + 1, mat.shape[1] + 1):
                        yield mat[i:x, j:y]
    result = [submat for submat in get_submatrices(matrix) if np.sum(submat) == -137]
    return result