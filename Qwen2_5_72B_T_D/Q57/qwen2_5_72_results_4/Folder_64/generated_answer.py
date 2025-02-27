import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_valid_submatrix_sum(submat):
        return np.sum(submat) == -4

    def get_all_submatrices(mat):
        n, m = mat.shape
        sub_matrices = []
        for i in range(n):
            for j in range(m):
                for p in range(i + 1, n + 1):
                    for q in range(j + 1, m + 1):
                        sub_matrices.append(mat[i:p, j:q])
        return sub_matrices
    all_submatrices = get_all_submatrices(matrix)
    result_matrices = [submat for submat in all_submatrices if is_valid_submatrix_sum(submat)]
    return result_matrices