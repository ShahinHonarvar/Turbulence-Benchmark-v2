import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum):
        rows, cols = matrix.shape
        submatrices = []
        for r_start in range(rows):
            for c_start in range(cols):
                for r_end in range(r_start, rows):
                    for c_end in range(c_start, cols):
                        submatrix = matrix[r_start:r_end + 1, c_start:c_end + 1]
                        if np.sum(submatrix) == target_sum:
                            submatrices.append(submatrix)
        return submatrices
    return find_submatrices(matrix, 17)