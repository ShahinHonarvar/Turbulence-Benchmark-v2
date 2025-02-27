import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrix_sum(row, col, size):
        submatrix_sum = np.sum(matrix[row:row + size, col:col + size])
        if submatrix_sum == 95:
            submatrices.append(matrix[row:row + size, col:col + size].tolist())
    submatrices = []
    rows, cols = matrix.shape
    for size in range(1, max(rows, cols) + 1):
        for row in range(rows - size + 1):
            for col in range(cols - size + 1):
                find_submatrix_sum(row, col, size)
    return submatrices