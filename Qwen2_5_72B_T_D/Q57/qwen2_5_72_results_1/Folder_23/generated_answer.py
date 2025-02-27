import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(start, matrix, target, current, result):
        if start >= matrix.size:
            return
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                for row_end in range(i + 1, rows + 1):
                    for col_end in range(j + 1, cols + 1):
                        submatrix = matrix[i:row_end, j:col_end]
                        if np.sum(submatrix) == target:
                            result.append(submatrix.tolist())
    result = []
    find_submatrices(0, matrix, 59, [], result)
    return result