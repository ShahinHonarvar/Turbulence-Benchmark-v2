import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_two_integers(m, n, matrix):
        count = 0
        for i in range(m):
            for j in range(n):
                for k in range(i + 1, m):
                    for l in range(j + 1, n):
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if submatrix.size == 2:
                            count += 1
        return count
    m, n = matrix.shape
    return count_submatrices_with_two_integers(m, n, matrix)