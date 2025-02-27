import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(submatrix_sum, rows, cols, matrix):
        sub_matrices = []
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        if np.sum(matrix[i:k, j:l]) == submatrix_sum:
                            sub_matrices.append(matrix[i:k, j:l])
        return sub_matrices
    rows, cols = matrix.shape
    return find_submatrices_with_sum(-394, rows, cols, matrix)