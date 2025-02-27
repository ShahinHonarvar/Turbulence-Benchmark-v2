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
    target_sum = -82
    result = []
    rows, cols = matrix.shape
    all_sub_matrices = submatrices(matrix, rows, cols)
    for sub_matrix in all_sub_matrices:
        if np.sum(sub_matrix) == target_sum:
            result.append(sub_matrix)
    return result