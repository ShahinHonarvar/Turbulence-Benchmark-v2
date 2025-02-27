import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(r1, c1, r2, c2):
        submatrices = []
        if r1 > r2 or c1 > c2:
            return submatrices
        current_sum = np.sum(matrix[r1:r2 + 1, c1:c2 + 1])
        if current_sum == -128:
            submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1].tolist())
        if r2 + 1 < matrix.shape[0]:
            submatrices.extend(find_submatrices(r1, c1, r2 + 1, c2))
        if c2 + 1 < matrix.shape[1]:
            submatrices.extend(find_submatrices(r1, c1, r2, c2 + 1))
        if r1 + 1 < matrix.shape[0]:
            submatrices.extend(find_submatrices(r1 + 1, c1, r2, c2))
        if c1 + 1 < matrix.shape[1]:
            submatrices.extend(find_submatrices(r1, c1 + 1, r2, c2))
        return submatrices
    return find_submatrices(0, 0, 0, 0)