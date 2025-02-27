import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 91

    def count_submatrices_with_sum(matrix, n):
        if n == 0:
            return 0
        count = 0
        rows, cols = matrix.shape
        for top in range(rows):
            for bottom in range(top, rows):
                for left in range(cols):
                    for right in range(left, cols):
                        if (bottom - top + 1) * (right - left + 1) == n:
                            submatrix = matrix[top:bottom + 1, left:right + 1]
                            if np.sum(submatrix) == n:
                                count += 1
        return count
    return count_submatrices_with_sum(matrix, n)