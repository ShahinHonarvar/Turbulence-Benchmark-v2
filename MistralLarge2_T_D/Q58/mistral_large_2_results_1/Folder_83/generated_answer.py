import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        if not matrix.size:
            return 0
        rows, cols = matrix.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for x in range(i + 1, rows + 1):
                    for y in range(j + 1, cols + 1):
                        submatrix = matrix[i:x, j:y]
                        if submatrix.size == n:
                            count += 1
        return count
    return count_submatrices(matrix, 47)