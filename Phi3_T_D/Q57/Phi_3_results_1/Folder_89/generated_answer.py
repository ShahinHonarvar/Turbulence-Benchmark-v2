import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        m, n = matrix.shape
        sub_matrices = []
        for r1 in range(m):
            for c1 in range(n):
                for r2 in range(r1, m):
                    for c2 in range(c1, n):
                        sub_matrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
        return sub_matrices

    def sums_to_80(sub_matrix):
        return np.sum(sub_matrix) == 80
    sub_matrices = all_submatrices(matrix)
    return [sub_matrix.tolist() for sub_matrix in sub_matrices if sums_to_80(sub_matrix)]