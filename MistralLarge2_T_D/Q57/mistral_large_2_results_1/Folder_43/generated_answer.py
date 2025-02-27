import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def find_submatrices(start_row, start_col, target_sum):
        if target_sum == 0:
            submatrices.append(matrix[start_row:, start_col:])
            return
        if start_row >= rows or start_col >= cols:
            return
        for r in range(start_row, rows):
            for c in range(start_col, cols):
                current_sum = np.sum(matrix[start_row:r + 1, start_col:c + 1])
                if current_sum == target_sum:
                    submatrices.append(matrix[start_row:r + 1, start_col:c + 1])
                elif current_sum < target_sum:
                    find_submatrices(r + 1, c + 1, target_sum - current_sum)
    find_submatrices(0, 0, -81)
    return submatrices