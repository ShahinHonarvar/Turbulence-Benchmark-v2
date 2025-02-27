import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []

    def kadane(submatrices):
        sums = [0] * len(submatrices)
        max_sum = max_i = max_j = 0
        for i, j in submatrices:
            sums[i] += submatrices[i][j][0, 1] if i else submatrices[i][j][0]
            if sums[i] > max_sum:
                max_sum = sums[i]
                max_i = i
                max_j = j
        if max_sum == -779:
            for i, j in submatrices[max_i]:
                result.append(matrix[i:i + len(j), j:j + len(j)])
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            kadane([[[i, j]]] + [[range(a, b), range(c, d)] for a, c in ((i, j), (i + 1, j)) for b, d in ((matrix.shape[0], matrix.shape[1]), (matrix.shape[0] + 1, matrix.shape[1]))])
    return result