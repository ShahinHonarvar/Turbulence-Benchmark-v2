import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    for left in range(ncols):
        for right in range(left, ncols):
            submatrix_sum = 0
            for top in range(nrows):
                for bottom in range(top, nrows):
                    submatrix_sum = np.sum(matrix[top:bottom + 1, left:right + 1])
                    if submatrix_sum == -617:
                        result.append(matrix[top:bottom + 1, left:right + 1])
    return result