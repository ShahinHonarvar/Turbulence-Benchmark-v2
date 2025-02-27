import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum):
        rows, cols = matrix.shape
        submatrices = []
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top + 1, rows + 1):
                    for right in range(left + 1, cols + 1):
                        submatrix = matrix[top:bottom, left:right]
                        if np.sum(submatrix) == target_sum:
                            submatrices.append(submatrix)
        return submatrices
    return find_submatrices(matrix, -47)