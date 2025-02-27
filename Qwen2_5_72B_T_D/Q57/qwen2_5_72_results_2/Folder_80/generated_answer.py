import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix, target_sum):
        rows, cols = matrix.shape
        submatrices = []
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top + 1, rows + 1):
                    for right in range(left + 1, cols + 1):
                        sub = matrix[top:bottom, left:right]
                        if sub.sum() == target_sum:
                            submatrices.append(sub)
        return submatrices
    return get_submatrices(np.array(matrix), 245)