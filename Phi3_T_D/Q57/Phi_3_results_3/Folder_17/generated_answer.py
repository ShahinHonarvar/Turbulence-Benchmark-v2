import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    total_elements = rows * cols
    target_sum = 398
    result = []
    for size in range(1, rows + 1):
        for row in range(rows - size + 1):
            for col in range(cols - size + 1):
                submatrix = matrix[row:row + size, col:col + size]
                if np.sum(submatrix) == target_sum:
                    result.append(submatrix)
    return result