import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, n):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                if (i + 1) * (j + 1) == n:
                    count += 1
                elif (rows - i) * (cols - j) >= n:
                    submatrix = matrix[i:rows, j:cols]
                    if submatrix.size == n:
                        count += 1
        return count
    return count_submatrices_of_size(matrix, 57)