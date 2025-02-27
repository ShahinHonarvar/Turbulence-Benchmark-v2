import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(start_row, start_col, current_sum, current_submatrix):
        if current_sum == 901:
            result.append(np.array(current_submatrix))
            return
        if current_sum > 901 or start_row >= rows or start_col >= cols:
            return
        for i in range(start_row, rows):
            for j in range(start_col if i == start_row else 0, cols):
                current_sum += matrix[i][j]
                current_submatrix.append(matrix[i][j])
                find_submatrices(i, j + 1, current_sum, current_submatrix)
                current_submatrix.pop()
                current_sum -= matrix[i][j]
    rows, cols = matrix.shape
    result = []
    find_submatrices(0, 0, 0, [])
    return result