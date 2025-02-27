import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_8(matrix, row, col):
        count = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if matrix[i][j] == 8:
                    count += 1
        return count == 8
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            if count_submatrices_with_8(matrix, i, j):
                count += 1
    return count