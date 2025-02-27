import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for width in range(1, min(rows - i, cols - j) + 1):
                for height in range(1, min(rows - i, cols - j) + 1):
                    if width * height < cols - j or height < rows - i:
                        continue
                    submatrix_sum = np.sum(matrix[i:i + width, j:j + height])
                    if submatrix_sum == 616:
                        submatrices.append(matrix[i:i + width, j:j + height])
    return submatrices