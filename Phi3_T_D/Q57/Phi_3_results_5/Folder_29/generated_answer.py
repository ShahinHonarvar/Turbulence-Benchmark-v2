import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy array')
    submatrices = []
    rows, cols = matrix.shape
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    current_submatrix = matrix[top:bottom + 1, left:right + 1]
                    if current_submatrix.sum() == 84:
                        submatrices.append(current_submatrix)
    return submatrices