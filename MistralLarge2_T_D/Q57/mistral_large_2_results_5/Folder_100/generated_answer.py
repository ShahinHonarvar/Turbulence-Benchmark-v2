import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def find_submatrices(start_row, start_col):
        for r in range(start_row, rows):
            for c in range(start_col, cols):
                if matrix[r, c] == 28:
                    result.append(matrix[r:r + 1, c:c + 1])
                for i in range(r + 1, rows):
                    for j in range(c + 1, cols):
                        submatrix = matrix[r:i + 1, c:j + 1]
                        if np.sum(submatrix) == 28:
                            result.append(submatrix)
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, j)
    return result