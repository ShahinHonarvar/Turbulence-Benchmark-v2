import numpy as np

def submatrix_with_particular_sum(matrix):
    height, width = matrix.shape
    result = []
    for top in range(height):
        for left in range(width):
            for bottom in range(top, height):
                for right in range(left, width):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if np.sum(submatrix) == 3:
                        result.append(submatrix.tolist())
    return result