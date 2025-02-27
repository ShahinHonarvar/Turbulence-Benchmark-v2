import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(matrix):
        rows, cols = matrix.shape
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row + 1, rows + 1):
                    for end_col in range(start_col + 1, cols + 1):
                        yield matrix[start_row:end_row, start_col:end_col]
    target_sum = -26
    submatrices = list(generate_submatrices(matrix))
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == target_sum]
    return result