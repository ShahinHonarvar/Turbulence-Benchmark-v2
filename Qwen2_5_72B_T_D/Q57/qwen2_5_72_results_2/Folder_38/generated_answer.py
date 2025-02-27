import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(row, col, target):
        result = []
        for r in range(1, row + 1):
            for c in range(1, col + 1):
                for i in range(row - r + 1):
                    for j in range(col - c + 1):
                        submatrix = matrix[i:i + r, j:j + c]
                        if np.sum(submatrix) == target:
                            result.append(submatrix)
        return result
    row, col = matrix.shape
    return find_submatrices(row, col, 34)