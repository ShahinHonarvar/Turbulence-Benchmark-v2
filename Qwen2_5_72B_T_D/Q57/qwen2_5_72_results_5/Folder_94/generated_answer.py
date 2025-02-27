import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        submatrices = []
        for i in range(rows):
            for j in range(cols):
                for p in range(i + 1, rows + 1):
                    for q in range(j + 1, cols + 1):
                        submatrices.append(mat[i:p, j:q])
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submat.tolist() for submat in submatrices if np.sum(submat) == 92]
    return result