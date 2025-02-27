import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_value(mat, value, count):
        rows, cols = mat.shape
        total = 0
        for i in range(rows):
            for j in range(cols):
                if mat[i, j] == value:
                    total += 1
                    if total == count:
                        return 1
        return 0 if total != count else 1
    rows, cols = matrix.shape
    result = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(1, rows - i + 1):
                for c in range(1, cols - j + 1):
                    submat = matrix[i:i + r, j:j + c]
                    result += count_submatrices_with_value(submat, 88, 88)
    return result