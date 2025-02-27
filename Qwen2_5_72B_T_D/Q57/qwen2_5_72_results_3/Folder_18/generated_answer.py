import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(i, j, rows, cols, target, current, result):
        if i >= rows or j >= cols:
            return
        if target == matrix[i, j]:
            result.append(current + [(i, j)])
            return
        if target < 0:
            return
        find_submatrices(i + 1, j, rows, cols, target - matrix[i, j], current + [(i, j)], result)
        find_submatrices(i, j + 1, rows, cols, target - matrix[i, j], current + [(i, j)], result)
        find_submatrices(i + 1, j, rows, cols, target, current, result)
        find_submatrices(i, j + 1, rows, cols, target, current, result)
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            find_submatrices(i, j, rows, cols, 616, [], result)
    submatrices = []
    for indices in result:
        r1, c1 = zip(*indices)
        r1, c1 = (min(r1), min(c1))
        r2, c2 = (max(indices[0][0], indices[-1][0]), max(indices[0][1], indices[-1][1]))
        submatrices.append(matrix[r1:r2 + 1, c1:c2 + 1])
    return submatrices