import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    submatrix = np.array([row[left:right + 1] for row in matrix[top:bottom + 1]])
                    if submatrix.sum() == -59:
                        submatrices.append(submatrix)
    return submatrices