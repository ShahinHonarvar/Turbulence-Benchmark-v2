import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submat):
        return np.sum(submat) == -137

    def find_submatrices(mat):
        rows, cols = mat.shape
        result = []
        for i in range(rows):
            for j in range(cols):
                for p in range(i + 1, rows + 1):
                    for q in range(j + 1, cols + 1):
                        submat = mat[i:p, j:q]
                        if submatrix_sum(submat):
                            result.append(submat)
        return result
    return find_submatrices(matrix)