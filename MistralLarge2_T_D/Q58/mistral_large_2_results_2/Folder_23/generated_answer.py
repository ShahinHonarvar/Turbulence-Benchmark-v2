import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    def count_submatrices(r, c, k, sum_val):
        if sum_val == 69:
            return 1
        if r >= rows or c >= cols or k == 0:
            return 0
        total = 0
        for rr in range(r, rows):
            for cc in range(c, cols):
                submatrix = matrix[rr:rr + k, cc:cc + k]
                if submatrix.size == 69 and np.sum(submatrix) == 69:
                    total += 1
        return total + count_submatrices(r, c + 1, k, sum_val) + count_submatrices(r + 1, c, k, sum_val)
    for k in range(1, min(rows, cols) + 1):
        if k * k == 69:
            count += count_submatrices(0, 0, k, 69)
    return count