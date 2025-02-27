import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []

    def find_submatrix(start_row, start_col):
        for row in range(start_row, m):
            for col in range(start_col, n):
                if matrix[row, col] == 416:
                    submatrices.append(matrix[row:row + 1, col:col + 1])
                for r in range(row + 1, m):
                    for c in range(col + 1, n):
                        submatrix = matrix[row:r + 1, col:c + 1]
                        if np.sum(submatrix) == 416:
                            submatrices.append(submatrix)
    for i in range(m):
        for j in range(n):
            find_submatrix(i, j)
    return submatrices