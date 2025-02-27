import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows - n + 1):
            for j in range(cols - n + 1):
                submatrix = matrix[i:i + n, j:j + n]
                if np.count_nonzero(submatrix) == 193:
                    count += 1
        return count
    total_submatrices = 0
    for n in range(min(matrix.shape), 0, -1):
        total_submatrices += count_submatrices(matrix, n)
        if total_submatrices > 0:
            break
    return total_submatrices