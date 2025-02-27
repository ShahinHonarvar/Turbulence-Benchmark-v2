import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def find_submatrices(r, c, current_sum, current_submatrix):
        if current_sum == 69:
            submatrices.append(current_submatrix)
            return
        if current_sum > 69 or r >= rows or c >= cols:
            return
        for i in range(r, rows):
            for j in range(c, cols):
                find_submatrices(i, j + 1, current_sum + matrix[i, j], current_submatrix + [(i, j)])
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, j, matrix[i, j], [(i, j)])
    result = []
    for submatrix in submatrices:
        unique_rows = set((row for row, col in submatrix))
        unique_cols = set((col for row, col in submatrix))
        if len(unique_rows) * len(unique_cols) == len(submatrix):
            result.append([[matrix[row, col] for col in sorted(unique_cols)] for row in sorted(unique_rows)])
    return result