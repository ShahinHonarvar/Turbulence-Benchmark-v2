import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for k in range(i, rows):
                    for l in range(j, cols):
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if submatrix.size == n:
                            count += 1
        return count
    return count_submatrices(matrix, 59)