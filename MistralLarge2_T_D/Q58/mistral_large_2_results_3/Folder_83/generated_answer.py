import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for r in range(rows):
            for c in range(cols):
                for rr in range(r, rows):
                    for cc in range(c, cols):
                        submatrix = matrix[r:rr + 1, c:cc + 1]
                        if np.prod(submatrix.shape) == n:
                            count += 1
        return count
    return count_submatrices(matrix, 47)