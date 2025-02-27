import numpy as np

def find_submatrices(matrix):
    matrix = np.array(matrix)
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for subrows in range(1, rows - i + 1):
                for subcols in range(1, cols - j + 1):
                    submatrix = matrix[i:i + subrows, j:j + subcols]
                    submatrix_sum = np.sum(submatrix)
                    if submatrix_sum == -617:
                        result.append(submatrix)
    return result