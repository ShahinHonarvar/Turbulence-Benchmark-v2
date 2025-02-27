import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(matrix, target_sum):
        row, col = matrix.shape
        submatrices = []
        for r_start in range(row):
            for r_end in range(r_start, row):
                for c_start in range(col):
                    for c_end in range(c_start, col):
                        submatrix = matrix[r_start:r_end + 1, c_start:c_end + 1]
                        if np.sum(submatrix) == target_sum:
                            submatrices.append(submatrix)
        return submatrices
    return find_submatrices_with_sum(matrix, 28)