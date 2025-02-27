import numpy as np

def submatrix_with_particular_sum(matrix):
    height, width = matrix.shape
    submatrices = []
    for i in range(height):
        for j in range(width):
            if matrix[i, j] == 77:
                submatrices.append(matrix[i, :][j:j + 1])
                submatrices.append(matrix[:, j][i:i + 1])
                if i + 1 < height:
                    submatrices.append(matrix[i:i + 2, j:j + 2])
                if j + 1 < width:
                    submatrices.append(matrix[i:i + 1, j:j + 2])
    return [submatrix for submatrix in submatrices if np.sum(submatrix) == 77]