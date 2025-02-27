import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(m, target):
        rows, cols = m.shape
        result = []
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row + 1, rows + 1):
                    for end_col in range(start_col + 1, cols + 1):
                        submatrix = m[start_row:end_row, start_col:end_col]
                        if np.sum(submatrix) == target:
                            result.append(submatrix)
        return result
    return find_submatrices_with_sum(matrix, 100)