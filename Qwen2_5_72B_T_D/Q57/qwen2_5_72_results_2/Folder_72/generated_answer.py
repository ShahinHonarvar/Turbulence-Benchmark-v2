import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(i, j, rows, cols, target, current_sum, current_submatrix, result):
        if current_sum == target:
            result.append(np.array(current_submatrix))
            return
        if i >= rows or j >= cols or current_sum > target:
            return
        for di, dj in [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1)]:
            ni, nj = (i + di, j + dj)
            if 0 <= ni < rows and 0 <= nj < cols:
                new_submatrix = current_submatrix + [(ni, nj)]
                find_submatrices(ni, nj, rows, cols, target, current_sum + matrix[ni, nj], new_submatrix, result)
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, j, rows, cols, 41, matrix[i, j], [(i, j)], result)
    unique_submatrices = []
    for indices in result:
        submatrix = matrix[np.array([x[0] for x in indices]), np.array([x[1] for x in indices])]
        if not any((np.array_equal(submatrix, sm) for sm in unique_submatrices)):
            unique_submatrices.append(submatrix)
    return unique_submatrices