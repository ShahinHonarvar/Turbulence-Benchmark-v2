import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat, r, c):
        sub_matrices = []
        for i in range(r):
            for j in range(c):
                for row_end in range(i + 1, r + 1):
                    for col_end in range(j + 1, c + 1):
                        sub_matrices.append(mat[i:row_end, j:col_end])
        return sub_matrices
    r, c = matrix.shape
    sub_matrices = get_submatrices(matrix, r, c)
    result = [sub_matrix for sub_matrix in sub_matrices if np.sum(sub_matrix) == 862]
    return result