import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(start, matrix, target, current, result):
        if start == matrix.size:
            if sum(sum(current)) == target:
                result.append(current)
            return
        new_current = np.copy(current)
        new_current[start // matrix.shape[1], start % matrix.shape[1]] = matrix[start // matrix.shape[1], start % matrix.shape[1]]
        find_submatrices(start + 1, matrix, target, new_current, result)
        find_submatrices(start + 1, matrix, target, current, result)
    result = []
    find_submatrices(0, matrix, -308, np.zeros_like(matrix), result)
    return [r for r in result if np.any(r != 0)]