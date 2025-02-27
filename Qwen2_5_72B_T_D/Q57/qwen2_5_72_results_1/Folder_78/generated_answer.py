import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        sub_matrices = []
        for i in range(rows):
            for j in range(cols):
                for x in range(i + 1, rows + 1):
                    for y in range(j + 1, cols + 1):
                        sub_matrices.append(mat[i:x, j:y])
        return sub_matrices
    submatrices = get_submatrices(matrix)
    result = [submat.tolist() for submat in submatrices if np.sum(submat) == 17]
    return result