import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        for size in range(1, len(mat) + 1):
            for i in range(len(mat) - size + 1):
                for j in range(len(mat[0]) - size + 1):
                    yield mat[i:i + size, j:j + size]
    result = []
    for submat in get_submatrices(matrix):
        if np.sum(submat) == -83:
            result.append(submat)
    return result