import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, target_sum):
        m, n = matrix.shape
        count = 0
        for top in range(m):
            for bottom in range(top, m):
                for left in range(n):
                    for right in range(left, n):
                        submatrix_sum = np.sum(matrix[top:bottom + 1, left:right + 1])
                        if submatrix_sum == target_sum:
                            count += 1
        return count
    return count_submatrices(matrix, 139)