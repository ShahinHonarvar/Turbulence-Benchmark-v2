import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for x in range(i, rows):
                    for y in range(j, cols):
                        submatrix = matrix[i:x + 1, j:y + 1]
                        if np.prod(submatrix.shape) == n:
                            count += 1
        return count
    return count_submatrices(matrix, 139)