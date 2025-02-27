import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        sub_matrices = []
        for i in range(rows):
            for j in range(cols):
                for row_end in range(i + 1, rows + 1):
                    for col_end in range(j + 1, cols + 1):
                        sub_matrices.append(matrix[i:row_end, j:col_end])
        return sub_matrices
    target_sum = -617
    sub_matrices = submatrices(matrix, matrix.shape[0], matrix.shape[1])
    result = [sub_matrix for sub_matrix in sub_matrices if np.sum(sub_matrix) == target_sum]
    return result