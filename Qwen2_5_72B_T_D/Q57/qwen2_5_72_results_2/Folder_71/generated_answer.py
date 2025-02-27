import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(start_row, start_col, target_sum, current_sum, current_submatrix, result):
        rows, cols = matrix.shape
        if current_sum == target_sum:
            result.append(current_submatrix.copy())
            return
        if current_sum > target_sum:
            return
        for row in range(start_row, rows):
            for col in range(start_col, cols):
                element = matrix[row, col]
                current_submatrix[row, col] = element
                find_submatrices(row, col + 1, target_sum, current_sum + element, current_submatrix, result)
                current_submatrix[row, col] = 0
    target_sum = 69
    rows, cols = matrix.shape
    result = []
    for row in range(rows):
        for col in range(cols):
            current_submatrix = np.zeros_like(matrix)
            find_submatrices(row, col, target_sum, 0, current_submatrix, result)
    return [submatrix for submatrix in result if np.sum(submatrix) == target_sum]