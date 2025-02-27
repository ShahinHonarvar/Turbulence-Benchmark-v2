import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(row, col, matrix, target_sum):
        sub_matrices = []
        for r in range(row + 1):
            for c in range(col + 1):
                for r_step in range(r + 1, row + 1):
                    for c_step in range(c + 1, col + 1):
                        sub = matrix[r:r_step, c:c_step]
                        if np.sum(sub) == target_sum:
                            sub_matrices.append(sub)
        return sub_matrices
    row, col = matrix.shape
    return find_submatrices(row, col, matrix, -617)