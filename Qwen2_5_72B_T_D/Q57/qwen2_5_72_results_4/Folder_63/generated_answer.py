import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols, target):
        result = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        submatrix_sum = np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1])
                        if submatrix_sum == target:
                            result.append(matrix[start_row:end_row + 1, start_col:end_col + 1].tolist())
        return result
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    return submatrices(matrix, rows, cols, 64)