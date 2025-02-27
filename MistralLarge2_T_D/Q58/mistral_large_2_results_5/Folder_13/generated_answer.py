import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        rows, cols = matrix.shape
        if n > rows * cols:
            return 0
        submatrix_count = 0
        for r in range(rows):
            for c in range(cols):
                for r_end in range(r, rows):
                    for c_end in range(c, cols):
                        submatrix = matrix[r:r_end + 1, c:c_end + 1]
                        if submatrix.size == n:
                            submatrix_count += 1
        return submatrix_count
    return count_submatrices(matrix, 175)