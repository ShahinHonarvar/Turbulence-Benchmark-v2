import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top + 1, rows + 1):
                    for right in range(left + 1, cols + 1):
                        submatrices.append(matrix[top:bottom, left:right])
        return submatrices

    def sum_of_submatrix(submatrix):
        return np.sum(submatrix)
    target_sum = -308
    submatrices = all_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if sum_of_submatrix(submatrix) == target_sum]
    return result