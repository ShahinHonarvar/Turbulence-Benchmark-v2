import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        rows, cols = matrix.shape
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top, rows):
                    for right in range(left, cols):
                        yield matrix[top:bottom + 1, left:right + 1]

    def has_sum(matrix, target_sum):
        return np.sum(matrix) == target_sum
    submatrices = list(all_submatrices(matrix))
    return [submatrix for submatrix in submatrices if has_sum(submatrix, -811)]