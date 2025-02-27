import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        submatrices = []
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                for p in range(i + 1, rows + 1):
                    for q in range(j + 1, cols + 1):
                        submatrices.append(mat[i:p, j:q])
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submat.tolist() for submat in submatrices if np.sum(submat) == -10]
    return result