import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        for r in range(rows):
            for c in range(cols):
                for width in range(1, cols - c + 1):
                    for height in range(1, rows - r + 1):
                        yield matrix[r:r + height, c:c + width]
    result = []
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    for submatrix in submatrices(matrix, rows, cols):
        if np.sum(submatrix) == 66:
            result.append(submatrix)
    return result