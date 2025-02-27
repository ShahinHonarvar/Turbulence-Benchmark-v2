import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def find_submatrices(start_row, start_col, target_sum):
        for r1 in range(start_row, rows):
            for c1 in range(start_col, cols):
                for r2 in range(r1, rows):
                    for c2 in range(c1, cols):
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix)
    find_submatrices(0, 0, -336)
    return result