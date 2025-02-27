import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum):
        rows, cols = matrix.shape
        submatrices = []
        for top in range(rows):
            for bottom in range(top, rows):
                for left in range(cols):
                    for right in range(left, cols):
                        submatrix_sum = np.sum(matrix[top:bottom + 1, left:right + 1])
                        if submatrix_sum == target_sum:
                            submatrices.append(matrix[top:bottom + 1, left:right + 1])
        return submatrices
    return find_submatrices(matrix, -452)