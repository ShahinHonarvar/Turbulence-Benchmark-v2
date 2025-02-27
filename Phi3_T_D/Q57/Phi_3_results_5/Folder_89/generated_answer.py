import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        rows, cols = matrix.shape
        for r1 in range(rows):
            for r2 in range(r1, rows):
                for c1 in range(cols):
                    for c2 in range(c1, cols):
                        yield (slice(r1, r2 + 1), slice(c1, c2 + 1))

    def sum_of_submatrix(matrix, rows_slice, cols_slice):
        return np.sum(matrix[rows_slice, cols_slice])
    all_subs = list(all_submatrices(matrix))
    target_subs = [sub for sub in all_subs if sum_of_submatrix(matrix, *sub) == 80]
    return target_subs