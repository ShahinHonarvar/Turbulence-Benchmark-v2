import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top + 1, rows + 1):
                for right in range(left + 1, cols + 1):
                    submatrix_sum = np.sum(matrix[top:bottom, left:right])
                    if submatrix_sum == -59:
                        result.append(matrix[top:bottom, left:right])
    return result