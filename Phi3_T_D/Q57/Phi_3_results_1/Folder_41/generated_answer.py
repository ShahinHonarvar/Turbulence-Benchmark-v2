import numpy as np

def submatrix_with_particular_sum(matrix):
    size = len(matrix)
    result = []
    for top in range(size):
        for left in range(size):
            for bottom in range(top + 1, size + 1):
                for right in range(left + 1, size + 1):
                    submatrix = matrix[top:bottom, left:right]
                    if np.sum(submatrix) == -26:
                        result.append(submatrix)
    return result